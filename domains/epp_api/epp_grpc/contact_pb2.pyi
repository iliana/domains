# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from common_pb2 import (
    TransferStatusValue as common_pb2___TransferStatusValue,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    NewType as typing___NewType,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

EntityTypeValue = typing___NewType('EntityTypeValue', builtin___int)
type___EntityTypeValue = EntityTypeValue
class EntityType(object):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> EntityTypeValue: ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List[EntityTypeValue]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, EntityTypeValue]]: ...
    NotSet = typing___cast(EntityTypeValue, 0)
    UnknownEntity = typing___cast(EntityTypeValue, 1)
    UkLimitedCompany = typing___cast(EntityTypeValue, 2)
    UkPublicLimitedCompany = typing___cast(EntityTypeValue, 3)
    UkPartnership = typing___cast(EntityTypeValue, 4)
    UkSoleTrader = typing___cast(EntityTypeValue, 5)
    UkLimitedLiabilityPartnership = typing___cast(EntityTypeValue, 6)
    UkIndustrialProvidentRegisteredCompany = typing___cast(EntityTypeValue, 7)
    UkIndividual = typing___cast(EntityTypeValue, 8)
    UkSchool = typing___cast(EntityTypeValue, 9)
    UkRegisteredCharity = typing___cast(EntityTypeValue, 10)
    UkGovernmentBody = typing___cast(EntityTypeValue, 11)
    UkCorporationByRoyalCharter = typing___cast(EntityTypeValue, 12)
    UkStatutoryBody = typing___cast(EntityTypeValue, 13)
    UkPoliticalParty = typing___cast(EntityTypeValue, 31)
    OtherUkEntity = typing___cast(EntityTypeValue, 14)
    FinnishIndividual = typing___cast(EntityTypeValue, 15)
    FinnishCompany = typing___cast(EntityTypeValue, 16)
    FinnishAssociation = typing___cast(EntityTypeValue, 17)
    FinnishInstitution = typing___cast(EntityTypeValue, 18)
    FinnishPoliticalParty = typing___cast(EntityTypeValue, 19)
    FinnishMunicipality = typing___cast(EntityTypeValue, 20)
    FinnishGovernment = typing___cast(EntityTypeValue, 21)
    FinnishPublicCommunity = typing___cast(EntityTypeValue, 22)
    OtherIndividual = typing___cast(EntityTypeValue, 23)
    OtherCompany = typing___cast(EntityTypeValue, 24)
    OtherAssociation = typing___cast(EntityTypeValue, 25)
    OtherInstitution = typing___cast(EntityTypeValue, 26)
    OtherPoliticalParty = typing___cast(EntityTypeValue, 27)
    OtherMunicipality = typing___cast(EntityTypeValue, 28)
    OtherGovernment = typing___cast(EntityTypeValue, 29)
    OtherPublicCommunity = typing___cast(EntityTypeValue, 30)
NotSet = typing___cast(EntityTypeValue, 0)
UnknownEntity = typing___cast(EntityTypeValue, 1)
UkLimitedCompany = typing___cast(EntityTypeValue, 2)
UkPublicLimitedCompany = typing___cast(EntityTypeValue, 3)
UkPartnership = typing___cast(EntityTypeValue, 4)
UkSoleTrader = typing___cast(EntityTypeValue, 5)
UkLimitedLiabilityPartnership = typing___cast(EntityTypeValue, 6)
UkIndustrialProvidentRegisteredCompany = typing___cast(EntityTypeValue, 7)
UkIndividual = typing___cast(EntityTypeValue, 8)
UkSchool = typing___cast(EntityTypeValue, 9)
UkRegisteredCharity = typing___cast(EntityTypeValue, 10)
UkGovernmentBody = typing___cast(EntityTypeValue, 11)
UkCorporationByRoyalCharter = typing___cast(EntityTypeValue, 12)
UkStatutoryBody = typing___cast(EntityTypeValue, 13)
UkPoliticalParty = typing___cast(EntityTypeValue, 31)
OtherUkEntity = typing___cast(EntityTypeValue, 14)
FinnishIndividual = typing___cast(EntityTypeValue, 15)
FinnishCompany = typing___cast(EntityTypeValue, 16)
FinnishAssociation = typing___cast(EntityTypeValue, 17)
FinnishInstitution = typing___cast(EntityTypeValue, 18)
FinnishPoliticalParty = typing___cast(EntityTypeValue, 19)
FinnishMunicipality = typing___cast(EntityTypeValue, 20)
FinnishGovernment = typing___cast(EntityTypeValue, 21)
FinnishPublicCommunity = typing___cast(EntityTypeValue, 22)
OtherIndividual = typing___cast(EntityTypeValue, 23)
OtherCompany = typing___cast(EntityTypeValue, 24)
OtherAssociation = typing___cast(EntityTypeValue, 25)
OtherInstitution = typing___cast(EntityTypeValue, 26)
OtherPoliticalParty = typing___cast(EntityTypeValue, 27)
OtherMunicipality = typing___cast(EntityTypeValue, 28)
OtherGovernment = typing___cast(EntityTypeValue, 29)
OtherPublicCommunity = typing___cast(EntityTypeValue, 30)
type___EntityType = EntityType

DisclosureTypeValue = typing___NewType('DisclosureTypeValue', builtin___int)
type___DisclosureTypeValue = DisclosureTypeValue
class DisclosureType(object):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> DisclosureTypeValue: ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List[DisclosureTypeValue]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, DisclosureTypeValue]]: ...
    LocalName = typing___cast(DisclosureTypeValue, 0)
    InternationalisedName = typing___cast(DisclosureTypeValue, 1)
    LocalOrganisation = typing___cast(DisclosureTypeValue, 2)
    InternationalisedOrganisation = typing___cast(DisclosureTypeValue, 3)
    LocalAddress = typing___cast(DisclosureTypeValue, 4)
    InternationalisedAddress = typing___cast(DisclosureTypeValue, 5)
    Voice = typing___cast(DisclosureTypeValue, 6)
    Fax = typing___cast(DisclosureTypeValue, 7)
    Email = typing___cast(DisclosureTypeValue, 8)
LocalName = typing___cast(DisclosureTypeValue, 0)
InternationalisedName = typing___cast(DisclosureTypeValue, 1)
LocalOrganisation = typing___cast(DisclosureTypeValue, 2)
InternationalisedOrganisation = typing___cast(DisclosureTypeValue, 3)
LocalAddress = typing___cast(DisclosureTypeValue, 4)
InternationalisedAddress = typing___cast(DisclosureTypeValue, 5)
Voice = typing___cast(DisclosureTypeValue, 6)
Fax = typing___cast(DisclosureTypeValue, 7)
Email = typing___cast(DisclosureTypeValue, 8)
type___DisclosureType = DisclosureType

ContactStatusValue = typing___NewType('ContactStatusValue', builtin___int)
type___ContactStatusValue = ContactStatusValue
class ContactStatus(object):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> ContactStatusValue: ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List[ContactStatusValue]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, ContactStatusValue]]: ...
    ClientDeleteProhibited = typing___cast(ContactStatusValue, 0)
    ClientTransferProhibited = typing___cast(ContactStatusValue, 1)
    ClientUpdateProhibited = typing___cast(ContactStatusValue, 2)
    Linked = typing___cast(ContactStatusValue, 3)
    Ok = typing___cast(ContactStatusValue, 4)
    PendingCreate = typing___cast(ContactStatusValue, 5)
    PendingDelete = typing___cast(ContactStatusValue, 6)
    PendingTransfer = typing___cast(ContactStatusValue, 7)
    PendingUpdate = typing___cast(ContactStatusValue, 8)
    ServerDeleteProhibited = typing___cast(ContactStatusValue, 9)
    ServerTransferProhibited = typing___cast(ContactStatusValue, 10)
    ServerUpdateProhibited = typing___cast(ContactStatusValue, 11)
ClientDeleteProhibited = typing___cast(ContactStatusValue, 0)
ClientTransferProhibited = typing___cast(ContactStatusValue, 1)
ClientUpdateProhibited = typing___cast(ContactStatusValue, 2)
Linked = typing___cast(ContactStatusValue, 3)
Ok = typing___cast(ContactStatusValue, 4)
PendingCreate = typing___cast(ContactStatusValue, 5)
PendingDelete = typing___cast(ContactStatusValue, 6)
PendingTransfer = typing___cast(ContactStatusValue, 7)
PendingUpdate = typing___cast(ContactStatusValue, 8)
ServerDeleteProhibited = typing___cast(ContactStatusValue, 9)
ServerTransferProhibited = typing___cast(ContactStatusValue, 10)
ServerUpdateProhibited = typing___cast(ContactStatusValue, 11)
type___ContactStatus = ContactStatus

class PostalAddress(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    streets: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...
    city: typing___Text = ...
    country_code: typing___Text = ...

    @property
    def organisation(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def province(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def postal_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def identity_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def birth_date(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        organisation : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        streets : typing___Optional[typing___Iterable[typing___Text]] = None,
        city : typing___Optional[typing___Text] = None,
        province : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        postal_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        country_code : typing___Optional[typing___Text] = None,
        identity_number : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        birth_date : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PostalAddress: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PostalAddress: ...
    def HasField(self, field_name: typing_extensions___Literal[u"birth_date",b"birth_date",u"identity_number",b"identity_number",u"organisation",b"organisation",u"postal_code",b"postal_code",u"province",b"province"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"birth_date",b"birth_date",u"city",b"city",u"country_code",b"country_code",u"identity_number",b"identity_number",u"name",b"name",u"organisation",b"organisation",u"postal_code",b"postal_code",u"province",b"province",u"streets",b"streets"]) -> None: ...
type___PostalAddress = PostalAddress

class Phone(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    number: typing___Text = ...

    @property
    def extension(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        number : typing___Optional[typing___Text] = None,
        extension : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Phone: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Phone: ...
    def HasField(self, field_name: typing_extensions___Literal[u"extension",b"extension"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"extension",b"extension",u"number",b"number"]) -> None: ...
type___Phone = Phone

class ContactCheckRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    registry_name: typing___Text = ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        registry_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactCheckRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactCheckRequest: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"registry_name",b"registry_name"]) -> None: ...
type___ContactCheckRequest = ContactCheckRequest

class ContactCheckReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    available: builtin___bool = ...

    @property
    def reason(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        available : typing___Optional[builtin___bool] = None,
        reason : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactCheckReply: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactCheckReply: ...
    def HasField(self, field_name: typing_extensions___Literal[u"reason",b"reason"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"available",b"available",u"reason",b"reason"]) -> None: ...
type___ContactCheckReply = ContactCheckReply

class ContactInfoRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    registry_name: typing___Text = ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        registry_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactInfoRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactInfoRequest: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"registry_name",b"registry_name"]) -> None: ...
type___ContactInfoRequest = ContactInfoRequest

class Disclosure(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    disclosure: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___DisclosureTypeValue] = ...

    def __init__(self,
        *,
        disclosure : typing___Optional[typing___Iterable[type___DisclosureTypeValue]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Disclosure: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Disclosure: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"disclosure",b"disclosure"]) -> None: ...
type___Disclosure = Disclosure

class ContactInfoReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    registry_id: typing___Text = ...
    statuses: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___ContactStatusValue] = ...
    email: typing___Text = ...
    client_id: typing___Text = ...
    entity_type: type___EntityTypeValue = ...
    disclosure: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___DisclosureTypeValue] = ...

    @property
    def local_address(self) -> type___PostalAddress: ...

    @property
    def internationalised_address(self) -> type___PostalAddress: ...

    @property
    def phone(self) -> type___Phone: ...

    @property
    def fax(self) -> type___Phone: ...

    @property
    def client_created_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def creation_date(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    @property
    def last_updated_client(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def last_updated_date(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    @property
    def last_transfer_date(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    @property
    def trading_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def company_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def auth_info(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        registry_id : typing___Optional[typing___Text] = None,
        statuses : typing___Optional[typing___Iterable[type___ContactStatusValue]] = None,
        local_address : typing___Optional[type___PostalAddress] = None,
        internationalised_address : typing___Optional[type___PostalAddress] = None,
        phone : typing___Optional[type___Phone] = None,
        fax : typing___Optional[type___Phone] = None,
        email : typing___Optional[typing___Text] = None,
        client_id : typing___Optional[typing___Text] = None,
        client_created_id : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        creation_date : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        last_updated_client : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        last_updated_date : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        last_transfer_date : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        entity_type : typing___Optional[type___EntityTypeValue] = None,
        trading_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        company_number : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        disclosure : typing___Optional[typing___Iterable[type___DisclosureTypeValue]] = None,
        auth_info : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactInfoReply: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactInfoReply: ...
    def HasField(self, field_name: typing_extensions___Literal[u"auth_info",b"auth_info",u"client_created_id",b"client_created_id",u"company_number",b"company_number",u"creation_date",b"creation_date",u"fax",b"fax",u"internationalised_address",b"internationalised_address",u"last_transfer_date",b"last_transfer_date",u"last_updated_client",b"last_updated_client",u"last_updated_date",b"last_updated_date",u"local_address",b"local_address",u"phone",b"phone",u"trading_name",b"trading_name"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"auth_info",b"auth_info",u"client_created_id",b"client_created_id",u"client_id",b"client_id",u"company_number",b"company_number",u"creation_date",b"creation_date",u"disclosure",b"disclosure",u"email",b"email",u"entity_type",b"entity_type",u"fax",b"fax",u"id",b"id",u"internationalised_address",b"internationalised_address",u"last_transfer_date",b"last_transfer_date",u"last_updated_client",b"last_updated_client",u"last_updated_date",b"last_updated_date",u"local_address",b"local_address",u"phone",b"phone",u"registry_id",b"registry_id",u"statuses",b"statuses",u"trading_name",b"trading_name"]) -> None: ...
type___ContactInfoReply = ContactInfoReply

class ContactCreateRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    email: typing___Text = ...
    entity_type: type___EntityTypeValue = ...
    registry_name: typing___Text = ...
    auth_info: typing___Text = ...

    @property
    def local_address(self) -> type___PostalAddress: ...

    @property
    def internationalised_address(self) -> type___PostalAddress: ...

    @property
    def phone(self) -> type___Phone: ...

    @property
    def fax(self) -> type___Phone: ...

    @property
    def trading_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def company_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def disclosure(self) -> type___Disclosure: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        local_address : typing___Optional[type___PostalAddress] = None,
        internationalised_address : typing___Optional[type___PostalAddress] = None,
        phone : typing___Optional[type___Phone] = None,
        fax : typing___Optional[type___Phone] = None,
        email : typing___Optional[typing___Text] = None,
        entity_type : typing___Optional[type___EntityTypeValue] = None,
        trading_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        company_number : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        disclosure : typing___Optional[type___Disclosure] = None,
        registry_name : typing___Optional[typing___Text] = None,
        auth_info : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactCreateRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactCreateRequest: ...
    def HasField(self, field_name: typing_extensions___Literal[u"company_number",b"company_number",u"disclosure",b"disclosure",u"fax",b"fax",u"internationalised_address",b"internationalised_address",u"local_address",b"local_address",u"phone",b"phone",u"trading_name",b"trading_name"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"auth_info",b"auth_info",u"company_number",b"company_number",u"disclosure",b"disclosure",u"email",b"email",u"entity_type",b"entity_type",u"fax",b"fax",u"id",b"id",u"internationalised_address",b"internationalised_address",u"local_address",b"local_address",u"phone",b"phone",u"registry_name",b"registry_name",u"trading_name",b"trading_name"]) -> None: ...
type___ContactCreateRequest = ContactCreateRequest

class ContactCreateReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    pending: builtin___bool = ...

    @property
    def creation_date(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        pending : typing___Optional[builtin___bool] = None,
        creation_date : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactCreateReply: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactCreateReply: ...
    def HasField(self, field_name: typing_extensions___Literal[u"creation_date",b"creation_date"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"creation_date",b"creation_date",u"id",b"id",u"pending",b"pending"]) -> None: ...
type___ContactCreateReply = ContactCreateReply

class ContactDeleteRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    registry_name: typing___Text = ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        registry_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactDeleteRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactDeleteRequest: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"registry_name",b"registry_name"]) -> None: ...
type___ContactDeleteRequest = ContactDeleteRequest

class ContactDeleteReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    pending: builtin___bool = ...

    def __init__(self,
        *,
        pending : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactDeleteReply: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactDeleteReply: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"pending",b"pending"]) -> None: ...
type___ContactDeleteReply = ContactDeleteReply

class ContactUpdateRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    add_statuses: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___ContactStatusValue] = ...
    remove_statuses: google___protobuf___internal___containers___RepeatedScalarFieldContainer[type___ContactStatusValue] = ...
    new_entity_type: type___EntityTypeValue = ...
    registry_name: typing___Text = ...

    @property
    def new_local_address(self) -> type___PostalAddress: ...

    @property
    def new_internationalised_address(self) -> type___PostalAddress: ...

    @property
    def new_phone(self) -> type___Phone: ...

    @property
    def new_fax(self) -> type___Phone: ...

    @property
    def new_email(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def new_trading_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def new_company_number(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def disclosure(self) -> type___Disclosure: ...

    @property
    def new_auth_info(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        add_statuses : typing___Optional[typing___Iterable[type___ContactStatusValue]] = None,
        remove_statuses : typing___Optional[typing___Iterable[type___ContactStatusValue]] = None,
        new_local_address : typing___Optional[type___PostalAddress] = None,
        new_internationalised_address : typing___Optional[type___PostalAddress] = None,
        new_phone : typing___Optional[type___Phone] = None,
        new_fax : typing___Optional[type___Phone] = None,
        new_email : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        new_entity_type : typing___Optional[type___EntityTypeValue] = None,
        new_trading_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        new_company_number : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        disclosure : typing___Optional[type___Disclosure] = None,
        registry_name : typing___Optional[typing___Text] = None,
        new_auth_info : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactUpdateRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactUpdateRequest: ...
    def HasField(self, field_name: typing_extensions___Literal[u"disclosure",b"disclosure",u"new_auth_info",b"new_auth_info",u"new_company_number",b"new_company_number",u"new_email",b"new_email",u"new_fax",b"new_fax",u"new_internationalised_address",b"new_internationalised_address",u"new_local_address",b"new_local_address",u"new_phone",b"new_phone",u"new_trading_name",b"new_trading_name"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"add_statuses",b"add_statuses",u"disclosure",b"disclosure",u"id",b"id",u"new_auth_info",b"new_auth_info",u"new_company_number",b"new_company_number",u"new_email",b"new_email",u"new_entity_type",b"new_entity_type",u"new_fax",b"new_fax",u"new_internationalised_address",b"new_internationalised_address",u"new_local_address",b"new_local_address",u"new_phone",b"new_phone",u"new_trading_name",b"new_trading_name",u"registry_name",b"registry_name",u"remove_statuses",b"remove_statuses"]) -> None: ...
type___ContactUpdateRequest = ContactUpdateRequest

class ContactUpdateReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    pending: builtin___bool = ...

    def __init__(self,
        *,
        pending : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactUpdateReply: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactUpdateReply: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"pending",b"pending"]) -> None: ...
type___ContactUpdateReply = ContactUpdateReply

class ContactTransferQueryRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    registry_name: typing___Text = ...

    @property
    def auth_info(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        auth_info : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        registry_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactTransferQueryRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactTransferQueryRequest: ...
    def HasField(self, field_name: typing_extensions___Literal[u"auth_info",b"auth_info"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"auth_info",b"auth_info",u"id",b"id",u"registry_name",b"registry_name"]) -> None: ...
type___ContactTransferQueryRequest = ContactTransferQueryRequest

class ContactTransferRequestRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id: typing___Text = ...
    auth_info: typing___Text = ...
    registry_name: typing___Text = ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        auth_info : typing___Optional[typing___Text] = None,
        registry_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactTransferRequestRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactTransferRequestRequest: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"auth_info",b"auth_info",u"id",b"id",u"registry_name",b"registry_name"]) -> None: ...
type___ContactTransferRequestRequest = ContactTransferRequestRequest

class ContactTransferReply(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    pending: builtin___bool = ...
    status: common_pb2___TransferStatusValue = ...
    requested_client_id: typing___Text = ...
    act_client_id: typing___Text = ...

    @property
    def requested_date(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    @property
    def act_date(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

    def __init__(self,
        *,
        pending : typing___Optional[builtin___bool] = None,
        status : typing___Optional[common_pb2___TransferStatusValue] = None,
        requested_client_id : typing___Optional[typing___Text] = None,
        requested_date : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        act_client_id : typing___Optional[typing___Text] = None,
        act_date : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContactTransferReply: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ContactTransferReply: ...
    def HasField(self, field_name: typing_extensions___Literal[u"act_date",b"act_date",u"requested_date",b"requested_date"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"act_client_id",b"act_client_id",u"act_date",b"act_date",u"pending",b"pending",u"requested_client_id",b"requested_client_id",u"requested_date",b"requested_date",u"status",b"status"]) -> None: ...
type___ContactTransferReply = ContactTransferReply
