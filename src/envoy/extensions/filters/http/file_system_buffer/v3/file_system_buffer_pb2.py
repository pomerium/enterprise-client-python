# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/http/file_system_buffer/v3/file_system_buffer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.extensions.common.async_files.v3 import async_file_manager_pb2 as envoy_dot_extensions_dot_common_dot_async__files_dot_v3_dot_async__file__manager__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from xds.annotations.v3 import status_pb2 as xds_dot_annotations_dot_v3_dot_status__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLenvoy/extensions/filters/http/file_system_buffer/v3/file_system_buffer.proto\x12\x33\x65nvoy.extensions.filters.http.file_system_buffer.v3\x1a?envoy/extensions/common/async_files/v3/async_file_manager.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fxds/annotations/v3/status.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\x96\x06\n\x0e\x42ufferBehavior\x12v\n\x14stream_when_possible\x18\x01 \x01(\x0b\x32V.envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.StreamWhenPossibleH\x00\x12\\\n\x06\x62ypass\x18\x02 \x01(\x0b\x32J.envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.BypassH\x00\x12\x90\x01\n\"inject_content_length_if_necessary\x18\x03 \x01(\x0b\x32\x62.envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.InjectContentLengthIfNecessaryH\x00\x12\xa4\x01\n-fully_buffer_and_always_inject_content_length\x18\x04 \x01(\x0b\x32k.envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.FullyBufferAndAlwaysInjectContentLengthH\x00\x12g\n\x0c\x66ully_buffer\x18\x05 \x01(\x0b\x32O.envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.FullyBufferH\x00\x1a\x14\n\x12StreamWhenPossible\x1a\x08\n\x06\x42ypass\x1a \n\x1eInjectContentLengthIfNecessary\x1a)\n\'FullyBufferAndAlwaysInjectContentLength\x1a\r\n\x0b\x46ullyBufferB\x0f\n\x08\x62\x65havior\x12\x03\xf8\x42\x01\"\xc2\x02\n\x0cStreamConfig\x12U\n\x08\x62\x65havior\x18\x01 \x01(\x0b\x32\x43.envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior\x12H\n\x19memory_buffer_bytes_limit\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\x07\xfa\x42\x04\x32\x02 \x00\x12@\n\x1astorage_buffer_bytes_limit\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12O\n)storage_buffer_queue_high_watermark_bytes\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\"\xda\x02\n\x1c\x46ileSystemBufferFilterConfig\x12V\n\x0emanager_config\x18\x01 \x01(\x0b\x32>.envoy.extensions.common.async_files.v3.AsyncFileManagerConfig\x12\x39\n\x13storage_buffer_path\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12R\n\x07request\x18\x03 \x01(\x0b\x32\x41.envoy.extensions.filters.http.file_system_buffer.v3.StreamConfig\x12S\n\x08response\x18\x04 \x01(\x0b\x32\x41.envoy.extensions.filters.http.file_system_buffer.v3.StreamConfigB\xdd\x01\nAio.envoyproxy.envoy.extensions.filters.http.file_system_buffer.v3B\x15\x46ileSystemBufferProtoP\x01Zogithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/file_system_buffer/v3;file_system_bufferv3\xba\x80\xc8\xd1\x06\x02\x10\x02\xd2\xc6\xa4\xe1\x06\x02\x08\x01\x62\x06proto3')



_BUFFERBEHAVIOR = DESCRIPTOR.message_types_by_name['BufferBehavior']
_BUFFERBEHAVIOR_STREAMWHENPOSSIBLE = _BUFFERBEHAVIOR.nested_types_by_name['StreamWhenPossible']
_BUFFERBEHAVIOR_BYPASS = _BUFFERBEHAVIOR.nested_types_by_name['Bypass']
_BUFFERBEHAVIOR_INJECTCONTENTLENGTHIFNECESSARY = _BUFFERBEHAVIOR.nested_types_by_name['InjectContentLengthIfNecessary']
_BUFFERBEHAVIOR_FULLYBUFFERANDALWAYSINJECTCONTENTLENGTH = _BUFFERBEHAVIOR.nested_types_by_name['FullyBufferAndAlwaysInjectContentLength']
_BUFFERBEHAVIOR_FULLYBUFFER = _BUFFERBEHAVIOR.nested_types_by_name['FullyBuffer']
_STREAMCONFIG = DESCRIPTOR.message_types_by_name['StreamConfig']
_FILESYSTEMBUFFERFILTERCONFIG = DESCRIPTOR.message_types_by_name['FileSystemBufferFilterConfig']
BufferBehavior = _reflection.GeneratedProtocolMessageType('BufferBehavior', (_message.Message,), {

  'StreamWhenPossible' : _reflection.GeneratedProtocolMessageType('StreamWhenPossible', (_message.Message,), {
    'DESCRIPTOR' : _BUFFERBEHAVIOR_STREAMWHENPOSSIBLE,
    '__module__' : 'envoy.extensions.filters.http.file_system_buffer.v3.file_system_buffer_pb2'
    # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.StreamWhenPossible)
    })
  ,

  'Bypass' : _reflection.GeneratedProtocolMessageType('Bypass', (_message.Message,), {
    'DESCRIPTOR' : _BUFFERBEHAVIOR_BYPASS,
    '__module__' : 'envoy.extensions.filters.http.file_system_buffer.v3.file_system_buffer_pb2'
    # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.Bypass)
    })
  ,

  'InjectContentLengthIfNecessary' : _reflection.GeneratedProtocolMessageType('InjectContentLengthIfNecessary', (_message.Message,), {
    'DESCRIPTOR' : _BUFFERBEHAVIOR_INJECTCONTENTLENGTHIFNECESSARY,
    '__module__' : 'envoy.extensions.filters.http.file_system_buffer.v3.file_system_buffer_pb2'
    # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.InjectContentLengthIfNecessary)
    })
  ,

  'FullyBufferAndAlwaysInjectContentLength' : _reflection.GeneratedProtocolMessageType('FullyBufferAndAlwaysInjectContentLength', (_message.Message,), {
    'DESCRIPTOR' : _BUFFERBEHAVIOR_FULLYBUFFERANDALWAYSINJECTCONTENTLENGTH,
    '__module__' : 'envoy.extensions.filters.http.file_system_buffer.v3.file_system_buffer_pb2'
    # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.FullyBufferAndAlwaysInjectContentLength)
    })
  ,

  'FullyBuffer' : _reflection.GeneratedProtocolMessageType('FullyBuffer', (_message.Message,), {
    'DESCRIPTOR' : _BUFFERBEHAVIOR_FULLYBUFFER,
    '__module__' : 'envoy.extensions.filters.http.file_system_buffer.v3.file_system_buffer_pb2'
    # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior.FullyBuffer)
    })
  ,
  'DESCRIPTOR' : _BUFFERBEHAVIOR,
  '__module__' : 'envoy.extensions.filters.http.file_system_buffer.v3.file_system_buffer_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.file_system_buffer.v3.BufferBehavior)
  })
_sym_db.RegisterMessage(BufferBehavior)
_sym_db.RegisterMessage(BufferBehavior.StreamWhenPossible)
_sym_db.RegisterMessage(BufferBehavior.Bypass)
_sym_db.RegisterMessage(BufferBehavior.InjectContentLengthIfNecessary)
_sym_db.RegisterMessage(BufferBehavior.FullyBufferAndAlwaysInjectContentLength)
_sym_db.RegisterMessage(BufferBehavior.FullyBuffer)

StreamConfig = _reflection.GeneratedProtocolMessageType('StreamConfig', (_message.Message,), {
  'DESCRIPTOR' : _STREAMCONFIG,
  '__module__' : 'envoy.extensions.filters.http.file_system_buffer.v3.file_system_buffer_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.file_system_buffer.v3.StreamConfig)
  })
_sym_db.RegisterMessage(StreamConfig)

FileSystemBufferFilterConfig = _reflection.GeneratedProtocolMessageType('FileSystemBufferFilterConfig', (_message.Message,), {
  'DESCRIPTOR' : _FILESYSTEMBUFFERFILTERCONFIG,
  '__module__' : 'envoy.extensions.filters.http.file_system_buffer.v3.file_system_buffer_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.file_system_buffer.v3.FileSystemBufferFilterConfig)
  })
_sym_db.RegisterMessage(FileSystemBufferFilterConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nAio.envoyproxy.envoy.extensions.filters.http.file_system_buffer.v3B\025FileSystemBufferProtoP\001Zogithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/file_system_buffer/v3;file_system_bufferv3\272\200\310\321\006\002\020\002\322\306\244\341\006\002\010\001'
  _BUFFERBEHAVIOR.oneofs_by_name['behavior']._options = None
  _BUFFERBEHAVIOR.oneofs_by_name['behavior']._serialized_options = b'\370B\001'
  _STREAMCONFIG.fields_by_name['memory_buffer_bytes_limit']._options = None
  _STREAMCONFIG.fields_by_name['memory_buffer_bytes_limit']._serialized_options = b'\372B\0042\002 \000'
  _BUFFERBEHAVIOR._serialized_start=320
  _BUFFERBEHAVIOR._serialized_end=1110
  _BUFFERBEHAVIOR_STREAMWHENPOSSIBLE._serialized_start=971
  _BUFFERBEHAVIOR_STREAMWHENPOSSIBLE._serialized_end=991
  _BUFFERBEHAVIOR_BYPASS._serialized_start=993
  _BUFFERBEHAVIOR_BYPASS._serialized_end=1001
  _BUFFERBEHAVIOR_INJECTCONTENTLENGTHIFNECESSARY._serialized_start=1003
  _BUFFERBEHAVIOR_INJECTCONTENTLENGTHIFNECESSARY._serialized_end=1035
  _BUFFERBEHAVIOR_FULLYBUFFERANDALWAYSINJECTCONTENTLENGTH._serialized_start=1037
  _BUFFERBEHAVIOR_FULLYBUFFERANDALWAYSINJECTCONTENTLENGTH._serialized_end=1078
  _BUFFERBEHAVIOR_FULLYBUFFER._serialized_start=1080
  _BUFFERBEHAVIOR_FULLYBUFFER._serialized_end=1093
  _STREAMCONFIG._serialized_start=1113
  _STREAMCONFIG._serialized_end=1435
  _FILESYSTEMBUFFERFILTERCONFIG._serialized_start=1438
  _FILESYSTEMBUFFERFILTERCONFIG._serialized_end=1784
# @@protoc_insertion_point(module_scope)
