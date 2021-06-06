from dataclasses import dataclass, field
from typing import List, Optional
from .annotation import VariationPoint
from .boolean import Boolean
from .flexray_fifo_configuration import FlexrayFifoConfiguration
from .integer import Integer
from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayCommunicationControllerConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar wake_up_by_controller_supported: Defines whether the ECU shall
        be woken up by this CommunicationController. TRUE: wake up is
        possible FALSE: wake up is not supported Note: If
        wakeUpByControllerSupported is set to TRUE the feature shall be
        supported by both hardware and basic software.
    :ivar accepted_startup_range: Expanded range of measured clock
        deviation allowed for startup frames during integration.
        Unit:microtick
    :ivar allow_halt_due_to_clock: Boolean flag that controls the
        transition to the POC:halt state due to a clock synchronization
        errors. If set to true, the Communication Controller is allowed
        to transition to POC:halt. If set to false, the Communication
        Controller will not transition to the POC:halt state but will
        enter or remain in the normal POC (passive State).
    :ivar allow_passive_to_active: Number of consecutive even/odd cycle
        pairs that shall have valid clock correction terms before the
        Communication Controller will be allowed to transition from the
        POC:normal passive state to POC:normal active state. If set to
        0, the Communication Controller is not allowed to transition
        from POC:norm
    :ivar cluster_drift_damping: The cluster drift damping factor used
        in clock synchronization rate correction in microticks
    :ivar decoding_correction: Value used by the receiver to calculate
        the difference between primary time reference point and
        secondary time reference point. Unit: Microticks
        (pDecodingCorrection)
    :ivar delay_compensation_a: Value used to compensate for reception
        delays on channel A Unit: Microticks. This optional parameter
        shall only be filled out if channel A is used.
    :ivar delay_compensation_b: Value used to compensate for reception
        delays on channel B. Unit: Microticks. This optional parameter
        shall only be filled out if channel B is used.
    :ivar extern_offset_correction: Fixed amount added or subtracted to
        the calculated offset correction term to facilitate external
        offset correction, expressed in node-local microticks.
    :ivar extern_rate_correction: Fixed amount added or subtracted to
        the calculated rate correction term to facilitate external rate
        correction, expressed in node-local microticks.
    :ivar external_sync: Flag indicating whether the node is externally
        synchronized (operating as Time Gateway Sink in an TT-E Time
        Triggered External Sync cluster) or locally synchronized.
    :ivar fall_back_internal: Flag indicating whether a Time Gateway
        Sink node will switch to local clock operation when
        synchronization with the Time Gateway Source node is lost
        (pFallBackInternal = true) or will instead go to POC:ready
        (pFallBackInternal = false).
    :ivar flexray_fifos: One First In First Out (FIFO) queued receive
        structure, defining the admittance criteria to the FIFO.
    :ivar key_slot_id: ID of the slot used to transmit the startup
        frame, sync frame, or designated single slot frame. If the
        attributes keySlotUsedForStartUp, keySlotUsedForSync, or
        keySlotOnlyEnabled are set to true the key slot value is
        mandatory.
    :ivar key_slot_only_enabled: Flag indicating whether or not the node
        shall enter key slot only mode following startup.
    :ivar key_slot_used_for_start_up: Flag indicating whether the Key
        Slot is used to transmit a startup frame.
    :ivar key_slot_used_for_sync: Flag indicating whether the Key Slot
        is used to transmit a sync frame.
    :ivar latest_tx: The number of the last minislot in which a
        transmission can start in the dynamic segment for the respective
        node
    :ivar listen_timeout: Value for the startup listen timeout and
        wakeup listen timeout. Although this is a node local parameter,
        the real time equivalent of this value should be the same for
        all nodes in the cluster. Unit: Microticks
    :ivar macro_initial_offset_a: Integer number of macroticks between
        the static slot boundary and the closest macrotick boundary of
        the secondary time reference point based on the nominal
        macrotick duration. (pMacroInitialOffset). This optional
        parameter shall only be filled out if channel A is used.
    :ivar macro_initial_offset_b: Integer number of macroticks between
        the static slot boundary and the closest macrotick boundary of
        the secondary time reference point based on the nominal
        macrotick duration. (pMacroInitialOffset). This optional
        parameter shall only be filled out if channel B is used.
    :ivar maximum_dynamic_payload_length: Maximum payload length for the
        dynamic channel of a frame in 16 bit WORDS.
    :ivar micro_initial_offset_a: Number of microticks between the
        closest macrotick boundary described by gMacroInitialOffset and
        the secondary time reference point.  The parameter depends on
        pDelayCompensationA and therefore it has to be set independently
        for each channel. This optional parameter shall only be filled
        out if channel A is used.
    :ivar micro_initial_offset_b: Number of microticks between the
        closest macrotick boundary described by gMacroInitialOffset and
        the secondary time reference point.  The parameter depends on
        pDelayCompensationB and therefore it has to be set independently
        for each channel. This optional parameter shall only be filled
        out if channel B is used.
    :ivar micro_per_cycle: The nominal number of microticks in a
        communication cycle
    :ivar microtick_duration: Duration of a microtick. This attribute
        can be derived from samplePerMicrotick and gdSampleClockPeriod.
        Unit: seconds
    :ivar nm_vector_early_update: Flag indicating when the update of the
        Network Management Vector in the CHI shall take place. If set to
        false, the update shall take place after the NIT. If set to
        true, the update shall take place after the end of the static
        segment.
    :ivar offset_correction_out: Magnitude of the maximum permissible
        offset correction value. Unit:microtick (pOffsetCorrectionOut)
    :ivar rate_correction_out: Magnitude of the maximum permissible rate
        correction value and the maximum drift offset between two nodes
        operating with unsynchronized clocks for one communication
        cycle. Unit:Microticks (pRateCorrectionOut) Remarks: This
        parameter maps to FlexRay Protocol 2.1 Rev. A parameter
        pdMaxDrift.
    :ivar samples_per_microtick: Number of samples per microtick
    :ivar second_key_slot_id: ID of the second Key slot, in which a
        second startup frame shall be sent in TT-L Time Triggered Local
        Master Sync or TT-E Time Triggered External Sync mode. If this
        parameter is set to zero the node does not have a second key
        slot.
    :ivar two_key_slot_mode: Flag indicating whether node operates as a
        startup node in a TT-E Time Triggered External Sync or TT-L Time
        Triggered Local Master Sync cluster.
    :ivar wake_up_pattern: Number of repetitions of the Tx-wakeup symbol
        to be sent during the CC_WakeupSend state of this Node in the
        cluster
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
        name = "FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL"

    wake_up_by_controller_supported: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "WAKE-UP-BY-CONTROLLER-SUPPORTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    accepted_startup_range: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "ACCEPTED-STARTUP-RANGE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    allow_halt_due_to_clock: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ALLOW-HALT-DUE-TO-CLOCK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    allow_passive_to_active: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "ALLOW-PASSIVE-TO-ACTIVE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    cluster_drift_damping: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "CLUSTER-DRIFT-DAMPING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    decoding_correction: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "DECODING-CORRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    delay_compensation_a: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "DELAY-COMPENSATION-A",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    delay_compensation_b: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "DELAY-COMPENSATION-B",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    extern_offset_correction: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "EXTERN-OFFSET-CORRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    extern_rate_correction: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "EXTERN-RATE-CORRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    external_sync: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "EXTERNAL-SYNC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    fall_back_internal: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "FALL-BACK-INTERNAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    flexray_fifos: Optional["FlexrayCommunicationControllerConditional.FlexrayFifos"] = field(
        default=None,
        metadata={
            "name": "FLEXRAY-FIFOS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    key_slot_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "KEY-SLOT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    key_slot_only_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "KEY-SLOT-ONLY-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    key_slot_used_for_start_up: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "KEY-SLOT-USED-FOR-START-UP",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    key_slot_used_for_sync: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "KEY-SLOT-USED-FOR-SYNC",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    latest_tx: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "LATEST-TX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    listen_timeout: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "LISTEN-TIMEOUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    macro_initial_offset_a: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MACRO-INITIAL-OFFSET-A",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    macro_initial_offset_b: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MACRO-INITIAL-OFFSET-B",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    maximum_dynamic_payload_length: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MAXIMUM-DYNAMIC-PAYLOAD-LENGTH",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    micro_initial_offset_a: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MICRO-INITIAL-OFFSET-A",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    micro_initial_offset_b: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MICRO-INITIAL-OFFSET-B",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    micro_per_cycle: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "MICRO-PER-CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    microtick_duration: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "MICROTICK-DURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    nm_vector_early_update: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-VECTOR-EARLY-UPDATE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    offset_correction_out: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "OFFSET-CORRECTION-OUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rate_correction_out: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "RATE-CORRECTION-OUT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    samples_per_microtick: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "SAMPLES-PER-MICROTICK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    second_key_slot_id: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "SECOND-KEY-SLOT-ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    two_key_slot_mode: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "TWO-KEY-SLOT-MODE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    wake_up_pattern: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "WAKE-UP-PATTERN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class FlexrayFifos:
        flexray_fifo_configuration: List[FlexrayFifoConfiguration] = field(
            default_factory=list,
            metadata={
                "name": "FLEXRAY-FIFO-CONFIGURATION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )
