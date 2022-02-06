from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TProcessType(Enum):
    NONE = "None"
    PUBLIC = "Public"
    PRIVATE = "Private"
