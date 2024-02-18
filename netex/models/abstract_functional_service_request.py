from dataclasses import dataclass
from .abstract_functional_service_request_structure import (
    AbstractFunctionalServiceRequestStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractFunctionalServiceRequest(
    AbstractFunctionalServiceRequestStructure
):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
