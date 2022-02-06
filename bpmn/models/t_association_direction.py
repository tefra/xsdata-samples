from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TAssociationDirection(Enum):
    NONE = "None"
    ONE = "One"
    BOTH = "Both"
