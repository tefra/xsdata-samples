from __future__ import annotations

from dataclasses import dataclass, field

from .float_mod import Float
from .multidimensional_time import MultidimensionalTime

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class ConfidenceInterval:
    """
    Additionally to the list of measured distances of event occurrences, a
    confidence interval can be specified for the expected distance of two
    consecutive event occurrences with a given probability.

    :ivar lower_bound: The lower bound of the expected distance of two
        consecutive event occurrences.
    :ivar propability: The probability for the measured lower and upper
        bound of the confidence interval.
    :ivar upper_bound: The upper bound of the expected distance of two
        consecutive event occurrences.
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
        name = "CONFIDENCE-INTERVAL"

    lower_bound: None | MultidimensionalTime = field(
        default=None,
        metadata={
            "name": "LOWER-BOUND",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    propability: None | Float = field(
        default=None,
        metadata={
            "name": "PROPABILITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    upper_bound: None | MultidimensionalTime = field(
        default=None,
        metadata={
            "name": "UPPER-BOUND",
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
