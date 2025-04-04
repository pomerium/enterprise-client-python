"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
adapted from :
https://github.com/envoyproxy/envoy/blob/main/api/envoy/config/core/v3/health_check.proto
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import types_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class HealthCheck(google.protobuf.message.Message):
    """[#next-free-field: 27]"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Payload(google.protobuf.message.Message):
        """Describes the encoding of the payload bytes in the payload."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TEXT_FIELD_NUMBER: builtins.int
        BINARY_FIELD_NUMBER: builtins.int
        text: builtins.str
        """Hex encoded payload. E.g., "000000FF"."""
        binary: builtins.bytes
        """Binary payload."""
        def __init__(
            self,
            *,
            text: builtins.str = ...,
            binary: builtins.bytes = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["binary", b"binary", "payload", b"payload", "text", b"text"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["binary", b"binary", "payload", b"payload", "text", b"text"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["payload", b"payload"]) -> typing.Literal["text", "binary"] | None: ...

    @typing.final
    class HttpHealthCheck(google.protobuf.message.Message):
        """[#next-free-field: 15]"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        HOST_FIELD_NUMBER: builtins.int
        PATH_FIELD_NUMBER: builtins.int
        EXPECTED_STATUSES_FIELD_NUMBER: builtins.int
        RETRIABLE_STATUSES_FIELD_NUMBER: builtins.int
        CODEC_CLIENT_TYPE_FIELD_NUMBER: builtins.int
        host: builtins.str
        """The value of the host header in the HTTP health check request. If
        left empty (default value), the name of the cluster this health check is
        associated with will be used. The host header can be customized for a
        specific endpoint by setting the :ref:`hostname
        <envoy_v3_api_field_config.endpoint.v3.Endpoint.HealthCheckConfig.hostname>`
        field.
        """
        path: builtins.str
        """Specifies the HTTP path that will be requested during health checking.
        For example
        ``/healthcheck``.
        """
        codec_client_type: types_pb2.CodecClientType.ValueType
        """Use specified application protocol for health checks."""
        @property
        def expected_statuses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[types_pb2.Int64Range]:
            """Specifies a list of HTTP response statuses considered healthy. If
            provided, replaces default 200-only policy - 200 must be included
            explicitly as needed. Ranges follow half-open semantics of
            :ref:`Int64Range <envoy_v3_api_msg_type.v3.Int64Range>`. The start and
            end of each range are required. Only statuses in the range [100, 600) are
            allowed.
            """

        @property
        def retriable_statuses(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[types_pb2.Int64Range]:
            """Specifies a list of HTTP response statuses considered retriable. If
            provided, responses in this range will count towards the configured
            :ref:`unhealthy_threshold
            <envoy_v3_api_field_config.core.v3.HealthCheck.unhealthy_threshold>`, but
            will not result in the host being considered immediately unhealthy.
            Ranges follow half-open semantics of :ref:`Int64Range
            <envoy_v3_api_msg_type.v3.Int64Range>`. The start and end of each range
            are required. Only statuses in the range [100, 600) are allowed. The
            :ref:`expected_statuses
            <envoy_v3_api_field_config.core.v3.HealthCheck.HttpHealthCheck.expected_statuses>`
            field takes precedence for any range overlaps with this field i.e. if
            status code 200 is both retriable and expected, a 200 response will be
            considered a successful health check. By default all responses not in
            :ref:`expected_statuses
            <envoy_v3_api_field_config.core.v3.HealthCheck.HttpHealthCheck.expected_statuses>`
            will result in the host being considered immediately unhealthy i.e. if
            status code 200 is expected and there are no configured retriable
            statuses, any non-200 response will result in the host being marked
            unhealthy.
            """

        def __init__(
            self,
            *,
            host: builtins.str = ...,
            path: builtins.str = ...,
            expected_statuses: collections.abc.Iterable[types_pb2.Int64Range] | None = ...,
            retriable_statuses: collections.abc.Iterable[types_pb2.Int64Range] | None = ...,
            codec_client_type: types_pb2.CodecClientType.ValueType = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["codec_client_type", b"codec_client_type", "expected_statuses", b"expected_statuses", "host", b"host", "path", b"path", "retriable_statuses", b"retriable_statuses"]) -> None: ...

    @typing.final
    class TcpHealthCheck(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SEND_FIELD_NUMBER: builtins.int
        RECEIVE_FIELD_NUMBER: builtins.int
        @property
        def send(self) -> global___HealthCheck.Payload:
            """Empty payloads imply a connect-only health check."""

        @property
        def receive(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___HealthCheck.Payload]:
            """When checking the response, “fuzzy” matching is performed such that each
            payload block must be found, and in the order specified, but not
            necessarily contiguous.
            """

        def __init__(
            self,
            *,
            send: global___HealthCheck.Payload | None = ...,
            receive: collections.abc.Iterable[global___HealthCheck.Payload] | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["send", b"send"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["receive", b"receive", "send", b"send"]) -> None: ...

    @typing.final
    class GrpcHealthCheck(google.protobuf.message.Message):
        """`grpc.health.v1.Health
        <https://github.com/grpc/grpc/blob/master/src/proto/grpc/health/v1/health.proto>`_-based
        healthcheck. See `gRPC doc
        <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>`_ for
        details.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SERVICE_NAME_FIELD_NUMBER: builtins.int
        AUTHORITY_FIELD_NUMBER: builtins.int
        service_name: builtins.str
        """An optional service name parameter which will be sent to gRPC service in
        `grpc.health.v1.HealthCheckRequest
        <https://github.com/grpc/grpc/blob/master/src/proto/grpc/health/v1/health.proto#L20>`_.
        message. See `gRPC health-checking overview
        <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>`_ for
        more information.
        """
        authority: builtins.str
        """The value of the :authority header in the gRPC health check request. If
        left empty (default value), the name of the cluster this health check is
        associated with will be used. The authority header can be customized for
        a specific endpoint by setting the :ref:`hostname
        <envoy_v3_api_field_config.endpoint.v3.Endpoint.HealthCheckConfig.hostname>`
        field.
        """
        def __init__(
            self,
            *,
            service_name: builtins.str = ...,
            authority: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["authority", b"authority", "service_name", b"service_name"]) -> None: ...

    TIMEOUT_FIELD_NUMBER: builtins.int
    INTERVAL_FIELD_NUMBER: builtins.int
    INITIAL_JITTER_FIELD_NUMBER: builtins.int
    INTERVAL_JITTER_FIELD_NUMBER: builtins.int
    INTERVAL_JITTER_PERCENT_FIELD_NUMBER: builtins.int
    UNHEALTHY_THRESHOLD_FIELD_NUMBER: builtins.int
    HEALTHY_THRESHOLD_FIELD_NUMBER: builtins.int
    HTTP_HEALTH_CHECK_FIELD_NUMBER: builtins.int
    TCP_HEALTH_CHECK_FIELD_NUMBER: builtins.int
    GRPC_HEALTH_CHECK_FIELD_NUMBER: builtins.int
    interval_jitter_percent: builtins.int
    """An optional jitter amount as a percentage of interval_ms. If specified,
    during every interval Envoy will add ``interval_ms`` *
    ``interval_jitter_percent`` / 100 to the wait time.

    If interval_jitter_ms and interval_jitter_percent are both set, both of
    them will be used to increase the wait time.
    """
    unhealthy_threshold: builtins.int
    """The number of unhealthy health checks required before a host is marked
    unhealthy. Note that for ``http`` health checking if a host responds with a
    code not in :ref:`expected_statuses
    <envoy_v3_api_field_config.core.v3.HealthCheck.HttpHealthCheck.expected_statuses>`
    or :ref:`retriable_statuses
    <envoy_v3_api_field_config.core.v3.HealthCheck.HttpHealthCheck.retriable_statuses>`,
    this threshold is ignored and the host is considered immediately unhealthy.
    """
    healthy_threshold: builtins.int
    """The number of healthy health checks required before a host is marked
    healthy. Note that during startup, only a single successful health check is
    required to mark a host healthy.
    """
    @property
    def timeout(self) -> google.protobuf.duration_pb2.Duration:
        """The time to wait for a health check response. If the timeout is reached the
        health check attempt will be considered a failure.
        """

    @property
    def interval(self) -> google.protobuf.duration_pb2.Duration:
        """The interval between health checks."""

    @property
    def initial_jitter(self) -> google.protobuf.duration_pb2.Duration:
        """An optional jitter amount in milliseconds. If specified, Envoy will start
        health checking after for a random time in ms between 0 and initial_jitter.
        This only applies to the first health check.
        """

    @property
    def interval_jitter(self) -> google.protobuf.duration_pb2.Duration:
        """An optional jitter amount in milliseconds. If specified, during every
        interval Envoy will add interval_jitter to the wait time.
        """

    @property
    def http_health_check(self) -> global___HealthCheck.HttpHealthCheck:
        """HTTP health check."""

    @property
    def tcp_health_check(self) -> global___HealthCheck.TcpHealthCheck:
        """TCP health check."""

    @property
    def grpc_health_check(self) -> global___HealthCheck.GrpcHealthCheck:
        """gRPC health check."""

    def __init__(
        self,
        *,
        timeout: google.protobuf.duration_pb2.Duration | None = ...,
        interval: google.protobuf.duration_pb2.Duration | None = ...,
        initial_jitter: google.protobuf.duration_pb2.Duration | None = ...,
        interval_jitter: google.protobuf.duration_pb2.Duration | None = ...,
        interval_jitter_percent: builtins.int = ...,
        unhealthy_threshold: builtins.int = ...,
        healthy_threshold: builtins.int = ...,
        http_health_check: global___HealthCheck.HttpHealthCheck | None = ...,
        tcp_health_check: global___HealthCheck.TcpHealthCheck | None = ...,
        grpc_health_check: global___HealthCheck.GrpcHealthCheck | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["grpc_health_check", b"grpc_health_check", "health_checker", b"health_checker", "http_health_check", b"http_health_check", "initial_jitter", b"initial_jitter", "interval", b"interval", "interval_jitter", b"interval_jitter", "tcp_health_check", b"tcp_health_check", "timeout", b"timeout"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["grpc_health_check", b"grpc_health_check", "health_checker", b"health_checker", "healthy_threshold", b"healthy_threshold", "http_health_check", b"http_health_check", "initial_jitter", b"initial_jitter", "interval", b"interval", "interval_jitter", b"interval_jitter", "interval_jitter_percent", b"interval_jitter_percent", "tcp_health_check", b"tcp_health_check", "timeout", b"timeout", "unhealthy_threshold", b"unhealthy_threshold"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["health_checker", b"health_checker"]) -> typing.Literal["http_health_check", "tcp_health_check", "grpc_health_check"] | None: ...

global___HealthCheck = HealthCheck
