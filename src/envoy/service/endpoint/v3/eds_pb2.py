# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/endpoint/v3/eds.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.service.discovery.v3 import discovery_pb2 as envoy_dot_service_dot_discovery_dot_v3_dot_discovery__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from envoy.annotations import resource_pb2 as envoy_dot_annotations_dot_resource__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#envoy/service/endpoint/v3/eds.proto\x12\x19\x65nvoy.service.endpoint.v3\x1a*envoy/service/discovery/v3/discovery.proto\x1a\x1cgoogle/api/annotations.proto\x1a envoy/annotations/resource.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"(\n\x08\x45\x64sDummy:\x1c\x9a\xc5\x88\x1e\x17\n\x15\x65nvoy.api.v2.EdsDummy2\xe1\x03\n\x18\x45ndpointDiscoveryService\x12t\n\x0fStreamEndpoints\x12,.envoy.service.discovery.v3.DiscoveryRequest\x1a-.envoy.service.discovery.v3.DiscoveryResponse\"\x00(\x01\x30\x01\x12}\n\x0e\x44\x65ltaEndpoints\x12\x31.envoy.service.discovery.v3.DeltaDiscoveryRequest\x1a\x32.envoy.service.discovery.v3.DeltaDiscoveryResponse\"\x00(\x01\x30\x01\x12\x97\x01\n\x0e\x46\x65tchEndpoints\x12,.envoy.service.discovery.v3.DiscoveryRequest\x1a-.envoy.service.discovery.v3.DiscoveryResponse\"(\x82\xd3\xe4\x93\x02\x19\"\x17/v3/discovery:endpoints\x82\xd3\xe4\x93\x02\x03:\x01*\x1a\x36\x8a\xa4\x96\xf3\x07\x30\n.envoy.config.endpoint.v3.ClusterLoadAssignmentB\x8d\x01\n\'io.envoyproxy.envoy.service.endpoint.v3B\x08\x45\x64sProtoP\x01ZKgithub.com/envoyproxy/go-control-plane/envoy/service/endpoint/v3;endpointv3\x88\x01\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_EDSDUMMY = DESCRIPTOR.message_types_by_name['EdsDummy']
EdsDummy = _reflection.GeneratedProtocolMessageType('EdsDummy', (_message.Message,), {
  'DESCRIPTOR' : _EDSDUMMY,
  '__module__' : 'envoy.service.endpoint.v3.eds_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.endpoint.v3.EdsDummy)
  })
_sym_db.RegisterMessage(EdsDummy)

_ENDPOINTDISCOVERYSERVICE = DESCRIPTOR.services_by_name['EndpointDiscoveryService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'io.envoyproxy.envoy.service.endpoint.v3B\010EdsProtoP\001ZKgithub.com/envoyproxy/go-control-plane/envoy/service/endpoint/v3;endpointv3\210\001\001\272\200\310\321\006\002\020\002'
  _EDSDUMMY._options = None
  _EDSDUMMY._serialized_options = b'\232\305\210\036\027\n\025envoy.api.v2.EdsDummy'
  _ENDPOINTDISCOVERYSERVICE._options = None
  _ENDPOINTDISCOVERYSERVICE._serialized_options = b'\212\244\226\363\0070\n.envoy.config.endpoint.v3.ClusterLoadAssignment'
  _ENDPOINTDISCOVERYSERVICE.methods_by_name['FetchEndpoints']._options = None
  _ENDPOINTDISCOVERYSERVICE.methods_by_name['FetchEndpoints']._serialized_options = b'\202\323\344\223\002\031\"\027/v3/discovery:endpoints\202\323\344\223\002\003:\001*'
  _EDSDUMMY._serialized_start=240
  _EDSDUMMY._serialized_end=280
  _ENDPOINTDISCOVERYSERVICE._serialized_start=283
  _ENDPOINTDISCOVERYSERVICE._serialized_end=764
# @@protoc_insertion_point(module_scope)
