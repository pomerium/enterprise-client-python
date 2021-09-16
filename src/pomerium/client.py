import grpc
from pomerium.pb.activity_log_pb2_grpc import ActivityLogServiceStub
from pomerium.pb.key_chain_pb2_grpc import KeyChainServiceStub
from pomerium.pb.namespaces_pb2_grpc import NamespacePermissionServiceStub
from pomerium.pb.namespaces_pb2_grpc import NamespaceServiceStub
from pomerium.pb.policy_pb2_grpc import PolicyServiceStub
from pomerium.pb.routes_pb2_grpc import RouteServiceStub
from pomerium.pb.users_pb2_grpc import PomeriumServiceAccountServiceStub
from pomerium.pb.users_pb2_grpc import PomeriumSessionServiceStub
from pomerium.pb.settings_pb2_grpc import SettingsServiceStub
from pomerium.pb.users_pb2_grpc import UserServiceStub


def authorize_header(auth_token) -> str:
    """create a properly formatted `authorization` header for Pomerium
    Args:
        auth_token: string format service account credentials
    """
    return 'Pomerium ' + auth_token


class AuthMetadataPlugin(grpc.AuthMetadataPlugin):
    """AuthMetadataPlugin implements a grpc.AuthMetadataPlugin to provide pomerium credentials for each request
    """

    def __init__(self, auth_token):
        self._authorization_header = (
            'authorization', authorize_header(auth_token)
        )

    def __call__(self, context, callback):
        callback((self._authorization_header,), None)


def _dial(target: str, auth_token: str, root_certificates: bytes = None, private_key: bytes = None, certificate_chain: bytes = None, options: "list[tuple[str, str]]" = None):
    return grpc.secure_channel(target, grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(root_certificates=root_certificates,
                                     private_key=private_key, certificate_chain=certificate_chain),
        grpc.metadata_call_credentials(
            AuthMetadataPlugin(auth_token)
        )
    ), options=options)


class Client(object):
    """Client provides the top level interface to Pomerium API methods
    """

    def __init__(self, target: str, auth_token: str, root_certificates: bytes = None, private_key: bytes = None, certificate_chain: bytes = None, options: "list[tuple[str, str]]" = None):
        """Construct a new Client with a connection to the Pomerium API
        Args:
            target: "hostname:port" of pomerium console endpoint
            auth_token: string format service account credentials
            root_certificates: PEM encoded root certificates to use for validating the target TLS connection
            private_key: PEM encoded client TLS key for authentication to the target
            certificate_chain: PEM encoded TLS certificate chain to present when connecting to target
            options: An optional list of key-value pairs (channel arguments <https://grpc.github.io/grpc/python/glossary.html#term-channel_arguments>) to configure the underlying grpc channel
        """

        self.channel = _dial(target, auth_token,
                             root_certificates, private_key, certificate_chain, options)

        self.ActivityLogService = ActivityLogServiceStub(self.channel)
        self.KeyChainService = KeyChainServiceStub(self.channel)
        self.NamespacePermissionService = NamespacePermissionServiceStub(
            self.channel)
        self.NamespaceService = NamespaceServiceStub(self.channel)
        self.PolicyService = PolicyServiceStub(self.channel)
        self.PomeriumServiceAccountService = PomeriumServiceAccountServiceStub(
            self.channel)
        self.PomeriumSessionService = PomeriumSessionServiceStub(self.channel)
        self.RouteService = RouteServiceStub(self.channel)
        self.SettingsService = SettingsServiceStub(self.channel)
        self.UserService = UserServiceStub(self.channel)
