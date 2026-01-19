from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.region_type import RegionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class CubeRegionType(RegionType):
    """
    CubeRegionType defines the structure of a data cube region.

    This is based on the abstract RegionType and simply refines the key and
    attribute values to conform with what is applicable for dimensions and
    attributes, respectively. See the documentation of the base type for
    more details on how a region is defined.
    """

    valid_from: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    valid_to: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
