# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/transport_sockets/alts/v3/alts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5envoy/extensions/transport_sockets/alts/v3/alts.proto\x12*envoy.extensions.transport_sockets.alts.v3\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\x82\x01\n\x04\x41lts\x12#\n\x12handshaker_service\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x1d\n\x15peer_service_accounts\x18\x02 \x03(\t:6\x9a\xc5\x88\x1e\x31\n/envoy.config.transport_socket.alts.v2alpha.AltsB\xa9\x01\n8io.envoyproxy.envoy.extensions.transport_sockets.alts.v3B\tAltsProtoP\x01ZXgithub.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/alts/v3;altsv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_ALTS = DESCRIPTOR.message_types_by_name['Alts']
Alts = _reflection.GeneratedProtocolMessageType('Alts', (_message.Message,), {
  'DESCRIPTOR' : _ALTS,
  '__module__' : 'envoy.extensions.transport_sockets.alts.v3.alts_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.transport_sockets.alts.v3.Alts)
  })
_sym_db.RegisterMessage(Alts)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n8io.envoyproxy.envoy.extensions.transport_sockets.alts.v3B\tAltsProtoP\001ZXgithub.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/alts/v3;altsv3\272\200\310\321\006\002\020\002'
  _ALTS.fields_by_name['handshaker_service']._options = None
  _ALTS.fields_by_name['handshaker_service']._serialized_options = b'\372B\004r\002\020\001'
  _ALTS._options = None
  _ALTS._serialized_options = b'\232\305\210\0361\n/envoy.config.transport_socket.alts.v2alpha.Alts'
  _ALTS._serialized_start=193
  _ALTS._serialized_end=323
# @@protoc_insertion_point(module_scope)
