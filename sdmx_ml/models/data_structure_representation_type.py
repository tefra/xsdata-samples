from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.representation_type import RepresentationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataStructureRepresentationType(RepresentationType):
    """
    DataStructureRepresentationType is an abstract base type which defines
    the allowable representations for any data structure definition
    component.

    The enumeration must be restricted to the proper type for item scheme
    for a given component.
    """

    min_occurs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
