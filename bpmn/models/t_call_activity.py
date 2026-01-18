from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_activity import TActivity

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TCallActivity(TActivity):
    class Meta:
        name = "tCallActivity"

    called_element: None | QName = field(
        default=None,
        metadata={
            "name": "calledElement",
            "type": "Attribute",
        },
    )
