# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/core/v3/address.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import socket_option_pb2 as envoy_dot_config_dot_core_dot_v3_dot_socket__option__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"envoy/config/core/v3/address.proto\x12\x14\x65nvoy.config.core.v3\x1a(envoy/config/core/v3/socket_option.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"T\n\x04Pipe\x12\x15\n\x04path\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x16\n\x04mode\x18\x02 \x01(\rB\x08\xfa\x42\x05*\x03\x18\xff\x03:\x1d\x9a\xc5\x88\x1e\x18\n\x16\x65nvoy.api.v2.core.Pipe\"j\n\x14\x45nvoyInternalAddress\x12\x1e\n\x14server_listener_name\x18\x01 \x01(\tH\x00\x12\x13\n\x0b\x65ndpoint_id\x18\x02 \x01(\tB\x1d\n\x16\x61\x64\x64ress_name_specifier\x12\x03\xf8\x42\x01\"\xb3\x02\n\rSocketAddress\x12H\n\x08protocol\x18\x01 \x01(\x0e\x32,.envoy.config.core.v3.SocketAddress.ProtocolB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x18\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x1f\n\nport_value\x18\x03 \x01(\rB\t\xfa\x42\x06*\x04\x18\xff\xff\x03H\x00\x12\x14\n\nnamed_port\x18\x04 \x01(\tH\x00\x12\x15\n\rresolver_name\x18\x05 \x01(\t\x12\x13\n\x0bipv4_compat\x18\x06 \x01(\x08\"\x1c\n\x08Protocol\x12\x07\n\x03TCP\x10\x00\x12\x07\n\x03UDP\x10\x01:&\x9a\xc5\x88\x1e!\n\x1f\x65nvoy.api.v2.core.SocketAddressB\x15\n\x0eport_specifier\x12\x03\xf8\x42\x01\"\xdd\x01\n\x0cTcpKeepalive\x12\x36\n\x10keepalive_probes\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x34\n\x0ekeepalive_time\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x38\n\x12keepalive_interval\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value:%\x9a\xc5\x88\x1e \n\x1e\x65nvoy.api.v2.core.TcpKeepalive\"\x99\x01\n\x12\x45xtraSourceAddress\x12>\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32#.envoy.config.core.v3.SocketAddressB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x43\n\x0esocket_options\x18\x02 \x01(\x0b\x32+.envoy.config.core.v3.SocketOptionsOverride\"\x83\x03\n\nBindConfig\x12\x45\n\x0esource_address\x18\x01 \x01(\x0b\x32#.envoy.config.core.v3.SocketAddressB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12,\n\x08\x66reebind\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x0esocket_options\x18\x03 \x03(\x0b\x32\".envoy.config.core.v3.SocketOption\x12H\n\x16\x65xtra_source_addresses\x18\x05 \x03(\x0b\x32(.envoy.config.core.v3.ExtraSourceAddress\x12U\n\x1b\x61\x64\x64itional_source_addresses\x18\x04 \x03(\x0b\x32#.envoy.config.core.v3.SocketAddressB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0:#\x9a\xc5\x88\x1e\x1e\n\x1c\x65nvoy.api.v2.core.BindConfig\"\xf4\x01\n\x07\x41\x64\x64ress\x12=\n\x0esocket_address\x18\x01 \x01(\x0b\x32#.envoy.config.core.v3.SocketAddressH\x00\x12*\n\x04pipe\x18\x02 \x01(\x0b\x32\x1a.envoy.config.core.v3.PipeH\x00\x12L\n\x16\x65nvoy_internal_address\x18\x03 \x01(\x0b\x32*.envoy.config.core.v3.EnvoyInternalAddressH\x00: \x9a\xc5\x88\x1e\x1b\n\x19\x65nvoy.api.v2.core.AddressB\x0e\n\x07\x61\x64\x64ress\x12\x03\xf8\x42\x01\"\x8c\x01\n\tCidrRange\x12\x1f\n\x0e\x61\x64\x64ress_prefix\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12:\n\nprefix_len\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x08\xfa\x42\x05*\x03\x18\x80\x01:\"\x9a\xc5\x88\x1e\x1d\n\x1b\x65nvoy.api.v2.core.CidrRangeB\x80\x01\n\"io.envoyproxy.envoy.config.core.v3B\x0c\x41\x64\x64ressProtoP\x01ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_PIPE = DESCRIPTOR.message_types_by_name['Pipe']
_ENVOYINTERNALADDRESS = DESCRIPTOR.message_types_by_name['EnvoyInternalAddress']
_SOCKETADDRESS = DESCRIPTOR.message_types_by_name['SocketAddress']
_TCPKEEPALIVE = DESCRIPTOR.message_types_by_name['TcpKeepalive']
_EXTRASOURCEADDRESS = DESCRIPTOR.message_types_by_name['ExtraSourceAddress']
_BINDCONFIG = DESCRIPTOR.message_types_by_name['BindConfig']
_ADDRESS = DESCRIPTOR.message_types_by_name['Address']
_CIDRRANGE = DESCRIPTOR.message_types_by_name['CidrRange']
_SOCKETADDRESS_PROTOCOL = _SOCKETADDRESS.enum_types_by_name['Protocol']
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

ExtraSourceAddress = _reflection.GeneratedProtocolMessageType('ExtraSourceAddress', (_message.Message,), {
  'DESCRIPTOR' : _EXTRASOURCEADDRESS,
  '__module__' : 'envoy.config.core.v3.address_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.ExtraSourceAddress)
  })
_sym_db.RegisterMessage(ExtraSourceAddress)

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

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"io.envoyproxy.envoy.config.core.v3B\014AddressProtoP\001ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\272\200\310\321\006\002\020\002'
  _PIPE.fields_by_name['path']._options = None
  _PIPE.fields_by_name['path']._serialized_options = b'\372B\004r\002\020\001'
  _PIPE.fields_by_name['mode']._options = None
  _PIPE.fields_by_name['mode']._serialized_options = b'\372B\005*\003\030\377\003'
  _PIPE._options = None
  _PIPE._serialized_options = b'\232\305\210\036\030\n\026envoy.api.v2.core.Pipe'
  _ENVOYINTERNALADDRESS.oneofs_by_name['address_name_specifier']._options = None
  _ENVOYINTERNALADDRESS.oneofs_by_name['address_name_specifier']._serialized_options = b'\370B\001'
  _SOCKETADDRESS.oneofs_by_name['port_specifier']._options = None
  _SOCKETADDRESS.oneofs_by_name['port_specifier']._serialized_options = b'\370B\001'
  _SOCKETADDRESS.fields_by_name['protocol']._options = None
  _SOCKETADDRESS.fields_by_name['protocol']._serialized_options = b'\372B\005\202\001\002\020\001'
  _SOCKETADDRESS.fields_by_name['address']._options = None
  _SOCKETADDRESS.fields_by_name['address']._serialized_options = b'\372B\004r\002\020\001'
  _SOCKETADDRESS.fields_by_name['port_value']._options = None
  _SOCKETADDRESS.fields_by_name['port_value']._serialized_options = b'\372B\006*\004\030\377\377\003'
  _SOCKETADDRESS._options = None
  _SOCKETADDRESS._serialized_options = b'\232\305\210\036!\n\037envoy.api.v2.core.SocketAddress'
  _TCPKEEPALIVE._options = None
  _TCPKEEPALIVE._serialized_options = b'\232\305\210\036 \n\036envoy.api.v2.core.TcpKeepalive'
  _EXTRASOURCEADDRESS.fields_by_name['address']._options = None
  _EXTRASOURCEADDRESS.fields_by_name['address']._serialized_options = b'\372B\005\212\001\002\020\001'
  _BINDCONFIG.fields_by_name['source_address']._options = None
  _BINDCONFIG.fields_by_name['source_address']._serialized_options = b'\372B\005\212\001\002\020\001'
  _BINDCONFIG.fields_by_name['additional_source_addresses']._options = None
  _BINDCONFIG.fields_by_name['additional_source_addresses']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _BINDCONFIG._options = None
  _BINDCONFIG._serialized_options = b'\232\305\210\036\036\n\034envoy.api.v2.core.BindConfig'
  _ADDRESS.oneofs_by_name['address']._options = None
  _ADDRESS.oneofs_by_name['address']._serialized_options = b'\370B\001'
  _ADDRESS._options = None
  _ADDRESS._serialized_options = b'\232\305\210\036\033\n\031envoy.api.v2.core.Address'
  _CIDRRANGE.fields_by_name['address_prefix']._options = None
  _CIDRRANGE.fields_by_name['address_prefix']._serialized_options = b'\372B\004r\002\020\001'
  _CIDRRANGE.fields_by_name['prefix_len']._options = None
  _CIDRRANGE.fields_by_name['prefix_len']._serialized_options = b'\372B\005*\003\030\200\001'
  _CIDRRANGE._options = None
  _CIDRRANGE._serialized_options = b'\232\305\210\036\035\n\033envoy.api.v2.core.CidrRange'
  _PIPE._serialized_start=262
  _PIPE._serialized_end=346
  _ENVOYINTERNALADDRESS._serialized_start=348
  _ENVOYINTERNALADDRESS._serialized_end=454
  _SOCKETADDRESS._serialized_start=457
  _SOCKETADDRESS._serialized_end=764
  _SOCKETADDRESS_PROTOCOL._serialized_start=673
  _SOCKETADDRESS_PROTOCOL._serialized_end=701
  _TCPKEEPALIVE._serialized_start=767
  _TCPKEEPALIVE._serialized_end=988
  _EXTRASOURCEADDRESS._serialized_start=991
  _EXTRASOURCEADDRESS._serialized_end=1144
  _BINDCONFIG._serialized_start=1147
  _BINDCONFIG._serialized_end=1534
  _ADDRESS._serialized_start=1537
  _ADDRESS._serialized_end=1781
  _CIDRRANGE._serialized_start=1784
  _CIDRRANGE._serialized_end=1924
# @@protoc_insertion_point(module_scope)
