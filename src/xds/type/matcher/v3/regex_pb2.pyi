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

class RegexMatcher(google.protobuf.message.Message):
    """[#protodoc-title: Regex matcher]

    A regex matcher designed for safety when used with untrusted input.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class GoogleRE2(google.protobuf.message.Message):
        """Google's `RE2 <https://github.com/google/re2>`_ regex engine. The regex
        string must adhere to the documented `syntax
        <https://github.com/google/re2/wiki/Syntax>`_. The engine is designed to
        complete execution in linear time as well as limit the amount of memory
        used.

        Envoy supports program size checking via runtime. The runtime keys
        `re2.max_program_size.error_level` and `re2.max_program_size.warn_level`
        can be set to integers as the maximum program size or complexity that a
        compiled regex can have before an exception is thrown or a warning is
        logged, respectively. `re2.max_program_size.error_level` defaults to 100,
        and `re2.max_program_size.warn_level` has no default if unset (will not
        check/log a warning).

        Envoy emits two stats for tracking the program size of regexes: the
        histogram `re2.program_size`, which records the program size, and the
        counter `re2.exceeded_warn_level`, which is incremented each time the
        program size exceeds the warn level threshold.
        """
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        def __init__(self,
            ) -> None: ...

    GOOGLE_RE2_FIELD_NUMBER: builtins.int
    REGEX_FIELD_NUMBER: builtins.int
    @property
    def google_re2(self) -> global___RegexMatcher.GoogleRE2:
        """Google's RE2 regex engine."""
        pass
    regex: typing.Text = ...
    """The regex match string. The string must be supported by the configured
    engine.
    """

    def __init__(self,
        *,
        google_re2 : typing.Optional[global___RegexMatcher.GoogleRE2] = ...,
        regex : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"engine_type",b"engine_type",u"google_re2",b"google_re2"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"engine_type",b"engine_type",u"google_re2",b"google_re2",u"regex",b"regex"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"engine_type",b"engine_type"]) -> typing.Optional[typing_extensions.Literal["google_re2"]]: ...
global___RegexMatcher = RegexMatcher
