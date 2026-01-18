from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import VersionedChildStructure
from .quay_ref import QuayRef
from .taxi_stand_ref import TaxiStandRef
from .vehicle_stopping_place_ref import VehicleStoppingPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleQuayAlignmentVersionStructure(VersionedChildStructure):
    class Meta:
        name = "VehicleQuayAlignment_VersionStructure"

    vehicle_stopping_place_ref: None | VehicleStoppingPlaceRef = field(
        default=None,
        metadata={
            "name": "VehicleStoppingPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quay_ref: None | TaxiStandRef | QuayRef = field(
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
    order: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
