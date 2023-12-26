from dataclasses import dataclass, field
from typing import Dict, List

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class ReferenceParametersType:
    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
