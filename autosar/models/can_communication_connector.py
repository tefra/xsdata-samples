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
from .communication_controller_subtypes_enum import (
    CommunicationControllerSubtypesEnum,
)
from .frame_port import FramePort
from .i_pdu_port import IPduPort
from .i_signal_port import ISignalPort
from .identifier import Identifier
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .pnc_gateway_type_enum import PncGatewayTypeEnum
from .positive_integer import PositiveInteger
from .positive_unlimited_integer import PositiveUnlimitedInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanCommunicationConnector:
    """
    CAN bus specific communication connector attributes.

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
    :ivar comm_controller_ref: Reference to the communication
        controller. The CommunicationConnector and referenced
        CommunicationController shall be aggregated by the same
        ECUInstance. The communicationController can be referenced by
        several CommunicationConnector elements. This is important for
        the FlexRay Bus. FlexRay communicates via two physical channels.
        But only one controller in an ECU is responsible for both
        channels. Thus, two connectors (for channel A and for channel B)
        shall reference to the same controller.
    :ivar create_ecu_wakeup_source: If this parameter is available and
        set to true then a channel wakeup source shall be created for
        the PhysicalChannel referencing this CommunicationConnector.
    :ivar dynamic_pnc_to_channel_mapping_enabled: Defines if this
        EcuInstance shall implement the dynamic PNC-to-channel-mapping
        functionality on this CommunicationConnector and its respective
        PhysicalChannel.
    :ivar ecu_comm_port_instances: The upper multiplicity of this role
        has been increased to * due to resolving an atpVariation
        stereotype. The previous value was -1.
    :ivar pnc_gateway_type: Defines if this EcuInstance shall implement
        the PncGateway functionality on this CommunicationConnector and
        its respective PhysicalChannel. Several EcuInstances on the same
        PhysicalChannel can have the PncGateway functionality enabled,
        but only one of them shall have the pncGatewayType "active".
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar pnc_wakeup_can_id: CAN Identifier used to configure the CAN
        Transceiver for partial network wakeup.
    :ivar pnc_wakeup_can_id_extended: Defines whether pncWakeupCanId and
        pncWakeupCanIdMask shall be interpreted as extended or standard
        CAN ID.
    :ivar pnc_wakeup_can_id_mask: Bit mask for CAN Identifier used to
        configure the CAN Transceiver for partial network wakeup.
    :ivar pnc_wakeup_data_mask: Bit mask for CAN Payload used to
        configure the CAN Transceiver for partial network wakeup.
    :ivar pnc_wakeup_dlc: Data Length of the remote data frame used to
        configure the CAN Transceiver for partial network wakeup in
        Bytes.
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
        name = "CAN-COMMUNICATION-CONNECTOR"

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
        "CanCommunicationConnector.ShortNameFragments"
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
    annotations: Optional["CanCommunicationConnector.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    comm_controller_ref: Optional[
        "CanCommunicationConnector.CommControllerRef"
    ] = field(
        default=None,
        metadata={
            "name": "COMM-CONTROLLER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    create_ecu_wakeup_source: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CREATE-ECU-WAKEUP-SOURCE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dynamic_pnc_to_channel_mapping_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "DYNAMIC-PNC-TO-CHANNEL-MAPPING-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ecu_comm_port_instances: Optional[
        "CanCommunicationConnector.EcuCommPortInstances"
    ] = field(
        default=None,
        metadata={
            "name": "ECU-COMM-PORT-INSTANCES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_gateway_type: Optional[PncGatewayTypeEnum] = field(
        default=None,
        metadata={
            "name": "PNC-GATEWAY-TYPE",
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
    pnc_wakeup_can_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PNC-WAKEUP-CAN-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_wakeup_can_id_extended: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "PNC-WAKEUP-CAN-ID-EXTENDED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_wakeup_can_id_mask: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PNC-WAKEUP-CAN-ID-MASK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_wakeup_data_mask: Optional[PositiveUnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "PNC-WAKEUP-DATA-MASK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    pnc_wakeup_dlc: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "PNC-WAKEUP-DLC",
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
    class CommControllerRef(Ref):
        dest: Optional[CommunicationControllerSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class EcuCommPortInstances:
        frame_port: list[FramePort] = field(
            default_factory=list,
            metadata={
                "name": "FRAME-PORT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        i_pdu_port: list[IPduPort] = field(
            default_factory=list,
            metadata={
                "name": "I-PDU-PORT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        i_signal_port: list[ISignalPort] = field(
            default_factory=list,
            metadata={
                "name": "I-SIGNAL-PORT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
