# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/harness.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1btests/harness/harness.proto\x12\rtests.harness\x1a\x19google/protobuf/any.proto\"1\n\x08TestCase\x12%\n\x07message\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"P\n\nTestResult\x12\r\n\x05Valid\x18\x01 \x01(\x08\x12\r\n\x05\x45rror\x18\x02 \x01(\x08\x12\x0e\n\x06Reason\x18\x03 \x01(\t\x12\x14\n\x0c\x41llowFailure\x18\x04 \x01(\x08\x42\x44ZBgithub.com/envoyproxy/protoc-gen-validate/tests/harness/go;harnessb\x06proto3')



_TESTCASE = DESCRIPTOR.message_types_by_name['TestCase']
_TESTRESULT = DESCRIPTOR.message_types_by_name['TestResult']
TestCase = _reflection.GeneratedProtocolMessageType('TestCase', (_message.Message,), {
  'DESCRIPTOR' : _TESTCASE,
  '__module__' : 'tests.harness.harness_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.TestCase)
  })
_sym_db.RegisterMessage(TestCase)

TestResult = _reflection.GeneratedProtocolMessageType('TestResult', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESULT,
  '__module__' : 'tests.harness.harness_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.TestResult)
  })
_sym_db.RegisterMessage(TestResult)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZBgithub.com/envoyproxy/protoc-gen-validate/tests/harness/go;harness'
  _TESTCASE._serialized_start=73
  _TESTCASE._serialized_end=122
  _TESTRESULT._serialized_start=124
  _TESTRESULT._serialized_end=204
# @@protoc_insertion_point(module_scope)
