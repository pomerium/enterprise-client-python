# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/discovery/v3/ads.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.service.discovery.v3 import discovery_pb2 as envoy_dot_service_dot_discovery_dot_v3_dot_discovery__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$envoy/service/discovery/v3/ads.proto\x12\x1a\x65nvoy.service.discovery.v3\x1a*envoy/service/discovery/v3/discovery.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"6\n\x08\x41\x64sDummy:*\x9a\xc5\x88\x1e%\n#envoy.service.discovery.v2.AdsDummy2\xa6\x02\n\x1a\x41ggregatedDiscoveryService\x12~\n\x19StreamAggregatedResources\x12,.envoy.service.discovery.v3.DiscoveryRequest\x1a-.envoy.service.discovery.v3.DiscoveryResponse\"\x00(\x01\x30\x01\x12\x87\x01\n\x18\x44\x65ltaAggregatedResources\x12\x31.envoy.service.discovery.v3.DeltaDiscoveryRequest\x1a\x32.envoy.service.discovery.v3.DeltaDiscoveryResponse\"\x00(\x01\x30\x01\x42\x90\x01\n(io.envoyproxy.envoy.service.discovery.v3B\x08\x41\x64sProtoP\x01ZMgithub.com/envoyproxy/go-control-plane/envoy/service/discovery/v3;discoveryv3\x88\x01\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_ADSDUMMY = DESCRIPTOR.message_types_by_name['AdsDummy']
AdsDummy = _reflection.GeneratedProtocolMessageType('AdsDummy', (_message.Message,), {
  'DESCRIPTOR' : _ADSDUMMY,
  '__module__' : 'envoy.service.discovery.v3.ads_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.discovery.v3.AdsDummy)
  })
_sym_db.RegisterMessage(AdsDummy)

_AGGREGATEDDISCOVERYSERVICE = DESCRIPTOR.services_by_name['AggregatedDiscoveryService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(io.envoyproxy.envoy.service.discovery.v3B\010AdsProtoP\001ZMgithub.com/envoyproxy/go-control-plane/envoy/service/discovery/v3;discoveryv3\210\001\001\272\200\310\321\006\002\020\002'
  _ADSDUMMY._options = None
  _ADSDUMMY._serialized_options = b'\232\305\210\036%\n#envoy.service.discovery.v2.AdsDummy'
  _ADSDUMMY._serialized_start=178
  _ADSDUMMY._serialized_end=232
  _AGGREGATEDDISCOVERYSERVICE._serialized_start=235
  _AGGREGATEDDISCOVERYSERVICE._serialized_end=529
# @@protoc_insertion_point(module_scope)
