# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from contrib.envoy.extensions.filters.network.sip_proxy.tra.v3alpha import tra_pb2 as contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2


class TraServiceStub(object):
    """[#protodoc-title: Tra]

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Create',
                request_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
                response_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Update',
                request_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
                response_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Retrieve',
                request_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
                response_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Delete',
                request_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
                response_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Subscribe',
                request_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
                response_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
                )


class TraServiceServicer(object):
    """[#protodoc-title: Tra]

    """

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TraServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.FromString,
                    response_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.FromString,
                    response_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.FromString,
                    response_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.FromString,
                    response_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.FromString,
                    response_serializer=contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TraService(object):
    """[#protodoc-title: Tra]

    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Create',
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Update',
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Retrieve',
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Delete',
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/envoy.extensions.filters.network.sip_proxy.tra.v3alpha.TraService/Subscribe',
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceRequest.SerializeToString,
            contrib_dot_envoy_dot_extensions_dot_filters_dot_network_dot_sip__proxy_dot_tra_dot_v3alpha_dot_tra__pb2.TraServiceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
