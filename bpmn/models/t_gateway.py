from __future__ import annotations

from dataclasses import dataclass, field

from .t_flow_node import TFlowNode
from .t_gateway_direction import TGatewayDirection

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TGateway(TFlowNode):
    class Meta:
        name = "tGateway"

    gateway_direction: TGatewayDirection = field(
        default=TGatewayDirection.UNSPECIFIED,
        metadata={
            "name": "gatewayDirection",
            "type": "Attribute",
        },
    )
