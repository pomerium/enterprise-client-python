"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import policy_pb2
import routes_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class PolicyReportRequest(google.protobuf.message.Message):
    """PolicyReportRequest may either specify a list of routes,
    or request to report all routes of the namespace
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROUTE_IDS_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    namespace_id: builtins.str
    @property
    def route_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        route_ids: collections.abc.Iterable[builtins.str] | None = ...,
        namespace_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["namespace_id", b"namespace_id", "route_ids", b"route_ids"]) -> None: ...

global___PolicyReportRequest = PolicyReportRequest

@typing.final
class PolicyReportResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROUTES_FIELD_NUMBER: builtins.int
    POLICIES_FIELD_NUMBER: builtins.int
    @property
    def routes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[routes_pb2.Route]: ...
    @property
    def policies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[policy_pb2.Policy]: ...
    def __init__(
        self,
        *,
        routes: collections.abc.Iterable[routes_pb2.Route] | None = ...,
        policies: collections.abc.Iterable[policy_pb2.Policy] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["policies", b"policies", "routes", b"routes"]) -> None: ...

global___PolicyReportResponse = PolicyReportResponse
