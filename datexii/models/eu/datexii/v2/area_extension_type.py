from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.area_extended import AreaExtended
from datexii.models.eu.datexii.v2.openlr_extended_area import (
    OpenlrExtendedArea,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AreaExtensionType:
    class Meta:
        name = "_AreaExtensionType"

    openlr_extended_area: Optional[OpenlrExtendedArea] = field(
        default=None,
        metadata={
            "name": "openlrExtendedArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    area_extended: Optional[AreaExtended] = field(
        default=None,
        metadata={
            "name": "areaExtended",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
