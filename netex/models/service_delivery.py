from __future__ import annotations

from dataclasses import dataclass

from .service_delivery_structure import ServiceDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceDelivery(ServiceDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
