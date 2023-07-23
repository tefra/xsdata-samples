from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.air_itinerary_solution_ref import AirItinerarySolutionRef
from travelport.models.air_pricing_info import AirPricingInfo
from travelport.models.air_pricing_solution_itinerary import AirPricingSolutionItinerary
from travelport.models.air_segment import AirSegment
from travelport.models.air_segment_ref import AirSegmentRef
from travelport.models.available_ssr import AvailableSsr
from travelport.models.connection import Connection
from travelport.models.fare_note import FareNote
from travelport.models.fare_note_ref import FareNoteRef
from travelport.models.fee_info import FeeInfo
from travelport.models.host_token_1 import HostToken1
from travelport.models.journey import Journey
from travelport.models.leg_ref import LegRef
from travelport.models.meta_data_1 import MetaData1
from travelport.models.optional_services import OptionalServices
from travelport.models.pricing_details import PricingDetails
from travelport.models.tax_info import TaxInfo
from travelport.models.type_result_message_1 import TypeResultMessage1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirPricingSolution:
    """
    The pricing container for an air travel itinerary.

    Parameters
    ----------
    air_segment
    air_segment_ref
    journey
    leg_ref
    air_pricing_info
    fare_note
    fare_note_ref
    connection
    meta_data
    air_pricing_result_message
    fee_info
    tax_info
        Itinerary level taxes
    air_itinerary_solution_ref
    host_token
    optional_services
    available_ssr
    pricing_details
    key
    complete_itinerary
        This attribute is used to return whether complete Itinerary is
        present in the AirPricingSolution structure or not. If set to true
        means AirPricingSolution contains the result for full requested
        itinerary.
    quote_date
        This date will be equal to the date of the transaction unless the
        request included a modified ticket date.
    total_price
        The total price for this entity including base price and all taxes.
    base_price
        Represents the base price for this entity. This does not include any
        taxes or surcharges.
    approximate_total_price
        The Converted total price in Default Currency for this entity
        including base price and all taxes.
    approximate_base_price
        The Converted base price in Default Currency for this entity. This
        does not include any taxes or surcharges.
    equivalent_base_price
        Represents the base price in the related currency for this entity.
        This does not include any taxes or surcharges.
    taxes
        The aggregated amount of all the taxes that are associated with this
        entity. See the associated TaxInfo array for a breakdown of the
        individual taxes.
    fees
        The aggregated amount of all the fees that are associated with this
        entity. See the associated FeeInfo array for a breakdown of the
        individual fees.
    services
        The total cost for all optional services.
    approximate_taxes
        The Converted tax amount in Default Currency.
    approximate_fees
        The Converted fee amount in Default Currency.
    itinerary
        For an exchange request this tells if the itinerary is the original
        one or new one. A value of Original will only apply to
        1G/1V/1P/1S/1A. A value of New will apply to 1G/1V/1P/1S/1A/ACH.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_segment_ref: list[AirSegmentRef] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    journey: list[Journey] = field(
        default_factory=list,
        metadata={
            "name": "Journey",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    leg_ref: list[LegRef] = field(
        default_factory=list,
        metadata={
            "name": "LegRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_pricing_info: list[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_note: list[FareNote] = field(
        default_factory=list,
        metadata={
            "name": "FareNote",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fare_note_ref: list[FareNoteRef] = field(
        default_factory=list,
        metadata={
            "name": "FareNoteRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    connection: list[Connection] = field(
        default_factory=list,
        metadata={
            "name": "Connection",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    meta_data: list[MetaData1] = field(
        default_factory=list,
        metadata={
            "name": "MetaData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    air_pricing_result_message: list[TypeResultMessage1] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingResultMessage",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    fee_info: list[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    tax_info: list[TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    air_itinerary_solution_ref: list[AirItinerarySolutionRef] = field(
        default_factory=list,
        metadata={
            "name": "AirItinerarySolutionRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    host_token: list[HostToken1] = field(
        default_factory=list,
        metadata={
            "name": "HostToken",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        }
    )
    optional_services: None | OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    available_ssr: None | AvailableSsr = field(
        default=None,
        metadata={
            "name": "AvailableSSR",
            "type": "Element",
        }
    )
    pricing_details: None | PricingDetails = field(
        default=None,
        metadata={
            "name": "PricingDetails",
            "type": "Element",
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
    complete_itinerary: bool = field(
        default=True,
        metadata={
            "name": "CompleteItinerary",
            "type": "Attribute",
        }
    )
    quote_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "QuoteDate",
            "type": "Attribute",
        }
    )
    total_price: None | str = field(
        default=None,
        metadata={
            "name": "TotalPrice",
            "type": "Attribute",
        }
    )
    base_price: None | str = field(
        default=None,
        metadata={
            "name": "BasePrice",
            "type": "Attribute",
        }
    )
    approximate_total_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotalPrice",
            "type": "Attribute",
        }
    )
    approximate_base_price: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateBasePrice",
            "type": "Attribute",
        }
    )
    equivalent_base_price: None | str = field(
        default=None,
        metadata={
            "name": "EquivalentBasePrice",
            "type": "Attribute",
        }
    )
    taxes: None | str = field(
        default=None,
        metadata={
            "name": "Taxes",
            "type": "Attribute",
        }
    )
    fees: None | str = field(
        default=None,
        metadata={
            "name": "Fees",
            "type": "Attribute",
        }
    )
    services: None | str = field(
        default=None,
        metadata={
            "name": "Services",
            "type": "Attribute",
        }
    )
    approximate_taxes: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTaxes",
            "type": "Attribute",
        }
    )
    approximate_fees: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateFees",
            "type": "Attribute",
        }
    )
    itinerary: None | AirPricingSolutionItinerary = field(
        default=None,
        metadata={
            "name": "Itinerary",
            "type": "Attribute",
        }
    )
