# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import pomerium.pb.settings_pb2 as settings__pb2

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
        + f' but the generated code in settings_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class SettingsServiceStub(object):
    """SettingsService manages global pomerium settings
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSettings = channel.unary_unary(
                '/pomerium.dashboard.SettingsService/GetSettings',
                request_serializer=settings__pb2.GetSettingsRequest.SerializeToString,
                response_deserializer=settings__pb2.GetSettingsResponse.FromString,
                _registered_method=True)
        self.SetSettings = channel.unary_unary(
                '/pomerium.dashboard.SettingsService/SetSettings',
                request_serializer=settings__pb2.SetSettingsRequest.SerializeToString,
                response_deserializer=settings__pb2.SetSettingsResponse.FromString,
                _registered_method=True)
        self.GetBrandingSettings = channel.unary_unary(
                '/pomerium.dashboard.SettingsService/GetBrandingSettings',
                request_serializer=settings__pb2.GetSettingsRequest.SerializeToString,
                response_deserializer=settings__pb2.GetSettingsResponse.FromString,
                _registered_method=True)
        self.GetConsoleSettings = channel.unary_unary(
                '/pomerium.dashboard.SettingsService/GetConsoleSettings',
                request_serializer=settings__pb2.GetConsoleSettingsRequest.SerializeToString,
                response_deserializer=settings__pb2.GetConsoleSettingsResponse.FromString,
                _registered_method=True)


class SettingsServiceServicer(object):
    """SettingsService manages global pomerium settings
    """

    def GetSettings(self, request, context):
        """GetSettings retrieves the currently applied settings
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetSettings(self, request, context):
        """SetSettings applies new global settings
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBrandingSettings(self, request, context):
        """GetBrandingSettings retrieves just the branding part of the settings
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConsoleSettings(self, request, context):
        """GetConsoleSettings retrieves the console settings.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SettingsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSettings,
                    request_deserializer=settings__pb2.GetSettingsRequest.FromString,
                    response_serializer=settings__pb2.GetSettingsResponse.SerializeToString,
            ),
            'SetSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.SetSettings,
                    request_deserializer=settings__pb2.SetSettingsRequest.FromString,
                    response_serializer=settings__pb2.SetSettingsResponse.SerializeToString,
            ),
            'GetBrandingSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBrandingSettings,
                    request_deserializer=settings__pb2.GetSettingsRequest.FromString,
                    response_serializer=settings__pb2.GetSettingsResponse.SerializeToString,
            ),
            'GetConsoleSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConsoleSettings,
                    request_deserializer=settings__pb2.GetConsoleSettingsRequest.FromString,
                    response_serializer=settings__pb2.GetConsoleSettingsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pomerium.dashboard.SettingsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('pomerium.dashboard.SettingsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class SettingsService(object):
    """SettingsService manages global pomerium settings
    """

    @staticmethod
    def GetSettings(request,
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
            '/pomerium.dashboard.SettingsService/GetSettings',
            settings__pb2.GetSettingsRequest.SerializeToString,
            settings__pb2.GetSettingsResponse.FromString,
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
    def SetSettings(request,
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
            '/pomerium.dashboard.SettingsService/SetSettings',
            settings__pb2.SetSettingsRequest.SerializeToString,
            settings__pb2.SetSettingsResponse.FromString,
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
    def GetBrandingSettings(request,
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
            '/pomerium.dashboard.SettingsService/GetBrandingSettings',
            settings__pb2.GetSettingsRequest.SerializeToString,
            settings__pb2.GetSettingsResponse.FromString,
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
    def GetConsoleSettings(request,
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
            '/pomerium.dashboard.SettingsService/GetConsoleSettings',
            settings__pb2.GetConsoleSettingsRequest.SerializeToString,
            settings__pb2.GetConsoleSettingsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
