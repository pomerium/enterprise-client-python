# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xds/annotations/v3/migrate.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n xds/annotations/v3/migrate.proto\x12\x12xds.annotations.v3\x1a google/protobuf/descriptor.proto\"#\n\x11MigrateAnnotation\x12\x0e\n\x06rename\x18\x01 \x01(\t\"A\n\x16\x46ieldMigrateAnnotation\x12\x0e\n\x06rename\x18\x01 \x01(\t\x12\x17\n\x0foneof_promotion\x18\x02 \x01(\t\"0\n\x15\x46ileMigrateAnnotation\x12\x17\n\x0fmove_to_package\x18\x02 \x01(\t:b\n\x0fmessage_migrate\x12\x1f.google.protobuf.MessageOptions\x18\xce\xe9\xed\x35 \x01(\x0b\x32%.xds.annotations.v3.MigrateAnnotation:c\n\rfield_migrate\x12\x1d.google.protobuf.FieldOptions\x18\xce\xe9\xed\x35 \x01(\x0b\x32*.xds.annotations.v3.FieldMigrateAnnotation:\\\n\x0c\x65num_migrate\x12\x1c.google.protobuf.EnumOptions\x18\xce\xe9\xed\x35 \x01(\x0b\x32%.xds.annotations.v3.MigrateAnnotation:g\n\x12\x65num_value_migrate\x12!.google.protobuf.EnumValueOptions\x18\xce\xe9\xed\x35 \x01(\x0b\x32%.xds.annotations.v3.MigrateAnnotation:`\n\x0c\x66ile_migrate\x12\x1c.google.protobuf.FileOptions\x18\xce\xe9\xed\x35 \x01(\x0b\x32).xds.annotations.v3.FileMigrateAnnotationB+Z)github.com/cncf/xds/go/xds/annotations/v3b\x06proto3')


MESSAGE_MIGRATE_FIELD_NUMBER = 112948430
message_migrate = DESCRIPTOR.extensions_by_name['message_migrate']
FIELD_MIGRATE_FIELD_NUMBER = 112948430
field_migrate = DESCRIPTOR.extensions_by_name['field_migrate']
ENUM_MIGRATE_FIELD_NUMBER = 112948430
enum_migrate = DESCRIPTOR.extensions_by_name['enum_migrate']
ENUM_VALUE_MIGRATE_FIELD_NUMBER = 112948430
enum_value_migrate = DESCRIPTOR.extensions_by_name['enum_value_migrate']
FILE_MIGRATE_FIELD_NUMBER = 112948430
file_migrate = DESCRIPTOR.extensions_by_name['file_migrate']

_MIGRATEANNOTATION = DESCRIPTOR.message_types_by_name['MigrateAnnotation']
_FIELDMIGRATEANNOTATION = DESCRIPTOR.message_types_by_name['FieldMigrateAnnotation']
_FILEMIGRATEANNOTATION = DESCRIPTOR.message_types_by_name['FileMigrateAnnotation']
MigrateAnnotation = _reflection.GeneratedProtocolMessageType('MigrateAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _MIGRATEANNOTATION,
  '__module__' : 'xds.annotations.v3.migrate_pb2'
  # @@protoc_insertion_point(class_scope:xds.annotations.v3.MigrateAnnotation)
  })
_sym_db.RegisterMessage(MigrateAnnotation)

FieldMigrateAnnotation = _reflection.GeneratedProtocolMessageType('FieldMigrateAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _FIELDMIGRATEANNOTATION,
  '__module__' : 'xds.annotations.v3.migrate_pb2'
  # @@protoc_insertion_point(class_scope:xds.annotations.v3.FieldMigrateAnnotation)
  })
_sym_db.RegisterMessage(FieldMigrateAnnotation)

FileMigrateAnnotation = _reflection.GeneratedProtocolMessageType('FileMigrateAnnotation', (_message.Message,), {
  'DESCRIPTOR' : _FILEMIGRATEANNOTATION,
  '__module__' : 'xds.annotations.v3.migrate_pb2'
  # @@protoc_insertion_point(class_scope:xds.annotations.v3.FileMigrateAnnotation)
  })
_sym_db.RegisterMessage(FileMigrateAnnotation)

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(message_migrate)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_migrate)
  google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_migrate)
  google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enum_value_migrate)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(file_migrate)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cncf/xds/go/xds/annotations/v3'
  _MIGRATEANNOTATION._serialized_start=90
  _MIGRATEANNOTATION._serialized_end=125
  _FIELDMIGRATEANNOTATION._serialized_start=127
  _FIELDMIGRATEANNOTATION._serialized_end=192
  _FILEMIGRATEANNOTATION._serialized_start=194
  _FILEMIGRATEANNOTATION._serialized_end=242
# @@protoc_insertion_point(module_scope)
