from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from ewp.models.github_com_erasmus_without_paper_ewp_specs_architecture_blob_stable_v1_common_types import StringWithOptionalLang

__NAMESPACE__ = "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1"


class OtherHeiIdValue(Enum):
    """
    :cvar PREVIOUS_SCHAC: A previously used SCHAC identifier. Servers
        MUST provide all SCHAC identifiers their HEI have used in the
        past.  https://github.com/erasmus-without-paper/ewp-specs-api-
        discovery/issues/4
    :cvar PIC: PIC identifier.
        https://ec.europa.eu/research/participants/portal/desktop/en/organisations/register.html
    :cvar ERASMUS: Erasmus institutional code.
    :cvar EUC: DEPRECATED, use "erasmus-charter" instead. Erasmus
        University Charter number (aka EUC number).  - Newer clients
        SHOULD treat this as an alias for "erasmus-charter" (for
        backward compatibility).  - Servers MAY still publish "euc"
        identifiers in their manifests. They also MAY   decide not to
        publish any "euc" identifiers, and only publish   "erasmus-
        charter" identifiers.  - If the server decides to publish "euc"
        identifiers, it still SHOULD NOT   publish newer Erasmus Charter
        numbers (such as ECHE numbers) under the "euc"   identifier
        type. It is RECOMMENDED to publish them via "erasmus-charter"
        instead, to avoid confusion.  See this thread:
        https://github.com/erasmus-without-paper/ewp-specs-api-
        registry/issues/3
    :cvar ERASMUS_CHARTER: Erasmus Charter number (EUC/ECHE/etc.)  This
        MAY contain both EUC numbers (Erasmus University Charter) or
        ECHE numbers (Erasmus Charter for Higher Education). In the
        future, it also MAY contain other similar identifiers, if the
        European Commission decides to replace ECHE numbers with such.
    """
    PREVIOUS_SCHAC = "previous-schac"
    PIC = "pic"
    ERASMUS = "erasmus"
    EUC = "euc"
    ERASMUS_CHARTER = "erasmus-charter"


@dataclass
class ApisImplemented:
    """This section describes all APIs implemented by a particular EWP host.

    Please note, that each API can be implemented a multiple number of times.
    Usually, you will have only a single entry for each of your APIs, but there are
    some use cases when serving two or more different versions of the same API is
    desirable. More background and discussion here:
    https://github.com/erasmus-without-paper/ewp-specs-architecture/issues/6

    :ivar other_element: Manifest entries for each of the APIs are
        defined in separate schemas, within repositories describing
        these APIs (usually in a file named `manifest-entry.xsd`).  We
        encourage you to include non-EWP-related APIs too, if you think
        that other partners in the EWP Network might make use of them!
        It is RECOMMENDED (but NOT strictly required) that all such API
        descriptions extend the `ApiEntry` complexType defined in
        common-types.xsd schema:  https://github.com/erasmus-without-
        paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd
    """
    class Meta:
        name = "apis-implemented"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )


@dataclass
class OtherHeiId:
    """
    :ivar value:
    :ivar type: HEI identifier type. It is advised to use the types
        provided in the enumeration (case sensitive), but custom
        identifier types are also allowed.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    type: Optional[OtherHeiIdValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Hei:
    """Briefly describes a single Higher Education Institution (HEI).

    These elements are listed in the Registry Service's cataloge, in
    order to allow the clients to identify all the HEIs by various types
    of identifiers.

    :ivar other_id: SCHAC identifier (provided in the `id` attribute
        described below) is the primary HEI identifier, but manifest
        authors are encouraged to provide all identifiers they can think
        of. (Otherwise, other EWP Hosts may not be able to recognize
        their HEIs.)  Note that there can be multiple IDs given, even
        within a single type. This won't happen often, but you should be
        aware of this. It is safer for the Registry to include both
        conflicting values (as they were found in the manifest files),
        than pick one at random.
    :ivar name: The name of the institution. Multiple values may be
        provided, and in multiple languages.  Note that there can be
        multiple names given even *for the same language*. This won't
        happen often, but you should be aware of this. It is safer for
        the Registry to include both such conflicting values (as they
        were found in the manifest files), than pick one at random.
    :ivar id: SCHAC identifier of this HEI. As described in the SCHAC
        documentation for the "schacHomeOrganization" element (e.g.
        "uw.edu.pl").  This attribute is REQUIRED. Manifest authors need
        to acquire a proper SCHAC identifier for all HEIs they intend to
        add to their manifest (acquiring them manually is usually quite
        simple).
    """
    class Meta:
        name = "hei"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1"

    other_id: List[OtherHeiId] = field(
        default_factory=list,
        metadata={
            "name": "other-id",
            "type": "Element",
        }
    )
    name: List[StringWithOptionalLang] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Catalogue:
    """The EWP Registry catalogue response.

    Most of the data published here is copied from the hosts' manifests,
    but the data is additionally verified (and portions of it may be
    modified, removed or transformed). The format is somewhat similar to
    the format of the manifest files, but different in places.

    :ivar host: This element describes a single EWP Host.
    :ivar institutions: The list of institutions referenced in the
        `host` sections above.  The list is using the Manifest's XML
        namespace, but the actual data MAY come from other sources too.
    :ivar binaries: This elements keeps a map of binaries.  Each binary
        object on this list is identified by its own SHA-256 digest.
        Note, that is would be possible for the Registry Service to
        simply include the actual binary content wherever it is referred
        to, but this would mean that the content might be duplicated
        many times, in many different elements (e.g. when a partner uses
        the same RSA key-pair in many of its hosts). In order to avoid
        that (and reduce the size of the catalogue response), we publish
        these elements in an entirely separate `binaries` section.
    """
    class Meta:
        name = "catalogue"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1"

    host: List["Catalogue.Host"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    institutions: Optional["Catalogue.Institutions"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    binaries: Optional["Catalogue.Binaries"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Host:
        """
        :ivar admin_email:
        :ivar admin_notes:
        :ivar apis_implemented:
        :ivar institutions_covered: A list of HEIs (Higher Education
            Institutions) covered by this host. The hosts states that
            all of its implemented institution-related APIs will be able
            to understand requests regarding all institutions listed
            here.  IMPORTANT: A single institution can be covered by
            multiple hosts. E.g. If you are looking for a particular API
            implementation for a particular institution, then you MUST
            use both of these selectors in your XPath query. Also, keep
            in mind, that a single API may be served in multiple
            versions, as described here: https://github.com/erasmus-
            without-paper/ewp-specs-architecture/issues/6.  Note, that
            this element is not the same element as the one used in the
            Discovery Manifest API (it has the same name, but a
            different namespace and contents).
        :ivar client_credentials_in_use: A list of client credentials
            used by this host to make requests to other EWP hosts in the
            name of all of the covered institutions.  Note, that this
            element is not the same element as the one used in the
            Discovery Manifest API (it has the same name, but a
            different namespace and contents).
        :ivar server_credentials_in_use: A list of credentials used by
            this host's server endpoints (URLs) for authenticating
            themselves. Note, that only *some* methods of server
            authentication make use of these credentials.  As opposed to
            client authentication, the keys used in server
            authentication are bound to specific endpoints (URLs), **not
            HEIs**. Clients can make use of these credentials for
            authenticating the servers when connecting to any of the
            APIs implemented by this host (in the `../apis-implemented`
            element).  Note, that this element is not the same element
            as the one used in the Discovery Manifest API (it has the
            same name, but a different namespace and contents).
        """
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
            }
        )
        institutions_covered: Optional["Catalogue.Host.InstitutionsCovered"] = field(
            default=None,
            metadata={
                "name": "institutions-covered",
                "type": "Element",
            }
        )
        client_credentials_in_use: Optional["Catalogue.Host.ClientCredentialsInUse"] = field(
            default=None,
            metadata={
                "name": "client-credentials-in-use",
                "type": "Element",
            }
        )
        server_credentials_in_use: Optional["Catalogue.Host.ServerCredentialsInUse"] = field(
            default=None,
            metadata={
                "name": "server-credentials-in-use",
                "type": "Element",
            }
        )

        @dataclass
        class InstitutionsCovered:
            """
            :ivar hei_id: SCHAC identifier of the HEI. If you don't use
                SCHAC identifiers, you will probably need to use the
                attached mapping (see `institutions` element described
                below).
            """
            hei_id: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "hei-id",
                    "type": "Element",
                }
            )

        @dataclass
        class ClientCredentialsInUse:
            """
            :ivar certificate: Identifies a client certificate with
                which the client has been allowed to make requests
                within the network using the TLS Client Certificate
                Authentication described here:
                https://github.com/erasmus-without-paper/ewp-specs-sec-
                cliauth-tlscert  The client which signs his
                communication with the private key matching this
                certificate is allowed to make requests in the name of
                the institutions listed in the adjacent `institutions-
                covered` element.  Note, that the Registry does NOT
                serve the actual certificate. Servers MUST use the
                `sha-256` attribute to match certificates the client
                actually uses.
            :ivar rsa_public_key: Identifies an RSA key-pair which has
                been allowed to make requests within the network using
                the HTTP Signature Client Authentication described here:
                https://github.com/erasmus-without-paper/ewp-specs-sec-
                cliauth-httpsig  The client who is in possession of the
                private part of this key is allowed to make requests in
                the name of the institutions listed in the adjacent
                `institutions-covered` element.  Please note, that the
                Registry also serves the *actual content* of the public
                part for this key-pair, but this content is not included
                here. Instead, you can look up it's SHA-256 digest in
                the `binaries` section below.
            """
            certificate: List["Catalogue.Host.ClientCredentialsInUse.Certificate"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                }
            )
            rsa_public_key: List["Catalogue.Host.ClientCredentialsInUse.RsaPublicKey"] = field(
                default_factory=list,
                metadata={
                    "name": "rsa-public-key",
                    "type": "Element",
                }
            )

            @dataclass
            class Certificate:
                """
                :ivar sha_256: Certificate's SHA-256 digest (in HEX).
                """
                sha_256: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "sha-256",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9a-f]{64}",
                    }
                )

            @dataclass
            class RsaPublicKey:
                """
                :ivar sha_256: Public key's SHA-256 digest (in HEX).
                """
                sha_256: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "sha-256",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9a-f]{64}",
                    }
                )

        @dataclass
        class ServerCredentialsInUse:
            """
            :ivar rsa_public_key: Identifies an RSA key-pair which has
                been allowed to be used to sign HTTP responses from APIs
                listed in the `../apis-implemented` element, as part of
                the HTTP Signature Server Authentication described here:
                https://github.com/erasmus-without-paper/ewp-specs-sec-
                cliauth-httpsig  Clients which intend to authenticate
                the server behind the URL X via this method, MUST verify
                if the response is signed with *any* of the keys
                supplied here. The list of valid keys MUST be extracted
                only from the single `host` entry being the parent of
                the element in the URL X has been discovered - the
                client MUST NOT treat keys found in other hosts as
                valid, even if these hosts claim to serve their APIs at
                the same URL as X.  Please note, that the Registry also
                serves the *actual content* of the public part for this
                key-pair, but this content is not included here.
                Instead, you can look up it's SHA-256 digest in the
                `binaries` section below.
            """
            rsa_public_key: List["Catalogue.Host.ServerCredentialsInUse.RsaPublicKey"] = field(
                default_factory=list,
                metadata={
                    "name": "rsa-public-key",
                    "type": "Element",
                }
            )

            @dataclass
            class RsaPublicKey:
                """
                :ivar sha_256: Public key's SHA-256 digest (in HEX).
                """
                sha_256: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "sha-256",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9a-f]{64}",
                    }
                )

    @dataclass
    class Institutions:
        hei: List[Hei] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )

    @dataclass
    class Binaries:
        """
        :ivar rsa_public_key: Contains base64-encoded binary content of
            RSA public key.
        """
        rsa_public_key: List["Catalogue.Binaries.RsaPublicKey"] = field(
            default_factory=list,
            metadata={
                "name": "rsa-public-key",
                "type": "Element",
            }
        )

        @dataclass
        class RsaPublicKey:
            """
            :ivar value:
            :ivar sha_256: The SHA-256 digest of the key's binary
                content.  You might have noticed that this is
                information is kind of redundant (because it can be
                evaluated from the content itself). However, the
                Registry publishes it nonetheless (e.g. to reduce the
                work required to perform by the clients, and to make it
                easier for manual matching by humans when debugging
                XML).
            """
            value: Optional[bytes] = field(
                default=None,
                metadata={
                    "required": True,
                    "format": "base64",
                }
            )
            sha_256: Optional[str] = field(
                default=None,
                metadata={
                    "name": "sha-256",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9a-f]{64}",
                }
            )
