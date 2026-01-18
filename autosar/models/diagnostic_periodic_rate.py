from __future__ import annotations

from dataclasses import dataclass, field

from .diagnostic_periodic_rate_category_enum import (
    DiagnosticPeriodicRateCategoryEnum,
)
from .time_value import TimeValue

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticPeriodicRate:
    """
    This represents the ability to define a periodic rate for the
    specification of the "read data by periodic ID" diagnostic service.

    :ivar period: This represents the period of the
        DiagnosticPeriodicRate in seconds.
    :ivar periodic_rate_category: This attribute represents the category
        of the periodic rate.
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
        name = "DIAGNOSTIC-PERIODIC-RATE"

    period: None | TimeValue = field(
        default=None,
        metadata={
            "name": "PERIOD",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    periodic_rate_category: None | DiagnosticPeriodicRateCategoryEnum = field(
        default=None,
        metadata={
            "name": "PERIODIC-RATE-CATEGORY",
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
