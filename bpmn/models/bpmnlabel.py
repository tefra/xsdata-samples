from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .label import Label

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


@dataclass(kw_only=True)
class Bpmnlabel(Label):
    class Meta:
        name = "BPMNLabel"
        namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

    label_style: None | QName = field(
        default=None,
        metadata={
            "name": "labelStyle",
            "type": "Attribute",
        },
    )
