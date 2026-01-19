from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.availability_constraint_type import (
    AvailabilityConstraintType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class AvailabilityConstraintsType:
    """
    AvailabilityConstraintsType describes the structure of the container
    for availability constraints.

    :ivar availability_constraint: AvailabilityConstraint specifies the
        available content for a set of data.
    """

    availability_constraint: tuple[AvailabilityConstraintType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AvailabilityConstraint",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
        },
    )
