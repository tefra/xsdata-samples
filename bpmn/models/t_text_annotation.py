from dataclasses import dataclass, field
from typing import Optional

from .t_artifact import TArtifact
from .text import Text

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TTextAnnotation(TArtifact):
    class Meta:
        name = "tTextAnnotation"

    text: Text | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.omg.org/spec/BPMN/20100524/MODEL",
        },
    )
    text_format: str = field(
        default="text/plain",
        metadata={
            "name": "textFormat",
            "type": "Attribute",
        },
    )
