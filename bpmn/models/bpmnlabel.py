from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from .label import Label

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


@dataclass
class Bpmnlabel(Label):
    class Meta:
        name = "BPMNLabel"
        namespace = "http://www.omg.org/spec/BPMN/20100524/DI"

    label_style: QName | None = field(
        default=None,
        metadata={
            "name": "labelStyle",
            "type": "Attribute",
        },
    )
