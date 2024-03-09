from dataclasses import dataclass, field
from typing import Optional, Union
from xml.etree.ElementTree import QName

from .t_implementation_value import TImplementationValue
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TReceiveTask(TTask):
    class Meta:
        name = "tReceiveTask"

    implementation: Union[str, TImplementationValue] = field(
        default=TImplementationValue.WEB_SERVICE,
        metadata={
            "type": "Attribute",
        },
    )
    instantiate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    message_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "messageRef",
            "type": "Attribute",
        },
    )
    operation_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "operationRef",
            "type": "Attribute",
        },
    )
