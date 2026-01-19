from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.dimension_constraint_type import DimensionConstraintType
from sdmx_ml.models.structure_usage_type import StructureUsageType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DataflowBaseType(StructureUsageType):
    """
    Extends StructureUsageType by adding a DimensionConstraint.

    :ivar dimension_constraint: Required when the referenced Data
        Structure can change Dimensionality under a minor version
        change.
    """

    dimension_constraint: None | DimensionConstraintType = field(
        default=None,
        metadata={
            "name": "DimensionConstraint",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
        },
    )
