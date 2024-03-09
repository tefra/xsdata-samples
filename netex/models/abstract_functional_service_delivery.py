from dataclasses import dataclass

from .abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractFunctionalServiceDelivery(AbstractServiceDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
