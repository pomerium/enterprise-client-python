"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class HashPolicy(google.protobuf.message.Message):
    """[#protodoc-title: Hash Policy]

    Specifies the hash policy
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class SourceIp(google.protobuf.message.Message):
        """The source IP will be used to compute the hash used by hash-based load balancing
        algorithms.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        def __init__(self,
            ) -> None: ...

    class FilterState(google.protobuf.message.Message):
        """An Object in the :ref:`filterState <arch_overview_data_sharing_between_filters>` will be used
        to compute the hash used by hash-based load balancing algorithms.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        """The name of the Object in the filterState, which is an Envoy::Hashable object. If there is no
        data associated with the key, or the stored object is not Envoy::Hashable, no hash will be
        produced.
        """

        def __init__(self,
            *,
            key : typing.Text = ...,
            ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"key",b"key"]) -> None: ...

    SOURCE_IP_FIELD_NUMBER: builtins.int
    FILTER_STATE_FIELD_NUMBER: builtins.int
    @property
    def source_ip(self) -> global___HashPolicy.SourceIp: ...
    @property
    def filter_state(self) -> global___HashPolicy.FilterState: ...
    def __init__(self,
        *,
        source_ip : typing.Optional[global___HashPolicy.SourceIp] = ...,
        filter_state : typing.Optional[global___HashPolicy.FilterState] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"filter_state",b"filter_state",u"policy_specifier",b"policy_specifier",u"source_ip",b"source_ip"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"filter_state",b"filter_state",u"policy_specifier",b"policy_specifier",u"source_ip",b"source_ip"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"policy_specifier",b"policy_specifier"]) -> typing.Optional[typing_extensions.Literal["source_ip","filter_state"]]: ...
global___HashPolicy = HashPolicy
