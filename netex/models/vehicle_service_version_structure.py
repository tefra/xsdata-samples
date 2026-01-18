from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .vehicle_service_parts_rel_structure import (
    VehicleServicePartsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServiceVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleService_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_service_parts: VehicleServicePartsRelStructure | None = field(
        default=None,
        metadata={
            "name": "vehicleServiceParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
