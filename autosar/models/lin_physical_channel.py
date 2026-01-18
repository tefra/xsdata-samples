from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .can_frame_triggering import CanFrameTriggering
from .category_string import CategoryString
from .communication_connector_ref_conditional import (
    CommunicationConnectorRefConditional,
)
from .ethernet_frame_triggering import EthernetFrameTriggering
from .flexray_frame_triggering import FlexrayFrameTriggering
from .i_signal_triggering import ISignalTriggering
from .identifier import Identifier
from .lin_frame_triggering import LinFrameTriggering
from .lin_schedule_table import LinScheduleTable
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_triggering import PduTriggering
from .physical_channel_subtypes_enum import PhysicalChannelSubtypesEnum
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class LinPhysicalChannel:
    """
    LIN specific attributes to the physicalChannel.

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
    :ivar comm_connectors: This property was modified due to
        atpVariation (DirectedAssociationPattern).
    :ivar frame_triggerings: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar i_signal_triggerings: The upper multiplicity of this role has
        been increased to * due to resolving an atpVariation stereotype.
        The previous value was -1.
    :ivar managed_physical_channel_refs: Reference between a channel
        with role managing channel and a channel with role managed
        channel.
    :ivar pdu_triggerings: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar bus_idle_timeout_period: This attribute shall be used to set
        an idle timeout period for the enclosing LinPhysicalChannel.
    :ivar schedule_tables: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
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
        name = "LIN-PHYSICAL-CHANNEL"

    short_name: Identifier | None = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: LinPhysicalChannel.ShortNameFragments | None = (
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
    annotations: LinPhysicalChannel.Annotations | None = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    comm_connectors: LinPhysicalChannel.CommConnectors | None = field(
        default=None,
        metadata={
            "name": "COMM-CONNECTORS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    frame_triggerings: LinPhysicalChannel.FrameTriggerings | None = field(
        default=None,
        metadata={
            "name": "FRAME-TRIGGERINGS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    i_signal_triggerings: LinPhysicalChannel.ISignalTriggerings | None = (
        field(
            default=None,
            metadata={
                "name": "I-SIGNAL-TRIGGERINGS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    managed_physical_channel_refs: LinPhysicalChannel.ManagedPhysicalChannelRefs | None = field(
        default=None,
        metadata={
            "name": "MANAGED-PHYSICAL-CHANNEL-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pdu_triggerings: LinPhysicalChannel.PduTriggerings | None = field(
        default=None,
        metadata={
            "name": "PDU-TRIGGERINGS",
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
    bus_idle_timeout_period: TimeValue | None = field(
        default=None,
        metadata={
            "name": "BUS-IDLE-TIMEOUT-PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    schedule_tables: LinPhysicalChannel.ScheduleTables | None = field(
        default=None,
        metadata={
            "name": "SCHEDULE-TABLES",
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
    class CommConnectors:
        communication_connector_ref_conditional: list[
            CommunicationConnectorRefConditional
        ] = field(
            default_factory=list,
            metadata={
                "name": "COMMUNICATION-CONNECTOR-REF-CONDITIONAL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class FrameTriggerings:
        can_frame_triggering: list[CanFrameTriggering] = field(
            default_factory=list,
            metadata={
                "name": "CAN-FRAME-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_frame_triggering: list[EthernetFrameTriggering] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-FRAME-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_frame_triggering: list[FlexrayFrameTriggering] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-FRAME-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_frame_triggering: list[LinFrameTriggering] = field(
            default_factory=list,
            metadata={
                "name": "LIN-FRAME-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ISignalTriggerings:
        i_signal_triggering: list[ISignalTriggering] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ManagedPhysicalChannelRefs:
        managed_physical_channel_ref: list[
            LinPhysicalChannel.ManagedPhysicalChannelRefs.ManagedPhysicalChannelRef
        ] = field(
            default_factory=list,
            metadata={
                "name": "MANAGED-PHYSICAL-CHANNEL-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class ManagedPhysicalChannelRef(Ref):
            dest: PhysicalChannelSubtypesEnum | None = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )

    @dataclass
    class PduTriggerings:
        pdu_triggering: list[PduTriggering] = field(
            default_factory=list,
            metadata={
                "name": "PDU-TRIGGERING",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ScheduleTables:
        lin_schedule_table: list[LinScheduleTable] = field(
            default_factory=list,
            metadata={
                "name": "LIN-SCHEDULE-TABLE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
