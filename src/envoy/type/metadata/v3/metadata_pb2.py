# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/metadata/v3/metadata.proto
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
  name='envoy/type/metadata/v3/metadata.proto',
  package='envoy.type.metadata.v3',
  syntax='proto3',
  serialized_options=b'\n$io.envoyproxy.envoy.type.metadata.v3B\rMetadataProtoP\001\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%envoy/type/metadata/v3/metadata.proto\x12\x16\x65nvoy.type.metadata.v3\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\x85\x02\n\x0bMetadataKey\x12\x14\n\x03key\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12G\n\x04path\x18\x02 \x03(\x0b\x32/.envoy.type.metadata.v3.MetadataKey.PathSegmentB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x1al\n\x0bPathSegment\x12\x16\n\x03key\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01H\x00:5\x9a\xc5\x88\x1e\x30\n.envoy.type.metadata.v2.MetadataKey.PathSegmentB\x0e\n\x07segment\x12\x03\xf8\x42\x01:)\x9a\xc5\x88\x1e$\n\"envoy.type.metadata.v2.MetadataKey\"\xb3\x04\n\x0cMetadataKind\x12?\n\x07request\x18\x01 \x01(\x0b\x32,.envoy.type.metadata.v3.MetadataKind.RequestH\x00\x12;\n\x05route\x18\x02 \x01(\x0b\x32*.envoy.type.metadata.v3.MetadataKind.RouteH\x00\x12?\n\x07\x63luster\x18\x03 \x01(\x0b\x32,.envoy.type.metadata.v3.MetadataKind.ClusterH\x00\x12\x39\n\x04host\x18\x04 \x01(\x0b\x32).envoy.type.metadata.v3.MetadataKind.HostH\x00\x1a=\n\x07Request:2\x9a\xc5\x88\x1e-\n+envoy.type.metadata.v2.MetadataKind.Request\x1a\x39\n\x05Route:0\x9a\xc5\x88\x1e+\n)envoy.type.metadata.v2.MetadataKind.Route\x1a=\n\x07\x43luster:2\x9a\xc5\x88\x1e-\n+envoy.type.metadata.v2.MetadataKind.Cluster\x1a\x37\n\x04Host:/\x9a\xc5\x88\x1e*\n(envoy.type.metadata.v2.MetadataKind.Host:*\x9a\xc5\x88\x1e%\n#envoy.type.metadata.v2.MetadataKindB\x0b\n\x04kind\x12\x03\xf8\x42\x01\x42?\n$io.envoyproxy.envoy.type.metadata.v3B\rMetadataProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_METADATAKEY_PATHSEGMENT = _descriptor.Descriptor(
  name='PathSegment',
  full_name='envoy.type.metadata.v3.MetadataKey.PathSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.type.metadata.v3.MetadataKey.PathSegment.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\0360\n.envoy.type.metadata.v2.MetadataKey.PathSegment',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='segment', full_name='envoy.type.metadata.v3.MetadataKey.PathSegment.segment',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=267,
  serialized_end=375,
)

_METADATAKEY = _descriptor.Descriptor(
  name='MetadataKey',
  full_name='envoy.type.metadata.v3.MetadataKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.type.metadata.v3.MetadataKey.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='envoy.type.metadata.v3.MetadataKey.path', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\222\001\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_METADATAKEY_PATHSEGMENT, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036$\n\"envoy.type.metadata.v2.MetadataKey',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=418,
)


_METADATAKIND_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='envoy.type.metadata.v3.MetadataKind.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036-\n+envoy.type.metadata.v2.MetadataKind.Request',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=687,
  serialized_end=748,
)

_METADATAKIND_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='envoy.type.metadata.v3.MetadataKind.Route',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036+\n)envoy.type.metadata.v2.MetadataKind.Route',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=750,
  serialized_end=807,
)

_METADATAKIND_CLUSTER = _descriptor.Descriptor(
  name='Cluster',
  full_name='envoy.type.metadata.v3.MetadataKind.Cluster',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036-\n+envoy.type.metadata.v2.MetadataKind.Cluster',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=809,
  serialized_end=870,
)

_METADATAKIND_HOST = _descriptor.Descriptor(
  name='Host',
  full_name='envoy.type.metadata.v3.MetadataKind.Host',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036*\n(envoy.type.metadata.v2.MetadataKind.Host',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=872,
  serialized_end=927,
)

_METADATAKIND = _descriptor.Descriptor(
  name='MetadataKind',
  full_name='envoy.type.metadata.v3.MetadataKind',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='envoy.type.metadata.v3.MetadataKind.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='route', full_name='envoy.type.metadata.v3.MetadataKind.route', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster', full_name='envoy.type.metadata.v3.MetadataKind.cluster', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='envoy.type.metadata.v3.MetadataKind.host', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_METADATAKIND_REQUEST, _METADATAKIND_ROUTE, _METADATAKIND_CLUSTER, _METADATAKIND_HOST, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036%\n#envoy.type.metadata.v2.MetadataKind',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='envoy.type.metadata.v3.MetadataKind.kind',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=421,
  serialized_end=984,
)

_METADATAKEY_PATHSEGMENT.containing_type = _METADATAKEY
_METADATAKEY_PATHSEGMENT.oneofs_by_name['segment'].fields.append(
  _METADATAKEY_PATHSEGMENT.fields_by_name['key'])
_METADATAKEY_PATHSEGMENT.fields_by_name['key'].containing_oneof = _METADATAKEY_PATHSEGMENT.oneofs_by_name['segment']
_METADATAKEY.fields_by_name['path'].message_type = _METADATAKEY_PATHSEGMENT
_METADATAKIND_REQUEST.containing_type = _METADATAKIND
_METADATAKIND_ROUTE.containing_type = _METADATAKIND
_METADATAKIND_CLUSTER.containing_type = _METADATAKIND
_METADATAKIND_HOST.containing_type = _METADATAKIND
_METADATAKIND.fields_by_name['request'].message_type = _METADATAKIND_REQUEST
_METADATAKIND.fields_by_name['route'].message_type = _METADATAKIND_ROUTE
_METADATAKIND.fields_by_name['cluster'].message_type = _METADATAKIND_CLUSTER
_METADATAKIND.fields_by_name['host'].message_type = _METADATAKIND_HOST
_METADATAKIND.oneofs_by_name['kind'].fields.append(
  _METADATAKIND.fields_by_name['request'])
_METADATAKIND.fields_by_name['request'].containing_oneof = _METADATAKIND.oneofs_by_name['kind']
_METADATAKIND.oneofs_by_name['kind'].fields.append(
  _METADATAKIND.fields_by_name['route'])
_METADATAKIND.fields_by_name['route'].containing_oneof = _METADATAKIND.oneofs_by_name['kind']
_METADATAKIND.oneofs_by_name['kind'].fields.append(
  _METADATAKIND.fields_by_name['cluster'])
_METADATAKIND.fields_by_name['cluster'].containing_oneof = _METADATAKIND.oneofs_by_name['kind']
_METADATAKIND.oneofs_by_name['kind'].fields.append(
  _METADATAKIND.fields_by_name['host'])
_METADATAKIND.fields_by_name['host'].containing_oneof = _METADATAKIND.oneofs_by_name['kind']
DESCRIPTOR.message_types_by_name['MetadataKey'] = _METADATAKEY
DESCRIPTOR.message_types_by_name['MetadataKind'] = _METADATAKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetadataKey = _reflection.GeneratedProtocolMessageType('MetadataKey', (_message.Message,), {

  'PathSegment' : _reflection.GeneratedProtocolMessageType('PathSegment', (_message.Message,), {
    'DESCRIPTOR' : _METADATAKEY_PATHSEGMENT,
    '__module__' : 'envoy.type.metadata.v3.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v3.MetadataKey.PathSegment)
    })
  ,
  'DESCRIPTOR' : _METADATAKEY,
  '__module__' : 'envoy.type.metadata.v3.metadata_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.metadata.v3.MetadataKey)
  })
_sym_db.RegisterMessage(MetadataKey)
_sym_db.RegisterMessage(MetadataKey.PathSegment)

MetadataKind = _reflection.GeneratedProtocolMessageType('MetadataKind', (_message.Message,), {

  'Request' : _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
    'DESCRIPTOR' : _METADATAKIND_REQUEST,
    '__module__' : 'envoy.type.metadata.v3.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v3.MetadataKind.Request)
    })
  ,

  'Route' : _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), {
    'DESCRIPTOR' : _METADATAKIND_ROUTE,
    '__module__' : 'envoy.type.metadata.v3.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v3.MetadataKind.Route)
    })
  ,

  'Cluster' : _reflection.GeneratedProtocolMessageType('Cluster', (_message.Message,), {
    'DESCRIPTOR' : _METADATAKIND_CLUSTER,
    '__module__' : 'envoy.type.metadata.v3.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v3.MetadataKind.Cluster)
    })
  ,

  'Host' : _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
    'DESCRIPTOR' : _METADATAKIND_HOST,
    '__module__' : 'envoy.type.metadata.v3.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v3.MetadataKind.Host)
    })
  ,
  'DESCRIPTOR' : _METADATAKIND,
  '__module__' : 'envoy.type.metadata.v3.metadata_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.metadata.v3.MetadataKind)
  })
_sym_db.RegisterMessage(MetadataKind)
_sym_db.RegisterMessage(MetadataKind.Request)
_sym_db.RegisterMessage(MetadataKind.Route)
_sym_db.RegisterMessage(MetadataKind.Cluster)
_sym_db.RegisterMessage(MetadataKind.Host)


DESCRIPTOR._options = None
_METADATAKEY_PATHSEGMENT.oneofs_by_name['segment']._options = None
_METADATAKEY_PATHSEGMENT.fields_by_name['key']._options = None
_METADATAKEY_PATHSEGMENT._options = None
_METADATAKEY.fields_by_name['key']._options = None
_METADATAKEY.fields_by_name['path']._options = None
_METADATAKEY._options = None
_METADATAKIND_REQUEST._options = None
_METADATAKIND_ROUTE._options = None
_METADATAKIND_CLUSTER._options = None
_METADATAKIND_HOST._options = None
_METADATAKIND.oneofs_by_name['kind']._options = None
_METADATAKIND._options = None
# @@protoc_insertion_point(module_scope)