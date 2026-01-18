from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .garage_point_ref_structure import GaragePointRefStructure
from .multilingual_string import MultilingualString
from .vehicle_service_ref import VehicleServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServicePartVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleServicePart_VersionStructure"

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
    vehicle_service_ref: VehicleServiceRef | None = field(
        default=None,
        metadata={
            "name": "VehicleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_point_ref: GaragePointRefStructure | None = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_point_ref: GaragePointRefStructure | None = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
