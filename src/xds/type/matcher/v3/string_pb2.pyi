"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions
import xds.type.matcher.v3.regex_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class StringMatcher(google.protobuf.message.Message):
    """[#protodoc-title: String matcher]

    Specifies the way to match a string.
    [#next-free-field: 8]
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    EXACT_FIELD_NUMBER: builtins.int
    PREFIX_FIELD_NUMBER: builtins.int
    SUFFIX_FIELD_NUMBER: builtins.int
    SAFE_REGEX_FIELD_NUMBER: builtins.int
    CONTAINS_FIELD_NUMBER: builtins.int
    IGNORE_CASE_FIELD_NUMBER: builtins.int
    exact: typing.Text = ...
    """The input string must match exactly the string specified here.

    Examples:

    * *abc* only matches the value *abc*.
    """

    prefix: typing.Text = ...
    """The input string must have the prefix specified here.
    Note: empty prefix is not allowed, please use regex instead.

    Examples:

    * *abc* matches the value *abc.xyz*
    """

    suffix: typing.Text = ...
    """The input string must have the suffix specified here.
    Note: empty prefix is not allowed, please use regex instead.

    Examples:

    * *abc* matches the value *xyz.abc*
    """

    @property
    def safe_regex(self) -> xds.type.matcher.v3.regex_pb2.RegexMatcher:
        """The input string must match the regular expression specified here."""
        pass
    contains: typing.Text = ...
    """The input string must have the substring specified here.
    Note: empty contains match is not allowed, please use regex instead.

    Examples:

    * *abc* matches the value *xyz.abc.def*
    """

    ignore_case: builtins.bool = ...
    """If true, indicates the exact/prefix/suffix matching should be case insensitive. This has no
    effect for the safe_regex match.
    For example, the matcher *data* will match both input string *Data* and *data* if set to true.
    """

    def __init__(self,
        *,
        exact : typing.Text = ...,
        prefix : typing.Text = ...,
        suffix : typing.Text = ...,
        safe_regex : typing.Optional[xds.type.matcher.v3.regex_pb2.RegexMatcher] = ...,
        contains : typing.Text = ...,
        ignore_case : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"contains",b"contains",u"exact",b"exact",u"match_pattern",b"match_pattern",u"prefix",b"prefix",u"safe_regex",b"safe_regex",u"suffix",b"suffix"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"contains",b"contains",u"exact",b"exact",u"ignore_case",b"ignore_case",u"match_pattern",b"match_pattern",u"prefix",b"prefix",u"safe_regex",b"safe_regex",u"suffix",b"suffix"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"match_pattern",b"match_pattern"]) -> typing.Optional[typing_extensions.Literal["exact","prefix","suffix","safe_regex","contains"]]: ...
global___StringMatcher = StringMatcher

class ListStringMatcher(google.protobuf.message.Message):
    """Specifies a list of ways to match a string."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PATTERNS_FIELD_NUMBER: builtins.int
    @property
    def patterns(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StringMatcher]: ...
    def __init__(self,
        *,
        patterns : typing.Optional[typing.Iterable[global___StringMatcher]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"patterns",b"patterns"]) -> None: ...
global___ListStringMatcher = ListStringMatcher
