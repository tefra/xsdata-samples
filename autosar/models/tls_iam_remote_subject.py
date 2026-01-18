from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .crypto_service_certificate_subtypes_enum import (
    CryptoServiceCertificateSubtypesEnum,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .string import String
from .tls_crypto_cipher_suite_subtypes_enum import (
    TlsCryptoCipherSuiteSubtypesEnum,
)
from .tls_secure_com_props_subtypes_enum import TlsSecureComPropsSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TlsIamRemoteSubject:
    """
    This meta-class defines the proxy information about the remote node in
    case of TLS.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar long_name: This specifies the long name of the object. Long
        name is targeted to human readers and acts like a headline.
    :ivar desc: This represents a general but brief (one paragraph)
        description what the object in question is about. It is only one
        paragraph! Desc is intended to be collected into overview
        tables. This property helps a human reader to identify the
        object in question. More elaborate documentation, (in particular
        how the object is built or used) should go to "introduction".
    :ivar category: The category is a keyword that specializes the
        semantics of the Identifiable. It affects the expected existence
        of attributes and the applicability of constraints.
    :ivar admin_data: This represents the administrative data for the
        identifiable object.
    :ivar introduction: This represents more information about how the
        object in question is built or is used. Therefore it is a
        DocumentationBlock.
    :ivar annotations: Possibility to provide additional notes while
        defining a model element (e.g. the ECU Configuration Parameter
        Values). These are not intended as documentation but are mere
        design notes.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar accepted_crypto_cipher_suite_with_psk_refs: This reference is
        used to identify a remote node by means of the preshared Key.
    :ivar accepted_remote_certificate_refs: This reference is used to
        identify a remote node by means of the certificate.
    :ivar cert_common_name: This attribute defines the common name (CN)
        of the certificate of the remote peer.
    :ivar derived_certificate_accepted: This attribute defines whether a
        derivedCertificate is accepted (true) or not (false).
    :ivar iam_relevant_tls_secure_com_props_refs: This reference defines
        the local TlsSecureComProps that are relevant for IAM.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    :ivar uuid: The purpose of this attribute is to provide a globally
        unique identifier for an instance of a meta-class. The values of
        this attribute should be globally unique strings prefixed by the
        type of identifier.  For example, to include a DCE UUID as
        defined by The Open Group, the UUID would be preceded by "DCE:".
        The values of this attribute may be used to support merging of
        different AUTOSAR models. The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed. An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "TLS-IAM-REMOTE-SUBJECT"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: TlsIamRemoteSubject.ShortNameFragments | None = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    long_name: MultilanguageLongName | None = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: MultiLanguageOverviewParagraph | None = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: CategoryString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: AdminData | None = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: DocumentationBlock | None = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: TlsIamRemoteSubject.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: VariationPoint | None = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    accepted_crypto_cipher_suite_with_psk_refs: (
        TlsIamRemoteSubject.AcceptedCryptoCipherSuiteWithPskRefs | None
    ) = field(
        default=None,
        metadata={
            "name": "ACCEPTED-CRYPTO-CIPHER-SUITE-WITH-PSK-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    accepted_remote_certificate_refs: (
        TlsIamRemoteSubject.AcceptedRemoteCertificateRefs | None
    ) = field(
        default=None,
        metadata={
            "name": "ACCEPTED-REMOTE-CERTIFICATE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cert_common_name: String | None = field(
        default=None,
        metadata={
            "name": "CERT-COMMON-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    derived_certificate_accepted: Boolean | None = field(
        default=None,
        metadata={
            "name": "DERIVED-CERTIFICATE-ACCEPTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    iam_relevant_tls_secure_com_props_refs: (
        TlsIamRemoteSubject.IamRelevantTlsSecureComPropsRefs | None
    ) = field(
        default=None,
        metadata={
            "name": "IAM-RELEVANT-TLS-SECURE-COM-PROPS-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: str | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        },
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: list[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class AcceptedCryptoCipherSuiteWithPskRefs:
        accepted_crypto_cipher_suite_with_psk_ref: list[
            TlsIamRemoteSubject.AcceptedCryptoCipherSuiteWithPskRefs.AcceptedCryptoCipherSuiteWithPskRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "ACCEPTED-CRYPTO-CIPHER-SUITE-WITH-PSK-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class AcceptedCryptoCipherSuiteWithPskRef(Ref):
            dest: TlsCryptoCipherSuiteSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class AcceptedRemoteCertificateRefs:
        accepted_remote_certificate_ref: list[
            TlsIamRemoteSubject.AcceptedRemoteCertificateRefs.AcceptedRemoteCertificateRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "ACCEPTED-REMOTE-CERTIFICATE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class AcceptedRemoteCertificateRef(Ref):
            dest: CryptoServiceCertificateSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class IamRelevantTlsSecureComPropsRefs:
        iam_relevant_tls_secure_com_props_ref: list[
            TlsIamRemoteSubject.IamRelevantTlsSecureComPropsRefs.IamRelevantTlsSecureComPropsRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "IAM-RELEVANT-TLS-SECURE-COM-PROPS-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class IamRelevantTlsSecureComPropsRef(Ref):
            dest: TlsSecureComPropsSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
