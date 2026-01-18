from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .i_pdu_port_subtypes_enum import IPduPortSubtypesEnum
from .i_signal_triggering_ref_conditional import (
    ISignalTriggeringRefConditional,
)
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_subtypes_enum import PduSubtypesEnum
from .ref import Ref
from .sec_oc_crypto_service_mapping_subtypes_enum import (
    SecOcCryptoServiceMappingSubtypesEnum,
)
from .short_name_fragment import ShortNameFragment
from .trigger_i_pdu_send_condition import TriggerIPduSendCondition

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PduTriggering:
    """
    The PduTriggering describes on which channel the IPdu is transmitted.

    The Pdu routing by the PduR is only allowed for subclasses of IPdu.
    Depending on its relation to entities such channels and clusters it can
    be unambiguously deduced whether a fan-out is handled by the Pdu router
    or the Bus Interface. If the fan-out is specified between different
    clusters it shall be handled by the Pdu Router. If the fan-out is
    specified between different channels of the same cluster it shall be
    handled by the Bus Interface.

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
    :ivar i_pdu_port_refs: References to the IPduPort on every ECU of
        the system which sends and/or receives the I-PDU. References for
        both the sender and the receiver side shall be included when the
        system is completely defined.
    :ivar i_pdu_ref: Reference to the Pdu for which the PduTriggering is
        defined. One I-Pdu can be triggered on different channels (PduR
        fan-out). The Pdu routing by the PduR is only allowed for
        subclasses of IPdu. Nevertheless is the reference to the Pdu
        element necessary since the PduTriggering element is also used
        to specify the sending and receiving connections to EcuPorts.
    :ivar i_signal_triggerings: This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar sec_oc_crypto_mapping_ref: This reference identifies the
        crypto profile applicable to  the usage (send, receive) of the
        also referenced SecuredIPdu. Obviously, this reference is only
        applicable if the Pdutriggering also references a SecuredIPdu in
        the role iPdu.
    :ivar trigger_i_pdu_send_conditions: Defines the trigger for the
        Com_TriggerIPDUSend API call. Only if all defined
        TriggerIPduSendConditions evaluate to true (AND associated) the
        Com_TriggerIPDUSend API shall be called.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "PDU-TRIGGERING"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: PduTriggering.ShortNameFragments | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
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
    annotations: PduTriggering.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_pdu_port_refs: PduTriggering.IPduPortRefs | None = field(
        default=None,
        metadata={
            "name": "I-PDU-PORT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_pdu_ref: PduTriggering.IPduRef | None = field(
        default=None,
        metadata={
            "name": "I-PDU-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_signal_triggerings: PduTriggering.ISignalTriggerings | None = field(
        default=None,
        metadata={
            "name": "I-SIGNAL-TRIGGERINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sec_oc_crypto_mapping_ref: PduTriggering.SecOcCryptoMappingRef | None = (
        field(
            default=None,
            metadata={
                "name": "SEC-OC-CRYPTO-MAPPING-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    trigger_i_pdu_send_conditions: (
        PduTriggering.TriggerIPduSendConditions | None
    ) = field(
        default=None,
        metadata={
            "name": "TRIGGER-I-PDU-SEND-CONDITIONS",
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
    class IPduPortRefs:
        i_pdu_port_ref: list[PduTriggering.IPduPortRefs.IPduPortRef] = field(
            default_factory=list,
            metadata={
                "name": "I-PDU-PORT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class IPduPortRef(Ref):
            dest: IPduPortSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class IPduRef(Ref):
        dest: PduSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class ISignalTriggerings:
        i_signal_triggering_ref_conditional: list[
            ISignalTriggeringRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL-TRIGGERING-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class SecOcCryptoMappingRef(Ref):
        dest: SecOcCryptoServiceMappingSubtypesEnum | None = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TriggerIPduSendConditions:
        trigger_i_pdu_send_condition: list[TriggerIPduSendCondition] = field(
            default_factory=list,
            metadata={
                "name": "TRIGGER-I-PDU-SEND-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
