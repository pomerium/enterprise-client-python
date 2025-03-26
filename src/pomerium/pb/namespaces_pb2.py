# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: namespaces.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10namespaces.proto\x12\x12pomerium.dashboard\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb3\x02\n\tNamespace\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tparent_id\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\ndeleted_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x15\n\roriginator_id\x18\t \x01(\t\x12\x17\n\ncluster_id\x18\n \x01(\tH\x00\x88\x01\x01\x12\x13\n\x0broute_count\x18\x07 \x01(\x03\x12\x14\n\x0cpolicy_count\x18\x08 \x01(\x03\x42\r\n\x0b_cluster_id\"$\n\x16\x44\x65leteNamespaceRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x19\n\x17\x44\x65leteNamespaceResponse\"!\n\x13GetNamespaceRequest\x12\n\n\x02id\x18\x01 \x01(\t\"H\n\x14GetNamespaceResponse\x12\x30\n\tnamespace\x18\x01 \x01(\x0b\x32\x1d.pomerium.dashboard.Namespace\"\x17\n\x15ListNamespacesRequest\"K\n\x16ListNamespacesResponse\x12\x31\n\nnamespaces\x18\x01 \x03(\x0b\x32\x1d.pomerium.dashboard.Namespace\",\n\x1dListNamespaceResourcesRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\"\xa4\x01\n\x1eListNamespaceResourcesResponse\x12N\n\tresources\x18\x01 \x03(\x0b\x32;.pomerium.dashboard.ListNamespaceResourcesResponse.Resource\x1a\x32\n\x08Resource\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"G\n\x13SetNamespaceRequest\x12\x30\n\tnamespace\x18\x01 \x01(\x0b\x32\x1d.pomerium.dashboard.Namespace\"H\n\x14SetNamespaceResponse\x12\x30\n\tnamespace\x18\x01 \x01(\x0b\x32\x1d.pomerium.dashboard.Namespace\"\xff\x01\n\x13NamespacePermission\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0bmodified_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cnamespace_id\x18\x04 \x01(\t\x12\x16\n\x0enamespace_name\x18\x08 \x01(\t\x12\x14\n\x0csubject_type\x18\x05 \x01(\t\x12\x12\n\nsubject_id\x18\x06 \x01(\t\x12\x0c\n\x04role\x18\x07 \x01(\t\x12\x15\n\roriginator_id\x18\t \x01(\t\"\xa8\x01\n\x18NamespacePermissionGroup\x12\x10\n\x08group_id\x18\x01 \x01(\t\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x13\n\x0bgroup_email\x18\x03 \x01(\t\x12\x14\n\x0cnamespace_id\x18\x04 \x01(\t\x12\x16\n\x0enamespace_name\x18\x05 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x15\n\roriginator_id\x18\x07 \x01(\t\"\xb7\x01\n\x17NamespacePermissionUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x12\n\nuser_email\x18\x03 \x01(\t\x12\x11\n\tgroup_ids\x18\x04 \x03(\t\x12\x14\n\x0cnamespace_id\x18\x05 \x01(\t\x12\x16\n\x0enamespace_name\x18\x07 \x01(\t\x12\x0c\n\x04role\x18\x06 \x01(\t\x12\x15\n\roriginator_id\x18\x08 \x01(\t\".\n DeleteNamespacePermissionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"#\n!DeleteNamespacePermissionResponse\"+\n\x1dGetNamespacePermissionRequest\x12\n\n\x02id\x18\x01 \x01(\t\"g\n\x1eGetNamespacePermissionResponse\x12\x45\n\x14namespace_permission\x18\x01 \x01(\x0b\x32\'.pomerium.dashboard.NamespacePermission\"!\n\x1fListNamespacePermissionsRequest\"j\n ListNamespacePermissionsResponse\x12\x46\n\x15namespace_permissions\x18\x01 \x03(\x0b\x32\'.pomerium.dashboard.NamespacePermission\"<\n$ListNamespacePermissionGroupsRequest\x12\x14\n\x0cnamespace_id\x18\x01 \x01(\t\"e\n%ListNamespacePermissionGroupsResponse\x12<\n\x06groups\x18\x01 \x03(\x0b\x32,.pomerium.dashboard.NamespacePermissionGroup\";\n#ListNamespacePermissionUsersRequest\x12\x14\n\x0cnamespace_id\x18\x01 \x01(\t\"b\n$ListNamespacePermissionUsersResponse\x12:\n\x05users\x18\x01 \x03(\x0b\x32+.pomerium.dashboard.NamespacePermissionUser\"f\n\x1dSetNamespacePermissionRequest\x12\x45\n\x14namespace_permission\x18\x01 \x01(\x0b\x32\'.pomerium.dashboard.NamespacePermission\"g\n\x1eSetNamespacePermissionResponse\x12\x45\n\x14namespace_permission\x18\x01 \x01(\x0b\x32\'.pomerium.dashboard.NamespacePermission2\xae\x04\n\x10NamespaceService\x12j\n\x0f\x44\x65leteNamespace\x12*.pomerium.dashboard.DeleteNamespaceRequest\x1a+.pomerium.dashboard.DeleteNamespaceResponse\x12\x61\n\x0cGetNamespace\x12\'.pomerium.dashboard.GetNamespaceRequest\x1a(.pomerium.dashboard.GetNamespaceResponse\x12g\n\x0eListNamespaces\x12).pomerium.dashboard.ListNamespacesRequest\x1a*.pomerium.dashboard.ListNamespacesResponse\x12\x7f\n\x16ListNamespaceResources\x12\x31.pomerium.dashboard.ListNamespaceResourcesRequest\x1a\x32.pomerium.dashboard.ListNamespaceResourcesResponse\x12\x61\n\x0cSetNamespace\x12\'.pomerium.dashboard.SetNamespaceRequest\x1a(.pomerium.dashboard.SetNamespaceResponse2\xdc\x06\n\x1aNamespacePermissionService\x12\x88\x01\n\x19\x44\x65leteNamespacePermission\x12\x34.pomerium.dashboard.DeleteNamespacePermissionRequest\x1a\x35.pomerium.dashboard.DeleteNamespacePermissionResponse\x12\x7f\n\x16GetNamespacePermission\x12\x31.pomerium.dashboard.GetNamespacePermissionRequest\x1a\x32.pomerium.dashboard.GetNamespacePermissionResponse\x12\x85\x01\n\x18ListNamespacePermissions\x12\x33.pomerium.dashboard.ListNamespacePermissionsRequest\x1a\x34.pomerium.dashboard.ListNamespacePermissionsResponse\x12\x94\x01\n\x1dListNamespacePermissionGroups\x12\x38.pomerium.dashboard.ListNamespacePermissionGroupsRequest\x1a\x39.pomerium.dashboard.ListNamespacePermissionGroupsResponse\x12\x91\x01\n\x1cListNamespacePermissionUsers\x12\x37.pomerium.dashboard.ListNamespacePermissionUsersRequest\x1a\x38.pomerium.dashboard.ListNamespacePermissionUsersResponse\x12\x7f\n\x16SetNamespacePermission\x12\x31.pomerium.dashboard.SetNamespacePermissionRequest\x1a\x32.pomerium.dashboard.SetNamespacePermissionResponseB-Z+github.com/pomerium/pomerium-console/pkg/pbb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'namespaces_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z+github.com/pomerium/pomerium-console/pkg/pb'
  _globals['_NAMESPACE']._serialized_start=74
  _globals['_NAMESPACE']._serialized_end=381
  _globals['_DELETENAMESPACEREQUEST']._serialized_start=383
  _globals['_DELETENAMESPACEREQUEST']._serialized_end=419
  _globals['_DELETENAMESPACERESPONSE']._serialized_start=421
  _globals['_DELETENAMESPACERESPONSE']._serialized_end=446
  _globals['_GETNAMESPACEREQUEST']._serialized_start=448
  _globals['_GETNAMESPACEREQUEST']._serialized_end=481
  _globals['_GETNAMESPACERESPONSE']._serialized_start=483
  _globals['_GETNAMESPACERESPONSE']._serialized_end=555
  _globals['_LISTNAMESPACESREQUEST']._serialized_start=557
  _globals['_LISTNAMESPACESREQUEST']._serialized_end=580
  _globals['_LISTNAMESPACESRESPONSE']._serialized_start=582
  _globals['_LISTNAMESPACESRESPONSE']._serialized_end=657
  _globals['_LISTNAMESPACERESOURCESREQUEST']._serialized_start=659
  _globals['_LISTNAMESPACERESOURCESREQUEST']._serialized_end=703
  _globals['_LISTNAMESPACERESOURCESRESPONSE']._serialized_start=706
  _globals['_LISTNAMESPACERESOURCESRESPONSE']._serialized_end=870
  _globals['_LISTNAMESPACERESOURCESRESPONSE_RESOURCE']._serialized_start=820
  _globals['_LISTNAMESPACERESOURCESRESPONSE_RESOURCE']._serialized_end=870
  _globals['_SETNAMESPACEREQUEST']._serialized_start=872
  _globals['_SETNAMESPACEREQUEST']._serialized_end=943
  _globals['_SETNAMESPACERESPONSE']._serialized_start=945
  _globals['_SETNAMESPACERESPONSE']._serialized_end=1017
  _globals['_NAMESPACEPERMISSION']._serialized_start=1020
  _globals['_NAMESPACEPERMISSION']._serialized_end=1275
  _globals['_NAMESPACEPERMISSIONGROUP']._serialized_start=1278
  _globals['_NAMESPACEPERMISSIONGROUP']._serialized_end=1446
  _globals['_NAMESPACEPERMISSIONUSER']._serialized_start=1449
  _globals['_NAMESPACEPERMISSIONUSER']._serialized_end=1632
  _globals['_DELETENAMESPACEPERMISSIONREQUEST']._serialized_start=1634
  _globals['_DELETENAMESPACEPERMISSIONREQUEST']._serialized_end=1680
  _globals['_DELETENAMESPACEPERMISSIONRESPONSE']._serialized_start=1682
  _globals['_DELETENAMESPACEPERMISSIONRESPONSE']._serialized_end=1717
  _globals['_GETNAMESPACEPERMISSIONREQUEST']._serialized_start=1719
  _globals['_GETNAMESPACEPERMISSIONREQUEST']._serialized_end=1762
  _globals['_GETNAMESPACEPERMISSIONRESPONSE']._serialized_start=1764
  _globals['_GETNAMESPACEPERMISSIONRESPONSE']._serialized_end=1867
  _globals['_LISTNAMESPACEPERMISSIONSREQUEST']._serialized_start=1869
  _globals['_LISTNAMESPACEPERMISSIONSREQUEST']._serialized_end=1902
  _globals['_LISTNAMESPACEPERMISSIONSRESPONSE']._serialized_start=1904
  _globals['_LISTNAMESPACEPERMISSIONSRESPONSE']._serialized_end=2010
  _globals['_LISTNAMESPACEPERMISSIONGROUPSREQUEST']._serialized_start=2012
  _globals['_LISTNAMESPACEPERMISSIONGROUPSREQUEST']._serialized_end=2072
  _globals['_LISTNAMESPACEPERMISSIONGROUPSRESPONSE']._serialized_start=2074
  _globals['_LISTNAMESPACEPERMISSIONGROUPSRESPONSE']._serialized_end=2175
  _globals['_LISTNAMESPACEPERMISSIONUSERSREQUEST']._serialized_start=2177
  _globals['_LISTNAMESPACEPERMISSIONUSERSREQUEST']._serialized_end=2236
  _globals['_LISTNAMESPACEPERMISSIONUSERSRESPONSE']._serialized_start=2238
  _globals['_LISTNAMESPACEPERMISSIONUSERSRESPONSE']._serialized_end=2336
  _globals['_SETNAMESPACEPERMISSIONREQUEST']._serialized_start=2338
  _globals['_SETNAMESPACEPERMISSIONREQUEST']._serialized_end=2440
  _globals['_SETNAMESPACEPERMISSIONRESPONSE']._serialized_start=2442
  _globals['_SETNAMESPACEPERMISSIONRESPONSE']._serialized_end=2545
  _globals['_NAMESPACESERVICE']._serialized_start=2548
  _globals['_NAMESPACESERVICE']._serialized_end=3106
  _globals['_NAMESPACEPERMISSIONSERVICE']._serialized_start=3109
  _globals['_NAMESPACEPERMISSIONSERVICE']._serialized_end=3969
# @@protoc_insertion_point(module_scope)
