"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ActivityLogEntry(google.protobuf.message.Message):
    """ActivityLogEntry contains context associated with a change in the deployment
    history
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class DiffSummary(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        ADDED_FIELD_NUMBER: builtins.int
        REMOVED_FIELD_NUMBER: builtins.int
        added: builtins.int
        """number of lines added"""
        removed: builtins.int
        """number of lines removed"""
        def __init__(
            self,
            *,
            added: builtins.int = ...,
            removed: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["added", b"added", "removed", b"removed"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    ACTIVITY_TYPE_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    NAMESPACE_NAME_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    USER_NAME_FIELD_NUMBER: builtins.int
    USER_EMAIL_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_FIELD_NUMBER: builtins.int
    ENTITY_ID_FIELD_NUMBER: builtins.int
    ENTITY_DATA_FIELD_NUMBER: builtins.int
    DIFF_SUMMARY_FIELD_NUMBER: builtins.int
    DB_VERSION_FIELD_NUMBER: builtins.int
    SESSION_ID_FIELD_NUMBER: builtins.int
    SERVICE_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    IMPERSONATE_USER_ID_FIELD_NUMBER: builtins.int
    IMPERSONATE_USER_NAME_FIELD_NUMBER: builtins.int
    IMPERSONATE_USER_EMAIL_FIELD_NUMBER: builtins.int
    IMPERSONATE_USER_GROUPS_FIELD_NUMBER: builtins.int
    id: builtins.str
    name: builtins.str
    activity_type: builtins.str
    """`DELETE` or `SET`"""
    cluster_id: builtins.str
    namespace_id: builtins.str
    namespace_name: builtins.str
    user_id: builtins.str
    user_name: builtins.str
    user_email: builtins.str
    entity_type: builtins.str
    """`route` | `policy` | `settings`"""
    entity_id: builtins.str
    entity_data: builtins.str
    db_version: builtins.int
    """databroker version this change synced to"""
    session_id: builtins.str
    service_account_id: builtins.str
    impersonate_user_id: builtins.str
    impersonate_user_name: builtins.str
    impersonate_user_email: builtins.str
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def diff_summary(self) -> global___ActivityLogEntry.DiffSummary: ...
    @property
    def impersonate_user_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        activity_type: builtins.str = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        cluster_id: builtins.str | None = ...,
        namespace_id: builtins.str = ...,
        namespace_name: builtins.str = ...,
        user_id: builtins.str = ...,
        user_name: builtins.str = ...,
        user_email: builtins.str = ...,
        entity_type: builtins.str = ...,
        entity_id: builtins.str = ...,
        entity_data: builtins.str = ...,
        diff_summary: global___ActivityLogEntry.DiffSummary | None = ...,
        db_version: builtins.int = ...,
        session_id: builtins.str = ...,
        service_account_id: builtins.str = ...,
        impersonate_user_id: builtins.str = ...,
        impersonate_user_name: builtins.str = ...,
        impersonate_user_email: builtins.str = ...,
        impersonate_user_groups: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_cluster_id", b"_cluster_id", "cluster_id", b"cluster_id", "created_at", b"created_at", "diff_summary", b"diff_summary"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_cluster_id", b"_cluster_id", "activity_type", b"activity_type", "cluster_id", b"cluster_id", "created_at", b"created_at", "db_version", b"db_version", "diff_summary", b"diff_summary", "entity_data", b"entity_data", "entity_id", b"entity_id", "entity_type", b"entity_type", "id", b"id", "impersonate_user_email", b"impersonate_user_email", "impersonate_user_groups", b"impersonate_user_groups", "impersonate_user_id", b"impersonate_user_id", "impersonate_user_name", b"impersonate_user_name", "name", b"name", "namespace_id", b"namespace_id", "namespace_name", b"namespace_name", "service_account_id", b"service_account_id", "session_id", b"session_id", "user_email", b"user_email", "user_id", b"user_id", "user_name", b"user_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_cluster_id", b"_cluster_id"]) -> typing.Literal["cluster_id"] | None: ...

global___ActivityLogEntry = ActivityLogEntry

@typing.final
class GetActivityLogEntryRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___GetActivityLogEntryRequest = GetActivityLogEntryRequest

@typing.final
class GetActivityLogEntryResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENTRY_FIELD_NUMBER: builtins.int
    PREVIOUS_ENTRY_ID_FIELD_NUMBER: builtins.int
    NEXT_ENTRY_ID_FIELD_NUMBER: builtins.int
    previous_entry_id: builtins.str
    next_entry_id: builtins.str
    @property
    def entry(self) -> global___ActivityLogEntry: ...
    def __init__(
        self,
        *,
        entry: global___ActivityLogEntry | None = ...,
        previous_entry_id: builtins.str | None = ...,
        next_entry_id: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_next_entry_id", b"_next_entry_id", "_previous_entry_id", b"_previous_entry_id", "entry", b"entry", "next_entry_id", b"next_entry_id", "previous_entry_id", b"previous_entry_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_next_entry_id", b"_next_entry_id", "_previous_entry_id", b"_previous_entry_id", "entry", b"entry", "next_entry_id", b"next_entry_id", "previous_entry_id", b"previous_entry_id"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_next_entry_id", b"_next_entry_id"]) -> typing.Literal["next_entry_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_previous_entry_id", b"_previous_entry_id"]) -> typing.Literal["previous_entry_id"] | None: ...

global___GetActivityLogEntryResponse = GetActivityLogEntryResponse

@typing.final
class ListActivityLogEntriesRequest(google.protobuf.message.Message):
    """ListActivityLogEntriesRequest defines the types of Activity Log entries to
    list
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Entity(google.protobuf.message.Message):
        """an entity is a single entity (route, policy, etc.)"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        TYPE_FIELD_NUMBER: builtins.int
        ID_FIELD_NUMBER: builtins.int
        type: builtins.str
        id: builtins.str
        def __init__(
            self,
            *,
            type: builtins.str = ...,
            id: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["id", b"id", "type", b"type"]) -> None: ...

    @typing.final
    class Sort(google.protobuf.message.Message):
        """used to sort the db query"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        COLUMN_FIELD_NUMBER: builtins.int
        DIRECTION_FIELD_NUMBER: builtins.int
        column: builtins.str
        """`activity_type` | `created_at` | `namespace_name` | `user_name` |
        `user_email` | `entity_type`
        """
        direction: builtins.str
        """`ASC` | `DESC`"""
        def __init__(
            self,
            *,
            column: builtins.str = ...,
            direction: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["column", b"column", "direction", b"direction"]) -> None: ...

    @typing.final
    class DateFilter(google.protobuf.message.Message):
        """filter for dates"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        OPERATOR_FIELD_NUMBER: builtins.int
        DATE_FIELD_NUMBER: builtins.int
        operator: builtins.str
        """`=` | `!=` | `<` | `<=` | `>` | `>=`"""
        @property
        def date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
        def __init__(
            self,
            *,
            operator: builtins.str = ...,
            date: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["date", b"date"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["date", b"date", "operator", b"operator"]) -> None: ...

    @typing.final
    class StringFilter(google.protobuf.message.Message):
        """filter for strings"""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        FIELDNAME_FIELD_NUMBER: builtins.int
        OPERATOR_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        fieldName: builtins.str
        operator: builtins.str
        """`contains` | `equals` | `startsWith` | `endsWith`"""
        value: builtins.str
        def __init__(
            self,
            *,
            fieldName: builtins.str = ...,
            operator: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["fieldName", b"fieldName", "operator", b"operator", "value", b"value"]) -> None: ...

    ACTIVITY_TYPE_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    ENTITY_TYPE_FIELD_NUMBER: builtins.int
    ENTITY_ID_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    DB_VERSIONS_FIELD_NUMBER: builtins.int
    RECURSE_NAMESPACE_FIELD_NUMBER: builtins.int
    ENTITIES_FIELD_NUMBER: builtins.int
    SORT_FIELD_NUMBER: builtins.int
    DATE_FILTER_FIELD_NUMBER: builtins.int
    STRING_FILTER_FIELD_NUMBER: builtins.int
    activity_type: builtins.str
    """`DELETE` | `SET`"""
    namespace_id: builtins.str
    user_id: builtins.str
    entity_type: builtins.str
    """`route` | `policy` | `settings`"""
    entity_id: builtins.str
    query: builtins.str
    """`newest` | `oldest` | `from` | `name`"""
    offset: builtins.int
    """list entries starting from an offset in the total list"""
    limit: builtins.int
    """limit the number of entries returned"""
    recurse_namespace: builtins.bool
    """if true, show activity for the namespace and any child namespaces"""
    @property
    def db_versions(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """databroker versions of the change"""

    @property
    def entities(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ListActivityLogEntriesRequest.Entity]:
        """the entities are a list of entities to retrieve the activity log for"""

    @property
    def sort(self) -> global___ListActivityLogEntriesRequest.Sort: ...
    @property
    def date_filter(self) -> global___ListActivityLogEntriesRequest.DateFilter: ...
    @property
    def string_filter(self) -> global___ListActivityLogEntriesRequest.StringFilter: ...
    def __init__(
        self,
        *,
        activity_type: builtins.str | None = ...,
        namespace_id: builtins.str | None = ...,
        user_id: builtins.str | None = ...,
        entity_type: builtins.str | None = ...,
        entity_id: builtins.str | None = ...,
        query: builtins.str | None = ...,
        offset: builtins.int | None = ...,
        limit: builtins.int | None = ...,
        db_versions: collections.abc.Iterable[builtins.int] | None = ...,
        recurse_namespace: builtins.bool | None = ...,
        entities: collections.abc.Iterable[global___ListActivityLogEntriesRequest.Entity] | None = ...,
        sort: global___ListActivityLogEntriesRequest.Sort | None = ...,
        date_filter: global___ListActivityLogEntriesRequest.DateFilter | None = ...,
        string_filter: global___ListActivityLogEntriesRequest.StringFilter | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_activity_type", b"_activity_type", "_entity_id", b"_entity_id", "_entity_type", b"_entity_type", "_limit", b"_limit", "_namespace_id", b"_namespace_id", "_offset", b"_offset", "_query", b"_query", "_recurse_namespace", b"_recurse_namespace", "_sort", b"_sort", "_user_id", b"_user_id", "activity_type", b"activity_type", "date_filter", b"date_filter", "entity_id", b"entity_id", "entity_type", b"entity_type", "limit", b"limit", "namespace_id", b"namespace_id", "offset", b"offset", "query", b"query", "recurse_namespace", b"recurse_namespace", "sort", b"sort", "string_filter", b"string_filter", "user_id", b"user_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_activity_type", b"_activity_type", "_entity_id", b"_entity_id", "_entity_type", b"_entity_type", "_limit", b"_limit", "_namespace_id", b"_namespace_id", "_offset", b"_offset", "_query", b"_query", "_recurse_namespace", b"_recurse_namespace", "_sort", b"_sort", "_user_id", b"_user_id", "activity_type", b"activity_type", "date_filter", b"date_filter", "db_versions", b"db_versions", "entities", b"entities", "entity_id", b"entity_id", "entity_type", b"entity_type", "limit", b"limit", "namespace_id", b"namespace_id", "offset", b"offset", "query", b"query", "recurse_namespace", b"recurse_namespace", "sort", b"sort", "string_filter", b"string_filter", "user_id", b"user_id"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_activity_type", b"_activity_type"]) -> typing.Literal["activity_type"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_entity_id", b"_entity_id"]) -> typing.Literal["entity_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_entity_type", b"_entity_type"]) -> typing.Literal["entity_type"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_limit", b"_limit"]) -> typing.Literal["limit"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_namespace_id", b"_namespace_id"]) -> typing.Literal["namespace_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_offset", b"_offset"]) -> typing.Literal["offset"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_query", b"_query"]) -> typing.Literal["query"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_recurse_namespace", b"_recurse_namespace"]) -> typing.Literal["recurse_namespace"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_sort", b"_sort"]) -> typing.Literal["sort"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_user_id", b"_user_id"]) -> typing.Literal["user_id"] | None: ...

global___ListActivityLogEntriesRequest = ListActivityLogEntriesRequest

@typing.final
class ListActivityLogEntriesResponse(google.protobuf.message.Message):
    """ListActivityLogEntriesResponse is a list of Activity Log entries found from a
    ListActivityLogEntriesRequest
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENTRIES_FIELD_NUMBER: builtins.int
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    total_count: builtins.int
    @property
    def entries(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ActivityLogEntry]:
        """Activity Log entries"""

    def __init__(
        self,
        *,
        entries: collections.abc.Iterable[global___ActivityLogEntry] | None = ...,
        total_count: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["entries", b"entries", "total_count", b"total_count"]) -> None: ...

global___ListActivityLogEntriesResponse = ListActivityLogEntriesResponse
