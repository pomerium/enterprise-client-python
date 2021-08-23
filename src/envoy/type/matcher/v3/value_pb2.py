# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/v3/value.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.type.matcher.v3 import number_pb2 as envoy_dot_type_dot_matcher_dot_v3_dot_number__pb2
from envoy.type.matcher.v3 import string_pb2 as envoy_dot_type_dot_matcher_dot_v3_dot_string__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/v3/value.proto',
  package='envoy.type.matcher.v3',
  syntax='proto3',
  serialized_options=b'\n#io.envoyproxy.envoy.type.matcher.v3B\nValueProtoP\001\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!envoy/type/matcher/v3/value.proto\x12\x15\x65nvoy.type.matcher.v3\x1a\"envoy/type/matcher/v3/number.proto\x1a\"envoy/type/matcher/v3/string.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xb5\x03\n\x0cValueMatcher\x12\x43\n\nnull_match\x18\x01 \x01(\x0b\x32-.envoy.type.matcher.v3.ValueMatcher.NullMatchH\x00\x12<\n\x0c\x64ouble_match\x18\x02 \x01(\x0b\x32$.envoy.type.matcher.v3.DoubleMatcherH\x00\x12<\n\x0cstring_match\x18\x03 \x01(\x0b\x32$.envoy.type.matcher.v3.StringMatcherH\x00\x12\x14\n\nbool_match\x18\x04 \x01(\x08H\x00\x12\x17\n\rpresent_match\x18\x05 \x01(\x08H\x00\x12\x38\n\nlist_match\x18\x06 \x01(\x0b\x32\".envoy.type.matcher.v3.ListMatcherH\x00\x1a=\n\tNullMatch:0\x9a\xc5\x88\x1e+\n)envoy.type.matcher.ValueMatcher.NullMatch:&\x9a\xc5\x88\x1e!\n\x1f\x65nvoy.type.matcher.ValueMatcherB\x14\n\rmatch_pattern\x12\x03\xf8\x42\x01\"\x81\x01\n\x0bListMatcher\x12\x35\n\x06one_of\x18\x01 \x01(\x0b\x32#.envoy.type.matcher.v3.ValueMatcherH\x00:%\x9a\xc5\x88\x1e \n\x1e\x65nvoy.type.matcher.ListMatcherB\x14\n\rmatch_pattern\x12\x03\xf8\x42\x01\x42;\n#io.envoyproxy.envoy.type.matcher.v3B\nValueProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[envoy_dot_type_dot_matcher_dot_v3_dot_number__pb2.DESCRIPTOR,envoy_dot_type_dot_matcher_dot_v3_dot_string__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_VALUEMATCHER_NULLMATCH = _descriptor.Descriptor(
  name='NullMatch',
  full_name='envoy.type.matcher.v3.ValueMatcher.NullMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036+\n)envoy.type.matcher.ValueMatcher.NullMatch',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=538,
  serialized_end=599,
)

_VALUEMATCHER = _descriptor.Descriptor(
  name='ValueMatcher',
  full_name='envoy.type.matcher.v3.ValueMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='null_match', full_name='envoy.type.matcher.v3.ValueMatcher.null_match', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='double_match', full_name='envoy.type.matcher.v3.ValueMatcher.double_match', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='string_match', full_name='envoy.type.matcher.v3.ValueMatcher.string_match', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_match', full_name='envoy.type.matcher.v3.ValueMatcher.bool_match', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='present_match', full_name='envoy.type.matcher.v3.ValueMatcher.present_match', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='list_match', full_name='envoy.type.matcher.v3.ValueMatcher.list_match', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_VALUEMATCHER_NULLMATCH, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036!\n\037envoy.type.matcher.ValueMatcher',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='match_pattern', full_name='envoy.type.matcher.v3.ValueMatcher.match_pattern',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=224,
  serialized_end=661,
)


_LISTMATCHER = _descriptor.Descriptor(
  name='ListMatcher',
  full_name='envoy.type.matcher.v3.ListMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='one_of', full_name='envoy.type.matcher.v3.ListMatcher.one_of', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036 \n\036envoy.type.matcher.ListMatcher',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='match_pattern', full_name='envoy.type.matcher.v3.ListMatcher.match_pattern',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=664,
  serialized_end=793,
)

_VALUEMATCHER_NULLMATCH.containing_type = _VALUEMATCHER
_VALUEMATCHER.fields_by_name['null_match'].message_type = _VALUEMATCHER_NULLMATCH
_VALUEMATCHER.fields_by_name['double_match'].message_type = envoy_dot_type_dot_matcher_dot_v3_dot_number__pb2._DOUBLEMATCHER
_VALUEMATCHER.fields_by_name['string_match'].message_type = envoy_dot_type_dot_matcher_dot_v3_dot_string__pb2._STRINGMATCHER
_VALUEMATCHER.fields_by_name['list_match'].message_type = _LISTMATCHER
_VALUEMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _VALUEMATCHER.fields_by_name['null_match'])
_VALUEMATCHER.fields_by_name['null_match'].containing_oneof = _VALUEMATCHER.oneofs_by_name['match_pattern']
_VALUEMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _VALUEMATCHER.fields_by_name['double_match'])
_VALUEMATCHER.fields_by_name['double_match'].containing_oneof = _VALUEMATCHER.oneofs_by_name['match_pattern']
_VALUEMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _VALUEMATCHER.fields_by_name['string_match'])
_VALUEMATCHER.fields_by_name['string_match'].containing_oneof = _VALUEMATCHER.oneofs_by_name['match_pattern']
_VALUEMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _VALUEMATCHER.fields_by_name['bool_match'])
_VALUEMATCHER.fields_by_name['bool_match'].containing_oneof = _VALUEMATCHER.oneofs_by_name['match_pattern']
_VALUEMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _VALUEMATCHER.fields_by_name['present_match'])
_VALUEMATCHER.fields_by_name['present_match'].containing_oneof = _VALUEMATCHER.oneofs_by_name['match_pattern']
_VALUEMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _VALUEMATCHER.fields_by_name['list_match'])
_VALUEMATCHER.fields_by_name['list_match'].containing_oneof = _VALUEMATCHER.oneofs_by_name['match_pattern']
_LISTMATCHER.fields_by_name['one_of'].message_type = _VALUEMATCHER
_LISTMATCHER.oneofs_by_name['match_pattern'].fields.append(
  _LISTMATCHER.fields_by_name['one_of'])
_LISTMATCHER.fields_by_name['one_of'].containing_oneof = _LISTMATCHER.oneofs_by_name['match_pattern']
DESCRIPTOR.message_types_by_name['ValueMatcher'] = _VALUEMATCHER
DESCRIPTOR.message_types_by_name['ListMatcher'] = _LISTMATCHER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ValueMatcher = _reflection.GeneratedProtocolMessageType('ValueMatcher', (_message.Message,), {

  'NullMatch' : _reflection.GeneratedProtocolMessageType('NullMatch', (_message.Message,), {
    'DESCRIPTOR' : _VALUEMATCHER_NULLMATCH,
    '__module__' : 'envoy.type.matcher.v3.value_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.ValueMatcher.NullMatch)
    })
  ,
  'DESCRIPTOR' : _VALUEMATCHER,
  '__module__' : 'envoy.type.matcher.v3.value_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.ValueMatcher)
  })
_sym_db.RegisterMessage(ValueMatcher)
_sym_db.RegisterMessage(ValueMatcher.NullMatch)

ListMatcher = _reflection.GeneratedProtocolMessageType('ListMatcher', (_message.Message,), {
  'DESCRIPTOR' : _LISTMATCHER,
  '__module__' : 'envoy.type.matcher.v3.value_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.ListMatcher)
  })
_sym_db.RegisterMessage(ListMatcher)


DESCRIPTOR._options = None
_VALUEMATCHER_NULLMATCH._options = None
_VALUEMATCHER.oneofs_by_name['match_pattern']._options = None
_VALUEMATCHER._options = None
_LISTMATCHER.oneofs_by_name['match_pattern']._options = None
_LISTMATCHER._options = None
# @@protoc_insertion_point(module_scope)