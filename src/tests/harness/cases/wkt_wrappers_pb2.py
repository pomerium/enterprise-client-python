# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tests/harness/cases/wkt_wrappers.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'tests/harness/cases/wkt_wrappers.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&tests/harness/cases/wkt_wrappers.proto\x12\x13tests.harness.cases\x1a\x17validate/validate.proto\x1a\x1egoogle/protobuf/wrappers.proto\"7\n\x0bWrapperNone\x12(\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\"D\n\x0cWrapperFloat\x12\x34\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValueB\n\xfa\x42\x07\n\x05%\x00\x00\x00\x00\"J\n\rWrapperDouble\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x0e\xfa\x42\x0b\x12\t!\x00\x00\x00\x00\x00\x00\x00\x00\"A\n\x0cWrapperInt64\x12\x31\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueB\x07\xfa\x42\x04\"\x02 \x00\"A\n\x0cWrapperInt32\x12\x31\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueB\x07\xfa\x42\x04\x1a\x02 \x00\"C\n\rWrapperUInt64\x12\x32\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\x07\xfa\x42\x04\x32\x02 \x00\"C\n\rWrapperUInt32\x12\x32\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x07\xfa\x42\x04*\x02 \x00\"?\n\x0bWrapperBool\x12\x30\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x07\xfa\x42\x04j\x02\x08\x01\"F\n\rWrapperString\x12\x35\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\n\xfa\x42\x07r\x05\x42\x03\x62\x61r\"A\n\x0cWrapperBytes\x12\x31\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.BytesValueB\x07\xfa\x42\x04z\x02\x10\x03\"S\n\x15WrapperRequiredString\x12:\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x0f\xfa\x42\x0cr\x05\n\x03\x62\x61r\x8a\x01\x02\x10\x01\"U\n\x1aWrapperRequiredEmptyString\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x0c\xfa\x42\tr\x02\n\x00\x8a\x01\x02\x10\x01\"U\n\x19WrapperOptionalUuidString\x12\x38\n\x03val\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\xfa\x42\nr\x03\xb0\x01\x01\x8a\x01\x02\x10\x00\"Q\n\x14WrapperRequiredFloat\x12\x39\n\x03val\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.FloatValueB\x0f\xfa\x42\x0c\n\x05%\x00\x00\x00\x00\x8a\x01\x02\x10\x01\x42HZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tests.harness.cases.wkt_wrappers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;cases'
  _globals['_WRAPPERFLOAT'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERFLOAT'].fields_by_name['val']._serialized_options = b'\372B\007\n\005%\000\000\000\000'
  _globals['_WRAPPERDOUBLE'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERDOUBLE'].fields_by_name['val']._serialized_options = b'\372B\013\022\t!\000\000\000\000\000\000\000\000'
  _globals['_WRAPPERINT64'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERINT64'].fields_by_name['val']._serialized_options = b'\372B\004\"\002 \000'
  _globals['_WRAPPERINT32'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERINT32'].fields_by_name['val']._serialized_options = b'\372B\004\032\002 \000'
  _globals['_WRAPPERUINT64'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERUINT64'].fields_by_name['val']._serialized_options = b'\372B\0042\002 \000'
  _globals['_WRAPPERUINT32'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERUINT32'].fields_by_name['val']._serialized_options = b'\372B\004*\002 \000'
  _globals['_WRAPPERBOOL'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERBOOL'].fields_by_name['val']._serialized_options = b'\372B\004j\002\010\001'
  _globals['_WRAPPERSTRING'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERSTRING'].fields_by_name['val']._serialized_options = b'\372B\007r\005B\003bar'
  _globals['_WRAPPERBYTES'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERBYTES'].fields_by_name['val']._serialized_options = b'\372B\004z\002\020\003'
  _globals['_WRAPPERREQUIREDSTRING'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERREQUIREDSTRING'].fields_by_name['val']._serialized_options = b'\372B\014r\005\n\003bar\212\001\002\020\001'
  _globals['_WRAPPERREQUIREDEMPTYSTRING'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERREQUIREDEMPTYSTRING'].fields_by_name['val']._serialized_options = b'\372B\tr\002\n\000\212\001\002\020\001'
  _globals['_WRAPPEROPTIONALUUIDSTRING'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPEROPTIONALUUIDSTRING'].fields_by_name['val']._serialized_options = b'\372B\nr\003\260\001\001\212\001\002\020\000'
  _globals['_WRAPPERREQUIREDFLOAT'].fields_by_name['val']._loaded_options = None
  _globals['_WRAPPERREQUIREDFLOAT'].fields_by_name['val']._serialized_options = b'\372B\014\n\005%\000\000\000\000\212\001\002\020\001'
  _globals['_WRAPPERNONE']._serialized_start=120
  _globals['_WRAPPERNONE']._serialized_end=175
  _globals['_WRAPPERFLOAT']._serialized_start=177
  _globals['_WRAPPERFLOAT']._serialized_end=245
  _globals['_WRAPPERDOUBLE']._serialized_start=247
  _globals['_WRAPPERDOUBLE']._serialized_end=321
  _globals['_WRAPPERINT64']._serialized_start=323
  _globals['_WRAPPERINT64']._serialized_end=388
  _globals['_WRAPPERINT32']._serialized_start=390
  _globals['_WRAPPERINT32']._serialized_end=455
  _globals['_WRAPPERUINT64']._serialized_start=457
  _globals['_WRAPPERUINT64']._serialized_end=524
  _globals['_WRAPPERUINT32']._serialized_start=526
  _globals['_WRAPPERUINT32']._serialized_end=593
  _globals['_WRAPPERBOOL']._serialized_start=595
  _globals['_WRAPPERBOOL']._serialized_end=658
  _globals['_WRAPPERSTRING']._serialized_start=660
  _globals['_WRAPPERSTRING']._serialized_end=730
  _globals['_WRAPPERBYTES']._serialized_start=732
  _globals['_WRAPPERBYTES']._serialized_end=797
  _globals['_WRAPPERREQUIREDSTRING']._serialized_start=799
  _globals['_WRAPPERREQUIREDSTRING']._serialized_end=882
  _globals['_WRAPPERREQUIREDEMPTYSTRING']._serialized_start=884
  _globals['_WRAPPERREQUIREDEMPTYSTRING']._serialized_end=969
  _globals['_WRAPPEROPTIONALUUIDSTRING']._serialized_start=971
  _globals['_WRAPPEROPTIONALUUIDSTRING']._serialized_end=1056
  _globals['_WRAPPERREQUIREDFLOAT']._serialized_start=1058
  _globals['_WRAPPERREQUIREDFLOAT']._serialized_end=1139
# @@protoc_insertion_point(module_scope)
