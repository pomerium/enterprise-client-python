# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/annotations/deprecation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#envoy/annotations/deprecation.proto\x12\x11\x65nvoy.annotations\x1a google/protobuf/descriptor.proto:?\n\x15\x64isallowed_by_default\x12\x1d.google.protobuf.FieldOptions\x18\xe7\xad\xaeZ \x01(\x08:E\n\x1b\x64\x65precated_at_minor_version\x12\x1d.google.protobuf.FieldOptions\x18\xf2\xe8\x80K \x01(\t:H\n\x1a\x64isallowed_by_default_enum\x12!.google.protobuf.EnumValueOptions\x18\xf5\xce\xb6! \x01(\x08:N\n deprecated_at_minor_version_enum\x12!.google.protobuf.EnumValueOptions\x18\xc1\xbe\xb3V \x01(\tB:Z8github.com/envoyproxy/go-control-plane/envoy/annotationsb\x06proto3')


DISALLOWED_BY_DEFAULT_FIELD_NUMBER = 189503207
disallowed_by_default = DESCRIPTOR.extensions_by_name['disallowed_by_default']
DEPRECATED_AT_MINOR_VERSION_FIELD_NUMBER = 157299826
deprecated_at_minor_version = DESCRIPTOR.extensions_by_name['deprecated_at_minor_version']
DISALLOWED_BY_DEFAULT_ENUM_FIELD_NUMBER = 70100853
disallowed_by_default_enum = DESCRIPTOR.extensions_by_name['disallowed_by_default_enum']
DEPRECATED_AT_MINOR_VERSION_ENUM_FIELD_NUMBER = 181198657
deprecated_at_minor_version_enum = DESCRIPTOR.extensions_by_name['deprecated_at_minor_version_enum']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(disallowed_by_default)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(deprecated_at_minor_version)
  google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(disallowed_by_default_enum)
  google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(deprecated_at_minor_version_enum)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/envoyproxy/go-control-plane/envoy/annotations'
# @@protoc_insertion_point(module_scope)
