# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/metadata/v2/metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/metadata/v2/metadata.proto',
  package='envoy.type.metadata.v2',
  syntax='proto3',
  serialized_options=b'\n$io.envoyproxy.envoy.type.metadata.v2B\rMetadataProtoP\001\362\230\376\217\005\030\022\026envoy.type.metadata.v3\272\200\310\321\006\002\020\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%envoy/type/metadata/v2/metadata.proto\x12\x16\x65nvoy.type.metadata.v2\x1a\x1eudpa/annotations/migrate.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xa3\x01\n\x0bMetadataKey\x12\x14\n\x03key\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x01\x12G\n\x04path\x18\x02 \x03(\x0b\x32/.envoy.type.metadata.v2.MetadataKey.PathSegmentB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x1a\x35\n\x0bPathSegment\x12\x16\n\x03key\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x01H\x00\x42\x0e\n\x07segment\x12\x03\xf8\x42\x01\"\xbc\x02\n\x0cMetadataKind\x12?\n\x07request\x18\x01 \x01(\x0b\x32,.envoy.type.metadata.v2.MetadataKind.RequestH\x00\x12;\n\x05route\x18\x02 \x01(\x0b\x32*.envoy.type.metadata.v2.MetadataKind.RouteH\x00\x12?\n\x07\x63luster\x18\x03 \x01(\x0b\x32,.envoy.type.metadata.v2.MetadataKind.ClusterH\x00\x12\x39\n\x04host\x18\x04 \x01(\x0b\x32).envoy.type.metadata.v2.MetadataKind.HostH\x00\x1a\t\n\x07Request\x1a\x07\n\x05Route\x1a\t\n\x07\x43luster\x1a\x06\n\x04HostB\x0b\n\x04kind\x12\x03\xf8\x42\x01\x42]\n$io.envoyproxy.envoy.type.metadata.v2B\rMetadataProtoP\x01\xf2\x98\xfe\x8f\x05\x18\x12\x16\x65nvoy.type.metadata.v3\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3'
  ,
  dependencies=[udpa_dot_annotations_dot_migrate__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_METADATAKEY_PATHSEGMENT = _descriptor.Descriptor(
  name='PathSegment',
  full_name='envoy.type.metadata.v2.MetadataKey.PathSegment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.type.metadata.v2.MetadataKey.PathSegment.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='segment', full_name='envoy.type.metadata.v2.MetadataKey.PathSegment.segment',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=264,
  serialized_end=317,
)

_METADATAKEY = _descriptor.Descriptor(
  name='MetadataKey',
  full_name='envoy.type.metadata.v2.MetadataKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.type.metadata.v2.MetadataKey.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002 \001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='path', full_name='envoy.type.metadata.v2.MetadataKey.path', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=317,
)


_METADATAKIND_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='envoy.type.metadata.v2.MetadataKind.Request',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=586,
  serialized_end=595,
)

_METADATAKIND_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='envoy.type.metadata.v2.MetadataKind.Route',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=597,
  serialized_end=604,
)

_METADATAKIND_CLUSTER = _descriptor.Descriptor(
  name='Cluster',
  full_name='envoy.type.metadata.v2.MetadataKind.Cluster',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=615,
)

_METADATAKIND_HOST = _descriptor.Descriptor(
  name='Host',
  full_name='envoy.type.metadata.v2.MetadataKind.Host',
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=623,
)

_METADATAKIND = _descriptor.Descriptor(
  name='MetadataKind',
  full_name='envoy.type.metadata.v2.MetadataKind',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='envoy.type.metadata.v2.MetadataKind.request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='route', full_name='envoy.type.metadata.v2.MetadataKind.route', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cluster', full_name='envoy.type.metadata.v2.MetadataKind.cluster', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='host', full_name='envoy.type.metadata.v2.MetadataKind.host', index=3,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='envoy.type.metadata.v2.MetadataKind.kind',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=320,
  serialized_end=636,
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
    '__module__' : 'envoy.type.metadata.v2.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v2.MetadataKey.PathSegment)
    })
  ,
  'DESCRIPTOR' : _METADATAKEY,
  '__module__' : 'envoy.type.metadata.v2.metadata_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.metadata.v2.MetadataKey)
  })
_sym_db.RegisterMessage(MetadataKey)
_sym_db.RegisterMessage(MetadataKey.PathSegment)

MetadataKind = _reflection.GeneratedProtocolMessageType('MetadataKind', (_message.Message,), {

  'Request' : _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
    'DESCRIPTOR' : _METADATAKIND_REQUEST,
    '__module__' : 'envoy.type.metadata.v2.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v2.MetadataKind.Request)
    })
  ,

  'Route' : _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), {
    'DESCRIPTOR' : _METADATAKIND_ROUTE,
    '__module__' : 'envoy.type.metadata.v2.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v2.MetadataKind.Route)
    })
  ,

  'Cluster' : _reflection.GeneratedProtocolMessageType('Cluster', (_message.Message,), {
    'DESCRIPTOR' : _METADATAKIND_CLUSTER,
    '__module__' : 'envoy.type.metadata.v2.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v2.MetadataKind.Cluster)
    })
  ,

  'Host' : _reflection.GeneratedProtocolMessageType('Host', (_message.Message,), {
    'DESCRIPTOR' : _METADATAKIND_HOST,
    '__module__' : 'envoy.type.metadata.v2.metadata_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.metadata.v2.MetadataKind.Host)
    })
  ,
  'DESCRIPTOR' : _METADATAKIND,
  '__module__' : 'envoy.type.metadata.v2.metadata_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.metadata.v2.MetadataKind)
  })
_sym_db.RegisterMessage(MetadataKind)
_sym_db.RegisterMessage(MetadataKind.Request)
_sym_db.RegisterMessage(MetadataKind.Route)
_sym_db.RegisterMessage(MetadataKind.Cluster)
_sym_db.RegisterMessage(MetadataKind.Host)


DESCRIPTOR._options = None
_METADATAKEY_PATHSEGMENT.oneofs_by_name['segment']._options = None
_METADATAKEY_PATHSEGMENT.fields_by_name['key']._options = None
_METADATAKEY.fields_by_name['key']._options = None
_METADATAKEY.fields_by_name['path']._options = None
_METADATAKIND.oneofs_by_name['kind']._options = None
# @@protoc_insertion_point(module_scope)
