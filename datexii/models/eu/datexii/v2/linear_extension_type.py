from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.openlr_extended_linear import OpenlrExtendedLinear

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LinearExtensionType:
    class Meta:
        name = "_LinearExtensionType"

    openlr_extended_linear: Optional[OpenlrExtendedLinear] = field(
        default=None,
        metadata={
            "name": "openlrExtendedLinear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
