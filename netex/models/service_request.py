from dataclasses import dataclass, field
from typing import List
from .data_object_request import DataObjectRequest
from .service_request_structure import ServiceRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceRequest(ServiceRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    data_object_request: List[DataObjectRequest] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
