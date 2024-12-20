from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .identifier import Identifier
from .integer import Integer
from .lin_schedule_table_subtypes_enum import LinScheduleTableSubtypesEnum
from .lin_unconditional_frame_subtypes_enum import (
    LinUnconditionalFrameSubtypesEnum,
)
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_to_frame_mapping import PduToFrameMapping
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinEventTriggeredFrame:
    """An event triggered frame is used as a placeholder to allow multiple slave
    nodes to provide its response.

    The header of an event triggered frame is transmitted when a frame
    slot allocated to the event triggered frame is processed. The
    publisher of an associated unconditional frame shall only transmit
    the response if at least one of the signals carried in its
    unconditional frame is updated. The LIN Master discovers and purges
    collisions with the collisionResolvingScheduleTable. The event
    controlled frame shall not contain any Pdus.

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
    :ivar frame_length: The used length (in bytes) of the referencing
        frame. Should not be confused with a static byte length reserved
        for each frame by some platforms (e.g. FlexRay). The frameLength
        of zero bytes is allowed. Please consider also TPS_SYST_02255.
    :ivar pdu_to_frame_mappings: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar collision_resolving_schedule_ref: Reference to the schedule
        table, which resolves a collision.
    :ivar lin_unconditional_frame_refs: A list of slaves can respond to
        the master request if at least one of the signals carried in its
        unconditional frame is updated. For each response a
        LinFrameTriggering and a LinUnconditionalFrame shall be defined.
        Within a channel a LIN Frame shall be referenced by only one
        FrameTriggering. This allows a derivation of the identifier of a
        substituted Frame. The identifier is specified in
        FrameTriggering element. The Unconditional frames associated
        with an event triggered frame shall: * have equal length. * use
        the same checksum model (i.e. mixing LIN 1.x and LIN 2.x frames
        is not allowed). * reserve the first data field to its protected
        identifier (even if the associated unconditional frame is
        scheduled as a unconditional frame in the same or another
        schedule table). * be published by different slave nodes. *
        shall not be included directly in the same schedule table as the
        event triggered frame is scheduled.
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
        name = "LIN-EVENT-TRIGGERED-FRAME"

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
        "LinEventTriggeredFrame.ShortNameFragments"
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
    annotations: Optional["LinEventTriggeredFrame.Annotations"] = field(
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
    frame_length: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "FRAME-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_to_frame_mappings: Optional[
        "LinEventTriggeredFrame.PduToFrameMappings"
    ] = field(
        default=None,
        metadata={
            "name": "PDU-TO-FRAME-MAPPINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    collision_resolving_schedule_ref: Optional[
        "LinEventTriggeredFrame.CollisionResolvingScheduleRef"
    ] = field(
        default=None,
        metadata={
            "name": "COLLISION-RESOLVING-SCHEDULE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    lin_unconditional_frame_refs: Optional[
        "LinEventTriggeredFrame.LinUnconditionalFrameRefs"
    ] = field(
        default=None,
        metadata={
            "name": "LIN-UNCONDITIONAL-FRAME-REFS",
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
    class PduToFrameMappings:
        pdu_to_frame_mapping: list[PduToFrameMapping] = field(
            default_factory=list,
            metadata={
                "name": "PDU-TO-FRAME-MAPPING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class CollisionResolvingScheduleRef(Ref):
        dest: Optional[LinScheduleTableSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class LinUnconditionalFrameRefs:
        lin_unconditional_frame_ref: list[
            "LinEventTriggeredFrame.LinUnconditionalFrameRefs.LinUnconditionalFrameRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "LIN-UNCONDITIONAL-FRAME-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class LinUnconditionalFrameRef(Ref):
            dest: Optional[LinUnconditionalFrameSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
