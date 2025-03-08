from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from sabre.models.adv_res_ticketing_type import AdvResTicketingType
from sabre.models.air_trip_type import AirTripType
from sabre.models.alliance_type import AllianceType
from sabre.models.alt_cities_combinations_type import AltCitiesCombinationsType
from sabre.models.cabin_pref_type import CabinPrefType
from sabre.models.company_name_pref_type import CompanyNamePrefType
from sabre.models.content_type_type import ContentTypeType
from sabre.models.equipment_type_pref import EquipmentTypePref
from sabre.models.fare_restrict_pref_type import FareRestrictPrefType
from sabre.models.flexible_fares_type import FlexibleFaresType
from sabre.models.flight_stops_as_connections_type import (
    FlightStopsAsConnectionsType,
)
from sabre.models.flight_type_pref_type import FlightTypePrefType
from sabre.models.governing_carrier_override_type import (
    GoverningCarrierOverrideType,
)
from sabre.models.interline_brands_type import InterlineBrandsType
from sabre.models.jump_cabin_logic_type import JumpCabinLogicType
from sabre.models.keep_same_cabin_type import KeepSameCabinType
from sabre.models.num_trips_type import NumTripsType
from sabre.models.options_per_date_pair_type import OptionsPerDatePairType
from sabre.models.retailer_rules_type import RetailerRulesType
from sabre.models.spanish_family_discount_level import (
    SpanishFamilyDiscountLevel,
)
from sabre.models.stay_restrictions_type import StayRestrictionsType
from sabre.models.tax_code_amount_type import TaxCodeAmountType
from sabre.models.tax_code_type import TaxCodeType
from sabre.models.ticket_distrib_pref_type import TicketDistribPrefType
from sabre.models.validating_carrier_type import ValidatingCarrierType
from sabre.models.voluntary_changes_type import VoluntaryChangesType
from sabre.models.xofares_type import XofaresType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class AirSearchPrefsType:
    """
    Defines user preferences to be used in conducting a search.

    Attributes:
        vendor_pref: Specify vendors to include and exclude from the
            response.
        flight_type_pref: Defines preferred flight characteristics to be
            used in a search.
        fare_restrict_pref: Constrains a fare search to those with
            restrictions that satisfy user-imposed limitations.
        equip_pref: Defines preferred equipment profile(s) to be used in
            a search.
        cabin_pref: Defines preferred cabin(s) to be used in a search.
            The Cabin type specified in a
            OriginDestinationInformation/TPA_Extensions overrides this
            Cabin type for that specific segment/leg. If a Cabin type is
            not specified in a
            OriginDestinationInformation/TPA_Extensions the cabin type
            in this element will be used as default cabin type for that
            segment/leg.
        ticket_distrib_pref: Defines Distribution prefernces.
        tpa_extensions: Additional elements and attributes to be
            included if required, per Trading Partner Agreement (TPA).
        ancillary_fees:
        frequent_flyer: Frequent Flyer Status Information
        spanish_family_discount:
        interline_brands:
        smoking_allowed:
        on_time_rate: Request for flights in response that meet the
            given Department of Transport on-time rate. This is a number
            between 0 and 100.
        eticket_desired: Request flights that are e-ticketable in the
            response.
        valid_interline_ticket: Request options that are validated on
            base of interline ticketing aggrement.
        max_stops_quantity: Request flights that have no more than the
            requested number of stops.
        use_all_flights: Each flight should appear at least once.
        all_flights_data: Return flights not combinable into roundtrips
            as one ways is a separate section.
        hybrid: If false no solutions priced outside of ATSE systems
            will be returned in response for carriers operating in
            hybrid content distribution model.
    """

    vendor_pref: list[CompanyNamePrefType] = field(
        default_factory=list,
        metadata={
            "name": "VendorPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    flight_type_pref: None | FlightTypePrefType = field(
        default=None,
        metadata={
            "name": "FlightTypePref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    fare_restrict_pref: list[AirSearchPrefsType.FareRestrictPref] = field(
        default_factory=list,
        metadata={
            "name": "FareRestrictPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 4,
        },
    )
    equip_pref: list[EquipmentTypePref] = field(
        default_factory=list,
        metadata={
            "name": "EquipPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 9,
        },
    )
    cabin_pref: list[CabinPrefType] = field(
        default_factory=list,
        metadata={
            "name": "CabinPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
        },
    )
    ticket_distrib_pref: list[TicketDistribPrefType] = field(
        default_factory=list,
        metadata={
            "name": "TicketDistribPref",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "max_occurs": 3,
        },
    )
    tpa_extensions: None | AirSearchPrefsType.TpaExtensions = field(
        default=None,
        metadata={
            "name": "TPA_Extensions",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    ancillary_fees: None | AirSearchPrefsType.AncillaryFees = field(
        default=None,
        metadata={
            "name": "AncillaryFees",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    frequent_flyer: list[AirSearchPrefsType.FrequentFlyer] = field(
        default_factory=list,
        metadata={
            "name": "FrequentFlyer",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    spanish_family_discount: (
        None | AirSearchPrefsType.SpanishFamilyDiscount
    ) = field(
        default=None,
        metadata={
            "name": "SpanishFamilyDiscount",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    interline_brands: None | InterlineBrandsType = field(
        default=None,
        metadata={
            "name": "InterlineBrands",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
        },
    )
    smoking_allowed: bool = field(
        default=False,
        metadata={
            "name": "SmokingAllowed",
            "type": "Attribute",
        },
    )
    on_time_rate: None | Decimal = field(
        default=None,
        metadata={
            "name": "OnTimeRate",
            "type": "Attribute",
            "min_inclusive": Decimal("0.01"),
            "max_inclusive": Decimal("100.00"),
        },
    )
    eticket_desired: bool = field(
        default=False,
        metadata={
            "name": "ETicketDesired",
            "type": "Attribute",
        },
    )
    valid_interline_ticket: bool = field(
        default=False,
        metadata={
            "name": "ValidInterlineTicket",
            "type": "Attribute",
        },
    )
    max_stops_quantity: None | int = field(
        default=None,
        metadata={
            "name": "MaxStopsQuantity",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        },
    )
    use_all_flights: bool = field(
        default=False,
        metadata={
            "name": "UseAllFlights",
            "type": "Attribute",
        },
    )
    all_flights_data: bool = field(
        default=False,
        metadata={
            "name": "AllFlightsData",
            "type": "Attribute",
        },
    )
    hybrid: bool = field(
        default=True,
        metadata={
            "name": "Hybrid",
            "type": "Attribute",
        },
    )

    @dataclass
    class FareRestrictPref(FareRestrictPrefType):
        """
        Attributes:
            adv_res_ticketing: Identifies whether advance reservation or
                ticketing restrictions are acceptable in the search
                results.
            stay_restrictions: Identifies whether restrictions on
                minimum or maximum stays should be included in the
                search results.
            voluntary_changes: Identifies whether penalties associated
                with voluntary changes should be included in the search
                results.
        """

        adv_res_ticketing: None | AdvResTicketingType = field(
            default=None,
            metadata={
                "name": "AdvResTicketing",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        stay_restrictions: None | StayRestrictionsType = field(
            default=None,
            metadata={
                "name": "StayRestrictions",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        voluntary_changes: None | VoluntaryChangesType = field(
            default=None,
            metadata={
                "name": "VoluntaryChanges",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

    @dataclass
    class TpaExtensions:
        """
        Attributes:
            departure_window: This should be of the form HHMMHHMM.
            arrival_window: This should be of the form HHMMHHMM.
            exclude_vendor_pref: This element allows a user to exclude
                certain carriers from the search.
            include_alliance_pref: Consider only these alliances.
            exclude_alliance_pref: Do not consider these alliances.
            num_trips:
            alt_cities_combinations:
            num_trips_with_routing: This element allows a user to
                specify the number of itineraries with special routing
                returned.
            online_indicator:
            interline_indicator:
            trip_type: Specify air trip type.
            max_price: Maximum price returned from LFE service.
            content_type: Restrict content type returned by LFE service.
            domestic_layover_time: Domestic maximum connecting hours.
            long_connect_time: Change minimum and maximum connect time
                per connection in long connection schedules if Long
                Connect Time logic is enabled. Specified values should
                be less than 1440 minutes (24 hours).
            long_connect_points: Minimum and maximum number of
                connection points (not necessarily long) for Long
                Connections.
            air_service_only: Return air service only.
            jet_service_only: Return jet service only.
            same_connection_airport_only: Same airport at connection
                point restriction
            same_origin_airport_only: Same airport at origin point
                restriction
            same_turnaround_airport_only: Same airport at turnaround
                point restriction
            aircraft_type_penalty: Aircraft type penalty (in dollars).
                Used to penalize propeller aircraft type in the
                response.
            alternate_airport_penalty: Alternate airport penalty (in
                dollars). Used to penalize options with alternate
                airports.
            fare_amount_threshold: % ESV value above the lowest
                itinerary
            num_of_low_fare_sol: Number of low fare solutions for ESV2
            num_of_must_price_onl_sol: Number of must price online
                solutions for ESV2
            num_of_must_price_inrl_sol: Number of must price interline
                solutions for ESV2
            num_of_must_price_nstp_onl_sol: Number of must price non-
                stop online solutions for ESV2
            num_of_must_price_nstp_inrl_sol: Number of must price non-
                stop interline solutions for ESV2
            num_of_must_price_sstop_onl_sol: Number of must price single
                stop online solutions for ESV2
            stp_penalty_in_usd: Stop penalty in dollars for ESV2
            dur_penalty_in_usd: Duration penalty in dollars for ESV2
            dep_penalty_in_usd: Departure penalty in dollars for ESV2
            max_allowed_must_price_overage_per_crr: Max allowed must
                price overage per carrier for ESV2
            flt_opt_must_price_reuse_limit: Flight option reuse limit
                (must price) for ESV2
            upper_bound_must_price_factor_for_not_non_stp: Upper bound
                factor for not non-stops (must price) for ESV2
            upper_bound_lfsfactor: Low fare search upper bound factor
                for ESV2
            num_of_must_price_nstp1_stp_onl_sol: Number of must price
                non-stop/one-stop online solutions for ESV2
            num_of_must_price_nstp1_stp_inrl_sol: Number of must price
                non-stop/one-stop interline solutions for ESV2
            upper_bound_must_price_factor_for_non_stp: Upper bound
                factor for non-stops (must price) for ESV2
            max_allowed_lfsoverage_per_crr_percent: Low fare search max
                allowed overage per carrier % for ESV2
            target_min_num_of_lfsonl_sol_per_crr: Low fare search target
                minimum number of online solutions per carrier for ESV2
            target_min_num_of_lfstot_onl_sol_percent: Low fare search
                target minimum number of total online solutions % for
                ESV2
            flt_opt_lfsreuse_limit_for_non_avs: Low fare search flight
                option reuse limit for non AVS for ESV2
            flt_opt_lfsreuse_limit_for_avs: Low fare search flight
                option reuse limit for AVS for ESV2
            avs_penalty_crrs: AVS penalty carrier list (| delimited) for
                ESV2
            max_num_of_non_stp_onl_sol: Max number of nonstop online
                solutions for ESV2
            max_num_of_non_stp_inrl_sol: Max number of nonstop interline
                solutions for ESV2
            max_num_of_single_stp_onl_sol: Max number of single stop
                online solutions for ESV2
            max_num_of2_plus_stp_sol: Max number of 2+ stops solutions
                for ESV2
            min_allowed_overage_per_crr_percent: Min allowed overage per
                carrier % for ESV2
            min_allowed_overage_per_crr: Min allowed overage per carrier
                for ESV2
            max_rel_fare_lvl_ofx_for_non_stp: Max relative fare level of
                x for nonstops for ESV2
            max_rel_fare_lvl_ofx_for_cnx: Max relative fare level of x
                for carrier for ESV2
            num_of_must_price2_plus_stp_sol: Number of must price 2+
                stops solutions for ESV2
            itinerary_number_threshold: Number of preffered/good itins
                to price
            xofares:
            exempt_all_taxes: Exempt all taxes (/TE)
            exempt_all_taxes_and_fees: Exempt all taxes and fees (/TN)
            taxes: Specify Taxes (/TX)
            exempt_tax: Exempt Tax (/TE)
            flight_stops_as_connections:
            ticketing_sum_of_locals: Settings specific to Ticketing Sum
                of Locals processing
            multi_airport_codes: Settings specific to Multi Airport
                Codes processing
            jump_cabin_logic:
            keep_same_cabin:
            governing_carrier_override:
            exclude_call_direct_carriers:
            validating_carrier:
            validating_carrier_check:
            settlement_method:
            flight_repeat_limit:
            flexible_fares:
            diversity_parameters:
            additional_fare_limit:
            fare_focus_rules:
            selling_levels:
            budget: Budget Shopping settings
            options_per_date_pair_list: List of dates/date pairs with
                different requested number of options
            country_pref: List of countries to be excluded from
                processing
            retailer_rules:
        """

        departure_window: None | str = field(
            default=None,
            metadata={
                "name": "DepartureWindow",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "pattern": r"([0-2][0-9][0-5][0-9]){2}",
            },
        )
        arrival_window: None | str = field(
            default=None,
            metadata={
                "name": "ArrivalWindow",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "pattern": r"([0-2][0-9][0-5][0-9]){2}",
            },
        )
        exclude_vendor_pref: list[
            AirSearchPrefsType.TpaExtensions.ExcludeVendorPref
        ] = field(
            default_factory=list,
            metadata={
                "name": "ExcludeVendorPref",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        include_alliance_pref: list[AllianceType] = field(
            default_factory=list,
            metadata={
                "name": "IncludeAlliancePref",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        exclude_alliance_pref: list[AllianceType] = field(
            default_factory=list,
            metadata={
                "name": "ExcludeAlliancePref",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_trips: None | NumTripsType = field(
            default=None,
            metadata={
                "name": "NumTrips",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        alt_cities_combinations: None | AltCitiesCombinationsType = field(
            default=None,
            metadata={
                "name": "AltCitiesCombinations",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_trips_with_routing: (
            None | AirSearchPrefsType.TpaExtensions.NumTripsWithRouting
        ) = field(
            default=None,
            metadata={
                "name": "NumTripsWithRouting",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        online_indicator: (
            None | AirSearchPrefsType.TpaExtensions.OnlineIndicator
        ) = field(
            default=None,
            metadata={
                "name": "OnlineIndicator",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        interline_indicator: (
            None | AirSearchPrefsType.TpaExtensions.InterlineIndicator
        ) = field(
            default=None,
            metadata={
                "name": "InterlineIndicator",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        trip_type: None | AirSearchPrefsType.TpaExtensions.TripType = field(
            default=None,
            metadata={
                "name": "TripType",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        max_price: None | AirSearchPrefsType.TpaExtensions.MaxPrice = field(
            default=None,
            metadata={
                "name": "MaxPrice",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        content_type: None | AirSearchPrefsType.TpaExtensions.ContentType = (
            field(
                default=None,
                metadata={
                    "name": "ContentType",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        domestic_layover_time: (
            None | AirSearchPrefsType.TpaExtensions.DomesticLayoverTime
        ) = field(
            default=None,
            metadata={
                "name": "DomesticLayoverTime",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        long_connect_time: (
            None | AirSearchPrefsType.TpaExtensions.LongConnectTime
        ) = field(
            default=None,
            metadata={
                "name": "LongConnectTime",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        long_connect_points: (
            None | AirSearchPrefsType.TpaExtensions.LongConnectPoints
        ) = field(
            default=None,
            metadata={
                "name": "LongConnectPoints",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        air_service_only: (
            None | AirSearchPrefsType.TpaExtensions.AirServiceOnly
        ) = field(
            default=None,
            metadata={
                "name": "AirServiceOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        jet_service_only: (
            None | AirSearchPrefsType.TpaExtensions.JetServiceOnly
        ) = field(
            default=None,
            metadata={
                "name": "JetServiceOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        same_connection_airport_only: (
            None | AirSearchPrefsType.TpaExtensions.SameConnectionAirportOnly
        ) = field(
            default=None,
            metadata={
                "name": "SameConnectionAirportOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        same_origin_airport_only: (
            None | AirSearchPrefsType.TpaExtensions.SameOriginAirportOnly
        ) = field(
            default=None,
            metadata={
                "name": "SameOriginAirportOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        same_turnaround_airport_only: (
            None | AirSearchPrefsType.TpaExtensions.SameTurnaroundAirportOnly
        ) = field(
            default=None,
            metadata={
                "name": "SameTurnaroundAirportOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        aircraft_type_penalty: (
            None | AirSearchPrefsType.TpaExtensions.AircraftTypePenalty
        ) = field(
            default=None,
            metadata={
                "name": "AircraftTypePenalty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        alternate_airport_penalty: (
            None | AirSearchPrefsType.TpaExtensions.AlternateAirportPenalty
        ) = field(
            default=None,
            metadata={
                "name": "AlternateAirportPenalty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        fare_amount_threshold: (
            None | AirSearchPrefsType.TpaExtensions.FareAmountThreshold
        ) = field(
            default=None,
            metadata={
                "name": "FareAmountThreshold",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_of_low_fare_sol: (
            None | AirSearchPrefsType.TpaExtensions.NumOfLowFareSol
        ) = field(
            default=None,
            metadata={
                "name": "numOfLowFareSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_of_must_price_onl_sol: (
            None | AirSearchPrefsType.TpaExtensions.NumOfMustPriceOnlSol
        ) = field(
            default=None,
            metadata={
                "name": "numOfMustPriceOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_of_must_price_inrl_sol: (
            None | AirSearchPrefsType.TpaExtensions.NumOfMustPriceInrlSol
        ) = field(
            default=None,
            metadata={
                "name": "numOfMustPriceInrlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_of_must_price_nstp_onl_sol: (
            None | AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstpOnlSol
        ) = field(
            default=None,
            metadata={
                "name": "numOfMustPriceNStpOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_of_must_price_nstp_inrl_sol: (
            None | AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstpInrlSol
        ) = field(
            default=None,
            metadata={
                "name": "numOfMustPriceNStpInrlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_of_must_price_sstop_onl_sol: (
            None | AirSearchPrefsType.TpaExtensions.NumOfMustPriceSstopOnlSol
        ) = field(
            default=None,
            metadata={
                "name": "numOfMustPriceSStopOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        stp_penalty_in_usd: (
            None | AirSearchPrefsType.TpaExtensions.StpPenaltyInUsd
        ) = field(
            default=None,
            metadata={
                "name": "stpPenaltyInUSD",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        dur_penalty_in_usd: (
            None | AirSearchPrefsType.TpaExtensions.DurPenaltyInUsd
        ) = field(
            default=None,
            metadata={
                "name": "durPenaltyInUSD",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        dep_penalty_in_usd: (
            None | AirSearchPrefsType.TpaExtensions.DepPenaltyInUsd
        ) = field(
            default=None,
            metadata={
                "name": "depPenaltyInUSD",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        max_allowed_must_price_overage_per_crr: (
            None
            | AirSearchPrefsType.TpaExtensions.MaxAllowedMustPriceOveragePerCrr
        ) = field(
            default=None,
            metadata={
                "name": "maxAllowedMustPriceOveragePerCrr",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        flt_opt_must_price_reuse_limit: (
            None | AirSearchPrefsType.TpaExtensions.FltOptMustPriceReuseLimit
        ) = field(
            default=None,
            metadata={
                "name": "fltOptMustPriceReuseLimit",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        upper_bound_must_price_factor_for_not_non_stp: (
            None
            | AirSearchPrefsType.TpaExtensions.UpperBoundMustPriceFactorForNotNonStp
        ) = field(
            default=None,
            metadata={
                "name": "upperBoundMustPriceFactorForNotNonStp",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        upper_bound_lfsfactor: (
            None | AirSearchPrefsType.TpaExtensions.UpperBoundLfsfactor
        ) = field(
            default=None,
            metadata={
                "name": "upperBoundLFSFactor",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_of_must_price_nstp1_stp_onl_sol: (
            None
            | AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstp1StpOnlSol
        ) = field(
            default=None,
            metadata={
                "name": "numOfMustPriceNStp1StpOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_of_must_price_nstp1_stp_inrl_sol: (
            None
            | AirSearchPrefsType.TpaExtensions.NumOfMustPriceNstp1StpInrlSol
        ) = field(
            default=None,
            metadata={
                "name": "numOfMustPriceNStp1StpInrlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        upper_bound_must_price_factor_for_non_stp: (
            None
            | AirSearchPrefsType.TpaExtensions.UpperBoundMustPriceFactorForNonStp
        ) = field(
            default=None,
            metadata={
                "name": "upperBoundMustPriceFactorForNonStp",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        max_allowed_lfsoverage_per_crr_percent: (
            None
            | AirSearchPrefsType.TpaExtensions.MaxAllowedLfsoveragePerCrrPercent
        ) = field(
            default=None,
            metadata={
                "name": "maxAllowedLFSOveragePerCrrPercent",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        target_min_num_of_lfsonl_sol_per_crr: (
            None
            | AirSearchPrefsType.TpaExtensions.TargetMinNumOfLfsonlSolPerCrr
        ) = field(
            default=None,
            metadata={
                "name": "targetMinNumOfLFSOnlSolPerCrr",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        target_min_num_of_lfstot_onl_sol_percent: (
            None
            | AirSearchPrefsType.TpaExtensions.TargetMinNumOfLfstotOnlSolPercent
        ) = field(
            default=None,
            metadata={
                "name": "targetMinNumOfLFSTotOnlSolPercent",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        flt_opt_lfsreuse_limit_for_non_avs: (
            None
            | AirSearchPrefsType.TpaExtensions.FltOptLfsreuseLimitForNonAvs
        ) = field(
            default=None,
            metadata={
                "name": "fltOptLFSReuseLimitForNonAVS",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        flt_opt_lfsreuse_limit_for_avs: (
            None | AirSearchPrefsType.TpaExtensions.FltOptLfsreuseLimitForAvs
        ) = field(
            default=None,
            metadata={
                "name": "fltOptLFSReuseLimitForAVS",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        avs_penalty_crrs: (
            None | AirSearchPrefsType.TpaExtensions.AvsPenaltyCrrs
        ) = field(
            default=None,
            metadata={
                "name": "avsPenaltyCrrs",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        max_num_of_non_stp_onl_sol: (
            None | AirSearchPrefsType.TpaExtensions.MaxNumOfNonStpOnlSol
        ) = field(
            default=None,
            metadata={
                "name": "maxNumOfNonStpOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        max_num_of_non_stp_inrl_sol: (
            None | AirSearchPrefsType.TpaExtensions.MaxNumOfNonStpInrlSol
        ) = field(
            default=None,
            metadata={
                "name": "maxNumOfNonStpInrlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        max_num_of_single_stp_onl_sol: (
            None | AirSearchPrefsType.TpaExtensions.MaxNumOfSingleStpOnlSol
        ) = field(
            default=None,
            metadata={
                "name": "maxNumOfSingleStpOnlSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        max_num_of2_plus_stp_sol: (
            None | AirSearchPrefsType.TpaExtensions.MaxNumOf2PlusStpSol
        ) = field(
            default=None,
            metadata={
                "name": "maxNumOf2PlusStpSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        min_allowed_overage_per_crr_percent: (
            None
            | AirSearchPrefsType.TpaExtensions.MinAllowedOveragePerCrrPercent
        ) = field(
            default=None,
            metadata={
                "name": "minAllowedOveragePerCrrPercent",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        min_allowed_overage_per_crr: (
            None | AirSearchPrefsType.TpaExtensions.MinAllowedOveragePerCrr
        ) = field(
            default=None,
            metadata={
                "name": "minAllowedOveragePerCrr",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        max_rel_fare_lvl_ofx_for_non_stp: (
            None | AirSearchPrefsType.TpaExtensions.MaxRelFareLvlOfxForNonStp
        ) = field(
            default=None,
            metadata={
                "name": "maxRelFareLvlOfxForNonStp",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        max_rel_fare_lvl_ofx_for_cnx: (
            None | AirSearchPrefsType.TpaExtensions.MaxRelFareLvlOfxForCnx
        ) = field(
            default=None,
            metadata={
                "name": "maxRelFareLvlOfxForCnx",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        num_of_must_price2_plus_stp_sol: (
            None | AirSearchPrefsType.TpaExtensions.NumOfMustPrice2PlusStpSol
        ) = field(
            default=None,
            metadata={
                "name": "numOfMustPrice2PlusStpSol",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        itinerary_number_threshold: (
            None | AirSearchPrefsType.TpaExtensions.ItineraryNumberThreshold
        ) = field(
            default=None,
            metadata={
                "name": "ItineraryNumberThreshold",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        xofares: None | XofaresType = field(
            default=None,
            metadata={
                "name": "XOFares",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        exempt_all_taxes: (
            None | AirSearchPrefsType.TpaExtensions.ExemptAllTaxes
        ) = field(
            default=None,
            metadata={
                "name": "ExemptAllTaxes",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        exempt_all_taxes_and_fees: (
            None | AirSearchPrefsType.TpaExtensions.ExemptAllTaxesAndFees
        ) = field(
            default=None,
            metadata={
                "name": "ExemptAllTaxesAndFees",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        taxes: None | AirSearchPrefsType.TpaExtensions.Taxes = field(
            default=None,
            metadata={
                "name": "Taxes",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        exempt_tax: list[TaxCodeType] = field(
            default_factory=list,
            metadata={
                "name": "ExemptTax",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        flight_stops_as_connections: None | FlightStopsAsConnectionsType = (
            field(
                default=None,
                metadata={
                    "name": "FlightStopsAsConnections",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        ticketing_sum_of_locals: (
            None | AirSearchPrefsType.TpaExtensions.TicketingSumOfLocals
        ) = field(
            default=None,
            metadata={
                "name": "TicketingSumOfLocals",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        multi_airport_codes: (
            None | AirSearchPrefsType.TpaExtensions.MultiAirportCodes
        ) = field(
            default=None,
            metadata={
                "name": "MultiAirportCodes",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        jump_cabin_logic: None | JumpCabinLogicType = field(
            default=None,
            metadata={
                "name": "JumpCabinLogic",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        keep_same_cabin: None | KeepSameCabinType = field(
            default=None,
            metadata={
                "name": "KeepSameCabin",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        governing_carrier_override: None | GoverningCarrierOverrideType = (
            field(
                default=None,
                metadata={
                    "name": "GoverningCarrierOverride",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        exclude_call_direct_carriers: (
            None | AirSearchPrefsType.TpaExtensions.ExcludeCallDirectCarriers
        ) = field(
            default=None,
            metadata={
                "name": "ExcludeCallDirectCarriers",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        validating_carrier: None | ValidatingCarrierType = field(
            default=None,
            metadata={
                "name": "ValidatingCarrier",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        validating_carrier_check: (
            None | AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck
        ) = field(
            default=None,
            metadata={
                "name": "ValidatingCarrierCheck",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        settlement_method: None | str = field(
            default=None,
            metadata={
                "name": "SettlementMethod",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "pattern": r"[a-zA-Z0-9]{3}",
            },
        )
        flight_repeat_limit: (
            None | AirSearchPrefsType.TpaExtensions.FlightRepeatLimit
        ) = field(
            default=None,
            metadata={
                "name": "FlightRepeatLimit",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        flexible_fares: None | FlexibleFaresType = field(
            default=None,
            metadata={
                "name": "FlexibleFares",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        diversity_parameters: (
            None | AirSearchPrefsType.TpaExtensions.DiversityParameters
        ) = field(
            default=None,
            metadata={
                "name": "DiversityParameters",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        additional_fare_limit: (
            None | AirSearchPrefsType.TpaExtensions.AdditionalFareLimit
        ) = field(
            default=None,
            metadata={
                "name": "AdditionalFareLimit",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        fare_focus_rules: (
            None | AirSearchPrefsType.TpaExtensions.FareFocusRules
        ) = field(
            default=None,
            metadata={
                "name": "FareFocusRules",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        selling_levels: (
            None | AirSearchPrefsType.TpaExtensions.SellingLevels
        ) = field(
            default=None,
            metadata={
                "name": "SellingLevels",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        budget: None | AirSearchPrefsType.TpaExtensions.Budget = field(
            default=None,
            metadata={
                "name": "Budget",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        options_per_date_pair_list: (
            None | AirSearchPrefsType.TpaExtensions.OptionsPerDatePairList
        ) = field(
            default=None,
            metadata={
                "name": "OptionsPerDatePairList",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        country_pref: list[AirSearchPrefsType.TpaExtensions.CountryPref] = (
            field(
                default_factory=list,
                metadata={
                    "name": "CountryPref",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        retailer_rules: None | RetailerRulesType = field(
            default=None,
            metadata={
                "name": "RetailerRules",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )

        @dataclass
        class ExcludeVendorPref:
            """
            Attributes:
                code: Identifies a company by the company code.
            """

            code: None | str = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "min_length": 1,
                    "max_length": 8,
                },
            )

        @dataclass
        class NumTripsWithRouting:
            number: int = field(
                default=5,
                metadata={
                    "name": "Number",
                    "type": "Attribute",
                    "min_inclusive": 1,
                },
            )

        @dataclass
        class TripType:
            value: None | AirTripType = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                },
            )

        @dataclass
        class MaxPrice:
            value: None | Decimal = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "fraction_digits": 3,
                },
            )

        @dataclass
        class ContentType:
            type_value: None | ContentTypeType = field(
                default=None,
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                },
            )

        @dataclass
        class DomesticLayoverTime:
            hours: None | int = field(
                default=None,
                metadata={
                    "name": "Hours",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class LongConnectTime:
            min: None | int = field(
                default=None,
                metadata={
                    "name": "Min",
                    "type": "Attribute",
                },
            )
            max: None | int = field(
                default=None,
                metadata={
                    "name": "Max",
                    "type": "Attribute",
                },
            )
            enable: None | bool = field(
                default=None,
                metadata={
                    "name": "Enable",
                    "type": "Attribute",
                },
            )

        @dataclass
        class LongConnectPoints:
            min: None | int = field(
                default=None,
                metadata={
                    "name": "Min",
                    "type": "Attribute",
                },
            )
            max: None | int = field(
                default=None,
                metadata={
                    "name": "Max",
                    "type": "Attribute",
                },
            )

        @dataclass
        class AirServiceOnly:
            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class JetServiceOnly:
            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class SameConnectionAirportOnly:
            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class SameOriginAirportOnly:
            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class SameTurnaroundAirportOnly:
            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class AircraftTypePenalty:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class AlternateAirportPenalty:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class FareAmountThreshold:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class NumOfLowFareSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class NumOfMustPriceOnlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class NumOfMustPriceInrlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class NumOfMustPriceNstpOnlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class NumOfMustPriceNstpInrlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class NumOfMustPriceSstopOnlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class StpPenaltyInUsd:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class DurPenaltyInUsd:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class DepPenaltyInUsd:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MaxAllowedMustPriceOveragePerCrr:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class FltOptMustPriceReuseLimit:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class UpperBoundMustPriceFactorForNotNonStp:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class UpperBoundLfsfactor:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class NumOfMustPriceNstp1StpOnlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class NumOfMustPriceNstp1StpInrlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class UpperBoundMustPriceFactorForNonStp:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MaxAllowedLfsoveragePerCrrPercent:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class TargetMinNumOfLfsonlSolPerCrr:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class TargetMinNumOfLfstotOnlSolPercent:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class FltOptLfsreuseLimitForNonAvs:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class FltOptLfsreuseLimitForAvs:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class AvsPenaltyCrrs:
            value: None | str = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MaxNumOfNonStpOnlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MaxNumOfNonStpInrlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MaxNumOfSingleStpOnlSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MaxNumOf2PlusStpSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MinAllowedOveragePerCrrPercent:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MinAllowedOveragePerCrr:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MaxRelFareLvlOfxForNonStp:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class MaxRelFareLvlOfxForCnx:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class NumOfMustPrice2PlusStpSol:
            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class ItineraryNumberThreshold:
            value: None | float = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class TicketingSumOfLocals:
            """
            Attributes:
                enable: Enable Ticketing Sum of Locals processing.
            """

            enable: bool = field(
                default=False,
                metadata={
                    "name": "Enable",
                    "type": "Attribute",
                },
            )

        @dataclass
        class MultiAirportCodes:
            """
            Attributes:
                enable_open_jaw: Enable open jaw leg combinations.
            """

            enable_open_jaw: bool = field(
                default=False,
                metadata={
                    "name": "EnableOpenJaw",
                    "type": "Attribute",
                },
            )

        @dataclass
        class ExcludeCallDirectCarriers:
            """
            Attributes:
                enabled: Force DSF to return schedules only for carriers
                    bookable by Sabre.
            """

            enabled: None | bool = field(
                default=None,
                metadata={
                    "name": "Enabled",
                    "type": "Attribute",
                },
            )

        @dataclass
        class ValidatingCarrierCheck:
            settlement_validation: (
                None
                | AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.SettlementValidation
            ) = field(
                default=None,
                metadata={
                    "name": "SettlementValidation",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                },
            )
            ietvalidation: (
                None
                | AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.Ietvalidation
            ) = field(
                default=None,
                metadata={
                    "name": "IETValidation",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "required": True,
                },
            )
            carrier: list[
                AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.Carrier
            ] = field(
                default_factory=list,
                metadata={
                    "name": "Carrier",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            country: list[
                AirSearchPrefsType.TpaExtensions.ValidatingCarrierCheck.Country
            ] = field(
                default_factory=list,
                metadata={
                    "name": "Country",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )

            @dataclass
            class SettlementValidation:
                """
                If set to true validate BSP agreement for given carriers.
                """

                ind: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class Ietvalidation:
                """
                If set to true validate IET agreement for listed countries.
                """

                ind: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Ind",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class Carrier:
                code: None | str = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[0-9A-Z]{2,3}",
                    },
                )

            @dataclass
            class Country:
                code: None | str = field(
                    default=None,
                    metadata={
                        "name": "Code",
                        "type": "Attribute",
                        "required": True,
                        "pattern": r"[a-zA-Z]{2}",
                    },
                )

        @dataclass
        class FlightRepeatLimit:
            """
            Attributes:
                value: Flight Repeat Limit for DSF. Expected value
                    1-100.
            """

            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class DiversityParameters:
            """
            Attributes:
                weightings: Defines how important various parameter
                    options are in the response. Sum of all weightings
                    needs to equal 10.
                time_of_day_distribution: Defines how the options in the
                    response should be distributed between certain
                    departure time of day ranges. All defined
                    TimeOfDayRanges need to cover the whole day and the
                    sum of all Percentages needs to equal 100.
                inbound_outbound_pairing: Defines the requested ratio of
                    inbounds to outbounds in the response.
                additional_non_stops_number: Defines how many additional
                    non-stop options should be added to the response.
                    Overrides @Percentage.
                additional_non_stops_percentage: Defines how many
                    additional non-stop options should be added to the
                    response as a percentage of the requested number of
                    options.
            """

            weightings: (
                None
                | AirSearchPrefsType.TpaExtensions.DiversityParameters.Weightings
            ) = field(
                default=None,
                metadata={
                    "name": "Weightings",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            time_of_day_distribution: (
                None
                | AirSearchPrefsType.TpaExtensions.DiversityParameters.TimeOfDayDistribution
            ) = field(
                default=None,
                metadata={
                    "name": "TimeOfDayDistribution",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            inbound_outbound_pairing: None | int = field(
                default=None,
                metadata={
                    "name": "InboundOutboundPairing",
                    "type": "Attribute",
                    "min_inclusive": 1,
                    "max_inclusive": 1000,
                },
            )
            additional_non_stops_number: None | int = field(
                default=None,
                metadata={
                    "name": "AdditionalNonStopsNumber",
                    "type": "Attribute",
                    "min_inclusive": 1,
                },
            )
            additional_non_stops_percentage: None | int = field(
                default=None,
                metadata={
                    "name": "AdditionalNonStopsPercentage",
                    "type": "Attribute",
                    "min_inclusive": 0,
                    "max_inclusive": 100,
                },
            )

            @dataclass
            class Weightings:
                """
                Attributes:
                    price_weight: Defines how important price options
                        are on a scale from 0 to 10.
                    travel_time_weight: Defines how important travel
                        time options are on a scale from 0 to 10.
                """

                price_weight: None | int = field(
                    default=None,
                    metadata={
                        "name": "PriceWeight",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0,
                        "max_inclusive": 10,
                    },
                )
                travel_time_weight: None | int = field(
                    default=None,
                    metadata={
                        "name": "TravelTimeWeight",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0,
                        "max_inclusive": 10,
                    },
                )

            @dataclass
            class TimeOfDayDistribution:
                time_of_day_range: list[
                    AirSearchPrefsType.TpaExtensions.DiversityParameters.TimeOfDayDistribution.TimeOfDayRange
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "TimeOfDayRange",
                        "type": "Element",
                        "namespace": "http://www.opentravel.org/OTA/2003/05",
                        "min_occurs": 2,
                        "max_occurs": 4,
                    },
                )

                @dataclass
                class TimeOfDayRange:
                    """
                    Attributes:
                        begin: Beginning of the TimeOfDayRange in HHMM
                            format.
                        end: End of the TimeOfDayRange in HHMM format.
                        percentage: Defines how many percent options
                            should be in the TimeOfDayRange.
                    """

                    begin: None | str = field(
                        default=None,
                        metadata={
                            "name": "Begin",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
                        },
                    )
                    end: None | str = field(
                        default=None,
                        metadata={
                            "name": "End",
                            "type": "Attribute",
                            "required": True,
                            "pattern": r"([0-1][0-9]|2[0-3])[0-5][0-9]",
                        },
                    )
                    percentage: None | int = field(
                        default=None,
                        metadata={
                            "name": "Percentage",
                            "type": "Attribute",
                            "required": True,
                            "min_inclusive": 0,
                            "max_inclusive": 100,
                        },
                    )

        @dataclass
        class AdditionalFareLimit:
            """
            Attributes:
                value: Additional fare limit.
            """

            value: None | int = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class FareFocusRules:
            """
            Attributes:
                exclude: Exclude fare focus rules.
            """

            exclude: None | bool = field(
                default=None,
                metadata={
                    "name": "Exclude",
                    "type": "Attribute",
                },
            )

        @dataclass
        class SellingLevels:
            selling_level_rules: (
                None
                | AirSearchPrefsType.TpaExtensions.SellingLevels.SellingLevelRules
            ) = field(
                default=None,
                metadata={
                    "name": "SellingLevelRules",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
            show_fare_amounts: (
                None
                | AirSearchPrefsType.TpaExtensions.SellingLevels.ShowFareAmounts
            ) = field(
                default=None,
                metadata={
                    "name": "ShowFareAmounts",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )

            @dataclass
            class SellingLevelRules:
                """
                Attributes:
                    ignore: Force ignore adjustment selling level rules
                """

                ignore: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Ignore",
                        "type": "Attribute",
                        "required": True,
                    },
                )

            @dataclass
            class ShowFareAmounts:
                """
                Attributes:
                    original: Show original selling fare level amounts
                        and total adjusted amount in Fare Calc line
                    adjusted: Show selling level amounts and total
                        adjusted amount in Fare Calc line
                """

                original: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Original",
                        "type": "Attribute",
                    },
                )
                adjusted: None | bool = field(
                    default=None,
                    metadata={
                        "name": "Adjusted",
                        "type": "Attribute",
                    },
                )

        @dataclass
        class Budget:
            """
            Attributes:
                minimum_price: Minimum price to include in response
                maximum_price: Maximum price to include in response
                relative_price_threshold: Relative price difference
                    threshold to be respected while choosing alternative
                    options
            """

            minimum_price: None | object = field(
                default=None,
                metadata={
                    "name": "MinimumPrice",
                    "type": "Attribute",
                },
            )
            maximum_price: None | object = field(
                default=None,
                metadata={
                    "name": "MaximumPrice",
                    "type": "Attribute",
                },
            )
            relative_price_threshold: None | str = field(
                default=None,
                metadata={
                    "name": "RelativePriceThreshold",
                    "type": "Attribute",
                    "pattern": r"0|-?[1-9][0-9]*%?",
                },
            )

        @dataclass
        class OptionsPerDatePairList:
            options_per_date_pair: list[OptionsPerDatePairType] = field(
                default_factory=list,
                metadata={
                    "name": "OptionsPerDatePair",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                    "min_occurs": 1,
                },
            )

        @dataclass
        class CountryPref:
            code: None | str = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[a-zA-Z]{2}",
                },
            )
            prefer_level: None | str = field(
                default=None,
                metadata={
                    "name": "PreferLevel",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"Unacceptable",
                },
            )

        @dataclass
        class OnlineIndicator:
            """
            Attributes:
                ind: Specifies if the associated data is formatted or
                    not. If true, then it is formatted, if false, then
                    not formatted.
            """

            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                },
            )

        @dataclass
        class InterlineIndicator:
            """
            Attributes:
                ind: Specifies if the associated data is formatted or
                    not. If true, then it is formatted, if false, then
                    not formatted.
            """

            ind: None | bool = field(
                default=None,
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                },
            )

        @dataclass
        class ExemptAllTaxes:
            value: None | bool = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class ExemptAllTaxesAndFees:
            value: None | bool = field(
                default=None,
                metadata={
                    "name": "Value",
                    "type": "Attribute",
                    "required": True,
                },
            )

        @dataclass
        class Taxes:
            """
            Attributes:
                tax: Specify tax amount and code.
            """

            tax: list[TaxCodeAmountType] = field(
                default_factory=list,
                metadata={
                    "name": "Tax",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )

    @dataclass
    class AncillaryFees:
        """
        Attributes:
            ancillary_fee_group: List of requested groups
            enable: Enable Ancillary Fees processing path.
            summary: Flag whether this is a summary request.
        """

        ancillary_fee_group: list[
            AirSearchPrefsType.AncillaryFees.AncillaryFeeGroup
        ] = field(
            default_factory=list,
            metadata={
                "name": "AncillaryFeeGroup",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        enable: None | bool = field(
            default=None,
            metadata={
                "name": "Enable",
                "type": "Attribute",
                "required": True,
            },
        )
        summary: None | bool = field(
            default=None,
            metadata={
                "name": "Summary",
                "type": "Attribute",
            },
        )

        @dataclass
        class AncillaryFeeGroup:
            """
            Attributes:
                code: Group code
                count: Number of items
            """

            code: None | object = field(
                default=None,
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                },
            )
            count: None | object = field(
                default=None,
                metadata={
                    "name": "Count",
                    "type": "Attribute",
                },
            )

    @dataclass
    class FrequentFlyer:
        """
        Attributes:
            status: Frequent Flyer Status
            airline_code: Airline Carrier Code
        """

        status: None | int = field(
            default=None,
            metadata={
                "name": "Status",
                "type": "Attribute",
                "required": True,
            },
        )
        airline_code: None | str = field(
            default=None,
            metadata={
                "name": "AirlineCode",
                "type": "Attribute",
            },
        )

    @dataclass
    class SpanishFamilyDiscount:
        """
        Attributes:
            level: Spanish Large Family Discount Level. Valid values are
                1 or 2.
        """

        level: None | SpanishFamilyDiscountLevel = field(
            default=None,
            metadata={
                "name": "Level",
                "type": "Attribute",
                "required": True,
            },
        )
