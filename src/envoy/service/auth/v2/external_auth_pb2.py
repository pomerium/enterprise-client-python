# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/auth/v2/external_auth.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import base_pb2 as envoy_dot_api_dot_v2_dot_core_dot_base__pb2
try:
  envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2 = envoy_dot_api_dot_v2_dot_core_dot_base__pb2.envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2
except AttributeError:
  envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2 = envoy_dot_api_dot_v2_dot_core_dot_base__pb2.envoy.api.v2.core.socket_option_pb2
from envoy.service.auth.v2 import attribute_context_pb2 as envoy_dot_service_dot_auth_dot_v2_dot_attribute__context__pb2
from envoy.type import http_status_pb2 as envoy_dot_type_dot_http__status__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)envoy/service/auth/v2/external_auth.proto\x12\x15\x65nvoy.service.auth.v2\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a-envoy/service/auth/v2/attribute_context.proto\x1a\x1c\x65nvoy/type/http_status.proto\x1a\x17google/rpc/status.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"K\n\x0c\x43heckRequest\x12;\n\nattributes\x18\x01 \x01(\x0b\x32\'.envoy.service.auth.v2.AttributeContext\"\x8b\x01\n\x12\x44\x65niedHttpResponse\x12\x30\n\x06status\x18\x01 \x01(\x0b\x32\x16.envoy.type.HttpStatusB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x35\n\x07headers\x18\x02 \x03(\x0b\x32$.envoy.api.v2.core.HeaderValueOption\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\"G\n\x0eOkHttpResponse\x12\x35\n\x07headers\x18\x02 \x03(\x0b\x32$.envoy.api.v2.core.HeaderValueOption\"\xc8\x01\n\rCheckResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.Status\x12\x44\n\x0f\x64\x65nied_response\x18\x02 \x01(\x0b\x32).envoy.service.auth.v2.DeniedHttpResponseH\x00\x12<\n\x0bok_response\x18\x03 \x01(\x0b\x32%.envoy.service.auth.v2.OkHttpResponseH\x00\x42\x0f\n\rhttp_response2e\n\rAuthorization\x12T\n\x05\x43heck\x12#.envoy.service.auth.v2.CheckRequest\x1a$.envoy.service.auth.v2.CheckResponse\"\x00\x42\x8a\x01\n#io.envoyproxy.envoy.service.auth.v2B\x11\x45xternalAuthProtoP\x01ZCgithub.com/envoyproxy/go-control-plane/envoy/service/auth/v2;authv2\x88\x01\x01\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')



_CHECKREQUEST = DESCRIPTOR.message_types_by_name['CheckRequest']
_DENIEDHTTPRESPONSE = DESCRIPTOR.message_types_by_name['DeniedHttpResponse']
_OKHTTPRESPONSE = DESCRIPTOR.message_types_by_name['OkHttpResponse']
_CHECKRESPONSE = DESCRIPTOR.message_types_by_name['CheckResponse']
CheckRequest = _reflection.GeneratedProtocolMessageType('CheckRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKREQUEST,
  '__module__' : 'envoy.service.auth.v2.external_auth_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.CheckRequest)
  })
_sym_db.RegisterMessage(CheckRequest)

DeniedHttpResponse = _reflection.GeneratedProtocolMessageType('DeniedHttpResponse', (_message.Message,), {
  'DESCRIPTOR' : _DENIEDHTTPRESPONSE,
  '__module__' : 'envoy.service.auth.v2.external_auth_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.DeniedHttpResponse)
  })
_sym_db.RegisterMessage(DeniedHttpResponse)

OkHttpResponse = _reflection.GeneratedProtocolMessageType('OkHttpResponse', (_message.Message,), {
  'DESCRIPTOR' : _OKHTTPRESPONSE,
  '__module__' : 'envoy.service.auth.v2.external_auth_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.OkHttpResponse)
  })
_sym_db.RegisterMessage(OkHttpResponse)

CheckResponse = _reflection.GeneratedProtocolMessageType('CheckResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKRESPONSE,
  '__module__' : 'envoy.service.auth.v2.external_auth_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.auth.v2.CheckResponse)
  })
_sym_db.RegisterMessage(CheckResponse)

_AUTHORIZATION = DESCRIPTOR.services_by_name['Authorization']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#io.envoyproxy.envoy.service.auth.v2B\021ExternalAuthProtoP\001ZCgithub.com/envoyproxy/go-control-plane/envoy/service/auth/v2;authv2\210\001\001\272\200\310\321\006\002\020\001'
  _DENIEDHTTPRESPONSE.fields_by_name['status']._options = None
  _DENIEDHTTPRESPONSE.fields_by_name['status']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CHECKREQUEST._serialized_start=256
  _CHECKREQUEST._serialized_end=331
  _DENIEDHTTPRESPONSE._serialized_start=334
  _DENIEDHTTPRESPONSE._serialized_end=473
  _OKHTTPRESPONSE._serialized_start=475
  _OKHTTPRESPONSE._serialized_end=546
  _CHECKRESPONSE._serialized_start=549
  _CHECKRESPONSE._serialized_end=749
  _AUTHORIZATION._serialized_start=751
  _AUTHORIZATION._serialized_end=852
# @@protoc_insertion_point(module_scope)