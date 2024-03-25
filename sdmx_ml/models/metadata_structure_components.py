from dataclasses import dataclass

from sdmx_ml.models.metadata_structure_components_type import (
    MetadataStructureComponentsType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataStructureComponents(MetadataStructureComponentsType):
    """
    MetadataStructureComponents defines the grouping of the sets of the components
    that make up the metadata structure definition.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
