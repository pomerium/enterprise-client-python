# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/overload/v3/overload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.type.v3 import percent_pb2 as envoy_dot_type_dot_v3_dot_percent__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'envoy/config/overload/v3/overload.proto\x12\x18\x65nvoy.config.overload.v3\x1a\x1b\x65nvoy/type/v3/percent.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xa9\x01\n\x0fResourceMonitor\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12,\n\x0ctyped_config\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00:4\x9a\xc5\x88\x1e/\n-envoy.config.overload.v2alpha.ResourceMonitorB\r\n\x0b\x63onfig_typeJ\x04\x08\x02\x10\x03R\x06\x63onfig\"q\n\x10ThresholdTrigger\x12&\n\x05value\x18\x01 \x01(\x01\x42\x17\xfa\x42\x14\x12\x12\x19\x00\x00\x00\x00\x00\x00\xf0?)\x00\x00\x00\x00\x00\x00\x00\x00:5\x9a\xc5\x88\x1e\x30\n.envoy.config.overload.v2alpha.ThresholdTrigger\"z\n\rScaledTrigger\x12\x32\n\x11scaling_threshold\x18\x01 \x01(\x01\x42\x17\xfa\x42\x14\x12\x12\x19\x00\x00\x00\x00\x00\x00\xf0?)\x00\x00\x00\x00\x00\x00\x00\x00\x12\x35\n\x14saturation_threshold\x18\x02 \x01(\x01\x42\x17\xfa\x42\x14\x12\x12\x19\x00\x00\x00\x00\x00\x00\xf0?)\x00\x00\x00\x00\x00\x00\x00\x00\"\xe0\x01\n\x07Trigger\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12?\n\tthreshold\x18\x02 \x01(\x0b\x32*.envoy.config.overload.v3.ThresholdTriggerH\x00\x12\x39\n\x06scaled\x18\x03 \x01(\x0b\x32\'.envoy.config.overload.v3.ScaledTriggerH\x00:,\x9a\xc5\x88\x1e\'\n%envoy.config.overload.v2alpha.TriggerB\x14\n\rtrigger_oneof\x12\x03\xf8\x42\x01\"\xf7\x03\n\x1fScaleTimersOverloadActionConfig\x12k\n\x13timer_scale_factors\x18\x01 \x03(\x0b\x32\x44.envoy.config.overload.v3.ScaleTimersOverloadActionConfig.ScaleTimerB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x1a\xe3\x01\n\nScaleTimer\x12^\n\x05timer\x18\x01 \x01(\x0e\x32\x43.envoy.config.overload.v3.ScaleTimersOverloadActionConfig.TimerTypeB\n\xfa\x42\x07\x82\x01\x04\x10\x01 \x00\x12\x30\n\x0bmin_timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationH\x00\x12+\n\tmin_scale\x18\x03 \x01(\x0b\x32\x16.envoy.type.v3.PercentH\x00\x42\x16\n\x0foverload_adjust\x12\x03\xf8\x42\x01\"\x80\x01\n\tTimerType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12#\n\x1fHTTP_DOWNSTREAM_CONNECTION_IDLE\x10\x01\x12\x1f\n\x1bHTTP_DOWNSTREAM_STREAM_IDLE\x10\x02\x12\x1c\n\x18TRANSPORT_SOCKET_CONNECT\x10\x03\"\xc7\x01\n\x0eOverloadAction\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12=\n\x08triggers\x18\x02 \x03(\x0b\x32!.envoy.config.overload.v3.TriggerB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x12*\n\x0ctyped_config\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any:3\x9a\xc5\x88\x1e.\n,envoy.config.overload.v2alpha.OverloadAction\"O\n\x13\x42ufferFactoryConfig\x12\x38\n%minimum_account_to_track_power_of_two\x18\x01 \x01(\rB\t\xfa\x42\x06*\x04\x18\x38(\n\"\xd5\x02\n\x0fOverloadManager\x12\x33\n\x10refresh_interval\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12N\n\x11resource_monitors\x18\x02 \x03(\x0b\x32).envoy.config.overload.v3.ResourceMonitorB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x12\x39\n\x07\x61\x63tions\x18\x03 \x03(\x0b\x32(.envoy.config.overload.v3.OverloadAction\x12L\n\x15\x62uffer_factory_config\x18\x04 \x01(\x0b\x32-.envoy.config.overload.v3.BufferFactoryConfig:4\x9a\xc5\x88\x1e/\n-envoy.config.overload.v2alpha.OverloadManagerB\x8d\x01\n&io.envoyproxy.envoy.config.overload.v3B\rOverloadProtoP\x01ZJgithub.com/envoyproxy/go-control-plane/envoy/config/overload/v3;overloadv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')



_RESOURCEMONITOR = DESCRIPTOR.message_types_by_name['ResourceMonitor']
_THRESHOLDTRIGGER = DESCRIPTOR.message_types_by_name['ThresholdTrigger']
_SCALEDTRIGGER = DESCRIPTOR.message_types_by_name['ScaledTrigger']
_TRIGGER = DESCRIPTOR.message_types_by_name['Trigger']
_SCALETIMERSOVERLOADACTIONCONFIG = DESCRIPTOR.message_types_by_name['ScaleTimersOverloadActionConfig']
_SCALETIMERSOVERLOADACTIONCONFIG_SCALETIMER = _SCALETIMERSOVERLOADACTIONCONFIG.nested_types_by_name['ScaleTimer']
_OVERLOADACTION = DESCRIPTOR.message_types_by_name['OverloadAction']
_BUFFERFACTORYCONFIG = DESCRIPTOR.message_types_by_name['BufferFactoryConfig']
_OVERLOADMANAGER = DESCRIPTOR.message_types_by_name['OverloadManager']
_SCALETIMERSOVERLOADACTIONCONFIG_TIMERTYPE = _SCALETIMERSOVERLOADACTIONCONFIG.enum_types_by_name['TimerType']
ResourceMonitor = _reflection.GeneratedProtocolMessageType('ResourceMonitor', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEMONITOR,
  '__module__' : 'envoy.config.overload.v3.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v3.ResourceMonitor)
  })
_sym_db.RegisterMessage(ResourceMonitor)

ThresholdTrigger = _reflection.GeneratedProtocolMessageType('ThresholdTrigger', (_message.Message,), {
  'DESCRIPTOR' : _THRESHOLDTRIGGER,
  '__module__' : 'envoy.config.overload.v3.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v3.ThresholdTrigger)
  })
_sym_db.RegisterMessage(ThresholdTrigger)

ScaledTrigger = _reflection.GeneratedProtocolMessageType('ScaledTrigger', (_message.Message,), {
  'DESCRIPTOR' : _SCALEDTRIGGER,
  '__module__' : 'envoy.config.overload.v3.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v3.ScaledTrigger)
  })
_sym_db.RegisterMessage(ScaledTrigger)

Trigger = _reflection.GeneratedProtocolMessageType('Trigger', (_message.Message,), {
  'DESCRIPTOR' : _TRIGGER,
  '__module__' : 'envoy.config.overload.v3.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v3.Trigger)
  })
_sym_db.RegisterMessage(Trigger)

ScaleTimersOverloadActionConfig = _reflection.GeneratedProtocolMessageType('ScaleTimersOverloadActionConfig', (_message.Message,), {

  'ScaleTimer' : _reflection.GeneratedProtocolMessageType('ScaleTimer', (_message.Message,), {
    'DESCRIPTOR' : _SCALETIMERSOVERLOADACTIONCONFIG_SCALETIMER,
    '__module__' : 'envoy.config.overload.v3.overload_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.overload.v3.ScaleTimersOverloadActionConfig.ScaleTimer)
    })
  ,
  'DESCRIPTOR' : _SCALETIMERSOVERLOADACTIONCONFIG,
  '__module__' : 'envoy.config.overload.v3.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v3.ScaleTimersOverloadActionConfig)
  })
_sym_db.RegisterMessage(ScaleTimersOverloadActionConfig)
_sym_db.RegisterMessage(ScaleTimersOverloadActionConfig.ScaleTimer)

OverloadAction = _reflection.GeneratedProtocolMessageType('OverloadAction', (_message.Message,), {
  'DESCRIPTOR' : _OVERLOADACTION,
  '__module__' : 'envoy.config.overload.v3.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v3.OverloadAction)
  })
_sym_db.RegisterMessage(OverloadAction)

BufferFactoryConfig = _reflection.GeneratedProtocolMessageType('BufferFactoryConfig', (_message.Message,), {
  'DESCRIPTOR' : _BUFFERFACTORYCONFIG,
  '__module__' : 'envoy.config.overload.v3.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v3.BufferFactoryConfig)
  })
_sym_db.RegisterMessage(BufferFactoryConfig)

OverloadManager = _reflection.GeneratedProtocolMessageType('OverloadManager', (_message.Message,), {
  'DESCRIPTOR' : _OVERLOADMANAGER,
  '__module__' : 'envoy.config.overload.v3.overload_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.overload.v3.OverloadManager)
  })
_sym_db.RegisterMessage(OverloadManager)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&io.envoyproxy.envoy.config.overload.v3B\rOverloadProtoP\001ZJgithub.com/envoyproxy/go-control-plane/envoy/config/overload/v3;overloadv3\272\200\310\321\006\002\020\002'
  _RESOURCEMONITOR.fields_by_name['name']._options = None
  _RESOURCEMONITOR.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _RESOURCEMONITOR._options = None
  _RESOURCEMONITOR._serialized_options = b'\232\305\210\036/\n-envoy.config.overload.v2alpha.ResourceMonitor'
  _THRESHOLDTRIGGER.fields_by_name['value']._options = None
  _THRESHOLDTRIGGER.fields_by_name['value']._serialized_options = b'\372B\024\022\022\031\000\000\000\000\000\000\360?)\000\000\000\000\000\000\000\000'
  _THRESHOLDTRIGGER._options = None
  _THRESHOLDTRIGGER._serialized_options = b'\232\305\210\0360\n.envoy.config.overload.v2alpha.ThresholdTrigger'
  _SCALEDTRIGGER.fields_by_name['scaling_threshold']._options = None
  _SCALEDTRIGGER.fields_by_name['scaling_threshold']._serialized_options = b'\372B\024\022\022\031\000\000\000\000\000\000\360?)\000\000\000\000\000\000\000\000'
  _SCALEDTRIGGER.fields_by_name['saturation_threshold']._options = None
  _SCALEDTRIGGER.fields_by_name['saturation_threshold']._serialized_options = b'\372B\024\022\022\031\000\000\000\000\000\000\360?)\000\000\000\000\000\000\000\000'
  _TRIGGER.oneofs_by_name['trigger_oneof']._options = None
  _TRIGGER.oneofs_by_name['trigger_oneof']._serialized_options = b'\370B\001'
  _TRIGGER.fields_by_name['name']._options = None
  _TRIGGER.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _TRIGGER._options = None
  _TRIGGER._serialized_options = b'\232\305\210\036\'\n%envoy.config.overload.v2alpha.Trigger'
  _SCALETIMERSOVERLOADACTIONCONFIG_SCALETIMER.oneofs_by_name['overload_adjust']._options = None
  _SCALETIMERSOVERLOADACTIONCONFIG_SCALETIMER.oneofs_by_name['overload_adjust']._serialized_options = b'\370B\001'
  _SCALETIMERSOVERLOADACTIONCONFIG_SCALETIMER.fields_by_name['timer']._options = None
  _SCALETIMERSOVERLOADACTIONCONFIG_SCALETIMER.fields_by_name['timer']._serialized_options = b'\372B\007\202\001\004\020\001 \000'
  _SCALETIMERSOVERLOADACTIONCONFIG.fields_by_name['timer_scale_factors']._options = None
  _SCALETIMERSOVERLOADACTIONCONFIG.fields_by_name['timer_scale_factors']._serialized_options = b'\372B\005\222\001\002\010\001'
  _OVERLOADACTION.fields_by_name['name']._options = None
  _OVERLOADACTION.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _OVERLOADACTION.fields_by_name['triggers']._options = None
  _OVERLOADACTION.fields_by_name['triggers']._serialized_options = b'\372B\005\222\001\002\010\001'
  _OVERLOADACTION._options = None
  _OVERLOADACTION._serialized_options = b'\232\305\210\036.\n,envoy.config.overload.v2alpha.OverloadAction'
  _BUFFERFACTORYCONFIG.fields_by_name['minimum_account_to_track_power_of_two']._options = None
  _BUFFERFACTORYCONFIG.fields_by_name['minimum_account_to_track_power_of_two']._serialized_options = b'\372B\006*\004\0308(\n'
  _OVERLOADMANAGER.fields_by_name['resource_monitors']._options = None
  _OVERLOADMANAGER.fields_by_name['resource_monitors']._serialized_options = b'\372B\005\222\001\002\010\001'
  _OVERLOADMANAGER._options = None
  _OVERLOADMANAGER._serialized_options = b'\232\305\210\036/\n-envoy.config.overload.v2alpha.OverloadManager'
  _RESOURCEMONITOR._serialized_start=249
  _RESOURCEMONITOR._serialized_end=418
  _THRESHOLDTRIGGER._serialized_start=420
  _THRESHOLDTRIGGER._serialized_end=533
  _SCALEDTRIGGER._serialized_start=535
  _SCALEDTRIGGER._serialized_end=657
  _TRIGGER._serialized_start=660
  _TRIGGER._serialized_end=884
  _SCALETIMERSOVERLOADACTIONCONFIG._serialized_start=887
  _SCALETIMERSOVERLOADACTIONCONFIG._serialized_end=1390
  _SCALETIMERSOVERLOADACTIONCONFIG_SCALETIMER._serialized_start=1032
  _SCALETIMERSOVERLOADACTIONCONFIG_SCALETIMER._serialized_end=1259
  _SCALETIMERSOVERLOADACTIONCONFIG_TIMERTYPE._serialized_start=1262
  _SCALETIMERSOVERLOADACTIONCONFIG_TIMERTYPE._serialized_end=1390
  _OVERLOADACTION._serialized_start=1393
  _OVERLOADACTION._serialized_end=1592
  _BUFFERFACTORYCONFIG._serialized_start=1594
  _BUFFERFACTORYCONFIG._serialized_end=1673
  _OVERLOADMANAGER._serialized_start=1676
  _OVERLOADMANAGER._serialized_end=2017
# @@protoc_insertion_point(module_scope)
