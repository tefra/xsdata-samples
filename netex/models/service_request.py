from collections.abc import Iterable
from dataclasses import dataclass, field

from .data_object_request import DataObjectRequest
from .service_request_structure import ServiceRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceRequest(ServiceRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    data_object_request: Iterable[DataObjectRequest] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
