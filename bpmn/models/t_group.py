from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName
from .t_artifact import TArtifact

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TGroup(TArtifact):
    class Meta:
        name = "tGroup"

    category_value_ref: Optional[QName] = field(
        default=None,
        metadata={
            "name": "categoryValueRef",
            "type": "Attribute",
        }
    )
