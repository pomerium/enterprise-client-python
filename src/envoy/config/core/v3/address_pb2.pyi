"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import envoy.config.core.v3.socket_option_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Pipe(google.protobuf.message.Message):
    """[#protodoc-title: Network addresses]

    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PATH_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    path: typing.Text = ...
    """Unix Domain Socket path. On Linux, paths starting with '@' will use the
    abstract namespace. The starting '@' is replaced by a null byte by Envoy.
    Paths starting with '@' will result in an error in environments other than
    Linux.
    """

    mode: builtins.int = ...
    """The mode for the Pipe. Not applicable for abstract sockets."""

    def __init__(self,
        *,
        path : typing.Text = ...,
        mode : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"mode",b"mode",u"path",b"path"]) -> None: ...
global___Pipe = Pipe

class EnvoyInternalAddress(google.protobuf.message.Message):
    """[#not-implemented-hide:] The address represents an envoy internal listener.
    TODO(lambdai): Make this address available for listener and endpoint.
    TODO(asraa): When address available, remove workaround from test/server/server_fuzz_test.cc:30.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SERVER_LISTENER_NAME_FIELD_NUMBER: builtins.int
    server_listener_name: typing.Text = ...
    """[#not-implemented-hide:] The :ref:`listener name <envoy_v3_api_field_config.listener.v3.Listener.name>` of the destination internal listener."""

    def __init__(self,
        *,
        server_listener_name : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"address_name_specifier",b"address_name_specifier",u"server_listener_name",b"server_listener_name"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address_name_specifier",b"address_name_specifier",u"server_listener_name",b"server_listener_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"address_name_specifier",b"address_name_specifier"]) -> typing.Optional[typing_extensions.Literal["server_listener_name"]]: ...
global___EnvoyInternalAddress = EnvoyInternalAddress

class SocketAddress(google.protobuf.message.Message):
    """[#next-free-field: 7]"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Protocol(_Protocol, metaclass=_ProtocolEnumTypeWrapper):
        pass
    class _Protocol:
        V = typing.NewType('V', builtins.int)
    class _ProtocolEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Protocol.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        TCP = SocketAddress.Protocol.V(0)
        UDP = SocketAddress.Protocol.V(1)

    TCP = SocketAddress.Protocol.V(0)
    UDP = SocketAddress.Protocol.V(1)

    PROTOCOL_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    PORT_VALUE_FIELD_NUMBER: builtins.int
    NAMED_PORT_FIELD_NUMBER: builtins.int
    RESOLVER_NAME_FIELD_NUMBER: builtins.int
    IPV4_COMPAT_FIELD_NUMBER: builtins.int
    protocol: global___SocketAddress.Protocol.V = ...
    address: typing.Text = ...
    """The address for this socket. :ref:`Listeners <config_listeners>` will bind
    to the address. An empty address is not allowed. Specify ``0.0.0.0`` or ``::``
    to bind to any address. [#comment:TODO(zuercher) reinstate when implemented:
    It is possible to distinguish a Listener address via the prefix/suffix matching
    in :ref:`FilterChainMatch <envoy_v3_api_msg_config.listener.v3.FilterChainMatch>`.] When used
    within an upstream :ref:`BindConfig <envoy_v3_api_msg_config.core.v3.BindConfig>`, the address
    controls the source address of outbound connections. For :ref:`clusters
    <envoy_v3_api_msg_config.cluster.v3.Cluster>`, the cluster type determines whether the
    address must be an IP (*STATIC* or *EDS* clusters) or a hostname resolved by DNS
    (*STRICT_DNS* or *LOGICAL_DNS* clusters). Address resolution can be customized
    via :ref:`resolver_name <envoy_v3_api_field_config.core.v3.SocketAddress.resolver_name>`.
    """

    port_value: builtins.int = ...
    named_port: typing.Text = ...
    """This is only valid if :ref:`resolver_name
    <envoy_v3_api_field_config.core.v3.SocketAddress.resolver_name>` is specified below and the
    named resolver is capable of named port resolution.
    """

    resolver_name: typing.Text = ...
    """The name of the custom resolver. This must have been registered with Envoy. If
    this is empty, a context dependent default applies. If the address is a concrete
    IP address, no resolution will occur. If address is a hostname this
    should be set for resolution other than DNS. Specifying a custom resolver with
    *STRICT_DNS* or *LOGICAL_DNS* will generate an error at runtime.
    """

    ipv4_compat: builtins.bool = ...
    """When binding to an IPv6 address above, this enables `IPv4 compatibility
    <https://tools.ietf.org/html/rfc3493#page-11>`_. Binding to ``::`` will
    allow both IPv4 and IPv6 connections, with peer IPv4 addresses mapped into
    IPv6 space as ``::FFFF:<IPv4-address>``.
    """

    def __init__(self,
        *,
        protocol : global___SocketAddress.Protocol.V = ...,
        address : typing.Text = ...,
        port_value : builtins.int = ...,
        named_port : typing.Text = ...,
        resolver_name : typing.Text = ...,
        ipv4_compat : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"named_port",b"named_port",u"port_specifier",b"port_specifier",u"port_value",b"port_value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"ipv4_compat",b"ipv4_compat",u"named_port",b"named_port",u"port_specifier",b"port_specifier",u"port_value",b"port_value",u"protocol",b"protocol",u"resolver_name",b"resolver_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"port_specifier",b"port_specifier"]) -> typing.Optional[typing_extensions.Literal["port_value","named_port"]]: ...
global___SocketAddress = SocketAddress

class TcpKeepalive(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEEPALIVE_PROBES_FIELD_NUMBER: builtins.int
    KEEPALIVE_TIME_FIELD_NUMBER: builtins.int
    KEEPALIVE_INTERVAL_FIELD_NUMBER: builtins.int
    @property
    def keepalive_probes(self) -> google.protobuf.wrappers_pb2.UInt32Value:
        """Maximum number of keepalive probes to send without response before deciding
        the connection is dead. Default is to use the OS level configuration (unless
        overridden, Linux defaults to 9.)
        """
        pass
    @property
    def keepalive_time(self) -> google.protobuf.wrappers_pb2.UInt32Value:
        """The number of seconds a connection needs to be idle before keep-alive probes
        start being sent. Default is to use the OS level configuration (unless
        overridden, Linux defaults to 7200s (i.e., 2 hours.)
        """
        pass
    @property
    def keepalive_interval(self) -> google.protobuf.wrappers_pb2.UInt32Value:
        """The number of seconds between keep-alive probes. Default is to use the OS
        level configuration (unless overridden, Linux defaults to 75s.)
        """
        pass
    def __init__(self,
        *,
        keepalive_probes : typing.Optional[google.protobuf.wrappers_pb2.UInt32Value] = ...,
        keepalive_time : typing.Optional[google.protobuf.wrappers_pb2.UInt32Value] = ...,
        keepalive_interval : typing.Optional[google.protobuf.wrappers_pb2.UInt32Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"keepalive_interval",b"keepalive_interval",u"keepalive_probes",b"keepalive_probes",u"keepalive_time",b"keepalive_time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"keepalive_interval",b"keepalive_interval",u"keepalive_probes",b"keepalive_probes",u"keepalive_time",b"keepalive_time"]) -> None: ...
global___TcpKeepalive = TcpKeepalive

class BindConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SOURCE_ADDRESS_FIELD_NUMBER: builtins.int
    FREEBIND_FIELD_NUMBER: builtins.int
    SOCKET_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def source_address(self) -> global___SocketAddress:
        """The address to bind to when creating a socket."""
        pass
    @property
    def freebind(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Whether to set the *IP_FREEBIND* option when creating the socket. When this
        flag is set to true, allows the :ref:`source_address
        <envoy_v3_api_field_config.cluster.v3.UpstreamBindConfig.source_address>` to be an IP address
        that is not configured on the system running Envoy. When this flag is set
        to false, the option *IP_FREEBIND* is disabled on the socket. When this
        flag is not set (default), the socket is not modified, i.e. the option is
        neither enabled nor disabled.
        """
        pass
    @property
    def socket_options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[envoy.config.core.v3.socket_option_pb2.SocketOption]:
        """Additional socket options that may not be present in Envoy source code or
        precompiled binaries.
        """
        pass
    def __init__(self,
        *,
        source_address : typing.Optional[global___SocketAddress] = ...,
        freebind : typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        socket_options : typing.Optional[typing.Iterable[envoy.config.core.v3.socket_option_pb2.SocketOption]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"freebind",b"freebind",u"source_address",b"source_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"freebind",b"freebind",u"socket_options",b"socket_options",u"source_address",b"source_address"]) -> None: ...
global___BindConfig = BindConfig

class Address(google.protobuf.message.Message):
    """Addresses specify either a logical or physical address and port, which are
    used to tell Envoy where to bind/listen, connect to upstream and find
    management servers.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SOCKET_ADDRESS_FIELD_NUMBER: builtins.int
    PIPE_FIELD_NUMBER: builtins.int
    ENVOY_INTERNAL_ADDRESS_FIELD_NUMBER: builtins.int
    @property
    def socket_address(self) -> global___SocketAddress: ...
    @property
    def pipe(self) -> global___Pipe: ...
    @property
    def envoy_internal_address(self) -> global___EnvoyInternalAddress:
        """[#not-implemented-hide:]"""
        pass
    def __init__(self,
        *,
        socket_address : typing.Optional[global___SocketAddress] = ...,
        pipe : typing.Optional[global___Pipe] = ...,
        envoy_internal_address : typing.Optional[global___EnvoyInternalAddress] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"address",b"address",u"envoy_internal_address",b"envoy_internal_address",u"pipe",b"pipe",u"socket_address",b"socket_address"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address",b"address",u"envoy_internal_address",b"envoy_internal_address",u"pipe",b"pipe",u"socket_address",b"socket_address"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"address",b"address"]) -> typing.Optional[typing_extensions.Literal["socket_address","pipe","envoy_internal_address"]]: ...
global___Address = Address

class CidrRange(google.protobuf.message.Message):
    """CidrRange specifies an IP Address and a prefix length to construct
    the subnet mask for a `CIDR <https://tools.ietf.org/html/rfc4632>`_ range.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADDRESS_PREFIX_FIELD_NUMBER: builtins.int
    PREFIX_LEN_FIELD_NUMBER: builtins.int
    address_prefix: typing.Text = ...
    """IPv4 or IPv6 address, e.g. ``192.0.0.0`` or ``2001:db8::``."""

    @property
    def prefix_len(self) -> google.protobuf.wrappers_pb2.UInt32Value:
        """Length of prefix, e.g. 0, 32. Defaults to 0 when unset."""
        pass
    def __init__(self,
        *,
        address_prefix : typing.Text = ...,
        prefix_len : typing.Optional[google.protobuf.wrappers_pb2.UInt32Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"prefix_len",b"prefix_len"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"address_prefix",b"address_prefix",u"prefix_len",b"prefix_len"]) -> None: ...
global___CidrRange = CidrRange
