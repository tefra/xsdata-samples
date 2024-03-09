from dataclasses import dataclass

from .service_delivery_error_condition_structure import (
    ServiceDeliveryErrorConditionStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceDeliveryErrorConditionElement(
    ServiceDeliveryErrorConditionStructure
):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
