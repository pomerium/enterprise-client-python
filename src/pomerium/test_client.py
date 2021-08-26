from src.pomerium.client import authorize_header
from src.pomerium.pb import namespaces_pb2, namespaces_pb2_grpc
import unittest

import grpc
import client
from concurrent import futures
import pb.namespaces_pb2_grpc as namespaces_pb2_grpc


class TestAuthMetadataPlugin(unittest.TestCase):
    def test_callback(self):
        token = "mysecrettoken"

        def mock_callback(metadata, error):
            self.assertEqual(
                (('authorization', client.authorize_header(token)),), metadata)

        client.AuthMetadataPlugin(token).__call__(None, mock_callback)


class TestClient(unittest.TestCase):
    token = "mysecrettoken"

    cert_string = """
-----BEGIN CERTIFICATE-----
MIICwzCCAaugAwIBAgIJAL2UgVvqvbc8MA0GCSqGSIb3DQEBBQUAMBQxEjAQBgNV
BAMTCWxvY2FsaG9zdDAeFw0yMTA4MjMyMjE4NDJaFw0zMTA4MjEyMjE4NDJaMBQx
EjAQBgNVBAMTCWxvY2FsaG9zdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC
ggEBAKvFD5mTTdU0AjL9a7VMNR/w20qdH391KKJVUaSA30SGLmLwcms5tHLgmIys
z6IWWR8k0h84AS3SOgubZtrk7laNuKoCDnyFlD4kxP2oRWlImK7LScYuozhb5GjC
N+4VfTU/SWFzaHFNxqpEcq6mkFzEdO7XXJtxQxV5tdINhRbSZgB9rjycM4lXLgFC
SucnGghvoU5oRfFdk9LUP78t5S6KVkLouFQeAfwimzrR8xPpOUKarBK0GkgsEi3g
xMTW0vVpwuYKVxMzwtHanz65G6FZMGWXKIt+K2ahTu87mJhkrBKDa/7ZgqyRdErY
arO8G4b9qg0Nc2TDcq4V7qspjtcCAwEAAaMYMBYwFAYDVR0RBA0wC4IJbG9jYWxo
b3N0MA0GCSqGSIb3DQEBBQUAA4IBAQBIj3t3E7L03U4gAIgRaTcakN8fj9Xg+oBC
ndYVqEXrnRauw2mZ8W3P4CqQ0FOtdfekvw+d+LZuvrESt+VjXJ86rLZEI5YtF/Nc
D/ve7j20qb0Gp6O9+9tSiTx6cYlS0hp9iqJ5zsCBrqCDNjsKI2TkK8reqiaY+BJq
8xZUgjj0hlOmeU1GUuQ9jhX1S8XsSZUQrERx0VRN0iulVKB+Skaeb/dDRpeVCN0S
GH5OmTydb9yAi/6bldcjwl74Y7qRx+pN9re2zJ/avNfx0pfL8SB9IYCrsUmvcyIS
h3H+sEJSodq22AdNC4Lpo4DU1eMiePh+ks3WLotEi2jaYe5woOIZ
-----END CERTIFICATE-----
"""

    key_string = """
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAq8UPmZNN1TQCMv1rtUw1H/DbSp0ff3UoolVRpIDfRIYuYvBy
azm0cuCYjKzPohZZHyTSHzgBLdI6C5tm2uTuVo24qgIOfIWUPiTE/ahFaUiYrstJ
xi6jOFvkaMI37hV9NT9JYXNocU3GqkRyrqaQXMR07tdcm3FDFXm10g2FFtJmAH2u
PJwziVcuAUJK5ycaCG+hTmhF8V2T0tQ/vy3lLopWQui4VB4B/CKbOtHzE+k5Qpqs
ErQaSCwSLeDExNbS9WnC5gpXEzPC0dqfPrkboVkwZZcoi34rZqFO7zuYmGSsEoNr
/tmCrJF0Sthqs7wbhv2qDQ1zZMNyrhXuqymO1wIDAQABAoIBADlw4NKeq/yMM+AR
Vx99qJZR2UOOX6Yj6769gVvdrMwhgwmbFug8l9eCvADvGVA+4PbFPW8rL1m/X6Ha
Cf9RZ1KSehqALY/+q6BMc4PP7cZTfJuXZ8haeEK0mCFgMYvwq7pOu59XFKovNCxk
T2WQVd5v5Bqq8lEZAzH/TYo88zC6Bw8CXt4BZjEAK0+Nqk9lLKvEI4GfHlya4ean
q1m7iJsDEawqouaSV1NI/AlwvZOyi7F0MGbgFz/uzjp8hRKafXLY3/yc7kL0tX3X
GXRGC9bZjDhg+klCs158yZ55XQOQ0rP3KavzMjXv3PNQj7ymT2Ar6n8ZZQimqWcV
GbdWC4ECgYEA1vwY8P+iXqVQU3BrorOdHAWg4Q6hubpVr+Bd/taUbwy4AmDPrMH2
NQH2skI/OFrAo1FIbQ0s7TQmg6gr+tCYMCo7HnwnSw2Xj1qIEuE/6cfrsQYGUF6B
iDOKg511BynB+wxFLpL2CzhQtMb0vhMoR+jRExEPydh4UxkVte8okbECgYEAzIpV
iDPEqFW5nZgpqd75kWnq7xez274AYqTtv+8zV69mD30H0KNV2Sc1rulg+t65HBY8
B9oFuedUZr7FSZ0oEVOiq9NJAvV0qtzMvUrWII0Qkx1wA16Aq/hDClvJVK4ok1h0
j4aOxxrkhzj5LaoVz+XPZCkIsATMPn4rnmaAgwcCgYEAkgCLf8BcqSJkNwZ2Uvzg
ihNYev/Q3a2qW9NogpWAIRrmLNdKsuzXJJC81bsf7EnV4hRlt4nnJQDx1x/zHldj
w/IqTD3NAa+tanH1T70iBsb7TjHlP9eu6Kz4OQJKZB772l8u7L5p0pzgUqV7uUqR
ZKS8uNIxgsc8kFLM584QI0ECgYBDCfQOuCj0o2Q66ux86MATkQuXYcVpeFTYAAaM
qfHCA5MH8IrnLyGsEtXdhlBq6STyt7blO+g0jkVzh4NSJVhElYzzlESR27FpbwUL
5cNY1+Ne1H8qG4dA1hXjB0JtpsdVw+AwSoHxcDcGuv2wodaUVVYsFebrCieHNANH
34CvcQKBgH7djIKcZQPdZNwYx7lQ69FGnQT0vkuBkhb7Wkx9T9kTI0FVdgaYdA9q
NPB8t/A+WbZMFsZ29JSU6KcjJS990bQufDe3hhTNWxovQOY8Ahvs7qU1YXmXnwn2
lfUb3y6WiE9eXteemVbD6f1xYL8PP+eRTKt93Cmnvp4IZ/Nh7umS
-----END RSA PRIVATE KEY-----
"""

    class MockNamespaceServiceServicer(namespaces_pb2_grpc.NamespaceServiceServicer):
        def __init__(self) -> None:
            super().__init__()
            self.authorization_header = ""

        def ListNamespaces(self, request, context):
            metadata = dict(context.invocation_metadata())
            self.authorization_header = metadata['authorization']
            return namespaces_pb2.ListNamespacePermissionGroupsResponse()

    def setUp(self) -> None:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
        port = server.add_secure_port(
            "localhost:0",
            grpc.ssl_server_credentials(
                [(self.key_string.encode('utf-8'), self.cert_string.encode('utf-8'))],
            )
        )

        self.server = server
        self.port = port

    def tearDown(self) -> None:
        self.server.stop(None)

    def test_list_namespaces_metadata(self):
        mockService = self.MockNamespaceServiceServicer()
        namespaces_pb2_grpc.add_NamespaceServiceServicer_to_server(
            mockService, self.server)

        self.server.start()

        c = client.Client("localhost:" + str(self.port),
                          self.token, self.cert_string.encode('utf-8'))
        c.NamespaceService.ListNamespaces(
            namespaces_pb2.ListNamespacesRequest())

        self.assertEqual(mockService.authorization_header,
                         authorize_header(self.token))
