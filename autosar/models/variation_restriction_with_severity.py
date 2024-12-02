from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .full_binding_time_enum import FullBindingTimeEnum
from .severity_enum import SeverityEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class VariationRestrictionWithSeverity:
    """
    Defines constraints on the usage of variation and on the valid binding times.

    :ivar severity: Severity level that is reported in case the
        restriction is violated.
    :ivar variation: Defines if the AUTOSAR model may define a
        VariationPoint at this location.
    :ivar valid_binding_times:
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
        name = "VARIATION-RESTRICTION-WITH-SEVERITY"

    severity: Optional[SeverityEnum] = field(
        default=None,
        metadata={
            "name": "SEVERITY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "VARIATION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    valid_binding_times: Optional[
        "VariationRestrictionWithSeverity.ValidBindingTimes"
    ] = field(
        default=None,
        metadata={
            "name": "VALID-BINDING-TIMES",
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

    @dataclass
    class ValidBindingTimes:
        """
        :ivar valid_binding_time: List of valid binding times.
        """

        valid_binding_time: list[FullBindingTimeEnum] = field(
            default_factory=list,
            metadata={
                "name": "VALID-BINDING-TIME",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
