from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_constraint_type import DataConstraintType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataConstraintsType:
    """
    DataConstraintsType describes the structure of the data constraints
    container.

    It contains one or more data constraint, which can be explicitly
    detailed or referenced from an external structure document or registry
    service. This container may contain both attachment and content
    constraints.

    :ivar data_constraint: DataConstraint specifies a sub set of the
        definition of the allowable or available content of a data set
        in terms of the content or in terms of the set of key
        combinations.
    """

    data_constraint: tuple[DataConstraintType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DataConstraint",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
