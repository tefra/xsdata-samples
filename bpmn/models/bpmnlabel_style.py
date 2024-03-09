from dataclasses import dataclass, field
from typing import Optional

from .font import Font
from .style import Style

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


@dataclass
class BpmnlabelStyle(Style):
    class Meta:
        name = "BPMNLabelStyle"
        namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

    font: Optional[Font] = field(
        default=None,
        metadata={
            "name": "Font",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/DD/20100524/DC",
            "required": True,
        },
    )
