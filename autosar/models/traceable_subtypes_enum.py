from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TraceableSubtypesEnum(Enum):
    AGE_CONSTRAINT = "AGE-CONSTRAINT"
    ARBITRARY_EVENT_TRIGGERING = "ARBITRARY-EVENT-TRIGGERING"
    BURST_PATTERN_EVENT_TRIGGERING = "BURST-PATTERN-EVENT-TRIGGERING"
    CONCRETE_PATTERN_EVENT_TRIGGERING = "CONCRETE-PATTERN-EVENT-TRIGGERING"
    EVENT_TRIGGERING_CONSTRAINT = "EVENT-TRIGGERING-CONSTRAINT"
    EXECUTION_ORDER_CONSTRAINT = "EXECUTION-ORDER-CONSTRAINT"
    EXECUTION_TIME_CONSTRAINT = "EXECUTION-TIME-CONSTRAINT"
    LATENCY_TIMING_CONSTRAINT = "LATENCY-TIMING-CONSTRAINT"
    OFFSET_TIMING_CONSTRAINT = "OFFSET-TIMING-CONSTRAINT"
    PERIODIC_EVENT_TRIGGERING = "PERIODIC-EVENT-TRIGGERING"
    SPORADIC_EVENT_TRIGGERING = "SPORADIC-EVENT-TRIGGERING"
    STRUCTURED_REQ = "STRUCTURED-REQ"
    SYNCHRONIZATION_POINT_CONSTRAINT = "SYNCHRONIZATION-POINT-CONSTRAINT"
    SYNCHRONIZATION_TIMING_CONSTRAINT = "SYNCHRONIZATION-TIMING-CONSTRAINT"
    TRACEABLE = "TRACEABLE"
    TRACEABLE_TABLE = "TRACEABLE-TABLE"
    TRACEABLE_TEXT = "TRACEABLE-TEXT"
    TIMING_CONSTRAINT = "TIMING-CONSTRAINT"