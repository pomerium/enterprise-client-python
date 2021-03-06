# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/v3/hash_policy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/v3/hash_policy.proto',
  package='envoy.type.v3',
  syntax='proto3',
  serialized_options=b'\n\033io.envoyproxy.envoy.type.v3B\017HashPolicyProtoP\001Z;github.com/envoyproxy/go-control-plane/envoy/type/v3;typev3\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x65nvoy/type/v3/hash_policy.proto\x12\renvoy.type.v3\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\x93\x02\n\nHashPolicy\x12\x37\n\tsource_ip\x18\x01 \x01(\x0b\x32\".envoy.type.v3.HashPolicy.SourceIpH\x00\x12=\n\x0c\x66ilter_state\x18\x02 \x01(\x0b\x32%.envoy.type.v3.HashPolicy.FilterStateH\x00\x1a\x31\n\x08SourceIp:%\x9a\xc5\x88\x1e \n\x1e\x65nvoy.type.HashPolicy.SourceIp\x1a#\n\x0b\x46ilterState\x12\x14\n\x03key\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01:\x1c\x9a\xc5\x88\x1e\x17\n\x15\x65nvoy.type.HashPolicyB\x17\n\x10policy_specifier\x12\x03\xf8\x42\x01\x42u\n\x1bio.envoyproxy.envoy.type.v3B\x0fHashPolicyProtoP\x01Z;github.com/envoyproxy/go-control-plane/envoy/type/v3;typev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_HASHPOLICY_SOURCEIP = _descriptor.Descriptor(
  name='SourceIp',
  full_name='envoy.type.v3.HashPolicy.SourceIp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036 \n\036envoy.type.HashPolicy.SourceIp',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=325,
)

_HASHPOLICY_FILTERSTATE = _descriptor.Descriptor(
  name='FilterState',
  full_name='envoy.type.v3.HashPolicy.FilterState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.type.v3.HashPolicy.FilterState.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=327,
  serialized_end=362,
)

_HASHPOLICY = _descriptor.Descriptor(
  name='HashPolicy',
  full_name='envoy.type.v3.HashPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_ip', full_name='envoy.type.v3.HashPolicy.source_ip', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter_state', full_name='envoy.type.v3.HashPolicy.filter_state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HASHPOLICY_SOURCEIP, _HASHPOLICY_FILTERSTATE, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036\027\n\025envoy.type.HashPolicy',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='policy_specifier', full_name='envoy.type.v3.HashPolicy.policy_specifier',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=142,
  serialized_end=417,
)

_HASHPOLICY_SOURCEIP.containing_type = _HASHPOLICY
_HASHPOLICY_FILTERSTATE.containing_type = _HASHPOLICY
_HASHPOLICY.fields_by_name['source_ip'].message_type = _HASHPOLICY_SOURCEIP
_HASHPOLICY.fields_by_name['filter_state'].message_type = _HASHPOLICY_FILTERSTATE
_HASHPOLICY.oneofs_by_name['policy_specifier'].fields.append(
  _HASHPOLICY.fields_by_name['source_ip'])
_HASHPOLICY.fields_by_name['source_ip'].containing_oneof = _HASHPOLICY.oneofs_by_name['policy_specifier']
_HASHPOLICY.oneofs_by_name['policy_specifier'].fields.append(
  _HASHPOLICY.fields_by_name['filter_state'])
_HASHPOLICY.fields_by_name['filter_state'].containing_oneof = _HASHPOLICY.oneofs_by_name['policy_specifier']
DESCRIPTOR.message_types_by_name['HashPolicy'] = _HASHPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HashPolicy = _reflection.GeneratedProtocolMessageType('HashPolicy', (_message.Message,), {

  'SourceIp' : _reflection.GeneratedProtocolMessageType('SourceIp', (_message.Message,), {
    'DESCRIPTOR' : _HASHPOLICY_SOURCEIP,
    '__module__' : 'envoy.type.v3.hash_policy_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.v3.HashPolicy.SourceIp)
    })
  ,

  'FilterState' : _reflection.GeneratedProtocolMessageType('FilterState', (_message.Message,), {
    'DESCRIPTOR' : _HASHPOLICY_FILTERSTATE,
    '__module__' : 'envoy.type.v3.hash_policy_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.v3.HashPolicy.FilterState)
    })
  ,
  'DESCRIPTOR' : _HASHPOLICY,
  '__module__' : 'envoy.type.v3.hash_policy_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.v3.HashPolicy)
  })
_sym_db.RegisterMessage(HashPolicy)
_sym_db.RegisterMessage(HashPolicy.SourceIp)
_sym_db.RegisterMessage(HashPolicy.FilterState)


DESCRIPTOR._options = None
_HASHPOLICY_SOURCEIP._options = None
_HASHPOLICY_FILTERSTATE.fields_by_name['key']._options = None
_HASHPOLICY.oneofs_by_name['policy_specifier']._options = None
_HASHPOLICY._options = None
# @@protoc_insertion_point(module_scope)
