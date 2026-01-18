from __future__ import annotations

from dataclasses import dataclass, field

from .t_gateway import TGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TExclusiveGateway(TGateway):
    class Meta:
        name = "tExclusiveGateway"

    default: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
