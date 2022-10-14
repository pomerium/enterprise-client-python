# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/data/tap/v3/http.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.data.tap.v3 import common_pb2 as envoy_dot_data_dot_tap_dot_v3_dot_common__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x65nvoy/data/tap/v3/http.proto\x12\x11\x65nvoy.data.tap.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a\x1e\x65nvoy/data/tap/v3/common.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"\x98\x03\n\x11HttpBufferedTrace\x12=\n\x07request\x18\x01 \x01(\x0b\x32,.envoy.data.tap.v3.HttpBufferedTrace.Message\x12>\n\x08response\x18\x02 \x01(\x0b\x32,.envoy.data.tap.v3.HttpBufferedTrace.Message\x1a\xd2\x01\n\x07Message\x12\x32\n\x07headers\x18\x01 \x03(\x0b\x32!.envoy.config.core.v3.HeaderValue\x12%\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x17.envoy.data.tap.v3.Body\x12\x33\n\x08trailers\x18\x03 \x03(\x0b\x32!.envoy.config.core.v3.HeaderValue:7\x9a\xc5\x88\x1e\x32\n0envoy.data.tap.v2alpha.HttpBufferedTrace.Message:/\x9a\xc5\x88\x1e*\n(envoy.data.tap.v2alpha.HttpBufferedTrace\"\xd8\x03\n\x18HttpStreamedTraceSegment\x12\x10\n\x08trace_id\x18\x01 \x01(\x04\x12:\n\x0frequest_headers\x18\x02 \x01(\x0b\x32\x1f.envoy.config.core.v3.HeaderMapH\x00\x12\x35\n\x12request_body_chunk\x18\x03 \x01(\x0b\x32\x17.envoy.data.tap.v3.BodyH\x00\x12;\n\x10request_trailers\x18\x04 \x01(\x0b\x32\x1f.envoy.config.core.v3.HeaderMapH\x00\x12;\n\x10response_headers\x18\x05 \x01(\x0b\x32\x1f.envoy.config.core.v3.HeaderMapH\x00\x12\x36\n\x13response_body_chunk\x18\x06 \x01(\x0b\x32\x17.envoy.data.tap.v3.BodyH\x00\x12<\n\x11response_trailers\x18\x07 \x01(\x0b\x32\x1f.envoy.config.core.v3.HeaderMapH\x00:6\x9a\xc5\x88\x1e\x31\n/envoy.data.tap.v2alpha.HttpStreamedTraceSegmentB\x0f\n\rmessage_pieceBv\n\x1fio.envoyproxy.envoy.data.tap.v3B\tHttpProtoP\x01Z>github.com/envoyproxy/go-control-plane/envoy/data/tap/v3;tapv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_HTTPBUFFEREDTRACE = DESCRIPTOR.message_types_by_name['HttpBufferedTrace']
_HTTPBUFFEREDTRACE_MESSAGE = _HTTPBUFFEREDTRACE.nested_types_by_name['Message']
_HTTPSTREAMEDTRACESEGMENT = DESCRIPTOR.message_types_by_name['HttpStreamedTraceSegment']
HttpBufferedTrace = _reflection.GeneratedProtocolMessageType('HttpBufferedTrace', (_message.Message,), {

  'Message' : _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
    'DESCRIPTOR' : _HTTPBUFFEREDTRACE_MESSAGE,
    '__module__' : 'envoy.data.tap.v3.http_pb2'
    # @@protoc_insertion_point(class_scope:envoy.data.tap.v3.HttpBufferedTrace.Message)
    })
  ,
  'DESCRIPTOR' : _HTTPBUFFEREDTRACE,
  '__module__' : 'envoy.data.tap.v3.http_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.tap.v3.HttpBufferedTrace)
  })
_sym_db.RegisterMessage(HttpBufferedTrace)
_sym_db.RegisterMessage(HttpBufferedTrace.Message)

HttpStreamedTraceSegment = _reflection.GeneratedProtocolMessageType('HttpStreamedTraceSegment', (_message.Message,), {
  'DESCRIPTOR' : _HTTPSTREAMEDTRACESEGMENT,
  '__module__' : 'envoy.data.tap.v3.http_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.tap.v3.HttpStreamedTraceSegment)
  })
_sym_db.RegisterMessage(HttpStreamedTraceSegment)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037io.envoyproxy.envoy.data.tap.v3B\tHttpProtoP\001Z>github.com/envoyproxy/go-control-plane/envoy/data/tap/v3;tapv3\272\200\310\321\006\002\020\002'
  _HTTPBUFFEREDTRACE_MESSAGE._options = None
  _HTTPBUFFEREDTRACE_MESSAGE._serialized_options = b'\232\305\210\0362\n0envoy.data.tap.v2alpha.HttpBufferedTrace.Message'
  _HTTPBUFFEREDTRACE._options = None
  _HTTPBUFFEREDTRACE._serialized_options = b'\232\305\210\036*\n(envoy.data.tap.v2alpha.HttpBufferedTrace'
  _HTTPSTREAMEDTRACESEGMENT._options = None
  _HTTPSTREAMEDTRACESEGMENT._serialized_options = b'\232\305\210\0361\n/envoy.data.tap.v2alpha.HttpStreamedTraceSegment'
  _HTTPBUFFEREDTRACE._serialized_start=183
  _HTTPBUFFEREDTRACE._serialized_end=591
  _HTTPBUFFEREDTRACE_MESSAGE._serialized_start=332
  _HTTPBUFFEREDTRACE_MESSAGE._serialized_end=542
  _HTTPSTREAMEDTRACESEGMENT._serialized_start=594
  _HTTPSTREAMEDTRACESEGMENT._serialized_end=1066
# @@protoc_insertion_point(module_scope)