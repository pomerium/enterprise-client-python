# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/accesslog/v2/file.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$envoy/config/accesslog/v2/file.proto\x12\x19\x65nvoy.config.accesslog.v2\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1eudpa/annotations/migrate.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xb3\x01\n\rFileAccessLog\x12\x15\n\x04path\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\x12\x10\n\x06\x66ormat\x18\x02 \x01(\tH\x00\x12.\n\x0bjson_format\x18\x03 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x12\x34\n\x11typed_json_format\x18\x04 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x42\x13\n\x11\x61\x63\x63\x65ss_log_formatB\xbb\x01\n\'io.envoyproxy.envoy.config.accesslog.v2B\tFileProtoP\x01ZLgithub.com/envoyproxy/go-control-plane/envoy/config/accesslog/v2;accesslogv2\xf2\x98\xfe\x8f\x05)\x12\'envoy.extensions.access_loggers.file.v3\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')



_FILEACCESSLOG = DESCRIPTOR.message_types_by_name['FileAccessLog']
FileAccessLog = _reflection.GeneratedProtocolMessageType('FileAccessLog', (_message.Message,), {
  'DESCRIPTOR' : _FILEACCESSLOG,
  '__module__' : 'envoy.config.accesslog.v2.file_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.accesslog.v2.FileAccessLog)
  })
_sym_db.RegisterMessage(FileAccessLog)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'io.envoyproxy.envoy.config.accesslog.v2B\tFileProtoP\001ZLgithub.com/envoyproxy/go-control-plane/envoy/config/accesslog/v2;accesslogv2\362\230\376\217\005)\022\'envoy.extensions.access_loggers.file.v3\272\200\310\321\006\002\020\001'
  _FILEACCESSLOG.fields_by_name['path']._options = None
  _FILEACCESSLOG.fields_by_name['path']._serialized_options = b'\372B\004r\002 \001'
  _FILEACCESSLOG._serialized_start=186
  _FILEACCESSLOG._serialized_end=365
# @@protoc_insertion_point(module_scope)
