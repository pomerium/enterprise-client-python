# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tests/harness/cases/wkt_timestamp.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'tests/harness/cases/wkt_timestamp.proto\x12\x13tests.harness.cases\x1a\x17validate/validate.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"8\n\rTimestampNone\x12\'\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"F\n\x11TimestampRequired\x12\x31\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xfa\x42\x05\xb2\x01\x02\x08\x01\"E\n\x0eTimestampConst\x12\x33\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xfa\x42\x07\xb2\x01\x04\x12\x02\x08\x03\"@\n\x0bTimestampLT\x12\x31\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xfa\x42\x05\xb2\x01\x02\x1a\x00\"C\n\x0cTimestampLTE\x12\x33\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\n\xfa\x42\x07\xb2\x01\x04\"\x02\x08\x01\"C\n\x0bTimestampGT\x12\x34\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0b\xfa\x42\x08\xb2\x01\x05*\x03\x10\xe8\x07\"E\n\x0cTimestampGTE\x12\x35\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0c\xfa\x42\t\xb2\x01\x06\x32\x04\x10\xc0\x84=\"F\n\rTimestampGTLT\x12\x35\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0c\xfa\x42\t\xb2\x01\x06\x1a\x02\x08\x01*\x00\"H\n\x0fTimestampExLTGT\x12\x35\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0c\xfa\x42\t\xb2\x01\x06\x1a\x00*\x02\x08\x01\"K\n\x0fTimestampGTELTE\x12\x38\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0f\xfa\x42\x0c\xb2\x01\t\"\x03\x08\x90\x1c\x32\x02\x08<\"M\n\x11TimestampExGTELTE\x12\x38\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0f\xfa\x42\x0c\xb2\x01\t\"\x02\x08<2\x03\x08\x90\x1c\"C\n\x0eTimestampLTNow\x12\x31\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xfa\x42\x05\xb2\x01\x02\x38\x01\"C\n\x0eTimestampGTNow\x12\x31\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xfa\x42\x05\xb2\x01\x02@\x01\"G\n\x0fTimestampWithin\x12\x34\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0b\xfa\x42\x08\xb2\x01\x05J\x03\x08\x90\x1c\"N\n\x14TimestampLTNowWithin\x12\x36\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xfa\x42\n\xb2\x01\x07\x38\x01J\x03\x08\x90\x1c\"N\n\x14TimestampGTNowWithin\x12\x36\n\x03val\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\r\xfa\x42\n\xb2\x01\x07@\x01J\x03\x08\x90\x1c\x42HZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;casesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tests.harness.cases.wkt_timestamp_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZFgithub.com/envoyproxy/protoc-gen-validate/tests/harness/cases/go;cases'
  _globals['_TIMESTAMPREQUIRED'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPREQUIRED'].fields_by_name['val']._serialized_options = b'\372B\005\262\001\002\010\001'
  _globals['_TIMESTAMPCONST'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPCONST'].fields_by_name['val']._serialized_options = b'\372B\007\262\001\004\022\002\010\003'
  _globals['_TIMESTAMPLT'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPLT'].fields_by_name['val']._serialized_options = b'\372B\005\262\001\002\032\000'
  _globals['_TIMESTAMPLTE'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPLTE'].fields_by_name['val']._serialized_options = b'\372B\007\262\001\004\"\002\010\001'
  _globals['_TIMESTAMPGT'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPGT'].fields_by_name['val']._serialized_options = b'\372B\010\262\001\005*\003\020\350\007'
  _globals['_TIMESTAMPGTE'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPGTE'].fields_by_name['val']._serialized_options = b'\372B\t\262\001\0062\004\020\300\204='
  _globals['_TIMESTAMPGTLT'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPGTLT'].fields_by_name['val']._serialized_options = b'\372B\t\262\001\006\032\002\010\001*\000'
  _globals['_TIMESTAMPEXLTGT'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPEXLTGT'].fields_by_name['val']._serialized_options = b'\372B\t\262\001\006\032\000*\002\010\001'
  _globals['_TIMESTAMPGTELTE'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPGTELTE'].fields_by_name['val']._serialized_options = b'\372B\014\262\001\t\"\003\010\220\0342\002\010<'
  _globals['_TIMESTAMPEXGTELTE'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPEXGTELTE'].fields_by_name['val']._serialized_options = b'\372B\014\262\001\t\"\002\010<2\003\010\220\034'
  _globals['_TIMESTAMPLTNOW'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPLTNOW'].fields_by_name['val']._serialized_options = b'\372B\005\262\001\0028\001'
  _globals['_TIMESTAMPGTNOW'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPGTNOW'].fields_by_name['val']._serialized_options = b'\372B\005\262\001\002@\001'
  _globals['_TIMESTAMPWITHIN'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPWITHIN'].fields_by_name['val']._serialized_options = b'\372B\010\262\001\005J\003\010\220\034'
  _globals['_TIMESTAMPLTNOWWITHIN'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPLTNOWWITHIN'].fields_by_name['val']._serialized_options = b'\372B\n\262\001\0078\001J\003\010\220\034'
  _globals['_TIMESTAMPGTNOWWITHIN'].fields_by_name['val']._options = None
  _globals['_TIMESTAMPGTNOWWITHIN'].fields_by_name['val']._serialized_options = b'\372B\n\262\001\007@\001J\003\010\220\034'
  _globals['_TIMESTAMPNONE']._serialized_start=122
  _globals['_TIMESTAMPNONE']._serialized_end=178
  _globals['_TIMESTAMPREQUIRED']._serialized_start=180
  _globals['_TIMESTAMPREQUIRED']._serialized_end=250
  _globals['_TIMESTAMPCONST']._serialized_start=252
  _globals['_TIMESTAMPCONST']._serialized_end=321
  _globals['_TIMESTAMPLT']._serialized_start=323
  _globals['_TIMESTAMPLT']._serialized_end=387
  _globals['_TIMESTAMPLTE']._serialized_start=389
  _globals['_TIMESTAMPLTE']._serialized_end=456
  _globals['_TIMESTAMPGT']._serialized_start=458
  _globals['_TIMESTAMPGT']._serialized_end=525
  _globals['_TIMESTAMPGTE']._serialized_start=527
  _globals['_TIMESTAMPGTE']._serialized_end=596
  _globals['_TIMESTAMPGTLT']._serialized_start=598
  _globals['_TIMESTAMPGTLT']._serialized_end=668
  _globals['_TIMESTAMPEXLTGT']._serialized_start=670
  _globals['_TIMESTAMPEXLTGT']._serialized_end=742
  _globals['_TIMESTAMPGTELTE']._serialized_start=744
  _globals['_TIMESTAMPGTELTE']._serialized_end=819
  _globals['_TIMESTAMPEXGTELTE']._serialized_start=821
  _globals['_TIMESTAMPEXGTELTE']._serialized_end=898
  _globals['_TIMESTAMPLTNOW']._serialized_start=900
  _globals['_TIMESTAMPLTNOW']._serialized_end=967
  _globals['_TIMESTAMPGTNOW']._serialized_start=969
  _globals['_TIMESTAMPGTNOW']._serialized_end=1036
  _globals['_TIMESTAMPWITHIN']._serialized_start=1038
  _globals['_TIMESTAMPWITHIN']._serialized_end=1109
  _globals['_TIMESTAMPLTNOWWITHIN']._serialized_start=1111
  _globals['_TIMESTAMPLTNOWWITHIN']._serialized_end=1189
  _globals['_TIMESTAMPGTNOWWITHIN']._serialized_start=1191
  _globals['_TIMESTAMPGTNOWWITHIN']._serialized_end=1269
# @@protoc_insertion_point(module_scope)
