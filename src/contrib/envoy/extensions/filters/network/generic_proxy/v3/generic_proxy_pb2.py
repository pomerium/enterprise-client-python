# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contrib/envoy/extensions/filters/network/generic_proxy/v3/generic_proxy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from contrib.envoy.extensions.filters.network.generic_proxy.v3 import route_pb2 as contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_generic__proxy_dot_v3_dot_route__pb2
from envoy.config.core.v3 import config_source_pb2 as envoy_dot_config_dot_core_dot_v3_dot_config__source__pb2
from envoy.config.core.v3 import extension_pb2 as envoy_dot_config_dot_core_dot_v3_dot_extension__pb2
from xds.annotations.v3 import status_pb2 as xds_dot_annotations_dot_v3_dot_status__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMcontrib/envoy/extensions/filters/network/generic_proxy/v3/generic_proxy.proto\x12\x31\x65nvoy.extensions.filters.network.generic_proxy.v3\x1a\x45\x63ontrib/envoy/extensions/filters/network/generic_proxy/v3/route.proto\x1a(envoy/config/core/v3/config_source.proto\x1a$envoy/config/core/v3/extension.proto\x1a\x1fxds/annotations/v3/status.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\x82\x03\n\x0cGenericProxy\x12\x1c\n\x0bstat_prefix\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12J\n\x0c\x63odec_config\x18\x02 \x01(\x0b\x32*.envoy.config.core.v3.TypedExtensionConfigB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12T\n\x0bgeneric_rds\x18\x03 \x01(\x0b\x32=.envoy.extensions.filters.network.generic_proxy.v3.GenericRdsH\x00\x12]\n\x0croute_config\x18\x04 \x01(\x0b\x32\x45.envoy.extensions.filters.network.generic_proxy.v3.RouteConfigurationH\x00\x12;\n\x07\x66ilters\x18\x05 \x03(\x0b\x32*.envoy.config.core.v3.TypedExtensionConfigB\x16\n\x0froute_specifier\x12\x03\xf8\x42\x01\"u\n\nGenericRds\x12\x43\n\rconfig_source\x18\x01 \x01(\x0b\x32\".envoy.config.core.v3.ConfigSourceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\"\n\x11route_config_name\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x42\xd0\x01\n?io.envoyproxy.envoy.extensions.filters.network.generic_proxy.v3B\x11GenericProxyProtoP\x01Zhgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/v3;generic_proxyv3\xba\x80\xc8\xd1\x06\x02\x10\x02\xd2\xc6\xa4\xe1\x06\x02\x08\x01\x62\x06proto3')



_GENERICPROXY = DESCRIPTOR.message_types_by_name['GenericProxy']
_GENERICRDS = DESCRIPTOR.message_types_by_name['GenericRds']
GenericProxy = _reflection.GeneratedProtocolMessageType('GenericProxy', (_message.Message,), {
  'DESCRIPTOR' : _GENERICPROXY,
  '__module__' : 'contrib.envoy.extensions.filters.network.generic_proxy.v3.generic_proxy_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.network.generic_proxy.v3.GenericProxy)
  })
_sym_db.RegisterMessage(GenericProxy)

GenericRds = _reflection.GeneratedProtocolMessageType('GenericRds', (_message.Message,), {
  'DESCRIPTOR' : _GENERICRDS,
  '__module__' : 'contrib.envoy.extensions.filters.network.generic_proxy.v3.generic_proxy_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.network.generic_proxy.v3.GenericRds)
  })
_sym_db.RegisterMessage(GenericRds)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n?io.envoyproxy.envoy.extensions.filters.network.generic_proxy.v3B\021GenericProxyProtoP\001Zhgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/v3;generic_proxyv3\272\200\310\321\006\002\020\002\322\306\244\341\006\002\010\001'
  _GENERICPROXY.oneofs_by_name['route_specifier']._options = None
  _GENERICPROXY.oneofs_by_name['route_specifier']._serialized_options = b'\370B\001'
  _GENERICPROXY.fields_by_name['stat_prefix']._options = None
  _GENERICPROXY.fields_by_name['stat_prefix']._serialized_options = b'\372B\004r\002\020\001'
  _GENERICPROXY.fields_by_name['codec_config']._options = None
  _GENERICPROXY.fields_by_name['codec_config']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GENERICRDS.fields_by_name['config_source']._options = None
  _GENERICRDS.fields_by_name['config_source']._serialized_options = b'\372B\005\212\001\002\020\001'
  _GENERICRDS.fields_by_name['route_config_name']._options = None
  _GENERICRDS.fields_by_name['route_config_name']._serialized_options = b'\372B\004r\002\020\001'
  _GENERICPROXY._serialized_start=373
  _GENERICPROXY._serialized_end=759
  _GENERICRDS._serialized_start=761
  _GENERICRDS._serialized_end=878
# @@protoc_insertion_point(module_scope)
