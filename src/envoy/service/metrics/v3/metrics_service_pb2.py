# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/metrics/v3/metrics_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from io.prometheus.client import metrics_pb2 as io_dot_prometheus_dot_client_dot_metrics__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.envoy/service/metrics/v3/metrics_service.proto\x12\x18\x65nvoy.service.metrics.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a\"io/prometheus/client/metrics.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"N\n\x15StreamMetricsResponse:5\x9a\xc5\x88\x1e\x30\n.envoy.service.metrics.v2.StreamMetricsResponse\"\xda\x02\n\x14StreamMetricsMessage\x12M\n\nidentifier\x18\x01 \x01(\x0b\x32\x39.envoy.service.metrics.v3.StreamMetricsMessage.Identifier\x12\x39\n\renvoy_metrics\x18\x02 \x03(\x0b\x32\".io.prometheus.client.MetricFamily\x1a\x81\x01\n\nIdentifier\x12\x32\n\x04node\x18\x01 \x01(\x0b\x32\x1a.envoy.config.core.v3.NodeB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01:?\x9a\xc5\x88\x1e:\n8envoy.service.metrics.v2.StreamMetricsMessage.Identifier:4\x9a\xc5\x88\x1e/\n-envoy.service.metrics.v2.StreamMetricsMessage2\x86\x01\n\x0eMetricsService\x12t\n\rStreamMetrics\x12..envoy.service.metrics.v3.StreamMetricsMessage\x1a/.envoy.service.metrics.v3.StreamMetricsResponse\"\x00(\x01\x42\x95\x01\n&io.envoyproxy.envoy.service.metrics.v3B\x13MetricsServiceProtoP\x01ZIgithub.com/envoyproxy/go-control-plane/envoy/service/metrics/v3;metricsv3\x88\x01\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_STREAMMETRICSRESPONSE = DESCRIPTOR.message_types_by_name['StreamMetricsResponse']
_STREAMMETRICSMESSAGE = DESCRIPTOR.message_types_by_name['StreamMetricsMessage']
_STREAMMETRICSMESSAGE_IDENTIFIER = _STREAMMETRICSMESSAGE.nested_types_by_name['Identifier']
StreamMetricsResponse = _reflection.GeneratedProtocolMessageType('StreamMetricsResponse', (_message.Message,), {
  'DESCRIPTOR' : _STREAMMETRICSRESPONSE,
  '__module__' : 'envoy.service.metrics.v3.metrics_service_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.metrics.v3.StreamMetricsResponse)
  })
_sym_db.RegisterMessage(StreamMetricsResponse)

StreamMetricsMessage = _reflection.GeneratedProtocolMessageType('StreamMetricsMessage', (_message.Message,), {

  'Identifier' : _reflection.GeneratedProtocolMessageType('Identifier', (_message.Message,), {
    'DESCRIPTOR' : _STREAMMETRICSMESSAGE_IDENTIFIER,
    '__module__' : 'envoy.service.metrics.v3.metrics_service_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.metrics.v3.StreamMetricsMessage.Identifier)
    })
  ,
  'DESCRIPTOR' : _STREAMMETRICSMESSAGE,
  '__module__' : 'envoy.service.metrics.v3.metrics_service_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.metrics.v3.StreamMetricsMessage)
  })
_sym_db.RegisterMessage(StreamMetricsMessage)
_sym_db.RegisterMessage(StreamMetricsMessage.Identifier)

_METRICSSERVICE = DESCRIPTOR.services_by_name['MetricsService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&io.envoyproxy.envoy.service.metrics.v3B\023MetricsServiceProtoP\001ZIgithub.com/envoyproxy/go-control-plane/envoy/service/metrics/v3;metricsv3\210\001\001\272\200\310\321\006\002\020\002'
  _STREAMMETRICSRESPONSE._options = None
  _STREAMMETRICSRESPONSE._serialized_options = b'\232\305\210\0360\n.envoy.service.metrics.v2.StreamMetricsResponse'
  _STREAMMETRICSMESSAGE_IDENTIFIER.fields_by_name['node']._options = None
  _STREAMMETRICSMESSAGE_IDENTIFIER.fields_by_name['node']._serialized_options = b'\372B\005\212\001\002\020\001'
  _STREAMMETRICSMESSAGE_IDENTIFIER._options = None
  _STREAMMETRICSMESSAGE_IDENTIFIER._serialized_options = b'\232\305\210\036:\n8envoy.service.metrics.v2.StreamMetricsMessage.Identifier'
  _STREAMMETRICSMESSAGE._options = None
  _STREAMMETRICSMESSAGE._serialized_options = b'\232\305\210\036/\n-envoy.service.metrics.v2.StreamMetricsMessage'
  _STREAMMETRICSRESPONSE._serialized_start=236
  _STREAMMETRICSRESPONSE._serialized_end=314
  _STREAMMETRICSMESSAGE._serialized_start=317
  _STREAMMETRICSMESSAGE._serialized_end=663
  _STREAMMETRICSMESSAGE_IDENTIFIER._serialized_start=480
  _STREAMMETRICSMESSAGE_IDENTIFIER._serialized_end=609
  _METRICSSERVICE._serialized_start=666
  _METRICSSERVICE._serialized_end=800
# @@protoc_insertion_point(module_scope)
