from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .bus_mirror_can_id_range_mapping import BusMirrorCanIdRangeMapping
from .bus_mirror_can_id_to_can_id_mapping import BusMirrorCanIdToCanIdMapping
from .bus_mirror_channel import BusMirrorChannel
from .bus_mirror_lin_pid_to_can_id_mapping import BusMirrorLinPidToCanIdMapping
from .category_string import CategoryString
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_triggering_ref_conditional import PduTriggeringRefConditional
from .positive_integer import PositiveInteger
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class BusMirrorChannelMappingCan:
    """
    This element defines the bus mirroring between a CAN or LIN sourceChannel and a
    CAN targetChannel.

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
    :ivar source_channel: Defines the sourceChannel from which frames
        are received.
    :ivar target_channel: Defines the targetChannel to which frames are
        forwarded.
    :ivar target_pdu_triggerings: Reference to the PduTriggering that is
        used for transmission of the mirrored frames on the
        targetChannel. Please note that on FlexRay several
        targetPduTriggerings may be used. For all other communcation
        channels only a single targetPduTriggering is supported. This
        property was modified due to atpVariation
        (DirectedAssociationPattern).
    :ivar can_id_range_mappings: Rules for remapping of a set of CAN
        IDs.
    :ivar can_id_to_can_id_mappings: Rules for remapping of single
        CanIds.
    :ivar lin_pid_to_can_id_mappings: Rules for remapping of single LIN
        Frames.
    :ivar mirror_source_lin_to_can_range_base_id: Base ID merged with
        the LIN frame ID to form the CAN ID. Only required when a
        BusMirrorChannel that refers to a LinPhysicalChannel in the role
        channel is referenced in the role sourceChannel.
    :ivar mirror_status_can_id: CAN ID of the CAN status frame. If
        configured, a status frame will be sent on the CAN destination
        bus that contains the state of all active source buses.
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
        name = "BUS-MIRROR-CHANNEL-MAPPING-CAN"

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
        "BusMirrorChannelMappingCan.ShortNameFragments"
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
    annotations: Optional["BusMirrorChannelMappingCan.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
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
    source_channel: Optional[BusMirrorChannel] = field(
        default=None,
        metadata={
            "name": "SOURCE-CHANNEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_channel: Optional[BusMirrorChannel] = field(
        default=None,
        metadata={
            "name": "TARGET-CHANNEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_pdu_triggerings: Optional[
        "BusMirrorChannelMappingCan.TargetPduTriggerings"
    ] = field(
        default=None,
        metadata={
            "name": "TARGET-PDU-TRIGGERINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_id_range_mappings: Optional[
        "BusMirrorChannelMappingCan.CanIdRangeMappings"
    ] = field(
        default=None,
        metadata={
            "name": "CAN-ID-RANGE-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    can_id_to_can_id_mappings: Optional[
        "BusMirrorChannelMappingCan.CanIdToCanIdMappings"
    ] = field(
        default=None,
        metadata={
            "name": "CAN-ID-TO-CAN-ID-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lin_pid_to_can_id_mappings: Optional[
        "BusMirrorChannelMappingCan.LinPidToCanIdMappings"
    ] = field(
        default=None,
        metadata={
            "name": "LIN-PID-TO-CAN-ID-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mirror_source_lin_to_can_range_base_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIRROR-SOURCE-LIN-TO-CAN-RANGE-BASE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mirror_status_can_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "MIRROR-STATUS-CAN-ID",
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
    class TargetPduTriggerings:
        pdu_triggering_ref_conditional: List[
            PduTriggeringRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "PDU-TRIGGERING-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CanIdRangeMappings:
        bus_mirror_can_id_range_mapping: List[
            BusMirrorCanIdRangeMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "BUS-MIRROR-CAN-ID-RANGE-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CanIdToCanIdMappings:
        bus_mirror_can_id_to_can_id_mapping: List[
            BusMirrorCanIdToCanIdMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "BUS-MIRROR-CAN-ID-TO-CAN-ID-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class LinPidToCanIdMappings:
        bus_mirror_lin_pid_to_can_id_mapping: List[
            BusMirrorLinPidToCanIdMapping
        ] = field(
            default_factory=list,
            metadata={
                "name": "BUS-MIRROR-LIN-PID-TO-CAN-ID-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
