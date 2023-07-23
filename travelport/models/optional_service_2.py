from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.option_journey_details import OptionJourneyDetails

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class OptionalService2:
    """
    Featues/Optionals supported with the cruise booked.

    Parameters
    ----------
    option_journey_details
        Contains PickUp Return Details for that Cruise Option Service.
    booking_traveler_ref
    feature_type
        Type of Optional Service. F: Feature, O: Option
    status
        Status of of the Optional Service
    quantity
        Number of Features/Options Requested.
    provider_defined_type
        Unique ID on vendors system
    description
        Descriptive Name of Feature or Option
    start_date
        Feature/Option Begin Date
    end_date
        Feature/Option End Date
    booking_date
        Date Cruise Booked
    set_identifier
        Feature/Option Unique ID Examples: B2NOXFR
    set_name
        Feature/Option Set Name Examples: PRE-CRUISE
    total_price
        Feature/Option Price
    transport_indicator
        Whether Features/ Options Affects TransportationIndicator. True -
        This Feature or Option group affects transportation False - This
        Feature or Option group does not affect transportation.
    air_city_indicator
        Feature/option is air or city dependent.
    purchase_indicator
        Option purchased by someone other than the passenger
    """
    class Meta:
        name = "OptionalService"
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    option_journey_details: None | OptionJourneyDetails = field(
        default=None,
        metadata={
            "name": "OptionJourneyDetails",
            "type": "Element",
        }
    )
    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
    feature_type: None | str = field(
        default=None,
        metadata={
            "name": "FeatureType",
            "type": "Attribute",
            "required": True,
            "length": 1,
        }
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "length": 2,
            "white_space": "collapse",
        }
    )
    quantity: None | int = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Attribute",
        }
    )
    provider_defined_type: None | str = field(
        default=None,
        metadata={
            "name": "ProviderDefinedType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 25,
        }
    )
    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        }
    )
    end_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Attribute",
        }
    )
    booking_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Attribute",
        }
    )
    set_identifier: None | str = field(
        default=None,
        metadata={
            "name": "SetIdentifier",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        }
    )
    set_name: None | str = field(
        default=None,
        metadata={
            "name": "SetName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        }
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    transport_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "TransportIndicator",
            "type": "Attribute",
        }
    )
    air_city_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "AirCityIndicator",
            "type": "Attribute",
        }
    )
    purchase_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "PurchaseIndicator",
            "type": "Attribute",
        }
    )
