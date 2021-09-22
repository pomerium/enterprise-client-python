"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PublicKeyAlgorithm(_PublicKeyAlgorithm, metaclass=_PublicKeyAlgorithmEnumTypeWrapper):
    """PublicKeyAlgorithm is the algorithm of a public key"""
    pass
class _PublicKeyAlgorithm:
    V = typing.NewType('V', builtins.int)
class _PublicKeyAlgorithmEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PublicKeyAlgorithm.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    PKA_UNKNOWN_DO_NOT_USE = PublicKeyAlgorithm.V(0)
    RSA = PublicKeyAlgorithm.V(1)
    DSA = PublicKeyAlgorithm.V(2)
    ECDSA = PublicKeyAlgorithm.V(3)
    ED25519 = PublicKeyAlgorithm.V(4)

PKA_UNKNOWN_DO_NOT_USE = PublicKeyAlgorithm.V(0)
RSA = PublicKeyAlgorithm.V(1)
DSA = PublicKeyAlgorithm.V(2)
ECDSA = PublicKeyAlgorithm.V(3)
ED25519 = PublicKeyAlgorithm.V(4)
global___PublicKeyAlgorithm = PublicKeyAlgorithm


class Format(_Format, metaclass=_FormatEnumTypeWrapper):
    """Format specifies the encoding format of a certificate or key"""
    pass
class _Format:
    V = typing.NewType('V', builtins.int)
class _FormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Format.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    FORMAT_UNDEFINED_DO_NOT_USE = Format.V(0)
    PEM = Format.V(1)

FORMAT_UNDEFINED_DO_NOT_USE = Format.V(0)
PEM = Format.V(1)
global___Format = Format


class KeyPair(google.protobuf.message.Message):
    """KeyPair represents raw Key Pair data for internal usage"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    CERTIFICATE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    name: typing.Text = ...
    namespace_id: typing.Text = ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    certificate: builtins.bytes = ...
    """public certificate data"""

    key: builtins.bytes = ...
    """private key data"""

    def __init__(self,
        *,
        id : typing.Text = ...,
        name : typing.Text = ...,
        namespace_id : typing.Text = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        modified_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        certificate : builtins.bytes = ...,
        key : builtins.bytes = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"created_at",b"created_at",u"modified_at",b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"certificate",b"certificate",u"created_at",b"created_at",u"id",b"id",u"key",b"key",u"modified_at",b"modified_at",u"name",b"name",u"namespace_id",b"namespace_id"]) -> None: ...
global___KeyPair = KeyPair

class KeyUsage(google.protobuf.message.Message):
    """KeyUsage specifies the usage flags set on a signed TLS certificate"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DIGITAL_SIGNATURE_FIELD_NUMBER: builtins.int
    CONTENT_COMMITMENT_FIELD_NUMBER: builtins.int
    KEY_ENCIPHERMENT_FIELD_NUMBER: builtins.int
    DATA_ENCIPHERMENT_FIELD_NUMBER: builtins.int
    KEY_AGREEMENT_FIELD_NUMBER: builtins.int
    CERT_SIGN_FIELD_NUMBER: builtins.int
    CRL_SIGN_FIELD_NUMBER: builtins.int
    ENCIPHER_ONLY_FIELD_NUMBER: builtins.int
    DECIPHER_ONLY_FIELD_NUMBER: builtins.int
    SERVER_AUTH_FIELD_NUMBER: builtins.int
    CLIENT_AUTH_FIELD_NUMBER: builtins.int
    digital_signature: builtins.bool = ...
    """standard key usages"""

    content_commitment: builtins.bool = ...
    key_encipherment: builtins.bool = ...
    data_encipherment: builtins.bool = ...
    key_agreement: builtins.bool = ...
    cert_sign: builtins.bool = ...
    """certificate authority"""

    crl_sign: builtins.bool = ...
    encipher_only: builtins.bool = ...
    decipher_only: builtins.bool = ...
    server_auth: builtins.bool = ...
    """extensions derived from x509.ExtKeyUsage
    server certificate
    """

    client_auth: builtins.bool = ...
    """client certificate"""

    def __init__(self,
        *,
        digital_signature : builtins.bool = ...,
        content_commitment : builtins.bool = ...,
        key_encipherment : builtins.bool = ...,
        data_encipherment : builtins.bool = ...,
        key_agreement : builtins.bool = ...,
        cert_sign : builtins.bool = ...,
        crl_sign : builtins.bool = ...,
        encipher_only : builtins.bool = ...,
        decipher_only : builtins.bool = ...,
        server_auth : builtins.bool = ...,
        client_auth : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cert_sign",b"cert_sign",u"client_auth",b"client_auth",u"content_commitment",b"content_commitment",u"crl_sign",b"crl_sign",u"data_encipherment",b"data_encipherment",u"decipher_only",b"decipher_only",u"digital_signature",b"digital_signature",u"encipher_only",b"encipher_only",u"key_agreement",b"key_agreement",u"key_encipherment",b"key_encipherment",u"server_auth",b"server_auth"]) -> None: ...
global___KeyUsage = KeyUsage

class Name(google.protobuf.message.Message):
    """Name defines the x509 identity"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COUNTRY_FIELD_NUMBER: builtins.int
    ORGANIZATION_FIELD_NUMBER: builtins.int
    ORGANIZATIONAL_UNIT_FIELD_NUMBER: builtins.int
    LOCALITY_FIELD_NUMBER: builtins.int
    PROVINCE_FIELD_NUMBER: builtins.int
    STREET_ADDRESS_FIELD_NUMBER: builtins.int
    POSTAL_CODE_FIELD_NUMBER: builtins.int
    SERIAL_NUMBER_FIELD_NUMBER: builtins.int
    COMMON_NAME_FIELD_NUMBER: builtins.int
    @property
    def country(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def organization(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def organizational_unit(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def locality(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def province(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def street_address(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def postal_code(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    serial_number: typing.Text = ...
    common_name: typing.Text = ...
    def __init__(self,
        *,
        country : typing.Optional[typing.Iterable[typing.Text]] = ...,
        organization : typing.Optional[typing.Iterable[typing.Text]] = ...,
        organizational_unit : typing.Optional[typing.Iterable[typing.Text]] = ...,
        locality : typing.Optional[typing.Iterable[typing.Text]] = ...,
        province : typing.Optional[typing.Iterable[typing.Text]] = ...,
        street_address : typing.Optional[typing.Iterable[typing.Text]] = ...,
        postal_code : typing.Optional[typing.Iterable[typing.Text]] = ...,
        serial_number : typing.Text = ...,
        common_name : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"common_name",b"common_name",u"country",b"country",u"locality",b"locality",u"organization",b"organization",u"organizational_unit",b"organizational_unit",u"postal_code",b"postal_code",u"province",b"province",u"serial_number",b"serial_number",u"street_address",b"street_address"]) -> None: ...
global___Name = Name

class CertificateInfo(google.protobuf.message.Message):
    """CertificateInfo is a .proto reflection of
    https://golang.org/pkg/crypto/x509/#Certificate
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    VERSION_FIELD_NUMBER: builtins.int
    SERIAL_FIELD_NUMBER: builtins.int
    ISSUER_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    NOT_BEFORE_FIELD_NUMBER: builtins.int
    NOT_AFTER_FIELD_NUMBER: builtins.int
    KEY_USAGE_FIELD_NUMBER: builtins.int
    DNS_NAMES_FIELD_NUMBER: builtins.int
    EMAIL_ADDRESSES_FIELD_NUMBER: builtins.int
    IP_ADDRESSES_FIELD_NUMBER: builtins.int
    URIS_FIELD_NUMBER: builtins.int
    PERMITTED_DNS_DOMAINS_CRITICAL_FIELD_NUMBER: builtins.int
    PERMITTED_DNS_DOMAINS_FIELD_NUMBER: builtins.int
    EXCLUDED_DNS_DOMAINS_FIELD_NUMBER: builtins.int
    PERMITTED_IP_RANGES_FIELD_NUMBER: builtins.int
    EXCLUDED_IP_RANGES_FIELD_NUMBER: builtins.int
    PERMITTED_EMAIL_ADDRESSES_FIELD_NUMBER: builtins.int
    EXCLUDED_EMAIL_ADDRESSES_FIELD_NUMBER: builtins.int
    PERMITTED_URI_DOMAINS_FIELD_NUMBER: builtins.int
    EXCLUDED_URI_DOMAINS_FIELD_NUMBER: builtins.int
    version: builtins.int = ...
    serial: typing.Text = ...
    @property
    def issuer(self) -> global___Name: ...
    @property
    def subject(self) -> global___Name: ...
    @property
    def not_before(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def not_after(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def key_usage(self) -> global___KeyUsage: ...
    @property
    def dns_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def email_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def ip_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def uris(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    permitted_dns_domains_critical: builtins.bool = ...
    @property
    def permitted_dns_domains(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def excluded_dns_domains(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def permitted_ip_ranges(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def excluded_ip_ranges(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def permitted_email_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def excluded_email_addresses(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def permitted_uri_domains(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    @property
    def excluded_uri_domains(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        version : builtins.int = ...,
        serial : typing.Text = ...,
        issuer : typing.Optional[global___Name] = ...,
        subject : typing.Optional[global___Name] = ...,
        not_before : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        not_after : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        key_usage : typing.Optional[global___KeyUsage] = ...,
        dns_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        email_addresses : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ip_addresses : typing.Optional[typing.Iterable[typing.Text]] = ...,
        uris : typing.Optional[typing.Iterable[typing.Text]] = ...,
        permitted_dns_domains_critical : builtins.bool = ...,
        permitted_dns_domains : typing.Optional[typing.Iterable[typing.Text]] = ...,
        excluded_dns_domains : typing.Optional[typing.Iterable[typing.Text]] = ...,
        permitted_ip_ranges : typing.Optional[typing.Iterable[typing.Text]] = ...,
        excluded_ip_ranges : typing.Optional[typing.Iterable[typing.Text]] = ...,
        permitted_email_addresses : typing.Optional[typing.Iterable[typing.Text]] = ...,
        excluded_email_addresses : typing.Optional[typing.Iterable[typing.Text]] = ...,
        permitted_uri_domains : typing.Optional[typing.Iterable[typing.Text]] = ...,
        excluded_uri_domains : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"issuer",b"issuer",u"key_usage",b"key_usage",u"not_after",b"not_after",u"not_before",b"not_before",u"subject",b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"dns_names",b"dns_names",u"email_addresses",b"email_addresses",u"excluded_dns_domains",b"excluded_dns_domains",u"excluded_email_addresses",b"excluded_email_addresses",u"excluded_ip_ranges",b"excluded_ip_ranges",u"excluded_uri_domains",b"excluded_uri_domains",u"ip_addresses",b"ip_addresses",u"issuer",b"issuer",u"key_usage",b"key_usage",u"not_after",b"not_after",u"not_before",b"not_before",u"permitted_dns_domains",b"permitted_dns_domains",u"permitted_dns_domains_critical",b"permitted_dns_domains_critical",u"permitted_email_addresses",b"permitted_email_addresses",u"permitted_ip_ranges",b"permitted_ip_ranges",u"permitted_uri_domains",b"permitted_uri_domains",u"serial",b"serial",u"subject",b"subject",u"uris",b"uris",u"version",b"version"]) -> None: ...
global___CertificateInfo = CertificateInfo

class KeyPairRecord(google.protobuf.message.Message):
    """KeyPairRecord provides existing Key Pair metadata"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    CERT_INFO_FIELD_NUMBER: builtins.int
    HAS_PRIVATE_KEY_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    name: typing.Text = ...
    namespace_id: typing.Text = ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """database record creation time"""
        pass
    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """database record modification time"""
        pass
    @property
    def cert_info(self) -> global___CertificateInfo:
        """information about the public certificate"""
        pass
    has_private_key: builtins.bool = ...
    """Key Pair has a private key attached"""

    def __init__(self,
        *,
        id : typing.Text = ...,
        name : typing.Text = ...,
        namespace_id : typing.Text = ...,
        created_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        modified_at : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        cert_info : typing.Optional[global___CertificateInfo] = ...,
        has_private_key : builtins.bool = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"cert_info",b"cert_info",u"created_at",b"created_at",u"modified_at",b"modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cert_info",b"cert_info",u"created_at",b"created_at",u"has_private_key",b"has_private_key",u"id",b"id",u"modified_at",b"modified_at",u"name",b"name",u"namespace_id",b"namespace_id"]) -> None: ...
global___KeyPairRecord = KeyPairRecord

class DeleteKeyPairRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___DeleteKeyPairRequest = DeleteKeyPairRequest

class DeleteKeyPairResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___DeleteKeyPairResponse = DeleteKeyPairResponse

class GetKeyPairRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___GetKeyPairRequest = GetKeyPairRequest

class GetKeyPairResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_PAIR_FIELD_NUMBER: builtins.int
    @property
    def key_pair(self) -> global___KeyPairRecord: ...
    def __init__(self,
        *,
        key_pair : typing.Optional[global___KeyPairRecord] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"key_pair",b"key_pair"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key_pair",b"key_pair"]) -> None: ...
global___GetKeyPairResponse = GetKeyPairResponse

class ListKeyPairsRequest(google.protobuf.message.Message):
    """ListKeyPairsRequest defines the types of key pairs to list"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    namespace_id: typing.Text = ...
    query: typing.Text = ...
    """list Key Pairs whose name contains the query string"""

    offset: builtins.int = ...
    """list Key Pairs starting from an offset in the total list"""

    limit: builtins.int = ...
    """limit the number of entries returned"""

    order_by: typing.Text = ...
    """`newest`, `oldest`, `name`, `from`"""

    def __init__(self,
        *,
        namespace_id : typing.Text = ...,
        query : typing.Text = ...,
        offset : builtins.int = ...,
        limit : builtins.int = ...,
        order_by : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"_limit",b"_limit",u"_offset",b"_offset",u"_order_by",b"_order_by",u"_query",b"_query",u"limit",b"limit",u"offset",b"offset",u"order_by",b"order_by",u"query",b"query"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"_limit",b"_limit",u"_offset",b"_offset",u"_order_by",b"_order_by",u"_query",b"_query",u"limit",b"limit",u"namespace_id",b"namespace_id",u"offset",b"offset",u"order_by",b"order_by",u"query",b"query"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_limit",b"_limit"]) -> typing.Optional[typing_extensions.Literal["limit"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_offset",b"_offset"]) -> typing.Optional[typing_extensions.Literal["offset"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_order_by",b"_order_by"]) -> typing.Optional[typing_extensions.Literal["order_by"]]: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"_query",b"_query"]) -> typing.Optional[typing_extensions.Literal["query"]]: ...
global___ListKeyPairsRequest = ListKeyPairsRequest

class ListKeyPairsResponse(google.protobuf.message.Message):
    """ListKeyPairsResponse is the list of Key Pairs found from a
    ListKeyPairsRequest
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_PAIRS_FIELD_NUMBER: builtins.int
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    @property
    def key_pairs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KeyPairRecord]:
        """Key Pairs found"""
        pass
    total_count: builtins.int = ...
    def __init__(self,
        *,
        key_pairs : typing.Optional[typing.Iterable[global___KeyPairRecord]] = ...,
        total_count : builtins.int = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key_pairs",b"key_pairs",u"total_count",b"total_count"]) -> None: ...
global___ListKeyPairsResponse = ListKeyPairsResponse

class CreateKeyPairRequest(google.protobuf.message.Message):
    """CreateKeyPairRequest defines a Key Pair to create"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    NAMESPACE_ID_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    CERTIFICATE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    namespace_id: typing.Text = ...
    format: global___Format.V = ...
    """encoding format of data"""

    certificate: builtins.bytes = ...
    """public certificate data"""

    key: builtins.bytes = ...
    """private key data"""

    def __init__(self,
        *,
        name : typing.Text = ...,
        namespace_id : typing.Text = ...,
        format : global___Format.V = ...,
        certificate : builtins.bytes = ...,
        key : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"certificate",b"certificate",u"format",b"format",u"key",b"key",u"name",b"name",u"namespace_id",b"namespace_id"]) -> None: ...
global___CreateKeyPairRequest = CreateKeyPairRequest

class CreateKeyPairResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_PAIR_FIELD_NUMBER: builtins.int
    @property
    def key_pair(self) -> global___KeyPairRecord: ...
    def __init__(self,
        *,
        key_pair : typing.Optional[global___KeyPairRecord] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"key_pair",b"key_pair"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key_pair",b"key_pair"]) -> None: ...
global___CreateKeyPairResponse = CreateKeyPairResponse

class UpdateKeyPairRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    FORMAT_FIELD_NUMBER: builtins.int
    CERTIFICATE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    id: typing.Text = ...
    format: global___Format.V = ...
    """encoding format of data"""

    certificate: builtins.bytes = ...
    """public certificate data"""

    key: builtins.bytes = ...
    """private key data"""

    def __init__(self,
        *,
        id : typing.Text = ...,
        format : global___Format.V = ...,
        certificate : builtins.bytes = ...,
        key : builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"certificate",b"certificate",u"format",b"format",u"id",b"id",u"key",b"key"]) -> None: ...
global___UpdateKeyPairRequest = UpdateKeyPairRequest

class UpdateKeyPairResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    KEY_PAIR_FIELD_NUMBER: builtins.int
    @property
    def key_pair(self) -> global___KeyPairRecord: ...
    def __init__(self,
        *,
        key_pair : typing.Optional[global___KeyPairRecord] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"key_pair",b"key_pair"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"key_pair",b"key_pair"]) -> None: ...
global___UpdateKeyPairResponse = UpdateKeyPairResponse
