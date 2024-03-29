# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/network/zookeeper_proxy/v3/zookeeper_proxy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIenvoy/extensions/filters/network/zookeeper_proxy/v3/zookeeper_proxy.proto\x12\x33\x65nvoy.extensions.filters.network.zookeeper_proxy.v3\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xc6\x01\n\x0eZooKeeperProxy\x12\x1c\n\x0bstat_prefix\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x12\n\naccess_log\x18\x02 \x01(\t\x12\x36\n\x10max_packet_bytes\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value:J\x9a\xc5\x88\x1e\x45\nCenvoy.config.filter.network.zookeeper_proxy.v1alpha1.ZooKeeperProxyB\xd0\x01\nAio.envoyproxy.envoy.extensions.filters.network.zookeeper_proxy.v3B\x13ZookeeperProxyProtoP\x01Zlgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/zookeeper_proxy/v3;zookeeper_proxyv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_ZOOKEEPERPROXY = DESCRIPTOR.message_types_by_name['ZooKeeperProxy']
ZooKeeperProxy = _reflection.GeneratedProtocolMessageType('ZooKeeperProxy', (_message.Message,), {
  'DESCRIPTOR' : _ZOOKEEPERPROXY,
  '__module__' : 'envoy.extensions.filters.network.zookeeper_proxy.v3.zookeeper_proxy_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.network.zookeeper_proxy.v3.ZooKeeperProxy)
  })
_sym_db.RegisterMessage(ZooKeeperProxy)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nAio.envoyproxy.envoy.extensions.filters.network.zookeeper_proxy.v3B\023ZookeeperProxyProtoP\001Zlgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/zookeeper_proxy/v3;zookeeper_proxyv3\272\200\310\321\006\002\020\002'
  _ZOOKEEPERPROXY.fields_by_name['stat_prefix']._options = None
  _ZOOKEEPERPROXY.fields_by_name['stat_prefix']._serialized_options = b'\372B\004r\002\020\001'
  _ZOOKEEPERPROXY._options = None
  _ZOOKEEPERPROXY._serialized_options = b'\232\305\210\036E\nCenvoy.config.filter.network.zookeeper_proxy.v1alpha1.ZooKeeperProxy'
  _ZOOKEEPERPROXY._serialized_start=254
  _ZOOKEEPERPROXY._serialized_end=452
# @@protoc_insertion_point(module_scope)
