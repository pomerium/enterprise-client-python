# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/harness.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1btests/harness/harness.proto\x12\rtests.harness\x1a\x19google/protobuf/any.proto\"1\n\x08TestCase\x12%\n\x07message\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"n\n\nTestResult\x12\r\n\x05Valid\x18\x01 \x01(\x08\x12\r\n\x05\x45rror\x18\x02 \x01(\x08\x12\x0f\n\x07Reasons\x18\x03 \x03(\t\x12\x14\n\x0c\x41llowFailure\x18\x04 \x01(\x08\x12\x1b\n\x13\x43heckMultipleErrors\x18\x05 \x01(\x08\x42\x44ZBgithub.com/envoyproxy/protoc-gen-validate/tests/harness/go;harnessb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tests.harness.harness_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/envoyproxy/protoc-gen-validate/tests/harness/go;harness'
  _globals['_TESTCASE']._serialized_start=73
  _globals['_TESTCASE']._serialized_end=122
  _globals['_TESTRESULT']._serialized_start=124
  _globals['_TESTRESULT']._serialized_end=234
# @@protoc_insertion_point(module_scope)
