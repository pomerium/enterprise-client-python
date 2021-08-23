# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/core/v3/substitution_format_string.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.config.core.v3 import extension_pb2 as envoy_dot_config_dot_core_dot_v3_dot_extension__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/core/v3/substitution_format_string.proto',
  package='envoy.config.core.v3',
  syntax='proto3',
  serialized_options=b'\n\"io.envoyproxy.envoy.config.core.v3B\035SubstitutionFormatStringProtoP\001\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n5envoy/config/core/v3/substitution_format_string.proto\x12\x14\x65nvoy.config.core.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a$envoy/config/core/v3/extension.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xb8\x02\n\x18SubstitutionFormatString\x12\"\n\x0btext_format\x18\x01 \x01(\tB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0H\x00\x12\x38\n\x0bjson_format\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00\x12>\n\x12text_format_source\x18\x05 \x01(\x0b\x32 .envoy.config.core.v3.DataSourceH\x00\x12\x19\n\x11omit_empty_values\x18\x03 \x01(\x08\x12\x14\n\x0c\x63ontent_type\x18\x04 \x01(\t\x12>\n\nformatters\x18\x06 \x03(\x0b\x32*.envoy.config.core.v3.TypedExtensionConfigB\r\n\x06\x66ormat\x12\x03\xf8\x42\x01\x42M\n\"io.envoyproxy.envoy.config.core.v3B\x1dSubstitutionFormatStringProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[envoy_dot_config_dot_core_dot_v3_dot_base__pb2.DESCRIPTOR,envoy_dot_config_dot_core_dot_v3_dot_extension__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,envoy_dot_annotations_dot_deprecation__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_SUBSTITUTIONFORMATSTRING = _descriptor.Descriptor(
  name='SubstitutionFormatString',
  full_name='envoy.config.core.v3.SubstitutionFormatString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text_format', full_name='envoy.config.core.v3.SubstitutionFormatString.text_format', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001\222\307\206\330\004\0033.0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='json_format', full_name='envoy.config.core.v3.SubstitutionFormatString.json_format', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\212\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text_format_source', full_name='envoy.config.core.v3.SubstitutionFormatString.text_format_source', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='omit_empty_values', full_name='envoy.config.core.v3.SubstitutionFormatString.omit_empty_values', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='envoy.config.core.v3.SubstitutionFormatString.content_type', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='formatters', full_name='envoy.config.core.v3.SubstitutionFormatString.formatters', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
      name='format', full_name='envoy.config.core.v3.SubstitutionFormatString.format',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=274,
  serialized_end=586,
)

_SUBSTITUTIONFORMATSTRING.fields_by_name['json_format'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SUBSTITUTIONFORMATSTRING.fields_by_name['text_format_source'].message_type = envoy_dot_config_dot_core_dot_v3_dot_base__pb2._DATASOURCE
_SUBSTITUTIONFORMATSTRING.fields_by_name['formatters'].message_type = envoy_dot_config_dot_core_dot_v3_dot_extension__pb2._TYPEDEXTENSIONCONFIG
_SUBSTITUTIONFORMATSTRING.oneofs_by_name['format'].fields.append(
  _SUBSTITUTIONFORMATSTRING.fields_by_name['text_format'])
_SUBSTITUTIONFORMATSTRING.fields_by_name['text_format'].containing_oneof = _SUBSTITUTIONFORMATSTRING.oneofs_by_name['format']
_SUBSTITUTIONFORMATSTRING.oneofs_by_name['format'].fields.append(
  _SUBSTITUTIONFORMATSTRING.fields_by_name['json_format'])
_SUBSTITUTIONFORMATSTRING.fields_by_name['json_format'].containing_oneof = _SUBSTITUTIONFORMATSTRING.oneofs_by_name['format']
_SUBSTITUTIONFORMATSTRING.oneofs_by_name['format'].fields.append(
  _SUBSTITUTIONFORMATSTRING.fields_by_name['text_format_source'])
_SUBSTITUTIONFORMATSTRING.fields_by_name['text_format_source'].containing_oneof = _SUBSTITUTIONFORMATSTRING.oneofs_by_name['format']
DESCRIPTOR.message_types_by_name['SubstitutionFormatString'] = _SUBSTITUTIONFORMATSTRING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubstitutionFormatString = _reflection.GeneratedProtocolMessageType('SubstitutionFormatString', (_message.Message,), {
  'DESCRIPTOR' : _SUBSTITUTIONFORMATSTRING,
  '__module__' : 'envoy.config.core.v3.substitution_format_string_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.SubstitutionFormatString)
  })
_sym_db.RegisterMessage(SubstitutionFormatString)


DESCRIPTOR._options = None
_SUBSTITUTIONFORMATSTRING.oneofs_by_name['format']._options = None
_SUBSTITUTIONFORMATSTRING.fields_by_name['text_format']._options = None
_SUBSTITUTIONFORMATSTRING.fields_by_name['json_format']._options = None
# @@protoc_insertion_point(module_scope)