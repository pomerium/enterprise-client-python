# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/cases/oneofs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tests/harness/cases/oneofs.proto\x12\x13tests.harness.cases\x1a\x17validate/validate.proto\"$\n\x0cTestOneOfMsg\x12\x14\n\x03val\x18\x01 \x01(\x08\x42\x07\xfa\x42\x04j\x02\x08\x01\"*\n\tOneOfNone\x12\x0b\n\x01x\x18\x01 \x01(\tH\x00\x12\x0b\n\x01y\x18\x02 \x01(\x05H\x00\x42\x03\n\x01o\"k\n\x05OneOf\x12\x17\n\x01x\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05:\x03\x66ooH\x00\x12\x14\n\x01y\x18\x02 \x01(\x05\x42\x07\xfa\x42\x04\x1a\x02 \x00H\x00\x12.\n\x01z\x18\x03 \x01(\x0b\x32!.tests.harness.cases.TestOneOfMsgH\x00\x42\x03\n\x01o\"r\n\rOneOfRequired\x12\x0b\n\x01x\x18\x01 \x01(\tH\x00\x12\x0b\n\x01y\x18\x02 \x01(\x05H\x00\x12\x1f\n\x15name_with_underscores\x18\x03 \x01(\x05H\x00\x12\x1c\n\x12under_and_1_number\x18\x04 \x01(\x05H\x00\x42\x08\n\x01o\x12\x03\xf8\x42\x01\x42HZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;casesb\x06proto3')



_TESTONEOFMSG = DESCRIPTOR.message_types_by_name['TestOneOfMsg']
_ONEOFNONE = DESCRIPTOR.message_types_by_name['OneOfNone']
_ONEOF = DESCRIPTOR.message_types_by_name['OneOf']
_ONEOFREQUIRED = DESCRIPTOR.message_types_by_name['OneOfRequired']
TestOneOfMsg = _reflection.GeneratedProtocolMessageType('TestOneOfMsg', (_message.Message,), {
  'DESCRIPTOR' : _TESTONEOFMSG,
  '__module__' : 'tests.harness.cases.oneofs_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.TestOneOfMsg)
  })
_sym_db.RegisterMessage(TestOneOfMsg)

OneOfNone = _reflection.GeneratedProtocolMessageType('OneOfNone', (_message.Message,), {
  'DESCRIPTOR' : _ONEOFNONE,
  '__module__' : 'tests.harness.cases.oneofs_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.OneOfNone)
  })
_sym_db.RegisterMessage(OneOfNone)

OneOf = _reflection.GeneratedProtocolMessageType('OneOf', (_message.Message,), {
  'DESCRIPTOR' : _ONEOF,
  '__module__' : 'tests.harness.cases.oneofs_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.OneOf)
  })
_sym_db.RegisterMessage(OneOf)

OneOfRequired = _reflection.GeneratedProtocolMessageType('OneOfRequired', (_message.Message,), {
  'DESCRIPTOR' : _ONEOFREQUIRED,
  '__module__' : 'tests.harness.cases.oneofs_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.OneOfRequired)
  })
_sym_db.RegisterMessage(OneOfRequired)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;cases'
  _TESTONEOFMSG.fields_by_name['val']._options = None
  _TESTONEOFMSG.fields_by_name['val']._serialized_options = b'\372B\004j\002\010\001'
  _ONEOF.fields_by_name['x']._options = None
  _ONEOF.fields_by_name['x']._serialized_options = b'\372B\007r\005:\003foo'
  _ONEOF.fields_by_name['y']._options = None
  _ONEOF.fields_by_name['y']._serialized_options = b'\372B\004\032\002 \000'
  _ONEOFREQUIRED.oneofs_by_name['o']._options = None
  _ONEOFREQUIRED.oneofs_by_name['o']._serialized_options = b'\370B\001'
  _TESTONEOFMSG._serialized_start=82
  _TESTONEOFMSG._serialized_end=118
  _ONEOFNONE._serialized_start=120
  _ONEOFNONE._serialized_end=162
  _ONEOF._serialized_start=164
  _ONEOF._serialized_end=271
  _ONEOFREQUIRED._serialized_start=273
  _ONEOFREQUIRED._serialized_end=387
# @@protoc_insertion_point(module_scope)
