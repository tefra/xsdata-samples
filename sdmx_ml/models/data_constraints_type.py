from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_constraint_type import DataConstraintType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DataConstraintsType:
    """
    DataConstraintsType describes the structure of the container for data
    constraints.

    :ivar data_constraint: DataConstraint specifies the allowed content
        for a set of data.
    """

    data_constraint: tuple[DataConstraintType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DataConstraint",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
        },
    )
