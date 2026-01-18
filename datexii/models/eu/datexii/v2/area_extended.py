from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.named_area import NamedArea
from datexii.models.eu.datexii.v2.polygon_area import PolygonArea

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AreaExtended:
    """
    Extension class for area used in parking publication extension.
    """

    named_area: NamedArea | None = field(
        default=None,
        metadata={
            "name": "namedArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    polygon_area: list[PolygonArea] = field(
        default_factory=list,
        metadata={
            "name": "polygonArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
