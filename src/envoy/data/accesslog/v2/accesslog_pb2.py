# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/data/accesslog/v2/accesslog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.api.v2.core import address_pb2 as envoy_dot_api_dot_v2_dot_core_dot_address__pb2
from envoy.api.v2.core import base_pb2 as envoy_dot_api_dot_v2_dot_core_dot_base__pb2
try:
  envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2 = envoy_dot_api_dot_v2_dot_core_dot_base__pb2.envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2
except AttributeError:
  envoy_dot_api_dot_v2_dot_core_dot_socket__option__pb2 = envoy_dot_api_dot_v2_dot_core_dot_base__pb2.envoy.api.v2.core.socket_option_pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'envoy/data/accesslog/v2/accesslog.proto\x12\x17\x65nvoy.data.accesslog.v2\x1a\x1f\x65nvoy/api/v2/core/address.proto\x1a\x1c\x65nvoy/api/v2/core/base.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\xa6\x01\n\x11TCPAccessLogEntry\x12\x43\n\x11\x63ommon_properties\x18\x01 \x01(\x0b\x32(.envoy.data.accesslog.v2.AccessLogCommon\x12L\n\x15\x63onnection_properties\x18\x02 \x01(\x0b\x32-.envoy.data.accesslog.v2.ConnectionProperties\"\x87\x03\n\x12HTTPAccessLogEntry\x12\x43\n\x11\x63ommon_properties\x18\x01 \x01(\x0b\x32(.envoy.data.accesslog.v2.AccessLogCommon\x12Q\n\x10protocol_version\x18\x02 \x01(\x0e\x32\x37.envoy.data.accesslog.v2.HTTPAccessLogEntry.HTTPVersion\x12?\n\x07request\x18\x03 \x01(\x0b\x32..envoy.data.accesslog.v2.HTTPRequestProperties\x12\x41\n\x08response\x18\x04 \x01(\x0b\x32/.envoy.data.accesslog.v2.HTTPResponseProperties\"U\n\x0bHTTPVersion\x12\x18\n\x14PROTOCOL_UNSPECIFIED\x10\x00\x12\n\n\x06HTTP10\x10\x01\x12\n\n\x06HTTP11\x10\x02\x12\t\n\x05HTTP2\x10\x03\x12\t\n\x05HTTP3\x10\x04\"B\n\x14\x43onnectionProperties\x12\x16\n\x0ereceived_bytes\x18\x01 \x01(\x04\x12\x12\n\nsent_bytes\x18\x02 \x01(\x04\"\xb0\n\n\x0f\x41\x63\x63\x65ssLogCommon\x12,\n\x0bsample_rate\x18\x01 \x01(\x01\x42\x17\xfa\x42\x14\x12\x12\x19\x00\x00\x00\x00\x00\x00\xf0?!\x00\x00\x00\x00\x00\x00\x00\x00\x12=\n\x19\x64ownstream_remote_address\x18\x02 \x01(\x0b\x32\x1a.envoy.api.v2.core.Address\x12<\n\x18\x64ownstream_local_address\x18\x03 \x01(\x0b\x32\x1a.envoy.api.v2.core.Address\x12>\n\x0etls_properties\x18\x04 \x01(\x0b\x32&.envoy.data.accesslog.v2.TLSProperties\x12.\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\x14time_to_last_rx_byte\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x41\n\x1etime_to_first_upstream_tx_byte\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12@\n\x1dtime_to_last_upstream_tx_byte\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x41\n\x1etime_to_first_upstream_rx_byte\x18\t \x01(\x0b\x32\x19.google.protobuf.Duration\x12@\n\x1dtime_to_last_upstream_rx_byte\x18\n \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x43\n time_to_first_downstream_tx_byte\x18\x0b \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x42\n\x1ftime_to_last_downstream_tx_byte\x18\x0c \x01(\x0b\x32\x19.google.protobuf.Duration\x12;\n\x17upstream_remote_address\x18\r \x01(\x0b\x32\x1a.envoy.api.v2.core.Address\x12:\n\x16upstream_local_address\x18\x0e \x01(\x0b\x32\x1a.envoy.api.v2.core.Address\x12\x18\n\x10upstream_cluster\x18\x0f \x01(\t\x12>\n\x0eresponse_flags\x18\x10 \x01(\x0b\x32&.envoy.data.accesslog.v2.ResponseFlags\x12-\n\x08metadata\x18\x11 \x01(\x0b\x32\x1b.envoy.api.v2.core.Metadata\x12)\n!upstream_transport_failure_reason\x18\x12 \x01(\t\x12\x12\n\nroute_name\x18\x13 \x01(\t\x12\x44\n downstream_direct_remote_address\x18\x14 \x01(\x0b\x32\x1a.envoy.api.v2.core.Address\x12^\n\x14\x66ilter_state_objects\x18\x15 \x03(\x0b\x32@.envoy.data.accesslog.v2.AccessLogCommon.FilterStateObjectsEntry\x1aO\n\x17\x46ilterStateObjectsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"\xae\x06\n\rResponseFlags\x12 \n\x18\x66\x61iled_local_healthcheck\x18\x01 \x01(\x08\x12\x1b\n\x13no_healthy_upstream\x18\x02 \x01(\x08\x12 \n\x18upstream_request_timeout\x18\x03 \x01(\x08\x12\x13\n\x0blocal_reset\x18\x04 \x01(\x08\x12\x1d\n\x15upstream_remote_reset\x18\x05 \x01(\x08\x12#\n\x1bupstream_connection_failure\x18\x06 \x01(\x08\x12\'\n\x1fupstream_connection_termination\x18\x07 \x01(\x08\x12\x19\n\x11upstream_overflow\x18\x08 \x01(\x08\x12\x16\n\x0eno_route_found\x18\t \x01(\x08\x12\x16\n\x0e\x64\x65lay_injected\x18\n \x01(\x08\x12\x16\n\x0e\x66\x61ult_injected\x18\x0b \x01(\x08\x12\x14\n\x0crate_limited\x18\x0c \x01(\x08\x12Q\n\x14unauthorized_details\x18\r \x01(\x0b\x32\x33.envoy.data.accesslog.v2.ResponseFlags.Unauthorized\x12 \n\x18rate_limit_service_error\x18\x0e \x01(\x08\x12)\n!downstream_connection_termination\x18\x0f \x01(\x08\x12%\n\x1dupstream_retry_limit_exceeded\x18\x10 \x01(\x08\x12\x1b\n\x13stream_idle_timeout\x18\x11 \x01(\x08\x12%\n\x1dinvalid_envoy_request_headers\x18\x12 \x01(\x08\x12!\n\x19\x64ownstream_protocol_error\x18\x13 \x01(\x08\x1a\x92\x01\n\x0cUnauthorized\x12J\n\x06reason\x18\x01 \x01(\x0e\x32:.envoy.data.accesslog.v2.ResponseFlags.Unauthorized.Reason\"6\n\x06Reason\x12\x16\n\x12REASON_UNSPECIFIED\x10\x00\x12\x14\n\x10\x45XTERNAL_SERVICE\x10\x01\"\xaa\x05\n\rTLSProperties\x12\x46\n\x0btls_version\x18\x01 \x01(\x0e\x32\x31.envoy.data.accesslog.v2.TLSProperties.TLSVersion\x12\x36\n\x10tls_cipher_suite\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x18\n\x10tls_sni_hostname\x18\x03 \x01(\t\x12\x62\n\x1clocal_certificate_properties\x18\x04 \x01(\x0b\x32<.envoy.data.accesslog.v2.TLSProperties.CertificateProperties\x12\x61\n\x1bpeer_certificate_properties\x18\x05 \x01(\x0b\x32<.envoy.data.accesslog.v2.TLSProperties.CertificateProperties\x12\x16\n\x0etls_session_id\x18\x06 \x01(\t\x1a\xc6\x01\n\x15\x43\x65rtificateProperties\x12\x65\n\x10subject_alt_name\x18\x01 \x03(\x0b\x32K.envoy.data.accesslog.v2.TLSProperties.CertificateProperties.SubjectAltName\x12\x0f\n\x07subject\x18\x02 \x01(\t\x1a\x35\n\x0eSubjectAltName\x12\r\n\x03uri\x18\x01 \x01(\tH\x00\x12\r\n\x03\x64ns\x18\x02 \x01(\tH\x00\x42\x05\n\x03san\"W\n\nTLSVersion\x12\x17\n\x13VERSION_UNSPECIFIED\x10\x00\x12\t\n\x05TLSv1\x10\x01\x12\x0b\n\x07TLSv1_1\x10\x02\x12\x0b\n\x07TLSv1_2\x10\x03\x12\x0b\n\x07TLSv1_3\x10\x04\"\xee\x03\n\x15HTTPRequestProperties\x12\x42\n\x0erequest_method\x18\x01 \x01(\x0e\x32 .envoy.api.v2.core.RequestMethodB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x0e\n\x06scheme\x18\x02 \x01(\t\x12\x11\n\tauthority\x18\x03 \x01(\t\x12*\n\x04port\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x0c\n\x04path\x18\x05 \x01(\t\x12\x12\n\nuser_agent\x18\x06 \x01(\t\x12\x0f\n\x07referer\x18\x07 \x01(\t\x12\x15\n\rforwarded_for\x18\x08 \x01(\t\x12\x12\n\nrequest_id\x18\t \x01(\t\x12\x15\n\roriginal_path\x18\n \x01(\t\x12\x1d\n\x15request_headers_bytes\x18\x0b \x01(\x04\x12\x1a\n\x12request_body_bytes\x18\x0c \x01(\x04\x12[\n\x0frequest_headers\x18\r \x03(\x0b\x32\x42.envoy.data.accesslog.v2.HTTPRequestProperties.RequestHeadersEntry\x1a\x35\n\x13RequestHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xdc\x03\n\x16HTTPResponseProperties\x12\x33\n\rresponse_code\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12\x1e\n\x16response_headers_bytes\x18\x02 \x01(\x04\x12\x1b\n\x13response_body_bytes\x18\x03 \x01(\x04\x12^\n\x10response_headers\x18\x04 \x03(\x0b\x32\x44.envoy.data.accesslog.v2.HTTPResponseProperties.ResponseHeadersEntry\x12`\n\x11response_trailers\x18\x05 \x03(\x0b\x32\x45.envoy.data.accesslog.v2.HTTPResponseProperties.ResponseTrailersEntry\x12\x1d\n\x15response_code_details\x18\x06 \x01(\t\x1a\x36\n\x14ResponseHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15ResponseTrailersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x8d\x01\n%io.envoyproxy.envoy.data.accesslog.v2B\x0e\x41\x63\x63\x65sslogProtoP\x01ZJgithub.com/envoyproxy/go-control-plane/envoy/data/accesslog/v2;accesslogv2\xba\x80\xc8\xd1\x06\x02\x10\x01\x62\x06proto3')



_TCPACCESSLOGENTRY = DESCRIPTOR.message_types_by_name['TCPAccessLogEntry']
_HTTPACCESSLOGENTRY = DESCRIPTOR.message_types_by_name['HTTPAccessLogEntry']
_CONNECTIONPROPERTIES = DESCRIPTOR.message_types_by_name['ConnectionProperties']
_ACCESSLOGCOMMON = DESCRIPTOR.message_types_by_name['AccessLogCommon']
_ACCESSLOGCOMMON_FILTERSTATEOBJECTSENTRY = _ACCESSLOGCOMMON.nested_types_by_name['FilterStateObjectsEntry']
_RESPONSEFLAGS = DESCRIPTOR.message_types_by_name['ResponseFlags']
_RESPONSEFLAGS_UNAUTHORIZED = _RESPONSEFLAGS.nested_types_by_name['Unauthorized']
_TLSPROPERTIES = DESCRIPTOR.message_types_by_name['TLSProperties']
_TLSPROPERTIES_CERTIFICATEPROPERTIES = _TLSPROPERTIES.nested_types_by_name['CertificateProperties']
_TLSPROPERTIES_CERTIFICATEPROPERTIES_SUBJECTALTNAME = _TLSPROPERTIES_CERTIFICATEPROPERTIES.nested_types_by_name['SubjectAltName']
_HTTPREQUESTPROPERTIES = DESCRIPTOR.message_types_by_name['HTTPRequestProperties']
_HTTPREQUESTPROPERTIES_REQUESTHEADERSENTRY = _HTTPREQUESTPROPERTIES.nested_types_by_name['RequestHeadersEntry']
_HTTPRESPONSEPROPERTIES = DESCRIPTOR.message_types_by_name['HTTPResponseProperties']
_HTTPRESPONSEPROPERTIES_RESPONSEHEADERSENTRY = _HTTPRESPONSEPROPERTIES.nested_types_by_name['ResponseHeadersEntry']
_HTTPRESPONSEPROPERTIES_RESPONSETRAILERSENTRY = _HTTPRESPONSEPROPERTIES.nested_types_by_name['ResponseTrailersEntry']
_HTTPACCESSLOGENTRY_HTTPVERSION = _HTTPACCESSLOGENTRY.enum_types_by_name['HTTPVersion']
_RESPONSEFLAGS_UNAUTHORIZED_REASON = _RESPONSEFLAGS_UNAUTHORIZED.enum_types_by_name['Reason']
_TLSPROPERTIES_TLSVERSION = _TLSPROPERTIES.enum_types_by_name['TLSVersion']
TCPAccessLogEntry = _reflection.GeneratedProtocolMessageType('TCPAccessLogEntry', (_message.Message,), {
  'DESCRIPTOR' : _TCPACCESSLOGENTRY,
  '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.TCPAccessLogEntry)
  })
_sym_db.RegisterMessage(TCPAccessLogEntry)

HTTPAccessLogEntry = _reflection.GeneratedProtocolMessageType('HTTPAccessLogEntry', (_message.Message,), {
  'DESCRIPTOR' : _HTTPACCESSLOGENTRY,
  '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.HTTPAccessLogEntry)
  })
_sym_db.RegisterMessage(HTTPAccessLogEntry)

ConnectionProperties = _reflection.GeneratedProtocolMessageType('ConnectionProperties', (_message.Message,), {
  'DESCRIPTOR' : _CONNECTIONPROPERTIES,
  '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.ConnectionProperties)
  })
_sym_db.RegisterMessage(ConnectionProperties)

AccessLogCommon = _reflection.GeneratedProtocolMessageType('AccessLogCommon', (_message.Message,), {

  'FilterStateObjectsEntry' : _reflection.GeneratedProtocolMessageType('FilterStateObjectsEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACCESSLOGCOMMON_FILTERSTATEOBJECTSENTRY,
    '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
    # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.AccessLogCommon.FilterStateObjectsEntry)
    })
  ,
  'DESCRIPTOR' : _ACCESSLOGCOMMON,
  '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.AccessLogCommon)
  })
_sym_db.RegisterMessage(AccessLogCommon)
_sym_db.RegisterMessage(AccessLogCommon.FilterStateObjectsEntry)

ResponseFlags = _reflection.GeneratedProtocolMessageType('ResponseFlags', (_message.Message,), {

  'Unauthorized' : _reflection.GeneratedProtocolMessageType('Unauthorized', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSEFLAGS_UNAUTHORIZED,
    '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
    # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.ResponseFlags.Unauthorized)
    })
  ,
  'DESCRIPTOR' : _RESPONSEFLAGS,
  '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.ResponseFlags)
  })
_sym_db.RegisterMessage(ResponseFlags)
_sym_db.RegisterMessage(ResponseFlags.Unauthorized)

TLSProperties = _reflection.GeneratedProtocolMessageType('TLSProperties', (_message.Message,), {

  'CertificateProperties' : _reflection.GeneratedProtocolMessageType('CertificateProperties', (_message.Message,), {

    'SubjectAltName' : _reflection.GeneratedProtocolMessageType('SubjectAltName', (_message.Message,), {
      'DESCRIPTOR' : _TLSPROPERTIES_CERTIFICATEPROPERTIES_SUBJECTALTNAME,
      '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
      # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.TLSProperties.CertificateProperties.SubjectAltName)
      })
    ,
    'DESCRIPTOR' : _TLSPROPERTIES_CERTIFICATEPROPERTIES,
    '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
    # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.TLSProperties.CertificateProperties)
    })
  ,
  'DESCRIPTOR' : _TLSPROPERTIES,
  '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.TLSProperties)
  })
_sym_db.RegisterMessage(TLSProperties)
_sym_db.RegisterMessage(TLSProperties.CertificateProperties)
_sym_db.RegisterMessage(TLSProperties.CertificateProperties.SubjectAltName)

HTTPRequestProperties = _reflection.GeneratedProtocolMessageType('HTTPRequestProperties', (_message.Message,), {

  'RequestHeadersEntry' : _reflection.GeneratedProtocolMessageType('RequestHeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _HTTPREQUESTPROPERTIES_REQUESTHEADERSENTRY,
    '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
    # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.HTTPRequestProperties.RequestHeadersEntry)
    })
  ,
  'DESCRIPTOR' : _HTTPREQUESTPROPERTIES,
  '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.HTTPRequestProperties)
  })
_sym_db.RegisterMessage(HTTPRequestProperties)
_sym_db.RegisterMessage(HTTPRequestProperties.RequestHeadersEntry)

HTTPResponseProperties = _reflection.GeneratedProtocolMessageType('HTTPResponseProperties', (_message.Message,), {

  'ResponseHeadersEntry' : _reflection.GeneratedProtocolMessageType('ResponseHeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _HTTPRESPONSEPROPERTIES_RESPONSEHEADERSENTRY,
    '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
    # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.HTTPResponseProperties.ResponseHeadersEntry)
    })
  ,

  'ResponseTrailersEntry' : _reflection.GeneratedProtocolMessageType('ResponseTrailersEntry', (_message.Message,), {
    'DESCRIPTOR' : _HTTPRESPONSEPROPERTIES_RESPONSETRAILERSENTRY,
    '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
    # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.HTTPResponseProperties.ResponseTrailersEntry)
    })
  ,
  'DESCRIPTOR' : _HTTPRESPONSEPROPERTIES,
  '__module__' : 'envoy.data.accesslog.v2.accesslog_pb2'
  # @@protoc_insertion_point(class_scope:envoy.data.accesslog.v2.HTTPResponseProperties)
  })
_sym_db.RegisterMessage(HTTPResponseProperties)
_sym_db.RegisterMessage(HTTPResponseProperties.ResponseHeadersEntry)
_sym_db.RegisterMessage(HTTPResponseProperties.ResponseTrailersEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%io.envoyproxy.envoy.data.accesslog.v2B\016AccesslogProtoP\001ZJgithub.com/envoyproxy/go-control-plane/envoy/data/accesslog/v2;accesslogv2\272\200\310\321\006\002\020\001'
  _ACCESSLOGCOMMON_FILTERSTATEOBJECTSENTRY._options = None
  _ACCESSLOGCOMMON_FILTERSTATEOBJECTSENTRY._serialized_options = b'8\001'
  _ACCESSLOGCOMMON.fields_by_name['sample_rate']._options = None
  _ACCESSLOGCOMMON.fields_by_name['sample_rate']._serialized_options = b'\372B\024\022\022\031\000\000\000\000\000\000\360?!\000\000\000\000\000\000\000\000'
  _HTTPREQUESTPROPERTIES_REQUESTHEADERSENTRY._options = None
  _HTTPREQUESTPROPERTIES_REQUESTHEADERSENTRY._serialized_options = b'8\001'
  _HTTPREQUESTPROPERTIES.fields_by_name['request_method']._options = None
  _HTTPREQUESTPROPERTIES.fields_by_name['request_method']._serialized_options = b'\372B\005\202\001\002\020\001'
  _HTTPRESPONSEPROPERTIES_RESPONSEHEADERSENTRY._options = None
  _HTTPRESPONSEPROPERTIES_RESPONSEHEADERSENTRY._serialized_options = b'8\001'
  _HTTPRESPONSEPROPERTIES_RESPONSETRAILERSENTRY._options = None
  _HTTPRESPONSEPROPERTIES_RESPONSETRAILERSENTRY._serialized_options = b'8\001'
  _TCPACCESSLOGENTRY._serialized_start=312
  _TCPACCESSLOGENTRY._serialized_end=478
  _HTTPACCESSLOGENTRY._serialized_start=481
  _HTTPACCESSLOGENTRY._serialized_end=872
  _HTTPACCESSLOGENTRY_HTTPVERSION._serialized_start=787
  _HTTPACCESSLOGENTRY_HTTPVERSION._serialized_end=872
  _CONNECTIONPROPERTIES._serialized_start=874
  _CONNECTIONPROPERTIES._serialized_end=940
  _ACCESSLOGCOMMON._serialized_start=943
  _ACCESSLOGCOMMON._serialized_end=2271
  _ACCESSLOGCOMMON_FILTERSTATEOBJECTSENTRY._serialized_start=2192
  _ACCESSLOGCOMMON_FILTERSTATEOBJECTSENTRY._serialized_end=2271
  _RESPONSEFLAGS._serialized_start=2274
  _RESPONSEFLAGS._serialized_end=3088
  _RESPONSEFLAGS_UNAUTHORIZED._serialized_start=2942
  _RESPONSEFLAGS_UNAUTHORIZED._serialized_end=3088
  _RESPONSEFLAGS_UNAUTHORIZED_REASON._serialized_start=3034
  _RESPONSEFLAGS_UNAUTHORIZED_REASON._serialized_end=3088
  _TLSPROPERTIES._serialized_start=3091
  _TLSPROPERTIES._serialized_end=3773
  _TLSPROPERTIES_CERTIFICATEPROPERTIES._serialized_start=3486
  _TLSPROPERTIES_CERTIFICATEPROPERTIES._serialized_end=3684
  _TLSPROPERTIES_CERTIFICATEPROPERTIES_SUBJECTALTNAME._serialized_start=3631
  _TLSPROPERTIES_CERTIFICATEPROPERTIES_SUBJECTALTNAME._serialized_end=3684
  _TLSPROPERTIES_TLSVERSION._serialized_start=3686
  _TLSPROPERTIES_TLSVERSION._serialized_end=3773
  _HTTPREQUESTPROPERTIES._serialized_start=3776
  _HTTPREQUESTPROPERTIES._serialized_end=4270
  _HTTPREQUESTPROPERTIES_REQUESTHEADERSENTRY._serialized_start=4217
  _HTTPREQUESTPROPERTIES_REQUESTHEADERSENTRY._serialized_end=4270
  _HTTPRESPONSEPROPERTIES._serialized_start=4273
  _HTTPRESPONSEPROPERTIES._serialized_end=4749
  _HTTPRESPONSEPROPERTIES_RESPONSEHEADERSENTRY._serialized_start=4638
  _HTTPRESPONSEPROPERTIES_RESPONSEHEADERSENTRY._serialized_end=4692
  _HTTPRESPONSEPROPERTIES_RESPONSETRAILERSENTRY._serialized_start=4694
  _HTTPRESPONSEPROPERTIES_RESPONSETRAILERSENTRY._serialized_end=4749
# @@protoc_insertion_point(module_scope)
