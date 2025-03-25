# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/cases/strings.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!tests/harness/cases/strings.proto\x12\x13tests.harness.cases\x1a\x17validate/validate.proto\"\x19\n\nStringNone\x12\x0b\n\x03val\x18\x01 \x01(\t\"&\n\x0bStringConst\x12\x17\n\x03val\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\n\x03\x66oo\"(\n\x08StringIn\x12\x1c\n\x03val\x18\x01 \x01(\tB\x0f\xfa\x42\x0cr\nR\x03\x62\x61rR\x03\x62\x61z\"-\n\x0bStringNotIn\x12\x1e\n\x03val\x18\x01 \x01(\tB\x11\xfa\x42\x0er\x0cZ\x04\x66izzZ\x04\x62uzz\"\"\n\tStringLen\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x98\x01\x03\"$\n\x0cStringMinLen\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x03\"$\n\x0cStringMaxLen\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x18\x05\")\n\x0fStringMinMaxLen\x12\x16\n\x03val\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x03\x18\x05\".\n\x14StringEqualMinMaxLen\x12\x16\n\x03val\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x05\x18\x05\"\'\n\x0eStringLenBytes\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xa0\x01\x04\"&\n\x0eStringMinBytes\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x04\"&\n\x0eStringMaxBytes\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02(\x08\"+\n\x11StringMinMaxBytes\x12\x16\n\x03val\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04 \x04(\x08\"0\n\x16StringEqualMinMaxBytes\x12\x16\n\x03val\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04 \x04(\x08\"4\n\rStringPattern\x12#\n\x03val\x18\x01 \x01(\tB\x16\xfa\x42\x13r\x11\x32\x0f(?i)^[a-z0-9]+$\"4\n\x14StringPatternEscapes\x12\x1c\n\x03val\x18\x01 \x01(\tB\x0f\xfa\x42\x0cr\n2\x08\\* \\\\ \\w\"\'\n\x0cStringPrefix\x12\x17\n\x03val\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05:\x03\x66oo\")\n\x0eStringContains\x12\x17\n\x03val\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05J\x03\x62\x61r\"-\n\x11StringNotContains\x12\x18\n\x03val\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xba\x01\x03\x62\x61r\"\'\n\x0cStringSuffix\x12\x17\n\x03val\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x42\x03\x62\x61z\"#\n\x0bStringEmail\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02`\x01\"&\n\rStringAddress\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xa8\x01\x01\"&\n\x0eStringHostname\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02h\x01\" \n\x08StringIP\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02p\x01\"\"\n\nStringIPv4\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02x\x01\"#\n\nStringIPv6\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x80\x01\x01\"\"\n\tStringURI\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x88\x01\x01\"%\n\x0cStringURIRef\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x90\x01\x01\"#\n\nStringUUID\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01\"-\n\x14StringHttpHeaderName\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xc0\x01\x01\".\n\x15StringHttpHeaderValue\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xc0\x01\x02\"-\n\x11StringValidHeader\x12\x18\n\x03val\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x02\xc8\x01\x00\",\n\x10StringUUIDIgnore\x12\x18\n\x03val\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xb0\x01\x01\xd0\x01\x01\"2\n\rStringInOneOf\x12\x1a\n\x03\x62\x61r\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06R\x01\x61R\x01\x62H\x00\x42\x05\n\x03\x66ooBHZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tests.harness.cases.strings_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;cases'
  _globals['_STRINGCONST'].fields_by_name['val']._options = None
  _globals['_STRINGCONST'].fields_by_name['val']._serialized_options = b'\372B\007r\005\n\003foo'
  _globals['_STRINGIN'].fields_by_name['val']._options = None
  _globals['_STRINGIN'].fields_by_name['val']._serialized_options = b'\372B\014r\nR\003barR\003baz'
  _globals['_STRINGNOTIN'].fields_by_name['val']._options = None
  _globals['_STRINGNOTIN'].fields_by_name['val']._serialized_options = b'\372B\016r\014Z\004fizzZ\004buzz'
  _globals['_STRINGLEN'].fields_by_name['val']._options = None
  _globals['_STRINGLEN'].fields_by_name['val']._serialized_options = b'\372B\005r\003\230\001\003'
  _globals['_STRINGMINLEN'].fields_by_name['val']._options = None
  _globals['_STRINGMINLEN'].fields_by_name['val']._serialized_options = b'\372B\004r\002\020\003'
  _globals['_STRINGMAXLEN'].fields_by_name['val']._options = None
  _globals['_STRINGMAXLEN'].fields_by_name['val']._serialized_options = b'\372B\004r\002\030\005'
  _globals['_STRINGMINMAXLEN'].fields_by_name['val']._options = None
  _globals['_STRINGMINMAXLEN'].fields_by_name['val']._serialized_options = b'\372B\006r\004\020\003\030\005'
  _globals['_STRINGEQUALMINMAXLEN'].fields_by_name['val']._options = None
  _globals['_STRINGEQUALMINMAXLEN'].fields_by_name['val']._serialized_options = b'\372B\006r\004\020\005\030\005'
  _globals['_STRINGLENBYTES'].fields_by_name['val']._options = None
  _globals['_STRINGLENBYTES'].fields_by_name['val']._serialized_options = b'\372B\005r\003\240\001\004'
  _globals['_STRINGMINBYTES'].fields_by_name['val']._options = None
  _globals['_STRINGMINBYTES'].fields_by_name['val']._serialized_options = b'\372B\004r\002 \004'
  _globals['_STRINGMAXBYTES'].fields_by_name['val']._options = None
  _globals['_STRINGMAXBYTES'].fields_by_name['val']._serialized_options = b'\372B\004r\002(\010'
  _globals['_STRINGMINMAXBYTES'].fields_by_name['val']._options = None
  _globals['_STRINGMINMAXBYTES'].fields_by_name['val']._serialized_options = b'\372B\006r\004 \004(\010'
  _globals['_STRINGEQUALMINMAXBYTES'].fields_by_name['val']._options = None
  _globals['_STRINGEQUALMINMAXBYTES'].fields_by_name['val']._serialized_options = b'\372B\006r\004 \004(\010'
  _globals['_STRINGPATTERN'].fields_by_name['val']._options = None
  _globals['_STRINGPATTERN'].fields_by_name['val']._serialized_options = b'\372B\023r\0212\017(?i)^[a-z0-9]+$'
  _globals['_STRINGPATTERNESCAPES'].fields_by_name['val']._options = None
  _globals['_STRINGPATTERNESCAPES'].fields_by_name['val']._serialized_options = b'\372B\014r\n2\010\\* \\\\ \\w'
  _globals['_STRINGPREFIX'].fields_by_name['val']._options = None
  _globals['_STRINGPREFIX'].fields_by_name['val']._serialized_options = b'\372B\007r\005:\003foo'
  _globals['_STRINGCONTAINS'].fields_by_name['val']._options = None
  _globals['_STRINGCONTAINS'].fields_by_name['val']._serialized_options = b'\372B\007r\005J\003bar'
  _globals['_STRINGNOTCONTAINS'].fields_by_name['val']._options = None
  _globals['_STRINGNOTCONTAINS'].fields_by_name['val']._serialized_options = b'\372B\010r\006\272\001\003bar'
  _globals['_STRINGSUFFIX'].fields_by_name['val']._options = None
  _globals['_STRINGSUFFIX'].fields_by_name['val']._serialized_options = b'\372B\007r\005B\003baz'
  _globals['_STRINGEMAIL'].fields_by_name['val']._options = None
  _globals['_STRINGEMAIL'].fields_by_name['val']._serialized_options = b'\372B\004r\002`\001'
  _globals['_STRINGADDRESS'].fields_by_name['val']._options = None
  _globals['_STRINGADDRESS'].fields_by_name['val']._serialized_options = b'\372B\005r\003\250\001\001'
  _globals['_STRINGHOSTNAME'].fields_by_name['val']._options = None
  _globals['_STRINGHOSTNAME'].fields_by_name['val']._serialized_options = b'\372B\004r\002h\001'
  _globals['_STRINGIP'].fields_by_name['val']._options = None
  _globals['_STRINGIP'].fields_by_name['val']._serialized_options = b'\372B\004r\002p\001'
  _globals['_STRINGIPV4'].fields_by_name['val']._options = None
  _globals['_STRINGIPV4'].fields_by_name['val']._serialized_options = b'\372B\004r\002x\001'
  _globals['_STRINGIPV6'].fields_by_name['val']._options = None
  _globals['_STRINGIPV6'].fields_by_name['val']._serialized_options = b'\372B\005r\003\200\001\001'
  _globals['_STRINGURI'].fields_by_name['val']._options = None
  _globals['_STRINGURI'].fields_by_name['val']._serialized_options = b'\372B\005r\003\210\001\001'
  _globals['_STRINGURIREF'].fields_by_name['val']._options = None
  _globals['_STRINGURIREF'].fields_by_name['val']._serialized_options = b'\372B\005r\003\220\001\001'
  _globals['_STRINGUUID'].fields_by_name['val']._options = None
  _globals['_STRINGUUID'].fields_by_name['val']._serialized_options = b'\372B\005r\003\260\001\001'
  _globals['_STRINGHTTPHEADERNAME'].fields_by_name['val']._options = None
  _globals['_STRINGHTTPHEADERNAME'].fields_by_name['val']._serialized_options = b'\372B\005r\003\300\001\001'
  _globals['_STRINGHTTPHEADERVALUE'].fields_by_name['val']._options = None
  _globals['_STRINGHTTPHEADERVALUE'].fields_by_name['val']._serialized_options = b'\372B\005r\003\300\001\002'
  _globals['_STRINGVALIDHEADER'].fields_by_name['val']._options = None
  _globals['_STRINGVALIDHEADER'].fields_by_name['val']._serialized_options = b'\372B\010r\006\300\001\002\310\001\000'
  _globals['_STRINGUUIDIGNORE'].fields_by_name['val']._options = None
  _globals['_STRINGUUIDIGNORE'].fields_by_name['val']._serialized_options = b'\372B\010r\006\260\001\001\320\001\001'
  _globals['_STRINGINONEOF'].fields_by_name['bar']._options = None
  _globals['_STRINGINONEOF'].fields_by_name['bar']._serialized_options = b'\372B\010r\006R\001aR\001b'
  _globals['_STRINGNONE']._serialized_start=83
  _globals['_STRINGNONE']._serialized_end=108
  _globals['_STRINGCONST']._serialized_start=110
  _globals['_STRINGCONST']._serialized_end=148
  _globals['_STRINGIN']._serialized_start=150
  _globals['_STRINGIN']._serialized_end=190
  _globals['_STRINGNOTIN']._serialized_start=192
  _globals['_STRINGNOTIN']._serialized_end=237
  _globals['_STRINGLEN']._serialized_start=239
  _globals['_STRINGLEN']._serialized_end=273
  _globals['_STRINGMINLEN']._serialized_start=275
  _globals['_STRINGMINLEN']._serialized_end=311
  _globals['_STRINGMAXLEN']._serialized_start=313
  _globals['_STRINGMAXLEN']._serialized_end=349
  _globals['_STRINGMINMAXLEN']._serialized_start=351
  _globals['_STRINGMINMAXLEN']._serialized_end=392
  _globals['_STRINGEQUALMINMAXLEN']._serialized_start=394
  _globals['_STRINGEQUALMINMAXLEN']._serialized_end=440
  _globals['_STRINGLENBYTES']._serialized_start=442
  _globals['_STRINGLENBYTES']._serialized_end=481
  _globals['_STRINGMINBYTES']._serialized_start=483
  _globals['_STRINGMINBYTES']._serialized_end=521
  _globals['_STRINGMAXBYTES']._serialized_start=523
  _globals['_STRINGMAXBYTES']._serialized_end=561
  _globals['_STRINGMINMAXBYTES']._serialized_start=563
  _globals['_STRINGMINMAXBYTES']._serialized_end=606
  _globals['_STRINGEQUALMINMAXBYTES']._serialized_start=608
  _globals['_STRINGEQUALMINMAXBYTES']._serialized_end=656
  _globals['_STRINGPATTERN']._serialized_start=658
  _globals['_STRINGPATTERN']._serialized_end=710
  _globals['_STRINGPATTERNESCAPES']._serialized_start=712
  _globals['_STRINGPATTERNESCAPES']._serialized_end=764
  _globals['_STRINGPREFIX']._serialized_start=766
  _globals['_STRINGPREFIX']._serialized_end=805
  _globals['_STRINGCONTAINS']._serialized_start=807
  _globals['_STRINGCONTAINS']._serialized_end=848
  _globals['_STRINGNOTCONTAINS']._serialized_start=850
  _globals['_STRINGNOTCONTAINS']._serialized_end=895
  _globals['_STRINGSUFFIX']._serialized_start=897
  _globals['_STRINGSUFFIX']._serialized_end=936
  _globals['_STRINGEMAIL']._serialized_start=938
  _globals['_STRINGEMAIL']._serialized_end=973
  _globals['_STRINGADDRESS']._serialized_start=975
  _globals['_STRINGADDRESS']._serialized_end=1013
  _globals['_STRINGHOSTNAME']._serialized_start=1015
  _globals['_STRINGHOSTNAME']._serialized_end=1053
  _globals['_STRINGIP']._serialized_start=1055
  _globals['_STRINGIP']._serialized_end=1087
  _globals['_STRINGIPV4']._serialized_start=1089
  _globals['_STRINGIPV4']._serialized_end=1123
  _globals['_STRINGIPV6']._serialized_start=1125
  _globals['_STRINGIPV6']._serialized_end=1160
  _globals['_STRINGURI']._serialized_start=1162
  _globals['_STRINGURI']._serialized_end=1196
  _globals['_STRINGURIREF']._serialized_start=1198
  _globals['_STRINGURIREF']._serialized_end=1235
  _globals['_STRINGUUID']._serialized_start=1237
  _globals['_STRINGUUID']._serialized_end=1272
  _globals['_STRINGHTTPHEADERNAME']._serialized_start=1274
  _globals['_STRINGHTTPHEADERNAME']._serialized_end=1319
  _globals['_STRINGHTTPHEADERVALUE']._serialized_start=1321
  _globals['_STRINGHTTPHEADERVALUE']._serialized_end=1367
  _globals['_STRINGVALIDHEADER']._serialized_start=1369
  _globals['_STRINGVALIDHEADER']._serialized_end=1414
  _globals['_STRINGUUIDIGNORE']._serialized_start=1416
  _globals['_STRINGUUIDIGNORE']._serialized_end=1460
  _globals['_STRINGINONEOF']._serialized_start=1462
  _globals['_STRINGINONEOF']._serialized_end=1512
# @@protoc_insertion_point(module_scope)
