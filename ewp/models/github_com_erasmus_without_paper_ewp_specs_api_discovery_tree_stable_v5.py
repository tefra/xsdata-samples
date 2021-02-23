from dataclasses import dataclass, field
from typing import List, Optional
from ewp.models.github_com_erasmus_without_paper_ewp_specs_api_registry_tree_stable_v1 import (
    ApisImplemented,
    Hei,
)

__NAMESPACE__ = "https://github.com/erasmus-without-paper/ewp-specs-api-discovery/tree/stable-v5"


@dataclass
class Host:
    """Defines a single EWP Host.

    EWP Host defines relationships between HEIs, APIs, server administrators and
    client credentials. One EWP Host defines a single Cartesian product (a "join")
    of all these sets. (E.g. if a client certificate X and a HEI Y is present in
    the same host, then it means that server which signs its requests with X is
    allowed to request resources visible to HEI Y. Similar statement is true for
    every other pair of sets.)

    Most partners will have exactly one `host` entry. However, in some cases you
    might need to describe more than one. For example, when you server covers
    two HEIs, but one of your APIs is available for only one of these two HEIs,
    then it's impossible to describe such relationship with a single Cartesian
    product. You will need to use a sum of at least two Cartesian products. (which
    is expressed by two `host` entries).

    :ivar admin_email: RECOMMENDED element. Address of a developer or
        server administrator who may be contacted in case of problems
        (e.g. invalid Manifest file, invalid certificates, server
        errors, etc.). Multiple addresses may be provided.  Please note,
        that additional `admin-email` elements can also be included
        inside specific APIs sections (this allows you to add extra
        admins to specific APIs without the need of creating extra
        `host` entries).
    :ivar admin_notes: Additional information provided by administrators
        and/or developers of this host for Registry maintainers and
        client developers. Must be provided in English.  E.g. "This host
        is a DEMO server. We plan to keep it online for testing.".
    :ivar apis_implemented:
    :ivar institutions_covered: A list of HEIs (Higher Education
        Institutions) that are covered by this host.  In conjunction
        with `apis-implemented`, enlisting a HEI here indicates that the
        partner wants to receive specific HEI-related API queries
        regarding this HEI, and that it will be able to understand them.
        In conjunction with `client-credentials-in-use`, enlisting a HEI
        here indicates that these credentials can be used to request
        resources "in the name of" this HEI.  Be advised, that the
        Registry Service MAY ignore some (or all) of the items published
        here, for example if it believes that this HEI does not *want*
        to be covered by you. If, for some reason, your items are not
        being imported, and you're not sure why, please contact the
        Registry Service maintainers. You can also take a look at this
        thread: https://github.com/erasmus-without-paper/ewp-specs-api-
        discovery/issues/12
    :ivar client_credentials_in_use: The list of client credentials used
        by this host to make requests to other EWP hosts.  You should
        have this element present if you intend to perform requests
        within the EWP Network. However, it's worth noting, that not
        having it is also valid (if you want your EWP Host to be "server
        only").  Be advised, that the Registry Service MAY ignore some
        (or all) of the credentials submitted here, for example if it
        finds they do not meet proper security standards. If, for some
        reason, your credentials are not being imported, and you're not
        sure why, please contact the Registry Service administrators.
    :ivar server_credentials_in_use: The list of server credentials used
        by this host to authenticate its servers when communicating to
        other EWP hosts. Note, that only *some* methods of server
        authentication make use of these credentials.  As opposed to
        client authentication, the keys used in server authentication
        are bound to specific endpoints (URLs), **not HEIs**. (Remember,
        that some services in EWP are not necessarily bound to any HEI,
        or are bound to multiple HEIs.) This means that - if you create
        multiple manifests - then each of your endpoints MAY use a
        different key for signing its responses. However, in most cases,
        you will want to use only a single key for all your APIs and
        endpoints.  Be advised, that the Registry Service MAY ignore
        some (or all) of the credentials submitted here, for example if
        it finds they do not meet proper security standards. If, for
        some reason, your credentials are not being imported, and you're
        not sure why, please contact the Registry Service
        administrators.
    """
    class Meta:
        name = "host"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-discovery/tree/stable-v5"

    admin_email: List[str] = field(
        default_factory=list,
        metadata={
            "name": "admin-email",
            "type": "Element",
            "namespace": "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd",
            "pattern": r"[^@]+@[^.]+\..+",
        }
    )
    admin_notes: Optional[str] = field(
        default=None,
        metadata={
            "name": "admin-notes",
            "type": "Element",
            "namespace": "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd",
        }
    )
    apis_implemented: Optional[ApisImplemented] = field(
        default=None,
        metadata={
            "name": "apis-implemented",
            "type": "Element",
            "namespace": "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1",
        }
    )
    institutions_covered: Optional["Host.InstitutionsCovered"] = field(
        default=None,
        metadata={
            "name": "institutions-covered",
            "type": "Element",
        }
    )
    client_credentials_in_use: Optional["Host.ClientCredentialsInUse"] = field(
        default=None,
        metadata={
            "name": "client-credentials-in-use",
            "type": "Element",
        }
    )
    server_credentials_in_use: Optional["Host.ServerCredentialsInUse"] = field(
        default=None,
        metadata={
            "name": "server-credentials-in-use",
            "type": "Element",
        }
    )

    @dataclass
    class InstitutionsCovered:
        hei: List[Hei] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1",
            }
        )

    @dataclass
    class ClientCredentialsInUse:
        """
        :ivar certificate: Base64-encoded X.509 certificate used by the
            partner for TLS Client Authentication, as described here:
            https://github.com/erasmus-without-paper/ewp-specs-sec-
            cliauth-tlscert  If your private key is compromised, you
            MUST immediately remove all certificates based on this key
            from your manifest.
        :ivar rsa_public_key: Base64-encoded RSA public key used by the
            partner for HTTP Signature Client Authentication, as
            described here:  https://github.com/erasmus-without-
            paper/ewp-specs-sec-cliauth-httpsig  If your private key is
            compromised, you MUST immediately remove all public keys
            related to this key from your manifest.
        """
        certificate: List[bytes] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "format": "base64",
            }
        )
        rsa_public_key: List[bytes] = field(
            default_factory=list,
            metadata={
                "name": "rsa-public-key",
                "type": "Element",
                "format": "base64",
            }
        )

    @dataclass
    class ServerCredentialsInUse:
        """
        :ivar rsa_public_key: Base64-encoded RSA public key used by the
            partner for HTTP Signature Server Authentication, as
            described here:  https://github.com/erasmus-without-
            paper/ewp-specs-sec-cliauth-httpsig  If your private key is
            compromised, you MUST immediately remove all public keys
            related to this key from your manifest.
        """
        rsa_public_key: List[bytes] = field(
            default_factory=list,
            metadata={
                "name": "rsa-public-key",
                "type": "Element",
                "format": "base64",
            }
        )


@dataclass
class Manifest:
    """EWP Discovery Manifest.

    Manifest files describe a set of EWP Hosts. Manifest files are
    usually read by the EWP Registry Service only.

    :ivar host: One v5 manifest file can describe multiple EWP Hosts
        (this is the primary difference between v4 and v5 of Discovery
        API).
    """
    class Meta:
        name = "manifest"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-discovery/tree/stable-v5"

    host: List[Host] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
