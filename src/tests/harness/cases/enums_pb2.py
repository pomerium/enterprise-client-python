# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/cases/enums.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from tests.harness.cases.other_package import embed_pb2 as tests_dot_harness_dot_cases_dot_other__package_dot_embed__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftests/harness/cases/enums.proto\x12\x13tests.harness.cases\x1a\x17validate/validate.proto\x1a-tests/harness/cases/other_package/embed.proto\"6\n\x08\x45numNone\x12*\n\x03val\x18\x01 \x01(\x0e\x32\x1d.tests.harness.cases.TestEnum\"A\n\tEnumConst\x12\x34\n\x03val\x18\x01 \x01(\x0e\x32\x1d.tests.harness.cases.TestEnumB\x08\xfa\x42\x05\x82\x01\x02\x08\x02\"K\n\x0e\x45numAliasConst\x12\x39\n\x03val\x18\x01 \x01(\x0e\x32\".tests.harness.cases.TestEnumAliasB\x08\xfa\x42\x05\x82\x01\x02\x08\x02\"C\n\x0b\x45numDefined\x12\x34\n\x03val\x18\x01 \x01(\x0e\x32\x1d.tests.harness.cases.TestEnumB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\"M\n\x10\x45numAliasDefined\x12\x39\n\x03val\x18\x01 \x01(\x0e\x32\".tests.harness.cases.TestEnumAliasB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\"@\n\x06\x45numIn\x12\x36\n\x03val\x18\x01 \x01(\x0e\x32\x1d.tests.harness.cases.TestEnumB\n\xfa\x42\x07\x82\x01\x04\x18\x00\x18\x02\"J\n\x0b\x45numAliasIn\x12;\n\x03val\x18\x01 \x01(\x0e\x32\".tests.harness.cases.TestEnumAliasB\n\xfa\x42\x07\x82\x01\x04\x18\x00\x18\x02\"A\n\tEnumNotIn\x12\x34\n\x03val\x18\x01 \x01(\x0e\x32\x1d.tests.harness.cases.TestEnumB\x08\xfa\x42\x05\x82\x01\x02 \x01\"K\n\x0e\x45numAliasNotIn\x12\x39\n\x03val\x18\x01 \x01(\x0e\x32\".tests.harness.cases.TestEnumAliasB\x08\xfa\x42\x05\x82\x01\x02 \x01\"Z\n\x0c\x45numExternal\x12J\n\x03val\x18\x01 \x01(\x0e\x32\x33.tests.harness.cases.other_package.Embed.EnumeratedB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\"P\n\x13RepeatedEnumDefined\x12\x39\n\x03val\x18\x01 \x03(\x0e\x32\x1d.tests.harness.cases.TestEnumB\r\xfa\x42\n\x92\x01\x07\"\x05\x82\x01\x02\x10\x01\"n\n\x1bRepeatedExternalEnumDefined\x12O\n\x03val\x18\x01 \x03(\x0e\x32\x33.tests.harness.cases.other_package.Embed.EnumeratedB\r\xfa\x42\n\x92\x01\x07\"\x05\x82\x01\x02\x10\x01\"\xa5\x01\n\x0eMapEnumDefined\x12H\n\x03val\x18\x01 \x03(\x0b\x32,.tests.harness.cases.MapEnumDefined.ValEntryB\r\xfa\x42\n\x9a\x01\x07*\x05\x82\x01\x02\x10\x01\x1aI\n\x08ValEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0e\x32\x1d.tests.harness.cases.TestEnum:\x02\x38\x01\"\xcb\x01\n\x16MapExternalEnumDefined\x12P\n\x03val\x18\x01 \x03(\x0b\x32\x34.tests.harness.cases.MapExternalEnumDefined.ValEntryB\r\xfa\x42\n\x9a\x01\x07*\x05\x82\x01\x02\x10\x01\x1a_\n\x08ValEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x42\n\x05value\x18\x02 \x01(\x0e\x32\x33.tests.harness.cases.other_package.Embed.Enumerated:\x02\x38\x01*&\n\x08TestEnum\x12\x08\n\x04ZERO\x10\x00\x12\x07\n\x03ONE\x10\x01\x12\x07\n\x03TWO\x10\x02*H\n\rTestEnumAlias\x12\x05\n\x01\x41\x10\x00\x12\x05\n\x01\x42\x10\x01\x12\x05\n\x01\x43\x10\x02\x12\t\n\x05\x41LPHA\x10\x00\x12\x08\n\x04\x42\x45TA\x10\x01\x12\t\n\x05GAMMA\x10\x02\x1a\x02\x10\x01\x42HZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;casesb\x06proto3')

_TESTENUM = DESCRIPTOR.enum_types_by_name['TestEnum']
TestEnum = enum_type_wrapper.EnumTypeWrapper(_TESTENUM)
_TESTENUMALIAS = DESCRIPTOR.enum_types_by_name['TestEnumAlias']
TestEnumAlias = enum_type_wrapper.EnumTypeWrapper(_TESTENUMALIAS)
ZERO = 0
ONE = 1
TWO = 2
A = 0
B = 1
C = 2
ALPHA = 0
BETA = 1
GAMMA = 2


_ENUMNONE = DESCRIPTOR.message_types_by_name['EnumNone']
_ENUMCONST = DESCRIPTOR.message_types_by_name['EnumConst']
_ENUMALIASCONST = DESCRIPTOR.message_types_by_name['EnumAliasConst']
_ENUMDEFINED = DESCRIPTOR.message_types_by_name['EnumDefined']
_ENUMALIASDEFINED = DESCRIPTOR.message_types_by_name['EnumAliasDefined']
_ENUMIN = DESCRIPTOR.message_types_by_name['EnumIn']
_ENUMALIASIN = DESCRIPTOR.message_types_by_name['EnumAliasIn']
_ENUMNOTIN = DESCRIPTOR.message_types_by_name['EnumNotIn']
_ENUMALIASNOTIN = DESCRIPTOR.message_types_by_name['EnumAliasNotIn']
_ENUMEXTERNAL = DESCRIPTOR.message_types_by_name['EnumExternal']
_REPEATEDENUMDEFINED = DESCRIPTOR.message_types_by_name['RepeatedEnumDefined']
_REPEATEDEXTERNALENUMDEFINED = DESCRIPTOR.message_types_by_name['RepeatedExternalEnumDefined']
_MAPENUMDEFINED = DESCRIPTOR.message_types_by_name['MapEnumDefined']
_MAPENUMDEFINED_VALENTRY = _MAPENUMDEFINED.nested_types_by_name['ValEntry']
_MAPEXTERNALENUMDEFINED = DESCRIPTOR.message_types_by_name['MapExternalEnumDefined']
_MAPEXTERNALENUMDEFINED_VALENTRY = _MAPEXTERNALENUMDEFINED.nested_types_by_name['ValEntry']
EnumNone = _reflection.GeneratedProtocolMessageType('EnumNone', (_message.Message,), {
  'DESCRIPTOR' : _ENUMNONE,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumNone)
  })
_sym_db.RegisterMessage(EnumNone)

EnumConst = _reflection.GeneratedProtocolMessageType('EnumConst', (_message.Message,), {
  'DESCRIPTOR' : _ENUMCONST,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumConst)
  })
_sym_db.RegisterMessage(EnumConst)

EnumAliasConst = _reflection.GeneratedProtocolMessageType('EnumAliasConst', (_message.Message,), {
  'DESCRIPTOR' : _ENUMALIASCONST,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumAliasConst)
  })
_sym_db.RegisterMessage(EnumAliasConst)

EnumDefined = _reflection.GeneratedProtocolMessageType('EnumDefined', (_message.Message,), {
  'DESCRIPTOR' : _ENUMDEFINED,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumDefined)
  })
_sym_db.RegisterMessage(EnumDefined)

EnumAliasDefined = _reflection.GeneratedProtocolMessageType('EnumAliasDefined', (_message.Message,), {
  'DESCRIPTOR' : _ENUMALIASDEFINED,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumAliasDefined)
  })
_sym_db.RegisterMessage(EnumAliasDefined)

EnumIn = _reflection.GeneratedProtocolMessageType('EnumIn', (_message.Message,), {
  'DESCRIPTOR' : _ENUMIN,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumIn)
  })
_sym_db.RegisterMessage(EnumIn)

EnumAliasIn = _reflection.GeneratedProtocolMessageType('EnumAliasIn', (_message.Message,), {
  'DESCRIPTOR' : _ENUMALIASIN,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumAliasIn)
  })
_sym_db.RegisterMessage(EnumAliasIn)

EnumNotIn = _reflection.GeneratedProtocolMessageType('EnumNotIn', (_message.Message,), {
  'DESCRIPTOR' : _ENUMNOTIN,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumNotIn)
  })
_sym_db.RegisterMessage(EnumNotIn)

EnumAliasNotIn = _reflection.GeneratedProtocolMessageType('EnumAliasNotIn', (_message.Message,), {
  'DESCRIPTOR' : _ENUMALIASNOTIN,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumAliasNotIn)
  })
_sym_db.RegisterMessage(EnumAliasNotIn)

EnumExternal = _reflection.GeneratedProtocolMessageType('EnumExternal', (_message.Message,), {
  'DESCRIPTOR' : _ENUMEXTERNAL,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.EnumExternal)
  })
_sym_db.RegisterMessage(EnumExternal)

RepeatedEnumDefined = _reflection.GeneratedProtocolMessageType('RepeatedEnumDefined', (_message.Message,), {
  'DESCRIPTOR' : _REPEATEDENUMDEFINED,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.RepeatedEnumDefined)
  })
_sym_db.RegisterMessage(RepeatedEnumDefined)

RepeatedExternalEnumDefined = _reflection.GeneratedProtocolMessageType('RepeatedExternalEnumDefined', (_message.Message,), {
  'DESCRIPTOR' : _REPEATEDEXTERNALENUMDEFINED,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.RepeatedExternalEnumDefined)
  })
_sym_db.RegisterMessage(RepeatedExternalEnumDefined)

MapEnumDefined = _reflection.GeneratedProtocolMessageType('MapEnumDefined', (_message.Message,), {

  'ValEntry' : _reflection.GeneratedProtocolMessageType('ValEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAPENUMDEFINED_VALENTRY,
    '__module__' : 'tests.harness.cases.enums_pb2'
    # @@protoc_insertion_point(class_scope:tests.harness.cases.MapEnumDefined.ValEntry)
    })
  ,
  'DESCRIPTOR' : _MAPENUMDEFINED,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.MapEnumDefined)
  })
_sym_db.RegisterMessage(MapEnumDefined)
_sym_db.RegisterMessage(MapEnumDefined.ValEntry)

MapExternalEnumDefined = _reflection.GeneratedProtocolMessageType('MapExternalEnumDefined', (_message.Message,), {

  'ValEntry' : _reflection.GeneratedProtocolMessageType('ValEntry', (_message.Message,), {
    'DESCRIPTOR' : _MAPEXTERNALENUMDEFINED_VALENTRY,
    '__module__' : 'tests.harness.cases.enums_pb2'
    # @@protoc_insertion_point(class_scope:tests.harness.cases.MapExternalEnumDefined.ValEntry)
    })
  ,
  'DESCRIPTOR' : _MAPEXTERNALENUMDEFINED,
  '__module__' : 'tests.harness.cases.enums_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.MapExternalEnumDefined)
  })
_sym_db.RegisterMessage(MapExternalEnumDefined)
_sym_db.RegisterMessage(MapExternalEnumDefined.ValEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;cases'
  _TESTENUMALIAS._options = None
  _TESTENUMALIAS._serialized_options = b'\020\001'
  _ENUMCONST.fields_by_name['val']._options = None
  _ENUMCONST.fields_by_name['val']._serialized_options = b'\372B\005\202\001\002\010\002'
  _ENUMALIASCONST.fields_by_name['val']._options = None
  _ENUMALIASCONST.fields_by_name['val']._serialized_options = b'\372B\005\202\001\002\010\002'
  _ENUMDEFINED.fields_by_name['val']._options = None
  _ENUMDEFINED.fields_by_name['val']._serialized_options = b'\372B\005\202\001\002\020\001'
  _ENUMALIASDEFINED.fields_by_name['val']._options = None
  _ENUMALIASDEFINED.fields_by_name['val']._serialized_options = b'\372B\005\202\001\002\020\001'
  _ENUMIN.fields_by_name['val']._options = None
  _ENUMIN.fields_by_name['val']._serialized_options = b'\372B\007\202\001\004\030\000\030\002'
  _ENUMALIASIN.fields_by_name['val']._options = None
  _ENUMALIASIN.fields_by_name['val']._serialized_options = b'\372B\007\202\001\004\030\000\030\002'
  _ENUMNOTIN.fields_by_name['val']._options = None
  _ENUMNOTIN.fields_by_name['val']._serialized_options = b'\372B\005\202\001\002 \001'
  _ENUMALIASNOTIN.fields_by_name['val']._options = None
  _ENUMALIASNOTIN.fields_by_name['val']._serialized_options = b'\372B\005\202\001\002 \001'
  _ENUMEXTERNAL.fields_by_name['val']._options = None
  _ENUMEXTERNAL.fields_by_name['val']._serialized_options = b'\372B\005\202\001\002\020\001'
  _REPEATEDENUMDEFINED.fields_by_name['val']._options = None
  _REPEATEDENUMDEFINED.fields_by_name['val']._serialized_options = b'\372B\n\222\001\007\"\005\202\001\002\020\001'
  _REPEATEDEXTERNALENUMDEFINED.fields_by_name['val']._options = None
  _REPEATEDEXTERNALENUMDEFINED.fields_by_name['val']._serialized_options = b'\372B\n\222\001\007\"\005\202\001\002\020\001'
  _MAPENUMDEFINED_VALENTRY._options = None
  _MAPENUMDEFINED_VALENTRY._serialized_options = b'8\001'
  _MAPENUMDEFINED.fields_by_name['val']._options = None
  _MAPENUMDEFINED.fields_by_name['val']._serialized_options = b'\372B\n\232\001\007*\005\202\001\002\020\001'
  _MAPEXTERNALENUMDEFINED_VALENTRY._options = None
  _MAPEXTERNALENUMDEFINED_VALENTRY._serialized_options = b'8\001'
  _MAPEXTERNALENUMDEFINED.fields_by_name['val']._options = None
  _MAPEXTERNALENUMDEFINED.fields_by_name['val']._serialized_options = b'\372B\n\232\001\007*\005\202\001\002\020\001'
  _TESTENUM._serialized_start=1422
  _TESTENUM._serialized_end=1460
  _TESTENUMALIAS._serialized_start=1462
  _TESTENUMALIAS._serialized_end=1534
  _ENUMNONE._serialized_start=128
  _ENUMNONE._serialized_end=182
  _ENUMCONST._serialized_start=184
  _ENUMCONST._serialized_end=249
  _ENUMALIASCONST._serialized_start=251
  _ENUMALIASCONST._serialized_end=326
  _ENUMDEFINED._serialized_start=328
  _ENUMDEFINED._serialized_end=395
  _ENUMALIASDEFINED._serialized_start=397
  _ENUMALIASDEFINED._serialized_end=474
  _ENUMIN._serialized_start=476
  _ENUMIN._serialized_end=540
  _ENUMALIASIN._serialized_start=542
  _ENUMALIASIN._serialized_end=616
  _ENUMNOTIN._serialized_start=618
  _ENUMNOTIN._serialized_end=683
  _ENUMALIASNOTIN._serialized_start=685
  _ENUMALIASNOTIN._serialized_end=760
  _ENUMEXTERNAL._serialized_start=762
  _ENUMEXTERNAL._serialized_end=852
  _REPEATEDENUMDEFINED._serialized_start=854
  _REPEATEDENUMDEFINED._serialized_end=934
  _REPEATEDEXTERNALENUMDEFINED._serialized_start=936
  _REPEATEDEXTERNALENUMDEFINED._serialized_end=1046
  _MAPENUMDEFINED._serialized_start=1049
  _MAPENUMDEFINED._serialized_end=1214
  _MAPENUMDEFINED_VALENTRY._serialized_start=1141
  _MAPENUMDEFINED_VALENTRY._serialized_end=1214
  _MAPEXTERNALENUMDEFINED._serialized_start=1217
  _MAPEXTERNALENUMDEFINED._serialized_end=1420
  _MAPEXTERNALENUMDEFINED_VALENTRY._serialized_start=1325
  _MAPEXTERNALENUMDEFINED_VALENTRY._serialized_end=1420
# @@protoc_insertion_point(module_scope)
