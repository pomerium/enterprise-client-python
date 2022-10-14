# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/transport_sockets/tls/v3/secret.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.config.core.v3 import config_source_pb2 as envoy_dot_config_dot_core_dot_v3_dot_config__source__pb2
from envoy.extensions.transport_sockets.tls.v3 import common_pb2 as envoy_dot_extensions_dot_transport__sockets_dot_tls_dot_v3_dot_common__pb2
from udpa.annotations import sensitive_pb2 as udpa_dot_annotations_dot_sensitive__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6envoy/extensions/transport_sockets/tls/v3/secret.proto\x12)envoy.extensions.transport_sockets.tls.v3\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a(envoy/config/core/v3/config_source.proto\x1a\x36\x65nvoy/extensions/transport_sockets/tls/v3/common.proto\x1a udpa/annotations/sensitive.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"q\n\rGenericSecret\x12\x38\n\x06secret\x18\x01 \x01(\x0b\x32 .envoy.config.core.v3.DataSourceB\x06\xb8\xb7\x8b\xa4\x02\x01:&\x9a\xc5\x88\x1e!\n\x1f\x65nvoy.api.v2.auth.GenericSecret\"\x8a\x01\n\x0fSdsSecretConfig\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x36\n\nsds_config\x18\x02 \x01(\x0b\x32\".envoy.config.core.v3.ConfigSource:(\x9a\xc5\x88\x1e#\n!envoy.api.v2.auth.SdsSecretConfig\"\xb0\x03\n\x06Secret\x12\x0c\n\x04name\x18\x01 \x01(\t\x12T\n\x0ftls_certificate\x18\x02 \x01(\x0b\x32\x39.envoy.extensions.transport_sockets.tls.v3.TlsCertificateH\x00\x12^\n\x13session_ticket_keys\x18\x03 \x01(\x0b\x32?.envoy.extensions.transport_sockets.tls.v3.TlsSessionTicketKeysH\x00\x12\x65\n\x12validation_context\x18\x04 \x01(\x0b\x32G.envoy.extensions.transport_sockets.tls.v3.CertificateValidationContextH\x00\x12R\n\x0egeneric_secret\x18\x05 \x01(\x0b\x32\x38.envoy.extensions.transport_sockets.tls.v3.GenericSecretH\x00:\x1f\x9a\xc5\x88\x1e\x1a\n\x18\x65nvoy.api.v2.auth.SecretB\x06\n\x04typeB\xa8\x01\n7io.envoyproxy.envoy.extensions.transport_sockets.tls.v3B\x0bSecretProtoP\x01ZVgithub.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/tls/v3;tlsv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_GENERICSECRET = DESCRIPTOR.message_types_by_name['GenericSecret']
_SDSSECRETCONFIG = DESCRIPTOR.message_types_by_name['SdsSecretConfig']
_SECRET = DESCRIPTOR.message_types_by_name['Secret']
GenericSecret = _reflection.GeneratedProtocolMessageType('GenericSecret', (_message.Message,), {
  'DESCRIPTOR' : _GENERICSECRET,
  '__module__' : 'envoy.extensions.transport_sockets.tls.v3.secret_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.transport_sockets.tls.v3.GenericSecret)
  })
_sym_db.RegisterMessage(GenericSecret)

SdsSecretConfig = _reflection.GeneratedProtocolMessageType('SdsSecretConfig', (_message.Message,), {
  'DESCRIPTOR' : _SDSSECRETCONFIG,
  '__module__' : 'envoy.extensions.transport_sockets.tls.v3.secret_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.transport_sockets.tls.v3.SdsSecretConfig)
  })
_sym_db.RegisterMessage(SdsSecretConfig)

Secret = _reflection.GeneratedProtocolMessageType('Secret', (_message.Message,), {
  'DESCRIPTOR' : _SECRET,
  '__module__' : 'envoy.extensions.transport_sockets.tls.v3.secret_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.transport_sockets.tls.v3.Secret)
  })
_sym_db.RegisterMessage(Secret)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n7io.envoyproxy.envoy.extensions.transport_sockets.tls.v3B\013SecretProtoP\001ZVgithub.com/envoyproxy/go-control-plane/envoy/extensions/transport_sockets/tls/v3;tlsv3\272\200\310\321\006\002\020\002'
  _GENERICSECRET.fields_by_name['secret']._options = None
  _GENERICSECRET.fields_by_name['secret']._serialized_options = b'\270\267\213\244\002\001'
  _GENERICSECRET._options = None
  _GENERICSECRET._serialized_options = b'\232\305\210\036!\n\037envoy.api.v2.auth.GenericSecret'
  _SDSSECRETCONFIG.fields_by_name['name']._options = None
  _SDSSECRETCONFIG.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _SDSSECRETCONFIG._options = None
  _SDSSECRETCONFIG._serialized_options = b'\232\305\210\036#\n!envoy.api.v2.auth.SdsSecretConfig'
  _SECRET._options = None
  _SECRET._serialized_options = b'\232\305\210\036\032\n\030envoy.api.v2.auth.Secret'
  _GENERICSECRET._serialized_start=357
  _GENERICSECRET._serialized_end=470
  _SDSSECRETCONFIG._serialized_start=473
  _SDSSECRETCONFIG._serialized_end=611
  _SECRET._serialized_start=614
  _SECRET._serialized_end=1046
# @@protoc_insertion_point(module_scope)