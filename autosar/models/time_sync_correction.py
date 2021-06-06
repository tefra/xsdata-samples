from dataclasses import dataclass, field
from typing import Optional
from .boolean import Boolean
from .positive_integer import PositiveInteger
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TimeSyncCorrection:
    """
    This meta-class represents the attributes used for the correction of time
    synchronization.

    :ivar allow_provider_rate_correction: Defines whether the rate
        correction value of a Time Base can be set by means of the
        method setRateCorrection(). false: rate correction cannot be set
        by method setRateCorrection(). true: rate correction can be set
        by method setRateCorrection().
    :ivar offset_correction_adaption_interval: Defines the interval
        during which the adaptive rate correction cancels out the rate
        and time deviation. Unit: seconds.
    :ivar offset_correction_jump_threshold: Threshold for the correction
        method. Deviations below this value will be corrected by a
        linear reduction over a defined timespan. Values equal and
        greater than this value will be corrected by immediately setting
        the correct time and rate in form of a jump. Unit: seconds.
    :ivar rate_corrections_per_measurement_duration: Number of
        simultaneous rate measurements to determine the current rate
        deviation.
    :ivar rate_deviation_measurement_duration: Time span used to
        calculate the rate deviation. Unit: seconds.
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
        name = "TIME-SYNC-CORRECTION"

    allow_provider_rate_correction: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "ALLOW-PROVIDER-RATE-CORRECTION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    offset_correction_adaption_interval: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "OFFSET-CORRECTION-ADAPTION-INTERVAL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    offset_correction_jump_threshold: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "OFFSET-CORRECTION-JUMP-THRESHOLD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rate_corrections_per_measurement_duration: Optional[PositiveInteger] = field(
        default=None,
        metadata={
            "name": "RATE-CORRECTIONS-PER-MEASUREMENT-DURATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    rate_deviation_measurement_duration: Optional[TimeValue] = field(
        default=None,
        metadata={
            "name": "RATE-DEVIATION-MEASUREMENT-DURATION",
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
