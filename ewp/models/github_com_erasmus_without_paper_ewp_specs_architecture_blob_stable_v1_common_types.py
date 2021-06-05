from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from ewp.models.w3_org_xml_1998_namespace import LangValue

__NAMESPACE__ = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"


@dataclass
class Empty:
    """Just a reusable empty element type, with no content nor attributes.

    See:
    http://stackoverflow.com/questions/20751782/
    """


class Gender(Enum):
    """ISO/IEC 5218 code of human sex.

    https://en.wikipedia.org/wiki/ISO/IEC_5218

    :cvar VALUE_0: not known
    :cvar VALUE_1: male
    :cvar VALUE_2: female
    :cvar VALUE_9: not applicable
    """
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_9 = 9


@dataclass
class ManifestApiEntryBase:
    """A common base type for children of the `apis-implemented` element of the
    manifest file. We declare it here (as opposed to declaring in the
    Discovery.

    API's namespace) because it is shared between all the APIs - we want it to
    stay backwards-compatible when new releases of the Discovery API are published.
    IMPORTANT: Clients MUST NOT assume that all children of `apis-implemented` will
    "inherit" these properties. It is true that most EWP-related APIs do, but
    manifest files may contain references to *any* APIs.

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
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]+\.[0-9]+\.[0-9]+",
        }
    )


@dataclass
class AdminEmail:
    """Address of a developer (or server administrator) who may be contacted in
    case of problems.

    This element was placed in the common-types namespace because it is
    being used in multiple schemas throughout the EWP project (most
    notably, various sections of the manifest file).
    """
    class Meta:
        name = "admin-email"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[^@]+@[^.]+\..+",
        }
    )


@dataclass
class AdminNotes:
    """Additional information provided by administrators and/or developers.

    This element was placed in the common-types namespace because it is
    being used in multiple schemas throughout the EWP project (most
    notably, various sections of the manifest file).
    """
    class Meta:
        name = "admin-notes"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class HttpwithOptionalLang:
    """An absolute URL (might be either HTTP or HTTPS) with an optional
    xml:lang attribute.

    This type is used in places where a single website can be provided
    in multiple language versions. However, as a general rule, if the
    website can correctly auto-detect client browser's preferred
    language, then server implementers SHOULD supply this element only
    once, and *without* the xml:lang attribute.

    :ivar value:
    :ivar lang: If given, it contains the language code the client
        should expect the website content to be in. Also see comments on
        xml:lang attribute in StringWithOptionalLang type.
    """
    class Meta:
        name = "HTTPWithOptionalLang"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"https?://.+",
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class MultilineStringWithOptionalLang:
    """A multiline string (as defined in the MultilineString) with an optional
    (but RECOMMENDED) xml:lang attribute.

    It is used in places where a description of some entity can be
    provided in multiple languages.

    :ivar value:
    :ivar lang: Also see comments on xml:lang attribute in
        StringWithOptionalLang type.
    """
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class StringWithOptionalLang:
    """A string with an optional (but RECOMMENDED) xml:lang attribute.

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
    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class ErrorResponse:
    """A generic envelope for all kinds of errors.

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

    developer_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "developer-message",
            "type": "Element",
            "required": True,
        }
    )
    user_message: List[MultilineStringWithOptionalLang] = field(
        default_factory=list,
        metadata={
            "name": "user-message",
            "type": "Element",
        }
    )


@dataclass
class SuccessUserMessage(MultilineStringWithOptionalLang):
    """This element is sometimes added to regular HTTP 200 responses.

    This serves as an equivalent of the `user-message` element
    introduced in the `error-response` above, but this one is for HTTP
    200 responses (not error responses). If the server includes this
    element in the response, then it indicates that it wants this
    message to be displayed for the human who had initiated the request.
    If it's given, then clients SHOULD display this message for their
    end users (if it is possible to display it). In case of most APIs no
    such extra message is necessary, because HTTP 200 means "success" in
    itself. However, in cases of some other APIs, the server is allowed
    some more flexibility in how the request is being processed. This
    element allows to developers to inform end users about
    irregularieties in this process. In places where we expect this
    element to appear, it will be referred to in a proper `response.xsd`
    file, along with some additional explanations. Usually it will be
    used along with minOccurs="0" and maxOccurs="unbounded" attributes,
    in order to allow servers to provide the message in multiple
    languages. It is RECOMMENDED for the server to provide it at least
    in English.
    """
    class Meta:
        name = "success-user-message"
        namespace = "https://github.com/erasmus-without-paper/ewp-specs-architecture/blob/stable-v1/common-types.xsd"
