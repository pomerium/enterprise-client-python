# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/http/grpc_stats/v3/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import grpc_method_list_pb2 as envoy_dot_config_dot_core_dot_v3_dot_grpc__method__list__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8envoy/extensions/filters/http/grpc_stats/v3/config.proto\x12+envoy.extensions.filters.http.grpc_stats.v3\x1a+envoy/config/core/v3/grpc_method_list.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"\xe1\x02\n\x0c\x46ilterConfig\x12\x19\n\x11\x65mit_filter_state\x18\x01 \x01(\x08\x12Q\n!individual_method_stats_allowlist\x18\x02 \x01(\x0b\x32$.envoy.config.core.v3.GrpcMethodListH\x00\x12;\n\x15stats_for_all_methods\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValueH\x00\x12\x1d\n\x15\x65nable_upstream_stats\x18\x04 \x01(\x08\x12)\n!replace_dots_in_grpc_service_name\x18\x05 \x01(\x08:?\x9a\xc5\x88\x1e:\n8envoy.config.filter.http.grpc_stats.v2alpha.FilterConfigB\x1b\n\x19per_method_stat_specifier\"\x8e\x01\n\x0c\x46ilterObject\x12\x1d\n\x15request_message_count\x18\x01 \x01(\x04\x12\x1e\n\x16response_message_count\x18\x02 \x01(\x04:?\x9a\xc5\x88\x1e:\n8envoy.config.filter.http.grpc_stats.v2alpha.FilterObjectB\xb3\x01\n9io.envoyproxy.envoy.extensions.filters.http.grpc_stats.v3B\x0b\x43onfigProtoP\x01Z_github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_stats/v3;grpc_statsv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_FILTERCONFIG = DESCRIPTOR.message_types_by_name['FilterConfig']
_FILTEROBJECT = DESCRIPTOR.message_types_by_name['FilterObject']
FilterConfig = _reflection.GeneratedProtocolMessageType('FilterConfig', (_message.Message,), {
  'DESCRIPTOR' : _FILTERCONFIG,
  '__module__' : 'envoy.extensions.filters.http.grpc_stats.v3.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.grpc_stats.v3.FilterConfig)
  })
_sym_db.RegisterMessage(FilterConfig)

FilterObject = _reflection.GeneratedProtocolMessageType('FilterObject', (_message.Message,), {
  'DESCRIPTOR' : _FILTEROBJECT,
  '__module__' : 'envoy.extensions.filters.http.grpc_stats.v3.config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.grpc_stats.v3.FilterObject)
  })
_sym_db.RegisterMessage(FilterObject)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n9io.envoyproxy.envoy.extensions.filters.http.grpc_stats.v3B\013ConfigProtoP\001Z_github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/grpc_stats/v3;grpc_statsv3\272\200\310\321\006\002\020\002'
  _FILTERCONFIG._options = None
  _FILTERCONFIG._serialized_options = b'\232\305\210\036:\n8envoy.config.filter.http.grpc_stats.v2alpha.FilterConfig'
  _FILTEROBJECT._options = None
  _FILTEROBJECT._serialized_options = b'\232\305\210\036:\n8envoy.config.filter.http.grpc_stats.v2alpha.FilterObject'
  _FILTERCONFIG._serialized_start=249
  _FILTERCONFIG._serialized_end=602
  _FILTEROBJECT._serialized_start=605
  _FILTEROBJECT._serialized_end=747
# @@protoc_insertion_point(module_scope)
