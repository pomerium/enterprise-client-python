"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.descriptor_pb2
import google.protobuf.internal.extension_dict

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

sensitive: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[google.protobuf.descriptor_pb2.FieldOptions, builtins.bool] = ...
"""Magic number is the 28 most significant bits in the sha256sum of "xds.annotations.v3.sensitive".
When set to true, `sensitive` indicates that this field contains sensitive data, such as
personally identifiable information, passwords, or private keys, and should be redacted for
display by tools aware of this annotation. Note that that this has no effect on standard
Protobuf functions such as `TextFormat::PrintToString`.
"""
