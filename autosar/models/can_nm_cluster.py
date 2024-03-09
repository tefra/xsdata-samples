from dataclasses import dataclass, field
from typing import List, Optional
from .admin_data import (
    AdminData,
    Annotation,
    DocumentationBlock,
    VariationPoint,
)
from .boolean import Boolean
from .can_nm_node import CanNmNode
from .category_string import CategoryString
from .communication_cluster_subtypes_enum import (
    CommunicationClusterSubtypesEnum,
)
from .flexray_nm_node import FlexrayNmNode
from .identifier import Identifier
from .integer import Integer
from .j_1939_nm_node import J1939NmNode
from .multi_language_overview_paragraph import MultiLanguageOverviewParagraph
from .multilanguage_long_name import MultilanguageLongName
from .positive_integer import PositiveInteger
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .time_value import TimeValue
from .udp_nm_node import UdpNmNode

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class CanNmCluster:
    """
    Can specific NmCluster attributes.

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
    :ivar communication_cluster_ref: Association to a
        CommunicationCluster in the topology description.
    :ivar nm_channel_id: This attribute has the status "removed" and
        shall not be used any longer. Old description: Channel
        identification number of the corresponding channel. Must be
        unique over all NmClusters.
    :ivar nm_channel_sleep_master: This parameter shall be set to
        indicate if the sleep of this network can be absolutely decided
        by the local node only and that no other nodes can oppose that
        decision.
    :ivar nm_nodes: The upper multiplicity of this role has been
        increased to * due to resolving an atpVariation stereotype. The
        previous value was -1.
    :ivar nm_node_detection_enabled: Enables the Request Repeat Message
        Request support. Only valid if nmNodeIdEnabled is set to true.
    :ivar nm_node_id_enabled: Enables the source node identifier.
    :ivar nm_pnc_participation: Defines whether this NmCluster
        contributes to the partial network mechanism.
    :ivar nm_repeat_msg_ind_enabled: Switch for enabling the Repeat
        Message Bit Indication.
    :ivar nm_synchronizing_network: If this parameter is true, then this
        network is a synchronizing network for the NM coordination
        cluster which it belongs to. The network is expected to call
        Nm_SynchronizationPoint() at regular intervals.
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
    :ivar nm_busload_reduction_active: It determines if bus load
        reduction for the respective CanNm channel is active or not.
    :ivar nm_car_wake_up_bit_position: Specifies the bit position of the
        CarWakeUp within the NmPdu.
    :ivar nm_car_wake_up_filter_enabled: Please note that this parameter
        is deprecated and will be removed in future. Old description: If
        this attribute is set to true the CareWakeUp filtering is
        supported. In this case only the CarWakeUp bit within the NmPdu
        with source node identifier nmCarWakeUpFilterNodeId is
        considered as CarWakeUp request.
    :ivar nm_car_wake_up_filter_node_id: Source node identifier for
        CarWakeUp filtering.
    :ivar nm_car_wake_up_rx_enabled: Please note that this parameter is
        deprecated and will be removed in future. Old description: If
        set to true this attribute enables the support of CarWakeUp bit
        evaluation in received NmPdus.
    :ivar nm_cbv_position: Defines the position of the control bit
        vector within the NmPdu (Byte position). If this attribute is
        not configured, the Control Bit Vector is not used.
    :ivar nm_channel_active: Please note that this attribute is
        deprecated and will be removed in future. This switch determines
        if the respective CanNm channel is active or not. Indicates
        whether a particular CanNm channel shall be initialized (TRUE)
        or not (FALSE). If this parameter is set to FALSE the respective
        NM instance shall not be used during runtime.
    :ivar nm_immediate_nm_cycle_time: Defines the immediate NmPdu cycle
        time in seconds which is used for nmImmediateNmTransmissions
        NmPdu transmissions. This parameter is only valid if
        CanNmImmediateNmTransmissions is greater one.
    :ivar nm_immediate_nm_transmissions: Defines the number of immediate
        NmPdus which shall be transmitted. If the value is zero no
        immediate NmPdus are transmitted. The cycle time of immeditate
        NmPdus is defined by nmImmediateNmCycleTime.
    :ivar nm_message_timeout_time: Timeout of an NmPdu in seconds. It
        determines how long the NM shall wait with notification of
        transmission failure while communication errors occur on the
        bus.
    :ivar nm_msg_cycle_time: Period of a NmPdu in seconds. It determines
        the periodic rate in the periodic transmission mode with bus
        load reduction and is the basis for transmit scheduling in the
        periodic transmission mode without bus load reduction.
    :ivar nm_network_timeout: Network Timeout for NmPdus in seconds It
        denotes the time how long the CanNm shall stay in the Network
        Mode before transition into Prepare Bus-Sleep Mode shall take
        place.
    :ivar nm_nid_position: Defines the byte position of the source node
        identifier within the NmPdu. If this attribute is not
        configured, the Node Identification is not used.
    :ivar nm_remote_sleep_indication_time: Timeout for Remote Sleep
        Indication in seconds. It defines the time how long it shall
        take to recognize that all other nodes are ready to sleep.
    :ivar nm_repeat_message_time: Timeout for Repeat Message State in
        seconds. Defines the time how long the NM shall stay in the
        Repeat Message State.
    :ivar nm_user_data_length: Defines the length of the user data
        contained in the NmPdu. Please note that this attribute is
        deprecated and will be removed in future.
    :ivar nm_wait_bus_sleep_time: Timeout for bus calm down phase in
        seconds. It denotes the time how long the CanNm shall stay in
        the Prepare Bus-Sleep Mode before transition into Bus-Sleep Mode
        shall take place.
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
        name = "CAN-NM-CLUSTER"

    short_name: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: Optional["CanNmCluster.ShortNameFragments"] = field(
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
    annotations: Optional["CanNmCluster.Annotations"] = field(
        default=None,
        metadata={
            "name": "ANNOTATIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    communication_cluster_ref: Optional[
        "CanNmCluster.CommunicationClusterRef"
    ] = field(
        default=None,
        metadata={
            "name": "COMMUNICATION-CLUSTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_channel_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "NM-CHANNEL-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_channel_sleep_master: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-CHANNEL-SLEEP-MASTER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_nodes: Optional["CanNmCluster.NmNodes"] = field(
        default=None,
        metadata={
            "name": "NM-NODES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_node_detection_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-NODE-DETECTION-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_node_id_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-NODE-ID-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_pnc_participation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-PNC-PARTICIPATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_repeat_msg_ind_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-REPEAT-MSG-IND-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_synchronizing_network: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-SYNCHRONIZING-NETWORK",
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
    nm_busload_reduction_active: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-BUSLOAD-REDUCTION-ACTIVE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_car_wake_up_bit_position: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "NM-CAR-WAKE-UP-BIT-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_car_wake_up_filter_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-CAR-WAKE-UP-FILTER-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_car_wake_up_filter_node_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "NM-CAR-WAKE-UP-FILTER-NODE-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_car_wake_up_rx_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-CAR-WAKE-UP-RX-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_cbv_position: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "NM-CBV-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_channel_active: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-CHANNEL-ACTIVE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_immediate_nm_cycle_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NM-IMMEDIATE-NM-CYCLE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_immediate_nm_transmissions: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "NM-IMMEDIATE-NM-TRANSMISSIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_message_timeout_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NM-MESSAGE-TIMEOUT-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_msg_cycle_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NM-MSG-CYCLE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_network_timeout: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NM-NETWORK-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_nid_position: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "NM-NID-POSITION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_remote_sleep_indication_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NM-REMOTE-SLEEP-INDICATION-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_repeat_message_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NM-REPEAT-MESSAGE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_user_data_length: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "NM-USER-DATA-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_wait_bus_sleep_time: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "NM-WAIT-BUS-SLEEP-TIME",
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
    class CommunicationClusterRef(Ref):
        dest: Optional[CommunicationClusterSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class NmNodes:
        can_nm_node: List[CanNmNode] = field(
            default_factory=list,
            metadata={
                "name": "CAN-NM-NODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_nm_node: List[FlexrayNmNode] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-NM-NODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        j_1939_nm_node: List[J1939NmNode] = field(
            default_factory=list,
            metadata={
                "name": "J-1939-NM-NODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        udp_nm_node: List[UdpNmNode] = field(
            default_factory=list,
            metadata={
                "name": "UDP-NM-NODE",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
