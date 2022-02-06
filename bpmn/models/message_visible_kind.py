from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/DI"


class MessageVisibleKind(Enum):
    INITIATING = "initiating"
    NON_INITIATING = "non_initiating"
