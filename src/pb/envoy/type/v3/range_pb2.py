# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/v3/range.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/v3/range.proto',
  package='envoy.type.v3',
  syntax='proto3',
  serialized_options=b'\n\033io.envoyproxy.envoy.type.v3B\nRangeProtoP\001\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x65nvoy/type/v3/range.proto\x12\renvoy.type.v3\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"F\n\nInt64Range\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03:\x1c\x9a\xc5\x88\x1e\x17\n\x15\x65nvoy.type.Int64Range\"F\n\nInt32Range\x12\r\n\x05start\x18\x01 \x01(\x05\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x05:\x1c\x9a\xc5\x88\x1e\x17\n\x15\x65nvoy.type.Int32Range\"H\n\x0b\x44oubleRange\x12\r\n\x05start\x18\x01 \x01(\x01\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x01:\x1d\x9a\xc5\x88\x1e\x18\n\x16\x65nvoy.type.DoubleRangeB3\n\x1bio.envoyproxy.envoy.type.v3B\nRangeProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,])




_INT64RANGE = _descriptor.Descriptor(
  name='Int64Range',
  full_name='envoy.type.v3.Int64Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='envoy.type.v3.Int64Range.start', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='envoy.type.v3.Int64Range.end', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036\027\n\025envoy.type.Int64Range',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=180,
)


_INT32RANGE = _descriptor.Descriptor(
  name='Int32Range',
  full_name='envoy.type.v3.Int32Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='envoy.type.v3.Int32Range.start', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='envoy.type.v3.Int32Range.end', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036\027\n\025envoy.type.Int32Range',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=252,
)


_DOUBLERANGE = _descriptor.Descriptor(
  name='DoubleRange',
  full_name='envoy.type.v3.DoubleRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='envoy.type.v3.DoubleRange.start', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end', full_name='envoy.type.v3.DoubleRange.end', index=1,
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
  serialized_options=b'\232\305\210\036\030\n\026envoy.type.DoubleRange',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=326,
)

DESCRIPTOR.message_types_by_name['Int64Range'] = _INT64RANGE
DESCRIPTOR.message_types_by_name['Int32Range'] = _INT32RANGE
DESCRIPTOR.message_types_by_name['DoubleRange'] = _DOUBLERANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Int64Range = _reflection.GeneratedProtocolMessageType('Int64Range', (_message.Message,), {
  'DESCRIPTOR' : _INT64RANGE,
  '__module__' : 'envoy.type.v3.range_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.v3.Int64Range)
  })
_sym_db.RegisterMessage(Int64Range)

Int32Range = _reflection.GeneratedProtocolMessageType('Int32Range', (_message.Message,), {
  'DESCRIPTOR' : _INT32RANGE,
  '__module__' : 'envoy.type.v3.range_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.v3.Int32Range)
  })
_sym_db.RegisterMessage(Int32Range)

DoubleRange = _reflection.GeneratedProtocolMessageType('DoubleRange', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLERANGE,
  '__module__' : 'envoy.type.v3.range_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.v3.DoubleRange)
  })
_sym_db.RegisterMessage(DoubleRange)


DESCRIPTOR._options = None
_INT64RANGE._options = None
_INT32RANGE._options = None
_DOUBLERANGE._options = None
# @@protoc_insertion_point(module_scope)
