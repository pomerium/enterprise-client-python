"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import routes_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class RouteServiceStub:
    """RouteService manages proxy route definitions"""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    DeleteRoute: grpc.UnaryUnaryMultiCallable[
        routes_pb2.DeleteRouteRequest,
        routes_pb2.DeleteRouteResponse,
    ]
    """DeleteRoute removes an existing route"""

    DeleteRoutes: grpc.UnaryUnaryMultiCallable[
        routes_pb2.DeleteRoutesRequest,
        routes_pb2.DeleteRoutesResponse,
    ]
    """DeleteRoutes removes existing routes."""

    GetRoute: grpc.UnaryUnaryMultiCallable[
        routes_pb2.GetRouteRequest,
        routes_pb2.GetRouteResponse,
    ]
    """GetRoute retrieves an existing route"""

    ListRoutes: grpc.UnaryUnaryMultiCallable[
        routes_pb2.ListRoutesRequest,
        routes_pb2.ListRoutesResponse,
    ]
    """ListRoutes lists routes based on ListRoutesRequest"""

    LoadRoutes: grpc.UnaryUnaryMultiCallable[
        routes_pb2.LoadRoutesRequest,
        routes_pb2.LoadRoutesResponse,
    ]
    """LoadRoutes imports routes from an existing OSS configuration"""

    SetRoute: grpc.UnaryUnaryMultiCallable[
        routes_pb2.SetRouteRequest,
        routes_pb2.SetRouteResponse,
    ]
    """SetRoute creates or, if id is defined, updates an existing route"""

    SetRoutes: grpc.UnaryUnaryMultiCallable[
        routes_pb2.SetRoutesRequest,
        routes_pb2.SetRoutesResponse,
    ]
    """SetRoutes creates or, if id is defined, updates existing routes"""

    MoveRoutes: grpc.UnaryUnaryMultiCallable[
        routes_pb2.MoveRoutesRequest,
        routes_pb2.MoveRoutesResponse,
    ]
    """MoveRoutes takes an array of routeIds and moves them to a new namespace"""

class RouteServiceAsyncStub:
    """RouteService manages proxy route definitions"""

    DeleteRoute: grpc.aio.UnaryUnaryMultiCallable[
        routes_pb2.DeleteRouteRequest,
        routes_pb2.DeleteRouteResponse,
    ]
    """DeleteRoute removes an existing route"""

    DeleteRoutes: grpc.aio.UnaryUnaryMultiCallable[
        routes_pb2.DeleteRoutesRequest,
        routes_pb2.DeleteRoutesResponse,
    ]
    """DeleteRoutes removes existing routes."""

    GetRoute: grpc.aio.UnaryUnaryMultiCallable[
        routes_pb2.GetRouteRequest,
        routes_pb2.GetRouteResponse,
    ]
    """GetRoute retrieves an existing route"""

    ListRoutes: grpc.aio.UnaryUnaryMultiCallable[
        routes_pb2.ListRoutesRequest,
        routes_pb2.ListRoutesResponse,
    ]
    """ListRoutes lists routes based on ListRoutesRequest"""

    LoadRoutes: grpc.aio.UnaryUnaryMultiCallable[
        routes_pb2.LoadRoutesRequest,
        routes_pb2.LoadRoutesResponse,
    ]
    """LoadRoutes imports routes from an existing OSS configuration"""

    SetRoute: grpc.aio.UnaryUnaryMultiCallable[
        routes_pb2.SetRouteRequest,
        routes_pb2.SetRouteResponse,
    ]
    """SetRoute creates or, if id is defined, updates an existing route"""

    SetRoutes: grpc.aio.UnaryUnaryMultiCallable[
        routes_pb2.SetRoutesRequest,
        routes_pb2.SetRoutesResponse,
    ]
    """SetRoutes creates or, if id is defined, updates existing routes"""

    MoveRoutes: grpc.aio.UnaryUnaryMultiCallable[
        routes_pb2.MoveRoutesRequest,
        routes_pb2.MoveRoutesResponse,
    ]
    """MoveRoutes takes an array of routeIds and moves them to a new namespace"""

class RouteServiceServicer(metaclass=abc.ABCMeta):
    """RouteService manages proxy route definitions"""

    @abc.abstractmethod
    def DeleteRoute(
        self,
        request: routes_pb2.DeleteRouteRequest,
        context: _ServicerContext,
    ) -> typing.Union[routes_pb2.DeleteRouteResponse, collections.abc.Awaitable[routes_pb2.DeleteRouteResponse]]:
        """DeleteRoute removes an existing route"""

    @abc.abstractmethod
    def DeleteRoutes(
        self,
        request: routes_pb2.DeleteRoutesRequest,
        context: _ServicerContext,
    ) -> typing.Union[routes_pb2.DeleteRoutesResponse, collections.abc.Awaitable[routes_pb2.DeleteRoutesResponse]]:
        """DeleteRoutes removes existing routes."""

    @abc.abstractmethod
    def GetRoute(
        self,
        request: routes_pb2.GetRouteRequest,
        context: _ServicerContext,
    ) -> typing.Union[routes_pb2.GetRouteResponse, collections.abc.Awaitable[routes_pb2.GetRouteResponse]]:
        """GetRoute retrieves an existing route"""

    @abc.abstractmethod
    def ListRoutes(
        self,
        request: routes_pb2.ListRoutesRequest,
        context: _ServicerContext,
    ) -> typing.Union[routes_pb2.ListRoutesResponse, collections.abc.Awaitable[routes_pb2.ListRoutesResponse]]:
        """ListRoutes lists routes based on ListRoutesRequest"""

    @abc.abstractmethod
    def LoadRoutes(
        self,
        request: routes_pb2.LoadRoutesRequest,
        context: _ServicerContext,
    ) -> typing.Union[routes_pb2.LoadRoutesResponse, collections.abc.Awaitable[routes_pb2.LoadRoutesResponse]]:
        """LoadRoutes imports routes from an existing OSS configuration"""

    @abc.abstractmethod
    def SetRoute(
        self,
        request: routes_pb2.SetRouteRequest,
        context: _ServicerContext,
    ) -> typing.Union[routes_pb2.SetRouteResponse, collections.abc.Awaitable[routes_pb2.SetRouteResponse]]:
        """SetRoute creates or, if id is defined, updates an existing route"""

    @abc.abstractmethod
    def SetRoutes(
        self,
        request: routes_pb2.SetRoutesRequest,
        context: _ServicerContext,
    ) -> typing.Union[routes_pb2.SetRoutesResponse, collections.abc.Awaitable[routes_pb2.SetRoutesResponse]]:
        """SetRoutes creates or, if id is defined, updates existing routes"""

    @abc.abstractmethod
    def MoveRoutes(
        self,
        request: routes_pb2.MoveRoutesRequest,
        context: _ServicerContext,
    ) -> typing.Union[routes_pb2.MoveRoutesResponse, collections.abc.Awaitable[routes_pb2.MoveRoutesResponse]]:
        """MoveRoutes takes an array of routeIds and moves them to a new namespace"""

def add_RouteServiceServicer_to_server(servicer: RouteServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
