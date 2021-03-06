# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udpa/annotations/security.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='udpa/annotations/security.proto',
  package='udpa.annotations',
  syntax='proto3',
  serialized_options=b'Z\"github.com/cncf/xds/go/annotations\272\200\310\321\006\002\010\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fudpa/annotations/security.proto\x12\x10udpa.annotations\x1a\x1dudpa/annotations/status.proto\x1a google/protobuf/descriptor.proto\"o\n\x17\x46ieldSecurityAnnotation\x12*\n\"configure_for_untrusted_downstream\x18\x01 \x01(\x08\x12(\n configure_for_untrusted_upstream\x18\x02 \x01(\x08:]\n\x08security\x12\x1d.google.protobuf.FieldOptions\x18\xb1\xf2\xa6\x05 \x01(\x0b\x32).udpa.annotations.FieldSecurityAnnotationB,Z\"github.com/cncf/xds/go/annotations\xba\x80\xc8\xd1\x06\x02\x08\x01\x62\x06proto3'
  ,
  dependencies=[udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


SECURITY_FIELD_NUMBER = 11122993
security = _descriptor.FieldDescriptor(
  name='security', full_name='udpa.annotations.security', index=0,
  number=11122993, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)


_FIELDSECURITYANNOTATION = _descriptor.Descriptor(
  name='FieldSecurityAnnotation',
  full_name='udpa.annotations.FieldSecurityAnnotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='configure_for_untrusted_downstream', full_name='udpa.annotations.FieldSecurityAnnotation.configure_for_untrusted_downstream', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='configure_for_untrusted_upstream', full_name='udpa.annotations.FieldSecurityAnnotation.configure_for_untrusted_upstream', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=118,
  serialized_end=229,
)

DESCRIPTOR.message_types_by_name['FieldSecurityAnnotation'] = _FIELDSECURITYANNOTATION
DESCRIPTOR.extensions_by_name['security'] = security
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FieldSecurityAnnotation = _reflection.GeneratedProtocolMessageType('FieldSecurityAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _FIELDSECURITYANNOTATION,
  '__module__' : 'udpa.annotations.security_pb2'
  # @@protoc_insertion_point(class_scope:udpa.annotations.FieldSecurityAnnotation)
  })
_sym_db.RegisterMessage(FieldSecurityAnnotation)

security.message_type = _FIELDSECURITYANNOTATION
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(security)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
