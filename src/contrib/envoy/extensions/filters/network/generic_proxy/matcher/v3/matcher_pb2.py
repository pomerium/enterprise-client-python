# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contrib/envoy/extensions/filters/network/generic_proxy/matcher/v3/matcher.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xds.annotations.v3 import status_pb2 as xds_dot_annotations_dot_v3_dot_status__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOcontrib/envoy/extensions/filters/network/generic_proxy/matcher/v3/matcher.proto\x12\x39\x65nvoy.extensions.filters.network.generic_proxy.matcher.v3\x1a\x1fxds/annotations/v3/status.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\x13\n\x11ServiceMatchInput\"\x12\n\x10MethodMatchInput\"4\n\x12PropertyMatchInput\x12\x1e\n\rproperty_name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x42\xd5\x01\nGio.envoyproxy.envoy.extensions.filters.network.generic_proxy.matcher.v3B\x0cMatcherProtoP\x01Zjgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/matcher/v3;matcherv3\xba\x80\xc8\xd1\x06\x02\x10\x02\xd2\xc6\xa4\xe1\x06\x02\x08\x01\x62\x06proto3')



_SERVICEMATCHINPUT = DESCRIPTOR.message_types_by_name['ServiceMatchInput']
_METHODMATCHINPUT = DESCRIPTOR.message_types_by_name['MethodMatchInput']
_PROPERTYMATCHINPUT = DESCRIPTOR.message_types_by_name['PropertyMatchInput']
ServiceMatchInput = _reflection.GeneratedProtocolMessageType('ServiceMatchInput', (_message.Message,), {
  'DESCRIPTOR' : _SERVICEMATCHINPUT,
  '__module__' : 'contrib.envoy.extensions.filters.network.generic_proxy.matcher.v3.matcher_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.network.generic_proxy.matcher.v3.ServiceMatchInput)
  })
_sym_db.RegisterMessage(ServiceMatchInput)

MethodMatchInput = _reflection.GeneratedProtocolMessageType('MethodMatchInput', (_message.Message,), {
  'DESCRIPTOR' : _METHODMATCHINPUT,
  '__module__' : 'contrib.envoy.extensions.filters.network.generic_proxy.matcher.v3.matcher_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.network.generic_proxy.matcher.v3.MethodMatchInput)
  })
_sym_db.RegisterMessage(MethodMatchInput)

PropertyMatchInput = _reflection.GeneratedProtocolMessageType('PropertyMatchInput', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTYMATCHINPUT,
  '__module__' : 'contrib.envoy.extensions.filters.network.generic_proxy.matcher.v3.matcher_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.filters.network.generic_proxy.matcher.v3.PropertyMatchInput)
  })
_sym_db.RegisterMessage(PropertyMatchInput)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nGio.envoyproxy.envoy.extensions.filters.network.generic_proxy.matcher.v3B\014MatcherProtoP\001Zjgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/network/generic_proxy/matcher/v3;matcherv3\272\200\310\321\006\002\020\002\322\306\244\341\006\002\010\001'
  _PROPERTYMATCHINPUT.fields_by_name['property_name']._options = None
  _PROPERTYMATCHINPUT.fields_by_name['property_name']._serialized_options = b'\372B\004r\002\020\001'
  _SERVICEMATCHINPUT._serialized_start=231
  _SERVICEMATCHINPUT._serialized_end=250
  _METHODMATCHINPUT._serialized_start=252
  _METHODMATCHINPUT._serialized_end=270
  _PROPERTYMATCHINPUT._serialized_start=272
  _PROPERTYMATCHINPUT._serialized_end=324
# @@protoc_insertion_point(module_scope)
