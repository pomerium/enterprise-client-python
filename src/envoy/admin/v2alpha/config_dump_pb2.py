# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/admin/v2alpha/config_dump.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.bootstrap.v2 import bootstrap_pb2 as envoy_dot_config_dot_bootstrap_dot_v2_dot_bootstrap__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%envoy/admin/v2alpha/config_dump.proto\x12\x13\x65nvoy.admin.v2alpha\x1a)envoy/config/bootstrap/v2/bootstrap.proto\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dudpa/annotations/status.proto\"3\n\nConfigDump\x12%\n\x07\x63onfigs\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\"\x92\x01\n\x12UpdateFailureState\x12\x32\n\x14\x66\x61iled_configuration\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x37\n\x13last_update_attempt\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x64\x65tails\x18\x03 \x01(\t\"\x80\x01\n\x13\x42ootstrapConfigDump\x12\x37\n\tbootstrap\x18\x01 \x01(\x0b\x32$.envoy.config.bootstrap.v2.Bootstrap\x12\x30\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xaa\x06\n\x13ListenersConfigDump\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12Q\n\x10static_listeners\x18\x02 \x03(\x0b\x32\x37.envoy.admin.v2alpha.ListenersConfigDump.StaticListener\x12S\n\x11\x64ynamic_listeners\x18\x03 \x03(\x0b\x32\x38.envoy.admin.v2alpha.ListenersConfigDump.DynamicListener\x1aj\n\x0eStaticListener\x12&\n\x08listener\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x86\x01\n\x14\x44ynamicListenerState\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12&\n\x08listener\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x0clast_updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\xdf\x02\n\x0f\x44ynamicListener\x12\x0c\n\x04name\x18\x01 \x01(\t\x12S\n\x0c\x61\x63tive_state\x18\x02 \x01(\x0b\x32=.envoy.admin.v2alpha.ListenersConfigDump.DynamicListenerState\x12T\n\rwarming_state\x18\x03 \x01(\x0b\x32=.envoy.admin.v2alpha.ListenersConfigDump.DynamicListenerState\x12U\n\x0e\x64raining_state\x18\x04 \x01(\x0b\x32=.envoy.admin.v2alpha.ListenersConfigDump.DynamicListenerState\x12<\n\x0b\x65rror_state\x18\x05 \x01(\x0b\x32\'.envoy.admin.v2alpha.UpdateFailureState\"\x98\x04\n\x12\x43lustersConfigDump\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12N\n\x0fstatic_clusters\x18\x02 \x03(\x0b\x32\x35.envoy.admin.v2alpha.ClustersConfigDump.StaticCluster\x12W\n\x17\x64ynamic_active_clusters\x18\x03 \x03(\x0b\x32\x36.envoy.admin.v2alpha.ClustersConfigDump.DynamicCluster\x12X\n\x18\x64ynamic_warming_clusters\x18\x04 \x03(\x0b\x32\x36.envoy.admin.v2alpha.ClustersConfigDump.DynamicCluster\x1ah\n\rStaticCluster\x12%\n\x07\x63luster\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x7f\n\x0e\x44ynamicCluster\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12%\n\x07\x63luster\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x0clast_updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc0\x03\n\x10RoutesConfigDump\x12U\n\x14static_route_configs\x18\x02 \x03(\x0b\x32\x37.envoy.admin.v2alpha.RoutesConfigDump.StaticRouteConfig\x12W\n\x15\x64ynamic_route_configs\x18\x03 \x03(\x0b\x32\x38.envoy.admin.v2alpha.RoutesConfigDump.DynamicRouteConfig\x1aq\n\x11StaticRouteConfig\x12*\n\x0croute_config\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\x88\x01\n\x12\x44ynamicRouteConfig\x12\x14\n\x0cversion_info\x18\x01 \x01(\t\x12*\n\x0croute_config\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x0clast_updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa9\x04\n\x16ScopedRoutesConfigDump\x12i\n\x1binline_scoped_route_configs\x18\x01 \x03(\x0b\x32\x44.envoy.admin.v2alpha.ScopedRoutesConfigDump.InlineScopedRouteConfigs\x12k\n\x1c\x64ynamic_scoped_route_configs\x18\x02 \x03(\x0b\x32\x45.envoy.admin.v2alpha.ScopedRoutesConfigDump.DynamicScopedRouteConfigs\x1a\x8e\x01\n\x18InlineScopedRouteConfigs\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\x14scoped_route_configs\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x0clast_updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a\xa5\x01\n\x19\x44ynamicScopedRouteConfigs\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cversion_info\x18\x02 \x01(\t\x12\x32\n\x14scoped_route_configs\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x0clast_updated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x91\x04\n\x11SecretsConfigDump\x12K\n\x0estatic_secrets\x18\x01 \x03(\x0b\x32\x33.envoy.admin.v2alpha.SecretsConfigDump.StaticSecret\x12T\n\x16\x64ynamic_active_secrets\x18\x02 \x03(\x0b\x32\x34.envoy.admin.v2alpha.SecretsConfigDump.DynamicSecret\x12U\n\x17\x64ynamic_warming_secrets\x18\x03 \x03(\x0b\x32\x34.envoy.admin.v2alpha.SecretsConfigDump.DynamicSecret\x1a\x8b\x01\n\rDynamicSecret\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cversion_info\x18\x02 \x01(\t\x12\x30\n\x0clast_updated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x06secret\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x1at\n\x0cStaticSecret\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\x0clast_updated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12$\n\x06secret\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyBz\n!io.envoyproxy.envoy.admin.v2alphaB\x0f\x43onfigDumpProtoP\x01Z:github.com/envoyproxy/go-control-plane/envoy/admin/v2alpha\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')



_CONFIGDUMP = DESCRIPTOR.message_types_by_name['ConfigDump']
_UPDATEFAILURESTATE = DESCRIPTOR.message_types_by_name['UpdateFailureState']
_BOOTSTRAPCONFIGDUMP = DESCRIPTOR.message_types_by_name['BootstrapConfigDump']
_LISTENERSCONFIGDUMP = DESCRIPTOR.message_types_by_name['ListenersConfigDump']
_LISTENERSCONFIGDUMP_STATICLISTENER = _LISTENERSCONFIGDUMP.nested_types_by_name['StaticListener']
_LISTENERSCONFIGDUMP_DYNAMICLISTENERSTATE = _LISTENERSCONFIGDUMP.nested_types_by_name['DynamicListenerState']
_LISTENERSCONFIGDUMP_DYNAMICLISTENER = _LISTENERSCONFIGDUMP.nested_types_by_name['DynamicListener']
_CLUSTERSCONFIGDUMP = DESCRIPTOR.message_types_by_name['ClustersConfigDump']
_CLUSTERSCONFIGDUMP_STATICCLUSTER = _CLUSTERSCONFIGDUMP.nested_types_by_name['StaticCluster']
_CLUSTERSCONFIGDUMP_DYNAMICCLUSTER = _CLUSTERSCONFIGDUMP.nested_types_by_name['DynamicCluster']
_ROUTESCONFIGDUMP = DESCRIPTOR.message_types_by_name['RoutesConfigDump']
_ROUTESCONFIGDUMP_STATICROUTECONFIG = _ROUTESCONFIGDUMP.nested_types_by_name['StaticRouteConfig']
_ROUTESCONFIGDUMP_DYNAMICROUTECONFIG = _ROUTESCONFIGDUMP.nested_types_by_name['DynamicRouteConfig']
_SCOPEDROUTESCONFIGDUMP = DESCRIPTOR.message_types_by_name['ScopedRoutesConfigDump']
_SCOPEDROUTESCONFIGDUMP_INLINESCOPEDROUTECONFIGS = _SCOPEDROUTESCONFIGDUMP.nested_types_by_name['InlineScopedRouteConfigs']
_SCOPEDROUTESCONFIGDUMP_DYNAMICSCOPEDROUTECONFIGS = _SCOPEDROUTESCONFIGDUMP.nested_types_by_name['DynamicScopedRouteConfigs']
_SECRETSCONFIGDUMP = DESCRIPTOR.message_types_by_name['SecretsConfigDump']
_SECRETSCONFIGDUMP_DYNAMICSECRET = _SECRETSCONFIGDUMP.nested_types_by_name['DynamicSecret']
_SECRETSCONFIGDUMP_STATICSECRET = _SECRETSCONFIGDUMP.nested_types_by_name['StaticSecret']
ConfigDump = _reflection.GeneratedProtocolMessageType('ConfigDump', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGDUMP,
  '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ConfigDump)
  })
_sym_db.RegisterMessage(ConfigDump)

UpdateFailureState = _reflection.GeneratedProtocolMessageType('UpdateFailureState', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFAILURESTATE,
  '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.UpdateFailureState)
  })
_sym_db.RegisterMessage(UpdateFailureState)

BootstrapConfigDump = _reflection.GeneratedProtocolMessageType('BootstrapConfigDump', (_message.Message,), {
  'DESCRIPTOR' : _BOOTSTRAPCONFIGDUMP,
  '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.BootstrapConfigDump)
  })
_sym_db.RegisterMessage(BootstrapConfigDump)

ListenersConfigDump = _reflection.GeneratedProtocolMessageType('ListenersConfigDump', (_message.Message,), {

  'StaticListener' : _reflection.GeneratedProtocolMessageType('StaticListener', (_message.Message,), {
    'DESCRIPTOR' : _LISTENERSCONFIGDUMP_STATICLISTENER,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ListenersConfigDump.StaticListener)
    })
  ,

  'DynamicListenerState' : _reflection.GeneratedProtocolMessageType('DynamicListenerState', (_message.Message,), {
    'DESCRIPTOR' : _LISTENERSCONFIGDUMP_DYNAMICLISTENERSTATE,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ListenersConfigDump.DynamicListenerState)
    })
  ,

  'DynamicListener' : _reflection.GeneratedProtocolMessageType('DynamicListener', (_message.Message,), {
    'DESCRIPTOR' : _LISTENERSCONFIGDUMP_DYNAMICLISTENER,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ListenersConfigDump.DynamicListener)
    })
  ,
  'DESCRIPTOR' : _LISTENERSCONFIGDUMP,
  '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ListenersConfigDump)
  })
_sym_db.RegisterMessage(ListenersConfigDump)
_sym_db.RegisterMessage(ListenersConfigDump.StaticListener)
_sym_db.RegisterMessage(ListenersConfigDump.DynamicListenerState)
_sym_db.RegisterMessage(ListenersConfigDump.DynamicListener)

ClustersConfigDump = _reflection.GeneratedProtocolMessageType('ClustersConfigDump', (_message.Message,), {

  'StaticCluster' : _reflection.GeneratedProtocolMessageType('StaticCluster', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTERSCONFIGDUMP_STATICCLUSTER,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ClustersConfigDump.StaticCluster)
    })
  ,

  'DynamicCluster' : _reflection.GeneratedProtocolMessageType('DynamicCluster', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTERSCONFIGDUMP_DYNAMICCLUSTER,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ClustersConfigDump.DynamicCluster)
    })
  ,
  'DESCRIPTOR' : _CLUSTERSCONFIGDUMP,
  '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ClustersConfigDump)
  })
_sym_db.RegisterMessage(ClustersConfigDump)
_sym_db.RegisterMessage(ClustersConfigDump.StaticCluster)
_sym_db.RegisterMessage(ClustersConfigDump.DynamicCluster)

RoutesConfigDump = _reflection.GeneratedProtocolMessageType('RoutesConfigDump', (_message.Message,), {

  'StaticRouteConfig' : _reflection.GeneratedProtocolMessageType('StaticRouteConfig', (_message.Message,), {
    'DESCRIPTOR' : _ROUTESCONFIGDUMP_STATICROUTECONFIG,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.RoutesConfigDump.StaticRouteConfig)
    })
  ,

  'DynamicRouteConfig' : _reflection.GeneratedProtocolMessageType('DynamicRouteConfig', (_message.Message,), {
    'DESCRIPTOR' : _ROUTESCONFIGDUMP_DYNAMICROUTECONFIG,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.RoutesConfigDump.DynamicRouteConfig)
    })
  ,
  'DESCRIPTOR' : _ROUTESCONFIGDUMP,
  '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.RoutesConfigDump)
  })
_sym_db.RegisterMessage(RoutesConfigDump)
_sym_db.RegisterMessage(RoutesConfigDump.StaticRouteConfig)
_sym_db.RegisterMessage(RoutesConfigDump.DynamicRouteConfig)

ScopedRoutesConfigDump = _reflection.GeneratedProtocolMessageType('ScopedRoutesConfigDump', (_message.Message,), {

  'InlineScopedRouteConfigs' : _reflection.GeneratedProtocolMessageType('InlineScopedRouteConfigs', (_message.Message,), {
    'DESCRIPTOR' : _SCOPEDROUTESCONFIGDUMP_INLINESCOPEDROUTECONFIGS,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ScopedRoutesConfigDump.InlineScopedRouteConfigs)
    })
  ,

  'DynamicScopedRouteConfigs' : _reflection.GeneratedProtocolMessageType('DynamicScopedRouteConfigs', (_message.Message,), {
    'DESCRIPTOR' : _SCOPEDROUTESCONFIGDUMP_DYNAMICSCOPEDROUTECONFIGS,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ScopedRoutesConfigDump.DynamicScopedRouteConfigs)
    })
  ,
  'DESCRIPTOR' : _SCOPEDROUTESCONFIGDUMP,
  '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.ScopedRoutesConfigDump)
  })
_sym_db.RegisterMessage(ScopedRoutesConfigDump)
_sym_db.RegisterMessage(ScopedRoutesConfigDump.InlineScopedRouteConfigs)
_sym_db.RegisterMessage(ScopedRoutesConfigDump.DynamicScopedRouteConfigs)

SecretsConfigDump = _reflection.GeneratedProtocolMessageType('SecretsConfigDump', (_message.Message,), {

  'DynamicSecret' : _reflection.GeneratedProtocolMessageType('DynamicSecret', (_message.Message,), {
    'DESCRIPTOR' : _SECRETSCONFIGDUMP_DYNAMICSECRET,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.SecretsConfigDump.DynamicSecret)
    })
  ,

  'StaticSecret' : _reflection.GeneratedProtocolMessageType('StaticSecret', (_message.Message,), {
    'DESCRIPTOR' : _SECRETSCONFIGDUMP_STATICSECRET,
    '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
    # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.SecretsConfigDump.StaticSecret)
    })
  ,
  'DESCRIPTOR' : _SECRETSCONFIGDUMP,
  '__module__' : 'envoy.admin.v2alpha.config_dump_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v2alpha.SecretsConfigDump)
  })
_sym_db.RegisterMessage(SecretsConfigDump)
_sym_db.RegisterMessage(SecretsConfigDump.DynamicSecret)
_sym_db.RegisterMessage(SecretsConfigDump.StaticSecret)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!io.envoyproxy.envoy.admin.v2alphaB\017ConfigDumpProtoP\001Z:github.com/envoyproxy/go-control-plane/envoy/admin/v2alpha\272\200\310\321\006\002\020\001'
  _CONFIGDUMP._serialized_start=196
  _CONFIGDUMP._serialized_end=247
  _UPDATEFAILURESTATE._serialized_start=250
  _UPDATEFAILURESTATE._serialized_end=396
  _BOOTSTRAPCONFIGDUMP._serialized_start=399
  _BOOTSTRAPCONFIGDUMP._serialized_end=527
  _LISTENERSCONFIGDUMP._serialized_start=530
  _LISTENERSCONFIGDUMP._serialized_end=1340
  _LISTENERSCONFIGDUMP_STATICLISTENER._serialized_start=743
  _LISTENERSCONFIGDUMP_STATICLISTENER._serialized_end=849
  _LISTENERSCONFIGDUMP_DYNAMICLISTENERSTATE._serialized_start=852
  _LISTENERSCONFIGDUMP_DYNAMICLISTENERSTATE._serialized_end=986
  _LISTENERSCONFIGDUMP_DYNAMICLISTENER._serialized_start=989
  _LISTENERSCONFIGDUMP_DYNAMICLISTENER._serialized_end=1340
  _CLUSTERSCONFIGDUMP._serialized_start=1343
  _CLUSTERSCONFIGDUMP._serialized_end=1879
  _CLUSTERSCONFIGDUMP_STATICCLUSTER._serialized_start=1646
  _CLUSTERSCONFIGDUMP_STATICCLUSTER._serialized_end=1750
  _CLUSTERSCONFIGDUMP_DYNAMICCLUSTER._serialized_start=1752
  _CLUSTERSCONFIGDUMP_DYNAMICCLUSTER._serialized_end=1879
  _ROUTESCONFIGDUMP._serialized_start=1882
  _ROUTESCONFIGDUMP._serialized_end=2330
  _ROUTESCONFIGDUMP_STATICROUTECONFIG._serialized_start=2078
  _ROUTESCONFIGDUMP_STATICROUTECONFIG._serialized_end=2191
  _ROUTESCONFIGDUMP_DYNAMICROUTECONFIG._serialized_start=2194
  _ROUTESCONFIGDUMP_DYNAMICROUTECONFIG._serialized_end=2330
  _SCOPEDROUTESCONFIGDUMP._serialized_start=2333
  _SCOPEDROUTESCONFIGDUMP._serialized_end=2886
  _SCOPEDROUTESCONFIGDUMP_INLINESCOPEDROUTECONFIGS._serialized_start=2576
  _SCOPEDROUTESCONFIGDUMP_INLINESCOPEDROUTECONFIGS._serialized_end=2718
  _SCOPEDROUTESCONFIGDUMP_DYNAMICSCOPEDROUTECONFIGS._serialized_start=2721
  _SCOPEDROUTESCONFIGDUMP_DYNAMICSCOPEDROUTECONFIGS._serialized_end=2886
  _SECRETSCONFIGDUMP._serialized_start=2889
  _SECRETSCONFIGDUMP._serialized_end=3418
  _SECRETSCONFIGDUMP_DYNAMICSECRET._serialized_start=3161
  _SECRETSCONFIGDUMP_DYNAMICSECRET._serialized_end=3300
  _SECRETSCONFIGDUMP_STATICSECRET._serialized_start=3302
  _SECRETSCONFIGDUMP_STATICSECRET._serialized_end=3418
# @@protoc_insertion_point(module_scope)
