from __future__ import annotations

from dataclasses import dataclass

from .abstract_discovery_delivery_structure import (
    AbstractDiscoveryDeliveryStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractDiscoveryDelivery(AbstractDiscoveryDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
