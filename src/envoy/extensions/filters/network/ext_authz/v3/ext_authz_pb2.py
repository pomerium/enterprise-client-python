# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/network/ext_authz/v3/ext_authz.proto
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
from envoy.type.matcher.v3 import metadata_pb2 as envoy_dot_type_dot_matcher_dot_v3_dot_metadata__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=envoy/extensions/filters/network/ext_authz/v3/ext_authz.proto\x12-envoy.extensions.filters.network.ext_authz.v3\x1a(envoy/config/core/v3/config_source.proto\x1a\'envoy/config/core/v3/grpc_service.proto\x1a$envoy/type/matcher/v3/metadata.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\x94\x03\n\x08\x45xtAuthz\x12\x1c\n\x0bstat_prefix\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x37\n\x0cgrpc_service\x18\x02 \x01(\x0b\x32!.envoy.config.core.v3.GrpcService\x12\x1a\n\x12\x66\x61ilure_mode_allow\x18\x03 \x01(\x08\x12 \n\x18include_peer_certificate\x18\x04 \x01(\x08\x12I\n\x15transport_api_version\x18\x05 \x01(\x0e\x32 .envoy.config.core.v3.ApiVersionB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12G\n\x17\x66ilter_enabled_metadata\x18\x06 \x01(\x0b\x32&.envoy.type.matcher.v3.MetadataMatcher\x12%\n\x1d\x62ootstrap_metadata_labels_key\x18\x07 \x01(\t:8\x9a\xc5\x88\x1e\x33\n1envoy.config.filter.network.ext_authz.v2.ExtAuthzB\xb8\x01\n;io.envoyproxy.envoy.extensions.filters.network.ext_authz.v3B\rExtAuthzProtoP\x01Z`github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/ext_authz/v3;ext_authzv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_EXTAUTHZ = DESCRIPTOR.message_types_by_name['ExtAuthz']
ExtAuthz = _reflection.GeneratedProtocolMessageType('ExtAuthz', (_message.Message,), {
  'DESCRIPTOR' : _EXTAUTHZ,
  '__module__' : 'envoy.extensions.filters.network.ext_authz.v3.ext_authz_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.network.ext_authz.v3.ExtAuthz)
  })
_sym_db.RegisterMessage(ExtAuthz)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n;io.envoyproxy.envoy.extensions.filters.network.ext_authz.v3B\rExtAuthzProtoP\001Z`github.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/ext_authz/v3;ext_authzv3\272\200\310\321\006\002\020\002'
  _EXTAUTHZ.fields_by_name['stat_prefix']._options = None
  _EXTAUTHZ.fields_by_name['stat_prefix']._serialized_options = b'\372B\004r\002\020\001'
  _EXTAUTHZ.fields_by_name['transport_api_version']._options = None
  _EXTAUTHZ.fields_by_name['transport_api_version']._serialized_options = b'\372B\005\202\001\002\020\001'
  _EXTAUTHZ._options = None
  _EXTAUTHZ._serialized_options = b'\232\305\210\0363\n1envoy.config.filter.network.ext_authz.v2.ExtAuthz'
  _EXTAUTHZ._serialized_start=325
  _EXTAUTHZ._serialized_end=729
# @@protoc_insertion_point(module_scope)
