# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udpa/annotations/versioning.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='udpa/annotations/versioning.proto',
  package='udpa.annotations',
  syntax='proto3',
  serialized_options=b'Z\"github.com/cncf/xds/go/annotations',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!udpa/annotations/versioning.proto\x12\x10udpa.annotations\x1a google/protobuf/descriptor.proto\"5\n\x14VersioningAnnotation\x12\x1d\n\x15previous_message_type\x18\x01 \x01(\t:^\n\nversioning\x12\x1f.google.protobuf.MessageOptions\x18\xd3\x88\xe1\x03 \x01(\x0b\x32&.udpa.annotations.VersioningAnnotationB$Z\"github.com/cncf/xds/go/annotationsb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


VERSIONING_FIELD_NUMBER = 7881811
versioning = _descriptor.FieldDescriptor(
  name='versioning', full_name='udpa.annotations.versioning', index=0,
  number=7881811, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_VERSIONINGANNOTATION = _descriptor.Descriptor(
  name='VersioningAnnotation',
  full_name='udpa.annotations.VersioningAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='previous_message_type', full_name='udpa.annotations.VersioningAnnotation.previous_message_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  ],
  serialized_start=89,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['VersioningAnnotation'] = _VERSIONINGANNOTATION
DESCRIPTOR.extensions_by_name['versioning'] = versioning
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VersioningAnnotation = _reflection.GeneratedProtocolMessageType('VersioningAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _VERSIONINGANNOTATION,
  '__module__' : 'udpa.annotations.versioning_pb2'
  # @@protoc_insertion_point(class_scope:udpa.annotations.VersioningAnnotation)
  })
_sym_db.RegisterMessage(VersioningAnnotation)

versioning.message_type = _VERSIONINGANNOTATION
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(versioning)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
