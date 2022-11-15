# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/metrics/v3/metrics_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import config_source_pb2 as envoy_dot_config_dot_core_dot_v3_dot_config__source__pb2
from envoy.config.core.v3 import grpc_service_pb2 as envoy_dot_config_dot_core_dot_v3_dot_grpc__service__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-envoy/config/metrics/v3/metrics_service.proto\x12\x17\x65nvoy.config.metrics.v3\x1a(envoy/config/core/v3/config_source.proto\x1a\'envoy/config/core/v3/grpc_service.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xb5\x02\n\x14MetricsServiceConfig\x12\x41\n\x0cgrpc_service\x18\x01 \x01(\x0b\x32!.envoy.config.core.v3.GrpcServiceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12I\n\x15transport_api_version\x18\x03 \x01(\x0e\x32 .envoy.config.core.v3.ApiVersionB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12=\n\x19report_counters_as_deltas\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x1b\n\x13\x65mit_tags_as_labels\x18\x04 \x01(\x08:3\x9a\xc5\x88\x1e.\n,envoy.config.metrics.v2.MetricsServiceConfigB\x90\x01\n%io.envoyproxy.envoy.config.metrics.v3B\x13MetricsServiceProtoP\x01ZHgithub.com/envoyproxy/go-control-plane/envoy/config/metrics/v3;metricsv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_METRICSSERVICECONFIG = DESCRIPTOR.message_types_by_name['MetricsServiceConfig']
MetricsServiceConfig = _reflection.GeneratedProtocolMessageType('MetricsServiceConfig', (_message.Message,), {
  'DESCRIPTOR' : _METRICSSERVICECONFIG,
  '__module__' : 'envoy.config.metrics.v3.metrics_service_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.metrics.v3.MetricsServiceConfig)
  })
_sym_db.RegisterMessage(MetricsServiceConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%io.envoyproxy.envoy.config.metrics.v3B\023MetricsServiceProtoP\001ZHgithub.com/envoyproxy/go-control-plane/envoy/config/metrics/v3;metricsv3\272\200\310\321\006\002\020\002'
  _METRICSSERVICECONFIG.fields_by_name['grpc_service']._options = None
  _METRICSSERVICECONFIG.fields_by_name['grpc_service']._serialized_options = b'\372B\005\212\001\002\020\001'
  _METRICSSERVICECONFIG.fields_by_name['transport_api_version']._options = None
  _METRICSSERVICECONFIG.fields_by_name['transport_api_version']._serialized_options = b'\372B\005\202\001\002\020\001'
  _METRICSSERVICECONFIG._options = None
  _METRICSSERVICECONFIG._serialized_options = b'\232\305\210\036.\n,envoy.config.metrics.v2.MetricsServiceConfig'
  _METRICSSERVICECONFIG._serialized_start=281
  _METRICSSERVICECONFIG._serialized_end=590
# @@protoc_insertion_point(module_scope)
