from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_structure_components import DataStructureComponents
from sdmx_ml.models.maintainable_type import MaintainableType
from sdmx_ml.models.metadata_structure_components import (
    MetadataStructureComponents,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class StructureTypeAbstract(MaintainableType):
    """
    StructureType is an abstract base type for all structure objects.

    Concrete instances of this should restrict to a concrete grouping.
    """

    class Meta:
        name = "StructureType"

    metadata_structure_components_or_data_structure_components: (
        None | MetadataStructureComponents | DataStructureComponents
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MetadataStructureComponents",
                    "type": MetadataStructureComponents,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "DataStructureComponents",
                    "type": DataStructureComponents,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
