from dataclasses import dataclass, field
from typing import List, Optional
from .resource_parameter import ResourceParameter
from .t_root_element import TRootElement

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TResource(TRootElement):
    class Meta:
        name = "tResource"

    resource_parameter: List[ResourceParameter] = field(
        default_factory=list,
        metadata={
            "name": "resourceParameter",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
