from dataclasses import dataclass, field
from typing import Optional

from .positive_integer_value_variation_point import (
    PositiveIntegerValueVariationPoint,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DiagnosticTestIdentifier:
    """
    This meta-class represents the ability to create a diagnostic test
    identifier.

    :ivar id: This represents the numerical id associated with the
        diagnostic test identifier.
    :ivar uas_id: This represents the unit and scaling Id of the
        diagnostic test result.
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
        name = "DIAGNOSTIC-TEST-IDENTIFIER"

    id: PositiveIntegerValueVariationPoint | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    uas_id: PositiveIntegerValueVariationPoint | None = field(
        default=None,
        metadata={
            "name": "UAS-ID",
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
