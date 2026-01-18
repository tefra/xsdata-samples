from __future__ import annotations

from dataclasses import dataclass

from .mobility_service_version_structure import MobilityServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehiclePoolingService2(MobilityServiceVersionStructure):
    class Meta:
        name = "VehiclePoolingService_"
        namespace = "http://www.netex.org.uk/netex"
