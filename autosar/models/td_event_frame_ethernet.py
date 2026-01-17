from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .category_string import CategoryString
from .ecu_instance_subtypes_enum import EcuInstanceSubtypesEnum
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pdu_triggering_subtypes_enum import PduTriggeringSubtypesEnum
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .socket_connection_bundle_subtypes_enum import (
    SocketConnectionBundleSubtypesEnum,
)
from .static_socket_connection_subtypes_enum import (
    StaticSocketConnectionSubtypesEnum,
)
from .td_event_frame_ethernet_type_enum import TdEventFrameEthernetTypeEnum
from .td_event_occurrence_expression import TdEventOccurrenceExpression
from .td_header_id_range import TdHeaderIdRange

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TdEventFrameEthernet:
    """
    This is used to describe timing description events related to the
    exchange of Ethernet frames between an Ethernet communication
    controller and the BSW Ethernet interface and driver module.

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
    :ivar occurrence_expression: The occurrence expression for this
        event.
    :ivar ecu_instance_ref: The ECU context for a particular timing
        event. The link is optional, because the EcuInstance can not be
        defined for events of type TDEventCycleStart.
    :ivar socket_connection_bundle_ref: Specifies the
        SocketConnectionBundle by the means of which the PDUs are
        transmitted or received within an Ethernet Frame.
    :ivar static_socket_connection_ref: Specifies the SocketConnection
        by the means of which Physical Data Units (PDU) are transmitted
        or received within an Ethernet Frame.
    :ivar td_event_type: This is used to describe the specific event
        type of a TDEventFrameEthernet.
    :ivar td_header_id_filters: Specifies the header identifier or a
        range of header identifiers that if contained in the Ethernet
        frame let the TDEventFrameEthernet occur.
    :ivar td_pdu_triggering_filter_refs: Specifies the PDU that if
        contained in the Ethernet frame let the TDEventFrameEthernet
        occur.
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
        name = "TD-EVENT-FRAME-ETHERNET"

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
        "TdEventFrameEthernet.ShortNameFragments"
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
    annotations: Optional["TdEventFrameEthernet.Annotations"] = field(
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
    occurrence_expression: Optional[TdEventOccurrenceExpression] = field(
        default=None,
        metadata={
            "name": "OCCURRENCE-EXPRESSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecu_instance_ref: Optional["TdEventFrameEthernet.EcuInstanceRef"] = field(
        default=None,
        metadata={
            "name": "ECU-INSTANCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    socket_connection_bundle_ref: Optional[
        "TdEventFrameEthernet.SocketConnectionBundleRef"
    ] = field(
        default=None,
        metadata={
            "name": "SOCKET-CONNECTION-BUNDLE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    static_socket_connection_ref: Optional[
        "TdEventFrameEthernet.StaticSocketConnectionRef"
    ] = field(
        default=None,
        metadata={
            "name": "STATIC-SOCKET-CONNECTION-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    td_event_type: Optional[TdEventFrameEthernetTypeEnum] = field(
        default=None,
        metadata={
            "name": "TD-EVENT-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    td_header_id_filters: Optional[
        "TdEventFrameEthernet.TdHeaderIdFilters"
    ] = field(
        default=None,
        metadata={
            "name": "TD-HEADER-ID-FILTERS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    td_pdu_triggering_filter_refs: Optional[
        "TdEventFrameEthernet.TdPduTriggeringFilterRefs"
    ] = field(
        default=None,
        metadata={
            "name": "TD-PDU-TRIGGERING-FILTER-REFS",
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
    class EcuInstanceRef(Ref):
        dest: Optional[EcuInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SocketConnectionBundleRef(Ref):
        dest: Optional[SocketConnectionBundleSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class StaticSocketConnectionRef(Ref):
        dest: Optional[StaticSocketConnectionSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class TdHeaderIdFilters:
        td_header_id_range: list[TdHeaderIdRange] = field(
            default_factory=list,
            metadata={
                "name": "TD-HEADER-ID-RANGE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TdPduTriggeringFilterRefs:
        td_pdu_triggering_filter_ref: list[
            "TdEventFrameEthernet.TdPduTriggeringFilterRefs.TdPduTriggeringFilterRef"
        ] = field(
            default_factory=list,
            metadata={
                "name": "TD-PDU-TRIGGERING-FILTER-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

        @dataclass
        class TdPduTriggeringFilterRef(Ref):
            dest: Optional[PduTriggeringSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
