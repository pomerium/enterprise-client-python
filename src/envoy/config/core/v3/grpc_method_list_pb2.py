# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/core/v3/grpc_method_list.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/core/v3/grpc_method_list.proto',
  package='envoy.config.core.v3',
  syntax='proto3',
  serialized_options=b'\n\"io.envoyproxy.envoy.config.core.v3B\023GrpcMethodListProtoP\001ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+envoy/config/core/v3/grpc_method_list.proto\x12\x14\x65nvoy.config.core.v3\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xec\x01\n\x0eGrpcMethodList\x12>\n\x08services\x18\x01 \x03(\x0b\x32,.envoy.config.core.v3.GrpcMethodList.Service\x1aq\n\x07Service\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x1e\n\x0cmethod_names\x18\x02 \x03(\tB\x08\xfa\x42\x05\x92\x01\x02\x08\x01:/\x9a\xc5\x88\x1e*\n(envoy.api.v2.core.GrpcMethodList.Service:\'\x9a\xc5\x88\x1e\"\n envoy.api.v2.core.GrpcMethodListB\x87\x01\n\"io.envoyproxy.envoy.config.core.v3B\x13GrpcMethodListProtoP\x01ZBgithub.com/envoyproxy/go-control-plane/envoy/config/core/v3;corev3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_GRPCMETHODLIST_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='envoy.config.core.v3.GrpcMethodList.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='envoy.config.core.v3.GrpcMethodList.Service.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='method_names', full_name='envoy.config.core.v3.GrpcMethodList.Service.method_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\222\001\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036*\n(envoy.api.v2.core.GrpcMethodList.Service',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=356,
)

_GRPCMETHODLIST = _descriptor.Descriptor(
  name='GrpcMethodList',
  full_name='envoy.config.core.v3.GrpcMethodList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='services', full_name='envoy.config.core.v3.GrpcMethodList.services', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GRPCMETHODLIST_SERVICE, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036\"\n envoy.api.v2.core.GrpcMethodList',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=397,
)

_GRPCMETHODLIST_SERVICE.containing_type = _GRPCMETHODLIST
_GRPCMETHODLIST.fields_by_name['services'].message_type = _GRPCMETHODLIST_SERVICE
DESCRIPTOR.message_types_by_name['GrpcMethodList'] = _GRPCMETHODLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GrpcMethodList = _reflection.GeneratedProtocolMessageType('GrpcMethodList', (_message.Message,), {

  'Service' : _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
    'DESCRIPTOR' : _GRPCMETHODLIST_SERVICE,
    '__module__' : 'envoy.config.core.v3.grpc_method_list_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.core.v3.GrpcMethodList.Service)
    })
  ,
  'DESCRIPTOR' : _GRPCMETHODLIST,
  '__module__' : 'envoy.config.core.v3.grpc_method_list_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.core.v3.GrpcMethodList)
  })
_sym_db.RegisterMessage(GrpcMethodList)
_sym_db.RegisterMessage(GrpcMethodList.Service)


DESCRIPTOR._options = None
_GRPCMETHODLIST_SERVICE.fields_by_name['name']._options = None
_GRPCMETHODLIST_SERVICE.fields_by_name['method_names']._options = None
_GRPCMETHODLIST_SERVICE._options = None
_GRPCMETHODLIST._options = None
# @@protoc_insertion_point(module_scope)
