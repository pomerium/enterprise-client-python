# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/core/v3/address.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import socket_option_pb2 as envoy_dot_config_dot_core_dot_v3_dot_socket__option__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/core/v3/address.proto',
  package='envoy.config.core.v3',
  syntax='proto3',
  serialized_options=b'\n\"io.envoyproxy.envoy.config.core.v3B\014AddressProtoP\001ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"envoy/config/core/v3/address.proto\x12\x14\x65nvoy.config.core.v3\x1a(envoy/config/core/v3/socket_option.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"T\n\x04Pipe\x12\x15\n\x04path\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x16\n\x04mode\x18\x02 \x01(\rB\x08\xfa\x42\x05*\x03\x18\xff\x03:\x1d\x9a\xc5\x88\x1e\x18\n\x16\x65nvoy.api.v2.core.Pipe\"U\n\x14\x45nvoyInternalAddress\x12\x1e\n\x14server_listener_name\x18\x01 \x01(\tH\x00\x42\x1d\n\x16\x61\x64\x64ress_name_specifier\x12\x03\xf8\x42\x01\"\xb3\x02\n\rSocketAddress\x12H\n\x08protocol\x18\x01 \x01(\x0e\x32,.envoy.config.core.v3.SocketAddress.ProtocolB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x1f\n\nport_value\x18\x03 \x01(\rB\t\xfa\x42\x06*\x04\x18\xff\xff\x03H\x00\x12\x14\n\nnamed_port\x18\x04 \x01(\tH\x00\x12\x15\n\rresolver_name\x18\x05 \x01(\t\x12\x13\n\x0bipv4_compat\x18\x06 \x01(\x08\"\x1c\n\x08Protocol\x12\x07\n\x03TCP\x10\x00\x12\x07\n\x03UDP\x10\x01:&\x9a\xc5\x88\x1e!\n\x1f\x65nvoy.api.v2.core.SocketAddressB\x15\n\x0eport_specifier\x12\x03\xf8\x42\x01\"\xdd\x01\n\x0cTcpKeepalive\x12\x36\n\x10keepalive_probes\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x34\n\x0ekeepalive_time\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x38\n\x12keepalive_interval\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value:%\x9a\xc5\x88\x1e \n\x1e\x65nvoy.api.v2.core.TcpKeepalive\"\xe2\x01\n\nBindConfig\x12\x45\n\x0esource_address\x18\x01 \x01(\x0b\x32#.envoy.config.core.v3.SocketAddressB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12,\n\x08\x66reebind\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x0esocket_options\x18\x03 \x03(\x0b\x32\".envoy.config.core.v3.SocketOption:#\x9a\xc5\x88\x1e\x1e\n\x1c\x65nvoy.api.v2.core.BindConfig\"\xf4\x01\n\x07\x41\x64\x64ress\x12=\n\x0esocket_address\x18\x01 \x01(\x0b\x32#.envoy.config.core.v3.SocketAddressH\x00\x12*\n\x04pipe\x18\x02 \x01(\x0b\x32\x1a.envoy.config.core.v3.PipeH\x00\x12L\n\x16\x65nvoy_internal_address\x18\x03 \x01(\x0b\x32*.envoy.config.core.v3.EnvoyInternalAddressH\x00: \x9a\xc5\x88\x1e\x1b\n\x19\x65nvoy.api.v2.core.AddressB\x0e\n\x07\x61\x64\x64ress\x12\x03\xf8\x42\x01\"\x8c\x01\n\tCidrRange\x12\x1f\n\x0e\x61\x64\x64ress_prefix\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12:\n\nprefix_len\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x08\xfa\x42\x05*\x03\x18\x80\x01:\"\x9a\xc5\x88\x1e\x1d\n\x1b\x65nvoy.api.v2.core.CidrRangeB\x80\x01\n\"io.envoyproxy.envoy.config.core.v3B\x0c\x41\x64\x64ressProtoP\x01ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[envoy_dot_config_dot_core_dot_v3_dot_socket__option__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])



_SOCKETADDRESS_PROTOCOL = _descriptor.EnumDescriptor(
  name='Protocol',
  full_name='envoy.config.core.v3.SocketAddress.Protocol',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TCP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UDP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=615,
  serialized_end=643,
)
_sym_db.RegisterEnumDescriptor(_SOCKETADDRESS_PROTOCOL)


_PIPE = _descriptor.Descriptor(
  name='Pipe',
  full_name='envoy.config.core.v3.Pipe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='envoy.config.core.v3.Pipe.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mode', full_name='envoy.config.core.v3.Pipe.mode', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005*\003\030\377\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036\030\n\026envoy.api.v2.core.Pipe',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=309,
)


_ENVOYINTERNALADDRESS = _descriptor.Descriptor(
  name='EnvoyInternalAddress',
  full_name='envoy.config.core.v3.EnvoyInternalAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_listener_name', full_name='envoy.config.core.v3.EnvoyInternalAddress.server_listener_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='address_name_specifier', full_name='envoy.config.core.v3.EnvoyInternalAddress.address_name_specifier',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=311,
  serialized_end=396,
)


_SOCKETADDRESS = _descriptor.Descriptor(
  name='SocketAddress',
  full_name='envoy.config.core.v3.SocketAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='protocol', full_name='envoy.config.core.v3.SocketAddress.protocol', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\202\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='envoy.config.core.v3.SocketAddress.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port_value', full_name='envoy.config.core.v3.SocketAddress.port_value', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\006*\004\030\377\377\003', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='named_port', full_name='envoy.config.core.v3.SocketAddress.named_port', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resolver_name', full_name='envoy.config.core.v3.SocketAddress.resolver_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ipv4_compat', full_name='envoy.config.core.v3.SocketAddress.ipv4_compat', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SOCKETADDRESS_PROTOCOL,
  ],
  serialized_options=b'\232\305\210\036!\n\037envoy.api.v2.core.SocketAddress',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='port_specifier', full_name='envoy.config.core.v3.SocketAddress.port_specifier',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=399,
  serialized_end=706,
)


_TCPKEEPALIVE = _descriptor.Descriptor(
  name='TcpKeepalive',
  full_name='envoy.config.core.v3.TcpKeepalive',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keepalive_probes', full_name='envoy.config.core.v3.TcpKeepalive.keepalive_probes', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keepalive_time', full_name='envoy.config.core.v3.TcpKeepalive.keepalive_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keepalive_interval', full_name='envoy.config.core.v3.TcpKeepalive.keepalive_interval', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\232\305\210\036 \n\036envoy.api.v2.core.TcpKeepalive',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=709,
  serialized_end=930,
)


_BINDCONFIG = _descriptor.Descriptor(
  name='BindConfig',
  full_name='envoy.config.core.v3.BindConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='source_address', full_name='envoy.config.core.v3.BindConfig.source_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\212\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='freebind', full_name='envoy.config.core.v3.BindConfig.freebind', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='socket_options', full_name='envoy.config.core.v3.BindConfig.socket_options', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036\036\n\034envoy.api.v2.core.BindConfig',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=933,
  serialized_end=1159,
)


_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='envoy.config.core.v3.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='socket_address', full_name='envoy.config.core.v3.Address.socket_address', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pipe', full_name='envoy.config.core.v3.Address.pipe', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='envoy_internal_address', full_name='envoy.config.core.v3.Address.envoy_internal_address', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\232\305\210\036\033\n\031envoy.api.v2.core.Address',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='address', full_name='envoy.config.core.v3.Address.address',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=1162,
  serialized_end=1406,
)


_CIDRRANGE = _descriptor.Descriptor(
  name='CidrRange',
  full_name='envoy.config.core.v3.CidrRange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_prefix', full_name='envoy.config.core.v3.CidrRange.address_prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prefix_len', full_name='envoy.config.core.v3.CidrRange.prefix_len', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005*\003\030\200\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036\035\n\033envoy.api.v2.core.CidrRange',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1409,
  serialized_end=1549,
)

_ENVOYINTERNALADDRESS.oneofs_by_name['address_name_specifier'].fields.append(
  _ENVOYINTERNALADDRESS.fields_by_name['server_listener_name'])
_ENVOYINTERNALADDRESS.fields_by_name['server_listener_name'].containing_oneof = _ENVOYINTERNALADDRESS.oneofs_by_name['address_name_specifier']
_SOCKETADDRESS.fields_by_name['protocol'].enum_type = _SOCKETADDRESS_PROTOCOL
_SOCKETADDRESS_PROTOCOL.containing_type = _SOCKETADDRESS
_SOCKETADDRESS.oneofs_by_name['port_specifier'].fields.append(
  _SOCKETADDRESS.fields_by_name['port_value'])
_SOCKETADDRESS.fields_by_name['port_value'].containing_oneof = _SOCKETADDRESS.oneofs_by_name['port_specifier']
_SOCKETADDRESS.oneofs_by_name['port_specifier'].fields.append(
  _SOCKETADDRESS.fields_by_name['named_port'])
_SOCKETADDRESS.fields_by_name['named_port'].containing_oneof = _SOCKETADDRESS.oneofs_by_name['port_specifier']
_TCPKEEPALIVE.fields_by_name['keepalive_probes'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TCPKEEPALIVE.fields_by_name['keepalive_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_TCPKEEPALIVE.fields_by_name['keepalive_interval'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_BINDCONFIG.fields_by_name['source_address'].message_type = _SOCKETADDRESS
_BINDCONFIG.fields_by_name['freebind'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_BINDCONFIG.fields_by_name['socket_options'].message_type = envoy_dot_config_dot_core_dot_v3_dot_socket__option__pb2._SOCKETOPTION
_ADDRESS.fields_by_name['socket_address'].message_type = _SOCKETADDRESS
_ADDRESS.fields_by_name['pipe'].message_type = _PIPE
_ADDRESS.fields_by_name['envoy_internal_address'].message_type = _ENVOYINTERNALADDRESS
_ADDRESS.oneofs_by_name['address'].fields.append(
  _ADDRESS.fields_by_name['socket_address'])
_ADDRESS.fields_by_name['socket_address'].containing_oneof = _ADDRESS.oneofs_by_name['address']
_ADDRESS.oneofs_by_name['address'].fields.append(
  _ADDRESS.fields_by_name['pipe'])
_ADDRESS.fields_by_name['pipe'].containing_oneof = _ADDRESS.oneofs_by_name['address']
_ADDRESS.oneofs_by_name['address'].fields.append(
  _ADDRESS.fields_by_name['envoy_internal_address'])
_ADDRESS.fields_by_name['envoy_internal_address'].containing_oneof = _ADDRESS.oneofs_by_name['address']
_CIDRRANGE.fields_by_name['prefix_len'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
DESCRIPTOR.message_types_by_name['Pipe'] = _PIPE
DESCRIPTOR.message_types_by_name['EnvoyInternalAddress'] = _ENVOYINTERNALADDRESS
DESCRIPTOR.message_types_by_name['SocketAddress'] = _SOCKETADDRESS
DESCRIPTOR.message_types_by_name['TcpKeepalive'] = _TCPKEEPALIVE
DESCRIPTOR.message_types_by_name['BindConfig'] = _BINDCONFIG
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['CidrRange'] = _CIDRRANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pipe = _reflection.GeneratedProtocolMessageType('Pipe', (_message.Message,), {
  'DESCRIPTOR' : _PIPE,
  '__module__' : 'envoy.config.core.v3.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.Pipe)
  })
_sym_db.RegisterMessage(Pipe)

EnvoyInternalAddress = _reflection.GeneratedProtocolMessageType('EnvoyInternalAddress', (_message.Message,), {
  'DESCRIPTOR' : _ENVOYINTERNALADDRESS,
  '__module__' : 'envoy.config.core.v3.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.EnvoyInternalAddress)
  })
_sym_db.RegisterMessage(EnvoyInternalAddress)

SocketAddress = _reflection.GeneratedProtocolMessageType('SocketAddress', (_message.Message,), {
  'DESCRIPTOR' : _SOCKETADDRESS,
  '__module__' : 'envoy.config.core.v3.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.SocketAddress)
  })
_sym_db.RegisterMessage(SocketAddress)

TcpKeepalive = _reflection.GeneratedProtocolMessageType('TcpKeepalive', (_message.Message,), {
  'DESCRIPTOR' : _TCPKEEPALIVE,
  '__module__' : 'envoy.config.core.v3.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.TcpKeepalive)
  })
_sym_db.RegisterMessage(TcpKeepalive)

BindConfig = _reflection.GeneratedProtocolMessageType('BindConfig', (_message.Message,), {
  'DESCRIPTOR' : _BINDCONFIG,
  '__module__' : 'envoy.config.core.v3.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.BindConfig)
  })
_sym_db.RegisterMessage(BindConfig)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESS,
  '__module__' : 'envoy.config.core.v3.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.Address)
  })
_sym_db.RegisterMessage(Address)

CidrRange = _reflection.GeneratedProtocolMessageType('CidrRange', (_message.Message,), {
  'DESCRIPTOR' : _CIDRRANGE,
  '__module__' : 'envoy.config.core.v3.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.CidrRange)
  })
_sym_db.RegisterMessage(CidrRange)


DESCRIPTOR._options = None
_PIPE.fields_by_name['path']._options = None
_PIPE.fields_by_name['mode']._options = None
_PIPE._options = None
_ENVOYINTERNALADDRESS.oneofs_by_name['address_name_specifier']._options = None
_SOCKETADDRESS.oneofs_by_name['port_specifier']._options = None
_SOCKETADDRESS.fields_by_name['protocol']._options = None
_SOCKETADDRESS.fields_by_name['address']._options = None
_SOCKETADDRESS.fields_by_name['port_value']._options = None
_SOCKETADDRESS._options = None
_TCPKEEPALIVE._options = None
_BINDCONFIG.fields_by_name['source_address']._options = None
_BINDCONFIG._options = None
_ADDRESS.oneofs_by_name['address']._options = None
_ADDRESS._options = None
_CIDRRANGE.fields_by_name['address_prefix']._options = None
_CIDRRANGE.fields_by_name['prefix_len']._options = None
_CIDRRANGE._options = None
# @@protoc_insertion_point(module_scope)
