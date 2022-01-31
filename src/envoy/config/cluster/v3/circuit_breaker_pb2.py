# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/cluster/v3/circuit_breaker.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.type.v3 import percent_pb2 as envoy_dot_type_dot_v3_dot_percent__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/cluster/v3/circuit_breaker.proto',
  package='envoy.config.cluster.v3',
  syntax='proto3',
  serialized_options=b'\n%io.envoyproxy.envoy.config.cluster.v3B\023CircuitBreakerProtoP\001ZHgithub.com/envoyproxy/go-control-plane/envoy/config/cluster/v3;clusterv3\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n-envoy/config/cluster/v3/circuit_breaker.proto\x12\x17\x65nvoy.config.cluster.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a\x1b\x65nvoy/type/v3/percent.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xd8\x06\n\x0f\x43ircuitBreakers\x12G\n\nthresholds\x18\x01 \x03(\x0b\x32\x33.envoy.config.cluster.v3.CircuitBreakers.Thresholds\x1a\xce\x05\n\nThresholds\x12\x41\n\x08priority\x18\x01 \x01(\x0e\x32%.envoy.config.core.v3.RoutingPriorityB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x35\n\x0fmax_connections\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12:\n\x14max_pending_requests\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x32\n\x0cmax_requests\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x31\n\x0bmax_retries\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12U\n\x0cretry_budget\x18\x08 \x01(\x0b\x32?.envoy.config.cluster.v3.CircuitBreakers.Thresholds.RetryBudget\x12\x17\n\x0ftrack_remaining\x18\x06 \x01(\x08\x12:\n\x14max_connection_pools\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x1a\xbe\x01\n\x0bRetryBudget\x12.\n\x0e\x62udget_percent\x18\x01 \x01(\x0b\x32\x16.envoy.type.v3.Percent\x12;\n\x15min_retry_concurrency\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value:B\x9a\xc5\x88\x1e=\n;envoy.api.v2.cluster.CircuitBreakers.Thresholds.RetryBudget:6\x9a\xc5\x88\x1e\x31\n/envoy.api.v2.cluster.CircuitBreakers.Thresholds:+\x9a\xc5\x88\x1e&\n$envoy.api.v2.cluster.CircuitBreakersB\x90\x01\n%io.envoyproxy.envoy.config.cluster.v3B\x13\x43ircuitBreakerProtoP\x01ZHgithub.com/envoyproxy/go-control-plane/envoy/config/cluster/v3;clusterv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[envoy_dot_config_dot_core_dot_v3_dot_base__pb2.DESCRIPTOR,envoy_dot_type_dot_v3_dot_percent__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_CIRCUITBREAKERS_THRESHOLDS_RETRYBUDGET = _descriptor.Descriptor(
  name='RetryBudget',
  full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.RetryBudget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='budget_percent', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.RetryBudget.budget_percent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_retry_concurrency', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.RetryBudget.min_retry_concurrency', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036=\n;envoy.api.v2.cluster.CircuitBreakers.Thresholds.RetryBudget',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=825,
  serialized_end=1015,
)

_CIRCUITBREAKERS_THRESHOLDS = _descriptor.Descriptor(
  name='Thresholds',
  full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.priority', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\202\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_connections', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.max_connections', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_pending_requests', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.max_pending_requests', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_requests', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.max_requests', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_retries', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.max_retries', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='retry_budget', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.retry_budget', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='track_remaining', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.track_remaining', index=6,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_connection_pools', full_name='envoy.config.cluster.v3.CircuitBreakers.Thresholds.max_connection_pools', index=7,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CIRCUITBREAKERS_THRESHOLDS_RETRYBUDGET, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\0361\n/envoy.api.v2.cluster.CircuitBreakers.Thresholds',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=1071,
)

_CIRCUITBREAKERS = _descriptor.Descriptor(
  name='CircuitBreakers',
  full_name='envoy.config.cluster.v3.CircuitBreakers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='thresholds', full_name='envoy.config.cluster.v3.CircuitBreakers.thresholds', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CIRCUITBREAKERS_THRESHOLDS, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036&\n$envoy.api.v2.cluster.CircuitBreakers',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=260,
  serialized_end=1116,
)

_CIRCUITBREAKERS_THRESHOLDS_RETRYBUDGET.fields_by_name['budget_percent'].message_type = envoy_dot_type_dot_v3_dot_percent__pb2._PERCENT
_CIRCUITBREAKERS_THRESHOLDS_RETRYBUDGET.fields_by_name['min_retry_concurrency'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_CIRCUITBREAKERS_THRESHOLDS_RETRYBUDGET.containing_type = _CIRCUITBREAKERS_THRESHOLDS
_CIRCUITBREAKERS_THRESHOLDS.fields_by_name['priority'].enum_type = envoy_dot_config_dot_core_dot_v3_dot_base__pb2._ROUTINGPRIORITY
_CIRCUITBREAKERS_THRESHOLDS.fields_by_name['max_connections'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_CIRCUITBREAKERS_THRESHOLDS.fields_by_name['max_pending_requests'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_CIRCUITBREAKERS_THRESHOLDS.fields_by_name['max_requests'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_CIRCUITBREAKERS_THRESHOLDS.fields_by_name['max_retries'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_CIRCUITBREAKERS_THRESHOLDS.fields_by_name['retry_budget'].message_type = _CIRCUITBREAKERS_THRESHOLDS_RETRYBUDGET
_CIRCUITBREAKERS_THRESHOLDS.fields_by_name['max_connection_pools'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_CIRCUITBREAKERS_THRESHOLDS.containing_type = _CIRCUITBREAKERS
_CIRCUITBREAKERS.fields_by_name['thresholds'].message_type = _CIRCUITBREAKERS_THRESHOLDS
DESCRIPTOR.message_types_by_name['CircuitBreakers'] = _CIRCUITBREAKERS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CircuitBreakers = _reflection.GeneratedProtocolMessageType('CircuitBreakers', (_message.Message,), {

  'Thresholds' : _reflection.GeneratedProtocolMessageType('Thresholds', (_message.Message,), {

    'RetryBudget' : _reflection.GeneratedProtocolMessageType('RetryBudget', (_message.Message,), {
      'DESCRIPTOR' : _CIRCUITBREAKERS_THRESHOLDS_RETRYBUDGET,
      '__module__' : 'envoy.config.cluster.v3.circuit_breaker_pb2'
      # @@protoc_insertion_point(class_scope:envoy.config.cluster.v3.CircuitBreakers.Thresholds.RetryBudget)
      })
    ,
    'DESCRIPTOR' : _CIRCUITBREAKERS_THRESHOLDS,
    '__module__' : 'envoy.config.cluster.v3.circuit_breaker_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.cluster.v3.CircuitBreakers.Thresholds)
    })
  ,
  'DESCRIPTOR' : _CIRCUITBREAKERS,
  '__module__' : 'envoy.config.cluster.v3.circuit_breaker_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.cluster.v3.CircuitBreakers)
  })
_sym_db.RegisterMessage(CircuitBreakers)
_sym_db.RegisterMessage(CircuitBreakers.Thresholds)
_sym_db.RegisterMessage(CircuitBreakers.Thresholds.RetryBudget)


DESCRIPTOR._options = None
_CIRCUITBREAKERS_THRESHOLDS_RETRYBUDGET._options = None
_CIRCUITBREAKERS_THRESHOLDS.fields_by_name['priority']._options = None
_CIRCUITBREAKERS_THRESHOLDS._options = None
_CIRCUITBREAKERS._options = None
# @@protoc_insertion_point(module_scope)
