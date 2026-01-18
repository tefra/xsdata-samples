from __future__ import annotations

from dataclasses import dataclass, field

from .t_gateway import TGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TInclusiveGateway(TGateway):
    class Meta:
        name = "tInclusiveGateway"

    default: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
