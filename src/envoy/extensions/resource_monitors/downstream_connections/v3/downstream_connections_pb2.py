# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/resource_monitors/downstream_connections/v3/downstream_connections.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xds.annotations.v3 import status_pb2 as xds_dot_annotations_dot_v3_dot_status__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nYenvoy/extensions/resource_monitors/downstream_connections/v3/downstream_connections.proto\x12<envoy.extensions.resource_monitors.downstream_connections.v3\x1a\x1fxds/annotations/v3/status.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"Q\n\x1b\x44ownstreamConnectionsConfig\x12\x32\n!max_active_downstream_connections\x18\x01 \x01(\x03\x42\x07\xfa\x42\x04\"\x02 \x00\x42\xf8\x01\nJio.envoyproxy.envoy.extensions.resource_monitors.downstream_connections.v3B\x1a\x44ownstreamConnectionsProtoP\x01Z|github.com/envoyproxy/go-control-plane/envoy/extensions/resource_monitors/downstream_connections/v3;downstream_connectionsv3\xba\x80\xc8\xd1\x06\x02\x10\x02\xd2\xc6\xa4\xe1\x06\x02\x08\x01\x62\x06proto3')



_DOWNSTREAMCONNECTIONSCONFIG = DESCRIPTOR.message_types_by_name['DownstreamConnectionsConfig']
DownstreamConnectionsConfig = _reflection.GeneratedProtocolMessageType('DownstreamConnectionsConfig', (_message.Message,), {
  'DESCRIPTOR' : _DOWNSTREAMCONNECTIONSCONFIG,
  '__module__' : 'envoy.extensions.resource_monitors.downstream_connections.v3.downstream_connections_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.resource_monitors.downstream_connections.v3.DownstreamConnectionsConfig)
  })
_sym_db.RegisterMessage(DownstreamConnectionsConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nJio.envoyproxy.envoy.extensions.resource_monitors.downstream_connections.v3B\032DownstreamConnectionsProtoP\001Z|github.com/envoyproxy/go-control-plane/envoy/extensions/resource_monitors/downstream_connections/v3;downstream_connectionsv3\272\200\310\321\006\002\020\002\322\306\244\341\006\002\010\001'
  _DOWNSTREAMCONNECTIONSCONFIG.fields_by_name['max_active_downstream_connections']._options = None
  _DOWNSTREAMCONNECTIONSCONFIG.fields_by_name['max_active_downstream_connections']._serialized_options = b'\372B\004\"\002 \000'
  _DOWNSTREAMCONNECTIONSCONFIG._serialized_start=244
  _DOWNSTREAMCONNECTIONSCONFIG._serialized_end=325
# @@protoc_insertion_point(module_scope)
