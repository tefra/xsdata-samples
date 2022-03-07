from dataclasses import dataclass, field
from typing import Dict

__NAMESPACE__ = "http://www.w3.org/2006/02/addressing/wsdl"


@dataclass
class UsingAddressing:
    class Meta:
        namespace = "http://www.w3.org/2006/02/addressing/wsdl"

    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
