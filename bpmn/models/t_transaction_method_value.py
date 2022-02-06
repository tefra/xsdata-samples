from enum import Enum

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


class TTransactionMethodValue(Enum):
    COMPENSATE = "##Compensate"
    IMAGE = "##Image"
    STORE = "##Store"
