# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/cases/kitchen_sink.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&tests/harness/cases/kitchen_sink.proto\x12\x13tests.harness.cases\x1a\x17validate/validate.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\"\xf0\x06\n\x0e\x43omplexTestMsg\x12\x1a\n\x05\x63onst\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\n\x04\x61\x62\x63\x64\x12\x33\n\x06nested\x18\x02 \x01(\x0b\x32#.tests.harness.cases.ComplexTestMsg\x12\x1a\n\tint_const\x18\x03 \x01(\x05\x42\x07\xfa\x42\x04\x1a\x02\x08\x05\x12\x1b\n\nbool_const\x18\x04 \x01(\x08\x42\x07\xfa\x42\x04j\x02\x08\x00\x12:\n\tfloat_val\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.FloatValueB\n\xfa\x42\x07\n\x05%\x00\x00\x00\x00\x12\x38\n\x07\x64ur_val\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xfa\x42\t\xaa\x01\x06\x08\x01\x1a\x02\x08\x11\x12\x36\n\x06ts_val\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xfa\x42\x07\xb2\x01\x04*\x02\x08\x07\x12\x34\n\x07\x61nother\x18\x08 \x01(\x0b\x32#.tests.harness.cases.ComplexTestMsg\x12\x1f\n\x0b\x66loat_const\x18\t \x01(\x02\x42\n\xfa\x42\x07\n\x05\x15\x00\x00\x00\x41\x12*\n\tdouble_in\x18\n \x01(\x01\x42\x17\xfa\x42\x14\x12\x12\x31\xb4\xc8v\xbe\x9f\x8c|@1\x00\x00\x00\x00\x00\xc0^@\x12\x42\n\nenum_const\x18\x0b \x01(\x0e\x32$.tests.harness.cases.ComplexTestEnumB\x08\xfa\x42\x05\x82\x01\x02\x08\x02\x12[\n\x07\x61ny_val\x18\x0c \x01(\x0b\x32\x14.google.protobuf.AnyB4\xfa\x42\x31\xa2\x01.\x12,type.googleapis.com/google.protobuf.Duration\x12\x41\n\nrep_ts_val\x18\r \x03(\x0b\x32\x1a.google.protobuf.TimestampB\x11\xfa\x42\x0e\x92\x01\x0b\"\t\xb2\x01\x06\x32\x04\x10\xc0\x84=\x12N\n\x07map_val\x18\x0e \x03(\x0b\x32/.tests.harness.cases.ComplexTestMsg.MapValEntryB\x0c\xfa\x42\t\x9a\x01\x06\"\x04:\x02\x10\x00\x12\x1c\n\tbytes_val\x18\x0f \x01(\x0c\x42\t\xfa\x42\x06z\x04\n\x02\x00\x99\x12\x0b\n\x01x\x18\x10 \x01(\tH\x00\x12\x0b\n\x01y\x18\x11 \x01(\x05H\x00\x1a-\n\x0bMapValEntry\x12\x0b\n\x03key\x18\x01 \x01(\x11\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x08\n\x01o\x12\x03\xf8\x42\x01\"F\n\x12KitchenSinkMessage\x12\x30\n\x03val\x18\x01 \x01(\x0b\x32#.tests.harness.cases.ComplexTestMsg*B\n\x0f\x43omplexTestEnum\x12\x0f\n\x0b\x43omplexZero\x10\x00\x12\x0e\n\nComplexONE\x10\x01\x12\x0e\n\nComplexTWO\x10\x02\x42HZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tests.harness.cases.kitchen_sink_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;cases'
  _globals['_COMPLEXTESTMSG_MAPVALENTRY']._options = None
  _globals['_COMPLEXTESTMSG_MAPVALENTRY']._serialized_options = b'8\001'
  _globals['_COMPLEXTESTMSG'].oneofs_by_name['o']._options = None
  _globals['_COMPLEXTESTMSG'].oneofs_by_name['o']._serialized_options = b'\370B\001'
  _globals['_COMPLEXTESTMSG'].fields_by_name['const']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['const']._serialized_options = b'\372B\010r\006\n\004abcd'
  _globals['_COMPLEXTESTMSG'].fields_by_name['int_const']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['int_const']._serialized_options = b'\372B\004\032\002\010\005'
  _globals['_COMPLEXTESTMSG'].fields_by_name['bool_const']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['bool_const']._serialized_options = b'\372B\004j\002\010\000'
  _globals['_COMPLEXTESTMSG'].fields_by_name['float_val']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['float_val']._serialized_options = b'\372B\007\n\005%\000\000\000\000'
  _globals['_COMPLEXTESTMSG'].fields_by_name['dur_val']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['dur_val']._serialized_options = b'\372B\t\252\001\006\010\001\032\002\010\021'
  _globals['_COMPLEXTESTMSG'].fields_by_name['ts_val']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['ts_val']._serialized_options = b'\372B\007\262\001\004*\002\010\007'
  _globals['_COMPLEXTESTMSG'].fields_by_name['float_const']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['float_const']._serialized_options = b'\372B\007\n\005\025\000\000\000A'
  _globals['_COMPLEXTESTMSG'].fields_by_name['double_in']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['double_in']._serialized_options = b'\372B\024\022\0221\264\310v\276\237\214|@1\000\000\000\000\000\300^@'
  _globals['_COMPLEXTESTMSG'].fields_by_name['enum_const']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['enum_const']._serialized_options = b'\372B\005\202\001\002\010\002'
  _globals['_COMPLEXTESTMSG'].fields_by_name['any_val']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['any_val']._serialized_options = b'\372B1\242\001.\022,type.googleapis.com/google.protobuf.Duration'
  _globals['_COMPLEXTESTMSG'].fields_by_name['rep_ts_val']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['rep_ts_val']._serialized_options = b'\372B\016\222\001\013\"\t\262\001\0062\004\020\300\204='
  _globals['_COMPLEXTESTMSG'].fields_by_name['map_val']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['map_val']._serialized_options = b'\372B\t\232\001\006\"\004:\002\020\000'
  _globals['_COMPLEXTESTMSG'].fields_by_name['bytes_val']._options = None
  _globals['_COMPLEXTESTMSG'].fields_by_name['bytes_val']._serialized_options = b'\372B\006z\004\n\002\000\231'
  _globals['_COMPLEXTESTENUM']._serialized_start=1167
  _globals['_COMPLEXTESTENUM']._serialized_end=1233
  _globals['_COMPLEXTESTMSG']._serialized_start=213
  _globals['_COMPLEXTESTMSG']._serialized_end=1093
  _globals['_COMPLEXTESTMSG_MAPVALENTRY']._serialized_start=1038
  _globals['_COMPLEXTESTMSG_MAPVALENTRY']._serialized_end=1083
  _globals['_KITCHENSINKMESSAGE']._serialized_start=1095
  _globals['_KITCHENSINKMESSAGE']._serialized_end=1165
# @@protoc_insertion_point(module_scope)
