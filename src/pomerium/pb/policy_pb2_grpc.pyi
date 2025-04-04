"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import policy_pb2
import typing

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class PolicyServiceStub:
    """PolicyService manages policy creation and definition"""

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    DeletePolicy: grpc.UnaryUnaryMultiCallable[
        policy_pb2.DeletePolicyRequest,
        policy_pb2.DeletePolicyResponse,
    ]
    """DeletePolicy deletes an existing policy"""

    GetPolicy: grpc.UnaryUnaryMultiCallable[
        policy_pb2.GetPolicyRequest,
        policy_pb2.GetPolicyResponse,
    ]
    """GetPolicy retrieves an existing policy"""

    ListPolicies: grpc.UnaryUnaryMultiCallable[
        policy_pb2.ListPoliciesRequest,
        policy_pb2.ListPoliciesResponse,
    ]
    """ListPolicies lists existing policies based on the ListPoliciesRequest
    parameters
    """

    SetPolicy: grpc.UnaryUnaryMultiCallable[
        policy_pb2.SetPolicyRequest,
        policy_pb2.SetPolicyResponse,
    ]
    """SetPolicy creates a new policy or, if the id is specified, updates an
    existing policy
    """

class PolicyServiceAsyncStub:
    """PolicyService manages policy creation and definition"""

    DeletePolicy: grpc.aio.UnaryUnaryMultiCallable[
        policy_pb2.DeletePolicyRequest,
        policy_pb2.DeletePolicyResponse,
    ]
    """DeletePolicy deletes an existing policy"""

    GetPolicy: grpc.aio.UnaryUnaryMultiCallable[
        policy_pb2.GetPolicyRequest,
        policy_pb2.GetPolicyResponse,
    ]
    """GetPolicy retrieves an existing policy"""

    ListPolicies: grpc.aio.UnaryUnaryMultiCallable[
        policy_pb2.ListPoliciesRequest,
        policy_pb2.ListPoliciesResponse,
    ]
    """ListPolicies lists existing policies based on the ListPoliciesRequest
    parameters
    """

    SetPolicy: grpc.aio.UnaryUnaryMultiCallable[
        policy_pb2.SetPolicyRequest,
        policy_pb2.SetPolicyResponse,
    ]
    """SetPolicy creates a new policy or, if the id is specified, updates an
    existing policy
    """

class PolicyServiceServicer(metaclass=abc.ABCMeta):
    """PolicyService manages policy creation and definition"""

    @abc.abstractmethod
    def DeletePolicy(
        self,
        request: policy_pb2.DeletePolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[policy_pb2.DeletePolicyResponse, collections.abc.Awaitable[policy_pb2.DeletePolicyResponse]]:
        """DeletePolicy deletes an existing policy"""

    @abc.abstractmethod
    def GetPolicy(
        self,
        request: policy_pb2.GetPolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[policy_pb2.GetPolicyResponse, collections.abc.Awaitable[policy_pb2.GetPolicyResponse]]:
        """GetPolicy retrieves an existing policy"""

    @abc.abstractmethod
    def ListPolicies(
        self,
        request: policy_pb2.ListPoliciesRequest,
        context: _ServicerContext,
    ) -> typing.Union[policy_pb2.ListPoliciesResponse, collections.abc.Awaitable[policy_pb2.ListPoliciesResponse]]:
        """ListPolicies lists existing policies based on the ListPoliciesRequest
        parameters
        """

    @abc.abstractmethod
    def SetPolicy(
        self,
        request: policy_pb2.SetPolicyRequest,
        context: _ServicerContext,
    ) -> typing.Union[policy_pb2.SetPolicyResponse, collections.abc.Awaitable[policy_pb2.SetPolicyResponse]]:
        """SetPolicy creates a new policy or, if the id is specified, updates an
        existing policy
        """

def add_PolicyServiceServicer_to_server(servicer: PolicyServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
