from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.air_segment_pricing_modifiers import (
    AirSegmentPricingModifiers,
)
from travelport.models.fare_ticket_designator import FareTicketDesignator
from travelport.models.fare_type import FareType
from travelport.models.repricing_modifiers_flight_type import (
    RepricingModifiersFlightType,
)
from travelport.models.type_price_class_of_service import (
    TypePriceClassOfService,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class RepricingModifiers:
    """Used for rapid reprice to provide additional options for the reprice.

    Providers: 1G/1V/1P/1S/1A

    Parameters
    ----------
    private_fare_options
        Public and/or Private Fares requested for pricing.
        Currently supported: AccountCodeOnly, PrivateFaresOnly,
        PublicPrivateFaresOnly.
    fare_type
    fare_ticket_designator
    override_currency
    air_segment_pricing_modifiers
    withhold_tax_code
        Used to request tax withholding for the tax code specified.
        Providers supported 1G/1P
    price_class_of_service
        Values allowed are ClassBooked or LowestClass. This tells how to
        price the new itinerary.
    create_date
        This is either today’s date or the date the repriced itinerary was
        created
    reissue_loc_city_code
        This is the city code of the reissue location
    reissue_loc_country_code
        This is the country code of the reissue location
    bulk_ticket
        Set to true and the itinerary is/will be a bulk ticket. Set to false
        and the itinerary being repriced will not be a bulk ticket.
    account_code
        May be used in conjunction with PrivateFareOptions
    penalty_as_tax_code
        Used to request that the penalty be applied as a tax, to the tax
        code specified. Providers supported 1G/1P
    air_pricing_solution_ref
        A reference to a AirPricingSolution. Providers: 1G, 1V, 1P.
    penalty_to_fare
        Will add the change fee/penalty amount to the total fare amount.
        Supported Providers: 1P
    price_ptconly
        A value of true forces the price for the PTC even if that fare is
        not the lowest fare for the passenger.
    brand_details
        Set to true full brand details will be returned.
    brand_modifier
        A value of MaintainBrand will maintain the brand from the original
        ticket if applicable.
    jet_service_only
        Request flights that are jet service only. Available in
        AirExchangeMultiQuoteReq only.
    time_window
        A value of Time Window is optional. Available in
        AirExchangeMultiQuoteReq only.
    flight_type
        Type of flights to be returned. Values are 'NonStop', 'Direct',
        'SingleConnection' and 'NoRestrictions'. Available in
        AirExchangeMultiQuoteReq only.
    multi_airport_search
        A value of Multi Airport Search Indicator is optional. Available in
        AirExchangeMultiQuoteReq only.
    connection_point
        A value of Connection City Code is optional. Available in
        AirExchangeMultiQuoteReq only.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    private_fare_options: None | str = field(
        default=None,
        metadata={
            "name": "PrivateFareOptions",
            "type": "Element",
            "max_length": 50,
        },
    )
    fare_type: list[FareType] = field(
        default_factory=list,
        metadata={
            "name": "FareType",
            "type": "Element",
            "max_occurs": 100,
        },
    )
    fare_ticket_designator: None | FareTicketDesignator = field(
        default=None,
        metadata={
            "name": "FareTicketDesignator",
            "type": "Element",
        },
    )
    override_currency: None | RepricingModifiers.OverrideCurrency = field(
        default=None,
        metadata={
            "name": "OverrideCurrency",
            "type": "Element",
        },
    )
    air_segment_pricing_modifiers: list[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "AirSegmentPricingModifiers",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    withhold_tax_code: list[str] = field(
        default_factory=list,
        metadata={
            "name": "WithholdTaxCode",
            "type": "Element",
            "max_occurs": 4,
            "length": 2,
        },
    )
    price_class_of_service: None | TypePriceClassOfService = field(
        default=None,
        metadata={
            "name": "PriceClassOfService",
            "type": "Attribute",
        },
    )
    create_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
        },
    )
    reissue_loc_city_code: None | str = field(
        default=None,
        metadata={
            "name": "ReissueLocCityCode",
            "type": "Attribute",
            "length": 3,
        },
    )
    reissue_loc_country_code: None | str = field(
        default=None,
        metadata={
            "name": "ReissueLocCountryCode",
            "type": "Attribute",
            "length": 2,
        },
    )
    bulk_ticket: bool = field(
        default=False,
        metadata={
            "name": "BulkTicket",
            "type": "Attribute",
        },
    )
    account_code: None | str = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Attribute",
        },
    )
    penalty_as_tax_code: None | str = field(
        default=None,
        metadata={
            "name": "PenaltyAsTaxCode",
            "type": "Attribute",
            "length": 2,
        },
    )
    air_pricing_solution_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirPricingSolutionRef",
            "type": "Attribute",
        },
    )
    penalty_to_fare: None | bool = field(
        default=None,
        metadata={
            "name": "PenaltyToFare",
            "type": "Attribute",
        },
    )
    price_ptconly: bool = field(
        default=False,
        metadata={
            "name": "PricePTCOnly",
            "type": "Attribute",
        },
    )
    brand_details: bool = field(
        default=False,
        metadata={
            "name": "BrandDetails",
            "type": "Attribute",
        },
    )
    brand_modifier: None | str = field(
        default=None,
        metadata={
            "name": "BrandModifier",
            "type": "Attribute",
        },
    )
    jet_service_only: bool = field(
        default=False,
        metadata={
            "name": "JetServiceOnly",
            "type": "Attribute",
        },
    )
    time_window: None | int = field(
        default=None,
        metadata={
            "name": "TimeWindow",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 12,
        },
    )
    flight_type: RepricingModifiersFlightType = field(
        default=RepricingModifiersFlightType.DIRECT,
        metadata={
            "name": "FlightType",
            "type": "Attribute",
        },
    )
    multi_airport_search: bool = field(
        default=True,
        metadata={
            "name": "MultiAirportSearch",
            "type": "Attribute",
        },
    )
    connection_point: None | str = field(
        default=None,
        metadata={
            "name": "ConnectionPoint",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )

    @dataclass
    class OverrideCurrency:
        currency_code: None | str = field(
            default=None,
            metadata={
                "name": "CurrencyCode",
                "type": "Attribute",
                "length": 3,
            },
        )
        country_code: None | str = field(
            default=None,
            metadata={
                "name": "CountryCode",
                "type": "Attribute",
                "length": 2,
            },
        )
