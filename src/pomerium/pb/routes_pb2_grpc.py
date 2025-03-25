# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pomerium.pb.routes_pb2 as routes__pb2


class RouteServiceStub(object):
    """RouteService manages proxy route definitions
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DeleteRoute = channel.unary_unary(
                '/pomerium.dashboard.RouteService/DeleteRoute',
                request_serializer=routes__pb2.DeleteRouteRequest.SerializeToString,
                response_deserializer=routes__pb2.DeleteRouteResponse.FromString,
                )
        self.DeleteRoutes = channel.unary_unary(
                '/pomerium.dashboard.RouteService/DeleteRoutes',
                request_serializer=routes__pb2.DeleteRoutesRequest.SerializeToString,
                response_deserializer=routes__pb2.DeleteRoutesResponse.FromString,
                )
        self.GetRoute = channel.unary_unary(
                '/pomerium.dashboard.RouteService/GetRoute',
                request_serializer=routes__pb2.GetRouteRequest.SerializeToString,
                response_deserializer=routes__pb2.GetRouteResponse.FromString,
                )
        self.ListRoutes = channel.unary_unary(
                '/pomerium.dashboard.RouteService/ListRoutes',
                request_serializer=routes__pb2.ListRoutesRequest.SerializeToString,
                response_deserializer=routes__pb2.ListRoutesResponse.FromString,
                )
        self.LoadRoutes = channel.unary_unary(
                '/pomerium.dashboard.RouteService/LoadRoutes',
                request_serializer=routes__pb2.LoadRoutesRequest.SerializeToString,
                response_deserializer=routes__pb2.LoadRoutesResponse.FromString,
                )
        self.SetRoute = channel.unary_unary(
                '/pomerium.dashboard.RouteService/SetRoute',
                request_serializer=routes__pb2.SetRouteRequest.SerializeToString,
                response_deserializer=routes__pb2.SetRouteResponse.FromString,
                )
        self.SetRoutes = channel.unary_unary(
                '/pomerium.dashboard.RouteService/SetRoutes',
                request_serializer=routes__pb2.SetRoutesRequest.SerializeToString,
                response_deserializer=routes__pb2.SetRoutesResponse.FromString,
                )
        self.MoveRoutes = channel.unary_unary(
                '/pomerium.dashboard.RouteService/MoveRoutes',
                request_serializer=routes__pb2.MoveRoutesRequest.SerializeToString,
                response_deserializer=routes__pb2.MoveRoutesResponse.FromString,
                )


class RouteServiceServicer(object):
    """RouteService manages proxy route definitions
    """

    def DeleteRoute(self, request, context):
        """DeleteRoute removes an existing route
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRoutes(self, request, context):
        """DeleteRoutes removes existing routes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRoute(self, request, context):
        """GetRoute retrieves an existing route
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRoutes(self, request, context):
        """ListRoutes lists routes based on ListRoutesRequest
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadRoutes(self, request, context):
        """LoadRoutes imports routes from an existing OSS configuration
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetRoute(self, request, context):
        """SetRoute creates or, if id is defined, updates an existing route
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetRoutes(self, request, context):
        """SetRoutes creates or, if id is defined, updates existing routes
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MoveRoutes(self, request, context):
        """MoveRoutes takes an array of routeIds and moves them to a new namespace
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RouteServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DeleteRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRoute,
                    request_deserializer=routes__pb2.DeleteRouteRequest.FromString,
                    response_serializer=routes__pb2.DeleteRouteResponse.SerializeToString,
            ),
            'DeleteRoutes': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRoutes,
                    request_deserializer=routes__pb2.DeleteRoutesRequest.FromString,
                    response_serializer=routes__pb2.DeleteRoutesResponse.SerializeToString,
            ),
            'GetRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRoute,
                    request_deserializer=routes__pb2.GetRouteRequest.FromString,
                    response_serializer=routes__pb2.GetRouteResponse.SerializeToString,
            ),
            'ListRoutes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRoutes,
                    request_deserializer=routes__pb2.ListRoutesRequest.FromString,
                    response_serializer=routes__pb2.ListRoutesResponse.SerializeToString,
            ),
            'LoadRoutes': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadRoutes,
                    request_deserializer=routes__pb2.LoadRoutesRequest.FromString,
                    response_serializer=routes__pb2.LoadRoutesResponse.SerializeToString,
            ),
            'SetRoute': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRoute,
                    request_deserializer=routes__pb2.SetRouteRequest.FromString,
                    response_serializer=routes__pb2.SetRouteResponse.SerializeToString,
            ),
            'SetRoutes': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRoutes,
                    request_deserializer=routes__pb2.SetRoutesRequest.FromString,
                    response_serializer=routes__pb2.SetRoutesResponse.SerializeToString,
            ),
            'MoveRoutes': grpc.unary_unary_rpc_method_handler(
                    servicer.MoveRoutes,
                    request_deserializer=routes__pb2.MoveRoutesRequest.FromString,
                    response_serializer=routes__pb2.MoveRoutesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pomerium.dashboard.RouteService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RouteService(object):
    """RouteService manages proxy route definitions
    """

    @staticmethod
    def DeleteRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.RouteService/DeleteRoute',
            routes__pb2.DeleteRouteRequest.SerializeToString,
            routes__pb2.DeleteRouteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRoutes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.RouteService/DeleteRoutes',
            routes__pb2.DeleteRoutesRequest.SerializeToString,
            routes__pb2.DeleteRoutesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.RouteService/GetRoute',
            routes__pb2.GetRouteRequest.SerializeToString,
            routes__pb2.GetRouteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRoutes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.RouteService/ListRoutes',
            routes__pb2.ListRoutesRequest.SerializeToString,
            routes__pb2.ListRoutesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadRoutes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.RouteService/LoadRoutes',
            routes__pb2.LoadRoutesRequest.SerializeToString,
            routes__pb2.LoadRoutesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetRoute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.RouteService/SetRoute',
            routes__pb2.SetRouteRequest.SerializeToString,
            routes__pb2.SetRouteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetRoutes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.RouteService/SetRoutes',
            routes__pb2.SetRoutesRequest.SerializeToString,
            routes__pb2.SetRoutesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MoveRoutes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.RouteService/MoveRoutes',
            routes__pb2.MoveRoutesRequest.SerializeToString,
            routes__pb2.MoveRoutesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
