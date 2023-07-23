from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_air_fare_1 import TypeAirFare1
from travelport.models.type_base_preference_1 import TypeBasePreference1
from travelport.models.type_geo_political_area_type_1 import TypeGeoPoliticalAreaType1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AirPreference1(TypeBasePreference1):
    """
    Defines an air preference for a particular set of criteria (e.g. dates,
    supplier, etc.).

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
    air_fare_type
    cabin_type_misc_travel
        : Util:ReferenceDataRetrieveReq, TypeCode AirAndRailMiscType
    cabin_type_ref_category
        : Util:ReferenceDataRetrieveReq, TypeCode AirAndRailMiscType
    starting_flight_number
    ending_flight_number
    interline
    max_fare_amount
        See uAPI Profile Help.
    max_connection_minutes
    max_employees_per_flight
    max_domestic_trip_hours
    max_international_trip_hours
    seat_number
    seat_type_misc_travel
        : Util:ReferenceDataRetrieveReq, TypeCode AirAndRailMiscType
    seat_type_misc_ref_category
        : Util:ReferenceDataRetrieveReq, TypeCode AirAndRailMiscType
    crscode
        Required if transmitting an SSR Code. Values are 1G or 1V
    ssrcode
        a. ReferenceDataSearchReq Type  SsrType
    """
    class Meta:
        name = "AirPreference"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    account_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    arrival_geo_political_area_type: None | TypeGeoPoliticalAreaType1 = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    arrival_geo_political_area_code: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    bench_mark_amount: None | str = field(
        default=None,
        metadata={
            "name": "BenchMarkAmount",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_type: None | TypeGeoPoliticalAreaType1 = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaType",
            "type": "Attribute",
        }
    )
    connection_geo_political_area_code: None | str = field(
        default=None,
        metadata={
            "name": "ConnectionGeoPoliticalAreaCode",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    contract_code: None | str = field(
        default=None,
        metadata={
            "name": "ContractCode",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    corporate_id: None | str = field(
        default=None,
        metadata={
            "name": "CorporateID",
            "type": "Attribute",
            "max_length": 25,
        }
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        }
    )
    travel_start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TravelStartDate",
            "type": "Attribute",
        }
    )
    travel_end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "TravelEndDate",
            "type": "Attribute",
        }
    )
    air_fare_type: None | TypeAirFare1 = field(
        default=None,
        metadata={
            "name": "AirFareType",
            "type": "Attribute",
        }
    )
    cabin_type_misc_travel: None | str = field(
        default=None,
        metadata={
            "name": "CabinTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    cabin_type_ref_category: str = field(
        default="ASC",
        metadata={
            "name": "CabinTypeRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    starting_flight_number: None | str = field(
        default=None,
        metadata={
            "name": "StartingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    ending_flight_number: None | str = field(
        default=None,
        metadata={
            "name": "EndingFlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    interline: bool = field(
        default=False,
        metadata={
            "name": "Interline",
            "type": "Attribute",
        }
    )
    max_fare_amount: None | str = field(
        default=None,
        metadata={
            "name": "MaxFareAmount",
            "type": "Attribute",
        }
    )
    max_connection_minutes: None | int = field(
        default=None,
        metadata={
            "name": "MaxConnectionMinutes",
            "type": "Attribute",
        }
    )
    max_employees_per_flight: None | int = field(
        default=None,
        metadata={
            "name": "MaxEmployeesPerFlight",
            "type": "Attribute",
        }
    )
    max_domestic_trip_hours: None | int = field(
        default=None,
        metadata={
            "name": "MaxDomesticTripHours",
            "type": "Attribute",
        }
    )
    max_international_trip_hours: None | int = field(
        default=None,
        metadata={
            "name": "MaxInternationalTripHours",
            "type": "Attribute",
        }
    )
    seat_number: None | str = field(
        default=None,
        metadata={
            "name": "SeatNumber",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    seat_type_misc_travel: None | str = field(
        default=None,
        metadata={
            "name": "SeatTypeMiscTravel",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    seat_type_misc_ref_category: str = field(
        default="ASS",
        metadata={
            "name": "SeatTypeMiscRefCategory",
            "type": "Attribute",
            "max_length": 3,
        }
    )
    crscode: None | str = field(
        default=None,
        metadata={
            "name": "CRSCode",
            "type": "Attribute",
            "max_length": 2,
        }
    )
    ssrcode: None | str = field(
        default=None,
        metadata={
            "name": "SSRCode",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 4,
        }
    )
