from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TRelationshipDirection(Enum):
    NONE = "None"
    FORWARD = "Forward"
    BACKWARD = "Backward"
    BOTH = "Both"
