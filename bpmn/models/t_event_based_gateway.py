from dataclasses import dataclass, field
from .t_event_based_gateway_type import TEventBasedGatewayType
from .t_gateway import TGateway

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TEventBasedGateway(TGateway):
    class Meta:
        name = "tEventBasedGateway"

    instantiate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    event_gateway_type: TEventBasedGatewayType = field(
        default=TEventBasedGatewayType.EXCLUSIVE,
        metadata={
            "name": "eventGatewayType",
            "type": "Attribute",
        },
    )
