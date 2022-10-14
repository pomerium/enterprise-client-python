# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/network/http_connection_manager/v2/http_connection_manager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import config_source_pb2 as envoy_dot_api_dot_v2_dot_core_dot_config__source__pb2
from envoy.api.v2.core import protocol_pb2 as envoy_dot_api_dot_v2_dot_core_dot_protocol__pb2
from envoy.api.v2 import route_pb2 as envoy_dot_api_dot_v2_dot_route__pb2
from envoy.api.v2 import scoped_route_pb2 as envoy_dot_api_dot_v2_dot_scoped__route__pb2
from envoy.config.filter.accesslog.v2 import accesslog_pb2 as envoy_dot_config_dot_filter_dot_accesslog_dot_v2_dot_accesslog__pb2
from envoy.config.trace.v2 import http_tracer_pb2 as envoy_dot_config_dot_trace_dot_v2_dot_http__tracer__pb2
from envoy.type import percent_pb2 as envoy_dot_type_dot_percent__pb2
from envoy.type.tracing.v2 import custom_tag_pb2 as envoy_dot_type_dot_tracing_dot_v2_dot_custom__tag__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nTenvoy/config/filter/network/http_connection_manager/v2/http_connection_manager.proto\x12\x36\x65nvoy.config.filter.network.http_connection_manager.v2\x1a%envoy/api/v2/core/config_source.proto\x1a envoy/api/v2/core/protocol.proto\x1a\x18\x65nvoy/api/v2/route.proto\x1a\x1f\x65nvoy/api/v2/scoped_route.proto\x1a\x30\x65nvoy/config/filter/accesslog/v2/accesslog.proto\x1a\'envoy/config/trace/v2/http_tracer.proto\x1a\x18\x65nvoy/type/percent.proto\x1a&envoy/type/tracing/v2/custom_tag.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1eudpa/annotations/migrate.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xff\x1c\n\x15HttpConnectionManager\x12u\n\ncodec_type\x18\x01 \x01(\x0e\x32W.envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.CodecTypeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x1c\n\x0bstat_prefix\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\x12J\n\x03rds\x18\x03 \x01(\x0b\x32;.envoy.config.filter.network.http_connection_manager.v2.RdsH\x00\x12\x38\n\x0croute_config\x18\x04 \x01(\x0b\x32 .envoy.api.v2.RouteConfigurationH\x00\x12]\n\rscoped_routes\x18\x1f \x01(\x0b\x32\x44.envoy.config.filter.network.http_connection_manager.v2.ScopedRoutesH\x00\x12X\n\x0chttp_filters\x18\x05 \x03(\x0b\x32\x42.envoy.config.filter.network.http_connection_manager.v2.HttpFilter\x12\x32\n\x0e\x61\x64\x64_user_agent\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x66\n\x07tracing\x18\x07 \x01(\x0b\x32U.envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.Tracing\x12L\n\x1c\x63ommon_http_protocol_options\x18# \x01(\x0b\x32&.envoy.api.v2.core.HttpProtocolOptions\x12\x46\n\x15http_protocol_options\x18\x08 \x01(\x0b\x32\'.envoy.api.v2.core.Http1ProtocolOptions\x12G\n\x16http2_protocol_options\x18\t \x01(\x0b\x32\'.envoy.api.v2.core.Http2ProtocolOptions\x12\x13\n\x0bserver_name\x18\n \x01(\t\x12\x98\x01\n\x1cserver_header_transformation\x18\" \x01(\x0e\x32h.envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.ServerHeaderTransformationB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12H\n\x16max_request_headers_kb\x18\x1d \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\n\xfa\x42\x07*\x05\x18\x80@ \x00\x12\x39\n\x0cidle_timeout\x18\x0b \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\x18\x01\xb8\xee\xf2\xd2\x05\x01\x12\x36\n\x13stream_idle_timeout\x18\x18 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x32\n\x0frequest_timeout\x18\x1c \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x30\n\rdrain_timeout\x18\x0c \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x38\n\x15\x64\x65layed_close_timeout\x18\x1a \x01(\x0b\x32\x19.google.protobuf.Duration\x12?\n\naccess_log\x18\r \x03(\x0b\x32+.envoy.config.filter.accesslog.v2.AccessLog\x12\x36\n\x12use_remote_address\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x1c\n\x14xff_num_trusted_hops\x18\x13 \x01(\r\x12\x84\x01\n\x17internal_address_config\x18\x19 \x01(\x0b\x32\x63.envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.InternalAddressConfig\x12\x17\n\x0fskip_xff_append\x18\x15 \x01(\x08\x12\x0b\n\x03via\x18\x16 \x01(\t\x12\x37\n\x13generate_request_id\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12$\n\x1cpreserve_external_request_id\x18  \x01(\x08\x12\x95\x01\n\x1b\x66orward_client_cert_details\x18\x10 \x01(\x0e\x32\x66.envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.ForwardClientCertDetailsB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x92\x01\n\x1fset_current_client_cert_details\x18\x11 \x01(\x0b\x32i.envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.SetCurrentClientCertDetails\x12\x1a\n\x12proxy_100_continue\x18\x12 \x01(\x08\x12\x39\n1represent_ipv4_remote_address_as_ipv4_mapped_ipv6\x18\x14 \x01(\x08\x12t\n\x0fupgrade_configs\x18\x17 \x03(\x0b\x32[.envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.UpgradeConfig\x12\x32\n\x0enormalize_path\x18\x1e \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x15\n\rmerge_slashes\x18! \x01(\x08\x12h\n\x14request_id_extension\x18$ \x01(\x0b\x32J.envoy.config.filter.network.http_connection_manager.v2.RequestIDExtension\x1a\xae\x04\n\x07Tracing\x12\x8d\x01\n\x0eoperation_name\x18\x01 \x01(\x0e\x32\x63.envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.Tracing.OperationNameB\x10\x18\x01\xfa\x42\x05\x82\x01\x02\x10\x01\xb8\xee\xf2\xd2\x05\x01\x12$\n\x18request_headers_for_tags\x18\x02 \x03(\tB\x02\x18\x01\x12,\n\x0f\x63lient_sampling\x18\x03 \x01(\x0b\x32\x13.envoy.type.Percent\x12,\n\x0frandom_sampling\x18\x04 \x01(\x0b\x32\x13.envoy.type.Percent\x12-\n\x10overall_sampling\x18\x05 \x01(\x0b\x32\x13.envoy.type.Percent\x12\x0f\n\x07verbose\x18\x06 \x01(\x08\x12\x39\n\x13max_path_tag_length\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x35\n\x0b\x63ustom_tags\x18\x08 \x03(\x0b\x32 .envoy.type.tracing.v2.CustomTag\x12\x35\n\x08provider\x18\t \x01(\x0b\x32#.envoy.config.trace.v2.Tracing.Http\"(\n\rOperationName\x12\x0b\n\x07INGRESS\x10\x00\x12\n\n\x06\x45GRESS\x10\x01\x1a-\n\x15InternalAddressConfig\x12\x14\n\x0cunix_sockets\x18\x01 \x01(\x08\x1a\x87\x01\n\x1bSetCurrentClientCertDetails\x12+\n\x07subject\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x0c\n\x04\x63\x65rt\x18\x03 \x01(\x08\x12\r\n\x05\x63hain\x18\x06 \x01(\x08\x12\x0b\n\x03\x64ns\x18\x04 \x01(\x08\x12\x0b\n\x03uri\x18\x05 \x01(\x08J\x04\x08\x02\x10\x03\x1a\xa7\x01\n\rUpgradeConfig\x12\x14\n\x0cupgrade_type\x18\x01 \x01(\t\x12S\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x42.envoy.config.filter.network.http_connection_manager.v2.HttpFilter\x12+\n\x07\x65nabled\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"6\n\tCodecType\x12\x08\n\x04\x41UTO\x10\x00\x12\t\n\x05HTTP1\x10\x01\x12\t\n\x05HTTP2\x10\x02\x12\t\n\x05HTTP3\x10\x03\"S\n\x1aServerHeaderTransformation\x12\r\n\tOVERWRITE\x10\x00\x12\x14\n\x10\x41PPEND_IF_ABSENT\x10\x01\x12\x10\n\x0cPASS_THROUGH\x10\x02\"y\n\x18\x46orwardClientCertDetails\x12\x0c\n\x08SANITIZE\x10\x00\x12\x10\n\x0c\x46ORWARD_ONLY\x10\x01\x12\x12\n\x0e\x41PPEND_FORWARD\x10\x02\x12\x10\n\x0cSANITIZE_SET\x10\x03\x12\x17\n\x13\x41LWAYS_FORWARD_ONLY\x10\x04\x42\x16\n\x0froute_specifier\x12\x03\xf8\x42\x01J\x04\x08\x1b\x10\x1c\"k\n\x03Rds\x12@\n\rconfig_source\x18\x01 \x01(\x0b\x32\x1f.envoy.api.v2.core.ConfigSourceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\"\n\x11route_config_name\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\"v\n\x1dScopedRouteConfigurationsList\x12U\n\x1bscoped_route_configurations\x18\x01 \x03(\x0b\x32&.envoy.api.v2.ScopedRouteConfigurationB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\"\xf8\x08\n\x0cScopedRoutes\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\x12y\n\x11scope_key_builder\x18\x02 \x01(\x0b\x32T.envoy.config.filter.network.http_connection_manager.v2.ScopedRoutes.ScopeKeyBuilderB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x44\n\x11rds_config_source\x18\x03 \x01(\x0b\x32\x1f.envoy.api.v2.core.ConfigSourceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x81\x01\n scoped_route_configurations_list\x18\x04 \x01(\x0b\x32U.envoy.config.filter.network.http_connection_manager.v2.ScopedRouteConfigurationsListH\x00\x12W\n\nscoped_rds\x18\x05 \x01(\x0b\x32\x41.envoy.config.filter.network.http_connection_manager.v2.ScopedRdsH\x00\x1a\x99\x05\n\x0fScopeKeyBuilder\x12\x81\x01\n\tfragments\x18\x01 \x03(\x0b\x32\x64.envoy.config.filter.network.http_connection_manager.v2.ScopedRoutes.ScopeKeyBuilder.FragmentBuilderB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x1a\x81\x04\n\x0f\x46ragmentBuilder\x12\x9b\x01\n\x16header_value_extractor\x18\x01 \x01(\x0b\x32y.envoy.config.filter.network.http_connection_manager.v2.ScopedRoutes.ScopeKeyBuilder.FragmentBuilder.HeaderValueExtractorH\x00\x1a\xc2\x02\n\x14HeaderValueExtractor\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\x12\x19\n\x11\x65lement_separator\x18\x02 \x01(\t\x12\x0f\n\x05index\x18\x03 \x01(\rH\x00\x12\x97\x01\n\x07\x65lement\x18\x04 \x01(\x0b\x32\x83\x01.envoy.config.filter.network.http_connection_manager.v2.ScopedRoutes.ScopeKeyBuilder.FragmentBuilder.HeaderValueExtractor.KvElementH\x00\x1a=\n\tKvElement\x12\x1a\n\tseparator\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\x12\x14\n\x03key\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\x42\x0e\n\x0c\x65xtract_typeB\x0b\n\x04type\x12\x03\xf8\x42\x01\x42\x17\n\x10\x63onfig_specifier\x12\x03\xf8\x42\x01\"X\n\tScopedRds\x12K\n\x18scoped_rds_config_source\x18\x01 \x01(\x0b\x32\x1f.envoy.api.v2.core.ConfigSourceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\"\x95\x01\n\nHttpFilter\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\x12-\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x02\x18\x01H\x00\x12,\n\x0ctyped_config\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\r\n\x0b\x63onfig_typeJ\x04\x08\x03\x10\x04\"@\n\x12RequestIDExtension\x12*\n\x0ctyped_config\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyB\xa8\x02\nDio.envoyproxy.envoy.config.filter.network.http_connection_manager.v2B\x1aHttpConnectionManagerProtoP\x01Zwgithub.com/envoyproxy/go-control-plane/envoy/config/filter/network/http_connection_manager/v2;http_connection_managerv2\xf2\x98\xfe\x8f\x05=\x12;envoy.extensions.filters.network.http_connection_manager.v3\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')



_HTTPCONNECTIONMANAGER = DESCRIPTOR.message_types_by_name['HttpConnectionManager']
_HTTPCONNECTIONMANAGER_TRACING = _HTTPCONNECTIONMANAGER.nested_types_by_name['Tracing']
_HTTPCONNECTIONMANAGER_INTERNALADDRESSCONFIG = _HTTPCONNECTIONMANAGER.nested_types_by_name['InternalAddressConfig']
_HTTPCONNECTIONMANAGER_SETCURRENTCLIENTCERTDETAILS = _HTTPCONNECTIONMANAGER.nested_types_by_name['SetCurrentClientCertDetails']
_HTTPCONNECTIONMANAGER_UPGRADECONFIG = _HTTPCONNECTIONMANAGER.nested_types_by_name['UpgradeConfig']
_RDS = DESCRIPTOR.message_types_by_name['Rds']
_SCOPEDROUTECONFIGURATIONSLIST = DESCRIPTOR.message_types_by_name['ScopedRouteConfigurationsList']
_SCOPEDROUTES = DESCRIPTOR.message_types_by_name['ScopedRoutes']
_SCOPEDROUTES_SCOPEKEYBUILDER = _SCOPEDROUTES.nested_types_by_name['ScopeKeyBuilder']
_SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER = _SCOPEDROUTES_SCOPEKEYBUILDER.nested_types_by_name['FragmentBuilder']
_SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR = _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER.nested_types_by_name['HeaderValueExtractor']
_SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR_KVELEMENT = _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR.nested_types_by_name['KvElement']
_SCOPEDRDS = DESCRIPTOR.message_types_by_name['ScopedRds']
_HTTPFILTER = DESCRIPTOR.message_types_by_name['HttpFilter']
_REQUESTIDEXTENSION = DESCRIPTOR.message_types_by_name['RequestIDExtension']
_HTTPCONNECTIONMANAGER_TRACING_OPERATIONNAME = _HTTPCONNECTIONMANAGER_TRACING.enum_types_by_name['OperationName']
_HTTPCONNECTIONMANAGER_CODECTYPE = _HTTPCONNECTIONMANAGER.enum_types_by_name['CodecType']
_HTTPCONNECTIONMANAGER_SERVERHEADERTRANSFORMATION = _HTTPCONNECTIONMANAGER.enum_types_by_name['ServerHeaderTransformation']
_HTTPCONNECTIONMANAGER_FORWARDCLIENTCERTDETAILS = _HTTPCONNECTIONMANAGER.enum_types_by_name['ForwardClientCertDetails']
HttpConnectionManager = _reflection.GeneratedProtocolMessageType('HttpConnectionManager', (_message.Message,), {

  'Tracing' : _reflection.GeneratedProtocolMessageType('Tracing', (_message.Message,), {
    'DESCRIPTOR' : _HTTPCONNECTIONMANAGER_TRACING,
    '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.Tracing)
    })
  ,

  'InternalAddressConfig' : _reflection.GeneratedProtocolMessageType('InternalAddressConfig', (_message.Message,), {
    'DESCRIPTOR' : _HTTPCONNECTIONMANAGER_INTERNALADDRESSCONFIG,
    '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.InternalAddressConfig)
    })
  ,

  'SetCurrentClientCertDetails' : _reflection.GeneratedProtocolMessageType('SetCurrentClientCertDetails', (_message.Message,), {
    'DESCRIPTOR' : _HTTPCONNECTIONMANAGER_SETCURRENTCLIENTCERTDETAILS,
    '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.SetCurrentClientCertDetails)
    })
  ,

  'UpgradeConfig' : _reflection.GeneratedProtocolMessageType('UpgradeConfig', (_message.Message,), {
    'DESCRIPTOR' : _HTTPCONNECTIONMANAGER_UPGRADECONFIG,
    '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager.UpgradeConfig)
    })
  ,
  'DESCRIPTOR' : _HTTPCONNECTIONMANAGER,
  '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.HttpConnectionManager)
  })
_sym_db.RegisterMessage(HttpConnectionManager)
_sym_db.RegisterMessage(HttpConnectionManager.Tracing)
_sym_db.RegisterMessage(HttpConnectionManager.InternalAddressConfig)
_sym_db.RegisterMessage(HttpConnectionManager.SetCurrentClientCertDetails)
_sym_db.RegisterMessage(HttpConnectionManager.UpgradeConfig)

Rds = _reflection.GeneratedProtocolMessageType('Rds', (_message.Message,), {
  'DESCRIPTOR' : _RDS,
  '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.Rds)
  })
_sym_db.RegisterMessage(Rds)

ScopedRouteConfigurationsList = _reflection.GeneratedProtocolMessageType('ScopedRouteConfigurationsList', (_message.Message,), {
  'DESCRIPTOR' : _SCOPEDROUTECONFIGURATIONSLIST,
  '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.ScopedRouteConfigurationsList)
  })
_sym_db.RegisterMessage(ScopedRouteConfigurationsList)

ScopedRoutes = _reflection.GeneratedProtocolMessageType('ScopedRoutes', (_message.Message,), {

  'ScopeKeyBuilder' : _reflection.GeneratedProtocolMessageType('ScopeKeyBuilder', (_message.Message,), {

    'FragmentBuilder' : _reflection.GeneratedProtocolMessageType('FragmentBuilder', (_message.Message,), {

      'HeaderValueExtractor' : _reflection.GeneratedProtocolMessageType('HeaderValueExtractor', (_message.Message,), {

        'KvElement' : _reflection.GeneratedProtocolMessageType('KvElement', (_message.Message,), {
          'DESCRIPTOR' : _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR_KVELEMENT,
          '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
          # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.ScopedRoutes.ScopeKeyBuilder.FragmentBuilder.HeaderValueExtractor.KvElement)
          })
        ,
        'DESCRIPTOR' : _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR,
        '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
        # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.ScopedRoutes.ScopeKeyBuilder.FragmentBuilder.HeaderValueExtractor)
        })
      ,
      'DESCRIPTOR' : _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER,
      '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
      # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.ScopedRoutes.ScopeKeyBuilder.FragmentBuilder)
      })
    ,
    'DESCRIPTOR' : _SCOPEDROUTES_SCOPEKEYBUILDER,
    '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.ScopedRoutes.ScopeKeyBuilder)
    })
  ,
  'DESCRIPTOR' : _SCOPEDROUTES,
  '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.ScopedRoutes)
  })
_sym_db.RegisterMessage(ScopedRoutes)
_sym_db.RegisterMessage(ScopedRoutes.ScopeKeyBuilder)
_sym_db.RegisterMessage(ScopedRoutes.ScopeKeyBuilder.FragmentBuilder)
_sym_db.RegisterMessage(ScopedRoutes.ScopeKeyBuilder.FragmentBuilder.HeaderValueExtractor)
_sym_db.RegisterMessage(ScopedRoutes.ScopeKeyBuilder.FragmentBuilder.HeaderValueExtractor.KvElement)

ScopedRds = _reflection.GeneratedProtocolMessageType('ScopedRds', (_message.Message,), {
  'DESCRIPTOR' : _SCOPEDRDS,
  '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.ScopedRds)
  })
_sym_db.RegisterMessage(ScopedRds)

HttpFilter = _reflection.GeneratedProtocolMessageType('HttpFilter', (_message.Message,), {
  'DESCRIPTOR' : _HTTPFILTER,
  '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.HttpFilter)
  })
_sym_db.RegisterMessage(HttpFilter)

RequestIDExtension = _reflection.GeneratedProtocolMessageType('RequestIDExtension', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTIDEXTENSION,
  '__module__' : 'envoy.config.filter.network.http_connection_manager.v2.http_connection_manager_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.filter.network.http_connection_manager.v2.RequestIDExtension)
  })
_sym_db.RegisterMessage(RequestIDExtension)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nDio.envoyproxy.envoy.config.filter.network.http_connection_manager.v2B\032HttpConnectionManagerProtoP\001Zwgithub.com/envoyproxy/go-control-plane/envoy/config/filter/network/http_connection_manager/v2;http_connection_managerv2\362\230\376\217\005=\022;envoy.extensions.filters.network.http_connection_manager.v3\272\200\310\321\006\002\020\001'
  _HTTPCONNECTIONMANAGER_TRACING.fields_by_name['operation_name']._options = None
  _HTTPCONNECTIONMANAGER_TRACING.fields_by_name['operation_name']._serialized_options = b'\030\001\372B\005\202\001\002\020\001\270\356\362\322\005\001'
  _HTTPCONNECTIONMANAGER_TRACING.fields_by_name['request_headers_for_tags']._options = None
  _HTTPCONNECTIONMANAGER_TRACING.fields_by_name['request_headers_for_tags']._serialized_options = b'\030\001'
  _HTTPCONNECTIONMANAGER.oneofs_by_name['route_specifier']._options = None
  _HTTPCONNECTIONMANAGER.oneofs_by_name['route_specifier']._serialized_options = b'\370B\001'
  _HTTPCONNECTIONMANAGER.fields_by_name['codec_type']._options = None
  _HTTPCONNECTIONMANAGER.fields_by_name['codec_type']._serialized_options = b'\372B\005\202\001\002\020\001'
  _HTTPCONNECTIONMANAGER.fields_by_name['stat_prefix']._options = None
  _HTTPCONNECTIONMANAGER.fields_by_name['stat_prefix']._serialized_options = b'\372B\004r\002 \001'
  _HTTPCONNECTIONMANAGER.fields_by_name['server_header_transformation']._options = None
  _HTTPCONNECTIONMANAGER.fields_by_name['server_header_transformation']._serialized_options = b'\372B\005\202\001\002\020\001'
  _HTTPCONNECTIONMANAGER.fields_by_name['max_request_headers_kb']._options = None
  _HTTPCONNECTIONMANAGER.fields_by_name['max_request_headers_kb']._serialized_options = b'\372B\007*\005\030\200@ \000'
  _HTTPCONNECTIONMANAGER.fields_by_name['idle_timeout']._options = None
  _HTTPCONNECTIONMANAGER.fields_by_name['idle_timeout']._serialized_options = b'\030\001\270\356\362\322\005\001'
  _HTTPCONNECTIONMANAGER.fields_by_name['forward_client_cert_details']._options = None
  _HTTPCONNECTIONMANAGER.fields_by_name['forward_client_cert_details']._serialized_options = b'\372B\005\202\001\002\020\001'
  _RDS.fields_by_name['config_source']._options = None
  _RDS.fields_by_name['config_source']._serialized_options = b'\372B\005\212\001\002\020\001'
  _RDS.fields_by_name['route_config_name']._options = None
  _RDS.fields_by_name['route_config_name']._serialized_options = b'\372B\004r\002 \001'
  _SCOPEDROUTECONFIGURATIONSLIST.fields_by_name['scoped_route_configurations']._options = None
  _SCOPEDROUTECONFIGURATIONSLIST.fields_by_name['scoped_route_configurations']._serialized_options = b'\372B\005\222\001\002\010\001'
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR_KVELEMENT.fields_by_name['separator']._options = None
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR_KVELEMENT.fields_by_name['separator']._serialized_options = b'\372B\004r\002 \001'
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR_KVELEMENT.fields_by_name['key']._options = None
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR_KVELEMENT.fields_by_name['key']._serialized_options = b'\372B\004r\002 \001'
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR.fields_by_name['name']._options = None
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR.fields_by_name['name']._serialized_options = b'\372B\004r\002 \001'
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER.oneofs_by_name['type']._options = None
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER.oneofs_by_name['type']._serialized_options = b'\370B\001'
  _SCOPEDROUTES_SCOPEKEYBUILDER.fields_by_name['fragments']._options = None
  _SCOPEDROUTES_SCOPEKEYBUILDER.fields_by_name['fragments']._serialized_options = b'\372B\005\222\001\002\010\001'
  _SCOPEDROUTES.oneofs_by_name['config_specifier']._options = None
  _SCOPEDROUTES.oneofs_by_name['config_specifier']._serialized_options = b'\370B\001'
  _SCOPEDROUTES.fields_by_name['name']._options = None
  _SCOPEDROUTES.fields_by_name['name']._serialized_options = b'\372B\004r\002 \001'
  _SCOPEDROUTES.fields_by_name['scope_key_builder']._options = None
  _SCOPEDROUTES.fields_by_name['scope_key_builder']._serialized_options = b'\372B\005\212\001\002\020\001'
  _SCOPEDROUTES.fields_by_name['rds_config_source']._options = None
  _SCOPEDROUTES.fields_by_name['rds_config_source']._serialized_options = b'\372B\005\212\001\002\020\001'
  _SCOPEDRDS.fields_by_name['scoped_rds_config_source']._options = None
  _SCOPEDRDS.fields_by_name['scoped_rds_config_source']._serialized_options = b'\372B\005\212\001\002\020\001'
  _HTTPFILTER.fields_by_name['name']._options = None
  _HTTPFILTER.fields_by_name['name']._serialized_options = b'\372B\004r\002 \001'
  _HTTPFILTER.fields_by_name['config']._options = None
  _HTTPFILTER.fields_by_name['config']._serialized_options = b'\030\001'
  _HTTPCONNECTIONMANAGER._serialized_start=680
  _HTTPCONNECTIONMANAGER._serialized_end=4391
  _HTTPCONNECTIONMANAGER_TRACING._serialized_start=3184
  _HTTPCONNECTIONMANAGER_TRACING._serialized_end=3742
  _HTTPCONNECTIONMANAGER_TRACING_OPERATIONNAME._serialized_start=3702
  _HTTPCONNECTIONMANAGER_TRACING_OPERATIONNAME._serialized_end=3742
  _HTTPCONNECTIONMANAGER_INTERNALADDRESSCONFIG._serialized_start=3744
  _HTTPCONNECTIONMANAGER_INTERNALADDRESSCONFIG._serialized_end=3789
  _HTTPCONNECTIONMANAGER_SETCURRENTCLIENTCERTDETAILS._serialized_start=3792
  _HTTPCONNECTIONMANAGER_SETCURRENTCLIENTCERTDETAILS._serialized_end=3927
  _HTTPCONNECTIONMANAGER_UPGRADECONFIG._serialized_start=3930
  _HTTPCONNECTIONMANAGER_UPGRADECONFIG._serialized_end=4097
  _HTTPCONNECTIONMANAGER_CODECTYPE._serialized_start=4099
  _HTTPCONNECTIONMANAGER_CODECTYPE._serialized_end=4153
  _HTTPCONNECTIONMANAGER_SERVERHEADERTRANSFORMATION._serialized_start=4155
  _HTTPCONNECTIONMANAGER_SERVERHEADERTRANSFORMATION._serialized_end=4238
  _HTTPCONNECTIONMANAGER_FORWARDCLIENTCERTDETAILS._serialized_start=4240
  _HTTPCONNECTIONMANAGER_FORWARDCLIENTCERTDETAILS._serialized_end=4361
  _RDS._serialized_start=4393
  _RDS._serialized_end=4500
  _SCOPEDROUTECONFIGURATIONSLIST._serialized_start=4502
  _SCOPEDROUTECONFIGURATIONSLIST._serialized_end=4620
  _SCOPEDROUTES._serialized_start=4623
  _SCOPEDROUTES._serialized_end=5767
  _SCOPEDROUTES_SCOPEKEYBUILDER._serialized_start=5077
  _SCOPEDROUTES_SCOPEKEYBUILDER._serialized_end=5742
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER._serialized_start=5229
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER._serialized_end=5742
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR._serialized_start=5407
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR._serialized_end=5729
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR_KVELEMENT._serialized_start=5652
  _SCOPEDROUTES_SCOPEKEYBUILDER_FRAGMENTBUILDER_HEADERVALUEEXTRACTOR_KVELEMENT._serialized_end=5713
  _SCOPEDRDS._serialized_start=5769
  _SCOPEDRDS._serialized_end=5857
  _HTTPFILTER._serialized_start=5860
  _HTTPFILTER._serialized_end=6009
  _REQUESTIDEXTENSION._serialized_start=6011
  _REQUESTIDEXTENSION._serialized_end=6075
# @@protoc_insertion_point(module_scope)