from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_implementation_value import TImplementationValue
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass(kw_only=True)
class TReceiveTask(TTask):
    class Meta:
        name = "tReceiveTask"

    implementation: str | TImplementationValue = field(
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
    message_ref: None | QName = field(
        default=None,
        metadata={
            "name": "messageRef",
            "type": "Attribute",
        },
    )
    operation_ref: None | QName = field(
        default=None,
        metadata={
            "name": "operationRef",
            "type": "Attribute",
        },
    )
