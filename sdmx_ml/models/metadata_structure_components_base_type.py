from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.grouping_type import GroupingType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataStructureComponentsBaseType(GroupingType):
    """
    MetadataStructureComponentsBaseType is an abstract base type that forms the
    basis for the MetadataStructureComponentsType.
    """

    choice: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
