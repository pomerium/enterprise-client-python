# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/load_balancing_policies/ring_hash/v3/ring_hash.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEenvoy/extensions/load_balancing_policies/ring_hash/v3/ring_hash.proto\x12\x35\x65nvoy.extensions.load_balancing_policies.ring_hash.v3\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xab\x03\n\x08RingHash\x12m\n\rhash_function\x18\x01 \x01(\x0e\x32L.envoy.extensions.load_balancing_policies.ring_hash.v3.RingHash.HashFunctionB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x43\n\x11minimum_ring_size\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\n\xfa\x42\x07\x32\x05\x18\x80\x80\x80\x04\x12\x43\n\x11maximum_ring_size\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\n\xfa\x42\x07\x32\x05\x18\x80\x80\x80\x04\x12 \n\x18use_hostname_for_hashing\x18\x04 \x01(\x08\x12\x42\n\x13hash_balance_factor\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x07\xfa\x42\x04*\x02(d\"@\n\x0cHashFunction\x12\x10\n\x0c\x44\x45\x46\x41ULT_HASH\x10\x00\x12\x0b\n\x07XX_HASH\x10\x01\x12\x11\n\rMURMUR_HASH_2\x10\x02\x42\xc8\x01\nCio.envoyproxy.envoy.extensions.load_balancing_policies.ring_hash.v3B\rRingHashProtoP\x01Zhgithub.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/ring_hash/v3;ring_hashv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_RINGHASH = DESCRIPTOR.message_types_by_name['RingHash']
_RINGHASH_HASHFUNCTION = _RINGHASH.enum_types_by_name['HashFunction']
RingHash = _reflection.GeneratedProtocolMessageType('RingHash', (_message.Message,), {
  'DESCRIPTOR' : _RINGHASH,
  '__module__' : 'envoy.extensions.load_balancing_policies.ring_hash.v3.ring_hash_pb2'
  # @@protoc_insertion_point(class_scope:envoy.extensions.load_balancing_policies.ring_hash.v3.RingHash)
  })
_sym_db.RegisterMessage(RingHash)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\nCio.envoyproxy.envoy.extensions.load_balancing_policies.ring_hash.v3B\rRingHashProtoP\001Zhgithub.com/envoyproxy/go-control-plane/envoy/extensions/load_balancing_policies/ring_hash/v3;ring_hashv3\272\200\310\321\006\002\020\002'
  _RINGHASH.fields_by_name['hash_function']._options = None
  _RINGHASH.fields_by_name['hash_function']._serialized_options = b'\372B\005\202\001\002\020\001'
  _RINGHASH.fields_by_name['minimum_ring_size']._options = None
  _RINGHASH.fields_by_name['minimum_ring_size']._serialized_options = b'\372B\0072\005\030\200\200\200\004'
  _RINGHASH.fields_by_name['maximum_ring_size']._options = None
  _RINGHASH.fields_by_name['maximum_ring_size']._serialized_options = b'\372B\0072\005\030\200\200\200\004'
  _RINGHASH.fields_by_name['hash_balance_factor']._options = None
  _RINGHASH.fields_by_name['hash_balance_factor']._serialized_options = b'\372B\004*\002(d'
  _RINGHASH._serialized_start=217
  _RINGHASH._serialized_end=644
  _RINGHASH_HASHFUNCTION._serialized_start=580
  _RINGHASH_HASHFUNCTION._serialized_end=644
# @@protoc_insertion_point(module_scope)
