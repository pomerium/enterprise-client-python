# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/http/ext_proc/v3/processing_mode.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?envoy/extensions/filters/http/ext_proc/v3/processing_mode.proto\x12)envoy.extensions.filters.http.ext_proc.v3\x1a\x1fxds/annotations/v3/status.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xb2\x06\n\x0eProcessingMode\x12o\n\x13request_header_mode\x18\x01 \x01(\x0e\x32H.envoy.extensions.filters.http.ext_proc.v3.ProcessingMode.HeaderSendModeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12p\n\x14response_header_mode\x18\x02 \x01(\x0e\x32H.envoy.extensions.filters.http.ext_proc.v3.ProcessingMode.HeaderSendModeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12k\n\x11request_body_mode\x18\x03 \x01(\x0e\x32\x46.envoy.extensions.filters.http.ext_proc.v3.ProcessingMode.BodySendModeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12l\n\x12response_body_mode\x18\x04 \x01(\x0e\x32\x46.envoy.extensions.filters.http.ext_proc.v3.ProcessingMode.BodySendModeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12p\n\x14request_trailer_mode\x18\x05 \x01(\x0e\x32H.envoy.extensions.filters.http.ext_proc.v3.ProcessingMode.HeaderSendModeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12q\n\x15response_trailer_mode\x18\x06 \x01(\x0e\x32H.envoy.extensions.filters.http.ext_proc.v3.ProcessingMode.HeaderSendModeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\"1\n\x0eHeaderSendMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x08\n\x04SEND\x10\x01\x12\x08\n\x04SKIP\x10\x02\"J\n\x0c\x42odySendMode\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08STREAMED\x10\x01\x12\x0c\n\x08\x42UFFERED\x10\x02\x12\x14\n\x10\x42UFFERED_PARTIAL\x10\x03\x42\xbd\x01\n7io.envoyproxy.envoy.extensions.filters.http.ext_proc.v3B\x13ProcessingModeProtoP\x01Z[github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/ext_proc/v3;ext_procv3\xba\x80\xc8\xd1\x06\x02\x10\x02\xd2\xc6\xa4\xe1\x06\x02\x08\x01\x62\x06proto3')



_PROCESSINGMODE = DESCRIPTOR.message_types_by_name['ProcessingMode']
_PROCESSINGMODE_HEADERSENDMODE = _PROCESSINGMODE.enum_types_by_name['HeaderSendMode']
_PROCESSINGMODE_BODYSENDMODE = _PROCESSINGMODE.enum_types_by_name['BodySendMode']
ProcessingMode = _reflection.GeneratedProtocolMessageType('ProcessingMode', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSINGMODE,
  '__module__' : 'envoy.extensions.filters.http.ext_proc.v3.processing_mode_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.ext_proc.v3.ProcessingMode)
  })
_sym_db.RegisterMessage(ProcessingMode)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n7io.envoyproxy.envoy.extensions.filters.http.ext_proc.v3B\023ProcessingModeProtoP\001Z[github.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/ext_proc/v3;ext_procv3\272\200\310\321\006\002\020\002\322\306\244\341\006\002\010\001'
  _PROCESSINGMODE.fields_by_name['request_header_mode']._options = None
  _PROCESSINGMODE.fields_by_name['request_header_mode']._serialized_options = b'\372B\005\202\001\002\020\001'
  _PROCESSINGMODE.fields_by_name['response_header_mode']._options = None
  _PROCESSINGMODE.fields_by_name['response_header_mode']._serialized_options = b'\372B\005\202\001\002\020\001'
  _PROCESSINGMODE.fields_by_name['request_body_mode']._options = None
  _PROCESSINGMODE.fields_by_name['request_body_mode']._serialized_options = b'\372B\005\202\001\002\020\001'
  _PROCESSINGMODE.fields_by_name['response_body_mode']._options = None
  _PROCESSINGMODE.fields_by_name['response_body_mode']._serialized_options = b'\372B\005\202\001\002\020\001'
  _PROCESSINGMODE.fields_by_name['request_trailer_mode']._options = None
  _PROCESSINGMODE.fields_by_name['request_trailer_mode']._serialized_options = b'\372B\005\202\001\002\020\001'
  _PROCESSINGMODE.fields_by_name['response_trailer_mode']._options = None
  _PROCESSINGMODE.fields_by_name['response_trailer_mode']._serialized_options = b'\372B\005\202\001\002\020\001'
  _PROCESSINGMODE._serialized_start=200
  _PROCESSINGMODE._serialized_end=1018
  _PROCESSINGMODE_HEADERSENDMODE._serialized_start=893
  _PROCESSINGMODE_HEADERSENDMODE._serialized_end=942
  _PROCESSINGMODE_BODYSENDMODE._serialized_start=944
  _PROCESSINGMODE_BODYSENDMODE._serialized_end=1018
# @@protoc_insertion_point(module_scope)
