# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: activity_log.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.timestamp_pb2
import activity_log_pb2


class ActivityLogServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetActivityLogEntry(self, stream: 'grpclib.server.Stream[activity_log_pb2.GetActivityLogEntryRequest, activity_log_pb2.GetActivityLogEntryResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListActivityLogEntries(self, stream: 'grpclib.server.Stream[activity_log_pb2.ListActivityLogEntriesRequest, activity_log_pb2.ListActivityLogEntriesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/pomerium.dashboard.ActivityLogService/GetActivityLogEntry': grpclib.const.Handler(
                self.GetActivityLogEntry,
                grpclib.const.Cardinality.UNARY_UNARY,
                activity_log_pb2.GetActivityLogEntryRequest,
                activity_log_pb2.GetActivityLogEntryResponse,
            ),
            '/pomerium.dashboard.ActivityLogService/ListActivityLogEntries': grpclib.const.Handler(
                self.ListActivityLogEntries,
                grpclib.const.Cardinality.UNARY_UNARY,
                activity_log_pb2.ListActivityLogEntriesRequest,
                activity_log_pb2.ListActivityLogEntriesResponse,
            ),
        }


class ActivityLogServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetActivityLogEntry = grpclib.client.UnaryUnaryMethod(
            channel,
            '/pomerium.dashboard.ActivityLogService/GetActivityLogEntry',
            activity_log_pb2.GetActivityLogEntryRequest,
            activity_log_pb2.GetActivityLogEntryResponse,
        )
        self.ListActivityLogEntries = grpclib.client.UnaryUnaryMethod(
            channel,
            '/pomerium.dashboard.ActivityLogService/ListActivityLogEntries',
            activity_log_pb2.ListActivityLogEntriesRequest,
            activity_log_pb2.ListActivityLogEntriesResponse,
        )
