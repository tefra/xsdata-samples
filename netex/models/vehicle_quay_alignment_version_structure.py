from dataclasses import dataclass, field
from typing import Optional, Union
from .entity_in_version_structure import VersionedChildStructure
from .quay_ref import QuayRef
from .taxi_stand_ref import TaxiStandRef
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleQuayAlignmentVersionStructure(VersionedChildStructure):
    class Meta:
        name = "VehicleQuayAlignment_VersionStructure"

    vehicle_stopping_place_ref: Optional[VehicleStoppingPlaceRef] = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_ref: Optional[Union[TaxiStandRef, QuayRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiStandRef",
                    "type": TaxiStandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QuayRef",
                    "type": QuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
