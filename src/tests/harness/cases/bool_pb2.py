# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/cases/bool.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1etests/harness/cases/bool.proto\x12\x13tests.harness.cases\x1a\x17validate/validate.proto\"\x17\n\x08\x42oolNone\x12\x0b\n\x03val\x18\x01 \x01(\x08\"%\n\rBoolConstTrue\x12\x14\n\x03val\x18\x01 \x01(\x08\x42\x07\xfa\x42\x04j\x02\x08\x01\"&\n\x0e\x42oolConstFalse\x12\x14\n\x03val\x18\x01 \x01(\x08\x42\x07\xfa\x42\x04j\x02\x08\x00\x42HZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;casesb\x06proto3')



_BOOLNONE = DESCRIPTOR.message_types_by_name['BoolNone']
_BOOLCONSTTRUE = DESCRIPTOR.message_types_by_name['BoolConstTrue']
_BOOLCONSTFALSE = DESCRIPTOR.message_types_by_name['BoolConstFalse']
BoolNone = _reflection.GeneratedProtocolMessageType('BoolNone', (_message.Message,), {
  'DESCRIPTOR' : _BOOLNONE,
  '__module__' : 'tests.harness.cases.bool_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.BoolNone)
  })
_sym_db.RegisterMessage(BoolNone)

BoolConstTrue = _reflection.GeneratedProtocolMessageType('BoolConstTrue', (_message.Message,), {
  'DESCRIPTOR' : _BOOLCONSTTRUE,
  '__module__' : 'tests.harness.cases.bool_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.BoolConstTrue)
  })
_sym_db.RegisterMessage(BoolConstTrue)

BoolConstFalse = _reflection.GeneratedProtocolMessageType('BoolConstFalse', (_message.Message,), {
  'DESCRIPTOR' : _BOOLCONSTFALSE,
  '__module__' : 'tests.harness.cases.bool_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.BoolConstFalse)
  })
_sym_db.RegisterMessage(BoolConstFalse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;cases'
  _BOOLCONSTTRUE.fields_by_name['val']._options = None
  _BOOLCONSTTRUE.fields_by_name['val']._serialized_options = b'\372B\004j\002\010\001'
  _BOOLCONSTFALSE.fields_by_name['val']._options = None
  _BOOLCONSTFALSE.fields_by_name['val']._serialized_options = b'\372B\004j\002\010\000'
  _BOOLNONE._serialized_start=80
  _BOOLNONE._serialized_end=103
  _BOOLCONSTTRUE._serialized_start=105
  _BOOLCONSTTRUE._serialized_end=142
  _BOOLCONSTFALSE._serialized_start=144
  _BOOLCONSTFALSE._serialized_end=182
# @@protoc_insertion_point(module_scope)