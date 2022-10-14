# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/metrics/v2/metrics_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import base_pb2 as envoy_dot_api_dot_v2_dot_core_dot_base__pb2
try:
  envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2 = envoy_dot_api_dot_v2_dot_core_dot_base__pb2.envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2
except AttributeError:
  envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2 = envoy_dot_api_dot_v2_dot_core_dot_base__pb2.envoy.api.v2.core.socket_option_pb2
from io.prometheus.client import metrics_pb2 as io_dot_prometheus_dot_client_dot_metrics__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.envoy/service/metrics/v2/metrics_service.proto\x12\x18\x65nvoy.service.metrics.v2\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a\"io/prometheus/client/metrics.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\x17\n\x15StreamMetricsResponse\"\xdf\x01\n\x14StreamMetricsMessage\x12M\n\nidentifier\x18\x01 \x01(\x0b\x32\x39.envoy.service.metrics.v2.StreamMetricsMessage.Identifier\x12\x39\n\renvoy_metrics\x18\x02 \x03(\x0b\x32\".io.prometheus.client.MetricFamily\x1a=\n\nIdentifier\x12/\n\x04node\x18\x01 \x01(\x0b\x32\x17.envoy.api.v2.core.NodeB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x32\x86\x01\n\x0eMetricsService\x12t\n\rStreamMetrics\x12..envoy.service.metrics.v2.StreamMetricsMessage\x1a/.envoy.service.metrics.v2.StreamMetricsResponse\"\x00(\x01\x42\x95\x01\n&io.envoyproxy.envoy.service.metrics.v2B\x13MetricsServiceProtoP\x01ZIgithub.com/envoyproxy/go-control-plane/envoy/service/metrics/v2;metricsv2\x88\x01\x01\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')



_STREAMMETRICSRESPONSE = DESCRIPTOR.message_types_by_name['StreamMetricsResponse']
_STREAMMETRICSMESSAGE = DESCRIPTOR.message_types_by_name['StreamMetricsMessage']
_STREAMMETRICSMESSAGE_IDENTIFIER = _STREAMMETRICSMESSAGE.nested_types_by_name['Identifier']
StreamMetricsResponse = _reflection.GeneratedProtocolMessageType('StreamMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMMETRICSRESPONSE,
  '__module__' : 'envoy.service.metrics.v2.metrics_service_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.metrics.v2.StreamMetricsResponse)
  })
_sym_db.RegisterMessage(StreamMetricsResponse)

StreamMetricsMessage = _reflection.GeneratedProtocolMessageType('StreamMetricsMessage', (_message.Message,), {

  'Identifier' : _reflection.GeneratedProtocolMessageType('Identifier', (_message.Message,), {
    'DESCRIPTOR' : _STREAMMETRICSMESSAGE_IDENTIFIER,
    '__module__' : 'envoy.service.metrics.v2.metrics_service_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.metrics.v2.StreamMetricsMessage.Identifier)
    })
  ,
  'DESCRIPTOR' : _STREAMMETRICSMESSAGE,
  '__module__' : 'envoy.service.metrics.v2.metrics_service_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.metrics.v2.StreamMetricsMessage)
  })
_sym_db.RegisterMessage(StreamMetricsMessage)
_sym_db.RegisterMessage(StreamMetricsMessage.Identifier)

_METRICSSERVICE = DESCRIPTOR.services_by_name['MetricsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&io.envoyproxy.envoy.service.metrics.v2B\023MetricsServiceProtoP\001ZIgithub.com/envoyproxy/go-control-plane/envoy/service/metrics/v2;metricsv2\210\001\001\272\200\310\321\006\002\020\001'
  _STREAMMETRICSMESSAGE_IDENTIFIER.fields_by_name['node']._options = None
  _STREAMMETRICSMESSAGE_IDENTIFIER.fields_by_name['node']._serialized_options = b'\372B\005\212\001\002\020\001'
  _STREAMMETRICSRESPONSE._serialized_start=198
  _STREAMMETRICSRESPONSE._serialized_end=221
  _STREAMMETRICSMESSAGE._serialized_start=224
  _STREAMMETRICSMESSAGE._serialized_end=447
  _STREAMMETRICSMESSAGE_IDENTIFIER._serialized_start=386
  _STREAMMETRICSMESSAGE_IDENTIFIER._serialized_end=447
  _METRICSSERVICE._serialized_start=450
  _METRICSSERVICE._serialized_end=584
# @@protoc_insertion_point(module_scope)
