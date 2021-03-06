"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class UdpSocketConfig(google.protobuf.message.Message):
    """[#protodoc-title: UDP socket config]

    Generic UDP socket configuration.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MAX_RX_DATAGRAM_SIZE_FIELD_NUMBER: builtins.int
    PREFER_GRO_FIELD_NUMBER: builtins.int
    @property
    def max_rx_datagram_size(self) -> google.protobuf.wrappers_pb2.UInt64Value:
        """The maximum size of received UDP datagrams. Using a larger size will cause Envoy to allocate
        more memory per socket. Received datagrams above this size will be dropped. If not set
        defaults to 1500 bytes.
        """
        pass
    @property
    def prefer_gro(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """Configures whether Generic Receive Offload (GRO)
        <https://en.wikipedia.org/wiki/Large_receive_offload>_ is preferred when reading from the
        UDP socket. The default is context dependent and is documented where UdpSocketConfig is used.
        This option affects performance but not functionality. If GRO is not supported by the operating
        system, non-GRO receive will be used.
        """
        pass
    def __init__(self,
        *,
        max_rx_datagram_size : typing.Optional[google.protobuf.wrappers_pb2.UInt64Value] = ...,
        prefer_gro : typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"max_rx_datagram_size",b"max_rx_datagram_size",u"prefer_gro",b"prefer_gro"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"max_rx_datagram_size",b"max_rx_datagram_size",u"prefer_gro",b"prefer_gro"]) -> None: ...
global___UdpSocketConfig = UdpSocketConfig
