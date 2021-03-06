"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class TypedStruct(google.protobuf.message.Message):
    """A TypedStruct contains an arbitrary JSON serialized protocol buffer message with a URL that
    describes the type of the serialized message. This is very similar to google.protobuf.Any,
    instead of having protocol buffer binary, this employs google.protobuf.Struct as value.

    This message is intended to be embedded inside Any, so it shouldn't be directly referred
    from other UDPA messages.

    When packing an opaque extension config, packing the expected type into Any is preferred
    wherever possible for its efficiency. TypedStruct should be used only if a proto descriptor
    is not available, for example if:
    - A control plane sends opaque message that is originally from external source in human readable
      format such as JSON or YAML.
    - The control plane doesn't have the knowledge of the protocol buffer schema hence it cannot
      serialize the message in protocol buffer binary format.
    - The DPLB doesn't have have the knowledge of the protocol buffer schema its plugin or extension
      uses. This has to be indicated in the DPLB capability negotiation.

    When a DPLB receives a TypedStruct in Any, it should:
    - Check if the type_url of the TypedStruct matches the type the extension expects.
    - Convert value to the type described in type_url and perform validation.
    TODO(lizan): Figure out how TypeStruct should be used with DPLB extensions that doesn't link
    protobuf descriptor with DPLB itself, (e.g. gRPC LB Plugin, Envoy WASM extensions).
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TYPE_URL_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    type_url: typing.Text = ...
    """A URL that uniquely identifies the type of the serialize protocol buffer message.
    This has same semantics and format described in google.protobuf.Any:
    https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/any.proto
    """

    @property
    def value(self) -> google.protobuf.struct_pb2.Struct:
        """A JSON representation of the above specified type."""
        pass
    def __init__(self,
        *,
        type_url : typing.Text = ...,
        value : typing.Optional[google.protobuf.struct_pb2.Struct] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"type_url",b"type_url",u"value",b"value"]) -> None: ...
global___TypedStruct = TypedStruct
