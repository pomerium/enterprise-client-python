# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example-workspace/foo/bar.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x65xample-workspace/foo/bar.proto\x12\x0fpgv.example.foo\x1a\x17validate/validate.proto\"\x18\n\x07\x42\x61rNone\x12\r\n\x05value\x18\x01 \x01(\x05\" \n\x06\x42\x61rOne\x12\x16\n\x05value\x18\x01 \x01(\x05\x42\x07\xfa\x42\x04\x1a\x02\x38\x01\"\\\n\x04\x42\x61rs\x12*\n\x08\x62\x61r_none\x18\x01 \x01(\x0b\x32\x18.pgv.example.foo.BarNone\x12(\n\x07\x62\x61r_one\x18\x02 \x01(\x0b\x32\x17.pgv.example.foo.BarOneb\x06proto3')



_BARNONE = DESCRIPTOR.message_types_by_name['BarNone']
_BARONE = DESCRIPTOR.message_types_by_name['BarOne']
_BARS = DESCRIPTOR.message_types_by_name['Bars']
BarNone = _reflection.GeneratedProtocolMessageType('BarNone', (_message.Message,), {
  'DESCRIPTOR' : _BARNONE,
  '__module__' : 'example_workspace.foo.bar_pb2'
  # @@protoc_insertion_point(class_scope:pgv.example.foo.BarNone)
  })
_sym_db.RegisterMessage(BarNone)

BarOne = _reflection.GeneratedProtocolMessageType('BarOne', (_message.Message,), {
  'DESCRIPTOR' : _BARONE,
  '__module__' : 'example_workspace.foo.bar_pb2'
  # @@protoc_insertion_point(class_scope:pgv.example.foo.BarOne)
  })
_sym_db.RegisterMessage(BarOne)

Bars = _reflection.GeneratedProtocolMessageType('Bars', (_message.Message,), {
  'DESCRIPTOR' : _BARS,
  '__module__' : 'example_workspace.foo.bar_pb2'
  # @@protoc_insertion_point(class_scope:pgv.example.foo.Bars)
  })
_sym_db.RegisterMessage(Bars)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BARONE.fields_by_name['value']._options = None
  _BARONE.fields_by_name['value']._serialized_options = b'\372B\004\032\0028\001'
  _BARNONE._serialized_start=77
  _BARNONE._serialized_end=101
  _BARONE._serialized_start=103
  _BARONE._serialized_end=135
  _BARS._serialized_start=137
  _BARS._serialized_end=229
# @@protoc_insertion_point(module_scope)
