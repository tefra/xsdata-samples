from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .category_string import CategoryString
from .flexray_absolutely_scheduled_timing import (
    FlexrayAbsolutelyScheduledTiming,
)
from .frame_port_subtypes_enum import FramePortSubtypesEnum
from .frame_subtypes_enum import FrameSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_triggering_ref_conditional import PduTriggeringRefConditional
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayFrameTriggering:
    """
    FlexRay specific attributes to the FrameTriggering.

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
    :ivar frame_port_refs: References to the FramePort on every ECU of
        the system which sends and/or receives the frame. References for
        both the sender and the receiver side shall be included when the
        system is completely defined.
    :ivar frame_ref: One frame can be triggered several times, e.g. on
        different channels. If a frame has no frame triggering, it won't
        be sent at all. A frame triggering has assigned exactly one
        frame, which it triggers.
    :ivar pdu_triggerings: This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar absolutely_scheduled_timings: Specification of a sending
        behaviour where the exact time for the frames transmission is
        guaranteed.
    :ivar allow_dynamic_l_sdu_length: Allows L-PDU length reduction and
        indicates that the related CC buffer has to be reconfigured for
        the actual length and Header-CRC before transmission of the
        L-PDU. If this attribute is set to true than the referenced
        Frame length attribute defines the max. length.
    :ivar message_id: The first two bytes of the payload segment of the
        FlexRay frame format for frames transmitted in the dynamic
        segment can be used as receiver filterable data called the
        message ID.
    :ivar payload_preamble_indicator: Switching the Payload Preamble
        bit.
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
        name = "FLEXRAY-FRAME-TRIGGERING"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional[
        "FlexrayFrameTriggering.ShortNameFragments"
    ] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    long_name: Optional[MultilanguageLongName] = field(
        default=None,
        metadata={
            "name": "LONG-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    desc: Optional[MultiLanguageOverviewParagraph] = field(
        default=None,
        metadata={
            "name": "DESC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: Optional[CategoryString] = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    admin_data: Optional[AdminData] = field(
        default=None,
        metadata={
            "name": "ADMIN-DATA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    introduction: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "INTRODUCTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    annotations: Optional["FlexrayFrameTriggering.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    frame_port_refs: Optional["FlexrayFrameTriggering.FramePortRefs"] = field(
        default=None,
        metadata={
            "name": "FRAME-PORT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    frame_ref: Optional["FlexrayFrameTriggering.FrameRef"] = field(
        default=None,
        metadata={
            "name": "FRAME-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_triggerings: Optional["FlexrayFrameTriggering.PduTriggerings"] = field(
        default=None,
        metadata={
            "name": "PDU-TRIGGERINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    absolutely_scheduled_timings: Optional[
        "FlexrayFrameTriggering.AbsolutelyScheduledTimings"
    ] = field(
        default=None,
        metadata={
            "name": "ABSOLUTELY-SCHEDULED-TIMINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    allow_dynamic_l_sdu_length: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ALLOW-DYNAMIC-L-SDU-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    message_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MESSAGE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    payload_preamble_indicator: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "PAYLOAD-PREAMBLE-INDICATOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )
    uuid: Optional[str] = field(
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
    class FramePortRefs:
        frame_port_ref: list[
            "FlexrayFrameTriggering.FramePortRefs.FramePortRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "FRAME-PORT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class FramePortRef(Ref):
            dest: Optional[FramePortSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class FrameRef(Ref):
        dest: Optional[FrameSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class PduTriggerings:
        pdu_triggering_ref_conditional: list[PduTriggeringRefConditional] = (
            field(
                default_factory=list,
                metadata={
                    "name": "PDU-TRIGGERING-REF-CONDITIONAL",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

    @dataclass
    class AbsolutelyScheduledTimings:
        flexray_absolutely_scheduled_timing: list[
            FlexrayAbsolutelyScheduledTiming
        ] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
