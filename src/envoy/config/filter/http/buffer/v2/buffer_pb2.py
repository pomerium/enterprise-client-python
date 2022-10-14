# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/http/buffer/v2/buffer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/envoy/config/filter/http/buffer/v2/buffer.proto\x12\"envoy.config.filter.http.buffer.v2\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1eudpa/annotations/migrate.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"X\n\x06\x42uffer\x12H\n\x11max_request_bytes\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x0f\xfa\x42\x04*\x02 \x00\xfa\x42\x05\x8a\x01\x02\x10\x01J\x04\x08\x02\x10\x03\"\x86\x01\n\x0e\x42ufferPerRoute\x12\x1b\n\x08\x64isabled\x18\x01 \x01(\x08\x42\x07\xfa\x42\x04j\x02\x08\x01H\x00\x12\x46\n\x06\x62uffer\x18\x02 \x01(\x0b\x32*.envoy.config.filter.http.buffer.v2.BufferB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00\x42\x0f\n\x08override\x12\x03\xf8\x42\x01\x42\xcc\x01\n0io.envoyproxy.envoy.config.filter.http.buffer.v2B\x0b\x42ufferProtoP\x01ZRgithub.com/envoyproxy/go-control-plane/envoy/config/filter/http/buffer/v2;bufferv2\xf2\x98\xfe\x8f\x05)\x12\'envoy.extensions.filters.http.buffer.v3\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')



_BUFFER = DESCRIPTOR.message_types_by_name['Buffer']
_BUFFERPERROUTE = DESCRIPTOR.message_types_by_name['BufferPerRoute']
Buffer = _reflection.GeneratedProtocolMessageType('Buffer', (_message.Message,), {
  'DESCRIPTOR' : _BUFFER,
  '__module__' : 'envoy.config.filter.http.buffer.v2.buffer_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.buffer.v2.Buffer)
  })
_sym_db.RegisterMessage(Buffer)

BufferPerRoute = _reflection.GeneratedProtocolMessageType('BufferPerRoute', (_message.Message,), {
  'DESCRIPTOR' : _BUFFERPERROUTE,
  '__module__' : 'envoy.config.filter.http.buffer.v2.buffer_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.http.buffer.v2.BufferPerRoute)
  })
_sym_db.RegisterMessage(BufferPerRoute)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n0io.envoyproxy.envoy.config.filter.http.buffer.v2B\013BufferProtoP\001ZRgithub.com/envoyproxy/go-control-plane/envoy/config/filter/http/buffer/v2;bufferv2\362\230\376\217\005)\022\'envoy.extensions.filters.http.buffer.v3\272\200\310\321\006\002\020\001'
  _BUFFER.fields_by_name['max_request_bytes']._options = None
  _BUFFER.fields_by_name['max_request_bytes']._serialized_options = b'\372B\004*\002 \000\372B\005\212\001\002\020\001'
  _BUFFERPERROUTE.oneofs_by_name['override']._options = None
  _BUFFERPERROUTE.oneofs_by_name['override']._serialized_options = b'\370B\001'
  _BUFFERPERROUTE.fields_by_name['disabled']._options = None
  _BUFFERPERROUTE.fields_by_name['disabled']._serialized_options = b'\372B\004j\002\010\001'
  _BUFFERPERROUTE.fields_by_name['buffer']._options = None
  _BUFFERPERROUTE.fields_by_name['buffer']._serialized_options = b'\372B\005\212\001\002\020\001'
  _BUFFER._serialized_start=207
  _BUFFER._serialized_end=295
  _BUFFERPERROUTE._serialized_start=298
  _BUFFERPERROUTE._serialized_end=432
# @@protoc_insertion_point(module_scope)
