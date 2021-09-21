#!/usr/bin/env python

import os
from pomerium.client import Client
from pomerium.pb.policy_pb2 import ListPoliciesRequest
from pomerium.pb.namespaces_pb2 import ListNamespacesRequest
from pomerium.pb.routes_pb2 import SetRouteRequest, Route

# get custom CA and service account credentials from environment
ca_cert = os.getenv('CA_CERT', '').encode('utf-8')
sa = os.getenv('SERVICE_ACCOUNT', '')
console_api = 'console-api.localhost.pomerium.io'

client = Client(console_api, sa, root_certificates=ca_cert)

# get id for namespace 'Production'
resp = client.NamespaceService.ListNamespaces(ListNamespacesRequest())
ns = [n for n in resp.namespaces if n.name == 'Production'][0]

# find policy named 'my policy' in namespace 'Production'
resp = client.PolicyService.ListPolicies(
    ListPoliciesRequest(query='my policy', namespace=ns.id)
)
policy = resp.policies[0]

# set route in namespace 'Production', associated to 'my policy'
route = Route(**{
    'namespace_id': ns.id,
    'name': 'my route',
    'from': 'https://test.localhost.pomerium.io',
    'to': ['https://verify.pomerium.com'],
    'policy_ids': [policy.id],
    'pass_identity_headers': True,
})

resp = client.RouteService.SetRoute(SetRouteRequest(route=route))
print(resp)
