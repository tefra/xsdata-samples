from dataclasses import dataclass, field
from typing import Dict, List, Optional
from generali.models.org.w3.pkg_2005.pkg_08.addressing.attributed_uritype import (
    AttributedUritype,
)
from generali.models.org.w3.pkg_2005.pkg_08.addressing.metadata import Metadata
from generali.models.org.w3.pkg_2005.pkg_08.addressing.reference_parameters import (
    ReferenceParameters,
)

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class EndpointReferenceType:
    address: Optional[AttributedUritype] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
            "required": True,
        },
    )
    reference_parameters: Optional[ReferenceParameters] = field(
        default=None,
        metadata={
            "name": "ReferenceParameters",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    metadata: Optional[Metadata] = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
