# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/request_id/uuid/v3/uuid.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.envoy/extensions/request_id/uuid/v3/uuid.proto\x12#envoy.extensions.request_id.uuid.v3\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\"\x93\x01\n\x13UuidRequestIdConfig\x12\x35\n\x11pack_trace_reason\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x45\n!use_request_id_for_trace_sampling\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x9b\x01\n1io.envoyproxy.envoy.extensions.request_id.uuid.v3B\tUuidProtoP\x01ZQgithub.com/envoyproxy/go-control-plane/envoy/extensions/request_id/uuid/v3;uuidv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_UUIDREQUESTIDCONFIG = DESCRIPTOR.message_types_by_name['UuidRequestIdConfig']
UuidRequestIdConfig = _reflection.GeneratedProtocolMessageType('UuidRequestIdConfig', (_message.Message,), {
  'DESCRIPTOR' : _UUIDREQUESTIDCONFIG,
  '__module__' : 'envoy.extensions.request_id.uuid.v3.uuid_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.request_id.uuid.v3.UuidRequestIdConfig)
  })
_sym_db.RegisterMessage(UuidRequestIdConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n1io.envoyproxy.envoy.extensions.request_id.uuid.v3B\tUuidProtoP\001ZQgithub.com/envoyproxy/go-control-plane/envoy/extensions/request_id/uuid/v3;uuidv3\272\200\310\321\006\002\020\002'
  _UUIDREQUESTIDCONFIG._serialized_start=151
  _UUIDREQUESTIDCONFIG._serialized_end=298
# @@protoc_insertion_point(module_scope)
