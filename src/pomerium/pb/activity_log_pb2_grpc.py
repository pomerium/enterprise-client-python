# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import pomerium.pb.activity_log_pb2 as activity__log__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in activity_log_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ActivityLogServiceStub(object):
    """ActivityLogService tracks historical changes to configuration made through
    Pomerium Enterprise
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetActivityLogEntry = channel.unary_unary(
                '/pomerium.dashboard.ActivityLogService/GetActivityLogEntry',
                request_serializer=activity__log__pb2.GetActivityLogEntryRequest.SerializeToString,
                response_deserializer=activity__log__pb2.GetActivityLogEntryResponse.FromString,
                _registered_method=True)
        self.ListActivityLogEntries = channel.unary_unary(
                '/pomerium.dashboard.ActivityLogService/ListActivityLogEntries',
                request_serializer=activity__log__pb2.ListActivityLogEntriesRequest.SerializeToString,
                response_deserializer=activity__log__pb2.ListActivityLogEntriesResponse.FromString,
                _registered_method=True)


class ActivityLogServiceServicer(object):
    """ActivityLogService tracks historical changes to configuration made through
    Pomerium Enterprise
    """

    def GetActivityLogEntry(self, request, context):
        """GetActivityLogEntry retrieves a specific activity log entry
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListActivityLogEntries(self, request, context):
        """ListActivityLogEntries lists activity log entries based on paramters in the
        ListActivityLogEntriesRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ActivityLogServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetActivityLogEntry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetActivityLogEntry,
                    request_deserializer=activity__log__pb2.GetActivityLogEntryRequest.FromString,
                    response_serializer=activity__log__pb2.GetActivityLogEntryResponse.SerializeToString,
            ),
            'ListActivityLogEntries': grpc.unary_unary_rpc_method_handler(
                    servicer.ListActivityLogEntries,
                    request_deserializer=activity__log__pb2.ListActivityLogEntriesRequest.FromString,
                    response_serializer=activity__log__pb2.ListActivityLogEntriesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pomerium.dashboard.ActivityLogService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pomerium.dashboard.ActivityLogService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ActivityLogService(object):
    """ActivityLogService tracks historical changes to configuration made through
    Pomerium Enterprise
    """

    @staticmethod
    def GetActivityLogEntry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pomerium.dashboard.ActivityLogService/GetActivityLogEntry',
            activity__log__pb2.GetActivityLogEntryRequest.SerializeToString,
            activity__log__pb2.GetActivityLogEntryResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListActivityLogEntries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/pomerium.dashboard.ActivityLogService/ListActivityLogEntries',
            activity__log__pb2.ListActivityLogEntriesRequest.SerializeToString,
            activity__log__pb2.ListActivityLogEntriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
