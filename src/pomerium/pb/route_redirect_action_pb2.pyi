"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
adapted from :
-
https://github.com/envoyproxy/envoy/blob/057f7e0223d1985fd3b8f1adb1f6191454d963de/api/envoy/type/matcher/v3/regex.proto
-
https://github.com/envoyproxy/envoy/blob/057f7e0223d1985fd3b8f1adb1f6191454d963de/api/envoy/config/route/v3/route_components.proto#L1654
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

@typing.final
class RedirectAction(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _RedirectResponseCode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RedirectResponseCodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RedirectAction._RedirectResponseCode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        MOVED_PERMANENTLY: RedirectAction._RedirectResponseCode.ValueType  # 0
        """Moved Permanently HTTP Status Code - 301."""
        FOUND: RedirectAction._RedirectResponseCode.ValueType  # 1
        """Found HTTP Status Code - 302."""
        SEE_OTHER: RedirectAction._RedirectResponseCode.ValueType  # 2
        """See Other HTTP Status Code - 303."""
        TEMPORARY_REDIRECT: RedirectAction._RedirectResponseCode.ValueType  # 3
        """Temporary Redirect HTTP Status Code - 307."""
        PERMANENT_REDIRECT: RedirectAction._RedirectResponseCode.ValueType  # 4
        """Permanent Redirect HTTP Status Code - 308."""

    class RedirectResponseCode(_RedirectResponseCode, metaclass=_RedirectResponseCodeEnumTypeWrapper): ...
    MOVED_PERMANENTLY: RedirectAction.RedirectResponseCode.ValueType  # 0
    """Moved Permanently HTTP Status Code - 301."""
    FOUND: RedirectAction.RedirectResponseCode.ValueType  # 1
    """Found HTTP Status Code - 302."""
    SEE_OTHER: RedirectAction.RedirectResponseCode.ValueType  # 2
    """See Other HTTP Status Code - 303."""
    TEMPORARY_REDIRECT: RedirectAction.RedirectResponseCode.ValueType  # 3
    """Temporary Redirect HTTP Status Code - 307."""
    PERMANENT_REDIRECT: RedirectAction.RedirectResponseCode.ValueType  # 4
    """Permanent Redirect HTTP Status Code - 308."""

    @typing.final
    class RegexMatchAndSubstitute(google.protobuf.message.Message):
        """Describes how to match a string and then produce a new string using a
        regular expression and a substitution string.
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PATTERN_FIELD_NUMBER: builtins.int
        SUBSTITUTION_FIELD_NUMBER: builtins.int
        pattern: builtins.str
        """The regular expression used to find portions of a string (hereafter
        called the "subject string") that should be replaced. When a new string
        is produced during the substitution operation, the new string is
        initially the same as the subject string, but then all matches in the
        subject string are replaced by the substitution string. If replacing all
        matches isn't desired, regular expression anchors can be used to ensure a
        single match, so as to replace just one occurrence of a pattern. Capture
        groups can be used in the pattern to extract portions of the subject
        string, and then referenced in the substitution string.
        """
        substitution: builtins.str
        """The string that should be substituted into matching portions of the
        subject string during a substitution operation to produce a new string.
        Capture groups in the pattern can be referenced in the substitution
        string. Note, however, that the syntax for referring to capture groups is
        defined by the chosen regular expression engine. Google's `RE2
        <https://github.com/google/re2>`_ regular expression engine uses a
        backslash followed by the capture group number to denote a numbered
        capture group. E.g., ``\\1`` refers to capture group 1, and ``\\2`` refers
        to capture group 2.
        """
        def __init__(
            self,
            *,
            pattern: builtins.str = ...,
            substitution: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["pattern", b"pattern", "substitution", b"substitution"]) -> None: ...

    HTTPS_REDIRECT_FIELD_NUMBER: builtins.int
    SCHEME_REDIRECT_FIELD_NUMBER: builtins.int
    HOST_REDIRECT_FIELD_NUMBER: builtins.int
    PORT_REDIRECT_FIELD_NUMBER: builtins.int
    PATH_REDIRECT_FIELD_NUMBER: builtins.int
    PREFIX_REWRITE_FIELD_NUMBER: builtins.int
    REGEX_REWRITE_FIELD_NUMBER: builtins.int
    RESPONSE_CODE_FIELD_NUMBER: builtins.int
    STRIP_QUERY_FIELD_NUMBER: builtins.int
    https_redirect: builtins.bool
    """The scheme portion of the URL will be swapped with "https"."""
    scheme_redirect: builtins.str
    """The scheme portion of the URL will be swapped with this value."""
    host_redirect: builtins.str
    """The host portion of the URL will be swapped with this value."""
    port_redirect: builtins.int
    """The port value of the URL will be swapped with this value."""
    path_redirect: builtins.str
    """The path portion of the URL will be swapped with this value.
    Please note that query string in path_redirect will override the
    request's query string and will not be stripped.

    For example, let's say we have the following routes:

    - match: { path: "/old-path-1" }
      redirect: { path_redirect: "/new-path-1" }
    - match: { path: "/old-path-2" }
      redirect: { path_redirect: "/new-path-2", strip-query: "true" }
    - match: { path: "/old-path-3" }
      redirect: { path_redirect: "/new-path-3?foo=1", strip_query: "true" }

    1. if request uri is "/old-path-1?bar=1", users will be redirected to
    "/new-path-1?bar=1"
    2. if request uri is "/old-path-2?bar=1", users will be redirected to
    "/new-path-2"
    3. if request uri is "/old-path-3?bar=1", users will be redirected to
    "/new-path-3?foo=1"
    """
    prefix_rewrite: builtins.str
    """Indicates that during redirection, the matched prefix (or path)
    should be swapped with this value. This option allows redirect URLs be
    dynamically created based on the request.

    .. attention::

      Pay attention to the use of trailing slashes as mentioned in
      :ref:`RouteAction's prefix_rewrite
      <envoy_v3_api_field_config.route.v3.RouteAction.prefix_rewrite>`.
    """
    response_code: global___RedirectAction.RedirectResponseCode.ValueType
    """The HTTP status code to use in the redirect response. The default response
    code is MOVED_PERMANENTLY (301).
    """
    strip_query: builtins.bool
    """Indicates that during redirection, the query portion of the URL will
    be removed. Default value is false.
    """
    @property
    def regex_rewrite(self) -> global___RedirectAction.RegexMatchAndSubstitute:
        """Indicates that during redirect, portions of the path that match the
        pattern should be rewritten, even allowing the substitution of capture
        groups from the pattern into the new path as specified by the rewrite
        substitution string. This is useful to allow application paths to be
        rewritten in a way that is aware of segments with variable content like
        identifiers.

        Examples using Google's `RE2 <https://github.com/google/re2>`_ engine:

        * The path pattern ``^/service/([^/]+)(/.*)$`` paired with a substitution
          string of ``\\2/instance/\\1`` would transform ``/service/foo/v1/api``
          into ``/v1/api/instance/foo``.

        * The pattern ``one`` paired with a substitution string of ``two`` would
          transform ``/xxx/one/yyy/one/zzz`` into ``/xxx/two/yyy/two/zzz``.

        * The pattern ``^(.*?)one(.*)$`` paired with a substitution string of
          ``\\1two\\2`` would replace only the first occurrence of ``one``,
          transforming path ``/xxx/one/yyy/one/zzz`` into
          ``/xxx/two/yyy/one/zzz``.

        * The pattern ``(?i)/xxx/`` paired with a substitution string of
        ``/yyy/``
          would do a case-insensitive match and transform path ``/aaa/XxX/bbb``
          to
          ``/aaa/yyy/bbb``.
        """

    def __init__(
        self,
        *,
        https_redirect: builtins.bool = ...,
        scheme_redirect: builtins.str = ...,
        host_redirect: builtins.str = ...,
        port_redirect: builtins.int = ...,
        path_redirect: builtins.str = ...,
        prefix_rewrite: builtins.str = ...,
        regex_rewrite: global___RedirectAction.RegexMatchAndSubstitute | None = ...,
        response_code: global___RedirectAction.RedirectResponseCode.ValueType = ...,
        strip_query: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["https_redirect", b"https_redirect", "path_redirect", b"path_redirect", "path_rewrite_specifier", b"path_rewrite_specifier", "prefix_rewrite", b"prefix_rewrite", "regex_rewrite", b"regex_rewrite", "scheme_redirect", b"scheme_redirect", "scheme_rewrite_specifier", b"scheme_rewrite_specifier"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["host_redirect", b"host_redirect", "https_redirect", b"https_redirect", "path_redirect", b"path_redirect", "path_rewrite_specifier", b"path_rewrite_specifier", "port_redirect", b"port_redirect", "prefix_rewrite", b"prefix_rewrite", "regex_rewrite", b"regex_rewrite", "response_code", b"response_code", "scheme_redirect", b"scheme_redirect", "scheme_rewrite_specifier", b"scheme_rewrite_specifier", "strip_query", b"strip_query"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["path_rewrite_specifier", b"path_rewrite_specifier"]) -> typing.Literal["path_redirect", "prefix_rewrite", "regex_rewrite"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["scheme_rewrite_specifier", b"scheme_rewrite_specifier"]) -> typing.Literal["https_redirect", "scheme_redirect"] | None: ...

global___RedirectAction = RedirectAction
