from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.data_structure_representation_type import (
    DataStructureRepresentationType,
)
from sdmx_ml.models.unbounded_code_type import UnboundedCodeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class SimpleDataStructureRepresentationType(DataStructureRepresentationType):
    """
    SimpleDataStructureRepresentationType defines the representation for
    any non-time dimension data structure definition component.
    """

    max_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
