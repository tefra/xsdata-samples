from dataclasses import dataclass, field
from typing import Dict, Optional
from generali.models.org.w3.pkg_2006.pkg_02.addressing.wsdl.anonymous_type import AnonymousType

__NAMESPACE__ = "http://www.w3.org/2006/02/addressing/wsdl"


@dataclass
class Anonymous:
    class Meta:
        namespace = "http://www.w3.org/2006/02/addressing/wsdl"

    value: Optional[AnonymousType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
