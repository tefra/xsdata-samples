from dataclasses import dataclass, field

from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class GlobalTimeCorrectionProps:
    """
    This meta-class defines the attributes for rate and offset correction.

    :ivar offset_correction_adaption_interval: Defines the interval
        during which the adaptive rate correction cancels out the rate-
        and time deviation.
    :ivar offset_correction_jump_threshold: Threshold for the correction
        method. Deviations below this value will be corrected by a
        linear reduction over a defined timespan. Values equal- and
        greater than this value will be corrected by immediately setting
        the correct time- and rate in form of a jump.
    :ivar rate_correction_measurement_duration: Definition of the time
        span which is used to calculate the rate deviation.
    :ivar rate_corrections_per_measurement_duration: Defines the number
        of simultaneous rate measurements to determine the current rate
        deviation.
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
        name = "GLOBAL-TIME-CORRECTION-PROPS"

    offset_correction_adaption_interval: TimeValue | None = field(
        default=None,
        metadata={
            "name": "OFFSET-CORRECTION-ADAPTION-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    offset_correction_jump_threshold: TimeValue | None = field(
        default=None,
        metadata={
            "name": "OFFSET-CORRECTION-JUMP-THRESHOLD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rate_correction_measurement_duration: TimeValue | None = field(
        default=None,
        metadata={
            "name": "RATE-CORRECTION-MEASUREMENT-DURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    rate_corrections_per_measurement_duration: PositiveInteger | None = field(
        default=None,
        metadata={
            "name": "RATE-CORRECTIONS-PER-MEASUREMENT-DURATION",
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
