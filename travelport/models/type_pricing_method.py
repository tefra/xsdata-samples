from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


class TypePricingMethod(Enum):
    """
    The method at which the pricing data was acquired.

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
        Expired fare, older than 7 days
    AUTO_USING_PRIVATE_FARE
        Agency private fares that are not guaranteed
    GUARANTEED_USING_AIRLINE_PRIVATE_FARE
        Guaranteed fare using Airline private fare that was filed with a
        fare distributor.
    AIRLINE
        Fare created as a result of Claim PNR which transfers data to GDS
        for ticketing purposes.
    AGENT_ASSISTED
        Fare is created using Agent Asisted Pricing. Worldspan TKG FAX Line
        Documentation - AGENT ASSISTEDPRICED
    VERIFY_PRICE
        Verify existing saved price on PNR . Worldspan TKG FAX Line
        Documentation -  AWAITING PRICE VERIFICATION
    ALT_SEGMENT_REMOVED_REPRICE
        ALT Segment removed, Reprice pricing. Worldspan TKG FAX Line
        Documentation - AWAITING REPRICING ALT SEGS RMVD
    AUXILIARY_SEGMENT_REMOVED_REPRICE
        AUX Segment removed, Reprice pricing. Worldspan TKG FAX Line
        Documentation -  AWAITING REPRICING AUX SEGS REMOVED
    DUPLICATE_SEGMENT_REMOVED_REPRICE
        Duplicate Segment removed, Reprice pricing. Worldspan TKG FAX Line
        Documentation - AWAITING REPRICING DUPE SEGS REMOVED
    UNKNOWN
        Any other kind of Pricing Method which is not supported by API.
    GUARANTEED_USING_AGENCY_PRIVATE_FARE
        Guaranteed fare using Agency private fare that was filed with a fare
        distributor.
    AUTO_RAPID_REPRICE
        Auto priced by rapid reprice. Provider 1P FCI code 4 .
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
    AGENT_ASSISTED = "AgentAssisted"
    VERIFY_PRICE = "VerifyPrice"
    ALT_SEGMENT_REMOVED_REPRICE = "AltSegmentRemovedReprice"
    AUXILIARY_SEGMENT_REMOVED_REPRICE = "AuxiliarySegmentRemovedReprice"
    DUPLICATE_SEGMENT_REMOVED_REPRICE = "DuplicateSegmentRemovedReprice"
    UNKNOWN = "Unknown"
    GUARANTEED_USING_AGENCY_PRIVATE_FARE = "GuaranteedUsingAgencyPrivateFare"
    AUTO_RAPID_REPRICE = "AutoRapidReprice"
