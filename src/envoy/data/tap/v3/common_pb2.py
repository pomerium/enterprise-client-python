# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/data/tap/v3/common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x65nvoy/data/tap/v3/common.proto\x12\x11\x65nvoy.data.tap.v3\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"s\n\x04\x42ody\x12\x12\n\x08\x61s_bytes\x18\x01 \x01(\x0cH\x00\x12\x13\n\tas_string\x18\x02 \x01(\tH\x00\x12\x11\n\ttruncated\x18\x03 \x01(\x08:\"\x9a\xc5\x88\x1e\x1d\n\x1b\x65nvoy.data.tap.v2alpha.BodyB\x0b\n\tbody_typeBx\n\x1fio.envoyproxy.envoy.data.tap.v3B\x0b\x43ommonProtoP\x01Z>github.com/envoyproxy/go-control-plane/envoy/data/tap/v3;tapv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_BODY = DESCRIPTOR.message_types_by_name['Body']
Body = _reflection.GeneratedProtocolMessageType('Body', (_message.Message,), {
  'DESCRIPTOR' : _BODY,
  '__module__' : 'envoy.data.tap.v3.common_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.tap.v3.Body)
  })
_sym_db.RegisterMessage(Body)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037io.envoyproxy.envoy.data.tap.v3B\013CommonProtoP\001Z>github.com/envoyproxy/go-control-plane/envoy/data/tap/v3;tapv3\272\200\310\321\006\002\020\002'
  _BODY._options = None
  _BODY._serialized_options = b'\232\305\210\036\035\n\033envoy.data.tap.v2alpha.Body'
  _BODY._serialized_start=119
  _BODY._serialized_end=234
# @@protoc_insertion_point(module_scope)
