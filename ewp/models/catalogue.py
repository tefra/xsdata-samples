from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class LangValue(Enum):
    VALUE = ""


class OtherHeiIdValue(Enum):
    """
    :cvar PREVIOUS_SCHAC: A previously used SCHAC identifier. Servers
        MUST provide all SCHAC identifiers their HEI have used in the
        past. https://github.com/erasmus-without-paper/ewp-specs-api-
        discovery/issues/4
    :cvar PIC: PIC identifier.
        https://ec.europa.eu/research/participants/portal/desktop/en/organisations/register.html
    :cvar ERASMUS: Erasmus institutional code.
    :cvar EUC: DEPRECATED, use "erasmus-charter" instead. Erasmus
        University Charter number (aka EUC number). - Newer clients
        SHOULD treat this as an alias for "erasmus-charter" (for
        backward compatibility). - Servers MAY still publish "euc"
        identifiers in their manifests. They also MAY decide not to
        publish any "euc" identifiers, and only publish "erasmus-
        charter" identifiers. - If the server decides to publish "euc"
        identifiers, it still SHOULD NOT publish newer Erasmus Charter
        numbers (such as ECHE numbers) under the "euc" identifier type.
        It is RECOMMENDED to publish them via "erasmus-charter" instead,
        to avoid confusion. See this thread: https://github.com/erasmus-
        without-paper/ewp-specs-api-registry/issues/3
    :cvar ERASMUS_CHARTER: Erasmus Charter number (EUC/ECHE/etc.) This
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
    """
    This section describes all APIs implemented by a particular EWP host.

    Please note, that each API can be implemented a multiple number of
    times. Usually, you will have only a single entry for each of your
    APIs, but there are some use cases when serving two or more different
    versions of the same API is desirable. More background and discussion
    here:
    https://github.com/erasmus-without-paper/ewp-specs-architecture/issues/6.

    :ivar other_element: Manifest entries for each of the APIs are
        defined in separate schemas, within repositories describing
        these APIs (usually in a file named `manifest-entry.xsd`). We
        encourage you to include non-EWP-related APIs too, if you think
        that other partners in the EWP Network might make use of them!
        It is RECOMMENDED (but NOT strictly required) that all such API
        descriptions extend the `ApiEntry` complexType defined in
        common-types.xsd schema: https://github.com/erasmus-without-
        paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd
    """

    class Meta:
        name = "apis-implemented"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1"

    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )


@dataclass
class Empty:
    """
    Just a reusable empty element type, with no content nor attributes.

    See: http://stackoverflow.com/questions/20751782/.
    """

    class Meta:
        target_namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"


@dataclass
class MultilineString:
    """
    This is very similar to a regular xs:string, but whenever this type is
    used it indicates that the content MAY contain basic whitespace
    formatting, such us line breaks and double line breaks (for splitting
    paragraphs).

    The values still MUST be in plaintext though (no HTML is allowed).
    Clients which process data of this type SHOULD respect line breaks when
    they display the data to the end user (e.g. replace CRs and LFs with
    &lt;br&gt;s when rendering to HTML).
    """

    class Meta:
        target_namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class AdminEmail:
    """
    Address of a developer (or server administrator) who may be contacted
    in case of problems.

    This element was placed in the common-types namespace because it is
    being used in multiple schemas throughout the EWP project (most
    notably, various sections of the manifest file).
    """

    class Meta:
        name = "admin-email"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[^@]+@[^.]+\..+",
        },
    )


@dataclass
class OtherHeiId:
    """
    :ivar value:
    :ivar type_value: HEI identifier type. It is advised to use the
        types provided in the enumeration (case sensitive), but custom
        identifier types are also allowed.
    """

    class Meta:
        target_namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    type_value: OtherHeiIdValue | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class HttpwithOptionalLang:
    """
    An absolute URL (might be either HTTP or HTTPS) with an optional
    xml:lang attribute.

    This type is used in places where a single website can be provided in
    multiple language versions. However, as a general rule, if the website
    can correctly auto-detect client browser's preferred language, then
    server implementers SHOULD supply this element only once, and *without*
    the xml:lang attribute.

    :ivar value:
    :ivar lang: If given, it contains the language code the client
        should expect the website content to be in. Also see comments on
        xml:lang attribute in StringWithOptionalLang type.
    """

    class Meta:
        name = "HTTPWithOptionalLang"
        target_namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"https?://.+",
        },
    )
    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class MultilineStringWithOptionalLang(MultilineString):
    """
    A multiline string (as defined in the MultilineString) with an optional
    (but RECOMMENDED) xml:lang attribute.

    It is used in places where a description of some entity can be provided
    in multiple languages.

    :ivar lang: Also see comments on xml:lang attribute in
        StringWithOptionalLang type.
    """

    class Meta:
        target_namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"

    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class StringWithOptionalLang:
    """
    A string with an optional (but RECOMMENDED) xml:lang attribute.

    It is used in places where a name of some entity can be provided in
    multiple languages.

    :ivar value:
    :ivar lang: A note for client developers: Keep in mind, that
        `xml:lang` is of the `xs:language` type. This means that it MAY
        contain values such as `en`, but also `en-US`, `ar-Cyrl-CO`, or
        `tlh-Kore-AQ-fonipa`. Most often, you will need to parse only
        the first component, but in some cases other components might
        also be pretty useful (like the script subtag - "Latn", "Cyrl",
        etc.). The `xml:language` datatype is defined here:
        https://www.ietf.org/rfc/bcp/bcp47.txt You can also discuss this
        tag in context of EWP here: https://github.com/erasmus-without-
        paper/ewp-specs-architecture/issues/11
    """

    class Meta:
        target_namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    lang: str | LangValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )


@dataclass
class AdminNotes(MultilineString):
    """
    Additional information provided by administrators and/or developers.

    This element was placed in the common-types namespace because it is
    being used in multiple schemas throughout the EWP project (most
    notably, various sections of the manifest file).
    """

    class Meta:
        name = "admin-notes"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"


@dataclass
class Hei:
    """
    Briefly describes a single Higher Education Institution (HEI).

    These elements are listed in the Registry Service's cataloge, in order
    to allow the clients to identify all the HEIs by various types of
    identifiers.

    :ivar other_id: SCHAC identifier (provided in the `id` attribute
        described below) is the primary HEI identifier, but manifest
        authors are encouraged to provide all identifiers they can think
        of. (Otherwise, other EWP Hosts may not be able to recognize
        their HEIs.) Note that there can be multiple IDs given, even
        within a single type. This won't happen often, but you should be
        aware of this. It is safer for the Registry to include both
        conflicting values (as they were found in the manifest files),
        than pick one at random.
    :ivar name: The name of the institution. Multiple values may be
        provided, and in multiple languages. Note that there can be
        multiple names given even *for the same language*. This won't
        happen often, but you should be aware of this. It is safer for
        the Registry to include both such conflicting values (as they
        were found in the manifest files), than pick one at random.
    :ivar id: SCHAC identifier of this HEI. As described in the SCHAC
        documentation for the "schacHomeOrganization" element (e.g.
        "uw.edu.pl"). This attribute is REQUIRED. Manifest authors need
        to acquire a proper SCHAC identifier for all HEIs they intend to
        add to their manifest (acquiring them manually is usually quite
        simple).
    """

    class Meta:
        name = "hei"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1"

    other_id: list[OtherHeiId] = field(
        default_factory=list,
        metadata={
            "name": "other-id",
            "type": "Element",
        },
    )
    name: list[StringWithOptionalLang] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class ManifestApiEntryBase:
    """
    A common base type for children of the `apis-implemented` element of
    the manifest file.

    We declare it here (as opposed to declaring in the Discovery API's
    namespace) because it is shared between all the APIs - we want it to
    stay backwards-compatible when new releases of the Discovery API are
    published. IMPORTANT: Clients MUST NOT assume that all children of
    `apis-implemented` will "inherit" these properties. It is true that
    most EWP-related APIs do, but manifest files may contain references to
    *any* APIs.

    :ivar admin_email: RECOMMENDED element. Address of a developer or
        server administrator who may be contacted in case of problems
        *with this particular API* (e.g. malformed responses, etc.).
        Multiple `admin-email` elements may be provided.
    :ivar admin_notes: Additional information provided by host
        developers for the client developers. E.g. "We are currently not
        delivering &lt;description&gt; elements because our model is
        incompatible with the `1.1.3` schema. We will start to deliver
        them once we upgrade to the `1.2.0` schema."
    :ivar version: The API version number the host claims its
        implementation of this API conforms to. Host implementers MUST
        make sure that this number is kept in sync with their
        implementations. E.g. If you have used the `1.1.3` release of
        some API when you have implemented your endpoint, then you
        SHOULD put `1.1.3` here. If you put `1.2.0` here later on, then
        it means that you have just implemented some new `1.2.0`
        features (and you want to let other clients know that you have
        implemented them). Use `0.0.0` when you're implementing a draft
        API, which has not been officially released yet and doesn't have
        any version number yet.
    """

    class Meta:
        target_namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"

    admin_email: list[AdminEmail] = field(
        default_factory=list,
        metadata={
            "name": "admin-email",
            "type": "Element",
            "namespace": "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd",
        },
    )
    admin_notes: AdminNotes | None = field(
        default=None,
        metadata={
            "name": "admin-notes",
            "type": "Element",
            "namespace": "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd",
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]+\.[0-9]+\.[0-9]+",
        },
    )


@dataclass
class ErrorResponse:
    """
    A generic envelope for all kinds of errors.

    Servers SHOULD return this element as the body of all their HTTP 4xx
    and HTTP 5xx responses.

    :ivar developer_message: A message for the client developer. In case
        of client errors (HTTP 4xx responses) it should describe what
        the client did wrong (e.g. a required parameter is missing,
        etc.). In case of server errors (HTTP 5xx responses) it's
        usually much harder for the server to determine what went wrong,
        so this element will probably contain just some generic message
        in such cases (e.g. "Something went wrong. Administrators have
        been notified. We'll try to fix it ASAP.").
    :ivar user_message: A message for the client user. This message will
        usually be provided only in case of some very specific client
        errors (HTTP 4xx responses) - the ones that the client actually
        *expects* to happen sometimes. For example, if the specification
        explicitly states that some parameter values can be rejected by
        the server, but it doesn't state which ones (because it's up to
        the server implementers to decide). In such cases, the "wrong"
        values are usually provided by the end user. And this error
        message should contain the explanation why the server believes
        they're "wrong". For example: '''University of Warsaw doesn't
        currently allow receiving institutions to propose changes to the
        content of the 'Recognition at the Sending Institution' table.
        Please contact the sending coordinator by email to propose this
        change.''' User messages MAY be provided in multiple languages.
        English SHOULD be among them.
    """

    class Meta:
        name = "error-response"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"

    developer_message: MultilineString | None = field(
        default=None,
        metadata={
            "name": "developer-message",
            "type": "Element",
            "required": True,
        },
    )
    user_message: list[MultilineStringWithOptionalLang] = field(
        default_factory=list,
        metadata={
            "name": "user-message",
            "type": "Element",
        },
    )


@dataclass
class SuccessUserMessage(MultilineStringWithOptionalLang):
    """
    This element is sometimes added to regular HTTP 200 responses.

    This serves as an equivalent of the `user-message` element introduced
    in the `error-response` above, but this one is for HTTP 200 responses
    (not error responses). If the server includes this element in the
    response, then it indicates that it wants this message to be displayed
    for the human who had initiated the request. If it's given, then
    clients SHOULD display this message for their end users (if it is
    possible to display it). In case of most APIs no such extra message is
    necessary, because HTTP 200 means "success" in itself. However, in
    cases of some other APIs, the server is allowed some more flexibility
    in how the request is being processed. This element allows to
    developers to inform end users about irregularieties in this process.
    In places where we expect this element to appear, it will be referred
    to in a proper `response.xsd` file, along with some additional
    explanations. Usually it will be used along with minOccurs="0" and
    maxOccurs="unbounded" attributes, in order to allow servers to provide
    the message in multiple languages. It is RECOMMENDED for the server to
    provide it at least in English.
    """

    class Meta:
        name = "success-user-message"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"


@dataclass
class Host:
    """
    Defines a single EWP Host.

    EWP Host defines relationships between HEIs, APIs, server
    administrators and client credentials. One EWP Host defines a single
    Cartesian product (a "join") of all these sets. (E.g. if a client
    certificate X and a HEI Y is present in the same host, then it means
    that server which signs its requests with X is allowed to request
    resources visible to HEI Y. Similar statement is true for every other
    pair of sets.) Most partners will have exactly one `host` entry.
    However, in some cases you might need to describe more than one. For
    example, when you server covers two HEIs, but one of your APIs is
    available for only one of these two HEIs, then it's impossible to
    describe such relationship with a single Cartesian product. You will
    need to use a sum of at least two Cartesian products. (which is
    expressed by two `host` entries).

    :ivar admin_email: RECOMMENDED element. Address of a developer or
        server administrator who may be contacted in case of problems
        (e.g. invalid Manifest file, invalid certificates, server
        errors, etc.). Multiple addresses may be provided. Please note,
        that additional `admin-email` elements can also be included
        inside specific APIs sections (this allows you to add extra
        admins to specific APIs without the need of creating extra
        `host` entries).
    :ivar admin_notes: Additional information provided by administrators
        and/or developers of this host for Registry maintainers and
        client developers. Must be provided in English. E.g. "This host
        is a DEMO server. We plan to keep it online for testing.".
    :ivar apis_implemented:
    :ivar institutions_covered: A list of HEIs (Higher Education
        Institutions) that are covered by this host. In conjunction with
        `apis-implemented`, enlisting a HEI here indicates that the
        partner wants to receive specific HEI-related API queries
        regarding this HEI, and that it will be able to understand them.
        In conjunction with `client-credentials-in-use`, enlisting a HEI
        here indicates that these credentials can be used to request
        resources "in the name of" this HEI. Be advised, that the
        Registry Service MAY ignore some (or all) of the items published
        here, for example if it believes that this HEI does not *want*
        to be covered by you. If, for some reason, your items are not
        being imported, and you're not sure why, please contact the
        Registry Service maintainers. You can also take a look at this
        thread: https://github.com/erasmus-without-paper/ewp-specs-api-
        discovery/issues/12
    :ivar client_credentials_in_use: The list of client credentials used
        by this host to make requests to other EWP hosts. You should
        have this element present if you intend to perform requests
        within the EWP Network. However, it's worth noting, that not
        having it is also valid (if you want your EWP Host to be "server
        only"). Be advised, that the Registry Service MAY ignore some
        (or all) of the credentials submitted here, for example if it
        finds they do not meet proper security standards. If, for some
        reason, your credentials are not being imported, and you're not
        sure why, please contact the Registry Service administrators.
    :ivar server_credentials_in_use: The list of server credentials used
        by this host to authenticate its servers when communicating to
        other EWP hosts. Note, that only *some* methods of server
        authentication make use of these credentials. As opposed to
        client authentication, the keys used in server authentication
        are bound to specific endpoints (URLs), **not HEIs**. (Remember,
        that some services in EWP are not necessarily bound to any HEI,
        or are bound to multiple HEIs.) This means that - if you create
        multiple manifests - then each of your endpoints MAY use a
        different key for signing its responses. However, in most cases,
        you will want to use only a single key for all your APIs and
        endpoints. Be advised, that the Registry Service MAY ignore some
        (or all) of the credentials submitted here, for example if it
        finds they do not meet proper security standards. If, for some
        reason, your credentials are not being imported, and you're not
        sure why, please contact the Registry Service administrators.
    """

    class Meta:
        name = "host"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-discovery/tree/stable-v5"

    admin_email: list[AdminEmail] = field(
        default_factory=list,
        metadata={
            "name": "admin-email",
            "type": "Element",
            "namespace": "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd",
        },
    )
    admin_notes: AdminNotes | None = field(
        default=None,
        metadata={
            "name": "admin-notes",
            "type": "Element",
            "namespace": "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd",
        },
    )
    apis_implemented: ApisImplemented | None = field(
        default=None,
        metadata={
            "name": "apis-implemented",
            "type": "Element",
            "namespace": "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1",
        },
    )
    institutions_covered: Host.InstitutionsCovered | None = field(
        default=None,
        metadata={
            "name": "institutions-covered",
            "type": "Element",
        },
    )
    client_credentials_in_use: Host.ClientCredentialsInUse | None = field(
        default=None,
        metadata={
            "name": "client-credentials-in-use",
            "type": "Element",
        },
    )
    server_credentials_in_use: Host.ServerCredentialsInUse | None = field(
        default=None,
        metadata={
            "name": "server-credentials-in-use",
            "type": "Element",
        },
    )

    @dataclass
    class InstitutionsCovered:
        hei: list[Hei] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "https://github.com/erasmus-without-paper/ewp-specs-api-registry/tree/stable-v1",
            },
        )

    @dataclass
    class ClientCredentialsInUse:
        """
        :ivar certificate: Base64-encoded X.509 certificate used by the
            partner for TLS Client Authentication, as described here:
            https://github.com/erasmus-without-paper/ewp-specs-sec-
            cliauth-tlscert If your private key is compromised, you MUST
            immediately remove all certificates based on this key from
            your manifest.
        :ivar rsa_public_key: Base64-encoded RSA public key used by the
            partner for HTTP Signature Client Authentication, as
            described here: https://github.com/erasmus-without-
            paper/ewp-specs-sec-cliauth-httpsig If your private key is
            compromised, you MUST immediately remove all public keys
            related to this key from your manifest.
        """

        certificate: list[bytes] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "format": "base64",
            },
        )
        rsa_public_key: list[bytes] = field(
            default_factory=list,
            metadata={
                "name": "rsa-public-key",
                "type": "Element",
                "format": "base64",
            },
        )

    @dataclass
    class ServerCredentialsInUse:
        """
        :ivar rsa_public_key: Base64-encoded RSA public key used by the
            partner for HTTP Signature Server Authentication, as
            described here: https://github.com/erasmus-without-
            paper/ewp-specs-sec-cliauth-httpsig If your private key is
            compromised, you MUST immediately remove all public keys
            related to this key from your manifest.
        """

        rsa_public_key: list[bytes] = field(
            default_factory=list,
            metadata={
                "name": "rsa-public-key",
                "type": "Element",
                "format": "base64",
            },
        )


@dataclass
class Catalogue:
    """
    The EWP Registry catalogue response.

    Most of the data published here is copied from the hosts' manifests,
    but the data is additionally verified (and portions of it may be
    modified, removed or transformed). The format is somewhat similar to
    the format of the manifest files, but different in places.

    :ivar host: This element describes a single EWP Host.
    :ivar institutions: The list of institutions referenced in the
        `host` sections above. The list is using the Manifest's XML
        namespace, but the actual data MAY come from other sources too.
    :ivar binaries: This elements keeps a map of binaries. Each binary
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

    host: list[Catalogue.Host] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    institutions: Catalogue.Institutions | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    binaries: Catalogue.Binaries | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
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
            here. IMPORTANT: A single institution can be covered by
            multiple hosts. E.g. If you are looking for a particular API
            implementation for a particular institution, then you MUST
            use both of these selectors in your XPath query. Also, keep
            in mind, that a single API may be served in multiple
            versions, as described here: https://github.com/erasmus-
            without-paper/ewp-specs-architecture/issues/6. Note, that
            this element is not the same element as the one used in the
            Discovery Manifest API (it has the same name, but a
            different namespace and contents).
        :ivar client_credentials_in_use: A list of client credentials
            used by this host to make requests to other EWP hosts in the
            name of all of the covered institutions. Note, that this
            element is not the same element as the one used in the
            Discovery Manifest API (it has the same name, but a
            different namespace and contents).
        :ivar server_credentials_in_use: A list of credentials used by
            this host's server endpoints (URLs) for authenticating
            themselves. Note, that only *some* methods of server
            authentication make use of these credentials. As opposed to
            client authentication, the keys used in server
            authentication are bound to specific endpoints (URLs), **not
            HEIs**. Clients can make use of these credentials for
            authenticating the servers when connecting to any of the
            APIs implemented by this host (in the `../apis-implemented`
            element). Note, that this element is not the same element as
            the one used in the Discovery Manifest API (it has the same
            name, but a different namespace and contents).
        """

        admin_email: list[AdminEmail] = field(
            default_factory=list,
            metadata={
                "name": "admin-email",
                "type": "Element",
                "namespace": "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd",
            },
        )
        admin_notes: AdminNotes | None = field(
            default=None,
            metadata={
                "name": "admin-notes",
                "type": "Element",
                "namespace": "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd",
            },
        )
        apis_implemented: ApisImplemented | None = field(
            default=None,
            metadata={
                "name": "apis-implemented",
                "type": "Element",
            },
        )
        institutions_covered: Catalogue.Host.InstitutionsCovered | None = (
            field(
                default=None,
                metadata={
                    "name": "institutions-covered",
                    "type": "Element",
                },
            )
        )
        client_credentials_in_use: (
            Catalogue.Host.ClientCredentialsInUse | None
        ) = field(
            default=None,
            metadata={
                "name": "client-credentials-in-use",
                "type": "Element",
            },
        )
        server_credentials_in_use: (
            Catalogue.Host.ServerCredentialsInUse | None
        ) = field(
            default=None,
            metadata={
                "name": "server-credentials-in-use",
                "type": "Element",
            },
        )

        @dataclass
        class InstitutionsCovered:
            """
            :ivar hei_id: SCHAC identifier of the HEI. If you don't use
                SCHAC identifiers, you will probably need to use the
                attached mapping (see `institutions` element described
                below).
            """

            hei_id: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "hei-id",
                    "type": "Element",
                },
            )

        @dataclass
        class ClientCredentialsInUse:
            """
            :ivar certificate: Identifies a client certificate with
                which the client has been allowed to make requests
                within the network using the TLS Client Certificate
                Authentication described here:
                https://github.com/erasmus-without-paper/ewp-specs-sec-
                cliauth-tlscert The client which signs his communication
                with the private key matching this certificate is
                allowed to make requests in the name of the institutions
                listed in the adjacent `institutions-covered` element.
                Note, that the Registry does NOT serve the actual
                certificate. Servers MUST use the `sha-256` attribute to
                match certificates the client actually uses.
            :ivar rsa_public_key: Identifies an RSA key-pair which has
                been allowed to make requests within the network using
                the HTTP Signature Client Authentication described here:
                https://github.com/erasmus-without-paper/ewp-specs-sec-
                cliauth-httpsig The client who is in possession of the
                private part of this key is allowed to make requests in
                the name of the institutions listed in the adjacent
                `institutions-covered` element. Please note, that the
                Registry also serves the *actual content* of the public
                part for this key-pair, but this content is not included
                here. Instead, you can look up it's SHA-256 digest in
                the `binaries` section below.
            """

            certificate: list[
                Catalogue.Host.ClientCredentialsInUse.Certificate
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            rsa_public_key: list[
                Catalogue.Host.ClientCredentialsInUse.RsaPublicKey
            ] = field(
                default_factory=list,
                metadata={
                    "name": "rsa-public-key",
                    "type": "Element",
                },
            )

            @dataclass
            class Certificate:
                """
                :ivar sha_256: Certificate's SHA-256 digest (in HEX).
                """

                sha_256: str | None = field(
                    default=None,
                    metadata={
                        "name": "sha-256",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9a-f]{64}",
                    },
                )

            @dataclass
            class RsaPublicKey:
                """
                :ivar sha_256: Public key's SHA-256 digest (in HEX).
                """

                sha_256: str | None = field(
                    default=None,
                    metadata={
                        "name": "sha-256",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9a-f]{64}",
                    },
                )

        @dataclass
        class ServerCredentialsInUse:
            """
            :ivar rsa_public_key: Identifies an RSA key-pair which has
                been allowed to be used to sign HTTP responses from APIs
                listed in the `../apis-implemented` element, as part of
                the HTTP Signature Server Authentication described here:
                https://github.com/erasmus-without-paper/ewp-specs-sec-
                cliauth-httpsig Clients which intend to authenticate the
                server behind the URL X via this method, MUST verify if
                the response is signed with *any* of the keys supplied
                here. The list of valid keys MUST be extracted only from
                the single `host` entry being the parent of the element
                in the URL X has been discovered - the client MUST NOT
                treat keys found in other hosts as valid, even if these
                hosts claim to serve their APIs at the same URL as X.
                Please note, that the Registry also serves the *actual
                content* of the public part for this key-pair, but this
                content is not included here. Instead, you can look up
                it's SHA-256 digest in the `binaries` section below.
            """

            rsa_public_key: list[
                Catalogue.Host.ServerCredentialsInUse.RsaPublicKey
            ] = field(
                default_factory=list,
                metadata={
                    "name": "rsa-public-key",
                    "type": "Element",
                },
            )

            @dataclass
            class RsaPublicKey:
                """
                :ivar sha_256: Public key's SHA-256 digest (in HEX).
                """

                sha_256: str | None = field(
                    default=None,
                    metadata={
                        "name": "sha-256",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9a-f]{64}",
                    },
                )

    @dataclass
    class Institutions:
        hei: list[Hei] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass
    class Binaries:
        """
        :ivar rsa_public_key: Contains base64-encoded binary content of
            RSA public key.
        """

        rsa_public_key: list[Catalogue.Binaries.RsaPublicKey] = field(
            default_factory=list,
            metadata={
                "name": "rsa-public-key",
                "type": "Element",
            },
        )

        @dataclass
        class RsaPublicKey:
            """
            :ivar value:
            :ivar sha_256: The SHA-256 digest of the key's binary
                content. You might have noticed that this is information
                is kind of redundant (because it can be evaluated from
                the content itself). However, the Registry publishes it
                nonetheless (e.g. to reduce the work required to perform
                by the clients, and to make it easier for manual
                matching by humans when debugging XML).
            """

            value: bytes | None = field(
                default=None,
                metadata={
                    "required": True,
                    "format": "base64",
                },
            )
            sha_256: str | None = field(
                default=None,
                metadata={
                    "name": "sha-256",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[0-9a-f]{64}",
                },
            )


@dataclass
class Manifest:
    """
    EWP Discovery Manifest.

    Manifest files describe a set of EWP Hosts. Manifest files are usually
    read by the EWP Registry Service only.

    :ivar host: One v5 manifest file can describe multiple EWP Hosts
        (this is the primary difference between v4 and v5 of Discovery
        API).
    """

    class Meta:
        name = "manifest"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-api-discovery/tree/stable-v5"

    host: list[Host] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
