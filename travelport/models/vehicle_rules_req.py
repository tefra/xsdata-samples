from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_search_req_1 import BaseSearchReq1
from travelport.models.vehicle_date_location import VehicleDateLocation
from travelport.models.vehicle_search_modifiers import VehicleSearchModifiers

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleRulesReq(BaseSearchReq1):
    """
    Used to request  rules for a specific vehicle and rate.

    Parameters
    ----------
    vehicle_reservation_locator_code
        Request vehicle rules using Locator code of existing vehicle
        reservation.
    vehicle_rules_lookup
        Details to request Vehicle rate rules post shopping request.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    vehicle_reservation_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "VehicleReservationLocatorCode",
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
        },
    )
    vehicle_rules_lookup: None | VehicleRulesReq.VehicleRulesLookup = field(
        default=None,
        metadata={
            "name": "VehicleRulesLookup",
            "type": "Element",
        },
    )

    @dataclass
    class VehicleRulesLookup:
        vehicle_date_location: None | VehicleDateLocation = field(
            default=None,
            metadata={
                "name": "VehicleDateLocation",
                "type": "Element",
                "required": True,
            },
        )
        vehicle_search_modifiers: None | VehicleSearchModifiers = field(
            default=None,
            metadata={
                "name": "VehicleSearchModifiers",
                "type": "Element",
                "required": True,
            },
        )
