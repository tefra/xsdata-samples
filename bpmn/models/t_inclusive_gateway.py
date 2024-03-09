from dataclasses import dataclass, field
from typing import Optional

from .t_gateway import TGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TInclusiveGateway(TGateway):
    class Meta:
        name = "tInclusiveGateway"

    default: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
