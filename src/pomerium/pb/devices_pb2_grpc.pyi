"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import devices_pb2
import google.protobuf.empty_pb2
import grpc
import grpc.aio
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class DeviceServiceStub:
    """DeviceService manages device credentials, enrollments and types"""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    ApproveDevice: grpc.UnaryUnaryMultiCallable[
        devices_pb2.ApproveDeviceRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    CreateDeviceEnrollment: grpc.UnaryUnaryMultiCallable[
        devices_pb2.CreateDeviceEnrollmentRequest,
        devices_pb2.CreateDeviceEnrollmentResponse,
    ]

    SetDeviceType: grpc.UnaryUnaryMultiCallable[
        devices_pb2.SetDeviceTypeRequest,
        devices_pb2.SetDeviceTypeResponse,
    ]

    DeleteDevice: grpc.UnaryUnaryMultiCallable[
        devices_pb2.DeleteDeviceRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    DeleteDeviceType: grpc.UnaryUnaryMultiCallable[
        devices_pb2.DeleteDeviceTypeRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    ListDevices: grpc.UnaryUnaryMultiCallable[
        devices_pb2.ListDevicesRequest,
        devices_pb2.ListDevicesResponse,
    ]

    ListDeviceTypes: grpc.UnaryUnaryMultiCallable[
        devices_pb2.ListDeviceTypesRequest,
        devices_pb2.ListDeviceTypesResponse,
    ]

class DeviceServiceAsyncStub:
    """DeviceService manages device credentials, enrollments and types"""

    ApproveDevice: grpc.aio.UnaryUnaryMultiCallable[
        devices_pb2.ApproveDeviceRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    CreateDeviceEnrollment: grpc.aio.UnaryUnaryMultiCallable[
        devices_pb2.CreateDeviceEnrollmentRequest,
        devices_pb2.CreateDeviceEnrollmentResponse,
    ]

    SetDeviceType: grpc.aio.UnaryUnaryMultiCallable[
        devices_pb2.SetDeviceTypeRequest,
        devices_pb2.SetDeviceTypeResponse,
    ]

    DeleteDevice: grpc.aio.UnaryUnaryMultiCallable[
        devices_pb2.DeleteDeviceRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    DeleteDeviceType: grpc.aio.UnaryUnaryMultiCallable[
        devices_pb2.DeleteDeviceTypeRequest,
        google.protobuf.empty_pb2.Empty,
    ]

    ListDevices: grpc.aio.UnaryUnaryMultiCallable[
        devices_pb2.ListDevicesRequest,
        devices_pb2.ListDevicesResponse,
    ]

    ListDeviceTypes: grpc.aio.UnaryUnaryMultiCallable[
        devices_pb2.ListDeviceTypesRequest,
        devices_pb2.ListDeviceTypesResponse,
    ]

class DeviceServiceServicer(metaclass=abc.ABCMeta):
    """DeviceService manages device credentials, enrollments and types"""

    @abc.abstractmethod
    def ApproveDevice(
        self,
        request: devices_pb2.ApproveDeviceRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def CreateDeviceEnrollment(
        self,
        request: devices_pb2.CreateDeviceEnrollmentRequest,
        context: _ServicerContext,
    ) -> typing.Union[devices_pb2.CreateDeviceEnrollmentResponse, collections.abc.Awaitable[devices_pb2.CreateDeviceEnrollmentResponse]]: ...

    @abc.abstractmethod
    def SetDeviceType(
        self,
        request: devices_pb2.SetDeviceTypeRequest,
        context: _ServicerContext,
    ) -> typing.Union[devices_pb2.SetDeviceTypeResponse, collections.abc.Awaitable[devices_pb2.SetDeviceTypeResponse]]: ...

    @abc.abstractmethod
    def DeleteDevice(
        self,
        request: devices_pb2.DeleteDeviceRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def DeleteDeviceType(
        self,
        request: devices_pb2.DeleteDeviceTypeRequest,
        context: _ServicerContext,
    ) -> typing.Union[google.protobuf.empty_pb2.Empty, collections.abc.Awaitable[google.protobuf.empty_pb2.Empty]]: ...

    @abc.abstractmethod
    def ListDevices(
        self,
        request: devices_pb2.ListDevicesRequest,
        context: _ServicerContext,
    ) -> typing.Union[devices_pb2.ListDevicesResponse, collections.abc.Awaitable[devices_pb2.ListDevicesResponse]]: ...

    @abc.abstractmethod
    def ListDeviceTypes(
        self,
        request: devices_pb2.ListDeviceTypesRequest,
        context: _ServicerContext,
    ) -> typing.Union[devices_pb2.ListDeviceTypesResponse, collections.abc.Awaitable[devices_pb2.ListDeviceTypesResponse]]: ...

def add_DeviceServiceServicer_to_server(servicer: DeviceServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
