# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/v3/regex.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/v3/regex.proto',
  package='envoy.type.matcher.v3',
  syntax='proto3',
  serialized_options=b'\n#io.envoyproxy.envoy.type.matcher.v3B\nRegexProtoP\001ZFgithub.com/envoyproxy/go-control-plane/envoy/type/matcher/v3;matcherv3\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!envoy/type/matcher/v3/regex.proto\x12\x15\x65nvoy.type.matcher.v3\x1a\x1egoogle/protobuf/wrappers.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xb6\x02\n\x0cRegexMatcher\x12M\n\ngoogle_re2\x18\x01 \x01(\x0b\x32-.envoy.type.matcher.v3.RegexMatcher.GoogleRE2B\x08\xfa\x42\x05\x8a\x01\x02\x10\x01H\x00\x12\x16\n\x05regex\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x1a\x82\x01\n\tGoogleRE2\x12\x43\n\x10max_program_size\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0:0\x9a\xc5\x88\x1e+\n)envoy.type.matcher.RegexMatcher.GoogleRE2:&\x9a\xc5\x88\x1e!\n\x1f\x65nvoy.type.matcher.RegexMatcherB\x12\n\x0b\x65ngine_type\x12\x03\xf8\x42\x01\"\xa2\x01\n\x17RegexMatchAndSubstitute\x12>\n\x07pattern\x18\x01 \x01(\x0b\x32#.envoy.type.matcher.v3.RegexMatcherB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x14\n\x0csubstitution\x18\x02 \x01(\t:1\x9a\xc5\x88\x1e,\n*envoy.type.matcher.RegexMatchAndSubstituteB\x83\x01\n#io.envoyproxy.envoy.type.matcher.v3B\nRegexProtoP\x01ZFgithub.com/envoyproxy/go-control-plane/envoy/type/matcher/v3;matcherv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,envoy_dot_annotations_dot_deprecation__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_REGEXMATCHER_GOOGLERE2 = _descriptor.Descriptor(
  name='GoogleRE2',
  full_name='envoy.type.matcher.v3.RegexMatcher.GoogleRE2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_program_size', full_name='envoy.type.matcher.v3.RegexMatcher.GoogleRE2.max_program_size', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001\222\307\206\330\004\0033.0', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036+\n)envoy.type.matcher.RegexMatcher.GoogleRE2',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=471,
)

_REGEXMATCHER = _descriptor.Descriptor(
  name='RegexMatcher',
  full_name='envoy.type.matcher.v3.RegexMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='google_re2', full_name='envoy.type.matcher.v3.RegexMatcher.google_re2', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\212\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='regex', full_name='envoy.type.matcher.v3.RegexMatcher.regex', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REGEXMATCHER_GOOGLERE2, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036!\n\037envoy.type.matcher.RegexMatcher',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='engine_type', full_name='envoy.type.matcher.v3.RegexMatcher.engine_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\370B\001'),
  ],
  serialized_start=221,
  serialized_end=531,
)


_REGEXMATCHANDSUBSTITUTE = _descriptor.Descriptor(
  name='RegexMatchAndSubstitute',
  full_name='envoy.type.matcher.v3.RegexMatchAndSubstitute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pattern', full_name='envoy.type.matcher.v3.RegexMatchAndSubstitute.pattern', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\212\001\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='substitution', full_name='envoy.type.matcher.v3.RegexMatchAndSubstitute.substitution', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036,\n*envoy.type.matcher.RegexMatchAndSubstitute',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=534,
  serialized_end=696,
)

_REGEXMATCHER_GOOGLERE2.fields_by_name['max_program_size'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_REGEXMATCHER_GOOGLERE2.containing_type = _REGEXMATCHER
_REGEXMATCHER.fields_by_name['google_re2'].message_type = _REGEXMATCHER_GOOGLERE2
_REGEXMATCHER.oneofs_by_name['engine_type'].fields.append(
  _REGEXMATCHER.fields_by_name['google_re2'])
_REGEXMATCHER.fields_by_name['google_re2'].containing_oneof = _REGEXMATCHER.oneofs_by_name['engine_type']
_REGEXMATCHANDSUBSTITUTE.fields_by_name['pattern'].message_type = _REGEXMATCHER
DESCRIPTOR.message_types_by_name['RegexMatcher'] = _REGEXMATCHER
DESCRIPTOR.message_types_by_name['RegexMatchAndSubstitute'] = _REGEXMATCHANDSUBSTITUTE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegexMatcher = _reflection.GeneratedProtocolMessageType('RegexMatcher', (_message.Message,), {

  'GoogleRE2' : _reflection.GeneratedProtocolMessageType('GoogleRE2', (_message.Message,), {
    'DESCRIPTOR' : _REGEXMATCHER_GOOGLERE2,
    '__module__' : 'envoy.type.matcher.v3.regex_pb2'
    # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.RegexMatcher.GoogleRE2)
    })
  ,
  'DESCRIPTOR' : _REGEXMATCHER,
  '__module__' : 'envoy.type.matcher.v3.regex_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.RegexMatcher)
  })
_sym_db.RegisterMessage(RegexMatcher)
_sym_db.RegisterMessage(RegexMatcher.GoogleRE2)

RegexMatchAndSubstitute = _reflection.GeneratedProtocolMessageType('RegexMatchAndSubstitute', (_message.Message,), {
  'DESCRIPTOR' : _REGEXMATCHANDSUBSTITUTE,
  '__module__' : 'envoy.type.matcher.v3.regex_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.RegexMatchAndSubstitute)
  })
_sym_db.RegisterMessage(RegexMatchAndSubstitute)


DESCRIPTOR._options = None
_REGEXMATCHER_GOOGLERE2.fields_by_name['max_program_size']._options = None
_REGEXMATCHER_GOOGLERE2._options = None
_REGEXMATCHER.oneofs_by_name['engine_type']._options = None
_REGEXMATCHER.fields_by_name['google_re2']._options = None
_REGEXMATCHER.fields_by_name['regex']._options = None
_REGEXMATCHER._options = None
_REGEXMATCHANDSUBSTITUTE.fields_by_name['pattern']._options = None
_REGEXMATCHANDSUBSTITUTE._options = None
# @@protoc_insertion_point(module_scope)
