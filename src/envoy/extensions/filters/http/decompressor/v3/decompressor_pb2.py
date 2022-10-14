# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/http/decompressor/v3/decompressor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.config.core.v3 import extension_pb2 as envoy_dot_config_dot_core_dot_v3_dot_extension__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@envoy/extensions/filters/http/decompressor/v3/decompressor.proto\x12-envoy.extensions.filters.http.decompressor.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a$envoy/config/core/v3/extension.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\x92\x06\n\x0c\x44\x65\x63ompressor\x12R\n\x14\x64\x65\x63ompressor_library\x18\x01 \x01(\x0b\x32*.envoy.config.core.v3.TypedExtensionConfigB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12t\n\x18request_direction_config\x18\x02 \x01(\x0b\x32R.envoy.extensions.filters.http.decompressor.v3.Decompressor.RequestDirectionConfig\x12v\n\x19response_direction_config\x18\x03 \x01(\x0b\x32S.envoy.extensions.filters.http.decompressor.v3.Decompressor.ResponseDirectionConfig\x1av\n\x15\x43ommonDirectionConfig\x12\x39\n\x07\x65nabled\x18\x01 \x01(\x0b\x32(.envoy.config.core.v3.RuntimeFeatureFlag\x12\"\n\x1aignore_no_transform_header\x18\x02 \x01(\x08\x1a\xc1\x01\n\x16RequestDirectionConfig\x12h\n\rcommon_config\x18\x01 \x01(\x0b\x32Q.envoy.extensions.filters.http.decompressor.v3.Decompressor.CommonDirectionConfig\x12=\n\x19\x61\x64vertise_accept_encoding\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x1a\x83\x01\n\x17ResponseDirectionConfig\x12h\n\rcommon_config\x18\x01 \x01(\x0b\x32Q.envoy.extensions.filters.http.decompressor.v3.Decompressor.CommonDirectionConfigB\xbf\x01\n;io.envoyproxy.envoy.extensions.filters.http.decompressor.v3B\x11\x44\x65\x63ompressorProtoP\x01Zcgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/decompressor/v3;decompressorv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_DECOMPRESSOR = DESCRIPTOR.message_types_by_name['Decompressor']
_DECOMPRESSOR_COMMONDIRECTIONCONFIG = _DECOMPRESSOR.nested_types_by_name['CommonDirectionConfig']
_DECOMPRESSOR_REQUESTDIRECTIONCONFIG = _DECOMPRESSOR.nested_types_by_name['RequestDirectionConfig']
_DECOMPRESSOR_RESPONSEDIRECTIONCONFIG = _DECOMPRESSOR.nested_types_by_name['ResponseDirectionConfig']
Decompressor = _reflection.GeneratedProtocolMessageType('Decompressor', (_message.Message,), {

  'CommonDirectionConfig' : _reflection.GeneratedProtocolMessageType('CommonDirectionConfig', (_message.Message,), {
    'DESCRIPTOR' : _DECOMPRESSOR_COMMONDIRECTIONCONFIG,
    '__module__' : 'envoy.extensions.filters.http.decompressor.v3.decompressor_pb2'
    # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.decompressor.v3.Decompressor.CommonDirectionConfig)
    })
  ,

  'RequestDirectionConfig' : _reflection.GeneratedProtocolMessageType('RequestDirectionConfig', (_message.Message,), {
    'DESCRIPTOR' : _DECOMPRESSOR_REQUESTDIRECTIONCONFIG,
    '__module__' : 'envoy.extensions.filters.http.decompressor.v3.decompressor_pb2'
    # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.decompressor.v3.Decompressor.RequestDirectionConfig)
    })
  ,

  'ResponseDirectionConfig' : _reflection.GeneratedProtocolMessageType('ResponseDirectionConfig', (_message.Message,), {
    'DESCRIPTOR' : _DECOMPRESSOR_RESPONSEDIRECTIONCONFIG,
    '__module__' : 'envoy.extensions.filters.http.decompressor.v3.decompressor_pb2'
    # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.decompressor.v3.Decompressor.ResponseDirectionConfig)
    })
  ,
  'DESCRIPTOR' : _DECOMPRESSOR,
  '__module__' : 'envoy.extensions.filters.http.decompressor.v3.decompressor_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.http.decompressor.v3.Decompressor)
  })
_sym_db.RegisterMessage(Decompressor)
_sym_db.RegisterMessage(Decompressor.CommonDirectionConfig)
_sym_db.RegisterMessage(Decompressor.RequestDirectionConfig)
_sym_db.RegisterMessage(Decompressor.ResponseDirectionConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n;io.envoyproxy.envoy.extensions.filters.http.decompressor.v3B\021DecompressorProtoP\001Zcgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/decompressor/v3;decompressorv3\272\200\310\321\006\002\020\002'
  _DECOMPRESSOR.fields_by_name['decompressor_library']._options = None
  _DECOMPRESSOR.fields_by_name['decompressor_library']._serialized_options = b'\372B\005\212\001\002\020\001'
  _DECOMPRESSOR._serialized_start=275
  _DECOMPRESSOR._serialized_end=1061
  _DECOMPRESSOR_COMMONDIRECTIONCONFIG._serialized_start=613
  _DECOMPRESSOR_COMMONDIRECTIONCONFIG._serialized_end=731
  _DECOMPRESSOR_REQUESTDIRECTIONCONFIG._serialized_start=734
  _DECOMPRESSOR_REQUESTDIRECTIONCONFIG._serialized_end=927
  _DECOMPRESSOR_RESPONSEDIRECTIONCONFIG._serialized_start=930
  _DECOMPRESSOR_RESPONSEDIRECTIONCONFIG._serialized_end=1061
# @@protoc_insertion_point(module_scope)