# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/annotations/deprecation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/annotations/deprecation.proto',
  package='envoy.annotations',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#envoy/annotations/deprecation.proto\x12\x11\x65nvoy.annotations\x1a google/protobuf/descriptor.proto:?\n\x15\x64isallowed_by_default\x12\x1d.google.protobuf.FieldOptions\x18\xe7\xad\xaeZ \x01(\x08:E\n\x1b\x64\x65precated_at_minor_version\x12\x1d.google.protobuf.FieldOptions\x18\xf2\xe8\x80K \x01(\t:H\n\x1a\x64isallowed_by_default_enum\x12!.google.protobuf.EnumValueOptions\x18\xf5\xce\xb6! \x01(\x08:N\n deprecated_at_minor_version_enum\x12!.google.protobuf.EnumValueOptions\x18\xc1\xbe\xb3V \x01(\tb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


DISALLOWED_BY_DEFAULT_FIELD_NUMBER = 189503207
disallowed_by_default = _descriptor.FieldDescriptor(
  name='disallowed_by_default', full_name='envoy.annotations.disallowed_by_default', index=0,
  number=189503207, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
DEPRECATED_AT_MINOR_VERSION_FIELD_NUMBER = 157299826
deprecated_at_minor_version = _descriptor.FieldDescriptor(
  name='deprecated_at_minor_version', full_name='envoy.annotations.deprecated_at_minor_version', index=1,
  number=157299826, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
DISALLOWED_BY_DEFAULT_ENUM_FIELD_NUMBER = 70100853
disallowed_by_default_enum = _descriptor.FieldDescriptor(
  name='disallowed_by_default_enum', full_name='envoy.annotations.disallowed_by_default_enum', index=2,
  number=70100853, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
DEPRECATED_AT_MINOR_VERSION_ENUM_FIELD_NUMBER = 181198657
deprecated_at_minor_version_enum = _descriptor.FieldDescriptor(
  name='deprecated_at_minor_version_enum', full_name='envoy.annotations.deprecated_at_minor_version_enum', index=3,
  number=181198657, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

DESCRIPTOR.extensions_by_name['disallowed_by_default'] = disallowed_by_default
DESCRIPTOR.extensions_by_name['deprecated_at_minor_version'] = deprecated_at_minor_version
DESCRIPTOR.extensions_by_name['disallowed_by_default_enum'] = disallowed_by_default_enum
DESCRIPTOR.extensions_by_name['deprecated_at_minor_version_enum'] = deprecated_at_minor_version_enum
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(disallowed_by_default)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(deprecated_at_minor_version)
google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(disallowed_by_default_enum)
google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(deprecated_at_minor_version_enum)

# @@protoc_insertion_point(module_scope)
