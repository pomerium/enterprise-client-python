# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xds/service/orca/v3/orca.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xds.data.orca.v3 import orca_load_report_pb2 as xds_dot_data_dot_orca_dot_v3_dot_orca__load__report__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='xds/service/orca/v3/orca.proto',
  package='xds.service.orca.v3',
  syntax='proto3',
  serialized_options=b'\n\036com.github.xds.service.orca.v3B\tOrcaProtoP\001Z*github.com/cncf/xds/go/xds/service/orca/v3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1exds/service/orca/v3/orca.proto\x12\x13xds.service.orca.v3\x1a\'xds/data/orca/v3/orca_load_report.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17validate/validate.proto\"g\n\x15OrcaLoadReportRequest\x12\x32\n\x0freport_interval\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1a\n\x12request_cost_names\x18\x02 \x03(\t2u\n\x0eOpenRcaService\x12\x63\n\x11StreamCoreMetrics\x12*.xds.service.orca.v3.OrcaLoadReportRequest\x1a .xds.data.orca.v3.OrcaLoadReport0\x01\x42Y\n\x1e\x63om.github.xds.service.orca.v3B\tOrcaProtoP\x01Z*github.com/cncf/xds/go/xds/service/orca/v3b\x06proto3'
  ,
  dependencies=[xds_dot_data_dot_orca_dot_v3_dot_orca__load__report__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_ORCALOADREPORTREQUEST = _descriptor.Descriptor(
  name='OrcaLoadReportRequest',
  full_name='xds.service.orca.v3.OrcaLoadReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='report_interval', full_name='xds.service.orca.v3.OrcaLoadReportRequest.report_interval', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_cost_names', full_name='xds.service.orca.v3.OrcaLoadReportRequest.request_cost_names', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=153,
  serialized_end=256,
)

_ORCALOADREPORTREQUEST.fields_by_name['report_interval'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['OrcaLoadReportRequest'] = _ORCALOADREPORTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrcaLoadReportRequest = _reflection.GeneratedProtocolMessageType('OrcaLoadReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORCALOADREPORTREQUEST,
  '__module__' : 'xds.service.orca.v3.orca_pb2'
  # @@protoc_insertion_point(class_scope:xds.service.orca.v3.OrcaLoadReportRequest)
  })
_sym_db.RegisterMessage(OrcaLoadReportRequest)


DESCRIPTOR._options = None

_OPENRCASERVICE = _descriptor.ServiceDescriptor(
  name='OpenRcaService',
  full_name='xds.service.orca.v3.OpenRcaService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=258,
  serialized_end=375,
  methods=[
  _descriptor.MethodDescriptor(
    name='StreamCoreMetrics',
    full_name='xds.service.orca.v3.OpenRcaService.StreamCoreMetrics',
    index=0,
    containing_service=None,
    input_type=_ORCALOADREPORTREQUEST,
    output_type=xds_dot_data_dot_orca_dot_v3_dot_orca__load__report__pb2._ORCALOADREPORT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_OPENRCASERVICE)

DESCRIPTOR.services_by_name['OpenRcaService'] = _OPENRCASERVICE

# @@protoc_insertion_point(module_scope)
