from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypeFareGuarantee(Enum):
    """
    The status of a fare.

    Properties
    ----------
    AUTO
        Automatically generated
    MANUAL
        Agent has overridden default(s)
    MANUAL_FARE
        Fare has been constructed by agent
    GUARANTEED
        Fare is guaranteed
    INVALID
        Invalid fare, e.g. due to name or itinerary change
    RESTORED
        Ticketed stored fare has been restored
    TICKETED
    UNTICKETABLE
        Unable to ticket
    REPRICE
        Need requote to ticket
    EXPIRED
        Expired fare due to older fare guarantee date typically older than 7
        days
    AUTO_USING_PRIVATE_FARE
        Agency private fares that are not guaranteed
    GUARANTEED_USING_AIRLINE_PRIVATE_FARE
        Guaranteed fare using Airline private fare that was filed with a
        fare distributor.
    AIRLINE
        Fare guaranteed by Airline.
    GUARANTEE_EXPIRED
        Guaranteed fare recently got expired as ticketing hadn't been done
        within a time frame typically midnight local time of POS .
    AGENCY_PRIVATE_FARE_NO_OVERRIDE
        Agency Private Fare with no rules override
    UNKNOWN
        To handle new enumerations added by provider but currently not
        recognized by API
    """
    AUTO = "Auto"
    MANUAL = "Manual"
    MANUAL_FARE = "ManualFare"
    GUARANTEED = "Guaranteed"
    INVALID = "Invalid"
    RESTORED = "Restored"
    TICKETED = "Ticketed"
    UNTICKETABLE = "Unticketable"
    REPRICE = "Reprice"
    EXPIRED = "Expired"
    AUTO_USING_PRIVATE_FARE = "AutoUsingPrivateFare"
    GUARANTEED_USING_AIRLINE_PRIVATE_FARE = "GuaranteedUsingAirlinePrivateFare"
    AIRLINE = "Airline"
    GUARANTEE_EXPIRED = "GuaranteeExpired"
    AGENCY_PRIVATE_FARE_NO_OVERRIDE = "AgencyPrivateFareNoOverride"
    UNKNOWN = "Unknown"
