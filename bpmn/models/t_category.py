from dataclasses import dataclass, field
from typing import List, Optional

from .category_value import CategoryValue
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCategory(TRootElement):
    class Meta:
        name = "tCategory"

    category_value: List[CategoryValue] = field(
        default_factory=list,
        metadata={
            "name": "categoryValue",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
