# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: route_redirect_action.proto
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
    'route_redirect_action.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1broute_redirect_action.proto\x12\x12pomerium.dashboard\x1a\x17validate/validate.proto\"\x98\x05\n\x0eRedirectAction\x12\x18\n\x0ehttps_redirect\x18\x04 \x01(\x08H\x00\x12\x19\n\x0fscheme_redirect\x18\x07 \x01(\tH\x00\x12\"\n\rhost_redirect\x18\x01 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x02\xc8\x01\x00\x12\x15\n\rport_redirect\x18\x08 \x01(\r\x12$\n\rpath_redirect\x18\x02 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x02\xc8\x01\x00H\x01\x12%\n\x0eprefix_rewrite\x18\x05 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x02\xc8\x01\x00H\x01\x12S\n\rregex_rewrite\x18\t \x01(\x0b\x32:.pomerium.dashboard.RedirectAction.RegexMatchAndSubstituteH\x01\x12X\n\rresponse_code\x18\x03 \x01(\x0e\x32\x37.pomerium.dashboard.RedirectAction.RedirectResponseCodeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x13\n\x0bstrip_query\x18\x06 \x01(\x08\x1aV\n\x17RegexMatchAndSubstitute\x12\x18\n\x07pattern\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12!\n\x0csubstitution\x18\x02 \x01(\tB\x0b\xfa\x42\x08r\x06\xc0\x01\x02\xc8\x01\x00\"w\n\x14RedirectResponseCode\x12\x15\n\x11MOVED_PERMANENTLY\x10\x00\x12\t\n\x05\x46OUND\x10\x01\x12\r\n\tSEE_OTHER\x10\x02\x12\x16\n\x12TEMPORARY_REDIRECT\x10\x03\x12\x16\n\x12PERMANENT_REDIRECT\x10\x04\x42\x1a\n\x18scheme_rewrite_specifierB\x18\n\x16path_rewrite_specifierB-Z+github.com/pomerium/pomerium-console/pkg/pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'route_redirect_action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/pomerium/pomerium-console/pkg/pb'
  _globals['_REDIRECTACTION_REGEXMATCHANDSUBSTITUTE'].fields_by_name['pattern']._loaded_options = None
  _globals['_REDIRECTACTION_REGEXMATCHANDSUBSTITUTE'].fields_by_name['pattern']._serialized_options = b'\372B\004r\002\020\001'
  _globals['_REDIRECTACTION_REGEXMATCHANDSUBSTITUTE'].fields_by_name['substitution']._loaded_options = None
  _globals['_REDIRECTACTION_REGEXMATCHANDSUBSTITUTE'].fields_by_name['substitution']._serialized_options = b'\372B\010r\006\300\001\002\310\001\000'
  _globals['_REDIRECTACTION'].fields_by_name['host_redirect']._loaded_options = None
  _globals['_REDIRECTACTION'].fields_by_name['host_redirect']._serialized_options = b'\372B\010r\006\300\001\002\310\001\000'
  _globals['_REDIRECTACTION'].fields_by_name['path_redirect']._loaded_options = None
  _globals['_REDIRECTACTION'].fields_by_name['path_redirect']._serialized_options = b'\372B\010r\006\300\001\002\310\001\000'
  _globals['_REDIRECTACTION'].fields_by_name['prefix_rewrite']._loaded_options = None
  _globals['_REDIRECTACTION'].fields_by_name['prefix_rewrite']._serialized_options = b'\372B\010r\006\300\001\002\310\001\000'
  _globals['_REDIRECTACTION'].fields_by_name['response_code']._loaded_options = None
  _globals['_REDIRECTACTION'].fields_by_name['response_code']._serialized_options = b'\372B\005\202\001\002\020\001'
  _globals['_REDIRECTACTION']._serialized_start=77
  _globals['_REDIRECTACTION']._serialized_end=741
  _globals['_REDIRECTACTION_REGEXMATCHANDSUBSTITUTE']._serialized_start=480
  _globals['_REDIRECTACTION_REGEXMATCHANDSUBSTITUTE']._serialized_end=566
  _globals['_REDIRECTACTION_REDIRECTRESPONSECODE']._serialized_start=568
  _globals['_REDIRECTACTION_REDIRECTRESPONSECODE']._serialized_end=687
# @@protoc_insertion_point(module_scope)
