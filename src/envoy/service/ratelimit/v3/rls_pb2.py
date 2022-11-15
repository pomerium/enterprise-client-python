# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/ratelimit/v3/rls.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.extensions.common.ratelimit.v3 import ratelimit_pb2 as envoy_dot_extensions_dot_common_dot_ratelimit_dot_v3_dot_ratelimit__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$envoy/service/ratelimit/v3/rls.proto\x12\x1a\x65nvoy.service.ratelimit.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a\x34\x65nvoy/extensions/common/ratelimit/v3/ratelimit.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xbb\x01\n\x10RateLimitRequest\x12\x0e\n\x06\x64omain\x18\x01 \x01(\t\x12N\n\x0b\x64\x65scriptors\x18\x02 \x03(\x0b\x32\x39.envoy.extensions.common.ratelimit.v3.RateLimitDescriptor\x12\x13\n\x0bhits_addend\x18\x03 \x01(\r:2\x9a\xc5\x88\x1e-\n+envoy.service.ratelimit.v2.RateLimitRequest\"\xa1\n\n\x11RateLimitResponse\x12H\n\x0coverall_code\x18\x01 \x01(\x0e\x32\x32.envoy.service.ratelimit.v3.RateLimitResponse.Code\x12P\n\x08statuses\x18\x02 \x03(\x0b\x32>.envoy.service.ratelimit.v3.RateLimitResponse.DescriptorStatus\x12\x42\n\x17response_headers_to_add\x18\x03 \x03(\x0b\x32!.envoy.config.core.v3.HeaderValue\x12\x41\n\x16request_headers_to_add\x18\x04 \x03(\x0b\x32!.envoy.config.core.v3.HeaderValue\x12\x10\n\x08raw_body\x18\x05 \x01(\x0c\x12\x31\n\x10\x64ynamic_metadata\x18\x06 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x42\n\x05quota\x18\x07 \x01(\x0b\x32\x33.envoy.service.ratelimit.v3.RateLimitResponse.Quota\x1a\xff\x01\n\tRateLimit\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x19\n\x11requests_per_unit\x18\x01 \x01(\r\x12J\n\x04unit\x18\x02 \x01(\x0e\x32<.envoy.service.ratelimit.v3.RateLimitResponse.RateLimit.Unit\">\n\x04Unit\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06SECOND\x10\x01\x12\n\n\x06MINUTE\x10\x02\x12\x08\n\x04HOUR\x10\x03\x12\x07\n\x03\x44\x41Y\x10\x04:=\x9a\xc5\x88\x1e\x38\n6envoy.service.ratelimit.v2.RateLimitResponse.RateLimit\x1ay\n\x05Quota\x12\x19\n\x08requests\x18\x01 \x01(\rB\x07\xfa\x42\x04*\x02 \x00\x12\x31\n\x0bvalid_until\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00\x12\n\n\x02id\x18\x03 \x01(\tB\x16\n\x14\x65xpiration_specifier\x1a\x80\x03\n\x10\x44\x65scriptorStatus\x12@\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x32.envoy.service.ratelimit.v3.RateLimitResponse.Code\x12N\n\rcurrent_limit\x18\x02 \x01(\x0b\x32\x37.envoy.service.ratelimit.v3.RateLimitResponse.RateLimit\x12\x17\n\x0flimit_remaining\x18\x03 \x01(\r\x12\x37\n\x14\x64uration_until_reset\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x42\n\x05quota\x18\x05 \x01(\x0b\x32\x33.envoy.service.ratelimit.v3.RateLimitResponse.Quota:D\x9a\xc5\x88\x1e?\n=envoy.service.ratelimit.v2.RateLimitResponse.DescriptorStatus\"+\n\x04\x43ode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x0e\n\nOVER_LIMIT\x10\x02:3\x9a\xc5\x88\x1e.\n,envoy.service.ratelimit.v2.RateLimitResponse2\x84\x01\n\x10RateLimitService\x12p\n\x0fShouldRateLimit\x12,.envoy.service.ratelimit.v3.RateLimitRequest\x1a-.envoy.service.ratelimit.v3.RateLimitResponse\"\x00\x42\x90\x01\n(io.envoyproxy.envoy.service.ratelimit.v3B\x08RlsProtoP\x01ZMgithub.com/envoyproxy/go-control-plane/envoy/service/ratelimit/v3;ratelimitv3\x88\x01\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_RATELIMITREQUEST = DESCRIPTOR.message_types_by_name['RateLimitRequest']
_RATELIMITRESPONSE = DESCRIPTOR.message_types_by_name['RateLimitResponse']
_RATELIMITRESPONSE_RATELIMIT = _RATELIMITRESPONSE.nested_types_by_name['RateLimit']
_RATELIMITRESPONSE_QUOTA = _RATELIMITRESPONSE.nested_types_by_name['Quota']
_RATELIMITRESPONSE_DESCRIPTORSTATUS = _RATELIMITRESPONSE.nested_types_by_name['DescriptorStatus']
_RATELIMITRESPONSE_RATELIMIT_UNIT = _RATELIMITRESPONSE_RATELIMIT.enum_types_by_name['Unit']
_RATELIMITRESPONSE_CODE = _RATELIMITRESPONSE.enum_types_by_name['Code']
RateLimitRequest = _reflection.GeneratedProtocolMessageType('RateLimitRequest', (_message.Message,), {
  'DESCRIPTOR' : _RATELIMITREQUEST,
  '__module__' : 'envoy.service.ratelimit.v3.rls_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.ratelimit.v3.RateLimitRequest)
  })
_sym_db.RegisterMessage(RateLimitRequest)

RateLimitResponse = _reflection.GeneratedProtocolMessageType('RateLimitResponse', (_message.Message,), {

  'RateLimit' : _reflection.GeneratedProtocolMessageType('RateLimit', (_message.Message,), {
    'DESCRIPTOR' : _RATELIMITRESPONSE_RATELIMIT,
    '__module__' : 'envoy.service.ratelimit.v3.rls_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.ratelimit.v3.RateLimitResponse.RateLimit)
    })
  ,

  'Quota' : _reflection.GeneratedProtocolMessageType('Quota', (_message.Message,), {
    'DESCRIPTOR' : _RATELIMITRESPONSE_QUOTA,
    '__module__' : 'envoy.service.ratelimit.v3.rls_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.ratelimit.v3.RateLimitResponse.Quota)
    })
  ,

  'DescriptorStatus' : _reflection.GeneratedProtocolMessageType('DescriptorStatus', (_message.Message,), {
    'DESCRIPTOR' : _RATELIMITRESPONSE_DESCRIPTORSTATUS,
    '__module__' : 'envoy.service.ratelimit.v3.rls_pb2'
    # @@protoc_insertion_point(class_scope:envoy.service.ratelimit.v3.RateLimitResponse.DescriptorStatus)
    })
  ,
  'DESCRIPTOR' : _RATELIMITRESPONSE,
  '__module__' : 'envoy.service.ratelimit.v3.rls_pb2'
  # @@protoc_insertion_point(class_scope:envoy.service.ratelimit.v3.RateLimitResponse)
  })
_sym_db.RegisterMessage(RateLimitResponse)
_sym_db.RegisterMessage(RateLimitResponse.RateLimit)
_sym_db.RegisterMessage(RateLimitResponse.Quota)
_sym_db.RegisterMessage(RateLimitResponse.DescriptorStatus)

_RATELIMITSERVICE = DESCRIPTOR.services_by_name['RateLimitService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(io.envoyproxy.envoy.service.ratelimit.v3B\010RlsProtoP\001ZMgithub.com/envoyproxy/go-control-plane/envoy/service/ratelimit/v3;ratelimitv3\210\001\001\272\200\310\321\006\002\020\002'
  _RATELIMITREQUEST._options = None
  _RATELIMITREQUEST._serialized_options = b'\232\305\210\036-\n+envoy.service.ratelimit.v2.RateLimitRequest'
  _RATELIMITRESPONSE_RATELIMIT._options = None
  _RATELIMITRESPONSE_RATELIMIT._serialized_options = b'\232\305\210\0368\n6envoy.service.ratelimit.v2.RateLimitResponse.RateLimit'
  _RATELIMITRESPONSE_QUOTA.fields_by_name['requests']._options = None
  _RATELIMITRESPONSE_QUOTA.fields_by_name['requests']._serialized_options = b'\372B\004*\002 \000'
  _RATELIMITRESPONSE_DESCRIPTORSTATUS._options = None
  _RATELIMITRESPONSE_DESCRIPTORSTATUS._serialized_options = b'\232\305\210\036?\n=envoy.service.ratelimit.v2.RateLimitResponse.DescriptorStatus'
  _RATELIMITRESPONSE._options = None
  _RATELIMITRESPONSE._serialized_options = b'\232\305\210\036.\n,envoy.service.ratelimit.v2.RateLimitResponse'
  _RATELIMITREQUEST._serialized_start=342
  _RATELIMITREQUEST._serialized_end=529
  _RATELIMITRESPONSE._serialized_start=532
  _RATELIMITRESPONSE._serialized_end=1845
  _RATELIMITRESPONSE_RATELIMIT._serialized_start=982
  _RATELIMITRESPONSE_RATELIMIT._serialized_end=1237
  _RATELIMITRESPONSE_RATELIMIT_UNIT._serialized_start=1112
  _RATELIMITRESPONSE_RATELIMIT_UNIT._serialized_end=1174
  _RATELIMITRESPONSE_QUOTA._serialized_start=1239
  _RATELIMITRESPONSE_QUOTA._serialized_end=1360
  _RATELIMITRESPONSE_DESCRIPTORSTATUS._serialized_start=1363
  _RATELIMITRESPONSE_DESCRIPTORSTATUS._serialized_end=1747
  _RATELIMITRESPONSE_CODE._serialized_start=1749
  _RATELIMITRESPONSE_CODE._serialized_end=1792
  _RATELIMITSERVICE._serialized_start=1848
  _RATELIMITSERVICE._serialized_end=1980
# @@protoc_insertion_point(module_scope)
