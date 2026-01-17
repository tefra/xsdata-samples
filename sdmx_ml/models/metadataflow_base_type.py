from dataclasses import dataclass

from sdmx_ml.models.structure_usage_type import StructureUsageType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataflowBaseType(StructureUsageType):
    """
    MetadataflowBaseType is an abstract base type that serves as the basis
    for the MetadataflowType.

    It restricts the structure to reference a metadata structure
    definition.
    """
