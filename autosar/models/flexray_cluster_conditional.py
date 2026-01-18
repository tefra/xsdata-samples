from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .boolean import Boolean
from .can_physical_channel import CanPhysicalChannel
from .ethernet_physical_channel import EthernetPhysicalChannel
from .flexray_physical_channel import FlexrayPhysicalChannel
from .float_mod import Float
from .integer import Integer
from .lin_physical_channel import LinPhysicalChannel
from .positive_unlimited_integer import PositiveUnlimitedInteger
from .string import String
from .time_value import TimeValue
from .ttcan_physical_channel import TtcanPhysicalChannel
from .user_defined_physical_channel import UserDefinedPhysicalChannel

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayClusterConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar baudrate: Channels speed in bits/s.
    :ivar physical_channels: This relationship defines which channel
        element belongs to which cluster. A channel shall be assigned to
        exactly one cluster, whereas a cluster may have one or more
        channels. The upper multiplicity of this role has been increased
        to * due to resolving an atpVariation stereotype. The previous
        value was -1.
    :ivar protocol_name: The name of the protocol used.
    :ivar protocol_version: The version of the protocol used.
    :ivar speed: This attribute is deprecated and is replaced by the
        attribute "baudrate". Old description: Channels speed in kbps.
    :ivar action_point_offset: The offset of the action point in
        networks
    :ivar bit: Nominal bit time (= 1 / fx:SPEED). gdBit = cSamplesPerBit
        * gdSampleClockPeriod. Unit: seconds (gdBit)
    :ivar cas_rx_low_max: Upper limit of the Collision Avoidance Symbol
        (CAS) acceptance window. Unit:bitDuration
    :ivar cold_start_attempts: The maximum number of times that a node
        in this cluster is permitted to attempt to start the cluster by
        initiating schedule synchronization
    :ivar cycle: Length of the cycle. Unit: seconds
    :ivar cycle_count_max: Maximum cycle counter value in a given
        cluster. Remark: Set to 63 for FlexRay Protocol 2.1 Rev. A
        compliance.
    :ivar detect_nit_error: Indicates whether NIT error status of each
        cluster shall be detected or not.
    :ivar dynamic_slot_idle_phase: The duration of the dynamic slot idle
        phase in minislots.
    :ivar ignore_after_tx: Duration for which the bitstrobing is paused
        after transmission [gdBit].
    :ivar listen_noise: Upper limit for the start up and wake up listen
        timeout in the presence of noise. Expressed as a multiple of the
        cluster constant pdListenTimeout. Unit microticks
    :ivar macro_per_cycle: The number of macroticks in a communication
        cycle
    :ivar macrotick_duration: Duration of the cluster wide nominal
        macrotick, expressed in s.
    :ivar max_without_clock_correction_fatal: Threshold concerning
        vClockCorrectionFailedCounter. Defines the number of consecutive
        even/odd Cycle pairs with missing clock correction terms that
        will cause the protocol to transition from the POC:normal active
        or POC:normal passive state into the POC:halt state.
    :ivar max_without_clock_correction_passive: Threshold concerning
        vClockCorrectionFailedCounter. Defines the number of consecutive
        even/odd Cycle pairs with missing clock correction terms that
        will cause the protocol to transition from the POC:normal active
        state to the POC:normal passive state.
    :ivar minislot_action_point_offset: The Offset of the action point
        within a minislot. Unit: macroticks
    :ivar minislot_duration: The duration of a minislot (dynamic
        segment). Unit: macroticks.
    :ivar network_idle_time: The duration of the network idle time in
        macroticks
    :ivar network_management_vector_length: Length of the Network
        Management vector in a cluster [bytes]
    :ivar number_of_minislots: Number of Minislots in the dynamic
        segment.
    :ivar number_of_static_slots: The number of static slots in the
        static segment.
    :ivar offset_correction_start: Start of the offset correction phase
        within the Network Idle Time (NIT), expressed as the number of
        macroticks from the start of cycle. Unit: macroticks
    :ivar payload_length_static: Globally configured payload length of a
        static frame. Unit: 16-bit WORDS.
    :ivar safety_margin: Additional timespan in macroticks which takes
        jitter into account to be able to set the JobListPointer to the
        next possible job which can be executed in case the FlexRay Job
        List Execution Function has be resynchronized.
    :ivar sample_clock_period: Sample clock period. Unit: seconds
    :ivar static_slot_duration: The duration of a slot in the static
        segment. Unit: macroticks
    :ivar symbol_window: The duration of the symbol window. Unit:
        macroticks
    :ivar symbol_window_action_point_offset: Number of macroticks the
        action point offset is from the beginning of the symbol window
        [Macroticks].
    :ivar sync_frame_id_count_max: Maximum number of distinct syncframe
        identifiers present in a given cluster. This parameter maps to
        FlexRay Protocol 2.1  Rev. A parameter gSyncNodeMax.
    :ivar tranceiver_standby_delay: The duration of timer
        t_TrcvStdbyDelay in seconds. The granularity of this parameter
        shall be restricted to full FlexRay cycles (cycle). The
        transceiver status setting to STANDBY shall be delayed by this
        value. Not specifying a value or a value of 0 shall imply that
        the timer is not used.
    :ivar transmission_start_sequence_duration: Number of bits in the
        Transmission Start Sequence [gdBits].
    :ivar wakeup_rx_idle: Number of bits used by the node to test the
        duration of the 'idle' or HIGH phase of a received wakeup.
        Unit:bitDuration Remarks: This parameter maps to FlexRay
        Protocol 2.1 Rev. A parameter gdWakeupSymbolRxIdle.
    :ivar wakeup_rx_low: Number of bits used by the node to test the
        duration of the LOW phase of a received wakeup. Unit:bitDuration
        Remarks: This parameter maps to FlexRay Protocol 2.1 Rev. A
        parameter gdWakeupSymbolRxLow.
    :ivar wakeup_rx_window: The size of the window used to detect
        wakeups [gdBit]. Remarks: This parameter maps to FlexRay
        Protocol 2.1 Rev. A parameter gdWakeupSymbolRxWindow.
    :ivar wakeup_tx_active: Number of bits used by the node to transmit
        the LOW phase of awakeup symbol and  the HIGH and LOW phases of
        a WUDOP. Unit:bitDuration
    :ivar wakeup_tx_idle: Number of bits used by the node to transmit
        the 'idle' part of a wakeup symbol. Unit: gDbit
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
    """

    class Meta:
        name = "FLEXRAY-CLUSTER-CONDITIONAL"

    baudrate: None | PositiveUnlimitedInteger = field(
        default=None,
        metadata={
            "name": "BAUDRATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    physical_channels: None | FlexrayClusterConditional.PhysicalChannels = (
        field(
            default=None,
            metadata={
                "name": "PHYSICAL-CHANNELS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
    )
    protocol_name: None | String = field(
        default=None,
        metadata={
            "name": "PROTOCOL-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    protocol_version: None | String = field(
        default=None,
        metadata={
            "name": "PROTOCOL-VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    speed: None | Integer = field(
        default=None,
        metadata={
            "name": "SPEED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    action_point_offset: None | Integer = field(
        default=None,
        metadata={
            "name": "ACTION-POINT-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    bit: None | TimeValue = field(
        default=None,
        metadata={
            "name": "BIT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cas_rx_low_max: None | Integer = field(
        default=None,
        metadata={
            "name": "CAS-RX-LOW-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cold_start_attempts: None | Integer = field(
        default=None,
        metadata={
            "name": "COLD-START-ATTEMPTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cycle: None | TimeValue = field(
        default=None,
        metadata={
            "name": "CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    cycle_count_max: None | Integer = field(
        default=None,
        metadata={
            "name": "CYCLE-COUNT-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    detect_nit_error: None | Boolean = field(
        default=None,
        metadata={
            "name": "DETECT-NIT-ERROR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dynamic_slot_idle_phase: None | Integer = field(
        default=None,
        metadata={
            "name": "DYNAMIC-SLOT-IDLE-PHASE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    ignore_after_tx: None | Integer = field(
        default=None,
        metadata={
            "name": "IGNORE-AFTER-TX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    listen_noise: None | Integer = field(
        default=None,
        metadata={
            "name": "LISTEN-NOISE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    macro_per_cycle: None | Integer = field(
        default=None,
        metadata={
            "name": "MACRO-PER-CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    macrotick_duration: None | TimeValue = field(
        default=None,
        metadata={
            "name": "MACROTICK-DURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_without_clock_correction_fatal: None | Integer = field(
        default=None,
        metadata={
            "name": "MAX-WITHOUT-CLOCK-CORRECTION-FATAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_without_clock_correction_passive: None | Integer = field(
        default=None,
        metadata={
            "name": "MAX-WITHOUT-CLOCK-CORRECTION-PASSIVE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minislot_action_point_offset: None | Integer = field(
        default=None,
        metadata={
            "name": "MINISLOT-ACTION-POINT-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    minislot_duration: None | Integer = field(
        default=None,
        metadata={
            "name": "MINISLOT-DURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_idle_time: None | Integer = field(
        default=None,
        metadata={
            "name": "NETWORK-IDLE-TIME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    network_management_vector_length: None | Integer = field(
        default=None,
        metadata={
            "name": "NETWORK-MANAGEMENT-VECTOR-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    number_of_minislots: None | Integer = field(
        default=None,
        metadata={
            "name": "NUMBER-OF-MINISLOTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    number_of_static_slots: None | Integer = field(
        default=None,
        metadata={
            "name": "NUMBER-OF-STATIC-SLOTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    offset_correction_start: None | Integer = field(
        default=None,
        metadata={
            "name": "OFFSET-CORRECTION-START",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    payload_length_static: None | Integer = field(
        default=None,
        metadata={
            "name": "PAYLOAD-LENGTH-STATIC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    safety_margin: None | Integer = field(
        default=None,
        metadata={
            "name": "SAFETY-MARGIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sample_clock_period: None | TimeValue = field(
        default=None,
        metadata={
            "name": "SAMPLE-CLOCK-PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    static_slot_duration: None | Integer = field(
        default=None,
        metadata={
            "name": "STATIC-SLOT-DURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    symbol_window: None | Integer = field(
        default=None,
        metadata={
            "name": "SYMBOL-WINDOW",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    symbol_window_action_point_offset: None | Integer = field(
        default=None,
        metadata={
            "name": "SYMBOL-WINDOW-ACTION-POINT-OFFSET",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sync_frame_id_count_max: None | Integer = field(
        default=None,
        metadata={
            "name": "SYNC-FRAME-ID-COUNT-MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    tranceiver_standby_delay: None | Float = field(
        default=None,
        metadata={
            "name": "TRANCEIVER-STANDBY-DELAY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmission_start_sequence_duration: None | Integer = field(
        default=None,
        metadata={
            "name": "TRANSMISSION-START-SEQUENCE-DURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_rx_idle: None | Integer = field(
        default=None,
        metadata={
            "name": "WAKEUP-RX-IDLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_rx_low: None | Integer = field(
        default=None,
        metadata={
            "name": "WAKEUP-RX-LOW",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_rx_window: None | Integer = field(
        default=None,
        metadata={
            "name": "WAKEUP-RX-WINDOW",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_tx_active: None | Integer = field(
        default=None,
        metadata={
            "name": "WAKEUP-TX-ACTIVE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    wakeup_tx_idle: None | Integer = field(
        default=None,
        metadata={
            "name": "WAKEUP-TX-IDLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class PhysicalChannels:
        can_physical_channel: list[CanPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "CAN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ethernet_physical_channel: list[EthernetPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "ETHERNET-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        flexray_physical_channel: list[FlexrayPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        lin_physical_channel: list[LinPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "LIN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        ttcan_physical_channel: list[TtcanPhysicalChannel] = field(
            default_factory=list,
            metadata={
                "name": "TTCAN-PHYSICAL-CHANNEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        user_defined_physical_channel: list[UserDefinedPhysicalChannel] = (
            field(
                default_factory=list,
                metadata={
                    "name": "USER-DEFINED-PHYSICAL-CHANNEL",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )
