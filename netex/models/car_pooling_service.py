from __future__ import annotations

from dataclasses import dataclass

from .car_pooling_service_version_structure import (
    CarPoolingServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarPoolingService(CarPoolingServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
