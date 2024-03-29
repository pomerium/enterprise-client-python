# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/cases/strings.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!tests/harness/cases/strings.proto\x12\x13tests.harness.cases\x1a\x17validate/validate.proto\"\x19\n\nStringNone\x12\x0b\n\x03val\x18\x01 \x01(\t\"&\n\x0bStringConst\x12\x17\n\x03val\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\n\x03\x66oo\"(\n\x08StringIn\x12\x1c\n\x03val\x18\x01 \x01(\tB\x0f\xfa\x42\x0cr\nR\x03\x62\x61rR\x03\x62\x61z\"-\n\x0bStringNotIn\x12\x1e\n\x03val\x18\x01 \x01(\tB\x11\xfa\x42\x0er\x0cZ\x04\x66izzZ\x04\x62uzz\"\"\n\tStringLen\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x98\x01\x03\"$\n\x0cStringMinLen\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x03\"$\n\x0cStringMaxLen\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x18\x05\")\n\x0fStringMinMaxLen\x12\x16\n\x03val\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x03\x18\x05\".\n\x14StringEqualMinMaxLen\x12\x16\n\x03val\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04\x10\x05\x18\x05\"\'\n\x0eStringLenBytes\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xa0\x01\x04\"&\n\x0eStringMinBytes\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02 \x04\"&\n\x0eStringMaxBytes\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02(\x08\"+\n\x11StringMinMaxBytes\x12\x16\n\x03val\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04 \x04(\x08\"0\n\x16StringEqualMinMaxBytes\x12\x16\n\x03val\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04 \x04(\x08\"4\n\rStringPattern\x12#\n\x03val\x18\x01 \x01(\tB\x16\xfa\x42\x13r\x11\x32\x0f(?i)^[a-z0-9]+$\"4\n\x14StringPatternEscapes\x12\x1c\n\x03val\x18\x01 \x01(\tB\x0f\xfa\x42\x0cr\n2\x08\\* \\\\ \\w\"\'\n\x0cStringPrefix\x12\x17\n\x03val\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05:\x03\x66oo\")\n\x0eStringContains\x12\x17\n\x03val\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05J\x03\x62\x61r\"-\n\x11StringNotContains\x12\x18\n\x03val\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xba\x01\x03\x62\x61r\"\'\n\x0cStringSuffix\x12\x17\n\x03val\x18\x01 \x01(\tB\n\xfa\x42\x07r\x05\x42\x03\x62\x61z\"#\n\x0bStringEmail\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02`\x01\"&\n\rStringAddress\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xa8\x01\x01\"&\n\x0eStringHostname\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02h\x01\" \n\x08StringIP\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02p\x01\"\"\n\nStringIPv4\x12\x14\n\x03val\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02x\x01\"#\n\nStringIPv6\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x80\x01\x01\"\"\n\tStringURI\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x88\x01\x01\"%\n\x0cStringURIRef\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\x90\x01\x01\"#\n\nStringUUID\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01\"-\n\x14StringHttpHeaderName\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xc0\x01\x01\".\n\x15StringHttpHeaderValue\x12\x15\n\x03val\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xc0\x01\x02\"-\n\x11StringValidHeader\x12\x18\n\x03val\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x02\xc8\x01\x00\",\n\x10StringUUIDIgnore\x12\x18\n\x03val\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xb0\x01\x01\xd0\x01\x01\x42HZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;casesb\x06proto3')



_STRINGNONE = DESCRIPTOR.message_types_by_name['StringNone']
_STRINGCONST = DESCRIPTOR.message_types_by_name['StringConst']
_STRINGIN = DESCRIPTOR.message_types_by_name['StringIn']
_STRINGNOTIN = DESCRIPTOR.message_types_by_name['StringNotIn']
_STRINGLEN = DESCRIPTOR.message_types_by_name['StringLen']
_STRINGMINLEN = DESCRIPTOR.message_types_by_name['StringMinLen']
_STRINGMAXLEN = DESCRIPTOR.message_types_by_name['StringMaxLen']
_STRINGMINMAXLEN = DESCRIPTOR.message_types_by_name['StringMinMaxLen']
_STRINGEQUALMINMAXLEN = DESCRIPTOR.message_types_by_name['StringEqualMinMaxLen']
_STRINGLENBYTES = DESCRIPTOR.message_types_by_name['StringLenBytes']
_STRINGMINBYTES = DESCRIPTOR.message_types_by_name['StringMinBytes']
_STRINGMAXBYTES = DESCRIPTOR.message_types_by_name['StringMaxBytes']
_STRINGMINMAXBYTES = DESCRIPTOR.message_types_by_name['StringMinMaxBytes']
_STRINGEQUALMINMAXBYTES = DESCRIPTOR.message_types_by_name['StringEqualMinMaxBytes']
_STRINGPATTERN = DESCRIPTOR.message_types_by_name['StringPattern']
_STRINGPATTERNESCAPES = DESCRIPTOR.message_types_by_name['StringPatternEscapes']
_STRINGPREFIX = DESCRIPTOR.message_types_by_name['StringPrefix']
_STRINGCONTAINS = DESCRIPTOR.message_types_by_name['StringContains']
_STRINGNOTCONTAINS = DESCRIPTOR.message_types_by_name['StringNotContains']
_STRINGSUFFIX = DESCRIPTOR.message_types_by_name['StringSuffix']
_STRINGEMAIL = DESCRIPTOR.message_types_by_name['StringEmail']
_STRINGADDRESS = DESCRIPTOR.message_types_by_name['StringAddress']
_STRINGHOSTNAME = DESCRIPTOR.message_types_by_name['StringHostname']
_STRINGIP = DESCRIPTOR.message_types_by_name['StringIP']
_STRINGIPV4 = DESCRIPTOR.message_types_by_name['StringIPv4']
_STRINGIPV6 = DESCRIPTOR.message_types_by_name['StringIPv6']
_STRINGURI = DESCRIPTOR.message_types_by_name['StringURI']
_STRINGURIREF = DESCRIPTOR.message_types_by_name['StringURIRef']
_STRINGUUID = DESCRIPTOR.message_types_by_name['StringUUID']
_STRINGHTTPHEADERNAME = DESCRIPTOR.message_types_by_name['StringHttpHeaderName']
_STRINGHTTPHEADERVALUE = DESCRIPTOR.message_types_by_name['StringHttpHeaderValue']
_STRINGVALIDHEADER = DESCRIPTOR.message_types_by_name['StringValidHeader']
_STRINGUUIDIGNORE = DESCRIPTOR.message_types_by_name['StringUUIDIgnore']
StringNone = _reflection.GeneratedProtocolMessageType('StringNone', (_message.Message,), {
  'DESCRIPTOR' : _STRINGNONE,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringNone)
  })
_sym_db.RegisterMessage(StringNone)

StringConst = _reflection.GeneratedProtocolMessageType('StringConst', (_message.Message,), {
  'DESCRIPTOR' : _STRINGCONST,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringConst)
  })
_sym_db.RegisterMessage(StringConst)

StringIn = _reflection.GeneratedProtocolMessageType('StringIn', (_message.Message,), {
  'DESCRIPTOR' : _STRINGIN,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringIn)
  })
_sym_db.RegisterMessage(StringIn)

StringNotIn = _reflection.GeneratedProtocolMessageType('StringNotIn', (_message.Message,), {
  'DESCRIPTOR' : _STRINGNOTIN,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringNotIn)
  })
_sym_db.RegisterMessage(StringNotIn)

StringLen = _reflection.GeneratedProtocolMessageType('StringLen', (_message.Message,), {
  'DESCRIPTOR' : _STRINGLEN,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringLen)
  })
_sym_db.RegisterMessage(StringLen)

StringMinLen = _reflection.GeneratedProtocolMessageType('StringMinLen', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMINLEN,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringMinLen)
  })
_sym_db.RegisterMessage(StringMinLen)

StringMaxLen = _reflection.GeneratedProtocolMessageType('StringMaxLen', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMAXLEN,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringMaxLen)
  })
_sym_db.RegisterMessage(StringMaxLen)

StringMinMaxLen = _reflection.GeneratedProtocolMessageType('StringMinMaxLen', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMINMAXLEN,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringMinMaxLen)
  })
_sym_db.RegisterMessage(StringMinMaxLen)

StringEqualMinMaxLen = _reflection.GeneratedProtocolMessageType('StringEqualMinMaxLen', (_message.Message,), {
  'DESCRIPTOR' : _STRINGEQUALMINMAXLEN,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringEqualMinMaxLen)
  })
_sym_db.RegisterMessage(StringEqualMinMaxLen)

StringLenBytes = _reflection.GeneratedProtocolMessageType('StringLenBytes', (_message.Message,), {
  'DESCRIPTOR' : _STRINGLENBYTES,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringLenBytes)
  })
_sym_db.RegisterMessage(StringLenBytes)

StringMinBytes = _reflection.GeneratedProtocolMessageType('StringMinBytes', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMINBYTES,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringMinBytes)
  })
_sym_db.RegisterMessage(StringMinBytes)

StringMaxBytes = _reflection.GeneratedProtocolMessageType('StringMaxBytes', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMAXBYTES,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringMaxBytes)
  })
_sym_db.RegisterMessage(StringMaxBytes)

StringMinMaxBytes = _reflection.GeneratedProtocolMessageType('StringMinMaxBytes', (_message.Message,), {
  'DESCRIPTOR' : _STRINGMINMAXBYTES,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringMinMaxBytes)
  })
_sym_db.RegisterMessage(StringMinMaxBytes)

StringEqualMinMaxBytes = _reflection.GeneratedProtocolMessageType('StringEqualMinMaxBytes', (_message.Message,), {
  'DESCRIPTOR' : _STRINGEQUALMINMAXBYTES,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringEqualMinMaxBytes)
  })
_sym_db.RegisterMessage(StringEqualMinMaxBytes)

StringPattern = _reflection.GeneratedProtocolMessageType('StringPattern', (_message.Message,), {
  'DESCRIPTOR' : _STRINGPATTERN,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringPattern)
  })
_sym_db.RegisterMessage(StringPattern)

StringPatternEscapes = _reflection.GeneratedProtocolMessageType('StringPatternEscapes', (_message.Message,), {
  'DESCRIPTOR' : _STRINGPATTERNESCAPES,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringPatternEscapes)
  })
_sym_db.RegisterMessage(StringPatternEscapes)

StringPrefix = _reflection.GeneratedProtocolMessageType('StringPrefix', (_message.Message,), {
  'DESCRIPTOR' : _STRINGPREFIX,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringPrefix)
  })
_sym_db.RegisterMessage(StringPrefix)

StringContains = _reflection.GeneratedProtocolMessageType('StringContains', (_message.Message,), {
  'DESCRIPTOR' : _STRINGCONTAINS,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringContains)
  })
_sym_db.RegisterMessage(StringContains)

StringNotContains = _reflection.GeneratedProtocolMessageType('StringNotContains', (_message.Message,), {
  'DESCRIPTOR' : _STRINGNOTCONTAINS,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringNotContains)
  })
_sym_db.RegisterMessage(StringNotContains)

StringSuffix = _reflection.GeneratedProtocolMessageType('StringSuffix', (_message.Message,), {
  'DESCRIPTOR' : _STRINGSUFFIX,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringSuffix)
  })
_sym_db.RegisterMessage(StringSuffix)

StringEmail = _reflection.GeneratedProtocolMessageType('StringEmail', (_message.Message,), {
  'DESCRIPTOR' : _STRINGEMAIL,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringEmail)
  })
_sym_db.RegisterMessage(StringEmail)

StringAddress = _reflection.GeneratedProtocolMessageType('StringAddress', (_message.Message,), {
  'DESCRIPTOR' : _STRINGADDRESS,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringAddress)
  })
_sym_db.RegisterMessage(StringAddress)

StringHostname = _reflection.GeneratedProtocolMessageType('StringHostname', (_message.Message,), {
  'DESCRIPTOR' : _STRINGHOSTNAME,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringHostname)
  })
_sym_db.RegisterMessage(StringHostname)

StringIP = _reflection.GeneratedProtocolMessageType('StringIP', (_message.Message,), {
  'DESCRIPTOR' : _STRINGIP,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringIP)
  })
_sym_db.RegisterMessage(StringIP)

StringIPv4 = _reflection.GeneratedProtocolMessageType('StringIPv4', (_message.Message,), {
  'DESCRIPTOR' : _STRINGIPV4,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringIPv4)
  })
_sym_db.RegisterMessage(StringIPv4)

StringIPv6 = _reflection.GeneratedProtocolMessageType('StringIPv6', (_message.Message,), {
  'DESCRIPTOR' : _STRINGIPV6,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringIPv6)
  })
_sym_db.RegisterMessage(StringIPv6)

StringURI = _reflection.GeneratedProtocolMessageType('StringURI', (_message.Message,), {
  'DESCRIPTOR' : _STRINGURI,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringURI)
  })
_sym_db.RegisterMessage(StringURI)

StringURIRef = _reflection.GeneratedProtocolMessageType('StringURIRef', (_message.Message,), {
  'DESCRIPTOR' : _STRINGURIREF,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringURIRef)
  })
_sym_db.RegisterMessage(StringURIRef)

StringUUID = _reflection.GeneratedProtocolMessageType('StringUUID', (_message.Message,), {
  'DESCRIPTOR' : _STRINGUUID,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringUUID)
  })
_sym_db.RegisterMessage(StringUUID)

StringHttpHeaderName = _reflection.GeneratedProtocolMessageType('StringHttpHeaderName', (_message.Message,), {
  'DESCRIPTOR' : _STRINGHTTPHEADERNAME,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringHttpHeaderName)
  })
_sym_db.RegisterMessage(StringHttpHeaderName)

StringHttpHeaderValue = _reflection.GeneratedProtocolMessageType('StringHttpHeaderValue', (_message.Message,), {
  'DESCRIPTOR' : _STRINGHTTPHEADERVALUE,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringHttpHeaderValue)
  })
_sym_db.RegisterMessage(StringHttpHeaderValue)

StringValidHeader = _reflection.GeneratedProtocolMessageType('StringValidHeader', (_message.Message,), {
  'DESCRIPTOR' : _STRINGVALIDHEADER,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringValidHeader)
  })
_sym_db.RegisterMessage(StringValidHeader)

StringUUIDIgnore = _reflection.GeneratedProtocolMessageType('StringUUIDIgnore', (_message.Message,), {
  'DESCRIPTOR' : _STRINGUUIDIGNORE,
  '__module__' : 'tests.harness.cases.strings_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.StringUUIDIgnore)
  })
_sym_db.RegisterMessage(StringUUIDIgnore)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;cases'
  _STRINGCONST.fields_by_name['val']._options = None
  _STRINGCONST.fields_by_name['val']._serialized_options = b'\372B\007r\005\n\003foo'
  _STRINGIN.fields_by_name['val']._options = None
  _STRINGIN.fields_by_name['val']._serialized_options = b'\372B\014r\nR\003barR\003baz'
  _STRINGNOTIN.fields_by_name['val']._options = None
  _STRINGNOTIN.fields_by_name['val']._serialized_options = b'\372B\016r\014Z\004fizzZ\004buzz'
  _STRINGLEN.fields_by_name['val']._options = None
  _STRINGLEN.fields_by_name['val']._serialized_options = b'\372B\005r\003\230\001\003'
  _STRINGMINLEN.fields_by_name['val']._options = None
  _STRINGMINLEN.fields_by_name['val']._serialized_options = b'\372B\004r\002\020\003'
  _STRINGMAXLEN.fields_by_name['val']._options = None
  _STRINGMAXLEN.fields_by_name['val']._serialized_options = b'\372B\004r\002\030\005'
  _STRINGMINMAXLEN.fields_by_name['val']._options = None
  _STRINGMINMAXLEN.fields_by_name['val']._serialized_options = b'\372B\006r\004\020\003\030\005'
  _STRINGEQUALMINMAXLEN.fields_by_name['val']._options = None
  _STRINGEQUALMINMAXLEN.fields_by_name['val']._serialized_options = b'\372B\006r\004\020\005\030\005'
  _STRINGLENBYTES.fields_by_name['val']._options = None
  _STRINGLENBYTES.fields_by_name['val']._serialized_options = b'\372B\005r\003\240\001\004'
  _STRINGMINBYTES.fields_by_name['val']._options = None
  _STRINGMINBYTES.fields_by_name['val']._serialized_options = b'\372B\004r\002 \004'
  _STRINGMAXBYTES.fields_by_name['val']._options = None
  _STRINGMAXBYTES.fields_by_name['val']._serialized_options = b'\372B\004r\002(\010'
  _STRINGMINMAXBYTES.fields_by_name['val']._options = None
  _STRINGMINMAXBYTES.fields_by_name['val']._serialized_options = b'\372B\006r\004 \004(\010'
  _STRINGEQUALMINMAXBYTES.fields_by_name['val']._options = None
  _STRINGEQUALMINMAXBYTES.fields_by_name['val']._serialized_options = b'\372B\006r\004 \004(\010'
  _STRINGPATTERN.fields_by_name['val']._options = None
  _STRINGPATTERN.fields_by_name['val']._serialized_options = b'\372B\023r\0212\017(?i)^[a-z0-9]+$'
  _STRINGPATTERNESCAPES.fields_by_name['val']._options = None
  _STRINGPATTERNESCAPES.fields_by_name['val']._serialized_options = b'\372B\014r\n2\010\\* \\\\ \\w'
  _STRINGPREFIX.fields_by_name['val']._options = None
  _STRINGPREFIX.fields_by_name['val']._serialized_options = b'\372B\007r\005:\003foo'
  _STRINGCONTAINS.fields_by_name['val']._options = None
  _STRINGCONTAINS.fields_by_name['val']._serialized_options = b'\372B\007r\005J\003bar'
  _STRINGNOTCONTAINS.fields_by_name['val']._options = None
  _STRINGNOTCONTAINS.fields_by_name['val']._serialized_options = b'\372B\010r\006\272\001\003bar'
  _STRINGSUFFIX.fields_by_name['val']._options = None
  _STRINGSUFFIX.fields_by_name['val']._serialized_options = b'\372B\007r\005B\003baz'
  _STRINGEMAIL.fields_by_name['val']._options = None
  _STRINGEMAIL.fields_by_name['val']._serialized_options = b'\372B\004r\002`\001'
  _STRINGADDRESS.fields_by_name['val']._options = None
  _STRINGADDRESS.fields_by_name['val']._serialized_options = b'\372B\005r\003\250\001\001'
  _STRINGHOSTNAME.fields_by_name['val']._options = None
  _STRINGHOSTNAME.fields_by_name['val']._serialized_options = b'\372B\004r\002h\001'
  _STRINGIP.fields_by_name['val']._options = None
  _STRINGIP.fields_by_name['val']._serialized_options = b'\372B\004r\002p\001'
  _STRINGIPV4.fields_by_name['val']._options = None
  _STRINGIPV4.fields_by_name['val']._serialized_options = b'\372B\004r\002x\001'
  _STRINGIPV6.fields_by_name['val']._options = None
  _STRINGIPV6.fields_by_name['val']._serialized_options = b'\372B\005r\003\200\001\001'
  _STRINGURI.fields_by_name['val']._options = None
  _STRINGURI.fields_by_name['val']._serialized_options = b'\372B\005r\003\210\001\001'
  _STRINGURIREF.fields_by_name['val']._options = None
  _STRINGURIREF.fields_by_name['val']._serialized_options = b'\372B\005r\003\220\001\001'
  _STRINGUUID.fields_by_name['val']._options = None
  _STRINGUUID.fields_by_name['val']._serialized_options = b'\372B\005r\003\260\001\001'
  _STRINGHTTPHEADERNAME.fields_by_name['val']._options = None
  _STRINGHTTPHEADERNAME.fields_by_name['val']._serialized_options = b'\372B\005r\003\300\001\001'
  _STRINGHTTPHEADERVALUE.fields_by_name['val']._options = None
  _STRINGHTTPHEADERVALUE.fields_by_name['val']._serialized_options = b'\372B\005r\003\300\001\002'
  _STRINGVALIDHEADER.fields_by_name['val']._options = None
  _STRINGVALIDHEADER.fields_by_name['val']._serialized_options = b'\372B\010r\006\300\001\002\310\001\000'
  _STRINGUUIDIGNORE.fields_by_name['val']._options = None
  _STRINGUUIDIGNORE.fields_by_name['val']._serialized_options = b'\372B\010r\006\260\001\001\320\001\001'
  _STRINGNONE._serialized_start=83
  _STRINGNONE._serialized_end=108
  _STRINGCONST._serialized_start=110
  _STRINGCONST._serialized_end=148
  _STRINGIN._serialized_start=150
  _STRINGIN._serialized_end=190
  _STRINGNOTIN._serialized_start=192
  _STRINGNOTIN._serialized_end=237
  _STRINGLEN._serialized_start=239
  _STRINGLEN._serialized_end=273
  _STRINGMINLEN._serialized_start=275
  _STRINGMINLEN._serialized_end=311
  _STRINGMAXLEN._serialized_start=313
  _STRINGMAXLEN._serialized_end=349
  _STRINGMINMAXLEN._serialized_start=351
  _STRINGMINMAXLEN._serialized_end=392
  _STRINGEQUALMINMAXLEN._serialized_start=394
  _STRINGEQUALMINMAXLEN._serialized_end=440
  _STRINGLENBYTES._serialized_start=442
  _STRINGLENBYTES._serialized_end=481
  _STRINGMINBYTES._serialized_start=483
  _STRINGMINBYTES._serialized_end=521
  _STRINGMAXBYTES._serialized_start=523
  _STRINGMAXBYTES._serialized_end=561
  _STRINGMINMAXBYTES._serialized_start=563
  _STRINGMINMAXBYTES._serialized_end=606
  _STRINGEQUALMINMAXBYTES._serialized_start=608
  _STRINGEQUALMINMAXBYTES._serialized_end=656
  _STRINGPATTERN._serialized_start=658
  _STRINGPATTERN._serialized_end=710
  _STRINGPATTERNESCAPES._serialized_start=712
  _STRINGPATTERNESCAPES._serialized_end=764
  _STRINGPREFIX._serialized_start=766
  _STRINGPREFIX._serialized_end=805
  _STRINGCONTAINS._serialized_start=807
  _STRINGCONTAINS._serialized_end=848
  _STRINGNOTCONTAINS._serialized_start=850
  _STRINGNOTCONTAINS._serialized_end=895
  _STRINGSUFFIX._serialized_start=897
  _STRINGSUFFIX._serialized_end=936
  _STRINGEMAIL._serialized_start=938
  _STRINGEMAIL._serialized_end=973
  _STRINGADDRESS._serialized_start=975
  _STRINGADDRESS._serialized_end=1013
  _STRINGHOSTNAME._serialized_start=1015
  _STRINGHOSTNAME._serialized_end=1053
  _STRINGIP._serialized_start=1055
  _STRINGIP._serialized_end=1087
  _STRINGIPV4._serialized_start=1089
  _STRINGIPV4._serialized_end=1123
  _STRINGIPV6._serialized_start=1125
  _STRINGIPV6._serialized_end=1160
  _STRINGURI._serialized_start=1162
  _STRINGURI._serialized_end=1196
  _STRINGURIREF._serialized_start=1198
  _STRINGURIREF._serialized_end=1235
  _STRINGUUID._serialized_start=1237
  _STRINGUUID._serialized_end=1272
  _STRINGHTTPHEADERNAME._serialized_start=1274
  _STRINGHTTPHEADERNAME._serialized_end=1319
  _STRINGHTTPHEADERVALUE._serialized_start=1321
  _STRINGHTTPHEADERVALUE._serialized_end=1367
  _STRINGVALIDHEADER._serialized_start=1369
  _STRINGVALIDHEADER._serialized_end=1414
  _STRINGUUIDIGNORE._serialized_start=1416
  _STRINGUUIDIGNORE._serialized_end=1460
# @@protoc_insertion_point(module_scope)
