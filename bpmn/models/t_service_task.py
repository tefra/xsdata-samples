from __future__ import annotations

from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from .t_implementation_value import TImplementationValue
from .t_task import TTask

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TServiceTask(TTask):
    class Meta:
        name = "tServiceTask"

    implementation: str | TImplementationValue = field(
        default=TImplementationValue.WEB_SERVICE,
        metadata={
            "type": "Attribute",
        },
    )
    operation_ref: QName | None = field(
        default=None,
        metadata={
            "name": "operationRef",
            "type": "Attribute",
        },
    )
