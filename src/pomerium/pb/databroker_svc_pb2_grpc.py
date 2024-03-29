# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pomerium.pb.databroker_svc_pb2 as databroker__svc__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class DataBrokerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListDataBrokerRecords = channel.unary_unary(
                '/pomerium.dashboard.DataBroker/ListDataBrokerRecords',
                request_serializer=databroker__svc__pb2.ListDataBrokerRecordsRequest.SerializeToString,
                response_deserializer=databroker__svc__pb2.ListDataBrokerRecordsResponse.FromString,
                )
        self.ListDataBrokerRecordTypes = channel.unary_unary(
                '/pomerium.dashboard.DataBroker/ListDataBrokerRecordTypes',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=databroker__svc__pb2.ListDataBrokerRecordTypesResponse.FromString,
                )


class DataBrokerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListDataBrokerRecords(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDataBrokerRecordTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataBrokerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListDataBrokerRecords': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDataBrokerRecords,
                    request_deserializer=databroker__svc__pb2.ListDataBrokerRecordsRequest.FromString,
                    response_serializer=databroker__svc__pb2.ListDataBrokerRecordsResponse.SerializeToString,
            ),
            'ListDataBrokerRecordTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.ListDataBrokerRecordTypes,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=databroker__svc__pb2.ListDataBrokerRecordTypesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pomerium.dashboard.DataBroker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataBroker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListDataBrokerRecords(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.DataBroker/ListDataBrokerRecords',
            databroker__svc__pb2.ListDataBrokerRecordsRequest.SerializeToString,
            databroker__svc__pb2.ListDataBrokerRecordsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDataBrokerRecordTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pomerium.dashboard.DataBroker/ListDataBrokerRecordTypes',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            databroker__svc__pb2.ListDataBrokerRecordTypesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
