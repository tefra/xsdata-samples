from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.metadata_constraint_base_type import (
    MetadataConstraintBaseType,
)
from sdmx_ml.models.metadata_target_region_type import MetadataTargetRegionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataConstraintType(MetadataConstraintBaseType):
    """
    MetadataConstraintType defines the structure of a metadata constraint.

    A metadata constraint can specify allowed attribute values for metadata
    described by the constrained artefact.

    :ivar metadata_target_region: MetadataTargetRegion describes the
        values allowed for metadata attributes.
    """

    metadata_target_region: tuple[MetadataTargetRegionType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MetadataTargetRegion",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "max_occurs": 2,
        },
    )
