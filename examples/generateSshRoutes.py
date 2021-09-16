#!/usr/bin/env python

import os
import io
import re
import yaml #pip install pyyaml
from pomerium.client import Client
from pomerium.pb.policy_pb2 import ListPoliciesRequest
from pomerium.pb.namespaces_pb2 import ListNamespacesRequest
from pomerium.pb.routes_pb2 import SetRouteRequest, Route

##########################################################################################
# User-specific variables can be set as environment variables or defined as static vars. #
##########################################################################################

# sa contains the service account JWT
sa = os.getenv('SERVICE_ACCOUNT', '')

# console_api matches the route to the console API ("From")
console_api = 'console-api.localhost.pomerium.io'

# If your Pomerium proxy uses an untrusted certificate, specify the CA cert as an environment variable
# ca_cert = os.getenv('CA_CERT', '').encode('utf-8')

# If you specify a ca_cert, include it when defining the client
#client = Client(console_api, sa, root_certificates=ca_cert)
client = Client(console_api, sa)


####################
# Helper functions #
####################

# Function stripHost to strip subdomain from items in hosts list:
# Expects input of 'host', i.e. foo.local.domain:22
# Returns a string of 'host' up to but not including the first '.'
def stripHost(host):
    hostname = re.search("[^.]*", host)
    if hostname is not None:
        return hostname.group(0)

# Function stripPort to strip the port from items in hosts list:
# Expects input of 'host', i.e. foo.local.domain
# Returns a string of 'hosts after but not including the ':'
def stripPort(host):
    port = re.search("(?:.(?!\:))+$", host)
    if port is not None:
        return port.group(0)

# Function getNS expects an input of 'name' and returns a dictionary object for
# the Namespace with a matching name:
def getNS(name):
    resp = client.NamespaceService.ListNamespaces(ListNamespacesRequest())
    ns = [n for n in resp.namespaces if n.name == name][0]
    return ns

# Function getPol expects and list input of policy names and a namespace object.
# It returns an array of the matching policies by name:
def getPols(policies, ns):
    thesePols = []
    for x in policies:
        resp = client.PolicyService.ListPolicies(
            ListPoliciesRequest(query=x, namespace=ns.id)
        )
        thesePols.append(resp.policies[0])
    return thesePols


#################
# Main function #
#################

def main():
    # Read the file specifying the routes to create.
    with io.open('example-ssh-routes.yaml', 'r') as file:
        data_routes = yaml.safe_load(file)
    #print(data_routes["namespaces"][0]["name"]) # For Debugging

    for namespace in data_routes["namespaces"]:
        ns = getNS(namespace["name"])
        print('In Namespace "' + ns.name + '" ('+ ns.id +'):')
        policies = getPols(namespace["policies", ns])
        print('With policies:')
        for policy in policies:
            print('  ' + policy.name)
        hosts = namespace["hosts"]
        for host in hosts:
            route = Route(**{
                'namespace_id': ns.id,
                'name': stripHost(host),
                'from': 'tcp+https://' + stripHost(host) + '.localhost.pomerium.io' + stripPort(host), #Change the last string to your domain space
                'to': ['tcp://' + host],
                'policy_ids': [str(policies)],
                'pass_identity_headers': True,
            })
            resp = client.RouteService.SetRoute(SetRouteRequest(route=route))
            print(resp)

main()