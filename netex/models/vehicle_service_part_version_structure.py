from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .garage_point_ref_structure import GaragePointRefStructure
from .multilingual_string import MultilingualString
from .vehicle_service_ref import VehicleServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleServicePartVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleServicePart_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_service_ref: Optional[VehicleServiceRef] = field(
        default=None,
        metadata={
            "name": "VehicleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start_point_ref: Optional[GaragePointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_point_ref: Optional[GaragePointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
