# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/v3/number.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.type.v3 import range_pb2 as envoy_dot_type_dot_v3_dot_range__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/v3/number.proto',
  package='envoy.type.matcher.v3',
  syntax='proto3',
  serialized_options=b'\n#io.envoyproxy.envoy.type.matcher.v3B\013NumberProtoP\001\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"envoy/type/matcher/v3/number.proto\x12\x15\x65nvoy.type.matcher.v3\x1a\x19\x65nvoy/type/v3/range.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\x8c\x01\n\rDoubleMatcher\x12+\n\x05range\x18\x01 \x01(\x0b\x32\x1a.envoy.type.v3.DoubleRangeH\x00\x12\x0f\n\x05\x65xact\x18\x02 \x01(\x01H\x00:\'\x9a\xc5\x88\x1e\"\n envoy.type.matcher.DoubleMatcherB\x14\n\rmatch_pattern\x12\x03\xf8\x42\x01\x42<\n#io.envoyproxy.envoy.type.matcher.v3B\x0bNumberProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[envoy_dot_type_dot_v3_dot_range__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_DOUBLEMATCHER = _descriptor.Descriptor(
  name='DoubleMatcher',
  full_name='envoy.type.matcher.v3.DoubleMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='range', full_name='envoy.type.matcher.v3.DoubleMatcher.range', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exact', full_name='envoy.type.matcher.v3.DoubleMatcher.exact', index=1,
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
  serialized_options=b'\232\305\210\036\"\n envoy.type.matcher.DoubleMatcher',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='match_pattern', full_name='envoy.type.matcher.v3.DoubleMatcher.match_pattern',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=180,
  serialized_end=320,
)

_DOUBLEMATCHER.fields_by_name['range'].message_type = envoy_dot_type_dot_v3_dot_range__pb2._DOUBLERANGE
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
  '__module__' : 'envoy.type.matcher.v3.number_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.DoubleMatcher)
  })
_sym_db.RegisterMessage(DoubleMatcher)


DESCRIPTOR._options = None
_DOUBLEMATCHER.oneofs_by_name['match_pattern']._options = None
_DOUBLEMATCHER._options = None
# @@protoc_insertion_point(module_scope)
