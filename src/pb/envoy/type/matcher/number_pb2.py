# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/number.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.type import range_pb2 as envoy_dot_type_dot_range__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/number.proto',
  package='envoy.type.matcher',
  syntax='proto3',
  serialized_options=b'\n io.envoyproxy.envoy.type.matcherB\013NumberProtoP\001\272\200\310\321\006\002\020\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1f\x65nvoy/type/matcher/number.proto\x12\x12\x65nvoy.type.matcher\x1a\x16\x65nvoy/type/range.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"`\n\rDoubleMatcher\x12(\n\x05range\x18\x01 \x01(\x0b\x32\x17.envoy.type.DoubleRangeH\x00\x12\x0f\n\x05\x65xact\x18\x02 \x01(\x01H\x00\x42\x14\n\rmatch_pattern\x12\x03\xf8\x42\x01\x42\x39\n io.envoyproxy.envoy.type.matcherB\x0bNumberProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3'
  ,
  dependencies=[envoy_dot_type_dot_range__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_DOUBLEMATCHER = _descriptor.Descriptor(
  name='DoubleMatcher',
  full_name='envoy.type.matcher.DoubleMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='range', full_name='envoy.type.matcher.DoubleMatcher.range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exact', full_name='envoy.type.matcher.DoubleMatcher.exact', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='match_pattern', full_name='envoy.type.matcher.DoubleMatcher.match_pattern',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=135,
  serialized_end=231,
)

_DOUBLEMATCHER.fields_by_name['range'].message_type = envoy_dot_type_dot_range__pb2._DOUBLERANGE
_DOUBLEMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _DOUBLEMATCHER.fields_by_name['range'])
_DOUBLEMATCHER.fields_by_name['range'].containing_oneof = _DOUBLEMATCHER.oneofs_by_name['match_pattern']
_DOUBLEMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _DOUBLEMATCHER.fields_by_name['exact'])
_DOUBLEMATCHER.fields_by_name['exact'].containing_oneof = _DOUBLEMATCHER.oneofs_by_name['match_pattern']
DESCRIPTOR.message_types_by_name['DoubleMatcher'] = _DOUBLEMATCHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DoubleMatcher = _reflection.GeneratedProtocolMessageType('DoubleMatcher', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLEMATCHER,
  '__module__' : 'envoy.type.matcher.number_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.DoubleMatcher)
  })
_sym_db.RegisterMessage(DoubleMatcher)


DESCRIPTOR._options = None
_DOUBLEMATCHER.oneofs_by_name['match_pattern']._options = None
# @@protoc_insertion_point(module_scope)
