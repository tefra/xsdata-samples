from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TDocumentation:
    class Meta:
        name = "tDocumentation"

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    text_format: str = field(
        default="text/plain",
        metadata={
            "name": "textFormat",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
