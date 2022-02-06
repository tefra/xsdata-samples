from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TGatewayDirection(Enum):
    UNSPECIFIED = "Unspecified"
    CONVERGING = "Converging"
    DIVERGING = "Diverging"
    MIXED = "Mixed"
