# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/http/grpc_http1_bridge/v3/config.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?envoy/extensions/filters/http/grpc_http1_bridge/v3/config.proto\x12\x32\x65nvoy.extensions.filters.http.grpc_http1_bridge.v3\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"g\n\x06\x43onfig\x12 \n\x18upgrade_protobuf_to_grpc\x18\x01 \x01(\x08:;\x9a\xc5\x88\x1e\x36\n4envoy.config.filter.http.grpc_http1_bridge.v2.ConfigB\xc8\x01\n@io.envoyproxy.envoy.extensions.filters.http.grpc_http1_bridge.v3B\x0b\x43onfigProtoP\x01Zmgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_http1_bridge/v3;grpc_http1_bridgev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'envoy.extensions.filters.http.grpc_http1_bridge.v3.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.grpc_http1_bridge.v3.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n@io.envoyproxy.envoy.extensions.filters.http.grpc_http1_bridge.v3B\013ConfigProtoP\001Zmgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_http1_bridge/v3;grpc_http1_bridgev3\272\200\310\321\006\002\020\002'
  _CONFIG._options = None
  _CONFIG._serialized_options = b'\232\305\210\0366\n4envoy.config.filter.http.grpc_http1_bridge.v2.Config'
  _CONFIG._serialized_start=185
  _CONFIG._serialized_end=288
# @@protoc_insertion_point(module_scope)
