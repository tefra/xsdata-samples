from __future__ import annotations

from dataclasses import dataclass

from .service_delivery_structure import ServiceDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceDelivery(ServiceDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
