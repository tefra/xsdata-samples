from dataclasses import dataclass, field
from typing import List, Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .can_addressing_mode_type import CanAddressingModeType
from .can_frame_rx_behavior_enum import CanFrameRxBehaviorEnum
from .can_frame_tx_behavior_enum import CanFrameTxBehaviorEnum
from .category_string import CategoryString
from .frame_port_subtypes_enum import FramePortSubtypesEnum
from .frame_subtypes_enum import FrameSubtypesEnum
from .identifier import Identifier
from .integer import Integer
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_triggering_ref_conditional import PduTriggeringRefConditional
from .positive_integer import PositiveInteger
from .ref import Ref
from .rx_identifier_range import RxIdentifierRange
from .short_name_fragment import ShortNameFragment
from .ttcan_absolutely_scheduled_timing import TtcanAbsolutelyScheduledTiming

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanFrameTriggering:
    """
    CAN specific attributes to the FrameTriggering.

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
    :ivar absolutely_scheduled_timings: Each frame in TTCAN is
        identified by its slot id and communication cycle. A description
        is provided by the usage of AbsolutelyScheduledTiming.
    :ivar can_addressing_mode: The CAN protocol supports two types of
        frame formats. The standard frame format uses 11-bit identifiers
        and is defined in the CAN specification 2.0 A. Additionally the
        extended frame format allows 29-bit identifiers and is defined
        in the CAN specification 2.0 B.
    :ivar can_fd_frame_support: This attribute describes whether the CAN
        FD option is activated or not. If this attribute is TRUE this
        frame can be sent/received as CAN FD frame. Otherwise it has to
        be CAN 2.0 compliant.
    :ivar can_frame_rx_behavior: Defines which CAN protocol shall be
        expected for frame reception.
    :ivar can_frame_tx_behavior: Defines which CAN protocol shall be
        used for frame transmission.
    :ivar identifier: This attribute is used to define the identifier
        this frame shall use on the CAN network.
    :ivar j_1939_requestable: Frame can be triggered by the J1939
        request message.
    :ivar rx_identifier_range: Optional definition of a CanId range.
    :ivar rx_mask: Identifier mask which denotes the relevant bits in
        the CAN Identifier. Together with the identifier, this parameter
        defines a CAN identifier range.
    :ivar tx_mask: Identifier mask which denotes static bits in the CAN
        identifier. The other bits can be set dynamically.
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
        name = "CAN-FRAME-TRIGGERING"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["CanFrameTriggering.ShortNameFragments"] = (
        field(
            default=None,
            metadata={
                "name": "SHORT-NAME-FRAGMENTS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    annotations: Optional["CanFrameTriggering.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    frame_port_refs: Optional["CanFrameTriggering.FramePortRefs"] = field(
        default=None,
        metadata={
            "name": "FRAME-PORT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    frame_ref: Optional["CanFrameTriggering.FrameRef"] = field(
        default=None,
        metadata={
            "name": "FRAME-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_triggerings: Optional["CanFrameTriggering.PduTriggerings"] = field(
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
        "CanFrameTriggering.AbsolutelyScheduledTimings"
    ] = field(
        default=None,
        metadata={
            "name": "ABSOLUTELY-SCHEDULED-TIMINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_addressing_mode: Optional[CanAddressingModeType] = field(
        default=None,
        metadata={
            "name": "CAN-ADDRESSING-MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_fd_frame_support: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CAN-FD-FRAME-SUPPORT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_frame_rx_behavior: Optional[CanFrameRxBehaviorEnum] = field(
        default=None,
        metadata={
            "name": "CAN-FRAME-RX-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_frame_tx_behavior: Optional[CanFrameTxBehaviorEnum] = field(
        default=None,
        metadata={
            "name": "CAN-FRAME-TX-BEHAVIOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    identifier: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "IDENTIFIER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    j_1939_requestable: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "J-1939-REQUESTABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rx_identifier_range: Optional[RxIdentifierRange] = field(
        default=None,
        metadata={
            "name": "RX-IDENTIFIER-RANGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rx_mask: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "RX-MASK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tx_mask: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "TX-MASK",
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
        short_name_fragment: List[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class Annotations:
        annotation: List[Annotation] = field(
            default_factory=list,
            metadata={
                "name": "ANNOTATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class FramePortRefs:
        frame_port_ref: List[
            "CanFrameTriggering.FramePortRefs.FramePortRef"
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
        pdu_triggering_ref_conditional: List[PduTriggeringRefConditional] = (
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
        ttcan_absolutely_scheduled_timing: List[
            TtcanAbsolutelyScheduledTiming
        ] = field(
            default_factory=list,
            metadata={
                "name": "TTCAN-ABSOLUTELY-SCHEDULED-TIMING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
