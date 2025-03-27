"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
adapted from :
- https://github.com/envoyproxy/envoy/blob/main/api/envoy/type/range.proto
- https://github.com/envoyproxy/envoy/blob/main/api/envoy/type/http.proto
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _CodecClientType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CodecClientTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_CodecClientType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    HTTP1: _CodecClientType.ValueType  # 0
    HTTP2: _CodecClientType.ValueType  # 1
    HTTP3: _CodecClientType.ValueType  # 2

class CodecClientType(_CodecClientType, metaclass=_CodecClientTypeEnumTypeWrapper): ...

HTTP1: CodecClientType.ValueType  # 0
HTTP2: CodecClientType.ValueType  # 1
HTTP3: CodecClientType.ValueType  # 2
global___CodecClientType = CodecClientType

@typing.final
class Int64Range(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_FIELD_NUMBER: builtins.int
    END_FIELD_NUMBER: builtins.int
    start: builtins.int
    """start of the range (inclusive)"""
    end: builtins.int
    """end of the range (exclusive)"""
    def __init__(
        self,
        *,
        start: builtins.int = ...,
        end: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["end", b"end", "start", b"start"]) -> None: ...

global___Int64Range = Int64Range
