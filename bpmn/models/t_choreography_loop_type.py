from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TChoreographyLoopType(Enum):
    NONE = "None"
    STANDARD = "Standard"
    MULTI_INSTANCE_SEQUENTIAL = "MultiInstanceSequential"
    MULTI_INSTANCE_PARALLEL = "MultiInstanceParallel"
