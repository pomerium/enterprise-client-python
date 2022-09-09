"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import key_chain_pb2

class KeyChainServiceStub:
    """KeyChainService manages and store TLS Certificates, Keys and CAs, known as
    Key Pairs
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    DeleteKeyPair: grpc.UnaryUnaryMultiCallable[
        key_chain_pb2.DeleteKeyPairRequest,
        key_chain_pb2.DeleteKeyPairResponse,
    ]
    """DeleteKeyPair remove an x509 key pair based on a DeleteKeyPairRequest"""
    GetKeyPair: grpc.UnaryUnaryMultiCallable[
        key_chain_pb2.GetKeyPairRequest,
        key_chain_pb2.GetKeyPairResponse,
    ]
    """GetKeyPair retrieves an existing key pair"""
    ListKeyPairs: grpc.UnaryUnaryMultiCallable[
        key_chain_pb2.ListKeyPairsRequest,
        key_chain_pb2.ListKeyPairsResponse,
    ]
    """ListKeyPairs lists existing key pairs based on parameters in
    ListKeyPairsRequest
    """
    CreateKeyPair: grpc.UnaryUnaryMultiCallable[
        key_chain_pb2.CreateKeyPairRequest,
        key_chain_pb2.CreateKeyPairResponse,
    ]
    """CreateKeyPair creates a new key pair"""
    UpdateKeyPair: grpc.UnaryUnaryMultiCallable[
        key_chain_pb2.UpdateKeyPairRequest,
        key_chain_pb2.UpdateKeyPairResponse,
    ]
    """CreateKeyPair creates a new key pair"""

class KeyChainServiceServicer(metaclass=abc.ABCMeta):
    """KeyChainService manages and store TLS Certificates, Keys and CAs, known as
    Key Pairs
    """

    @abc.abstractmethod
    def DeleteKeyPair(
        self,
        request: key_chain_pb2.DeleteKeyPairRequest,
        context: grpc.ServicerContext,
    ) -> key_chain_pb2.DeleteKeyPairResponse:
        """DeleteKeyPair remove an x509 key pair based on a DeleteKeyPairRequest"""
    @abc.abstractmethod
    def GetKeyPair(
        self,
        request: key_chain_pb2.GetKeyPairRequest,
        context: grpc.ServicerContext,
    ) -> key_chain_pb2.GetKeyPairResponse:
        """GetKeyPair retrieves an existing key pair"""
    @abc.abstractmethod
    def ListKeyPairs(
        self,
        request: key_chain_pb2.ListKeyPairsRequest,
        context: grpc.ServicerContext,
    ) -> key_chain_pb2.ListKeyPairsResponse:
        """ListKeyPairs lists existing key pairs based on parameters in
        ListKeyPairsRequest
        """
    @abc.abstractmethod
    def CreateKeyPair(
        self,
        request: key_chain_pb2.CreateKeyPairRequest,
        context: grpc.ServicerContext,
    ) -> key_chain_pb2.CreateKeyPairResponse:
        """CreateKeyPair creates a new key pair"""
    @abc.abstractmethod
    def UpdateKeyPair(
        self,
        request: key_chain_pb2.UpdateKeyPairRequest,
        context: grpc.ServicerContext,
    ) -> key_chain_pb2.UpdateKeyPairResponse:
        """CreateKeyPair creates a new key pair"""

def add_KeyChainServiceServicer_to_server(servicer: KeyChainServiceServicer, server: grpc.Server) -> None: ...
