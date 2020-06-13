# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rgp.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import fee_pb2 as fee__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rgp.proto',
  package='epp.rgp',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\trgp.proto\x12\x07\x65pp.rgp\x1a\tfee.proto\"\x1e\n\x0eRequestRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x94\x01\n\x0cRestoreReply\x12\x0f\n\x07pending\x18\x01 \x01(\x08\x12\x16\n\x0etransaction_id\x18\x05 \x01(\t\x12 \n\x05state\x18\x02 \x03(\x0e\x32\x11.epp.rgp.RGPState\x12\"\n\x08\x66\x65\x65_data\x18\x04 \x01(\x0b\x32\x10.epp.fee.FeeData\x12\x15\n\rregistry_name\x18\x03 \x01(\t*\x9d\x01\n\x08RGPState\x12\x0b\n\x07Unknown\x10\x00\x12\r\n\tAddPeriod\x10\x01\x12\x13\n\x0f\x41utoRenewPeriod\x10\x02\x12\x0f\n\x0bRenewPeriod\x10\x03\x12\x12\n\x0eTransferPeriod\x10\x04\x12\x14\n\x10RedemptionPeriod\x10\x05\x12\x12\n\x0ePendingRestore\x10\x06\x12\x11\n\rPendingDelete\x10\x07\x62\x06proto3'
  ,
  dependencies=[fee__pb2.DESCRIPTOR,])

_RGPSTATE = _descriptor.EnumDescriptor(
  name='RGPState',
  full_name='epp.rgp.RGPState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AddPeriod', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AutoRenewPeriod', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RenewPeriod', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TransferPeriod', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RedemptionPeriod', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PendingRestore', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PendingDelete', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=217,
  serialized_end=374,
)
_sym_db.RegisterEnumDescriptor(_RGPSTATE)

RGPState = enum_type_wrapper.EnumTypeWrapper(_RGPSTATE)
Unknown = 0
AddPeriod = 1
AutoRenewPeriod = 2
RenewPeriod = 3
TransferPeriod = 4
RedemptionPeriod = 5
PendingRestore = 6
PendingDelete = 7



_REQUESTREQUEST = _descriptor.Descriptor(
  name='RequestRequest',
  full_name='epp.rgp.RequestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='epp.rgp.RequestRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=33,
  serialized_end=63,
)


_RESTOREREPLY = _descriptor.Descriptor(
  name='RestoreReply',
  full_name='epp.rgp.RestoreReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pending', full_name='epp.rgp.RestoreReply.pending', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_id', full_name='epp.rgp.RestoreReply.transaction_id', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='epp.rgp.RestoreReply.state', index=2,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_data', full_name='epp.rgp.RestoreReply.fee_data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='registry_name', full_name='epp.rgp.RestoreReply.registry_name', index=4,
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
  serialized_start=66,
  serialized_end=214,
)

_RESTOREREPLY.fields_by_name['state'].enum_type = _RGPSTATE
_RESTOREREPLY.fields_by_name['fee_data'].message_type = fee__pb2._FEEDATA
DESCRIPTOR.message_types_by_name['RequestRequest'] = _REQUESTREQUEST
DESCRIPTOR.message_types_by_name['RestoreReply'] = _RESTOREREPLY
DESCRIPTOR.enum_types_by_name['RGPState'] = _RGPSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestRequest = _reflection.GeneratedProtocolMessageType('RequestRequest', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTREQUEST,
  '__module__' : 'rgp_pb2'
  # @@protoc_insertion_point(class_scope:epp.rgp.RequestRequest)
  })
_sym_db.RegisterMessage(RequestRequest)

RestoreReply = _reflection.GeneratedProtocolMessageType('RestoreReply', (_message.Message,), {
  'DESCRIPTOR' : _RESTOREREPLY,
  '__module__' : 'rgp_pb2'
  # @@protoc_insertion_point(class_scope:epp.rgp.RestoreReply)
  })
_sym_db.RegisterMessage(RestoreReply)


# @@protoc_insertion_point(module_scope)
