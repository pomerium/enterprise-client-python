# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/core/v3/udp_socket_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/core/v3/udp_socket_config.proto',
  package='envoy.config.core.v3',
  syntax='proto3',
  serialized_options=b'\n\"io.envoyproxy.envoy.config.core.v3B\024UdpSocketConfigProtoP\001\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,envoy/config/core/v3/udp_socket_config.proto\x12\x14\x65nvoy.config.core.v3\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\x8a\x01\n\x0fUdpSocketConfig\x12G\n\x14max_rx_datagram_size\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\x0b\xfa\x42\x08\x32\x06\x10\x80\x80\x04 \x00\x12.\n\nprefer_gro\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValueBD\n\"io.envoyproxy.envoy.config.core.v3B\x14UdpSocketConfigProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_UDPSOCKETCONFIG = _descriptor.Descriptor(
  name='UdpSocketConfig',
  full_name='envoy.config.core.v3.UdpSocketConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_rx_datagram_size', full_name='envoy.config.core.v3.UdpSocketConfig.max_rx_datagram_size', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\0102\006\020\200\200\004 \000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prefer_gro', full_name='envoy.config.core.v3.UdpSocketConfig.prefer_gro', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=297,
)

_UDPSOCKETCONFIG.fields_by_name['max_rx_datagram_size'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT64VALUE
_UDPSOCKETCONFIG.fields_by_name['prefer_gro'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
DESCRIPTOR.message_types_by_name['UdpSocketConfig'] = _UDPSOCKETCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UdpSocketConfig = _reflection.GeneratedProtocolMessageType('UdpSocketConfig', (_message.Message,), {
  'DESCRIPTOR' : _UDPSOCKETCONFIG,
  '__module__' : 'envoy.config.core.v3.udp_socket_config_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.UdpSocketConfig)
  })
_sym_db.RegisterMessage(UdpSocketConfig)


DESCRIPTOR._options = None
_UDPSOCKETCONFIG.fields_by_name['max_rx_datagram_size']._options = None
# @@protoc_insertion_point(module_scope)
