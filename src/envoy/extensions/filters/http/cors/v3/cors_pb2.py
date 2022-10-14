# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/http/cors/v3/cors.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.type.matcher.v3 import string_pb2 as envoy_dot_type_dot_matcher_dot_v3_dot_string__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0envoy/extensions/filters/http/cors/v3/cors.proto\x12%envoy.extensions.filters.http.cors.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a\"envoy/type/matcher/v3/string.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"4\n\x04\x43ors:,\x9a\xc5\x88\x1e\'\n%envoy.config.filter.http.cors.v2.Cors\"\xb5\x03\n\nCorsPolicy\x12G\n\x19\x61llow_origin_string_match\x18\x01 \x03(\x0b\x32$.envoy.type.matcher.v3.StringMatcher\x12\x15\n\rallow_methods\x18\x02 \x01(\t\x12\x15\n\rallow_headers\x18\x03 \x01(\t\x12\x16\n\x0e\x65xpose_headers\x18\x04 \x01(\t\x12\x0f\n\x07max_age\x18\x05 \x01(\t\x12\x35\n\x11\x61llow_credentials\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x46\n\x0e\x66ilter_enabled\x18\x07 \x01(\x0b\x32..envoy.config.core.v3.RuntimeFractionalPercent\x12\x46\n\x0eshadow_enabled\x18\x08 \x01(\x0b\x32..envoy.config.core.v3.RuntimeFractionalPercent\x12@\n\x1c\x61llow_private_network_access\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x9f\x01\n3io.envoyproxy.envoy.extensions.filters.http.cors.v3B\tCorsProtoP\x01ZSgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/cors/v3;corsv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_CORS = DESCRIPTOR.message_types_by_name['Cors']
_CORSPOLICY = DESCRIPTOR.message_types_by_name['CorsPolicy']
Cors = _reflection.GeneratedProtocolMessageType('Cors', (_message.Message,), {
  'DESCRIPTOR' : _CORS,
  '__module__' : 'envoy.extensions.filters.http.cors.v3.cors_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.cors.v3.Cors)
  })
_sym_db.RegisterMessage(Cors)

CorsPolicy = _reflection.GeneratedProtocolMessageType('CorsPolicy', (_message.Message,), {
  'DESCRIPTOR' : _CORSPOLICY,
  '__module__' : 'envoy.extensions.filters.http.cors.v3.cors_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.cors.v3.CorsPolicy)
  })
_sym_db.RegisterMessage(CorsPolicy)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n3io.envoyproxy.envoy.extensions.filters.http.cors.v3B\tCorsProtoP\001ZSgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/cors/v3;corsv3\272\200\310\321\006\002\020\002'
  _CORS._options = None
  _CORS._serialized_options = b'\232\305\210\036\'\n%envoy.config.filter.http.cors.v2.Cors'
  _CORS._serialized_start=258
  _CORS._serialized_end=310
  _CORSPOLICY._serialized_start=313
  _CORSPOLICY._serialized_end=750
# @@protoc_insertion_point(module_scope)
