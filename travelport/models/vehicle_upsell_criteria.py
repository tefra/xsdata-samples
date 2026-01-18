from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.vehicle_upsell_add import VehicleUpsellAdd
from travelport.models.vehicle_upsell_delete import VehicleUpsellDelete
from travelport.models.vehicle_upsell_update import VehicleUpsellUpdate

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class VehicleUpsellCriteria:
    """
    Wraps all Upsell Admin commands related to Vehicle.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    vehicle_upsell_add: list[VehicleUpsellAdd] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellAdd",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_upsell_update: list[VehicleUpsellUpdate] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellUpdate",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_upsell_delete: list[VehicleUpsellDelete] = field(
        default_factory=list,
        metadata={
            "name": "VehicleUpsellDelete",
            "type": "Element",
            "max_occurs": 999,
        },
    )
