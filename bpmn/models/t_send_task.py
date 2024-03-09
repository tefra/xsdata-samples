from dataclasses import dataclass, field
from typing import Optional, Union
from xml.etree.ElementTree import QName

from .t_implementation_value import TImplementationValue
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TSendTask(TTask):
    class Meta:
        name = "tSendTask"

    implementation: Union[str, TImplementationValue] = field(
        default=TImplementationValue.WEB_SERVICE,
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
