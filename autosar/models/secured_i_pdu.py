from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from autosar.models.boolean import Boolean
from autosar.models.category_string import CategoryString
from autosar.models.contained_i_pdu_props import ContainedIPduProps
from autosar.models.identifier import Identifier
from autosar.models.integer import Integer
from autosar.models.multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from autosar.models.multilanguage_long_name import MultilanguageLongName
from autosar.models.pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from autosar.models.positive_integer import PositiveInteger
from autosar.models.ref import Ref
from autosar.models.secure_communication_authentication_props_subtypes_enum import SecureCommunicationAuthenticationPropsSubtypesEnum
from autosar.models.secure_communication_freshness_props_subtypes_enum import SecureCommunicationFreshnessPropsSubtypesEnum
from autosar.models.secure_communication_props import SecureCommunicationProps
from autosar.models.secured_pdu_header_enum import SecuredPduHeaderEnum
from autosar.models.short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SecuredIPdu:
    """If useAsCryptographicPdu is not set or set to false this IPdu contains
    the payload of an Authentic IPdu supplemented by additional Authentication
    Information (Freshness Counter and an Authenticator).

    If useAsCryptographicPdu is set to true this IPdu contains the
    Authenticator for a payload that is transported in a separate
    message. The separate Authentic IPdu is described by the Pdu that is
    referenced with the payload reference from this SecuredIPdu.

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
        object in question.  More elaborate documentation, (in
        particular how the object is built or used) should go to
        "introduction".
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
    :ivar has_dynamic_length: This attribute defines whether the Pdu has
        dynamic length (true) or not (false). Please note that the usage
        of this attribute is restricted by [constr_3448].
    :ivar length: Pdu length in bytes. In case of dynamic length IPdus
        (containing a dynamical length signal), this value indicates the
        maximum data length. It should be noted that in former AUTOSAR
        releases (Rel 2.1, Rel 3.0, Rel 3.1, Rel 4.0 Rev. 1) this
        parameter was defined in bits.   The Pdu length of zero bytes is
        allowed.
    :ivar meta_data_length: Number of additional bytes of MetaData in
        the PDU data field. The MetaData contains auxiliary information
        for the PDU, e.g. the CAN ID.
    :ivar contained_i_pdu_props: Defines whether this IPdu may be
        collected inside a ContainerIPdu.
    :ivar authentication_props_ref: Reference to authentication
        properties that are valid for this SecuredIPdu.
    :ivar freshness_props_ref: Reference to freshness properties that
        are valid for this SecuredIPdu.
    :ivar payload_ref: Reference to a Pdu that will be protected against
        unauthorized manipulation and replay attacks.
    :ivar secure_communication_props: Specific configuration properties
        for this SecuredIPdu.
    :ivar use_as_cryptographic_i_pdu: If this attribute is set to true
        the SecuredIPdu contains the Authentication Information for an
        AuthenticIPdu that is transmitted in a separate message. The
        AuthenticIPdu contains the original payload, i.e. the secured
        data.  If this attribute is set to false this SecuredIPdu
        contains the payload of an Authentic IPdu supplemented by
        additional Authentication Information.
    :ivar use_secured_pdu_header: This attribute defines the size of the
        header which is inserted into the SecuredIPdu. If this attribute
        is set to anything but noHeader, the SecuredIPdu contains the
        Secured I-PDU Header to indicate the length of the
        AuthenticIPdu. The AuthenticIPdu contains the original payload,
        i.e. the secured data.
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
        different AUTOSAR models.  The form of the UUID (Universally
        Unique Identifier) is taken from a standard defined by the Open
        Group (was Open Software Foundation). This standard is widely
        used, including by Microsoft for COM (GUIDs) and by many
        companies for DCE, which is based on CORBA. The method for
        generating these 128-bit IDs is published in the standard and
        the effectiveness and uniqueness of the IDs is not in practice
        disputed. If the id namespace is omitted, DCE is assumed.  An
        example is "DCE:2fac1234-31f8-11b4-a222-08002b34c003". The uuid
        attribute has no semantic meaning for an AUTOSAR model and there
        is no requirement for AUTOSAR tools to manage the timestamp.
    """
    class Meta:
        name = "SECURED-I-PDU"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        }
    )
    short_name_fragments: Optional["SecuredIPdu.ShortNameFragments"] = field(
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
    annotations: Optional["SecuredIPdu.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    has_dynamic_length: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "HAS-DYNAMIC-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    length: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    meta_data_length: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "META-DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    contained_i_pdu_props: Optional[ContainedIPduProps] = field(
        default=None,
        metadata={
            "name": "CONTAINED-I-PDU-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    authentication_props_ref: Optional["SecuredIPdu.AuthenticationPropsRef"] = field(
        default=None,
        metadata={
            "name": "AUTHENTICATION-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    freshness_props_ref: Optional["SecuredIPdu.FreshnessPropsRef"] = field(
        default=None,
        metadata={
            "name": "FRESHNESS-PROPS-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    payload_ref: Optional["SecuredIPdu.PayloadRef"] = field(
        default=None,
        metadata={
            "name": "PAYLOAD-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    secure_communication_props: Optional[SecureCommunicationProps] = field(
        default=None,
        metadata={
            "name": "SECURE-COMMUNICATION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    use_as_cryptographic_i_pdu: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "USE-AS-CRYPTOGRAPHIC-I-PDU",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    use_secured_pdu_header: Optional[SecuredPduHeaderEnum] = field(
        default=None,
        metadata={
            "name": "USE-SECURED-PDU-HEADER",
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
    class AuthenticationPropsRef(Ref):
        dest: Optional[SecureCommunicationAuthenticationPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class FreshnessPropsRef(Ref):
        dest: Optional[SecureCommunicationFreshnessPropsSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class PayloadRef(Ref):
        dest: Optional[PduTriggeringSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
