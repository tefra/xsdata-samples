from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TMultiInstanceFlowCondition(Enum):
    NONE = "None"
    ONE = "One"
    ALL = "All"
    COMPLEX = "Complex"
