# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: java/pgv-java-stub/src/test/proto/embedded.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0java/pgv-java-stub/src/test/proto/embedded.proto\x12\x17io.envoyproxy.pvg.cases\x1a\x17validate/validate.proto\"\xa9\x01\n\x08TokenUse\x12:\n\x07payload\x18\x01 \x01(\x0b\x32).io.envoyproxy.pvg.cases.TokenUse.Payload\x1a\x61\n\x07Payload\x12>\n\x05token\x18\x01 \x01(\x0b\x32/.io.envoyproxy.pvg.cases.TokenUse.Payload.Token\x1a\x16\n\x05Token\x12\r\n\x05value\x18\x01 \x01(\tB\x02P\x01\x62\x06proto3')



_TOKENUSE = DESCRIPTOR.message_types_by_name['TokenUse']
_TOKENUSE_PAYLOAD = _TOKENUSE.nested_types_by_name['Payload']
_TOKENUSE_PAYLOAD_TOKEN = _TOKENUSE_PAYLOAD.nested_types_by_name['Token']
TokenUse = _reflection.GeneratedProtocolMessageType('TokenUse', (_message.Message,), {

  'Payload' : _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), {

    'Token' : _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
      'DESCRIPTOR' : _TOKENUSE_PAYLOAD_TOKEN,
      '__module__' : 'java.pgv_java_stub.src.test.proto.embedded_pb2'
      # @@protoc_insertion_point(class_scope:io.envoyproxy.pvg.cases.TokenUse.Payload.Token)
      })
    ,
    'DESCRIPTOR' : _TOKENUSE_PAYLOAD,
    '__module__' : 'java.pgv_java_stub.src.test.proto.embedded_pb2'
    # @@protoc_insertion_point(class_scope:io.envoyproxy.pvg.cases.TokenUse.Payload)
    })
  ,
  'DESCRIPTOR' : _TOKENUSE,
  '__module__' : 'java.pgv_java_stub.src.test.proto.embedded_pb2'
  # @@protoc_insertion_point(class_scope:io.envoyproxy.pvg.cases.TokenUse)
  })
_sym_db.RegisterMessage(TokenUse)
_sym_db.RegisterMessage(TokenUse.Payload)
_sym_db.RegisterMessage(TokenUse.Payload.Token)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _TOKENUSE._serialized_start=103
  _TOKENUSE._serialized_end=272
  _TOKENUSE_PAYLOAD._serialized_start=175
  _TOKENUSE_PAYLOAD._serialized_end=272
  _TOKENUSE_PAYLOAD_TOKEN._serialized_start=250
  _TOKENUSE_PAYLOAD_TOKEN._serialized_end=272
# @@protoc_insertion_point(module_scope)
