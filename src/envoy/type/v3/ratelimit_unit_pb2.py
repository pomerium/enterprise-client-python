# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/v3/ratelimit_unit.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"envoy/type/v3/ratelimit_unit.proto\x12\renvoy.type.v3\x1a\x1dudpa/annotations/status.proto*G\n\rRateLimitUnit\x12\x0b\n\x07UNKNOWN\x10\x00\x12\n\n\x06SECOND\x10\x01\x12\n\n\x06MINUTE\x10\x02\x12\x08\n\x04HOUR\x10\x03\x12\x07\n\x03\x44\x41Y\x10\x04\x42x\n\x1bio.envoyproxy.envoy.type.v3B\x12RatelimitUnitProtoP\x01Z;github.com/envoyproxy/go-control-plane/envoy/type/v3;typev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_RATELIMITUNIT = DESCRIPTOR.enum_types_by_name['RateLimitUnit']
RateLimitUnit = enum_type_wrapper.EnumTypeWrapper(_RATELIMITUNIT)
UNKNOWN = 0
SECOND = 1
MINUTE = 2
HOUR = 3
DAY = 4


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.envoyproxy.envoy.type.v3B\022RatelimitUnitProtoP\001Z;github.com/envoyproxy/go-control-plane/envoy/type/v3;typev3\272\200\310\321\006\002\020\002'
  _RATELIMITUNIT._serialized_start=84
  _RATELIMITUNIT._serialized_end=155
# @@protoc_insertion_point(module_scope)
