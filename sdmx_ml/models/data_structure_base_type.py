from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.structure_type_abstract import StructureTypeAbstract

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataStructureBaseType(StructureTypeAbstract):
    """DataStructureBaseType describes base refinement of the StructureType for a
    data structure definition.

    A data structure definition is defined as a collection of metadata
    concepts, their structure and usage when used to collect or
    disseminate data.
    """

    metadata_structure_components: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
