from __future__ import annotations

from dataclasses import dataclass, field

from .font import Font
from .style import Style

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


@dataclass(kw_only=True)
class BpmnlabelStyle(Style):
    class Meta:
        name = "BPMNLabelStyle"
        namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

    font: Font = field(
        metadata={
            "name": "Font",
            "type": "Element",
            "namespace": "http://www.omg.org/spec/DD/20100524/DC",
            "required": True,
        }
    )
