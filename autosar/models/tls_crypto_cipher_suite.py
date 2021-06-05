from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
)
from autosar.models.category_string import CategoryString
from autosar.models.crypto_service_certificate_subtypes_enum import CryptoServiceCertificateSubtypesEnum
from autosar.models.crypto_service_key_subtypes_enum import CryptoServiceKeySubtypesEnum
from autosar.models.crypto_service_primitive_subtypes_enum import CryptoServicePrimitiveSubtypesEnum
from autosar.models.identifier import Identifier
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref
from autosar.models.short_name_fragment import ShortNameFragment
from autosar.models.tls_psk_identity import TlsPskIdentity
from autosar.models.tls_version_enum import TlsVersionEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TlsCryptoCipherSuite:
    """
    This meta-class represents a cipher suite for describing cryptographic
    operations in the context of establishing a connection of
    ApplicationEndpoints that is protected by TLS.

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
    :ivar authentication_ref: This reference identifies the crypto
        service primitive for the generation and verification of MACs.
    :ivar certificate_ref: This reference identifies the applicable
        certificate.
    :ivar encryption_ref: This reference identifies the crypto service
        primitive for the execution of encryption.
    :ivar key_exchange_refs: This reference identifies the individual
        (i.e. per cipher suite) crypto service primitive for the
        execution of key exchange during the handshake phase.
    :ivar pre_shared_key_ref: This reference identifies the applicable
        cryptograhic key if the handshake is based on the existence of a
        pre-shared key (PSK)
    :ivar priority: This attribute identifies the priority of the cipher
        suite. Range: 1..65535. Lower values represent higher
        priorities.
    :ivar psk_identity: Pre-shared key identity shared during the
        handshake among the communication parties, to establish a TLS
        connection if the handshake is based on the existence of a pre-
        shared key.
    :ivar version: This attribute supports the definition of the
        applicable version of TLS.
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
        name = "TLS-CRYPTO-CIPHER-SUITE"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["TlsCryptoCipherSuite.ShortNameFragments"] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    annotations: Optional["TlsCryptoCipherSuite.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    authentication_ref: Optional["TlsCryptoCipherSuite.AuthenticationRef"] = field(
        default=None,
        metadata={
            "name": "AUTHENTICATION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    certificate_ref: Optional["TlsCryptoCipherSuite.CertificateRef"] = field(
        default=None,
        metadata={
            "name": "CERTIFICATE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    encryption_ref: Optional["TlsCryptoCipherSuite.EncryptionRef"] = field(
        default=None,
        metadata={
            "name": "ENCRYPTION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    key_exchange_refs: Optional["TlsCryptoCipherSuite.KeyExchangeRefs"] = field(
        default=None,
        metadata={
            "name": "KEY-EXCHANGE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    pre_shared_key_ref: Optional["TlsCryptoCipherSuite.PreSharedKeyRef"] = field(
        default=None,
        metadata={
            "name": "PRE-SHARED-KEY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    priority: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PRIORITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    psk_identity: Optional[TlsPskIdentity] = field(
        default=None,
        metadata={
            "name": "PSK-IDENTITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    version: Optional[TlsVersionEnum] = field(
        default=None,
        metadata={
            "name": "VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
        }
    )

    @dataclass
    class ShortNameFragments:
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

    @dataclass
    class AuthenticationRef(Ref):
        dest: Optional[CryptoServicePrimitiveSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class CertificateRef(Ref):
        dest: Optional[CryptoServiceCertificateSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class EncryptionRef(Ref):
        dest: Optional[CryptoServicePrimitiveSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class KeyExchangeRefs:
        key_exchange_ref: List["TlsCryptoCipherSuite.KeyExchangeRefs.KeyExchangeRef"] = field(
            default_factory=list,
            metadata={
                "name": "KEY-EXCHANGE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class KeyExchangeRef(Ref):
            dest: Optional[CryptoServicePrimitiveSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class PreSharedKeyRef(Ref):
        dest: Optional[CryptoServiceKeySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
