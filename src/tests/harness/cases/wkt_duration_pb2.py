# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/cases/wkt_duration.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&tests/harness/cases/wkt_duration.proto\x12\x13tests.harness.cases\x1a\x17validate/validate.proto\x1a\x1egoogle/protobuf/duration.proto\"6\n\x0c\x44urationNone\x12&\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"D\n\x10\x44urationRequired\x12\x30\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\x42\x05\xaa\x01\x02\x08\x01\"C\n\rDurationConst\x12\x32\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xfa\x42\x07\xaa\x01\x04\x12\x02\x08\x03\"E\n\nDurationIn\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0f\xfa\x42\x0c\xaa\x01\t:\x02\x08\x01:\x03\x10\xe8\x07\"A\n\rDurationNotIn\x12\x30\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\x42\x05\xaa\x01\x02\x42\x00\">\n\nDurationLT\x12\x30\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\x42\x05\xaa\x01\x02\x1a\x00\"A\n\x0b\x44urationLTE\x12\x32\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xfa\x42\x07\xaa\x01\x04\"\x02\x08\x01\"A\n\nDurationGT\x12\x33\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0b\xfa\x42\x08\xaa\x01\x05*\x03\x10\xe8\x07\"C\n\x0b\x44urationGTE\x12\x34\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xfa\x42\t\xaa\x01\x06\x32\x04\x10\xc0\x84=\"D\n\x0c\x44urationGTLT\x12\x34\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xfa\x42\t\xaa\x01\x06\x1a\x02\x08\x01*\x00\"F\n\x0e\x44urationExLTGT\x12\x34\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xfa\x42\t\xaa\x01\x06\x1a\x00*\x02\x08\x01\"I\n\x0e\x44urationGTELTE\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0f\xfa\x42\x0c\xaa\x01\t\"\x03\x08\x90\x1c\x32\x02\x08<\"K\n\x10\x44urationExGTELTE\x12\x37\n\x03val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0f\xfa\x42\x0c\xaa\x01\t\"\x02\x08<2\x03\x08\x90\x1c\"u\n\x1c\x44urationFieldWithOtherFields\x12;\n\x0c\x64uration_val\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\n\xfa\x42\x07\xaa\x01\x04\"\x02\x08\x01\x12\x18\n\x07int_val\x18\x02 \x01(\x05\x42\x07\xfa\x42\x04\x1a\x02 \x10\x42HZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;casesb\x06proto3')



_DURATIONNONE = DESCRIPTOR.message_types_by_name['DurationNone']
_DURATIONREQUIRED = DESCRIPTOR.message_types_by_name['DurationRequired']
_DURATIONCONST = DESCRIPTOR.message_types_by_name['DurationConst']
_DURATIONIN = DESCRIPTOR.message_types_by_name['DurationIn']
_DURATIONNOTIN = DESCRIPTOR.message_types_by_name['DurationNotIn']
_DURATIONLT = DESCRIPTOR.message_types_by_name['DurationLT']
_DURATIONLTE = DESCRIPTOR.message_types_by_name['DurationLTE']
_DURATIONGT = DESCRIPTOR.message_types_by_name['DurationGT']
_DURATIONGTE = DESCRIPTOR.message_types_by_name['DurationGTE']
_DURATIONGTLT = DESCRIPTOR.message_types_by_name['DurationGTLT']
_DURATIONEXLTGT = DESCRIPTOR.message_types_by_name['DurationExLTGT']
_DURATIONGTELTE = DESCRIPTOR.message_types_by_name['DurationGTELTE']
_DURATIONEXGTELTE = DESCRIPTOR.message_types_by_name['DurationExGTELTE']
_DURATIONFIELDWITHOTHERFIELDS = DESCRIPTOR.message_types_by_name['DurationFieldWithOtherFields']
DurationNone = _reflection.GeneratedProtocolMessageType('DurationNone', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONNONE,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationNone)
  })
_sym_db.RegisterMessage(DurationNone)

DurationRequired = _reflection.GeneratedProtocolMessageType('DurationRequired', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONREQUIRED,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationRequired)
  })
_sym_db.RegisterMessage(DurationRequired)

DurationConst = _reflection.GeneratedProtocolMessageType('DurationConst', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONCONST,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationConst)
  })
_sym_db.RegisterMessage(DurationConst)

DurationIn = _reflection.GeneratedProtocolMessageType('DurationIn', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONIN,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationIn)
  })
_sym_db.RegisterMessage(DurationIn)

DurationNotIn = _reflection.GeneratedProtocolMessageType('DurationNotIn', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONNOTIN,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationNotIn)
  })
_sym_db.RegisterMessage(DurationNotIn)

DurationLT = _reflection.GeneratedProtocolMessageType('DurationLT', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONLT,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationLT)
  })
_sym_db.RegisterMessage(DurationLT)

DurationLTE = _reflection.GeneratedProtocolMessageType('DurationLTE', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONLTE,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationLTE)
  })
_sym_db.RegisterMessage(DurationLTE)

DurationGT = _reflection.GeneratedProtocolMessageType('DurationGT', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONGT,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationGT)
  })
_sym_db.RegisterMessage(DurationGT)

DurationGTE = _reflection.GeneratedProtocolMessageType('DurationGTE', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONGTE,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationGTE)
  })
_sym_db.RegisterMessage(DurationGTE)

DurationGTLT = _reflection.GeneratedProtocolMessageType('DurationGTLT', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONGTLT,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationGTLT)
  })
_sym_db.RegisterMessage(DurationGTLT)

DurationExLTGT = _reflection.GeneratedProtocolMessageType('DurationExLTGT', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONEXLTGT,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationExLTGT)
  })
_sym_db.RegisterMessage(DurationExLTGT)

DurationGTELTE = _reflection.GeneratedProtocolMessageType('DurationGTELTE', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONGTELTE,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationGTELTE)
  })
_sym_db.RegisterMessage(DurationGTELTE)

DurationExGTELTE = _reflection.GeneratedProtocolMessageType('DurationExGTELTE', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONEXGTELTE,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationExGTELTE)
  })
_sym_db.RegisterMessage(DurationExGTELTE)

DurationFieldWithOtherFields = _reflection.GeneratedProtocolMessageType('DurationFieldWithOtherFields', (_message.Message,), {
  'DESCRIPTOR' : _DURATIONFIELDWITHOTHERFIELDS,
  '__module__' : 'tests.harness.cases.wkt_duration_pb2'
  # @@protoc_insertion_point(class_scope:tests.harness.cases.DurationFieldWithOtherFields)
  })
_sym_db.RegisterMessage(DurationFieldWithOtherFields)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;cases'
  _DURATIONREQUIRED.fields_by_name['val']._options = None
  _DURATIONREQUIRED.fields_by_name['val']._serialized_options = b'\372B\005\252\001\002\010\001'
  _DURATIONCONST.fields_by_name['val']._options = None
  _DURATIONCONST.fields_by_name['val']._serialized_options = b'\372B\007\252\001\004\022\002\010\003'
  _DURATIONIN.fields_by_name['val']._options = None
  _DURATIONIN.fields_by_name['val']._serialized_options = b'\372B\014\252\001\t:\002\010\001:\003\020\350\007'
  _DURATIONNOTIN.fields_by_name['val']._options = None
  _DURATIONNOTIN.fields_by_name['val']._serialized_options = b'\372B\005\252\001\002B\000'
  _DURATIONLT.fields_by_name['val']._options = None
  _DURATIONLT.fields_by_name['val']._serialized_options = b'\372B\005\252\001\002\032\000'
  _DURATIONLTE.fields_by_name['val']._options = None
  _DURATIONLTE.fields_by_name['val']._serialized_options = b'\372B\007\252\001\004\"\002\010\001'
  _DURATIONGT.fields_by_name['val']._options = None
  _DURATIONGT.fields_by_name['val']._serialized_options = b'\372B\010\252\001\005*\003\020\350\007'
  _DURATIONGTE.fields_by_name['val']._options = None
  _DURATIONGTE.fields_by_name['val']._serialized_options = b'\372B\t\252\001\0062\004\020\300\204='
  _DURATIONGTLT.fields_by_name['val']._options = None
  _DURATIONGTLT.fields_by_name['val']._serialized_options = b'\372B\t\252\001\006\032\002\010\001*\000'
  _DURATIONEXLTGT.fields_by_name['val']._options = None
  _DURATIONEXLTGT.fields_by_name['val']._serialized_options = b'\372B\t\252\001\006\032\000*\002\010\001'
  _DURATIONGTELTE.fields_by_name['val']._options = None
  _DURATIONGTELTE.fields_by_name['val']._serialized_options = b'\372B\014\252\001\t\"\003\010\220\0342\002\010<'
  _DURATIONEXGTELTE.fields_by_name['val']._options = None
  _DURATIONEXGTELTE.fields_by_name['val']._serialized_options = b'\372B\014\252\001\t\"\002\010<2\003\010\220\034'
  _DURATIONFIELDWITHOTHERFIELDS.fields_by_name['duration_val']._options = None
  _DURATIONFIELDWITHOTHERFIELDS.fields_by_name['duration_val']._serialized_options = b'\372B\007\252\001\004\"\002\010\001'
  _DURATIONFIELDWITHOTHERFIELDS.fields_by_name['int_val']._options = None
  _DURATIONFIELDWITHOTHERFIELDS.fields_by_name['int_val']._serialized_options = b'\372B\004\032\002 \020'
  _DURATIONNONE._serialized_start=120
  _DURATIONNONE._serialized_end=174
  _DURATIONREQUIRED._serialized_start=176
  _DURATIONREQUIRED._serialized_end=244
  _DURATIONCONST._serialized_start=246
  _DURATIONCONST._serialized_end=313
  _DURATIONIN._serialized_start=315
  _DURATIONIN._serialized_end=384
  _DURATIONNOTIN._serialized_start=386
  _DURATIONNOTIN._serialized_end=451
  _DURATIONLT._serialized_start=453
  _DURATIONLT._serialized_end=515
  _DURATIONLTE._serialized_start=517
  _DURATIONLTE._serialized_end=582
  _DURATIONGT._serialized_start=584
  _DURATIONGT._serialized_end=649
  _DURATIONGTE._serialized_start=651
  _DURATIONGTE._serialized_end=718
  _DURATIONGTLT._serialized_start=720
  _DURATIONGTLT._serialized_end=788
  _DURATIONEXLTGT._serialized_start=790
  _DURATIONEXLTGT._serialized_end=860
  _DURATIONGTELTE._serialized_start=862
  _DURATIONGTELTE._serialized_end=935
  _DURATIONEXGTELTE._serialized_start=937
  _DURATIONEXGTELTE._serialized_end=1012
  _DURATIONFIELDWITHOTHERFIELDS._serialized_start=1014
  _DURATIONFIELDWITHOTHERFIELDS._serialized_end=1131
# @@protoc_insertion_point(module_scope)
