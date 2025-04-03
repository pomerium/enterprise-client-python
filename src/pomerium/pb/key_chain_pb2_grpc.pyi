"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import key_chain_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class KeyChainServiceStub:
    """KeyChainService manages and store TLS Certificates, Keys and CAs, known as
    Key Pairs
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
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

class KeyChainServiceAsyncStub:
    """KeyChainService manages and store TLS Certificates, Keys and CAs, known as
    Key Pairs
    """

    DeleteKeyPair: grpc.aio.UnaryUnaryMultiCallable[
        key_chain_pb2.DeleteKeyPairRequest,
        key_chain_pb2.DeleteKeyPairResponse,
    ]
    """DeleteKeyPair remove an x509 key pair based on a DeleteKeyPairRequest"""

    GetKeyPair: grpc.aio.UnaryUnaryMultiCallable[
        key_chain_pb2.GetKeyPairRequest,
        key_chain_pb2.GetKeyPairResponse,
    ]
    """GetKeyPair retrieves an existing key pair"""

    ListKeyPairs: grpc.aio.UnaryUnaryMultiCallable[
        key_chain_pb2.ListKeyPairsRequest,
        key_chain_pb2.ListKeyPairsResponse,
    ]
    """ListKeyPairs lists existing key pairs based on parameters in
    ListKeyPairsRequest
    """

    CreateKeyPair: grpc.aio.UnaryUnaryMultiCallable[
        key_chain_pb2.CreateKeyPairRequest,
        key_chain_pb2.CreateKeyPairResponse,
    ]
    """CreateKeyPair creates a new key pair"""

    UpdateKeyPair: grpc.aio.UnaryUnaryMultiCallable[
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
        context: _ServicerContext,
    ) -> typing.Union[key_chain_pb2.DeleteKeyPairResponse, collections.abc.Awaitable[key_chain_pb2.DeleteKeyPairResponse]]:
        """DeleteKeyPair remove an x509 key pair based on a DeleteKeyPairRequest"""

    @abc.abstractmethod
    def GetKeyPair(
        self,
        request: key_chain_pb2.GetKeyPairRequest,
        context: _ServicerContext,
    ) -> typing.Union[key_chain_pb2.GetKeyPairResponse, collections.abc.Awaitable[key_chain_pb2.GetKeyPairResponse]]:
        """GetKeyPair retrieves an existing key pair"""

    @abc.abstractmethod
    def ListKeyPairs(
        self,
        request: key_chain_pb2.ListKeyPairsRequest,
        context: _ServicerContext,
    ) -> typing.Union[key_chain_pb2.ListKeyPairsResponse, collections.abc.Awaitable[key_chain_pb2.ListKeyPairsResponse]]:
        """ListKeyPairs lists existing key pairs based on parameters in
        ListKeyPairsRequest
        """

    @abc.abstractmethod
    def CreateKeyPair(
        self,
        request: key_chain_pb2.CreateKeyPairRequest,
        context: _ServicerContext,
    ) -> typing.Union[key_chain_pb2.CreateKeyPairResponse, collections.abc.Awaitable[key_chain_pb2.CreateKeyPairResponse]]:
        """CreateKeyPair creates a new key pair"""

    @abc.abstractmethod
    def UpdateKeyPair(
        self,
        request: key_chain_pb2.UpdateKeyPairRequest,
        context: _ServicerContext,
    ) -> typing.Union[key_chain_pb2.UpdateKeyPairResponse, collections.abc.Awaitable[key_chain_pb2.UpdateKeyPairResponse]]:
        """CreateKeyPair creates a new key pair"""

def add_KeyChainServiceServicer_to_server(servicer: KeyChainServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
