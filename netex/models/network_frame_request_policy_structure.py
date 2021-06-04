from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from netex.models.output_detail_enumeration import OutputDetailEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkFrameRequestPolicyStructure:
    maximum_number_of_elements: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    include_deleted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IncludeDeleted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    urgency: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Urgency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    must_have_by: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "MustHaveBy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    request_detail: List[OutputDetailEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "RequestDetail",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
