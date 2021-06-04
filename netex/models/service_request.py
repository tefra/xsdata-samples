from dataclasses import dataclass, field
from typing import List
from netex.models.abstract_functional_service_request import AbstractFunctionalServiceRequest
from netex.models.data_object_request import DataObjectRequest
from netex.models.service_request_structure import ServiceRequestStructure

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
            "min_occurs": 1,
        }
    )
    abstract_functional_service_request: List[AbstractFunctionalServiceRequest] = field(
        default_factory=list,
        metadata={
            "name": "AbstractFunctionalServiceRequest",
            "type": "Element",
            "min_occurs": 1,
        }
    )
