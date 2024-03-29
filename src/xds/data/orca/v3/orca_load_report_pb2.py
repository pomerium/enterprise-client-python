# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xds/data/orca/v3/orca_load_report.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'xds/data/orca/v3/orca_load_report.proto\x12\x10xds.data.orca.v3\x1a\x17validate/validate.proto\"\xac\x03\n\x0eOrcaLoadReport\x12\x35\n\x0f\x63pu_utilization\x18\x01 \x01(\x01\x42\x1c\xfa\x42\x0b\x12\t)\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x42\x0b\x12\t\x19\x00\x00\x00\x00\x00\x00\xf0?\x12\x35\n\x0fmem_utilization\x18\x02 \x01(\x01\x42\x1c\xfa\x42\x0b\x12\t)\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x42\x0b\x12\t\x19\x00\x00\x00\x00\x00\x00\xf0?\x12\x0b\n\x03rps\x18\x03 \x01(\x04\x12G\n\x0crequest_cost\x18\x04 \x03(\x0b\x32\x31.xds.data.orca.v3.OrcaLoadReport.RequestCostEntry\x12n\n\x0butilization\x18\x05 \x03(\x0b\x32\x31.xds.data.orca.v3.OrcaLoadReport.UtilizationEntryB&\xfa\x42\x10\x9a\x01\r*\x0b\x12\t)\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x42\x10\x9a\x01\r*\x0b\x12\t\x19\x00\x00\x00\x00\x00\x00\xf0?\x1a\x32\n\x10RequestCostEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a\x32\n\x10UtilizationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x42]\n\x1b\x63om.github.xds.data.orca.v3B\x13OrcaLoadReportProtoP\x01Z\'github.com/cncf/xds/go/xds/data/orca/v3b\x06proto3')



_ORCALOADREPORT = DESCRIPTOR.message_types_by_name['OrcaLoadReport']
_ORCALOADREPORT_REQUESTCOSTENTRY = _ORCALOADREPORT.nested_types_by_name['RequestCostEntry']
_ORCALOADREPORT_UTILIZATIONENTRY = _ORCALOADREPORT.nested_types_by_name['UtilizationEntry']
OrcaLoadReport = _reflection.GeneratedProtocolMessageType('OrcaLoadReport', (_message.Message,), {

  'RequestCostEntry' : _reflection.GeneratedProtocolMessageType('RequestCostEntry', (_message.Message,), {
    'DESCRIPTOR' : _ORCALOADREPORT_REQUESTCOSTENTRY,
    '__module__' : 'xds.data.orca.v3.orca_load_report_pb2'
    # @@protoc_insertion_point(class_scope:xds.data.orca.v3.OrcaLoadReport.RequestCostEntry)
    })
  ,

  'UtilizationEntry' : _reflection.GeneratedProtocolMessageType('UtilizationEntry', (_message.Message,), {
    'DESCRIPTOR' : _ORCALOADREPORT_UTILIZATIONENTRY,
    '__module__' : 'xds.data.orca.v3.orca_load_report_pb2'
    # @@protoc_insertion_point(class_scope:xds.data.orca.v3.OrcaLoadReport.UtilizationEntry)
    })
  ,
  'DESCRIPTOR' : _ORCALOADREPORT,
  '__module__' : 'xds.data.orca.v3.orca_load_report_pb2'
  # @@protoc_insertion_point(class_scope:xds.data.orca.v3.OrcaLoadReport)
  })
_sym_db.RegisterMessage(OrcaLoadReport)
_sym_db.RegisterMessage(OrcaLoadReport.RequestCostEntry)
_sym_db.RegisterMessage(OrcaLoadReport.UtilizationEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.github.xds.data.orca.v3B\023OrcaLoadReportProtoP\001Z\'github.com/cncf/xds/go/xds/data/orca/v3'
  _ORCALOADREPORT_REQUESTCOSTENTRY._options = None
  _ORCALOADREPORT_REQUESTCOSTENTRY._serialized_options = b'8\001'
  _ORCALOADREPORT_UTILIZATIONENTRY._options = None
  _ORCALOADREPORT_UTILIZATIONENTRY._serialized_options = b'8\001'
  _ORCALOADREPORT.fields_by_name['cpu_utilization']._options = None
  _ORCALOADREPORT.fields_by_name['cpu_utilization']._serialized_options = b'\372B\013\022\t)\000\000\000\000\000\000\000\000\372B\013\022\t\031\000\000\000\000\000\000\360?'
  _ORCALOADREPORT.fields_by_name['mem_utilization']._options = None
  _ORCALOADREPORT.fields_by_name['mem_utilization']._serialized_options = b'\372B\013\022\t)\000\000\000\000\000\000\000\000\372B\013\022\t\031\000\000\000\000\000\000\360?'
  _ORCALOADREPORT.fields_by_name['utilization']._options = None
  _ORCALOADREPORT.fields_by_name['utilization']._serialized_options = b'\372B\020\232\001\r*\013\022\t)\000\000\000\000\000\000\000\000\372B\020\232\001\r*\013\022\t\031\000\000\000\000\000\000\360?'
  _ORCALOADREPORT._serialized_start=87
  _ORCALOADREPORT._serialized_end=515
  _ORCALOADREPORT_REQUESTCOSTENTRY._serialized_start=413
  _ORCALOADREPORT_REQUESTCOSTENTRY._serialized_end=463
  _ORCALOADREPORT_UTILIZATIONENTRY._serialized_start=465
  _ORCALOADREPORT_UTILIZATIONENTRY._serialized_end=515
# @@protoc_insertion_point(module_scope)
