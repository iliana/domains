from django.conf import settings
import decimal
import django_keycloak_auth.clients
import requests
from . import apps


def _mul(value, unit):
    if unit == 1:
        return decimal.Decimal(value) / decimal.Decimal(12)
    else:
        return decimal.Decimal(value)


class SimplePrice:
    def __init__(self, price: int, periods=None, restore=0, renewal=None, transfer=0):
        self.price = price
        self._renewal = renewal if renewal else price
        self._restore = restore
        self._transfer = transfer
        self.periods = list(periods) if periods else list(map(lambda i: apps.epp_api.Period(
            unit=0,
            value=i
        ), range(1, 11)))

    @property
    def currency(self):
        return "GBP"

    def representative_registration(self):
        return decimal.Decimal(self.price) / decimal.Decimal(100)

    def representative_renewal(self):
        return decimal.Decimal(self._renewal) / decimal.Decimal(100) if self._renewal is not None else None

    def representative_restore(self):
        return decimal.Decimal(self._restore) / decimal.Decimal(100) if self._restore is not None else None

    def representative_transfer(self):
        return decimal.Decimal(self._transfer) / decimal.Decimal(100) if self._transfer is not None else None

    def registration(self, _sld: str, value=1, unit=0):
        if apps.epp_api.Period(
            unit=unit,
            value=value
        ) not in self.periods:
            return None
        return (decimal.Decimal(self.price) / decimal.Decimal(100)) * _mul(value, unit)

    def renewal(self, _sld: str, value=1, unit=0):
        if apps.epp_api.Period(
                unit=unit,
                value=value
        ) not in self.periods:
            return None
        return (decimal.Decimal(self._renewal) / decimal.Decimal(100)) * _mul(value, unit)

    def restore(self, _sld: str):
        return decimal.Decimal(self._restore) / decimal.Decimal(100)

    def transfer(self, _sld: str, value=1, unit=0):
        if apps.epp_api.Period(
                unit=unit,
                value=value
        ) not in self.periods:
            return None
        return (decimal.Decimal(self._transfer) / decimal.Decimal(100)) * _mul(value, unit)


class LengthPrice:
    def __init__(self, standard_price: int, lengths, periods=None, restore=0, renewal=None, transfer=0):
        self.standard_price = standard_price
        self.lengths = lengths
        self._renewal = renewal if renewal else standard_price
        self._restore = restore
        self._transfer = transfer
        self.periods = periods if periods else list(map(lambda i: apps.epp_api.Period(
            unit=0,
            value=i
        ), range(1, 11)))

    @property
    def currency(self):
        return "GBP"

    def representative_registration(self):
        return decimal.Decimal(self.standard_price) / decimal.Decimal(100)

    def representative_renewal(self):
        return decimal.Decimal(self._renewal) / decimal.Decimal(100) if self._renewal is not None else None

    def representative_restore(self):
        return decimal.Decimal(self._restore) / decimal.Decimal(100) if self._restore is not None else None

    def representative_transfer(self):
        return decimal.Decimal(self._transfer) / decimal.Decimal(100) if self._transfer is not None else None

    def registration(self, sld: str, value=1, unit=0):
        if apps.epp_api.Period(
                unit=unit,
                value=value
        ) not in self.periods:
            return None
        return (decimal.Decimal(
            self.lengths.get(len(sld), self.standard_price)
        ) / decimal.Decimal(100)) * _mul(value, unit)

    def renewal(self, _sld: str, value=1, unit=0):
        if apps.epp_api.Period(
                unit=unit,
                value=value
        ) not in self.periods:
            return None
        return (decimal.Decimal(self._renewal) / decimal.Decimal(100)) * _mul(value, unit)

    def restore(self, _sld: str):
        return decimal.Decimal(self._restore) / decimal.Decimal(100)

    def transfer(self, _sld: str, value=1, unit=0):
        if apps.epp_api.Period(
                unit=unit,
                value=value
        ) not in self.periods:
            return None
        return (decimal.Decimal(self._transfer) / decimal.Decimal(100)) * _mul(value, unit)


class MarkupPrice:
    def __init__(self, price: int, markup: decimal.Decimal, tld: str, currency: str, periods=None, restore=0, renewal=None, transfer=0):
        self.price = price
        self._tld = tld
        self._markup = markup
        self._currency = currency
        self._renewal = renewal if renewal else price
        self._restore = restore
        self._transfer = transfer
        self.periods = list(periods) if periods else list(map(lambda i: apps.epp_api.Period(
            unit=0,
            value=i
        ), range(1, 11)))

    @property
    def currency(self):
        return self._currency

    def representative_registration(self):
        return decimal.Decimal(self.price) / decimal.Decimal(100)

    def representative_renewal(self):
        return decimal.Decimal(self._renewal) / decimal.Decimal(100) if self._renewal is not None else None

    def representative_restore(self):
        return decimal.Decimal(self._restore) / decimal.Decimal(100) if self._restore is not None else None

    def representative_transfer(self):
        return decimal.Decimal(self._transfer) / decimal.Decimal(100) if self._transfer is not None else None

    def _get_fee(self, sld, value, unit, command):
        domain = f"{sld}.{self._tld}"
        if unit is not None:
            period = apps.epp_api.Period(
                unit=unit,
                value=value
            )
            if period not in self.periods:
                return None

        resp = apps.epp_client.stub.DomainCheck(apps.epp_api.domain_pb2.DomainCheckRequest(
            name=domain,
            fee_check=apps.epp_api.fee_pb2.FeeCheck(
                currency=apps.epp_api.StringValue(value=self._currency),
                commands=[apps.epp_api.fee_pb2.FeeCommand(
                    command=command,
                    period=period.to_pb() if unit is not None else None
                )]
            )
        ))
        if not resp.HasField("fee_check"):
            return None
        if not resp.fee_check.available:
            return None
        command = resp.fee_check.commands[0]
        total_fee = decimal.Decimal(0)
        for fee in command.fees:
            total_fee += decimal.Decimal(fee.value)
        for credit in command.credits:
            total_fee += decimal.Decimal(credit.value)

        final_fee = total_fee * self._markup

        client_token = django_keycloak_auth.clients.get_access_token()
        r = requests.post(
            f"{settings.BILLING_URL}/convert_currency/", json={
                "amount": str(final_fee),
                "from": command.currency,
                "to": "GBP",
            }, headers={
                "Authorization": f"Bearer {client_token}"
            }
        )
        r_data = r.json()
        return decimal.Decimal(r_data.get("amount"))

    def registration(self, sld: str, value=1, unit=0):
        return self._get_fee(sld, value, unit, apps.epp_api.fee_pb2.Create)

    def renewal(self, sld: str, value=1, unit=0):
        return self._get_fee(sld, value, unit, apps.epp_api.fee_pb2.Renew)

    def restore(self, sld: str):
        fee = self._get_fee(sld, None, None, apps.epp_api.fee_pb2.Restore)
        if not fee:
            return self.representative_restore()
        else:
            return fee

    def transfer(self, sld: str, value=None, unit=None):
        return self._get_fee(sld, value, unit, apps.epp_api.fee_pb2.Transfer)


class DomainInfo:
    REGISTRY_NOMINET = "nominet"
    REGISTRY_SWITCH = "switch"
    REGISTRY_TRAFICOM = "traficom"
    REGISTRY_AFILIAS = "afilias"
    REGISTRY_DENIC = "denic"
    REGISTRY_VERISIGN = "verisign"
    REGISTRY_DONUTS = "donuts"
    REGISTRY_VERISIGN_COMNET = "verisign-comnet"
    REGISTRY_PIR = "pir"
    REGISTRY_CENTRALNIC = "centralnic"
    REGISTRY_NOMINET_GTLD = "nominet-gtld"
    REGISTRY_DNSBELGIUM = "dnsbelgium"

    def __init__(self, registry, pricing):
        self.registry = registry
        self.pricing = pricing

    @property
    def transfer_supported(self):
        return self.registry in (
            self.REGISTRY_SWITCH,
            self.REGISTRY_DENIC
        )

    @property
    def pre_transfer_query_supported(self):
        return self.registry in (
            self.REGISTRY_SWITCH,
            self.REGISTRY_AFILIAS,
            self.REGISTRY_NOMINET,
            self.REGISTRY_TRAFICOM,
            self.REGISTRY_VERISIGN
        )

    @property
    def renew_supported(self):
        return self.registry not in (
            self.REGISTRY_SWITCH,
            self.REGISTRY_DENIC
        )

    @property
    def restore_supported(self):
        return self.registry not in (
            self.REGISTRY_NOMINET,
        )

    @property
    def transfer_lock_supported(self):
        return self.registry not in (
            self.REGISTRY_NOMINET,
            self.REGISTRY_SWITCH,
            self.REGISTRY_TRAFICOM
        )

    @property
    def fee_supported(self):
        return self.registry not in (
            self.REGISTRY_TRAFICOM,
            self.REGISTRY_NOMINET,
            self.REGISTRY_SWITCH
        )

    @property
    def registrant_supported(self):
        return self.registry not in (
            self.REGISTRY_VERISIGN
        )

    @property
    def registrant_change_supported(self):
        return self.registry not in (
            self.REGISTRY_TRAFICOM,
            self.REGISTRY_DNSBELGIUM,
        )

    @property
    def ds_data_supported(self):
        return self.registry not in (
            self.REGISTRY_DENIC
        )

    @property
    def admin_supported(self):
        return self.registry not in (
            self.REGISTRY_SWITCH,
            self.REGISTRY_NOMINET,
            self.REGISTRY_TRAFICOM,
            self.REGISTRY_VERISIGN,
            self.REGISTRY_DNSBELGIUM,
        )

    @property
    def admin_required(self):
        return self.registry in (
            self.REGISTRY_AFILIAS,
            self.REGISTRY_DONUTS,
            self.REGISTRY_VERISIGN_COMNET,
            self.REGISTRY_PIR,
            self.REGISTRY_CENTRALNIC,
            self.REGISTRY_NOMINET_GTLD,
        )

    @property
    def tech_supported(self):
        return self.registry not in (
            self.REGISTRY_NOMINET,
            self.REGISTRY_TRAFICOM,
            self.REGISTRY_VERISIGN,
        )

    @property
    def tech_required(self):
        return self.registry in (
            self.REGISTRY_AFILIAS,
            self.REGISTRY_DONUTS,
            self.REGISTRY_VERISIGN_COMNET,
            self.REGISTRY_PIR,
            self.REGISTRY_CENTRALNIC,
            self.REGISTRY_NOMINET_GTLD,
        )

    @property
    def billing_supported(self):
        return self.registry not in (
            self.REGISTRY_SWITCH,
            self.REGISTRY_NOMINET,
            self.REGISTRY_TRAFICOM,
            self.REGISTRY_VERISIGN,
        )

    @property
    def billing_required(self):
        return self.registry in (
            self.REGISTRY_AFILIAS,
            self.REGISTRY_DONUTS,
            self.REGISTRY_VERISIGN_COMNET,
            self.REGISTRY_PIR,
            self.REGISTRY_CENTRALNIC,
            self.REGISTRY_NOMINET_GTLD,
        )


if settings.DEBUG:
    ZONES = (
        ('uk', DomainInfo(DomainInfo.REGISTRY_NOMINET, SimplePrice(8000, periods=[apps.epp_api.Period(
            unit=0,
            value=2
        )]))),
        ('co.uk', DomainInfo(DomainInfo.REGISTRY_NOMINET, SimplePrice(8000, periods=[apps.epp_api.Period(
            unit=0,
            value=2
        )]))),
        ('org.uk', DomainInfo(DomainInfo.REGISTRY_NOMINET, SimplePrice(8000, periods=[apps.epp_api.Period(
            unit=0,
            value=2
        )]))),
        ('me.uk', DomainInfo(DomainInfo.REGISTRY_NOMINET, SimplePrice(8000, periods=[apps.epp_api.Period(
            unit=0,
            value=2
        )]))),
        ('ltd.uk', DomainInfo(DomainInfo.REGISTRY_NOMINET, SimplePrice(8000, periods=[apps.epp_api.Period(
            unit=0,
            value=2
        )]))),
        ('plc.uk', DomainInfo(DomainInfo.REGISTRY_NOMINET, SimplePrice(8000, periods=[apps.epp_api.Period(
            unit=0,
            value=2
        )]))),
        ('net.uk', DomainInfo(DomainInfo.REGISTRY_NOMINET, SimplePrice(8000, periods=[apps.epp_api.Period(
            unit=0,
            value=2
        )]))),
        ('ch', DomainInfo(DomainInfo.REGISTRY_SWITCH, SimplePrice(1400, periods=[apps.epp_api.Period(
            unit=0,
            value=1
        )]))),
        ('li', DomainInfo(DomainInfo.REGISTRY_SWITCH, SimplePrice(1400, periods=[apps.epp_api.Period(
            unit=0,
            value=1
        )]))),
        # ('ae.org', LengthPrice(1600, {2: 17000})),
        # ('br.com', LengthPrice(3200, {2: 17000})),
        # ('cn.com', LengthPrice(1400, {2: 17000}, renewal=3000)),
        # ('co.com', SimplePrice(2000, restore=4000)),
        # ('co.nl', SimplePrice(700, restore=5000)),
        # ('co.no', SimplePrice(1600, restore=5000)),
        # ('com.de', LengthPrice(500, {2: 12500})),
        # ('com.se', SimplePrice(900)),
        # ('de.com', LengthPrice(1400, {2: 12500})),
        # ('eu.com', LengthPrice(1400, {2: 12500})),
        # ('fm', SimplePrice(7500, restore=3500)),
        # ('fo', SimplePrice(4500, restore=4500)),
        # ('gb.net', SimplePrice(700)),
        # ('gd', SimplePrice(2500, restore=4300)),
        # ('gr.com', SimplePrice(1500)),
        # ('hu.net', SimplePrice(2500)),
        # ('in.net', SimplePrice(700)),
        # ('jp.net', SimplePrice(900)),
        # ('jpn.com', SimplePrice(3200)),
        # ('mex.com', SimplePrice(1200)),
        # ('pw', SimplePrice(1800)),
        # ('radio.am', SimplePrice(1400, restore=3500)),
        # ('radio.fm', SimplePrice(1400, restore=3500)),
        # ('ru.com', SimplePrice(3000)),
        # ('sa.com', SimplePrice(4500)),
        # ('se.net', SimplePrice(2700)),
        # ('uk.com', SimplePrice(2100)),
        # ('uk.net', SimplePrice(2100)),
        # ('us.com', SimplePrice(1900)),
        # ('us.org', SimplePrice(1900)),
        # ('vg', SimplePrice(2500, restore=4500)),
        # ('za.com', SimplePrice(4700)),
        ('fi', DomainInfo(DomainInfo.REGISTRY_TRAFICOM, SimplePrice(2500, periods=map(lambda i: apps.epp_api.Period(
            unit=0,
            value=i
        ), range(1, 6))))),
        ('me', DomainInfo(
            DomainInfo.REGISTRY_AFILIAS,
            MarkupPrice(1400, currency='EUR', tld='me', markup=decimal.Decimal("1.25"))
        )),
        ('de', DomainInfo(
            DomainInfo.REGISTRY_DENIC,
            MarkupPrice(1368, renewal=1080, restore=4500, currency='EUR', tld='de', markup=decimal.Decimal("1.5"))
        )),
        ('tv', DomainInfo(DomainInfo.REGISTRY_VERISIGN, SimplePrice(2566, restore=4000))),
        ('cc', DomainInfo(DomainInfo.REGISTRY_VERISIGN, SimplePrice(825, restore=4000))),
    )
else:
    ZONES = (
        ('com', DomainInfo(
            DomainInfo.REGISTRY_VERISIGN_COMNET,
            MarkupPrice(1975, renewal=1975, restore=14331, currency='EUR', tld='com', markup=decimal.Decimal("1.5"))
        )),
        ('net', DomainInfo(
            DomainInfo.REGISTRY_VERISIGN_COMNET,
            MarkupPrice(2661, renewal=2661, restore=13376, currency='EUR', tld='net', markup=decimal.Decimal("1.4"))
        )),
        ('org', DomainInfo(
            DomainInfo.REGISTRY_PIR,
            MarkupPrice(2438, renewal=2438, restore=1383, currency='EUR', tld='org', markup=decimal.Decimal("1.45"))
        )),
        ('gay', DomainInfo(
            DomainInfo.REGISTRY_CENTRALNIC,
            MarkupPrice(5731, renewal=5731, restore=33173, currency='EUR', tld='gay', markup=decimal.Decimal("1.25"))
        )),
        ('site', DomainInfo(
            DomainInfo.REGISTRY_CENTRALNIC,
            MarkupPrice(4603, renewal=4603, restore=1496, currency='EUR', tld='site', markup=decimal.Decimal("1.25"))
        )),
        ('website', DomainInfo(
            DomainInfo.REGISTRY_CENTRALNIC,
            MarkupPrice(3450, renewal=3450, restore=11943, currency='EUR', tld='website', markup=decimal.Decimal("1.25"))
        )),
        ('tech', DomainInfo(
            DomainInfo.REGISTRY_CENTRALNIC,
            MarkupPrice(7987, renewal=7987, restore=14596, currency='EUR', tld='tech', markup=decimal.Decimal("1.25"))
        )),
        ('xyz', DomainInfo(
            DomainInfo.REGISTRY_CENTRALNIC,
            MarkupPrice(2212, renewal=2212, restore=15924, currency='EUR', tld='xyz', markup=decimal.Decimal("1.5"))
        )),
        ('de', DomainInfo(
            DomainInfo.REGISTRY_DENIC,
            MarkupPrice(1596, renewal=1260, restore=5250, currency='EUR', tld='de', markup=decimal.Decimal("1.75"))
        )),
        ('ch', DomainInfo(DomainInfo.REGISTRY_SWITCH, SimplePrice(999, periods=[apps.epp_api.Period(
            unit=0,
            value=1
        )]))),
        ('li', DomainInfo(DomainInfo.REGISTRY_SWITCH, SimplePrice(999, periods=[apps.epp_api.Period(
            unit=0,
            value=1
        )]))),
        ('space', DomainInfo(
            DomainInfo.REGISTRY_DONUTS,
            MarkupPrice(3443, renewal=3443, restore=11943, currency='EUR', tld='space', markup=decimal.Decimal("1.25"))
        )),
        ('fi', DomainInfo(DomainInfo.REGISTRY_TRAFICOM, SimplePrice(1400, periods=map(lambda i: apps.epp_api.Period(
            unit=0,
            value=i
        ), range(1, 6))))),
        ('cymru', DomainInfo(
            DomainInfo.REGISTRY_NOMINET_GTLD,
            MarkupPrice(2418, renewal=2418, restore=2999, currency='EUR', tld='cymru', markup=decimal.Decimal("1.4"))
        )),
        ('wales', DomainInfo(
            DomainInfo.REGISTRY_NOMINET_GTLD,
            MarkupPrice(2418, renewal=2418, restore=2999, currency='EUR', tld='wales', markup=decimal.Decimal("1.4"))
        )),
    )


def get_domain_info(domain: str):
    parts = domain.rstrip(".").split(".", maxsplit=1)
    if len(parts) != 2:
        return None, domain
    sld, tld = parts
    for zone in ZONES:
        if zone[0] == tld:
            return zone[1], sld

    return None, sld
