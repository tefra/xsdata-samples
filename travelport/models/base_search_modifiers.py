from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_date_spec import TypeDateSpec

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class BaseSearchModifiers:
    """
    Controls and switches for the Universal Record Search and Saved Trip search
    request.

    Parameters
    ----------
    travel_date
        Matched with flight departure date or hotel check-in date or vehicle
        pick-up date. For Rail, travel date should be between journey start
        and end dates, Cannot be combined with any date in product level
        ReservationCriteria
    include_all_names
        If true, include all the passenger names in the results. Otherwise
        include only the name of the primary passenger.
    include_agent_info
        Include information about the agent who created, modified or
        ticketed the Universal Record.
    max_results
    start_from_result
    exclude_air
        Exclude Air reservations from the results
    exclude_vehicle
        Exclude Vehicle reservations from the results
    exclude_hotel
        Exclude Hotel reservations from the results.
    """
    travel_date: None | TypeDateSpec = field(
        default=None,
        metadata={
            "name": "TravelDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/universal_v52_0",
        }
    )
    include_all_names: bool = field(
        default=False,
        metadata={
            "name": "IncludeAllNames",
            "type": "Attribute",
        }
    )
    include_agent_info: bool = field(
        default=False,
        metadata={
            "name": "IncludeAgentInfo",
            "type": "Attribute",
        }
    )
    max_results: int = field(
        default=20,
        metadata={
            "name": "MaxResults",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 200,
        }
    )
    start_from_result: None | int = field(
        default=None,
        metadata={
            "name": "StartFromResult",
            "type": "Attribute",
            "min_inclusive": 1,
        }
    )
    exclude_air: bool = field(
        default=False,
        metadata={
            "name": "ExcludeAir",
            "type": "Attribute",
        }
    )
    exclude_vehicle: bool = field(
        default=False,
        metadata={
            "name": "ExcludeVehicle",
            "type": "Attribute",
        }
    )
    exclude_hotel: bool = field(
        default=False,
        metadata={
            "name": "ExcludeHotel",
            "type": "Attribute",
        }
    )
