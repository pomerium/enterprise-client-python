# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/admin/v3/mutex_stats.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n envoy/admin/v3/mutex_stats.proto\x12\x0e\x65nvoy.admin.v3\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"\x87\x01\n\nMutexStats\x12\x17\n\x0fnum_contentions\x18\x01 \x01(\x04\x12\x1b\n\x13\x63urrent_wait_cycles\x18\x02 \x01(\x04\x12\x1c\n\x14lifetime_wait_cycles\x18\x03 \x01(\x04:%\x9a\xc5\x88\x1e \n\x1e\x65nvoy.admin.v2alpha.MutexStatsBx\n\x1cio.envoyproxy.envoy.admin.v3B\x0fMutexStatsProtoP\x01Z=github.com/envoyproxy/go-control-plane/envoy/admin/v3;adminv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_MUTEXSTATS = DESCRIPTOR.message_types_by_name['MutexStats']
MutexStats = _reflection.GeneratedProtocolMessageType('MutexStats', (_message.Message,), {
  'DESCRIPTOR' : _MUTEXSTATS,
  '__module__' : 'envoy.admin.v3.mutex_stats_pb2'
  # @@protoc_insertion_point(class_scope:envoy.admin.v3.MutexStats)
  })
_sym_db.RegisterMessage(MutexStats)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034io.envoyproxy.envoy.admin.v3B\017MutexStatsProtoP\001Z=github.com/envoyproxy/go-control-plane/envoy/admin/v3;adminv3\272\200\310\321\006\002\020\002'
  _MUTEXSTATS._options = None
  _MUTEXSTATS._serialized_options = b'\232\305\210\036 \n\036envoy.admin.v2alpha.MutexStats'
  _MUTEXSTATS._serialized_start=119
  _MUTEXSTATS._serialized_end=254
# @@protoc_insertion_point(module_scope)