from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.type_base_preference_2 import TypeBasePreference2
from travelport.models.type_geo_political_area_type_2 import (
    TypeGeoPoliticalAreaType2,
)
from travelport.models.type_rail_coach_compartment_2 import (
    TypeRailCoachCompartment2,
)
from travelport.models.type_rail_gender_compartment_2 import (
    TypeRailGenderCompartment2,
)
from travelport.models.type_rail_seat_arrangement_2 import (
    TypeRailSeatArrangement2,
)
from travelport.models.type_rail_seating_2 import TypeRailSeating2
from travelport.models.type_rail_ticket_fulfillment_option_2 import (
    TypeRailTicketFulfillmentOption2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class RailPreference2(TypeBasePreference2):
    """
    Defines a preference for a particular set of criteria for rail (e.g.,
    dates, compartment type).

    Parameters
    ----------
    account_code
    arrival_geo_political_area_type
        Util: ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    arrival_geo_political_area_code
        Util: ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    bench_mark_amount
    connection_geo_political_area_type
        Util: ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    connection_geo_political_area_code
        Util: ReferenceDataRetrieveReq, TypeCodes  Airport, City Airport,
        City, Country, StateProvince and GeoPoliticalAreaType
    contract_code
    corporate_id
    pseudo_city_code
    travel_start_date
        A valid date in YYYY-MM-DD format.
    travel_end_date
        A valid date in YYYY-MM-DD format.
    domestic_trip_journey_hours
    starting_train_number
    ending_train_number
    international_trip_journey_hours
    max_employees_per_train
    max_fare_amount
        See uAPI Profile Help.
    cabin_type
        Util: ReferenceDataRetrieveReq, TypeCode RailCabinType
    gender_compartment_type
    coach_compartment_type
    seat_arrangement_type
    seating_type
    seat_position_misc_travel
        Util:ReferenceDataRetrieveReq, TypeCode AirAndRailMiscType
    seat_position_ref_category
    smoking
    ticket_fulfillment_type
    """

    class Meta:
        name = "RailPreference"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    account_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    arrival_geo_political_area_type: None | TypeGeoPoliticalAreaType2 = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaType",
            "type": "Attribute",
        },
    )
    arrival_geo_political_area_code: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    bench_mark_amount: None | str = field(
        default=None,
        metadata={
            "name": "BenchMarkAmount",
            "type": "Attribute",
        },
    )
    connection_geo_political_area_type: None | TypeGeoPoliticalAreaType2 = (
        field(
            default=None,
            metadata={
                "name": "ConnectionGeoPoliticalAreaType",
                "type": "Attribute",
            },
        )
    )
    connection_geo_political_area_code: None | str = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    contract_code: None | str = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    corporate_id: None | str = field(
        default=None,
        metadata={
            "name": "CorporateID",
            "type": "Attribute",
            "max_length": 25,
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    travel_start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TravelStartDate",
            "type": "Attribute",
        },
    )
    travel_end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TravelEndDate",
            "type": "Attribute",
        },
    )
    domestic_trip_journey_hours: None | int = field(
        default=None,
        metadata={
            "name": "DomesticTripJourneyHours",
            "type": "Attribute",
        },
    )
    starting_train_number: None | str = field(
        default=None,
        metadata={
            "name": "StartingTrainNumber",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    ending_train_number: None | str = field(
        default=None,
        metadata={
            "name": "EndingTrainNumber",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    international_trip_journey_hours: None | int = field(
        default=None,
        metadata={
            "name": "InternationalTripJourneyHours",
            "type": "Attribute",
        },
    )
    max_employees_per_train: None | int = field(
        default=None,
        metadata={
            "name": "MaxEmployeesPerTrain",
            "type": "Attribute",
        },
    )
    max_fare_amount: None | str = field(
        default=None,
        metadata={
            "name": "MaxFareAmount",
            "type": "Attribute",
        },
    )
    cabin_type: None | str = field(
        default=None,
        metadata={
            "name": "CabinType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    gender_compartment_type: None | TypeRailGenderCompartment2 = field(
        default=None,
        metadata={
            "name": "GenderCompartmentType",
            "type": "Attribute",
        },
    )
    coach_compartment_type: None | TypeRailCoachCompartment2 = field(
        default=None,
        metadata={
            "name": "CoachCompartmentType",
            "type": "Attribute",
        },
    )
    seat_arrangement_type: None | TypeRailSeatArrangement2 = field(
        default=None,
        metadata={
            "name": "SeatArrangementType",
            "type": "Attribute",
        },
    )
    seating_type: None | TypeRailSeating2 = field(
        default=None,
        metadata={
            "name": "SeatingType",
            "type": "Attribute",
        },
    )
    seat_position_misc_travel: None | str = field(
        default=None,
        metadata={
            "name": "SeatPositionMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    seat_position_ref_category: None | str = field(
        default=None,
        metadata={
            "name": "SeatPositionRefCategory",
            "type": "Attribute",
            "max_length": 3,
        },
    )
    smoking: bool = field(
        default=False,
        metadata={
            "name": "Smoking",
            "type": "Attribute",
        },
    )
    ticket_fulfillment_type: None | TypeRailTicketFulfillmentOption2 = field(
        default=None,
        metadata={
            "name": "TicketFulfillmentType",
            "type": "Attribute",
        },
    )
