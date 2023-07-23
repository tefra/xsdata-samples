from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.air_avail_info import AirAvailInfo
from travelport.models.alternate_location_distance_ref import AlternateLocationDistanceRef
from travelport.models.codeshare_info import CodeshareInfo
from travelport.models.connection import Connection
from travelport.models.flight_details import FlightDetails
from travelport.models.flight_details_ref import FlightDetailsRef
from travelport.models.rail_coach_details import RailCoachDetails
from travelport.models.segment_1 import Segment1
from travelport.models.sponsored_flt_info import SponsoredFltInfo
from travelport.models.type_eticketability import TypeEticketability

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeBaseAirSegment(Segment1):
    """
    Parameters
    ----------
    sponsored_flt_info
    codeshare_info
    air_avail_info
    flight_details
    flight_details_ref
    alternate_location_distance_ref
    connection
    sell_message
    rail_coach_details
    open_segment
        Indicates OpenSegment when True
    group
        The Origin Destination Grouping of this segment.
    carrier
        The carrier that is marketing this segment
    cabin_class
        Specifies Cabin class for a group of class of services. Cabin class
        is not identified if it is not present.
    flight_number
        The flight number under which the marketing carrier is marketing
        this flight
    origin
        The IATA location code for this origination of this entity.
    destination
        The IATA location code for this destination of this entity.
    departure_time
        The date and time at which this entity departs. Date and time are
        represented as Airport Local Time at the place of departure. The
        correct time zone offset is also included.
    arrival_time
        The date and time at which this entity arrives at the destination.
        Date and time are represented as Airport Local Time at the place of
        arrival. The correct time zone offset is also included.
    flight_time
        Time spent (minutes) traveling in flight, including airport taxi
        time.
    travel_time
        Total time spent (minutes) traveling including flight time and
        ground time.
    distance
        The distance traveled. Units are specified in the parent response
        element.
    provider_code
    supplier_code
    participant_level
        Type of sell agreement between host and link carrier.
    link_availability
        Indicates if carrier has link (carrier specific) display option.
    polled_availability_option
        Indicates if carrier has Inside (polled)Availability option.
    availability_display_type
        The type of availability from which the segment is sold.Possible
        Values (List): G - General S - Flight Specific L - Carrier
        Specific/Direct Access M - Manual Sell F - Fare Shop/Optimal Shop Q
        - Fare Specific Fare Quote unbooked R - Redemption Availability used
        to complete the sell. Supported Providers: 1G,1V.
    class_of_service
    eticketability
        Identifies if this particular segment is E-Ticketable
    equipment
        Identifies the equipment that this segment is operating under.
    marriage_group
        Identifies this segment as being a married segment. It is paired
        with other segments of the same value.
    number_of_stops
        Identifies the number of stops for each within the segment.
    seamless
        Identifies that this segment was sold via a direct access channel to
        the marketing carrier.
    change_of_plane
        Indicates the traveler must change planes between flights.
    guaranteed_payment_carrier
        Identifies that this segment has Guaranteed Payment Carrier.
    host_token_ref
        Identifies that this segment has Guaranteed Payment Carrier.
    provider_reservation_info_ref
        Provider reservation reference key.
    passive_provider_reservation_info_ref
        Provider reservation reference key.
    optional_services_indicator
        Indicates true if flight provides optional services.
    availability_source
        Indicates Availability source of AirSegment.
    apisrequirements_ref
        Reference to the APIS Requirements for this AirSegment.
    black_listed
        Indicates blacklisted carriers which are banned from servicing
        points to, from and within the European Community.
    operational_status
        Refers to the flight operational status for the segment. This
        attribute will only be returned in the AvailabilitySearchRsp and not
        used/returned in any other request/responses. If this attribute is
        not returned back in the response, it means the flight is
        operational and not past scheduled departure.
    number_in_party
        Number of person traveling in this air segment excluding the number
        of infants on lap.
    rail_coach_number
        Coach number for which rail seatmap/coachmap is returned.
    booking_date
        Used for rapid reprice. The date the booking was made. Providers:
        1G/1V/1P/1S/1A
    flown_segment
        Used for rapid reprice. Tells whether or not the air segment has
        been flown. Providers: 1G/1V/1P/1S/1A
    schedule_change
        Used for rapid reprice. Tells whether or not the air segment had a
        schedule change by the carrier. This tells rapid reprice that the
        change in the air segment was involuntary and because of a schedule
        change, not because the user is changing the segment. Providers:
        1G/1V/1P/1S/1A
    brand_indicator
        Value “B” specifies that the carrier supports Rich Content and
        Branding.  The Brand Indicator is only returned in the availability
        search response.  Provider: 1G, 1V, 1P, ACH
    """
    class Meta:
        name = "typeBaseAirSegment"

    sponsored_flt_info: None | SponsoredFltInfo = field(
        default=None,
        metadata={
            "name": "SponsoredFltInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    codeshare_info: None | CodeshareInfo = field(
        default=None,
        metadata={
            "name": "CodeshareInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    air_avail_info: list[AirAvailInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirAvailInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    flight_details: list[FlightDetails] = field(
        default_factory=list,
        metadata={
            "name": "FlightDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    flight_details_ref: list[FlightDetailsRef] = field(
        default_factory=list,
        metadata={
            "name": "FlightDetailsRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    alternate_location_distance_ref: list[AlternateLocationDistanceRef] = field(
        default_factory=list,
        metadata={
            "name": "AlternateLocationDistanceRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    connection: None | Connection = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        }
    )
    sell_message: list[str] = field(
        default_factory=list,
        metadata={
            "name": "SellMessage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    rail_coach_details: list[RailCoachDetails] = field(
        default_factory=list,
        metadata={
            "name": "RailCoachDetails",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        }
    )
    open_segment: None | bool = field(
        default=None,
        metadata={
            "name": "OpenSegment",
            "type": "Attribute",
        }
    )
    group: None | int = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Attribute",
            "required": True,
        }
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    cabin_class: None | str = field(
        default=None,
        metadata={
            "name": "CabinClass",
            "type": "Attribute",
        }
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    departure_time: None | str = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Attribute",
        }
    )
    arrival_time: None | str = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Attribute",
        }
    )
    flight_time: None | int = field(
        default=None,
        metadata={
            "name": "FlightTime",
            "type": "Attribute",
        }
    )
    travel_time: None | int = field(
        default=None,
        metadata={
            "name": "TravelTime",
            "type": "Attribute",
        }
    )
    distance: None | int = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Attribute",
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        }
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        }
    )
    participant_level: None | str = field(
        default=None,
        metadata={
            "name": "ParticipantLevel",
            "type": "Attribute",
        }
    )
    link_availability: None | bool = field(
        default=None,
        metadata={
            "name": "LinkAvailability",
            "type": "Attribute",
        }
    )
    polled_availability_option: None | str = field(
        default=None,
        metadata={
            "name": "PolledAvailabilityOption",
            "type": "Attribute",
        }
    )
    availability_display_type: None | str = field(
        default=None,
        metadata={
            "name": "AvailabilityDisplayType",
            "type": "Attribute",
        }
    )
    class_of_service: None | str = field(
        default=None,
        metadata={
            "name": "ClassOfService",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 2,
        }
    )
    eticketability: None | TypeEticketability = field(
        default=None,
        metadata={
            "name": "ETicketability",
            "type": "Attribute",
        }
    )
    equipment: None | str = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Attribute",
            "length": 3,
        }
    )
    marriage_group: None | int = field(
        default=None,
        metadata={
            "name": "MarriageGroup",
            "type": "Attribute",
        }
    )
    number_of_stops: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfStops",
            "type": "Attribute",
        }
    )
    seamless: None | bool = field(
        default=None,
        metadata={
            "name": "Seamless",
            "type": "Attribute",
        }
    )
    change_of_plane: bool = field(
        default=False,
        metadata={
            "name": "ChangeOfPlane",
            "type": "Attribute",
        }
    )
    guaranteed_payment_carrier: None | str = field(
        default=None,
        metadata={
            "name": "GuaranteedPaymentCarrier",
            "type": "Attribute",
        }
    )
    host_token_ref: None | str = field(
        default=None,
        metadata={
            "name": "HostTokenRef",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    passive_provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    optional_services_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "OptionalServicesIndicator",
            "type": "Attribute",
        }
    )
    availability_source: None | str = field(
        default=None,
        metadata={
            "name": "AvailabilitySource",
            "type": "Attribute",
            "max_length": 1,
        }
    )
    apisrequirements_ref: None | str = field(
        default=None,
        metadata={
            "name": "APISRequirementsRef",
            "type": "Attribute",
        }
    )
    black_listed: None | bool = field(
        default=None,
        metadata={
            "name": "BlackListed",
            "type": "Attribute",
        }
    )
    operational_status: None | str = field(
        default=None,
        metadata={
            "name": "OperationalStatus",
            "type": "Attribute",
        }
    )
    number_in_party: None | int = field(
        default=None,
        metadata={
            "name": "NumberInParty",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    rail_coach_number: None | str = field(
        default=None,
        metadata={
            "name": "RailCoachNumber",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    booking_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "BookingDate",
            "type": "Attribute",
        }
    )
    flown_segment: bool = field(
        default=False,
        metadata={
            "name": "FlownSegment",
            "type": "Attribute",
        }
    )
    schedule_change: bool = field(
        default=False,
        metadata={
            "name": "ScheduleChange",
            "type": "Attribute",
        }
    )
    brand_indicator: None | str = field(
        default=None,
        metadata={
            "name": "BrandIndicator",
            "type": "Attribute",
        }
    )
