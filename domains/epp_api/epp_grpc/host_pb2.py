# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: host.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='host.proto',
  package='epp.host',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nhost.proto\x12\x08\x65pp.host\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0c\x63ommon.proto\"7\n\x10HostCheckRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rregistry_name\x18\x02 \x01(\t\"Q\n\x0eHostCheckReply\x12\x11\n\tavailable\x18\x01 \x01(\x08\x12,\n\x06reason\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"6\n\x0fHostInfoRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rregistry_name\x18\x02 \x01(\t\"\xad\x03\n\rHostInfoReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bregistry_id\x18\x02 \x01(\t\x12&\n\x08statuses\x18\x03 \x03(\x0e\x32\x14.epp.host.HostStatus\x12(\n\taddresses\x18\x04 \x03(\x0b\x32\x15.epp.common.IPAddress\x12\x11\n\tclient_id\x18\x05 \x01(\t\x12\x37\n\x11\x63lient_created_id\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\rcreation_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x39\n\x13last_updated_client\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x11last_updated_date\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x12last_transfer_date\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"b\n\x11HostCreateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\taddresses\x18\x02 \x03(\x0b\x32\x15.epp.common.IPAddress\x12\x15\n\rregistry_name\x18\x03 \x01(\t\"{\n\x0fHostCreateReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07pending\x18\x02 \x01(\x08\x12\x16\n\x0etransaction_id\x18\x04 \x01(\t\x12\x31\n\rcreation_date\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"8\n\x11HostDeleteRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rregistry_name\x18\x02 \x01(\t\":\n\x0fHostDeleteReply\x12\x0f\n\x07pending\x18\x01 \x01(\x08\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t\"\xae\x02\n\x11HostUpdateRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x03\x61\x64\x64\x18\x02 \x03(\x0b\x32!.epp.host.HostUpdateRequest.Param\x12\x31\n\x06remove\x18\x03 \x03(\x0b\x32!.epp.host.HostUpdateRequest.Param\x12.\n\x08new_name\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x15\n\rregistry_name\x18\x05 \x01(\t\x1a\x61\n\x05Param\x12(\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x15.epp.common.IPAddressH\x00\x12%\n\x05state\x18\x02 \x01(\x0e\x32\x14.epp.host.HostStatusH\x00\x42\x07\n\x05param\":\n\x0fHostUpdateReply\x12\x0f\n\x07pending\x18\x01 \x01(\x08\x12\x16\n\x0etransaction_id\x18\x02 \x01(\t*\xde\x01\n\nHostStatus\x12\x1a\n\x16\x43lientDeleteProhibited\x10\x00\x12\x1a\n\x16\x43lientUpdateProhibited\x10\x01\x12\n\n\x06Linked\x10\x02\x12\x06\n\x02Ok\x10\x03\x12\x11\n\rPendingCreate\x10\x04\x12\x11\n\rPendingDelete\x10\x05\x12\x13\n\x0fPendingTransfer\x10\x06\x12\x11\n\rPendingUpdate\x10\x07\x12\x1a\n\x16ServerDeleteProhibited\x10\x08\x12\x1a\n\x16ServerUpdateProhibited\x10\tb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,common__pb2.DESCRIPTOR,])

_HOSTSTATUS = _descriptor.EnumDescriptor(
  name='HostStatus',
  full_name='epp.host.HostStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ClientDeleteProhibited', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ClientUpdateProhibited', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Linked', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Ok', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PendingCreate', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PendingDelete', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PendingTransfer', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PendingUpdate', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ServerDeleteProhibited', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ServerUpdateProhibited', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1440,
  serialized_end=1662,
)
_sym_db.RegisterEnumDescriptor(_HOSTSTATUS)

HostStatus = enum_type_wrapper.EnumTypeWrapper(_HOSTSTATUS)
ClientDeleteProhibited = 0
ClientUpdateProhibited = 1
Linked = 2
Ok = 3
PendingCreate = 4
PendingDelete = 5
PendingTransfer = 6
PendingUpdate = 7
ServerDeleteProhibited = 8
ServerUpdateProhibited = 9



_HOSTCHECKREQUEST = _descriptor.Descriptor(
  name='HostCheckRequest',
  full_name='epp.host.HostCheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='epp.host.HostCheckRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_name', full_name='epp.host.HostCheckRequest.registry_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=158,
)


_HOSTCHECKREPLY = _descriptor.Descriptor(
  name='HostCheckReply',
  full_name='epp.host.HostCheckReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='available', full_name='epp.host.HostCheckReply.available', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reason', full_name='epp.host.HostCheckReply.reason', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=160,
  serialized_end=241,
)


_HOSTINFOREQUEST = _descriptor.Descriptor(
  name='HostInfoRequest',
  full_name='epp.host.HostInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='epp.host.HostInfoRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_name', full_name='epp.host.HostInfoRequest.registry_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=297,
)


_HOSTINFOREPLY = _descriptor.Descriptor(
  name='HostInfoReply',
  full_name='epp.host.HostInfoReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='epp.host.HostInfoReply.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_id', full_name='epp.host.HostInfoReply.registry_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statuses', full_name='epp.host.HostInfoReply.statuses', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='epp.host.HostInfoReply.addresses', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='epp.host.HostInfoReply.client_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_created_id', full_name='epp.host.HostInfoReply.client_created_id', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='epp.host.HostInfoReply.creation_date', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_updated_client', full_name='epp.host.HostInfoReply.last_updated_client', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_updated_date', full_name='epp.host.HostInfoReply.last_updated_date', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_transfer_date', full_name='epp.host.HostInfoReply.last_transfer_date', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=729,
)


_HOSTCREATEREQUEST = _descriptor.Descriptor(
  name='HostCreateRequest',
  full_name='epp.host.HostCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='epp.host.HostCreateRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='epp.host.HostCreateRequest.addresses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_name', full_name='epp.host.HostCreateRequest.registry_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=731,
  serialized_end=829,
)


_HOSTCREATEREPLY = _descriptor.Descriptor(
  name='HostCreateReply',
  full_name='epp.host.HostCreateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='epp.host.HostCreateReply.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending', full_name='epp.host.HostCreateReply.pending', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='epp.host.HostCreateReply.transaction_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='epp.host.HostCreateReply.creation_date', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=831,
  serialized_end=954,
)


_HOSTDELETEREQUEST = _descriptor.Descriptor(
  name='HostDeleteRequest',
  full_name='epp.host.HostDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='epp.host.HostDeleteRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_name', full_name='epp.host.HostDeleteRequest.registry_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=956,
  serialized_end=1012,
)


_HOSTDELETEREPLY = _descriptor.Descriptor(
  name='HostDeleteReply',
  full_name='epp.host.HostDeleteReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pending', full_name='epp.host.HostDeleteReply.pending', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='epp.host.HostDeleteReply.transaction_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1014,
  serialized_end=1072,
)


_HOSTUPDATEREQUEST_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='epp.host.HostUpdateRequest.Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='epp.host.HostUpdateRequest.Param.address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='epp.host.HostUpdateRequest.Param.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='param', full_name='epp.host.HostUpdateRequest.Param.param',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1280,
  serialized_end=1377,
)

_HOSTUPDATEREQUEST = _descriptor.Descriptor(
  name='HostUpdateRequest',
  full_name='epp.host.HostUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='epp.host.HostUpdateRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add', full_name='epp.host.HostUpdateRequest.add', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='epp.host.HostUpdateRequest.remove', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_name', full_name='epp.host.HostUpdateRequest.new_name', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_name', full_name='epp.host.HostUpdateRequest.registry_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_HOSTUPDATEREQUEST_PARAM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1075,
  serialized_end=1377,
)


_HOSTUPDATEREPLY = _descriptor.Descriptor(
  name='HostUpdateReply',
  full_name='epp.host.HostUpdateReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pending', full_name='epp.host.HostUpdateReply.pending', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='epp.host.HostUpdateReply.transaction_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1379,
  serialized_end=1437,
)

_HOSTCHECKREPLY.fields_by_name['reason'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_HOSTINFOREPLY.fields_by_name['statuses'].enum_type = _HOSTSTATUS
_HOSTINFOREPLY.fields_by_name['addresses'].message_type = common__pb2._IPADDRESS
_HOSTINFOREPLY.fields_by_name['client_created_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_HOSTINFOREPLY.fields_by_name['creation_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HOSTINFOREPLY.fields_by_name['last_updated_client'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_HOSTINFOREPLY.fields_by_name['last_updated_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HOSTINFOREPLY.fields_by_name['last_transfer_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HOSTCREATEREQUEST.fields_by_name['addresses'].message_type = common__pb2._IPADDRESS
_HOSTCREATEREPLY.fields_by_name['creation_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HOSTUPDATEREQUEST_PARAM.fields_by_name['address'].message_type = common__pb2._IPADDRESS
_HOSTUPDATEREQUEST_PARAM.fields_by_name['state'].enum_type = _HOSTSTATUS
_HOSTUPDATEREQUEST_PARAM.containing_type = _HOSTUPDATEREQUEST
_HOSTUPDATEREQUEST_PARAM.oneofs_by_name['param'].fields.append(
  _HOSTUPDATEREQUEST_PARAM.fields_by_name['address'])
_HOSTUPDATEREQUEST_PARAM.fields_by_name['address'].containing_oneof = _HOSTUPDATEREQUEST_PARAM.oneofs_by_name['param']
_HOSTUPDATEREQUEST_PARAM.oneofs_by_name['param'].fields.append(
  _HOSTUPDATEREQUEST_PARAM.fields_by_name['state'])
_HOSTUPDATEREQUEST_PARAM.fields_by_name['state'].containing_oneof = _HOSTUPDATEREQUEST_PARAM.oneofs_by_name['param']
_HOSTUPDATEREQUEST.fields_by_name['add'].message_type = _HOSTUPDATEREQUEST_PARAM
_HOSTUPDATEREQUEST.fields_by_name['remove'].message_type = _HOSTUPDATEREQUEST_PARAM
_HOSTUPDATEREQUEST.fields_by_name['new_name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['HostCheckRequest'] = _HOSTCHECKREQUEST
DESCRIPTOR.message_types_by_name['HostCheckReply'] = _HOSTCHECKREPLY
DESCRIPTOR.message_types_by_name['HostInfoRequest'] = _HOSTINFOREQUEST
DESCRIPTOR.message_types_by_name['HostInfoReply'] = _HOSTINFOREPLY
DESCRIPTOR.message_types_by_name['HostCreateRequest'] = _HOSTCREATEREQUEST
DESCRIPTOR.message_types_by_name['HostCreateReply'] = _HOSTCREATEREPLY
DESCRIPTOR.message_types_by_name['HostDeleteRequest'] = _HOSTDELETEREQUEST
DESCRIPTOR.message_types_by_name['HostDeleteReply'] = _HOSTDELETEREPLY
DESCRIPTOR.message_types_by_name['HostUpdateRequest'] = _HOSTUPDATEREQUEST
DESCRIPTOR.message_types_by_name['HostUpdateReply'] = _HOSTUPDATEREPLY
DESCRIPTOR.enum_types_by_name['HostStatus'] = _HOSTSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HostCheckRequest = _reflection.GeneratedProtocolMessageType('HostCheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _HOSTCHECKREQUEST,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostCheckRequest)
  })
_sym_db.RegisterMessage(HostCheckRequest)

HostCheckReply = _reflection.GeneratedProtocolMessageType('HostCheckReply', (_message.Message,), {
  'DESCRIPTOR' : _HOSTCHECKREPLY,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostCheckReply)
  })
_sym_db.RegisterMessage(HostCheckReply)

HostInfoRequest = _reflection.GeneratedProtocolMessageType('HostInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _HOSTINFOREQUEST,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostInfoRequest)
  })
_sym_db.RegisterMessage(HostInfoRequest)

HostInfoReply = _reflection.GeneratedProtocolMessageType('HostInfoReply', (_message.Message,), {
  'DESCRIPTOR' : _HOSTINFOREPLY,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostInfoReply)
  })
_sym_db.RegisterMessage(HostInfoReply)

HostCreateRequest = _reflection.GeneratedProtocolMessageType('HostCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _HOSTCREATEREQUEST,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostCreateRequest)
  })
_sym_db.RegisterMessage(HostCreateRequest)

HostCreateReply = _reflection.GeneratedProtocolMessageType('HostCreateReply', (_message.Message,), {
  'DESCRIPTOR' : _HOSTCREATEREPLY,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostCreateReply)
  })
_sym_db.RegisterMessage(HostCreateReply)

HostDeleteRequest = _reflection.GeneratedProtocolMessageType('HostDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _HOSTDELETEREQUEST,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostDeleteRequest)
  })
_sym_db.RegisterMessage(HostDeleteRequest)

HostDeleteReply = _reflection.GeneratedProtocolMessageType('HostDeleteReply', (_message.Message,), {
  'DESCRIPTOR' : _HOSTDELETEREPLY,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostDeleteReply)
  })
_sym_db.RegisterMessage(HostDeleteReply)

HostUpdateRequest = _reflection.GeneratedProtocolMessageType('HostUpdateRequest', (_message.Message,), {

  'Param' : _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), {
    'DESCRIPTOR' : _HOSTUPDATEREQUEST_PARAM,
    '__module__' : 'host_pb2'
    # @@protoc_insertion_point(class_scope:epp.host.HostUpdateRequest.Param)
    })
  ,
  'DESCRIPTOR' : _HOSTUPDATEREQUEST,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostUpdateRequest)
  })
_sym_db.RegisterMessage(HostUpdateRequest)
_sym_db.RegisterMessage(HostUpdateRequest.Param)

HostUpdateReply = _reflection.GeneratedProtocolMessageType('HostUpdateReply', (_message.Message,), {
  'DESCRIPTOR' : _HOSTUPDATEREPLY,
  '__module__' : 'host_pb2'
  # @@protoc_insertion_point(class_scope:epp.host.HostUpdateReply)
  })
_sym_db.RegisterMessage(HostUpdateReply)


# @@protoc_insertion_point(module_scope)
