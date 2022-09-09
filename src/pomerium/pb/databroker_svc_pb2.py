# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: databroker_svc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.pomerium.pomerium.pkg.grpc.databroker import databroker_pb2 as github_dot_com_dot_pomerium_dot_pomerium_dot_pkg_dot_grpc_dot_databroker_dot_databroker__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x64\x61tabroker_svc.proto\x12\x12pomerium.dashboard\x1a\x41github.com/pomerium/pomerium/pkg/grpc/databroker/databroker.proto\x1a\x1bgoogle/protobuf/empty.proto\"3\n\x1cListDataBrokerRecordsRequest\x12\x13\n\x0brecord_type\x18\x01 \x01(\t\"D\n\x1dListDataBrokerRecordsResponse\x12#\n\x07records\x18\x01 \x03(\x0b\x32\x12.databroker.Record\"9\n!ListDataBrokerRecordTypesResponse\x12\x14\n\x0crecord_types\x18\x01 \x03(\t2\xf6\x01\n\nDataBroker\x12|\n\x15ListDataBrokerRecords\x12\x30.pomerium.dashboard.ListDataBrokerRecordsRequest\x1a\x31.pomerium.dashboard.ListDataBrokerRecordsResponse\x12j\n\x19ListDataBrokerRecordTypes\x12\x16.google.protobuf.Empty\x1a\x35.pomerium.dashboard.ListDataBrokerRecordTypesResponseB-Z+github.com/pomerium/pomerium-console/pkg/pbb\x06proto3')



_LISTDATABROKERRECORDSREQUEST = DESCRIPTOR.message_types_by_name['ListDataBrokerRecordsRequest']
_LISTDATABROKERRECORDSRESPONSE = DESCRIPTOR.message_types_by_name['ListDataBrokerRecordsResponse']
_LISTDATABROKERRECORDTYPESRESPONSE = DESCRIPTOR.message_types_by_name['ListDataBrokerRecordTypesResponse']
ListDataBrokerRecordsRequest = _reflection.GeneratedProtocolMessageType('ListDataBrokerRecordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATABROKERRECORDSREQUEST,
  '__module__' : 'databroker_svc_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListDataBrokerRecordsRequest)
  })
_sym_db.RegisterMessage(ListDataBrokerRecordsRequest)

ListDataBrokerRecordsResponse = _reflection.GeneratedProtocolMessageType('ListDataBrokerRecordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATABROKERRECORDSRESPONSE,
  '__module__' : 'databroker_svc_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListDataBrokerRecordsResponse)
  })
_sym_db.RegisterMessage(ListDataBrokerRecordsResponse)

ListDataBrokerRecordTypesResponse = _reflection.GeneratedProtocolMessageType('ListDataBrokerRecordTypesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATABROKERRECORDTYPESRESPONSE,
  '__module__' : 'databroker_svc_pb2'
  # @@protoc_insertion_point(class_scope:pomerium.dashboard.ListDataBrokerRecordTypesResponse)
  })
_sym_db.RegisterMessage(ListDataBrokerRecordTypesResponse)

_DATABROKER = DESCRIPTOR.services_by_name['DataBroker']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z+github.com/pomerium/pomerium-console/pkg/pb'
  _LISTDATABROKERRECORDSREQUEST._serialized_start=140
  _LISTDATABROKERRECORDSREQUEST._serialized_end=191
  _LISTDATABROKERRECORDSRESPONSE._serialized_start=193
  _LISTDATABROKERRECORDSRESPONSE._serialized_end=261
  _LISTDATABROKERRECORDTYPESRESPONSE._serialized_start=263
  _LISTDATABROKERRECORDTYPESRESPONSE._serialized_end=320
  _DATABROKER._serialized_start=323
  _DATABROKER._serialized_end=569
# @@protoc_insertion_point(module_scope)
