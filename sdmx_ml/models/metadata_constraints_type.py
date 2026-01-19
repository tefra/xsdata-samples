from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.metadata_constraint_type import MetadataConstraintType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class MetadataConstraintsType:
    """
    MetadataConstraintsType describes the structure of the metadata
    constraints container.

    It contains one or more metadata constraint, which can be explicitly
    detailed or referenced from an external structure document or registry
    service. This container may contain both attachment and content
    constraints.

    :ivar metadata_constraint: MetadataConstraint specifies a subset of
        the definition of the allowable content of a metadata set.
    """

    metadata_constraint: tuple[MetadataConstraintType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MetadataConstraint",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
        },
    )
