# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: settings.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.duration_pb2
import google.protobuf.timestamp_pb2
import settings_pb2


class SettingsServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetSettings(self, stream: 'grpclib.server.Stream[settings_pb2.GetSettingsRequest, settings_pb2.GetSettingsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SetSettings(self, stream: 'grpclib.server.Stream[settings_pb2.SetSettingsRequest, settings_pb2.SetSettingsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/pomerium.dashboard.SettingsService/GetSettings': grpclib.const.Handler(
                self.GetSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                settings_pb2.GetSettingsRequest,
                settings_pb2.GetSettingsResponse,
            ),
            '/pomerium.dashboard.SettingsService/SetSettings': grpclib.const.Handler(
                self.SetSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                settings_pb2.SetSettingsRequest,
                settings_pb2.SetSettingsResponse,
            ),
        }


class SettingsServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/pomerium.dashboard.SettingsService/GetSettings',
            settings_pb2.GetSettingsRequest,
            settings_pb2.GetSettingsResponse,
        )
        self.SetSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/pomerium.dashboard.SettingsService/SetSettings',
            settings_pb2.SetSettingsRequest,
            settings_pb2.SetSettingsResponse,
        )
