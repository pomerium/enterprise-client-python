# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/type/matcher/v3/http_inputs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/type/matcher/v3/http_inputs.proto',
  package='envoy.type.matcher.v3',
  syntax='proto3',
  serialized_options=b'\n#io.envoyproxy.envoy.type.matcher.v3B\017HttpInputsProtoP\001ZFgithub.com/envoyproxy/go-control-plane/envoy/type/matcher/v3;matcherv3\272\200\310\321\006\002\020\002',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'envoy/type/matcher/v3/http_inputs.proto\x12\x15\x65nvoy.type.matcher.v3\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"?\n\x1bHttpRequestHeaderMatchInput\x12 \n\x0bheader_name\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xc8\x01\x00\"@\n\x1cHttpRequestTrailerMatchInput\x12 \n\x0bheader_name\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xc8\x01\x00\"@\n\x1cHttpResponseHeaderMatchInput\x12 \n\x0bheader_name\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xc8\x01\x00\"A\n\x1dHttpResponseTrailerMatchInput\x12 \n\x0bheader_name\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x01\xc8\x01\x00\x42\x88\x01\n#io.envoyproxy.envoy.type.matcher.v3B\x0fHttpInputsProtoP\x01ZFgithub.com/envoyproxy/go-control-plane/envoy/type/matcher/v3;matcherv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3'
  ,
  dependencies=[udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_HTTPREQUESTHEADERMATCHINPUT = _descriptor.Descriptor(
  name='HttpRequestHeaderMatchInput',
  full_name='envoy.type.matcher.v3.HttpRequestHeaderMatchInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header_name', full_name='envoy.type.matcher.v3.HttpRequestHeaderMatchInput.header_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\010r\006\300\001\001\310\001\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=185,
)


_HTTPREQUESTTRAILERMATCHINPUT = _descriptor.Descriptor(
  name='HttpRequestTrailerMatchInput',
  full_name='envoy.type.matcher.v3.HttpRequestTrailerMatchInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header_name', full_name='envoy.type.matcher.v3.HttpRequestTrailerMatchInput.header_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\010r\006\300\001\001\310\001\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=251,
)


_HTTPRESPONSEHEADERMATCHINPUT = _descriptor.Descriptor(
  name='HttpResponseHeaderMatchInput',
  full_name='envoy.type.matcher.v3.HttpResponseHeaderMatchInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header_name', full_name='envoy.type.matcher.v3.HttpResponseHeaderMatchInput.header_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\010r\006\300\001\001\310\001\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=317,
)


_HTTPRESPONSETRAILERMATCHINPUT = _descriptor.Descriptor(
  name='HttpResponseTrailerMatchInput',
  full_name='envoy.type.matcher.v3.HttpResponseTrailerMatchInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='header_name', full_name='envoy.type.matcher.v3.HttpResponseTrailerMatchInput.header_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\010r\006\300\001\001\310\001\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=384,
)

DESCRIPTOR.message_types_by_name['HttpRequestHeaderMatchInput'] = _HTTPREQUESTHEADERMATCHINPUT
DESCRIPTOR.message_types_by_name['HttpRequestTrailerMatchInput'] = _HTTPREQUESTTRAILERMATCHINPUT
DESCRIPTOR.message_types_by_name['HttpResponseHeaderMatchInput'] = _HTTPRESPONSEHEADERMATCHINPUT
DESCRIPTOR.message_types_by_name['HttpResponseTrailerMatchInput'] = _HTTPRESPONSETRAILERMATCHINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HttpRequestHeaderMatchInput = _reflection.GeneratedProtocolMessageType('HttpRequestHeaderMatchInput', (_message.Message,), {
  'DESCRIPTOR' : _HTTPREQUESTHEADERMATCHINPUT,
  '__module__' : 'envoy.type.matcher.v3.http_inputs_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.HttpRequestHeaderMatchInput)
  })
_sym_db.RegisterMessage(HttpRequestHeaderMatchInput)

HttpRequestTrailerMatchInput = _reflection.GeneratedProtocolMessageType('HttpRequestTrailerMatchInput', (_message.Message,), {
  'DESCRIPTOR' : _HTTPREQUESTTRAILERMATCHINPUT,
  '__module__' : 'envoy.type.matcher.v3.http_inputs_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.HttpRequestTrailerMatchInput)
  })
_sym_db.RegisterMessage(HttpRequestTrailerMatchInput)

HttpResponseHeaderMatchInput = _reflection.GeneratedProtocolMessageType('HttpResponseHeaderMatchInput', (_message.Message,), {
  'DESCRIPTOR' : _HTTPRESPONSEHEADERMATCHINPUT,
  '__module__' : 'envoy.type.matcher.v3.http_inputs_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.HttpResponseHeaderMatchInput)
  })
_sym_db.RegisterMessage(HttpResponseHeaderMatchInput)

HttpResponseTrailerMatchInput = _reflection.GeneratedProtocolMessageType('HttpResponseTrailerMatchInput', (_message.Message,), {
  'DESCRIPTOR' : _HTTPRESPONSETRAILERMATCHINPUT,
  '__module__' : 'envoy.type.matcher.v3.http_inputs_pb2'
  # @@protoc_insertion_point(class_scope:envoy.type.matcher.v3.HttpResponseTrailerMatchInput)
  })
_sym_db.RegisterMessage(HttpResponseTrailerMatchInput)


DESCRIPTOR._options = None
_HTTPREQUESTHEADERMATCHINPUT.fields_by_name['header_name']._options = None
_HTTPREQUESTTRAILERMATCHINPUT.fields_by_name['header_name']._options = None
_HTTPRESPONSEHEADERMATCHINPUT.fields_by_name['header_name']._options = None
_HTTPRESPONSETRAILERMATCHINPUT.fields_by_name['header_name']._options = None
# @@protoc_insertion_point(module_scope)
