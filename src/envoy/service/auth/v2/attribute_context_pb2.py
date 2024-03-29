# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/auth/v2/attribute_context.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import address_pb2 as envoy_dot_api_dot_v2_dot_core_dot_address__pb2
from envoy.api.v2.core import base_pb2 as envoy_dot_api_dot_v2_dot_core_dot_base__pb2
try:
  envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2 = envoy_dot_api_dot_v2_dot_core_dot_base__pb2.envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2
except AttributeError:
  envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2 = envoy_dot_api_dot_v2_dot_core_dot_base__pb2.envoy.api.v2.core.socket_option_pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-envoy/service/auth/v2/attribute_context.proto\x12\x15\x65nvoy.service.auth.v2\x1a\x1f\x65nvoy/api/v2/core/address.proto\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dudpa/annotations/status.proto\"\xac\x08\n\x10\x41ttributeContext\x12<\n\x06source\x18\x01 \x01(\x0b\x32,.envoy.service.auth.v2.AttributeContext.Peer\x12\x41\n\x0b\x64\x65stination\x18\x02 \x01(\x0b\x32,.envoy.service.auth.v2.AttributeContext.Peer\x12@\n\x07request\x18\x04 \x01(\x0b\x32/.envoy.service.auth.v2.AttributeContext.Request\x12Z\n\x12\x63ontext_extensions\x18\n \x03(\x0b\x32>.envoy.service.auth.v2.AttributeContext.ContextExtensionsEntry\x12\x35\n\x10metadata_context\x18\x0b \x01(\x0b\x32\x1b.envoy.api.v2.core.Metadata\x1a\xe5\x01\n\x04Peer\x12+\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1a.envoy.api.v2.core.Address\x12\x0f\n\x07service\x18\x02 \x01(\t\x12H\n\x06labels\x18\x03 \x03(\x0b\x32\x38.envoy.service.auth.v2.AttributeContext.Peer.LabelsEntry\x12\x11\n\tprincipal\x18\x04 \x01(\t\x12\x13\n\x0b\x63\x65rtificate\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1av\n\x07Request\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\x04http\x18\x02 \x01(\x0b\x32\x33.envoy.service.auth.v2.AttributeContext.HttpRequest\x1a\xa7\x02\n\x0bHttpRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12Q\n\x07headers\x18\x03 \x03(\x0b\x32@.envoy.service.auth.v2.AttributeContext.HttpRequest.HeadersEntry\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0e\n\x06scheme\x18\x06 \x01(\t\x12\r\n\x05query\x18\x07 \x01(\t\x12\x10\n\x08\x66ragment\x18\x08 \x01(\t\x12\x0c\n\x04size\x18\t \x01(\x03\x12\x10\n\x08protocol\x18\n \x01(\t\x12\x0c\n\x04\x62ody\x18\x0b \x01(\t\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16\x43ontextExtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x8b\x01\n#io.envoyproxy.envoy.service.auth.v2B\x15\x41ttributeContextProtoP\x01ZCgithub.com/envoyproxy/go-control-plane/envoy/service/auth/v2;authv2\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')



_ATTRIBUTECONTEXT = DESCRIPTOR.message_types_by_name['AttributeContext']
_ATTRIBUTECONTEXT_PEER = _ATTRIBUTECONTEXT.nested_types_by_name['Peer']
_ATTRIBUTECONTEXT_PEER_LABELSENTRY = _ATTRIBUTECONTEXT_PEER.nested_types_by_name['LabelsEntry']
_ATTRIBUTECONTEXT_REQUEST = _ATTRIBUTECONTEXT.nested_types_by_name['Request']
_ATTRIBUTECONTEXT_HTTPREQUEST = _ATTRIBUTECONTEXT.nested_types_by_name['HttpRequest']
_ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY = _ATTRIBUTECONTEXT_HTTPREQUEST.nested_types_by_name['HeadersEntry']
_ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY = _ATTRIBUTECONTEXT.nested_types_by_name['ContextExtensionsEntry']
AttributeContext = _reflection.GeneratedProtocolMessageType('AttributeContext', (_message.Message,), {

  'Peer' : _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), {

    'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
      'DESCRIPTOR' : _ATTRIBUTECONTEXT_PEER_LABELSENTRY,
      '__module__' : 'envoy.service.auth.v2.attribute_context_pb2'
      # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.Peer.LabelsEntry)
      })
    ,
    'DESCRIPTOR' : _ATTRIBUTECONTEXT_PEER,
    '__module__' : 'envoy.service.auth.v2.attribute_context_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.Peer)
    })
  ,

  'Request' : _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
    'DESCRIPTOR' : _ATTRIBUTECONTEXT_REQUEST,
    '__module__' : 'envoy.service.auth.v2.attribute_context_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.Request)
    })
  ,

  'HttpRequest' : _reflection.GeneratedProtocolMessageType('HttpRequest', (_message.Message,), {

    'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
      'DESCRIPTOR' : _ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY,
      '__module__' : 'envoy.service.auth.v2.attribute_context_pb2'
      # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.HttpRequest.HeadersEntry)
      })
    ,
    'DESCRIPTOR' : _ATTRIBUTECONTEXT_HTTPREQUEST,
    '__module__' : 'envoy.service.auth.v2.attribute_context_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.HttpRequest)
    })
  ,

  'ContextExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ContextExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY,
    '__module__' : 'envoy.service.auth.v2.attribute_context_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext.ContextExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _ATTRIBUTECONTEXT,
  '__module__' : 'envoy.service.auth.v2.attribute_context_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.AttributeContext)
  })
_sym_db.RegisterMessage(AttributeContext)
_sym_db.RegisterMessage(AttributeContext.Peer)
_sym_db.RegisterMessage(AttributeContext.Peer.LabelsEntry)
_sym_db.RegisterMessage(AttributeContext.Request)
_sym_db.RegisterMessage(AttributeContext.HttpRequest)
_sym_db.RegisterMessage(AttributeContext.HttpRequest.HeadersEntry)
_sym_db.RegisterMessage(AttributeContext.ContextExtensionsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#io.envoyproxy.envoy.service.auth.v2B\025AttributeContextProtoP\001ZCgithub.com/envoyproxy/go-control-plane/envoy/service/auth/v2;authv2\272\200\310\321\006\002\020\001'
  _ATTRIBUTECONTEXT_PEER_LABELSENTRY._options = None
  _ATTRIBUTECONTEXT_PEER_LABELSENTRY._serialized_options = b'8\001'
  _ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY._options = None
  _ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY._serialized_options = b'8\001'
  _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY._options = None
  _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY._serialized_options = b'8\001'
  _ATTRIBUTECONTEXT._serialized_start=200
  _ATTRIBUTECONTEXT._serialized_end=1268
  _ATTRIBUTECONTEXT_PEER._serialized_start=563
  _ATTRIBUTECONTEXT_PEER._serialized_end=792
  _ATTRIBUTECONTEXT_PEER_LABELSENTRY._serialized_start=747
  _ATTRIBUTECONTEXT_PEER_LABELSENTRY._serialized_end=792
  _ATTRIBUTECONTEXT_REQUEST._serialized_start=794
  _ATTRIBUTECONTEXT_REQUEST._serialized_end=912
  _ATTRIBUTECONTEXT_HTTPREQUEST._serialized_start=915
  _ATTRIBUTECONTEXT_HTTPREQUEST._serialized_end=1210
  _ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY._serialized_start=1164
  _ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY._serialized_end=1210
  _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY._serialized_start=1212
  _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY._serialized_end=1268
# @@protoc_insertion_point(module_scope)
