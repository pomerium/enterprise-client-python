# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/access_loggers/wasm/v3/wasm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.extensions.wasm.v3 import wasm_pb2 as envoy_dot_extensions_dot_wasm_dot_v3_dot_wasm__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2envoy/extensions/access_loggers/wasm/v3/wasm.proto\x12\'envoy.extensions.access_loggers.wasm.v3\x1a#envoy/extensions/wasm/v3/wasm.proto\x1a\x1dudpa/annotations/status.proto\"G\n\rWasmAccessLog\x12\x36\n\x06\x63onfig\x18\x01 \x01(\x0b\x32&.envoy.extensions.wasm.v3.PluginConfigB\xa3\x01\n5io.envoyproxy.envoy.extensions.access_loggers.wasm.v3B\tWasmProtoP\x01ZUgithub.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/wasm/v3;wasmv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_WASMACCESSLOG = DESCRIPTOR.message_types_by_name['WasmAccessLog']
WasmAccessLog = _reflection.GeneratedProtocolMessageType('WasmAccessLog', (_message.Message,), {
  'DESCRIPTOR' : _WASMACCESSLOG,
  '__module__' : 'envoy.extensions.access_loggers.wasm.v3.wasm_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.access_loggers.wasm.v3.WasmAccessLog)
  })
_sym_db.RegisterMessage(WasmAccessLog)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n5io.envoyproxy.envoy.extensions.access_loggers.wasm.v3B\tWasmProtoP\001ZUgithub.com/envoyproxy/go-control-plane/envoy/extensions/access_loggers/wasm/v3;wasmv3\272\200\310\321\006\002\020\002'
  _WASMACCESSLOG._serialized_start=163
  _WASMACCESSLOG._serialized_end=234
# @@protoc_insertion_point(module_scope)