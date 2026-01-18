from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .boolean import Boolean
from .byte_order_enum import ByteOrderEnum
from .diagnostic_clear_dtc_limitation_enum import (
    DiagnosticClearDtcLimitationEnum,
)
from .diagnostic_data_capture_enum import DiagnosticDataCaptureEnum
from .diagnostic_debounce_algorithm_props import (
    DiagnosticDebounceAlgorithmProps,
)
from .diagnostic_event_displacement_strategy_enum import (
    DiagnosticEventDisplacementStrategyEnum,
)
from .diagnostic_memory_entry_storage_trigger_enum import (
    DiagnosticMemoryEntryStorageTriggerEnum,
)
from .diagnostic_occurrence_counter_processing_enum import (
    DiagnosticOccurrenceCounterProcessingEnum,
)
from .diagnostic_status_bit_handling_test_failed_since_last_clear_enum import (
    DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum,
)
from .diagnostic_type_of_dtc_supported_enum import (
    DiagnosticTypeOfDtcSupportedEnum,
)
from .diagnostic_type_of_freeze_frame_record_numeration_enum import (
    DiagnosticTypeOfFreezeFrameRecordNumerationEnum,
)
from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticCommonPropsConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar aging_requires_tested_cycle: Defines whether the aging cycle
        counter is processed every aging cycles or else only tested
        aging cycle are considered. If the attribute is set to TRUE:
        only tested aging cycle are considered for aging cycle counter.
        If the attribute is set to FALSE: aging cycle counter is
        processed every aging cycle.
    :ivar clear_dtc_limitation: Defines the scope of the DEM_ClearDTC
        Api.
    :ivar debounce_algorithm_propss: Defines the used debounce
        algorithms relevant in the context of the enclosing
        DiagnosticCommonProps. Usually, there is a variety of debouncing
        algorithms to take into account and therefore the multiplicity
        of this aggregation is set to 0..*.
    :ivar default_endianness: Defines the default endianness of the data
        belonging to a DID or RID which is applicable if the
        DiagnosticDataElement does not define the endianness via the
        swDataDefProps.baseType attribute.
    :ivar dtc_status_availability_mask: Mask for the supported DTC
        status bits by the Dem.
    :ivar environment_data_capture: This attribute determines whether
        the capturing of environment data is done synchronously inside
        the report API function or whether the capturing shall be done
        asynchronously, i.e. after the report API function already
        terminated.
    :ivar event_displacement_strategy: This attribute defines, whether
        support for event displacement is enabled or not, and which
        displacement strategy is followed.
    :ivar max_number_of_event_entries: This attribute fixes the maximum
        number of event entries in the fault memory.
    :ivar max_number_of_request_correctly_received_response_pending:
        Maximum number of negative responses with response code 0x78
        (requestCorrectlyReceived-ResponsePending) allowed per request.
        DCM will send a negative response with response code 0x10
        (generalReject), in case the limit value gets reached. Value
        0xFF means that no limit number of NRC 0x78 response apply.
    :ivar memory_entry_storage_trigger: Describes the primary trigger to
        allocate an event memory entry.
    :ivar occurrence_counter_processing: This attribute defines the
        consideration of the fault confirmation process for the
        occurrence counter.
    :ivar reset_confirmed_bit_on_overflow: This attribute defines,
        whether the confirmed bit is reset or not while an event memory
        entry will be displaced.
    :ivar response_on_all_request_sids: If set to FALSE the DCM will not
        respond to diagnostic request that contains a service ID which
        is in the range from 0x40 to 0x7F or in the  range from 0xC0 to
        0xFF (Response IDs).
    :ivar response_on_second_declined_request: Defines the reaction upon
        a second request (ClientB) that can not be processed (e.g. due
        to priority assessment). TRUE: when the second request (Client
        B) can not be processed, it shall be answered with NRC21
        BusyRepeatRequest. FALSE: when the second request (Client B) can
        not be processed, it shall not be responded.
    :ivar security_delay_time_on_boot: Start delay timer on power on in
        seconds. This delay indicates the time at ECU boot power-on time
        where the Dcm remains in the default session and does not accept
        a security access.
    :ivar status_bit_handling_test_failed_since_last_clear: This
        attribute defines, whether the aging and displacement mechanism
        shall be applied to the "TestFailedSinceLastClear" status bits.
    :ivar status_bit_storage_test_failed: This parameter is used to
        activate/deactivate the permanent storage of the "TestFailed"
        status bits. true: storage activated false: storage deactivated
    :ivar type_of_dtc_supported: This attribute defines the format
        returned by Dem_DcmGetTranslationType and does not relate
        to/influence the supported Dem functionality.
    :ivar type_of_freeze_frame_record_numeration: This attribute defines
        the type of assigning freeze frame record numbers for event-
        specific freeze frame records.
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
        name = "DIAGNOSTIC-COMMON-PROPS-CONDITIONAL"

    aging_requires_tested_cycle: Boolean | None = field(
        default=None,
        metadata={
            "name": "AGING-REQUIRES-TESTED-CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    clear_dtc_limitation: DiagnosticClearDtcLimitationEnum | None = field(
        default=None,
        metadata={
            "name": "CLEAR-DTC-LIMITATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    debounce_algorithm_propss: (
        DiagnosticCommonPropsConditional.DebounceAlgorithmPropss | None
    ) = field(
        default=None,
        metadata={
            "name": "DEBOUNCE-ALGORITHM-PROPSS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    default_endianness: ByteOrderEnum | None = field(
        default=None,
        metadata={
            "name": "DEFAULT-ENDIANNESS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    dtc_status_availability_mask: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "DTC-STATUS-AVAILABILITY-MASK",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    environment_data_capture: DiagnosticDataCaptureEnum | None = field(
        default=None,
        metadata={
            "name": "ENVIRONMENT-DATA-CAPTURE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_displacement_strategy: (
        DiagnosticEventDisplacementStrategyEnum | None
    ) = field(
        default=None,
        metadata={
            "name": "EVENT-DISPLACEMENT-STRATEGY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_number_of_event_entries: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-OF-EVENT-ENTRIES",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max_number_of_request_correctly_received_response_pending: (
        PositiveInteger | None
    ) = field(
        default=None,
        metadata={
            "name": "MAX-NUMBER-OF-REQUEST-CORRECTLY-RECEIVED-RESPONSE-PENDING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    memory_entry_storage_trigger: (
        DiagnosticMemoryEntryStorageTriggerEnum | None
    ) = field(
        default=None,
        metadata={
            "name": "MEMORY-ENTRY-STORAGE-TRIGGER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    occurrence_counter_processing: (
        DiagnosticOccurrenceCounterProcessingEnum | None
    ) = field(
        default=None,
        metadata={
            "name": "OCCURRENCE-COUNTER-PROCESSING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    reset_confirmed_bit_on_overflow: Boolean | None = field(
        default=None,
        metadata={
            "name": "RESET-CONFIRMED-BIT-ON-OVERFLOW",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    response_on_all_request_sids: Boolean | None = field(
        default=None,
        metadata={
            "name": "RESPONSE-ON-ALL-REQUEST-SIDS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    response_on_second_declined_request: Boolean | None = field(
        default=None,
        metadata={
            "name": "RESPONSE-ON-SECOND-DECLINED-REQUEST",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    security_delay_time_on_boot: TimeValue | None = field(
        default=None,
        metadata={
            "name": "SECURITY-DELAY-TIME-ON-BOOT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    status_bit_handling_test_failed_since_last_clear: (
        DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum | None
    ) = field(
        default=None,
        metadata={
            "name": "STATUS-BIT-HANDLING-TEST-FAILED-SINCE-LAST-CLEAR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    status_bit_storage_test_failed: Boolean | None = field(
        default=None,
        metadata={
            "name": "STATUS-BIT-STORAGE-TEST-FAILED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    type_of_dtc_supported: DiagnosticTypeOfDtcSupportedEnum | None = field(
        default=None,
        metadata={
            "name": "TYPE-OF-DTC-SUPPORTED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    type_of_freeze_frame_record_numeration: (
        DiagnosticTypeOfFreezeFrameRecordNumerationEnum | None
    ) = field(
        default=None,
        metadata={
            "name": "TYPE-OF-FREEZE-FRAME-RECORD-NUMERATION",
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

    @dataclass
    class DebounceAlgorithmPropss:
        diagnostic_debounce_algorithm_props: list[
            DiagnosticDebounceAlgorithmProps
        ] = field(
            default_factory=list,
            metadata={
                "name": "DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
