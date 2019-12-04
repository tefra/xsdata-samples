from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FareMasterPricerTravelBoardSearch:
    """
    :ivar number_of_unit:
    :ivar global_options:
    :ivar pax_reference:
    :ivar customer_ref:
    :ivar form_of_payment_by_passenger:
    :ivar solution_family:
    :ivar passenger_info_grp:
    :ivar fare_families:
    :ivar fare_options:
    :ivar price_to_beat:
    :ivar tax_info:
    :ivar travel_flight_info:
    :ivar value_search:
    :ivar buckets:
    :ivar itinerary:
    :ivar ticket_change_info:
    :ivar combination_fare_families:
    :ivar fee_option:
    :ivar office_id_details:
    """
    class Meta:
        name = "Fare_MasterPricerTravelBoardSearch"
        namespace = "http://xml.amadeus.com/FMPTBQ_15_3_1A"

    number_of_unit: Optional["FareMasterPricerTravelBoardSearch.NumberOfUnit"] = field(
        default=None,
        metadata=dict(
            name="numberOfUnit",
            type="Element"
        )
    )
    global_options: Optional["FareMasterPricerTravelBoardSearch.GlobalOptions"] = field(
        default=None,
        metadata=dict(
            name="globalOptions",
            type="Element"
        )
    )
    pax_reference: List["FareMasterPricerTravelBoardSearch.PaxReference"] = field(
        default_factory=list,
        metadata=dict(
            name="paxReference",
            type="Element",
            min_occurs=0,
            max_occurs=6
        )
    )
    customer_ref: Optional["FareMasterPricerTravelBoardSearch.CustomerRef"] = field(
        default=None,
        metadata=dict(
            name="customerRef",
            type="Element"
        )
    )
    form_of_payment_by_passenger: List["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger"] = field(
        default_factory=list,
        metadata=dict(
            name="formOfPaymentByPassenger",
            type="Element",
            min_occurs=0,
            max_occurs=60
        )
    )
    solution_family: List["FareMasterPricerTravelBoardSearch.SolutionFamily"] = field(
        default_factory=list,
        metadata=dict(
            name="solutionFamily",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    passenger_info_grp: List["FareMasterPricerTravelBoardSearch.PassengerInfoGrp"] = field(
        default_factory=list,
        metadata=dict(
            name="passengerInfoGrp",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    fare_families: List["FareMasterPricerTravelBoardSearch.FareFamilies"] = field(
        default_factory=list,
        metadata=dict(
            name="fareFamilies",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )
    fare_options: Optional["FareMasterPricerTravelBoardSearch.FareOptions"] = field(
        default=None,
        metadata=dict(
            name="fareOptions",
            type="Element"
        )
    )
    price_to_beat: Optional["FareMasterPricerTravelBoardSearch.PriceToBeat"] = field(
        default=None,
        metadata=dict(
            name="priceToBeat",
            type="Element"
        )
    )
    tax_info: List["FareMasterPricerTravelBoardSearch.TaxInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="taxInfo",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    travel_flight_info: Optional["FareMasterPricerTravelBoardSearch.TravelFlightInfo"] = field(
        default=None,
        metadata=dict(
            name="travelFlightInfo",
            type="Element"
        )
    )
    value_search: List["FareMasterPricerTravelBoardSearch.ValueSearch"] = field(
        default_factory=list,
        metadata=dict(
            name="valueSearch",
            type="Element",
            min_occurs=0,
            max_occurs=99
        )
    )
    buckets: List["FareMasterPricerTravelBoardSearch.Buckets"] = field(
        default_factory=list,
        metadata=dict(
            name="buckets",
            type="Element",
            min_occurs=0,
            max_occurs=10
        )
    )
    itinerary: List["FareMasterPricerTravelBoardSearch.Itinerary"] = field(
        default_factory=list,
        metadata=dict(
            name="itinerary",
            type="Element",
            min_occurs=0,
            max_occurs=18
        )
    )
    ticket_change_info: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo"] = field(
        default=None,
        metadata=dict(
            name="ticketChangeInfo",
            type="Element"
        )
    )
    combination_fare_families: List["FareMasterPricerTravelBoardSearch.CombinationFareFamilies"] = field(
        default_factory=list,
        metadata=dict(
            name="combinationFareFamilies",
            type="Element",
            min_occurs=0,
            max_occurs=2000
        )
    )
    fee_option: List["FareMasterPricerTravelBoardSearch.FeeOption"] = field(
        default_factory=list,
        metadata=dict(
            name="feeOption",
            type="Element",
            min_occurs=0,
            max_occurs=9
        )
    )
    office_id_details: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails"] = field(
        default_factory=list,
        metadata=dict(
            name="officeIdDetails",
            type="Element",
            min_occurs=0,
            max_occurs=20
        )
    )

    @dataclass
    class NumberOfUnit:
        """
        :ivar unit_number_detail:
        """
        unit_number_detail: List["FareMasterPricerTravelBoardSearch.NumberOfUnit.UnitNumberDetail"] = field(
            default_factory=list,
            metadata=dict(
                name="unitNumberDetail",
                type="Element",
                min_occurs=1,
                max_occurs=20
            )
        )

        @dataclass
        class UnitNumberDetail:
            """
            :ivar number_of_units:
            :ivar type_of_unit:
            """
            number_of_units: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="numberOfUnits",
                    type="Element",
                    required=True
                )
            )
            type_of_unit: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="typeOfUnit",
                    type="Element",
                    required=True,
                    min_length=1.0,
                    max_length=3.0
                )
            )

    @dataclass
    class GlobalOptions:
        """
        :ivar selection_details:
        """
        selection_details: List["FareMasterPricerTravelBoardSearch.GlobalOptions.SelectionDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="selectionDetails",
                type="Element",
                min_occurs=1,
                max_occurs=10
            )
        )

        @dataclass
        class SelectionDetails:
            """
            :ivar option:
            :ivar option_information:
            """
            option: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="option",
                    type="Element",
                    required=True,
                    min_length=1.0,
                    max_length=3.0
                )
            )
            option_information: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="optionInformation",
                    type="Element",
                    min_length=1.0,
                    max_length=35.0
                )
            )

    @dataclass
    class PaxReference:
        """
        :ivar ptc:
        :ivar traveller:
        """
        ptc: List[str] = field(
            default_factory=list,
            metadata=dict(
                name="ptc",
                type="Element",
                min_occurs=0,
                max_occurs=3,
                min_length=1.0,
                max_length=6.0
            )
        )
        traveller: List["FareMasterPricerTravelBoardSearch.PaxReference.Traveller"] = field(
            default_factory=list,
            metadata=dict(
                name="traveller",
                type="Element",
                min_occurs=1,
                max_occurs=9
            )
        )

        @dataclass
        class Traveller:
            """
            :ivar ref:
            :ivar infant_indicator:
            """
            ref: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="ref",
                    type="Element",
                    required=True
                )
            )
            infant_indicator: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="infantIndicator",
                    type="Element",
                    min_length=1.0,
                    max_length=1.0
                )
            )

    @dataclass
    class CustomerRef:
        """
        :ivar customer_references:
        """
        customer_references: List["FareMasterPricerTravelBoardSearch.CustomerRef.CustomerReferences"] = field(
            default_factory=list,
            metadata=dict(
                name="customerReferences",
                type="Element",
                min_occurs=1,
                max_occurs=20
            )
        )

        @dataclass
        class CustomerReferences:
            """
            :ivar reference_qualifier:
            :ivar reference_number:
            :ivar reference_party_name:
            :ivar traveller_reference_nbr:
            """
            reference_qualifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="referenceQualifier",
                    type="Element",
                    required=True,
                    min_length=1.0,
                    max_length=3.0
                )
            )
            reference_number: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="referenceNumber",
                    type="Element",
                    min_length=1.0,
                    max_length=35.0
                )
            )
            reference_party_name: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="referencePartyName",
                    type="Element",
                    min_length=1.0,
                    max_length=35.0
                )
            )
            traveller_reference_nbr: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="travellerReferenceNbr",
                    type="Element",
                    min_length=1.0,
                    max_length=10.0
                )
            )

    @dataclass
    class FormOfPaymentByPassenger:
        """
        :ivar form_of_payment_details:
        :ivar passenger_fee_reference:
        """
        form_of_payment_details: Optional["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.FormOfPaymentDetails"] = field(
            default=None,
            metadata=dict(
                name="formOfPaymentDetails",
                type="Element",
                required=True
            )
        )
        passenger_fee_reference: Optional["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.PassengerFeeReference"] = field(
            default=None,
            metadata=dict(
                name="passengerFeeReference",
                type="Element"
            )
        )

        @dataclass
        class FormOfPaymentDetails:
            """
            :ivar form_of_payment_details:
            """
            form_of_payment_details: List["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.FormOfPaymentDetails.FormOfPaymentDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="formOfPaymentDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9
                )
            )

            @dataclass
            class FormOfPaymentDetails:
                """
                :ivar type:
                :ivar charged_amount:
                :ivar credit_card_number:
                """
                type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="type",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                charged_amount: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="chargedAmount",
                        type="Element"
                    )
                )
                credit_card_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="creditCardNumber",
                        type="Element",
                        min_length=1.0,
                        max_length=20.0
                    )
                )

        @dataclass
        class PassengerFeeReference:
            """
            :ivar passenger_fee_ref_type:
            :ivar passenger_fee_ref_number:
            :ivar other_characteristics:
            """
            passenger_fee_ref_type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="passengerFeeRefType",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            passenger_fee_ref_number: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="passengerFeeRefNumber",
                    type="Element"
                )
            )
            other_characteristics: Optional["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.PassengerFeeReference.OtherCharacteristics"] = field(
                default=None,
                metadata=dict(
                    name="otherCharacteristics",
                    type="Element"
                )
            )

            @dataclass
            class OtherCharacteristics:
                """
                :ivar passenger_fee_ref_qualif:
                """
                passenger_fee_ref_qualif: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="passengerFeeRefQualif",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

    @dataclass
    class SolutionFamily:
        """
        :ivar value_qualifier:
        :ivar value:
        :ivar fare_details:
        :ivar identity_number:
        :ivar fare_type_grouping:
        :ivar rate_category:
        """
        value_qualifier: Optional[str] = field(
            default=None,
            metadata=dict(
                name="valueQualifier",
                type="Element",
                min_length=1.0,
                max_length=3.0
            )
        )
        value: Optional[float] = field(
            default=None,
            metadata=dict(
                name="value",
                type="Element"
            )
        )
        fare_details: Optional["FareMasterPricerTravelBoardSearch.SolutionFamily.FareDetails"] = field(
            default=None,
            metadata=dict(
                name="fareDetails",
                type="Element"
            )
        )
        identity_number: Optional[str] = field(
            default=None,
            metadata=dict(
                name="identityNumber",
                type="Element",
                min_length=1.0,
                max_length=35.0
            )
        )
        fare_type_grouping: Optional["FareMasterPricerTravelBoardSearch.SolutionFamily.FareTypeGrouping"] = field(
            default=None,
            metadata=dict(
                name="fareTypeGrouping",
                type="Element"
            )
        )
        rate_category: Optional[str] = field(
            default=None,
            metadata=dict(
                name="rateCategory",
                type="Element",
                min_length=1.0,
                max_length=35.0
            )
        )

        @dataclass
        class FareDetails:
            """
            :ivar qualifier:
            :ivar rate:
            :ivar country:
            :ivar fare_category:
            """
            qualifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="qualifier",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            rate: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="rate",
                    type="Element"
                )
            )
            country: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="country",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            fare_category: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="fareCategory",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )

        @dataclass
        class FareTypeGrouping:
            """
            :ivar pricing_group:
            """
            pricing_group: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="pricingGroup",
                    type="Element",
                    min_length=1.0,
                    max_length=35.0
                )
            )

    @dataclass
    class PassengerInfoGrp:
        """
        :ivar passenger_reference:
        :ivar psg_details_info:
        """
        passenger_reference: Optional["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PassengerReference"] = field(
            default=None,
            metadata=dict(
                name="passengerReference",
                type="Element",
                required=True
            )
        )
        psg_details_info: List["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo"] = field(
            default_factory=list,
            metadata=dict(
                name="psgDetailsInfo",
                type="Element",
                min_occurs=0,
                max_occurs=2
            )
        )

        @dataclass
        class PassengerReference:
            """
            :ivar segment_control_details:
            """
            segment_control_details: List["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PassengerReference.SegmentControlDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="segmentControlDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9
                )
            )

            @dataclass
            class SegmentControlDetails:
                """
                :ivar quantity:
                """
                quantity: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="quantity",
                        type="Element"
                    )
                )

        @dataclass
        class PsgDetailsInfo:
            """
            :ivar discount_ptc:
            :ivar flequent_flyer_details:
            """
            discount_ptc: Optional["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo.DiscountPtc"] = field(
                default=None,
                metadata=dict(
                    name="discountPtc",
                    type="Element",
                    required=True
                )
            )
            flequent_flyer_details: Optional["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo.FlequentFlyerDetails"] = field(
                default=None,
                metadata=dict(
                    name="flequentFlyerDetails",
                    type="Element"
                )
            )

            @dataclass
            class DiscountPtc:
                """
                :ivar value_qualifier:
                :ivar value:
                """
                value_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="valueQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                value: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="value",
                        type="Element"
                    )
                )

            @dataclass
            class FlequentFlyerDetails:
                """
                :ivar frequent_traveller_details:
                """
                frequent_traveller_details: List["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo.FlequentFlyerDetails.FrequentTravellerDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="frequentTravellerDetails",
                        type="Element",
                        min_occurs=1,
                        max_occurs=99
                    )
                )

                @dataclass
                class FrequentTravellerDetails:
                    """
                    :ivar carrier:
                    :ivar number:
                    :ivar customer_reference:
                    :ivar status:
                    :ivar tier_level:
                    :ivar priority_code:
                    :ivar tier_description:
                    :ivar company_code:
                    :ivar customer_value:
                    :ivar type:
                    """
                    carrier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="carrier",
                            type="Element",
                            min_length=1.0,
                            max_length=35.0
                        )
                    )
                    number: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="number",
                            type="Element",
                            min_length=1.0,
                            max_length=28.0
                        )
                    )
                    customer_reference: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="customerReference",
                            type="Element",
                            min_length=1.0,
                            max_length=10.0
                        )
                    )
                    status: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="status",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    tier_level: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="tierLevel",
                            type="Element",
                            min_length=1.0,
                            max_length=35.0
                        )
                    )
                    priority_code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="priorityCode",
                            type="Element",
                            min_length=1.0,
                            max_length=12.0
                        )
                    )
                    tier_description: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="tierDescription",
                            type="Element",
                            min_length=1.0,
                            max_length=35.0
                        )
                    )
                    company_code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="companyCode",
                            type="Element",
                            min_length=1.0,
                            max_length=35.0
                        )
                    )
                    customer_value: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="customerValue",
                            type="Element"
                        )
                    )
                    type: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="type",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

    @dataclass
    class FareFamilies:
        """
        :ivar family_information:
        :ivar family_criteria:
        :ivar fare_family_segment:
        :ivar other_possible_criteria:
        """
        family_information: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyInformation"] = field(
            default=None,
            metadata=dict(
                name="familyInformation",
                type="Element",
                required=True
            )
        )
        family_criteria: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria"] = field(
            default=None,
            metadata=dict(
                name="familyCriteria",
                type="Element"
            )
        )
        fare_family_segment: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment"] = field(
            default_factory=list,
            metadata=dict(
                name="fareFamilySegment",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )
        other_possible_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria"] = field(
            default_factory=list,
            metadata=dict(
                name="otherPossibleCriteria",
                type="Element",
                min_occurs=0,
                max_occurs=20
            )
        )

        @dataclass
        class FamilyInformation:
            """
            :ivar ref_number:
            :ivar fare_familyname:
            :ivar hierarchy:
            :ivar commercial_family_details:
            """
            ref_number: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="refNumber",
                    type="Element"
                )
            )
            fare_familyname: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="fareFamilyname",
                    type="Element",
                    min_length=1.0,
                    max_length=10.0
                )
            )
            hierarchy: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="hierarchy",
                    type="Element"
                )
            )
            commercial_family_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyInformation.CommercialFamilyDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="commercialFamilyDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )

            @dataclass
            class CommercialFamilyDetails:
                """
                :ivar commercial_family:
                """
                commercial_family: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="commercialFamily",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=10.0
                    )
                )

        @dataclass
        class FamilyCriteria:
            """
            :ivar carrier_id:
            :ivar rdb:
            :ivar fare_family_info:
            :ivar fare_product_detail:
            :ivar corporate_info:
            :ivar cabin_product:
            :ivar cabin_processing_identifier:
            :ivar date_time_details:
            :ivar other_criteria:
            """
            carrier_id: List[str] = field(
                default_factory=list,
                metadata=dict(
                    name="carrierId",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20,
                    min_length=1.0,
                    max_length=3.0
                )
            )
            rdb: List[str] = field(
                default_factory=list,
                metadata=dict(
                    name="rdb",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20,
                    min_length=1.0,
                    max_length=2.0
                )
            )
            fare_family_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.FareFamilyInfo"] = field(
                default=None,
                metadata=dict(
                    name="fareFamilyInfo",
                    type="Element"
                )
            )
            fare_product_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.FareProductDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="fareProductDetail",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            corporate_info: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.CorporateInfo"] = field(
                default_factory=list,
                metadata=dict(
                    name="corporateInfo",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            cabin_product: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.CabinProduct"] = field(
                default_factory=list,
                metadata=dict(
                    name="cabinProduct",
                    type="Element",
                    min_occurs=0,
                    max_occurs=6
                )
            )
            cabin_processing_identifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="cabinProcessingIdentifier",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            date_time_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.DateTimeDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="dateTimeDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            other_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.OtherCriteria"] = field(
                default_factory=list,
                metadata=dict(
                    name="otherCriteria",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )

            @dataclass
            class FareFamilyInfo:
                """
                :ivar fare_family_qual:
                """
                fare_family_qual: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="fareFamilyQual",
                        type="Element",
                        min_occurs=1,
                        max_occurs=9,
                        min_length=0.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class FareProductDetail:
                """
                :ivar fare_basis:
                :ivar fare_type:
                """
                fare_basis: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="fareBasis",
                        type="Element",
                        min_length=0.0,
                        max_length=18.0
                    )
                )
                fare_type: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="fareType",
                        type="Element",
                        min_occurs=0,
                        max_occurs=3,
                        min_length=0.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class CorporateInfo:
                """
                :ivar corporate_number_identifier:
                :ivar corporate_name:
                """
                corporate_number_identifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="corporateNumberIdentifier",
                        type="Element",
                        min_length=1.0,
                        max_length=12.0
                    )
                )
                corporate_name: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="corporateName",
                        type="Element",
                        min_length=1.0,
                        max_length=20.0
                    )
                )

            @dataclass
            class CabinProduct:
                """
                :ivar cabin_designator:
                """
                cabin_designator: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="cabinDesignator",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class DateTimeDetails:
                """
                :ivar date:
                :ivar other_date:
                """
                date: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="date",
                        type="Element",
                        required=True,
                        min_length=6.0,
                        max_length=6.0
                    )
                )
                other_date: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="otherDate",
                        type="Element"
                    )
                )

            @dataclass
            class OtherCriteria:
                """
                :ivar name:
                :ivar value:
                """
                name: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="name",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=5.0
                    )
                )
                value: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="value",
                        type="Element",
                        min_occurs=0,
                        max_occurs=10,
                        min_length=1.0,
                        max_length=20.0
                    )
                )

        @dataclass
        class FareFamilySegment:
            """
            :ivar reference_info:
            :ivar family_criteria:
            """
            reference_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.ReferenceInfo"] = field(
                default=None,
                metadata=dict(
                    name="referenceInfo",
                    type="Element",
                    required=True
                )
            )
            family_criteria: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria"] = field(
                default=None,
                metadata=dict(
                    name="familyCriteria",
                    type="Element"
                )
            )

            @dataclass
            class ReferenceInfo:
                """
                :ivar referencing_detail:
                """
                referencing_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.ReferenceInfo.ReferencingDetail"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="referencingDetail",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9
                    )
                )

                @dataclass
                class ReferencingDetail:
                    """
                    :ivar ref_qualifier:
                    :ivar ref_number:
                    """
                    ref_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="refQualifier",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    ref_number: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="refNumber",
                            type="Element",
                            required=True
                        )
                    )

            @dataclass
            class FamilyCriteria:
                """
                :ivar carrier_id:
                :ivar rdb:
                :ivar fare_family_info:
                :ivar fare_product_detail:
                :ivar corporate_info:
                :ivar cabin_product:
                :ivar cabin_processing_identifier:
                :ivar date_time_details:
                :ivar other_criteria:
                """
                carrier_id: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="carrierId",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20,
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                rdb: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="rdb",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20,
                        min_length=1.0,
                        max_length=2.0
                    )
                )
                fare_family_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.FareFamilyInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="fareFamilyInfo",
                        type="Element"
                    )
                )
                fare_product_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.FareProductDetail"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="fareProductDetail",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )
                corporate_info: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.CorporateInfo"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="corporateInfo",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )
                cabin_product: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.CabinProduct"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="cabinProduct",
                        type="Element",
                        min_occurs=0,
                        max_occurs=6
                    )
                )
                cabin_processing_identifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="cabinProcessingIdentifier",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                date_time_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.DateTimeDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="dateTimeDetails",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )
                other_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.OtherCriteria"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="otherCriteria",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )

                @dataclass
                class FareFamilyInfo:
                    """
                    :ivar fare_family_qual:
                    """
                    fare_family_qual: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="fareFamilyQual",
                            type="Element",
                            min_occurs=1,
                            max_occurs=9,
                            min_length=0.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class FareProductDetail:
                    """
                    :ivar fare_basis:
                    :ivar fare_type:
                    """
                    fare_basis: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="fareBasis",
                            type="Element",
                            min_length=0.0,
                            max_length=18.0
                        )
                    )
                    fare_type: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="fareType",
                            type="Element",
                            min_occurs=0,
                            max_occurs=3,
                            min_length=0.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class CorporateInfo:
                    """
                    :ivar corporate_number_identifier:
                    :ivar corporate_name:
                    """
                    corporate_number_identifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="corporateNumberIdentifier",
                            type="Element",
                            min_length=1.0,
                            max_length=12.0
                        )
                    )
                    corporate_name: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="corporateName",
                            type="Element",
                            min_length=1.0,
                            max_length=20.0
                        )
                    )

                @dataclass
                class CabinProduct:
                    """
                    :ivar cabin_designator:
                    """
                    cabin_designator: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="cabinDesignator",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

                @dataclass
                class DateTimeDetails:
                    """
                    :ivar date:
                    :ivar other_date:
                    """
                    date: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="date",
                            type="Element",
                            required=True,
                            min_length=6.0,
                            max_length=6.0
                        )
                    )
                    other_date: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="otherDate",
                            type="Element"
                        )
                    )

                @dataclass
                class OtherCriteria:
                    """
                    :ivar name:
                    :ivar value:
                    """
                    name: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="name",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=5.0
                        )
                    )
                    value: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="value",
                            type="Element",
                            min_occurs=0,
                            max_occurs=10,
                            min_length=1.0,
                            max_length=20.0
                        )
                    )

        @dataclass
        class OtherPossibleCriteria:
            """
            :ivar logical_link:
            :ivar family_criteria:
            :ivar fare_family_segment:
            """
            logical_link: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.LogicalLink"] = field(
                default=None,
                metadata=dict(
                    name="logicalLink",
                    type="Element",
                    required=True
                )
            )
            family_criteria: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria"] = field(
                default=None,
                metadata=dict(
                    name="familyCriteria",
                    type="Element"
                )
            )
            fare_family_segment: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment"] = field(
                default_factory=list,
                metadata=dict(
                    name="fareFamilySegment",
                    type="Element",
                    min_occurs=0,
                    max_occurs=6
                )
            )

            @dataclass
            class LogicalLink:
                """
                :ivar boolean_expression:
                """
                boolean_expression: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.LogicalLink.BooleanExpression"] = field(
                    default=None,
                    metadata=dict(
                        name="booleanExpression",
                        type="Element",
                        required=True
                    )
                )

                @dataclass
                class BooleanExpression:
                    """
                    :ivar code_operator:
                    """
                    code_operator: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="codeOperator",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

            @dataclass
            class FamilyCriteria:
                """
                :ivar carrier_id:
                :ivar rdb:
                :ivar fare_family_info:
                :ivar fare_product_detail:
                :ivar corporate_info:
                :ivar cabin_product:
                :ivar cabin_processing_identifier:
                :ivar date_time_details:
                :ivar other_criteria:
                """
                carrier_id: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="carrierId",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20,
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                rdb: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="rdb",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20,
                        min_length=1.0,
                        max_length=2.0
                    )
                )
                fare_family_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.FareFamilyInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="fareFamilyInfo",
                        type="Element"
                    )
                )
                fare_product_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.FareProductDetail"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="fareProductDetail",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )
                corporate_info: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.CorporateInfo"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="corporateInfo",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )
                cabin_product: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.CabinProduct"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="cabinProduct",
                        type="Element",
                        min_occurs=0,
                        max_occurs=6
                    )
                )
                cabin_processing_identifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="cabinProcessingIdentifier",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                date_time_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.DateTimeDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="dateTimeDetails",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )
                other_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.OtherCriteria"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="otherCriteria",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )

                @dataclass
                class FareFamilyInfo:
                    """
                    :ivar fare_family_qual:
                    """
                    fare_family_qual: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="fareFamilyQual",
                            type="Element",
                            min_occurs=1,
                            max_occurs=9,
                            min_length=0.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class FareProductDetail:
                    """
                    :ivar fare_basis:
                    :ivar fare_type:
                    """
                    fare_basis: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="fareBasis",
                            type="Element",
                            min_length=0.0,
                            max_length=18.0
                        )
                    )
                    fare_type: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="fareType",
                            type="Element",
                            min_occurs=0,
                            max_occurs=3,
                            min_length=0.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class CorporateInfo:
                    """
                    :ivar corporate_number_identifier:
                    :ivar corporate_name:
                    """
                    corporate_number_identifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="corporateNumberIdentifier",
                            type="Element",
                            min_length=1.0,
                            max_length=12.0
                        )
                    )
                    corporate_name: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="corporateName",
                            type="Element",
                            min_length=1.0,
                            max_length=20.0
                        )
                    )

                @dataclass
                class CabinProduct:
                    """
                    :ivar cabin_designator:
                    """
                    cabin_designator: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="cabinDesignator",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

                @dataclass
                class DateTimeDetails:
                    """
                    :ivar date:
                    :ivar other_date:
                    """
                    date: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="date",
                            type="Element",
                            required=True,
                            min_length=6.0,
                            max_length=6.0
                        )
                    )
                    other_date: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="otherDate",
                            type="Element"
                        )
                    )

                @dataclass
                class OtherCriteria:
                    """
                    :ivar name:
                    :ivar value:
                    """
                    name: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="name",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=5.0
                        )
                    )
                    value: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="value",
                            type="Element",
                            min_occurs=0,
                            max_occurs=10,
                            min_length=1.0,
                            max_length=20.0
                        )
                    )

            @dataclass
            class FareFamilySegment:
                """
                :ivar reference_info:
                :ivar family_criteria:
                """
                reference_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.ReferenceInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="referenceInfo",
                        type="Element",
                        required=True
                    )
                )
                family_criteria: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria"] = field(
                    default=None,
                    metadata=dict(
                        name="familyCriteria",
                        type="Element"
                    )
                )

                @dataclass
                class ReferenceInfo:
                    """
                    :ivar referencing_detail:
                    """
                    referencing_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.ReferenceInfo.ReferencingDetail"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="referencingDetail",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9
                        )
                    )

                    @dataclass
                    class ReferencingDetail:
                        """
                        :ivar ref_qualifier:
                        :ivar ref_number:
                        """
                        ref_qualifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="refQualifier",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        ref_number: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="refNumber",
                                type="Element",
                                required=True
                            )
                        )

                @dataclass
                class FamilyCriteria:
                    """
                    :ivar carrier_id:
                    :ivar rdb:
                    :ivar fare_family_info:
                    :ivar fare_product_detail:
                    :ivar corporate_info:
                    :ivar cabin_product:
                    :ivar cabin_processing_identifier:
                    :ivar date_time_details:
                    :ivar other_criteria:
                    """
                    carrier_id: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="carrierId",
                            type="Element",
                            min_occurs=0,
                            max_occurs=20,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    rdb: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="rdb",
                            type="Element",
                            min_occurs=0,
                            max_occurs=20,
                            min_length=1.0,
                            max_length=2.0
                        )
                    )
                    fare_family_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.FareFamilyInfo"] = field(
                        default=None,
                        metadata=dict(
                            name="fareFamilyInfo",
                            type="Element"
                        )
                    )
                    fare_product_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.FareProductDetail"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="fareProductDetail",
                            type="Element",
                            min_occurs=0,
                            max_occurs=20
                        )
                    )
                    corporate_info: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.CorporateInfo"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="corporateInfo",
                            type="Element",
                            min_occurs=0,
                            max_occurs=20
                        )
                    )
                    cabin_product: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.CabinProduct"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="cabinProduct",
                            type="Element",
                            min_occurs=0,
                            max_occurs=6
                        )
                    )
                    cabin_processing_identifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="cabinProcessingIdentifier",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    date_time_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.DateTimeDetails"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="dateTimeDetails",
                            type="Element",
                            min_occurs=0,
                            max_occurs=20
                        )
                    )
                    other_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.OtherCriteria"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="otherCriteria",
                            type="Element",
                            min_occurs=0,
                            max_occurs=20
                        )
                    )

                    @dataclass
                    class FareFamilyInfo:
                        """
                        :ivar fare_family_qual:
                        """
                        fare_family_qual: List[str] = field(
                            default_factory=list,
                            metadata=dict(
                                name="fareFamilyQual",
                                type="Element",
                                min_occurs=1,
                                max_occurs=9,
                                min_length=0.0,
                                max_length=3.0
                            )
                        )

                    @dataclass
                    class FareProductDetail:
                        """
                        :ivar fare_basis:
                        :ivar fare_type:
                        """
                        fare_basis: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="fareBasis",
                                type="Element",
                                min_length=0.0,
                                max_length=18.0
                            )
                        )
                        fare_type: List[str] = field(
                            default_factory=list,
                            metadata=dict(
                                name="fareType",
                                type="Element",
                                min_occurs=0,
                                max_occurs=3,
                                min_length=0.0,
                                max_length=3.0
                            )
                        )

                    @dataclass
                    class CorporateInfo:
                        """
                        :ivar corporate_number_identifier:
                        :ivar corporate_name:
                        """
                        corporate_number_identifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="corporateNumberIdentifier",
                                type="Element",
                                min_length=1.0,
                                max_length=12.0
                            )
                        )
                        corporate_name: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="corporateName",
                                type="Element",
                                min_length=1.0,
                                max_length=20.0
                            )
                        )

                    @dataclass
                    class CabinProduct:
                        """
                        :ivar cabin_designator:
                        """
                        cabin_designator: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="cabinDesignator",
                                type="Element",
                                required=True,
                                min_length=1.0,
                                max_length=1.0
                            )
                        )

                    @dataclass
                    class DateTimeDetails:
                        """
                        :ivar date:
                        :ivar other_date:
                        """
                        date: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="date",
                                type="Element",
                                required=True,
                                min_length=6.0,
                                max_length=6.0
                            )
                        )
                        other_date: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="otherDate",
                                type="Element"
                            )
                        )

                    @dataclass
                    class OtherCriteria:
                        """
                        :ivar name:
                        :ivar value:
                        """
                        name: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="name",
                                type="Element",
                                required=True,
                                min_length=1.0,
                                max_length=5.0
                            )
                        )
                        value: List[str] = field(
                            default_factory=list,
                            metadata=dict(
                                name="value",
                                type="Element",
                                min_occurs=0,
                                max_occurs=10,
                                min_length=1.0,
                                max_length=20.0
                            )
                        )

    @dataclass
    class FareOptions:
        """
        :ivar pricing_tick_info:
        :ivar corporate:
        :ivar ticketing_price_scheme:
        :ivar fee_id_description:
        :ivar conversion_rate:
        :ivar form_of_payment:
        :ivar frequent_traveller_info:
        :ivar monetary_cabin_info:
        """
        pricing_tick_info: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo"] = field(
            default=None,
            metadata=dict(
                name="pricingTickInfo",
                type="Element",
                required=True
            )
        )
        corporate: Optional["FareMasterPricerTravelBoardSearch.FareOptions.Corporate"] = field(
            default=None,
            metadata=dict(
                name="corporate",
                type="Element"
            )
        )
        ticketing_price_scheme: Optional["FareMasterPricerTravelBoardSearch.FareOptions.TicketingPriceScheme"] = field(
            default=None,
            metadata=dict(
                name="ticketingPriceScheme",
                type="Element"
            )
        )
        fee_id_description: Optional["FareMasterPricerTravelBoardSearch.FareOptions.FeeIdDescription"] = field(
            default=None,
            metadata=dict(
                name="feeIdDescription",
                type="Element"
            )
        )
        conversion_rate: Optional["FareMasterPricerTravelBoardSearch.FareOptions.ConversionRate"] = field(
            default=None,
            metadata=dict(
                name="conversionRate",
                type="Element"
            )
        )
        form_of_payment: Optional["FareMasterPricerTravelBoardSearch.FareOptions.FormOfPayment"] = field(
            default=None,
            metadata=dict(
                name="formOfPayment",
                type="Element"
            )
        )
        frequent_traveller_info: Optional["FareMasterPricerTravelBoardSearch.FareOptions.FrequentTravellerInfo"] = field(
            default=None,
            metadata=dict(
                name="frequentTravellerInfo",
                type="Element"
            )
        )
        monetary_cabin_info: Optional["FareMasterPricerTravelBoardSearch.FareOptions.MonetaryCabinInfo"] = field(
            default=None,
            metadata=dict(
                name="monetaryCabinInfo",
                type="Element"
            )
        )

        @dataclass
        class PricingTickInfo:
            """
            :ivar pricing_ticketing:
            :ivar ticketing_date:
            :ivar company_id:
            :ivar selling_point:
            :ivar ticketing_point:
            :ivar journey_origin_point:
            :ivar corporate_id:
            """
            pricing_ticketing: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.PricingTicketing"] = field(
                default=None,
                metadata=dict(
                    name="pricingTicketing",
                    type="Element"
                )
            )
            ticketing_date: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.TicketingDate"] = field(
                default=None,
                metadata=dict(
                    name="ticketingDate",
                    type="Element"
                )
            )
            company_id: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.CompanyId"] = field(
                default=None,
                metadata=dict(
                    name="companyId",
                    type="Element"
                )
            )
            selling_point: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.SellingPoint"] = field(
                default=None,
                metadata=dict(
                    name="sellingPoint",
                    type="Element"
                )
            )
            ticketing_point: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.TicketingPoint"] = field(
                default=None,
                metadata=dict(
                    name="ticketingPoint",
                    type="Element"
                )
            )
            journey_origin_point: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.JourneyOriginPoint"] = field(
                default=None,
                metadata=dict(
                    name="journeyOriginPoint",
                    type="Element"
                )
            )
            corporate_id: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.CorporateId"] = field(
                default=None,
                metadata=dict(
                    name="corporateId",
                    type="Element"
                )
            )

            @dataclass
            class PricingTicketing:
                """
                :ivar price_type:
                """
                price_type: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="priceType",
                        type="Element",
                        min_occurs=1,
                        max_occurs=50,
                        min_length=0.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class TicketingDate:
                """
                :ivar date:
                :ivar rtc_date:
                """
                date: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="date",
                        type="Element",
                        required=True,
                        min_length=6.0,
                        max_length=6.0
                    )
                )
                rtc_date: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="rtcDate",
                        type="Element",
                        min_length=6.0,
                        max_length=6.0
                    )
                )

            @dataclass
            class CompanyId:
                """
                :ivar value:
                """
                value: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="value",
                        type="Extension"
                    )
                )

            @dataclass
            class SellingPoint:
                """
                :ivar location_id:
                :ivar country:
                """
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                country: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="country",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class TicketingPoint:
                """
                :ivar location_id:
                :ivar country:
                """
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                country: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="country",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class JourneyOriginPoint:
                """
                :ivar location_id:
                :ivar country:
                """
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                country: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="country",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class CorporateId:
                """
                :ivar arc_number:
                :ivar ersp_number:
                :ivar iata_number:
                """
                arc_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="arcNumber",
                        type="Element",
                        min_length=1.0,
                        max_length=12.0
                    )
                )
                ersp_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="erspNumber",
                        type="Element",
                        min_length=1.0,
                        max_length=12.0
                    )
                )
                iata_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="iataNumber",
                        type="Element",
                        min_length=1.0,
                        max_length=12.0
                    )
                )

        @dataclass
        class Corporate:
            """
            :ivar corporate_id:
            """
            corporate_id: List["FareMasterPricerTravelBoardSearch.FareOptions.Corporate.CorporateId"] = field(
                default_factory=list,
                metadata=dict(
                    name="corporateId",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )

            @dataclass
            class CorporateId:
                """
                :ivar corporate_qualifier:
                :ivar identity:
                """
                corporate_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="corporateQualifier",
                        type="Element",
                        required=True,
                        min_length=0.0,
                        max_length=3.0
                    )
                )
                identity: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="identity",
                        type="Element",
                        min_occurs=1,
                        max_occurs=9,
                        min_length=1.0,
                        max_length=20.0
                    )
                )

        @dataclass
        class TicketingPriceScheme:
            """
            :ivar reference_number:
            :ivar name:
            :ivar status:
            :ivar description:
            """
            reference_number: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="referenceNumber",
                    type="Element",
                    required=True,
                    min_length=1.0,
                    max_length=35.0
                )
            )
            name: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="name",
                    type="Element",
                    min_length=1.0,
                    max_length=35.0
                )
            )
            status: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="status",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            description: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="description",
                    type="Element",
                    min_length=1.0,
                    max_length=250.0
                )
            )

        @dataclass
        class FeeIdDescription:
            """
            :ivar fee_id:
            """
            fee_id: List["FareMasterPricerTravelBoardSearch.FareOptions.FeeIdDescription.FeeId"] = field(
                default_factory=list,
                metadata=dict(
                    name="feeId",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )

            @dataclass
            class FeeId:
                """
                :ivar fee_type:
                :ivar fee_id_number:
                """
                fee_type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="feeType",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=5.0
                    )
                )
                fee_id_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="feeIdNumber",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=50.0
                    )
                )

        @dataclass
        class ConversionRate:
            """
            :ivar conversion_rate_detail:
            """
            conversion_rate_detail: List["FareMasterPricerTravelBoardSearch.FareOptions.ConversionRate.ConversionRateDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="conversionRateDetail",
                    type="Element",
                    min_occurs=1,
                    max_occurs=2
                )
            )

            @dataclass
            class ConversionRateDetail:
                """
                :ivar conversion_type:
                :ivar currency:
                """
                conversion_type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="conversionType",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                currency: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="currency",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )

        @dataclass
        class FormOfPayment:
            """
            :ivar form_of_payment_details:
            """
            form_of_payment_details: List["FareMasterPricerTravelBoardSearch.FareOptions.FormOfPayment.FormOfPaymentDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="formOfPaymentDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9
                )
            )

            @dataclass
            class FormOfPaymentDetails:
                """
                :ivar type:
                :ivar charged_amount:
                :ivar credit_card_number:
                """
                type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="type",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                charged_amount: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="chargedAmount",
                        type="Element"
                    )
                )
                credit_card_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="creditCardNumber",
                        type="Element",
                        min_length=1.0,
                        max_length=20.0
                    )
                )

        @dataclass
        class FrequentTravellerInfo:
            """
            :ivar frequent_traveller_details:
            """
            frequent_traveller_details: List["FareMasterPricerTravelBoardSearch.FareOptions.FrequentTravellerInfo.FrequentTravellerDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="frequentTravellerDetails",
                    type="Element",
                    min_occurs=1,
                    max_occurs=99
                )
            )

            @dataclass
            class FrequentTravellerDetails:
                """
                :ivar carrier:
                :ivar number:
                :ivar customer_reference:
                :ivar tier_level:
                :ivar priority_code:
                :ivar tier_description:
                :ivar type:
                """
                carrier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="carrier",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="number",
                        type="Element",
                        min_length=1.0,
                        max_length=25.0
                    )
                )
                customer_reference: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="customerReference",
                        type="Element",
                        min_length=1.0,
                        max_length=10.0
                    )
                )
                tier_level: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="tierLevel",
                        type="Element",
                        min_length=1.0,
                        max_length=35.0
                    )
                )
                priority_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="priorityCode",
                        type="Element",
                        min_length=1.0,
                        max_length=12.0
                    )
                )
                tier_description: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="tierDescription",
                        type="Element",
                        min_length=1.0,
                        max_length=35.0
                    )
                )
                type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="type",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

        @dataclass
        class MonetaryCabinInfo:
            """
            :ivar money_and_cabin_info:
            """
            money_and_cabin_info: List["FareMasterPricerTravelBoardSearch.FareOptions.MonetaryCabinInfo.MoneyAndCabinInfo"] = field(
                default_factory=list,
                metadata=dict(
                    name="moneyAndCabinInfo",
                    type="Element",
                    min_occurs=0,
                    max_occurs=99
                )
            )

            @dataclass
            class MoneyAndCabinInfo:
                """
                :ivar amount_type:
                :ivar amount:
                :ivar currency:
                :ivar location_id:
                :ivar cabin_class_designator:
                """
                amount_type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="amountType",
                        type="Element",
                        min_length=0.0,
                        max_length=3.0
                    )
                )
                amount: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="amount",
                        type="Element",
                        required=True
                    )
                )
                currency: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="currency",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                cabin_class_designator: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="cabinClassDesignator",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9,
                        min_length=1.0,
                        max_length=1.0
                    )
                )

    @dataclass
    class PriceToBeat:
        """
        :ivar money_info:
        :ivar additional_money_info:
        """
        money_info: Optional["FareMasterPricerTravelBoardSearch.PriceToBeat.MoneyInfo"] = field(
            default=None,
            metadata=dict(
                name="moneyInfo",
                type="Element",
                required=True
            )
        )
        additional_money_info: List["FareMasterPricerTravelBoardSearch.PriceToBeat.AdditionalMoneyInfo"] = field(
            default_factory=list,
            metadata=dict(
                name="additionalMoneyInfo",
                type="Element",
                min_occurs=0,
                max_occurs=19
            )
        )

        @dataclass
        class MoneyInfo:
            """
            :ivar qualifier:
            :ivar amount:
            :ivar currency:
            """
            qualifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="qualifier",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            amount: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="amount",
                    type="Element",
                    required=True
                )
            )
            currency: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="currency",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )

        @dataclass
        class AdditionalMoneyInfo:
            """
            :ivar qualifier:
            :ivar amount:
            :ivar currency:
            :ivar location_id:
            """
            qualifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="qualifier",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            amount: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="amount",
                    type="Element",
                    required=True
                )
            )
            currency: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="currency",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            location_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="locationId",
                    type="Element",
                    min_length=3.0,
                    max_length=3.0
                )
            )

    @dataclass
    class TaxInfo:
        """
        :ivar withhold_tax_surcharge:
        :ivar tax_detail:
        """
        withhold_tax_surcharge: Optional[str] = field(
            default=None,
            metadata=dict(
                name="withholdTaxSurcharge",
                type="Element",
                min_length=1.0,
                max_length=3.0
            )
        )
        tax_detail: List["FareMasterPricerTravelBoardSearch.TaxInfo.TaxDetail"] = field(
            default_factory=list,
            metadata=dict(
                name="taxDetail",
                type="Element",
                min_occurs=0,
                max_occurs=99
            )
        )

        @dataclass
        class TaxDetail:
            """
            :ivar rate:
            :ivar country:
            :ivar currency:
            :ivar type:
            :ivar amount_qualifier:
            """
            rate: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="rate",
                    type="Element",
                    min_length=1.0,
                    max_length=18.0
                )
            )
            country: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="country",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            currency: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="currency",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="type",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            amount_qualifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="amountQualifier",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )

    @dataclass
    class TravelFlightInfo:
        """
        :ivar cabin_id:
        :ivar company_identity:
        :ivar flight_detail:
        :ivar inclusion_detail:
        :ivar exclusion_detail:
        :ivar unit_number_detail:
        """
        cabin_id: Optional["FareMasterPricerTravelBoardSearch.TravelFlightInfo.CabinId"] = field(
            default=None,
            metadata=dict(
                name="cabinId",
                type="Element"
            )
        )
        company_identity: List["FareMasterPricerTravelBoardSearch.TravelFlightInfo.CompanyIdentity"] = field(
            default_factory=list,
            metadata=dict(
                name="companyIdentity",
                type="Element",
                min_occurs=0,
                max_occurs=20
            )
        )
        flight_detail: Optional["FareMasterPricerTravelBoardSearch.TravelFlightInfo.FlightDetail"] = field(
            default=None,
            metadata=dict(
                name="flightDetail",
                type="Element"
            )
        )
        inclusion_detail: List["FareMasterPricerTravelBoardSearch.TravelFlightInfo.InclusionDetail"] = field(
            default_factory=list,
            metadata=dict(
                name="inclusionDetail",
                type="Element",
                min_occurs=0,
                max_occurs=20
            )
        )
        exclusion_detail: List["FareMasterPricerTravelBoardSearch.TravelFlightInfo.ExclusionDetail"] = field(
            default_factory=list,
            metadata=dict(
                name="exclusionDetail",
                type="Element",
                min_occurs=0,
                max_occurs=20
            )
        )
        unit_number_detail: List["FareMasterPricerTravelBoardSearch.TravelFlightInfo.UnitNumberDetail"] = field(
            default_factory=list,
            metadata=dict(
                name="unitNumberDetail",
                type="Element",
                min_occurs=0,
                max_occurs=20
            )
        )

        @dataclass
        class CabinId:
            """
            :ivar cabin_qualifier:
            :ivar cabin:
            """
            cabin_qualifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="cabinQualifier",
                    type="Element",
                    min_length=1.0,
                    max_length=2.0
                )
            )
            cabin: List[str] = field(
                default_factory=list,
                metadata=dict(
                    name="cabin",
                    type="Element",
                    min_occurs=0,
                    max_occurs=5,
                    min_length=0.0,
                    max_length=1.0
                )
            )

        @dataclass
        class CompanyIdentity:
            """
            :ivar carrier_qualifier:
            :ivar carrier_id:
            """
            carrier_qualifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="carrierQualifier",
                    type="Element",
                    required=True,
                    min_length=0.0,
                    max_length=1.0
                )
            )
            carrier_id: List[str] = field(
                default_factory=list,
                metadata=dict(
                    name="carrierId",
                    type="Element",
                    min_occurs=1,
                    max_occurs=999,
                    min_length=2.0,
                    max_length=3.0
                )
            )

        @dataclass
        class FlightDetail:
            """
            :ivar flight_type:
            """
            flight_type: List[str] = field(
                default_factory=list,
                metadata=dict(
                    name="flightType",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9,
                    min_length=1.0,
                    max_length=2.0
                )
            )

        @dataclass
        class InclusionDetail:
            """
            :ivar inclusion_identifier:
            :ivar location_id:
            :ivar airport_city_qualifier:
            """
            inclusion_identifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="inclusionIdentifier",
                    type="Element",
                    required=True,
                    min_length=0.0,
                    max_length=1.0
                )
            )
            location_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="locationId",
                    type="Element",
                    required=True,
                    min_length=3.0,
                    max_length=5.0
                )
            )
            airport_city_qualifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="airportCityQualifier",
                    type="Element",
                    min_length=1.0,
                    max_length=1.0
                )
            )

        @dataclass
        class ExclusionDetail:
            """
            :ivar exclusion_identifier:
            :ivar location_id:
            :ivar airport_city_qualifier:
            """
            exclusion_identifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="exclusionIdentifier",
                    type="Element",
                    required=True,
                    min_length=0.0,
                    max_length=1.0
                )
            )
            location_id: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="locationId",
                    type="Element",
                    required=True,
                    min_length=3.0,
                    max_length=5.0
                )
            )
            airport_city_qualifier: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="airportCityQualifier",
                    type="Element",
                    min_length=1.0,
                    max_length=1.0
                )
            )

        @dataclass
        class UnitNumberDetail:
            """
            :ivar number_of_units:
            :ivar type_of_unit:
            """
            number_of_units: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="numberOfUnits",
                    type="Element",
                    required=True
                )
            )
            type_of_unit: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="typeOfUnit",
                    type="Element",
                    required=True,
                    min_length=1.0,
                    max_length=3.0
                )
            )

    @dataclass
    class ValueSearch:
        """
        :ivar criteria_name:
        :ivar criteria_code:
        :ivar value:
        :ivar criteria_details:
        """
        criteria_name: Optional[str] = field(
            default=None,
            metadata=dict(
                name="criteriaName",
                type="Element",
                min_length=1.0,
                max_length=50.0
            )
        )
        criteria_code: Optional[str] = field(
            default=None,
            metadata=dict(
                name="criteriaCode",
                type="Element",
                min_length=1.0,
                max_length=3.0
            )
        )
        value: Optional[str] = field(
            default=None,
            metadata=dict(
                name="value",
                type="Element",
                min_length=1.0,
                max_length=18.0
            )
        )
        criteria_details: List["FareMasterPricerTravelBoardSearch.ValueSearch.CriteriaDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="criteriaDetails",
                type="Element",
                min_occurs=0,
                max_occurs=10
            )
        )

        @dataclass
        class CriteriaDetails:
            """
            :ivar type:
            :ivar value:
            :ivar attribute:
            """
            type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="type",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            value: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="value",
                    type="Element",
                    min_length=1.0,
                    max_length=18.0
                )
            )
            attribute: List[str] = field(
                default_factory=list,
                metadata=dict(
                    name="attribute",
                    type="Element",
                    min_occurs=0,
                    max_occurs=99,
                    min_length=1.0,
                    max_length=9.0
                )
            )

    @dataclass
    class Buckets:
        """
        :ivar bucket_info:
        :ivar bucket_details:
        """
        bucket_info: Optional["FareMasterPricerTravelBoardSearch.Buckets.BucketInfo"] = field(
            default=None,
            metadata=dict(
                name="bucketInfo",
                type="Element",
                required=True
            )
        )
        bucket_details: List["FareMasterPricerTravelBoardSearch.Buckets.BucketDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="bucketDetails",
                type="Element",
                min_occurs=0,
                max_occurs=15
            )
        )

        @dataclass
        class BucketInfo:
            """
            :ivar number:
            :ivar name:
            :ivar completion:
            :ivar mode:
            :ivar value_ref:
            :ivar weight:
            :ivar count:
            :ivar attribute_count:
            """
            number: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="number",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            name: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="name",
                    type="Element",
                    min_length=1.0,
                    max_length=20.0
                )
            )
            completion: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="completion",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            mode: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="mode",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            value_ref: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="valueRef",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            weight: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="weight",
                    type="Element"
                )
            )
            count: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="count",
                    type="Element"
                )
            )
            attribute_count: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="attributeCount",
                    type="Element"
                )
            )

        @dataclass
        class BucketDetails:
            """
            :ivar code:
            :ivar type:
            :ivar attribute:
            """
            code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="code",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="type",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            attribute: List["FareMasterPricerTravelBoardSearch.Buckets.BucketDetails.Attribute"] = field(
                default_factory=list,
                metadata=dict(
                    name="attribute",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )

            @dataclass
            class Attribute:
                """
                :ivar requested_sgt:
                :ivar value:
                """
                requested_sgt: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="requestedSgt",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                value: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="value",
                        type="Element",
                        min_occurs=0,
                        max_occurs=50,
                        min_length=1.0,
                        max_length=20.0
                    )
                )

    @dataclass
    class Itinerary:
        """
        :ivar requested_segment_ref:
        :ivar departure_localization:
        :ivar arrival_localization:
        :ivar time_details:
        :ivar flight_info:
        :ivar family_information:
        :ivar value_search:
        :ivar group_of_flights:
        :ivar flight_info_pnr:
        :ivar requested_segment_action:
        :ivar attributes:
        """
        requested_segment_ref: Optional["FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentRef"] = field(
            default=None,
            metadata=dict(
                name="requestedSegmentRef",
                type="Element",
                required=True
            )
        )
        departure_localization: Optional["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization"] = field(
            default=None,
            metadata=dict(
                name="departureLocalization",
                type="Element"
            )
        )
        arrival_localization: Optional["FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization"] = field(
            default=None,
            metadata=dict(
                name="arrivalLocalization",
                type="Element"
            )
        )
        time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails"] = field(
            default=None,
            metadata=dict(
                name="timeDetails",
                type="Element"
            )
        )
        flight_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo"] = field(
            default=None,
            metadata=dict(
                name="flightInfo",
                type="Element"
            )
        )
        family_information: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FamilyInformation"] = field(
            default=None,
            metadata=dict(
                name="familyInformation",
                type="Element"
            )
        )
        value_search: List["FareMasterPricerTravelBoardSearch.Itinerary.ValueSearch"] = field(
            default_factory=list,
            metadata=dict(
                name="valueSearch",
                type="Element",
                min_occurs=0,
                max_occurs=99
            )
        )
        group_of_flights: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights"] = field(
            default_factory=list,
            metadata=dict(
                name="groupOfFlights",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )
        flight_info_pnr: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr"] = field(
            default_factory=list,
            metadata=dict(
                name="flightInfoPNR",
                type="Element",
                min_occurs=0,
                max_occurs=4
            )
        )
        requested_segment_action: Optional["FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentAction"] = field(
            default=None,
            metadata=dict(
                name="requestedSegmentAction",
                type="Element"
            )
        )
        attributes: Optional["FareMasterPricerTravelBoardSearch.Itinerary.Attributes"] = field(
            default=None,
            metadata=dict(
                name="attributes",
                type="Element"
            )
        )

        @dataclass
        class RequestedSegmentRef:
            """
            :ivar seg_ref:
            :ivar location_forcing:
            """
            seg_ref: Optional[float] = field(
                default=None,
                metadata=dict(
                    name="segRef",
                    type="Element",
                    required=True
                )
            )
            location_forcing: List["FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentRef.LocationForcing"] = field(
                default_factory=list,
                metadata=dict(
                    name="locationForcing",
                    type="Element",
                    min_occurs=0,
                    max_occurs=2
                )
            )

            @dataclass
            class LocationForcing:
                """
                :ivar airport_city_qualifier:
                :ivar segment_number:
                """
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="airportCityQualifier",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=1.0
                    )
                )
                segment_number: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="segmentNumber",
                        type="Element",
                        required=True
                    )
                )

        @dataclass
        class DepartureLocalization:
            """
            :ivar departure_point:
            :ivar dep_multi_city:
            :ivar first_pnr_segment_ref:
            :ivar attribute_details:
            """
            departure_point: Optional["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.DeparturePoint"] = field(
                default=None,
                metadata=dict(
                    name="departurePoint",
                    type="Element"
                )
            )
            dep_multi_city: List["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.DepMultiCity"] = field(
                default_factory=list,
                metadata=dict(
                    name="depMultiCity",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            first_pnr_segment_ref: Optional["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.FirstPnrSegmentRef"] = field(
                default=None,
                metadata=dict(
                    name="firstPnrSegmentRef",
                    type="Element"
                )
            )
            attribute_details: List["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.AttributeDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="attributeDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )

            @dataclass
            class DeparturePoint:
                """
                :ivar distance:
                :ivar distance_unit:
                :ivar location_id:
                :ivar airport_city_qualifier:
                :ivar latitude:
                :ivar longitude:
                """
                distance: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="distance",
                        type="Element"
                    )
                )
                distance_unit: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="distanceUnit",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="airportCityQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )
                latitude: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="latitude",
                        type="Element",
                        min_length=6.0,
                        max_length=6.0
                    )
                )
                longitude: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="longitude",
                        type="Element",
                        min_length=6.0,
                        max_length=6.0
                    )
                )

            @dataclass
            class DepMultiCity:
                """
                :ivar location_id:
                :ivar airport_city_qualifier:
                """
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="airportCityQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class FirstPnrSegmentRef:
                """
                :ivar pnr_segment_tattoo:
                :ivar pnr_segment_qualifier:
                """
                pnr_segment_tattoo: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="pnrSegmentTattoo",
                        type="Element"
                    )
                )
                pnr_segment_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="pnrSegmentQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class AttributeDetails:
                """
                :ivar type:
                :ivar value:
                """
                type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="type",
                        type="Element",
                        min_length=1.0,
                        max_length=5.0
                    )
                )
                value: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="value",
                        type="Element",
                        min_occurs=0,
                        max_occurs=10,
                        min_length=1.0,
                        max_length=20.0
                    )
                )

        @dataclass
        class ArrivalLocalization:
            """
            :ivar arrival_point_details:
            :ivar arrival_multi_city:
            :ivar attribute_details:
            """
            arrival_point_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization.ArrivalPointDetails"] = field(
                default=None,
                metadata=dict(
                    name="arrivalPointDetails",
                    type="Element"
                )
            )
            arrival_multi_city: List["FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization.ArrivalMultiCity"] = field(
                default_factory=list,
                metadata=dict(
                    name="arrivalMultiCity",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            attribute_details: List["FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization.AttributeDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="attributeDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )

            @dataclass
            class ArrivalPointDetails:
                """
                :ivar distance:
                :ivar distance_unit:
                :ivar location_id:
                :ivar airport_city_qualifier:
                :ivar latitude:
                :ivar longitude:
                """
                distance: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="distance",
                        type="Element"
                    )
                )
                distance_unit: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="distanceUnit",
                        type="Element",
                        min_length=0.0,
                        max_length=3.0
                    )
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="airportCityQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )
                latitude: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="latitude",
                        type="Element",
                        min_length=6.0,
                        max_length=6.0
                    )
                )
                longitude: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="longitude",
                        type="Element",
                        min_length=6.0,
                        max_length=6.0
                    )
                )

            @dataclass
            class ArrivalMultiCity:
                """
                :ivar location_id:
                :ivar airport_city_qualifier:
                """
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="airportCityQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class AttributeDetails:
                """
                :ivar type:
                :ivar value:
                """
                type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="type",
                        type="Element",
                        min_length=1.0,
                        max_length=5.0
                    )
                )
                value: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="value",
                        type="Element",
                        min_occurs=0,
                        max_occurs=10,
                        min_length=1.0,
                        max_length=20.0
                    )
                )

        @dataclass
        class TimeDetails:
            """
            :ivar first_date_time_detail:
            :ivar range_of_date:
            :ivar trip_details:
            """
            first_date_time_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails.FirstDateTimeDetail"] = field(
                default=None,
                metadata=dict(
                    name="firstDateTimeDetail",
                    type="Element",
                    required=True
                )
            )
            range_of_date: Optional["FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails.RangeOfDate"] = field(
                default=None,
                metadata=dict(
                    name="rangeOfDate",
                    type="Element"
                )
            )
            trip_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails.TripDetails"] = field(
                default=None,
                metadata=dict(
                    name="tripDetails",
                    type="Element"
                )
            )

            @dataclass
            class FirstDateTimeDetail:
                """
                :ivar time_qualifier:
                :ivar date:
                :ivar time:
                :ivar time_window:
                """
                time_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="timeQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                date: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="date",
                        type="Element",
                        min_length=6.0,
                        max_length=6.0
                    )
                )
                time: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="time",
                        type="Element",
                        min_length=4.0,
                        max_length=4.0
                    )
                )
                time_window: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="timeWindow",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class RangeOfDate:
                """
                :ivar range_qualifier:
                :ivar day_interval:
                :ivar time_atdestination:
                """
                range_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="rangeQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                day_interval: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="dayInterval",
                        type="Element"
                    )
                )
                time_atdestination: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="timeAtdestination",
                        type="Element",
                        min_length=4.0,
                        max_length=4.0
                    )
                )

            @dataclass
            class TripDetails:
                """
                :ivar flexibility_qualifier:
                :ivar trip_interval:
                :ivar trip_duration:
                """
                flexibility_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="flexibilityQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                trip_interval: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="tripInterval",
                        type="Element"
                    )
                )
                trip_duration: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="tripDuration",
                        type="Element"
                    )
                )

        @dataclass
        class FlightInfo:
            """
            :ivar cabin_id:
            :ivar company_identity:
            :ivar flight_detail:
            :ivar inclusion_detail:
            :ivar exclusion_detail:
            :ivar unit_number_detail:
            """
            cabin_id: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.CabinId"] = field(
                default=None,
                metadata=dict(
                    name="cabinId",
                    type="Element"
                )
            )
            company_identity: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.CompanyIdentity"] = field(
                default_factory=list,
                metadata=dict(
                    name="companyIdentity",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            flight_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.FlightDetail"] = field(
                default=None,
                metadata=dict(
                    name="flightDetail",
                    type="Element"
                )
            )
            inclusion_detail: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.InclusionDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="inclusionDetail",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            exclusion_detail: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.ExclusionDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="exclusionDetail",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            unit_number_detail: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.UnitNumberDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="unitNumberDetail",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )

            @dataclass
            class CabinId:
                """
                :ivar cabin_qualifier:
                :ivar cabin:
                """
                cabin_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="cabinQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=2.0
                    )
                )
                cabin: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="cabin",
                        type="Element",
                        min_occurs=0,
                        max_occurs=5,
                        min_length=0.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class CompanyIdentity:
                """
                :ivar carrier_qualifier:
                :ivar carrier_id:
                """
                carrier_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="carrierQualifier",
                        type="Element",
                        required=True,
                        min_length=0.0,
                        max_length=1.0
                    )
                )
                carrier_id: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="carrierId",
                        type="Element",
                        min_occurs=1,
                        max_occurs=99,
                        min_length=2.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class FlightDetail:
                """
                :ivar flight_type:
                """
                flight_type: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="flightType",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9,
                        min_length=1.0,
                        max_length=2.0
                    )
                )

            @dataclass
            class InclusionDetail:
                """
                :ivar inclusion_identifier:
                :ivar location_id:
                :ivar airport_city_qualifier:
                """
                inclusion_identifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="inclusionIdentifier",
                        type="Element",
                        required=True,
                        min_length=0.0,
                        max_length=1.0
                    )
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="airportCityQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class ExclusionDetail:
                """
                :ivar exclusion_identifier:
                :ivar location_id:
                :ivar airport_city_qualifier:
                """
                exclusion_identifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="exclusionIdentifier",
                        type="Element",
                        required=True,
                        min_length=0.0,
                        max_length=1.0
                    )
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="airportCityQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class UnitNumberDetail:
                """
                :ivar number_of_units:
                :ivar type_of_unit:
                """
                number_of_units: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="numberOfUnits",
                        type="Element",
                        required=True
                    )
                )
                type_of_unit: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="typeOfUnit",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )

        @dataclass
        class FamilyInformation:
            """
            :ivar commercial_family_details:
            """
            commercial_family_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FamilyInformation.CommercialFamilyDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="commercialFamilyDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )

            @dataclass
            class CommercialFamilyDetails:
                """
                :ivar commercial_family:
                """
                commercial_family: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="commercialFamily",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=10.0
                    )
                )

        @dataclass
        class ValueSearch:
            """
            :ivar criteria_name:
            :ivar criteria_code:
            :ivar value:
            :ivar criteria_details:
            """
            criteria_name: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="criteriaName",
                    type="Element",
                    min_length=1.0,
                    max_length=50.0
                )
            )
            criteria_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="criteriaCode",
                    type="Element",
                    min_length=1.0,
                    max_length=3.0
                )
            )
            value: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="value",
                    type="Element",
                    min_length=1.0,
                    max_length=18.0
                )
            )
            criteria_details: List["FareMasterPricerTravelBoardSearch.Itinerary.ValueSearch.CriteriaDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="criteriaDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=10
                )
            )

            @dataclass
            class CriteriaDetails:
                """
                :ivar type:
                :ivar value:
                :ivar attribute:
                """
                type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="type",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                value: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="value",
                        type="Element",
                        min_length=1.0,
                        max_length=18.0
                    )
                )
                attribute: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="attribute",
                        type="Element",
                        min_occurs=0,
                        max_occurs=99,
                        min_length=1.0,
                        max_length=9.0
                    )
                )

        @dataclass
        class GroupOfFlights:
            """
            :ivar prop_flight_gr_detail:
            :ivar price_to_beat:
            :ivar flight_details:
            """
            prop_flight_gr_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PropFlightGrDetail"] = field(
                default=None,
                metadata=dict(
                    name="propFlightGrDetail",
                    type="Element",
                    required=True
                )
            )
            price_to_beat: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PriceToBeat"] = field(
                default=None,
                metadata=dict(
                    name="priceToBeat",
                    type="Element"
                )
            )
            flight_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="flightDetails",
                    type="Element",
                    min_occurs=1,
                    max_occurs=4
                )
            )

            @dataclass
            class PropFlightGrDetail:
                """
                :ivar flight_proposal:
                :ivar flight_characteristic:
                :ivar maj_cabin:
                """
                flight_proposal: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PropFlightGrDetail.FlightProposal"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="flightProposal",
                        type="Element",
                        min_occurs=1,
                        max_occurs=9
                    )
                )
                flight_characteristic: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="flightCharacteristic",
                        type="Element",
                        min_length=0.0,
                        max_length=3.0
                    )
                )
                maj_cabin: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="majCabin",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )

                @dataclass
                class FlightProposal:
                    """
                    :ivar ref:
                    :ivar unit_qualifier:
                    """
                    ref: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="ref",
                            type="Element",
                            min_length=1.0,
                            max_length=6.0
                        )
                    )
                    unit_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="unitQualifier",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

            @dataclass
            class PriceToBeat:
                """
                :ivar money_info:
                :ivar additional_money_info:
                """
                money_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PriceToBeat.MoneyInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="moneyInfo",
                        type="Element",
                        required=True
                    )
                )
                additional_money_info: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PriceToBeat.AdditionalMoneyInfo"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="additionalMoneyInfo",
                        type="Element",
                        min_occurs=0,
                        max_occurs=19
                    )
                )

                @dataclass
                class MoneyInfo:
                    """
                    :ivar qualifier:
                    :ivar amount:
                    :ivar currency:
                    """
                    qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="qualifier",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    amount: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="amount",
                            type="Element",
                            required=True
                        )
                    )
                    currency: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="currency",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class AdditionalMoneyInfo:
                    """
                    :ivar qualifier:
                    :ivar amount:
                    :ivar currency:
                    :ivar location_id:
                    """
                    qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="qualifier",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    amount: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="amount",
                            type="Element",
                            required=True
                        )
                    )
                    currency: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="currency",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    location_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="locationId",
                            type="Element",
                            min_length=3.0,
                            max_length=3.0
                        )
                    )

            @dataclass
            class FlightDetails:
                """
                :ivar flight_information:
                :ivar avl_info:
                :ivar technical_stop:
                :ivar commercial_agreement:
                :ivar add_info:
                :ivar terminal_equipment_details:
                :ivar reservation_info:
                :ivar price_to_beat:
                """
                flight_information: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation"] = field(
                    default=None,
                    metadata=dict(
                        name="flightInformation",
                        type="Element",
                        required=True
                    )
                )
                avl_info: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AvlInfo"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="avlInfo",
                        type="Element",
                        min_occurs=0,
                        max_occurs=6
                    )
                )
                technical_stop: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TechnicalStop"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="technicalStop",
                        type="Element",
                        min_occurs=0,
                        max_occurs=5
                    )
                )
                commercial_agreement: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.CommercialAgreement"] = field(
                    default=None,
                    metadata=dict(
                        name="commercialAgreement",
                        type="Element"
                    )
                )
                add_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AddInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="addInfo",
                        type="Element"
                    )
                )
                terminal_equipment_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="terminalEquipmentDetails",
                        type="Element",
                        min_occurs=0,
                        max_occurs=2
                    )
                )
                reservation_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.ReservationInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="reservationInfo",
                        type="Element"
                    )
                )
                price_to_beat: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.PriceToBeat"] = field(
                    default=None,
                    metadata=dict(
                        name="priceToBeat",
                        type="Element"
                    )
                )

                @dataclass
                class FlightInformation:
                    """
                    :ivar product_date_time:
                    :ivar location:
                    :ivar company_id:
                    :ivar flight_ortrain_number:
                    :ivar product_detail:
                    :ivar add_product_detail:
                    :ivar attribute_details:
                    """
                    product_date_time: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.ProductDateTime"] = field(
                        default=None,
                        metadata=dict(
                            name="productDateTime",
                            type="Element",
                            required=True
                        )
                    )
                    location: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.Location"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="location",
                            type="Element",
                            min_occurs=1,
                            max_occurs=2
                        )
                    )
                    company_id: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.CompanyId"] = field(
                        default=None,
                        metadata=dict(
                            name="companyId",
                            type="Element"
                        )
                    )
                    flight_ortrain_number: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="flightOrtrainNumber",
                            type="Element",
                            min_length=1.0,
                            max_length=8.0
                        )
                    )
                    product_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.ProductDetail"] = field(
                        default=None,
                        metadata=dict(
                            name="productDetail",
                            type="Element"
                        )
                    )
                    add_product_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.AddProductDetail"] = field(
                        default=None,
                        metadata=dict(
                            name="addProductDetail",
                            type="Element"
                        )
                    )
                    attribute_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.AttributeDetails"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="attributeDetails",
                            type="Element",
                            min_occurs=0,
                            max_occurs=20
                        )
                    )

                    @dataclass
                    class ProductDateTime:
                        """
                        :ivar date_of_departure:
                        :ivar time_of_departure:
                        :ivar date_of_arrival:
                        :ivar time_of_arrival:
                        :ivar date_variation:
                        """
                        date_of_departure: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="dateOfDeparture",
                                type="Element",
                                required=True,
                                min_length=6.0,
                                max_length=6.0
                            )
                        )
                        time_of_departure: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="timeOfDeparture",
                                type="Element",
                                min_length=4.0,
                                max_length=4.0
                            )
                        )
                        date_of_arrival: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="dateOfArrival",
                                type="Element",
                                min_length=6.0,
                                max_length=6.0
                            )
                        )
                        time_of_arrival: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="timeOfArrival",
                                type="Element",
                                min_length=4.0,
                                max_length=4.0
                            )
                        )
                        date_variation: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="dateVariation",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )

                    @dataclass
                    class Location:
                        """
                        :ivar location_id:
                        :ivar airport_city_qualifier:
                        :ivar terminal:
                        """
                        location_id: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="locationId",
                                type="Element",
                                required=True,
                                min_length=3.0,
                                max_length=5.0
                            )
                        )
                        airport_city_qualifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="airportCityQualifier",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )
                        terminal: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="terminal",
                                type="Element",
                                min_length=1.0,
                                max_length=5.0
                            )
                        )

                    @dataclass
                    class CompanyId:
                        """
                        :ivar marketing_carrier:
                        :ivar operating_carrier:
                        """
                        marketing_carrier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="marketingCarrier",
                                type="Element",
                                required=True,
                                min_length=2.0,
                                max_length=3.0
                            )
                        )
                        operating_carrier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="operatingCarrier",
                                type="Element",
                                min_length=2.0,
                                max_length=3.0
                            )
                        )

                    @dataclass
                    class ProductDetail:
                        """
                        :ivar equipment_type:
                        :ivar operating_day:
                        :ivar tech_stop_number:
                        :ivar location_id:
                        """
                        equipment_type: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="equipmentType",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        operating_day: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="operatingDay",
                                type="Element",
                                min_length=1.0,
                                max_length=7.0
                            )
                        )
                        tech_stop_number: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="techStopNumber",
                                type="Element"
                            )
                        )
                        location_id: List[str] = field(
                            default_factory=list,
                            metadata=dict(
                                name="locationId",
                                type="Element",
                                min_occurs=0,
                                max_occurs=3,
                                min_length=3.0,
                                max_length=5.0
                            )
                        )

                    @dataclass
                    class AddProductDetail:
                        """
                        :ivar last_seat_available:
                        :ivar level_of_access:
                        :ivar electronic_ticketing:
                        :ivar operational_suffix:
                        :ivar product_detail_qualifier:
                        :ivar flight_characteristic:
                        """
                        last_seat_available: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="lastSeatAvailable",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )
                        level_of_access: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="levelOfAccess",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        electronic_ticketing: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="electronicTicketing",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )
                        operational_suffix: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="operationalSuffix",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )
                        product_detail_qualifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="productDetailQualifier",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        flight_characteristic: List[str] = field(
                            default_factory=list,
                            metadata=dict(
                                name="flightCharacteristic",
                                type="Element",
                                min_occurs=0,
                                max_occurs=9,
                                min_length=1.0,
                                max_length=3.0
                            )
                        )

                    @dataclass
                    class AttributeDetails:
                        """
                        :ivar attribute_type:
                        :ivar attribute_description:
                        """
                        attribute_type: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="attributeType",
                                type="Element",
                                required=True,
                                min_length=1.0,
                                max_length=5.0
                            )
                        )
                        attribute_description: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="attributeDescription",
                                type="Element",
                                min_length=1.0,
                                max_length=10.0
                            )
                        )

                @dataclass
                class AvlInfo:
                    """
                    :ivar cabin_product:
                    :ivar context_details:
                    """
                    cabin_product: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AvlInfo.CabinProduct"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="cabinProduct",
                            type="Element",
                            min_occurs=0,
                            max_occurs=26
                        )
                    )
                    context_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AvlInfo.ContextDetails"] = field(
                        default=None,
                        metadata=dict(
                            name="contextDetails",
                            type="Element"
                        )
                    )

                    @dataclass
                    class CabinProduct:
                        """
                        :ivar rbd:
                        :ivar booking_modifier:
                        :ivar cabin:
                        :ivar avl_status:
                        """
                        rbd: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="rbd",
                                type="Element",
                                required=True,
                                min_length=1.0,
                                max_length=1.0
                            )
                        )
                        booking_modifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="bookingModifier",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )
                        cabin: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="cabin",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )
                        avl_status: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="avlStatus",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )

                    @dataclass
                    class ContextDetails:
                        """
                        :ivar avl:
                        """
                        avl: List[str] = field(
                            default_factory=list,
                            metadata=dict(
                                name="avl",
                                type="Element",
                                min_occurs=1,
                                max_occurs=9,
                                min_length=1.0,
                                max_length=6.0
                            )
                        )

                @dataclass
                class TechnicalStop:
                    """
                    :ivar stop_details:
                    :ivar dummy_net:
                    """
                    stop_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TechnicalStop.StopDetails"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="stopDetails",
                            type="Element",
                            min_occurs=1,
                            max_occurs=2
                        )
                    )
                    dummy_net: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="Dummy.NET",
                            type="Element"
                        )
                    )

                    @dataclass
                    class StopDetails:
                        """
                        :ivar date_qualifier:
                        :ivar date:
                        :ivar first_time:
                        :ivar equipement_type:
                        :ivar location_id:
                        """
                        date_qualifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="dateQualifier",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        date: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="date",
                                type="Element",
                                min_length=6.0,
                                max_length=6.0
                            )
                        )
                        first_time: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="firstTime",
                                type="Element",
                                min_length=4.0,
                                max_length=4.0
                            )
                        )
                        equipement_type: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="equipementType",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        location_id: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="locationId",
                                type="Element",
                                min_length=3.0,
                                max_length=5.0
                            )
                        )

                @dataclass
                class CommercialAgreement:
                    """
                    :ivar codeshare_details:
                    :ivar other_codeshare_details:
                    """
                    codeshare_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.CommercialAgreement.CodeshareDetails"] = field(
                        default=None,
                        metadata=dict(
                            name="codeshareDetails",
                            type="Element"
                        )
                    )
                    other_codeshare_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.CommercialAgreement.OtherCodeshareDetails"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="otherCodeshareDetails",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9
                        )
                    )

                    @dataclass
                    class CodeshareDetails:
                        """
                        :ivar code_share_type:
                        :ivar airline_designator:
                        :ivar flight_number:
                        """
                        code_share_type: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="codeShareType",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )
                        airline_designator: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="airlineDesignator",
                                type="Element",
                                min_length=2.0,
                                max_length=3.0
                            )
                        )
                        flight_number: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="flightNumber",
                                type="Element"
                            )
                        )

                    @dataclass
                    class OtherCodeshareDetails:
                        """
                        :ivar code_share_type:
                        :ivar airline_designator:
                        :ivar flight_number:
                        """
                        code_share_type: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="codeShareType",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )
                        airline_designator: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="airlineDesignator",
                                type="Element",
                                min_length=2.0,
                                max_length=3.0
                            )
                        )
                        flight_number: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="flightNumber",
                                type="Element"
                            )
                        )

                @dataclass
                class AddInfo:
                    """
                    :ivar status:
                    :ivar date_time_period_details:
                    :ivar reference_number:
                    :ivar product_identification:
                    """
                    status: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="status",
                            type="Element",
                            min_occurs=0,
                            max_occurs=2,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    date_time_period_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AddInfo.DateTimePeriodDetails"] = field(
                        default=None,
                        metadata=dict(
                            name="dateTimePeriodDetails",
                            type="Element"
                        )
                    )
                    reference_number: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="referenceNumber",
                            type="Element",
                            min_length=1.0,
                            max_length=35.0
                        )
                    )
                    product_identification: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="productIdentification",
                            type="Element",
                            min_occurs=0,
                            max_occurs=2,
                            min_length=1.0,
                            max_length=35.0
                        )
                    )

                    @dataclass
                    class DateTimePeriodDetails:
                        """
                        :ivar qualifier:
                        :ivar value:
                        """
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="qualifier",
                                type="Element",
                                required=True,
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        value: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="value",
                                type="Element",
                                min_length=1.0,
                                max_length=35.0
                            )
                        )

                @dataclass
                class TerminalEquipmentDetails:
                    """
                    :ivar leg_details:
                    :ivar departure_station_info:
                    :ivar arrival_station_info:
                    :ivar mileage_time_details:
                    """
                    leg_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.LegDetails"] = field(
                        default=None,
                        metadata=dict(
                            name="legDetails",
                            type="Element"
                        )
                    )
                    departure_station_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.DepartureStationInfo"] = field(
                        default=None,
                        metadata=dict(
                            name="departureStationInfo",
                            type="Element"
                        )
                    )
                    arrival_station_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.ArrivalStationInfo"] = field(
                        default=None,
                        metadata=dict(
                            name="arrivalStationInfo",
                            type="Element"
                        )
                    )
                    mileage_time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.MileageTimeDetails"] = field(
                        default=None,
                        metadata=dict(
                            name="mileageTimeDetails",
                            type="Element"
                        )
                    )

                    @dataclass
                    class LegDetails:
                        """
                        :ivar equipment:
                        :ivar duration:
                        :ivar complexing_flight_indicator:
                        """
                        equipment: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="equipment",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        duration: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="duration",
                                type="Element"
                            )
                        )
                        complexing_flight_indicator: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="complexingFlightIndicator",
                                type="Element",
                                min_length=1.0,
                                max_length=1.0
                            )
                        )

                    @dataclass
                    class DepartureStationInfo:
                        """
                        :ivar terminal:
                        """
                        terminal: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="terminal",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )

                    @dataclass
                    class ArrivalStationInfo:
                        """
                        :ivar terminal:
                        """
                        terminal: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="terminal",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )

                    @dataclass
                    class MileageTimeDetails:
                        """
                        :ivar elapsed_ground_time:
                        """
                        elapsed_ground_time: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="elapsedGroundTime",
                                type="Element"
                            )
                        )

                @dataclass
                class ReservationInfo:
                    """
                    :ivar booking:
                    :ivar identifier:
                    :ivar status:
                    :ivar item_number:
                    :ivar date_time_details:
                    :ivar designator:
                    :ivar movement_type:
                    :ivar product_type_details:
                    """
                    booking: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="booking",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )
                    identifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="identifier",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )
                    status: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="status",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    item_number: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="itemNumber",
                            type="Element"
                        )
                    )
                    date_time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.ReservationInfo.DateTimeDetails"] = field(
                        default=None,
                        metadata=dict(
                            name="dateTimeDetails",
                            type="Element"
                        )
                    )
                    designator: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="designator",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )
                    movement_type: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="movementType",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    product_type_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.ReservationInfo.ProductTypeDetails"] = field(
                        default=None,
                        metadata=dict(
                            name="productTypeDetails",
                            type="Element"
                        )
                    )

                    @dataclass
                    class DateTimeDetails:
                        """
                        :ivar date:
                        :ivar time:
                        """
                        date: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="date",
                                type="Element",
                                required=True,
                                min_length=6.0,
                                max_length=6.0
                            )
                        )
                        time: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="time",
                                type="Element",
                                min_length=4.0,
                                max_length=4.0
                            )
                        )

                    @dataclass
                    class ProductTypeDetails:
                        """
                        :ivar sequence_number:
                        :ivar availability_context:
                        """
                        sequence_number: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="sequenceNumber",
                                type="Element",
                                min_length=1.0,
                                max_length=6.0
                            )
                        )
                        availability_context: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="availabilityContext",
                                type="Element",
                                min_length=1.0,
                                max_length=6.0
                            )
                        )

                @dataclass
                class PriceToBeat:
                    """
                    :ivar money_info:
                    :ivar additional_money_info:
                    """
                    money_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.PriceToBeat.MoneyInfo"] = field(
                        default=None,
                        metadata=dict(
                            name="moneyInfo",
                            type="Element",
                            required=True
                        )
                    )
                    additional_money_info: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.PriceToBeat.AdditionalMoneyInfo"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="additionalMoneyInfo",
                            type="Element",
                            min_occurs=0,
                            max_occurs=19
                        )
                    )

                    @dataclass
                    class MoneyInfo:
                        """
                        :ivar qualifier:
                        :ivar amount:
                        :ivar currency:
                        """
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="qualifier",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        amount: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="amount",
                                type="Element",
                                required=True
                            )
                        )
                        currency: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="currency",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )

                    @dataclass
                    class AdditionalMoneyInfo:
                        """
                        :ivar qualifier:
                        :ivar amount:
                        :ivar currency:
                        :ivar location_id:
                        """
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="qualifier",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        amount: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="amount",
                                type="Element",
                                required=True
                            )
                        )
                        currency: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="currency",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        location_id: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="locationId",
                                type="Element",
                                min_length=3.0,
                                max_length=3.0
                            )
                        )

        @dataclass
        class FlightInfoPnr:
            """
            :ivar travel_response_details:
            :ivar time_table_date:
            :ivar terminal_equipment_details:
            :ivar codeshare_data:
            :ivar disclosure:
            :ivar stop_details:
            :ivar traffic_restriction_data:
            :ivar reservation_info:
            :ivar incidental_stop_info:
            """
            travel_response_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails"] = field(
                default=None,
                metadata=dict(
                    name="travelResponseDetails",
                    type="Element",
                    required=True
                )
            )
            time_table_date: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate"] = field(
                default=None,
                metadata=dict(
                    name="timeTableDate",
                    type="Element"
                )
            )
            terminal_equipment_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="terminalEquipmentDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=2
                )
            )
            codeshare_data: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.CodeshareData"] = field(
                default=None,
                metadata=dict(
                    name="codeshareData",
                    type="Element"
                )
            )
            disclosure: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.Disclosure"] = field(
                default=None,
                metadata=dict(
                    name="disclosure",
                    type="Element"
                )
            )
            stop_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.StopDetails"] = field(
                default=None,
                metadata=dict(
                    name="stopDetails",
                    type="Element"
                )
            )
            traffic_restriction_data: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TrafficRestrictionData"] = field(
                default=None,
                metadata=dict(
                    name="trafficRestrictionData",
                    type="Element"
                )
            )
            reservation_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.ReservationInfo"] = field(
                default=None,
                metadata=dict(
                    name="reservationInfo",
                    type="Element"
                )
            )
            incidental_stop_info: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo"] = field(
                default_factory=list,
                metadata=dict(
                    name="incidentalStopInfo",
                    type="Element",
                    min_occurs=0,
                    max_occurs=8
                )
            )

            @dataclass
            class TravelResponseDetails:
                """
                :ivar flight_date:
                :ivar board_point_details:
                :ivar offpoint_details:
                :ivar company_details:
                :ivar flight_identification:
                :ivar flight_type_details:
                """
                flight_date: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.FlightDate"] = field(
                    default=None,
                    metadata=dict(
                        name="flightDate",
                        type="Element"
                    )
                )
                board_point_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.BoardPointDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="boardPointDetails",
                        type="Element",
                        required=True
                    )
                )
                offpoint_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.OffpointDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="offpointDetails",
                        type="Element",
                        required=True
                    )
                )
                company_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.CompanyDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="companyDetails",
                        type="Element",
                        required=True
                    )
                )
                flight_identification: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.FlightIdentification"] = field(
                    default=None,
                    metadata=dict(
                        name="flightIdentification",
                        type="Element"
                    )
                )
                flight_type_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.FlightTypeDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="flightTypeDetails",
                        type="Element"
                    )
                )

                @dataclass
                class FlightDate:
                    """
                    :ivar departure_date:
                    :ivar departure_time:
                    :ivar arrival_date:
                    :ivar arrival_time:
                    :ivar date_variation:
                    """
                    departure_date: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="departureDate",
                            type="Element",
                            min_length=8.0,
                            max_length=8.0
                        )
                    )
                    departure_time: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="departureTime",
                            type="Element",
                            min_length=4.0,
                            max_length=4.0
                        )
                    )
                    arrival_date: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="arrivalDate",
                            type="Element",
                            min_length=8.0,
                            max_length=8.0
                        )
                    )
                    arrival_time: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="arrivalTime",
                            type="Element",
                            min_length=4.0,
                            max_length=4.0
                        )
                    )
                    date_variation: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="dateVariation",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

                @dataclass
                class BoardPointDetails:
                    """
                    :ivar true_location_id:
                    """
                    true_location_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="trueLocationId",
                            type="Element",
                            required=True,
                            min_length=3.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class OffpointDetails:
                    """
                    :ivar true_location_id:
                    """
                    true_location_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="trueLocationId",
                            type="Element",
                            required=True,
                            min_length=3.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class CompanyDetails:
                    """
                    :ivar marketing_company:
                    """
                    marketing_company: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="marketingCompany",
                            type="Element",
                            required=True,
                            min_length=2.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class FlightIdentification:
                    """
                    :ivar flight_number:
                    :ivar operational_suffix:
                    """
                    flight_number: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="flightNumber",
                            type="Element",
                            required=True
                        )
                    )
                    operational_suffix: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="operationalSuffix",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

                @dataclass
                class FlightTypeDetails:
                    """
                    :ivar flight_indicator:
                    """
                    flight_indicator: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="flightIndicator",
                            type="Element",
                            min_occurs=1,
                            max_occurs=5,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

            @dataclass
            class TimeTableDate:
                """
                :ivar begin_date_time:
                :ivar end_date_time:
                :ivar frequency:
                """
                begin_date_time: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate.BeginDateTime"] = field(
                    default=None,
                    metadata=dict(
                        name="beginDateTime",
                        type="Element"
                    )
                )
                end_date_time: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate.EndDateTime"] = field(
                    default=None,
                    metadata=dict(
                        name="endDateTime",
                        type="Element"
                    )
                )
                frequency: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate.Frequency"] = field(
                    default=None,
                    metadata=dict(
                        name="frequency",
                        type="Element"
                    )
                )

                @dataclass
                class BeginDateTime:
                    """
                    :ivar year:
                    :ivar month:
                    :ivar day:
                    """
                    year: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="year",
                            type="Element",
                            min_length=4.0,
                            max_length=4.0
                        )
                    )
                    month: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="month",
                            type="Element"
                        )
                    )
                    day: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="day",
                            type="Element"
                        )
                    )

                @dataclass
                class EndDateTime:
                    """
                    :ivar year:
                    :ivar month:
                    :ivar day:
                    """
                    year: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="year",
                            type="Element",
                            min_length=4.0,
                            max_length=4.0
                        )
                    )
                    month: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="month",
                            type="Element"
                        )
                    )
                    day: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="day",
                            type="Element"
                        )
                    )

                @dataclass
                class Frequency:
                    """
                    :ivar qualifier:
                    :ivar value:
                    """
                    qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="qualifier",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    value: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="value",
                            type="Element",
                            min_occurs=0,
                            max_occurs=7,
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

            @dataclass
            class TerminalEquipmentDetails:
                """
                :ivar leg_details:
                :ivar departure_station_info:
                :ivar arrival_station_info:
                :ivar mileage_time_details:
                """
                leg_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.LegDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="legDetails",
                        type="Element"
                    )
                )
                departure_station_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.DepartureStationInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="departureStationInfo",
                        type="Element"
                    )
                )
                arrival_station_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.ArrivalStationInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="arrivalStationInfo",
                        type="Element"
                    )
                )
                mileage_time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.MileageTimeDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="mileageTimeDetails",
                        type="Element"
                    )
                )

                @dataclass
                class LegDetails:
                    """
                    :ivar equipment:
                    :ivar duration:
                    :ivar complexing_flight_indicator:
                    """
                    equipment: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="equipment",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    duration: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="duration",
                            type="Element"
                        )
                    )
                    complexing_flight_indicator: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="complexingFlightIndicator",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

                @dataclass
                class DepartureStationInfo:
                    """
                    :ivar terminal:
                    """
                    terminal: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="terminal",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class ArrivalStationInfo:
                    """
                    :ivar terminal:
                    """
                    terminal: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="terminal",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class MileageTimeDetails:
                    """
                    :ivar elapsed_ground_time:
                    """
                    elapsed_ground_time: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="elapsedGroundTime",
                            type="Element"
                        )
                    )

            @dataclass
            class CodeshareData:
                """
                :ivar codeshare_details:
                :ivar other_codeshare_details:
                """
                codeshare_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.CodeshareData.CodeshareDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="codeshareDetails",
                        type="Element",
                        required=True
                    )
                )
                other_codeshare_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.CodeshareData.OtherCodeshareDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="otherCodeshareDetails",
                        type="Element",
                        min_occurs=0,
                        max_occurs=8
                    )
                )

                @dataclass
                class CodeshareDetails:
                    """
                    :ivar transport_stage_qualifier:
                    :ivar airline_designator:
                    :ivar flight_number:
                    :ivar operational_suffix:
                    """
                    transport_stage_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="transportStageQualifier",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=1.0
                        )
                    )
                    airline_designator: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="airlineDesignator",
                            type="Element",
                            min_length=2.0,
                            max_length=3.0
                        )
                    )
                    flight_number: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="flightNumber",
                            type="Element"
                        )
                    )
                    operational_suffix: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="operationalSuffix",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

                @dataclass
                class OtherCodeshareDetails:
                    """
                    :ivar transport_stage_qualifier:
                    :ivar airline_designator:
                    :ivar flight_number:
                    :ivar operational_suffix:
                    """
                    transport_stage_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="transportStageQualifier",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=1.0
                        )
                    )
                    airline_designator: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="airlineDesignator",
                            type="Element",
                            min_length=2.0,
                            max_length=3.0
                        )
                    )
                    flight_number: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="flightNumber",
                            type="Element"
                        )
                    )
                    operational_suffix: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="operationalSuffix",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

            @dataclass
            class Disclosure:
                """
                :ivar free_text_details:
                :ivar free_text:
                """
                free_text_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.Disclosure.FreeTextDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="freeTextDetails",
                        type="Element",
                        required=True
                    )
                )
                free_text: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="freeText",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=70.0
                    )
                )

                @dataclass
                class FreeTextDetails:
                    """
                    :ivar text_subject_qualifier:
                    :ivar information_type:
                    :ivar source:
                    :ivar encoding:
                    """
                    text_subject_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="textSubjectQualifier",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    information_type: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="informationType",
                            type="Element",
                            min_length=1.0,
                            max_length=4.0
                        )
                    )
                    source: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="source",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    encoding: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="encoding",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

            @dataclass
            class StopDetails:
                """
                :ivar routing_details:
                """
                routing_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.StopDetails.RoutingDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="routingDetails",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9
                    )
                )

                @dataclass
                class RoutingDetails:
                    """
                    :ivar station:
                    """
                    station: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="station",
                            type="Element",
                            min_length=3.0,
                            max_length=3.0
                        )
                    )

            @dataclass
            class TrafficRestrictionData:
                """
                :ivar traffic_restriction_details:
                """
                traffic_restriction_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TrafficRestrictionData.TrafficRestrictionDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="trafficRestrictionDetails",
                        type="Element",
                        min_occurs=0,
                        max_occurs=5
                    )
                )

                @dataclass
                class TrafficRestrictionDetails:
                    """
                    :ivar code:
                    """
                    code: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="code",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

            @dataclass
            class ReservationInfo:
                """
                :ivar booking:
                :ivar identifier:
                :ivar status:
                :ivar item_number:
                :ivar date_time_details:
                :ivar designator:
                :ivar movement_type:
                :ivar product_type_details:
                """
                booking: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="booking",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )
                identifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="identifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )
                status: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="status",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                item_number: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="itemNumber",
                        type="Element"
                    )
                )
                date_time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.ReservationInfo.DateTimeDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="dateTimeDetails",
                        type="Element"
                    )
                )
                designator: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="designator",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )
                movement_type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="movementType",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                product_type_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.ReservationInfo.ProductTypeDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="productTypeDetails",
                        type="Element"
                    )
                )

                @dataclass
                class DateTimeDetails:
                    """
                    :ivar date:
                    :ivar time:
                    """
                    date: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="date",
                            type="Element",
                            required=True,
                            min_length=6.0,
                            max_length=6.0
                        )
                    )
                    time: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="time",
                            type="Element",
                            min_length=4.0,
                            max_length=4.0
                        )
                    )

                @dataclass
                class ProductTypeDetails:
                    """
                    :ivar sequence_number:
                    :ivar availability_context:
                    """
                    sequence_number: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="sequenceNumber",
                            type="Element",
                            min_length=1.0,
                            max_length=6.0
                        )
                    )
                    availability_context: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="availabilityContext",
                            type="Element",
                            min_length=1.0,
                            max_length=6.0
                        )
                    )

            @dataclass
            class IncidentalStopInfo:
                """
                :ivar date_time_info:
                """
                date_time_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo.DateTimeInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="dateTimeInfo",
                        type="Element",
                        required=True
                    )
                )

                @dataclass
                class DateTimeInfo:
                    """
                    :ivar date_time_details:
                    """
                    date_time_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo.DateTimeInfo.DateTimeDetails"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="dateTimeDetails",
                            type="Element",
                            min_occurs=0,
                            max_occurs=2
                        )
                    )

                    @dataclass
                    class DateTimeDetails:
                        """
                        :ivar qualifier:
                        :ivar date:
                        :ivar time:
                        :ivar qualifier2:
                        :ivar reserved1:
                        :ivar reserved2:
                        """
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="qualifier",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        date: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="date",
                                type="Element",
                                min_length=6.0,
                                max_length=6.0
                            )
                        )
                        time: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="time",
                                type="Element",
                                min_length=4.0,
                                max_length=4.0
                            )
                        )
                        qualifier2: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="qualifier2",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        reserved1: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="reserved1",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        reserved2: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="reserved2",
                                type="Element",
                                min_length=3.0,
                                max_length=5.0
                            )
                        )

        @dataclass
        class RequestedSegmentAction:
            """
            :ivar action_request_code:
            :ivar product_details:
            """
            action_request_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="actionRequestCode",
                    type="Element",
                    required=True,
                    min_length=1.0,
                    max_length=3.0
                )
            )
            product_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentAction.ProductDetails"] = field(
                default=None,
                metadata=dict(
                    name="productDetails",
                    type="Element"
                )
            )

            @dataclass
            class ProductDetails:
                """
                :ivar flight_number:
                :ivar booking_class:
                :ivar operational_suffix:
                :ivar modifier:
                """
                flight_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="flightNumber",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=5.0
                    )
                )
                booking_class: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="bookingClass",
                        type="Element",
                        min_length=1.0,
                        max_length=2.0
                    )
                )
                operational_suffix: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="operationalSuffix",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                modifier: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="modifier",
                        type="Element",
                        min_occurs=0,
                        max_occurs=3,
                        min_length=1.0,
                        max_length=7.0
                    )
                )

        @dataclass
        class Attributes:
            """
            :ivar attribute_details:
            """
            attribute_details: List["FareMasterPricerTravelBoardSearch.Itinerary.Attributes.AttributeDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="attributeDetails",
                    type="Element",
                    min_occurs=1,
                    max_occurs=9
                )
            )

            @dataclass
            class AttributeDetails:
                """
                :ivar attribute_type:
                :ivar attribute_description:
                """
                attribute_type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="attributeType",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=5.0
                    )
                )
                attribute_description: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="attributeDescription",
                        type="Element",
                        min_length=1.0,
                        max_length=50.0
                    )
                )

    @dataclass
    class TicketChangeInfo:
        """
        :ivar ticket_number_details:
        :ivar ticket_requested_segments:
        """
        ticket_number_details: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketNumberDetails"] = field(
            default=None,
            metadata=dict(
                name="ticketNumberDetails",
                type="Element",
                required=True
            )
        )
        ticket_requested_segments: List["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments"] = field(
            default_factory=list,
            metadata=dict(
                name="ticketRequestedSegments",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )

        @dataclass
        class TicketNumberDetails:
            """
            :ivar document_details:
            """
            document_details: List["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketNumberDetails.DocumentDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="documentDetails",
                    type="Element",
                    min_occurs=1,
                    max_occurs=99
                )
            )

            @dataclass
            class DocumentDetails:
                """
                :ivar number:
                """
                number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="number",
                        type="Element",
                        min_length=1.0,
                        max_length=35.0
                    )
                )

        @dataclass
        class TicketRequestedSegments:
            """
            :ivar action_identification:
            :ivar connect_point_details:
            """
            action_identification: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ActionIdentification"] = field(
                default=None,
                metadata=dict(
                    name="actionIdentification",
                    type="Element",
                    required=True
                )
            )
            connect_point_details: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ConnectPointDetails"] = field(
                default=None,
                metadata=dict(
                    name="connectPointDetails",
                    type="Element"
                )
            )

            @dataclass
            class ActionIdentification:
                """
                :ivar action_request_code:
                :ivar product_details:
                """
                action_request_code: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="actionRequestCode",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                product_details: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ActionIdentification.ProductDetails"] = field(
                    default=None,
                    metadata=dict(
                        name="productDetails",
                        type="Element"
                    )
                )

                @dataclass
                class ProductDetails:
                    """
                    :ivar flight_number:
                    :ivar booking_class:
                    :ivar operational_suffix:
                    :ivar modifier:
                    """
                    flight_number: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="flightNumber",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=5.0
                        )
                    )
                    booking_class: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="bookingClass",
                            type="Element",
                            min_length=1.0,
                            max_length=2.0
                        )
                    )
                    operational_suffix: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="operationalSuffix",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    modifier: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="modifier",
                            type="Element",
                            min_occurs=0,
                            max_occurs=3,
                            min_length=1.0,
                            max_length=7.0
                        )
                    )

            @dataclass
            class ConnectPointDetails:
                """
                :ivar connection_details:
                """
                connection_details: List["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ConnectPointDetails.ConnectionDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="connectionDetails",
                        type="Element",
                        min_occurs=1,
                        max_occurs=17
                    )
                )

                @dataclass
                class ConnectionDetails:
                    """
                    :ivar location:
                    """
                    location: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="location",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

    @dataclass
    class CombinationFareFamilies:
        """
        :ivar item_ffcnumber:
        :ivar nb_of_units:
        :ivar reference_info:
        """
        item_ffcnumber: Optional["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ItemFfcnumber"] = field(
            default=None,
            metadata=dict(
                name="itemFFCNumber",
                type="Element",
                required=True
            )
        )
        nb_of_units: Optional["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.NbOfUnits"] = field(
            default=None,
            metadata=dict(
                name="nbOfUnits",
                type="Element"
            )
        )
        reference_info: List["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ReferenceInfo"] = field(
            default_factory=list,
            metadata=dict(
                name="referenceInfo",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )

        @dataclass
        class ItemFfcnumber:
            """
            :ivar item_number_id:
            """
            item_number_id: Optional["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ItemFfcnumber.ItemNumberId"] = field(
                default=None,
                metadata=dict(
                    name="itemNumberId",
                    type="Element",
                    required=True
                )
            )

            @dataclass
            class ItemNumberId:
                """
                :ivar number:
                :ivar type:
                :ivar qualifier:
                :ivar responsible_agency:
                """
                number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="number",
                        type="Element",
                        min_length=1.0,
                        max_length=4.0
                    )
                )
                type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="type",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="qualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                responsible_agency: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="responsibleAgency",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

        @dataclass
        class NbOfUnits:
            """
            :ivar unit_number_detail:
            """
            unit_number_detail: List["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.NbOfUnits.UnitNumberDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="unitNumberDetail",
                    type="Element",
                    min_occurs=1,
                    max_occurs=20
                )
            )

            @dataclass
            class UnitNumberDetail:
                """
                :ivar number_of_units:
                :ivar type_of_unit:
                """
                number_of_units: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="numberOfUnits",
                        type="Element"
                    )
                )
                type_of_unit: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="typeOfUnit",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )

        @dataclass
        class ReferenceInfo:
            """
            :ivar referencing_detail:
            :ivar dummy_net:
            """
            referencing_detail: List["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ReferenceInfo.ReferencingDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="referencingDetail",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9
                )
            )
            dummy_net: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="Dummy.NET",
                    type="Element"
                )
            )

            @dataclass
            class ReferencingDetail:
                """
                :ivar ref_qualifier:
                :ivar ref_number:
                """
                ref_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="refQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                ref_number: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="refNumber",
                        type="Element",
                        required=True
                    )
                )

    @dataclass
    class FeeOption:
        """
        :ivar fee_type_info:
        :ivar rate_tax:
        :ivar fee_details:
        """
        fee_type_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeTypeInfo"] = field(
            default=None,
            metadata=dict(
                name="feeTypeInfo",
                type="Element",
                required=True
            )
        )
        rate_tax: Optional["FareMasterPricerTravelBoardSearch.FeeOption.RateTax"] = field(
            default=None,
            metadata=dict(
                name="rateTax",
                type="Element"
            )
        )
        fee_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="feeDetails",
                type="Element",
                min_occurs=0,
                max_occurs=99
            )
        )

        @dataclass
        class FeeTypeInfo:
            """
            :ivar carrier_fee_details:
            :ivar other_selection_details:
            """
            carrier_fee_details: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeTypeInfo.CarrierFeeDetails"] = field(
                default=None,
                metadata=dict(
                    name="carrierFeeDetails",
                    type="Element",
                    required=True
                )
            )
            other_selection_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeTypeInfo.OtherSelectionDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="otherSelectionDetails",
                    type="Element",
                    min_occurs=0,
                    max_occurs=98
                )
            )

            @dataclass
            class CarrierFeeDetails:
                """
                :ivar type:
                :ivar option_information:
                """
                type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="type",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                option_information: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="optionInformation",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class OtherSelectionDetails:
                """
                :ivar option:
                :ivar option_information:
                """
                option: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="option",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                option_information: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="optionInformation",
                        type="Element",
                        min_length=1.0,
                        max_length=35.0
                    )
                )

        @dataclass
        class RateTax:
            """
            :ivar monetary_details:
            """
            monetary_details: List["FareMasterPricerTravelBoardSearch.FeeOption.RateTax.MonetaryDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="monetaryDetails",
                    type="Element",
                    min_occurs=1,
                    max_occurs=20
                )
            )

            @dataclass
            class MonetaryDetails:
                """
                :ivar type_qualifier:
                :ivar amount:
                :ivar currency:
                """
                type_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="typeQualifier",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                amount: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="amount",
                        type="Element",
                        min_length=1.0,
                        max_length=12.0
                    )
                )
                currency: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="currency",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

        @dataclass
        class FeeDetails:
            """
            :ivar fee_info:
            :ivar associated_amounts:
            :ivar fee_description_grp:
            """
            fee_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeInfo"] = field(
                default=None,
                metadata=dict(
                    name="feeInfo",
                    type="Element",
                    required=True
                )
            )
            associated_amounts: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.AssociatedAmounts"] = field(
                default=None,
                metadata=dict(
                    name="associatedAmounts",
                    type="Element"
                )
            )
            fee_description_grp: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp"] = field(
                default=None,
                metadata=dict(
                    name="feeDescriptionGrp",
                    type="Element"
                )
            )

            @dataclass
            class FeeInfo:
                """
                :ivar data_type_information:
                :ivar data_information:
                """
                data_type_information: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeInfo.DataTypeInformation"] = field(
                    default=None,
                    metadata=dict(
                        name="dataTypeInformation",
                        type="Element",
                        required=True
                    )
                )
                data_information: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeInfo.DataInformation"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="dataInformation",
                        type="Element",
                        min_occurs=0,
                        max_occurs=99
                    )
                )

                @dataclass
                class DataTypeInformation:
                    """
                    :ivar sub_type:
                    :ivar option:
                    """
                    sub_type: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="subType",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    option: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="option",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class DataInformation:
                    """
                    :ivar indicator:
                    """
                    indicator: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="indicator",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

            @dataclass
            class AssociatedAmounts:
                """
                :ivar monetary_details:
                """
                monetary_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.AssociatedAmounts.MonetaryDetails"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="monetaryDetails",
                        type="Element",
                        min_occurs=1,
                        max_occurs=20
                    )
                )

                @dataclass
                class MonetaryDetails:
                    """
                    :ivar type_qualifier:
                    :ivar amount:
                    :ivar currency:
                    :ivar location:
                    """
                    type_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="typeQualifier",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    amount: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="amount",
                            type="Element",
                            min_length=1.0,
                            max_length=12.0
                        )
                    )
                    currency: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="currency",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    location: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="location",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )

            @dataclass
            class FeeDescriptionGrp:
                """
                :ivar item_number_info:
                :ivar service_attributes_info:
                :ivar service_description_info:
                """
                item_number_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ItemNumberInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="itemNumberInfo",
                        type="Element",
                        required=True
                    )
                )
                service_attributes_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceAttributesInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="serviceAttributesInfo",
                        type="Element"
                    )
                )
                service_description_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceDescriptionInfo"] = field(
                    default=None,
                    metadata=dict(
                        name="serviceDescriptionInfo",
                        type="Element"
                    )
                )

                @dataclass
                class ItemNumberInfo:
                    """
                    :ivar item_number_details:
                    """
                    item_number_details: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ItemNumberInfo.ItemNumberDetails"] = field(
                        default=None,
                        metadata=dict(
                            name="itemNumberDetails",
                            type="Element",
                            required=True
                        )
                    )

                    @dataclass
                    class ItemNumberDetails:
                        """
                        :ivar number:
                        :ivar type:
                        :ivar qualifier:
                        :ivar responsible_agency:
                        """
                        number: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="number",
                                type="Element",
                                min_length=1.0,
                                max_length=4.0
                            )
                        )
                        type: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="type",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="qualifier",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        responsible_agency: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="responsibleAgency",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )

                @dataclass
                class ServiceAttributesInfo:
                    """
                    :ivar attribute_qualifier:
                    :ivar attribute_details:
                    """
                    attribute_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="attributeQualifier",
                            type="Element",
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
                    attribute_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceAttributesInfo.AttributeDetails"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="attributeDetails",
                            type="Element",
                            min_occurs=1,
                            max_occurs=99
                        )
                    )

                    @dataclass
                    class AttributeDetails:
                        """
                        :ivar attribute_type:
                        :ivar attribute_description:
                        """
                        attribute_type: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="attributeType",
                                type="Element",
                                required=True,
                                min_length=1.0,
                                max_length=25.0
                            )
                        )
                        attribute_description: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="attributeDescription",
                                type="Element",
                                min_length=1.0,
                                max_length=256.0
                            )
                        )

                @dataclass
                class ServiceDescriptionInfo:
                    """
                    :ivar service_requirements_info:
                    :ivar seat_details:
                    """
                    service_requirements_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceDescriptionInfo.ServiceRequirementsInfo"] = field(
                        default=None,
                        metadata=dict(
                            name="serviceRequirementsInfo",
                            type="Element",
                            required=True
                        )
                    )
                    seat_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceDescriptionInfo.SeatDetails"] = field(
                        default_factory=list,
                        metadata=dict(
                            name="seatDetails",
                            type="Element",
                            min_occurs=0,
                            max_occurs=999
                        )
                    )

                    @dataclass
                    class ServiceRequirementsInfo:
                        """
                        :ivar service_classification:
                        :ivar service_status:
                        :ivar service_number_of_instances:
                        :ivar service_marketing_carrier:
                        :ivar service_group:
                        :ivar service_sub_group:
                        :ivar service_free_text:
                        """
                        service_classification: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="serviceClassification",
                                type="Element",
                                required=True,
                                min_length=1.0,
                                max_length=4.0
                            )
                        )
                        service_status: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="serviceStatus",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        service_number_of_instances: Optional[float] = field(
                            default=None,
                            metadata=dict(
                                name="serviceNumberOfInstances",
                                type="Element"
                            )
                        )
                        service_marketing_carrier: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="serviceMarketingCarrier",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        service_group: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="serviceGroup",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        service_sub_group: Optional[str] = field(
                            default=None,
                            metadata=dict(
                                name="serviceSubGroup",
                                type="Element",
                                min_length=1.0,
                                max_length=3.0
                            )
                        )
                        service_free_text: List[str] = field(
                            default_factory=list,
                            metadata=dict(
                                name="serviceFreeText",
                                type="Element",
                                min_occurs=0,
                                max_occurs=99,
                                min_length=1.0,
                                max_length=70.0
                            )
                        )

                    @dataclass
                    class SeatDetails:
                        """
                        :ivar seat_characteristics:
                        """
                        seat_characteristics: List[str] = field(
                            default_factory=list,
                            metadata=dict(
                                name="seatCharacteristics",
                                type="Element",
                                min_occurs=0,
                                max_occurs=5,
                                min_length=1.0,
                                max_length=2.0
                            )
                        )

    @dataclass
    class OfficeIdDetails:
        """
        :ivar office_id_information:
        :ivar nb_of_units:
        :ivar uid_option:
        :ivar pricing_tick_info:
        :ivar corporate_fare_info:
        :ivar travel_flight_info:
        :ivar airline_distribution_details:
        """
        office_id_information: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.OfficeIdInformation"] = field(
            default=None,
            metadata=dict(
                name="officeIdInformation",
                type="Element",
                required=True
            )
        )
        nb_of_units: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.NbOfUnits"] = field(
            default=None,
            metadata=dict(
                name="nbOfUnits",
                type="Element"
            )
        )
        uid_option: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.UidOption"] = field(
            default=None,
            metadata=dict(
                name="uidOption",
                type="Element"
            )
        )
        pricing_tick_info: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo"] = field(
            default=None,
            metadata=dict(
                name="pricingTickInfo",
                type="Element"
            )
        )
        corporate_fare_info: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.CorporateFareInfo"] = field(
            default=None,
            metadata=dict(
                name="corporateFareInfo",
                type="Element"
            )
        )
        travel_flight_info: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo"] = field(
            default=None,
            metadata=dict(
                name="travelFlightInfo",
                type="Element"
            )
        )
        airline_distribution_details: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails"] = field(
            default_factory=list,
            metadata=dict(
                name="airlineDistributionDetails",
                type="Element",
                min_occurs=0,
                max_occurs=6
            )
        )

        @dataclass
        class OfficeIdInformation:
            """
            :ivar office_identification:
            :ivar office_type:
            :ivar office_code:
            """
            office_identification: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.OfficeIdInformation.OfficeIdentification"] = field(
                default=None,
                metadata=dict(
                    name="officeIdentification",
                    type="Element"
                )
            )
            office_type: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="officeType",
                    type="Element",
                    min_length=1.0,
                    max_length=1.0
                )
            )
            office_code: Optional[str] = field(
                default=None,
                metadata=dict(
                    name="officeCode",
                    type="Element",
                    min_length=1.0,
                    max_length=30.0
                )
            )

            @dataclass
            class OfficeIdentification:
                """
                :ivar office_name:
                :ivar agent_signin:
                :ivar confidential_office:
                :ivar other_office:
                """
                office_name: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="officeName",
                        type="Element"
                    )
                )
                agent_signin: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="agentSignin",
                        type="Element",
                        min_length=1.0,
                        max_length=9.0
                    )
                )
                confidential_office: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="confidentialOffice",
                        type="Element",
                        min_length=1.0,
                        max_length=9.0
                    )
                )
                other_office: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="otherOffice",
                        type="Element",
                        min_length=1.0,
                        max_length=9.0
                    )
                )

        @dataclass
        class NbOfUnits:
            """
            :ivar unit_number_detail:
            """
            unit_number_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.NbOfUnits.UnitNumberDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="unitNumberDetail",
                    type="Element",
                    min_occurs=1,
                    max_occurs=20
                )
            )

            @dataclass
            class UnitNumberDetail:
                """
                :ivar number_of_units:
                :ivar type_of_unit:
                """
                number_of_units: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="numberOfUnits",
                        type="Element"
                    )
                )
                type_of_unit: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="typeOfUnit",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )

        @dataclass
        class UidOption:
            """
            :ivar attribute_details:
            """
            attribute_details: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.UidOption.AttributeDetails"] = field(
                default_factory=list,
                metadata=dict(
                    name="attributeDetails",
                    type="Element",
                    min_occurs=1,
                    max_occurs=20
                )
            )

            @dataclass
            class AttributeDetails:
                """
                :ivar attribute_type:
                :ivar attribute_description:
                """
                attribute_type: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="attributeType",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=5.0
                    )
                )
                attribute_description: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="attributeDescription",
                        type="Element",
                        min_length=1.0,
                        max_length=20.0
                    )
                )

        @dataclass
        class PricingTickInfo:
            """
            :ivar pricing_ticketing:
            :ivar ticketing_date:
            :ivar company_id:
            :ivar selling_point:
            :ivar ticketing_point:
            :ivar journey_origin_point:
            :ivar corporate_id:
            """
            pricing_ticketing: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.PricingTicketing"] = field(
                default=None,
                metadata=dict(
                    name="pricingTicketing",
                    type="Element"
                )
            )
            ticketing_date: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.TicketingDate"] = field(
                default=None,
                metadata=dict(
                    name="ticketingDate",
                    type="Element"
                )
            )
            company_id: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.CompanyId"] = field(
                default=None,
                metadata=dict(
                    name="companyId",
                    type="Element"
                )
            )
            selling_point: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.SellingPoint"] = field(
                default=None,
                metadata=dict(
                    name="sellingPoint",
                    type="Element"
                )
            )
            ticketing_point: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.TicketingPoint"] = field(
                default=None,
                metadata=dict(
                    name="ticketingPoint",
                    type="Element"
                )
            )
            journey_origin_point: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.JourneyOriginPoint"] = field(
                default=None,
                metadata=dict(
                    name="journeyOriginPoint",
                    type="Element"
                )
            )
            corporate_id: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.CorporateId"] = field(
                default=None,
                metadata=dict(
                    name="corporateId",
                    type="Element"
                )
            )

            @dataclass
            class PricingTicketing:
                """
                :ivar price_type:
                """
                price_type: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="priceType",
                        type="Element",
                        min_occurs=1,
                        max_occurs=50,
                        min_length=0.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class TicketingDate:
                """
                :ivar date:
                :ivar rtc_date:
                """
                date: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="date",
                        type="Element",
                        required=True,
                        min_length=6.0,
                        max_length=6.0
                    )
                )
                rtc_date: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="rtcDate",
                        type="Element",
                        min_length=6.0,
                        max_length=6.0
                    )
                )

            @dataclass
            class CompanyId:
                """
                :ivar value:
                """
                value: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="value",
                        type="Extension"
                    )
                )

            @dataclass
            class SellingPoint:
                """
                :ivar location_id:
                :ivar country:
                """
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                country: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="country",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class TicketingPoint:
                """
                :ivar location_id:
                :ivar country:
                """
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                country: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="country",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class JourneyOriginPoint:
                """
                :ivar location_id:
                :ivar country:
                """
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                country: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="country",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class CorporateId:
                """
                :ivar arc_number:
                :ivar ersp_number:
                :ivar iata_number:
                """
                arc_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="arcNumber",
                        type="Element",
                        min_length=1.0,
                        max_length=12.0
                    )
                )
                ersp_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="erspNumber",
                        type="Element",
                        min_length=1.0,
                        max_length=12.0
                    )
                )
                iata_number: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="iataNumber",
                        type="Element",
                        min_length=1.0,
                        max_length=12.0
                    )
                )

        @dataclass
        class CorporateFareInfo:
            """
            :ivar corporate_fare_identifiers:
            """
            corporate_fare_identifiers: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.CorporateFareInfo.CorporateFareIdentifiers"] = field(
                default=None,
                metadata=dict(
                    name="corporateFareIdentifiers",
                    type="Element"
                )
            )

            @dataclass
            class CorporateFareIdentifiers:
                """
                :ivar fare_qualifier:
                :ivar identify_number:
                """
                fare_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="fareQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=3.0
                    )
                )
                identify_number: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="identifyNumber",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20,
                        min_length=1.0,
                        max_length=35.0
                    )
                )

        @dataclass
        class TravelFlightInfo:
            """
            :ivar cabin_id:
            :ivar company_identity:
            :ivar flight_detail:
            :ivar inclusion_detail:
            :ivar exclusion_detail:
            :ivar unit_number_detail:
            """
            cabin_id: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.CabinId"] = field(
                default=None,
                metadata=dict(
                    name="cabinId",
                    type="Element"
                )
            )
            company_identity: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.CompanyIdentity"] = field(
                default_factory=list,
                metadata=dict(
                    name="companyIdentity",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            flight_detail: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.FlightDetail"] = field(
                default=None,
                metadata=dict(
                    name="flightDetail",
                    type="Element"
                )
            )
            inclusion_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.InclusionDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="inclusionDetail",
                    type="Element",
                    min_occurs=0,
                    max_occurs=20
                )
            )
            exclusion_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.ExclusionDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="exclusionDetail",
                    type="Element",
                    min_occurs=0,
                    max_occurs=2
                )
            )
            unit_number_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.UnitNumberDetail"] = field(
                default_factory=list,
                metadata=dict(
                    name="unitNumberDetail",
                    type="Element",
                    min_occurs=0,
                    max_occurs=9
                )
            )

            @dataclass
            class CabinId:
                """
                :ivar cabin_qualifier:
                :ivar cabin:
                """
                cabin_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="cabinQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=2.0
                    )
                )
                cabin: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="cabin",
                        type="Element",
                        min_occurs=1,
                        max_occurs=3,
                        min_length=0.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class CompanyIdentity:
                """
                :ivar carrier_qualifier:
                :ivar carrier_id:
                """
                carrier_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="carrierQualifier",
                        type="Element",
                        required=True,
                        min_length=0.0,
                        max_length=1.0
                    )
                )
                carrier_id: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="carrierId",
                        type="Element",
                        min_occurs=1,
                        max_occurs=99,
                        min_length=2.0,
                        max_length=3.0
                    )
                )

            @dataclass
            class FlightDetail:
                """
                :ivar flight_type:
                """
                flight_type: List[str] = field(
                    default_factory=list,
                    metadata=dict(
                        name="flightType",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9,
                        min_length=1.0,
                        max_length=2.0
                    )
                )

            @dataclass
            class InclusionDetail:
                """
                :ivar inclusion_identifier:
                :ivar location_id:
                :ivar airport_city_qualifier:
                """
                inclusion_identifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="inclusionIdentifier",
                        type="Element",
                        required=True,
                        min_length=0.0,
                        max_length=1.0
                    )
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="airportCityQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class ExclusionDetail:
                """
                :ivar exclusion_identifier:
                :ivar location_id:
                :ivar airport_city_qualifier:
                """
                exclusion_identifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="exclusionIdentifier",
                        type="Element",
                        required=True,
                        min_length=0.0,
                        max_length=1.0
                    )
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="locationId",
                        type="Element",
                        required=True,
                        min_length=3.0,
                        max_length=5.0
                    )
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="airportCityQualifier",
                        type="Element",
                        min_length=1.0,
                        max_length=1.0
                    )
                )

            @dataclass
            class UnitNumberDetail:
                """
                :ivar number_of_units:
                :ivar type_of_unit:
                """
                number_of_units: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="numberOfUnits",
                        type="Element",
                        required=True
                    )
                )
                type_of_unit: Optional[str] = field(
                    default=None,
                    metadata=dict(
                        name="typeOfUnit",
                        type="Element",
                        required=True,
                        min_length=1.0,
                        max_length=3.0
                    )
                )

        @dataclass
        class AirlineDistributionDetails:
            """
            :ivar requested_segment_ref:
            :ivar flight_info:
            """
            requested_segment_ref: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.RequestedSegmentRef"] = field(
                default=None,
                metadata=dict(
                    name="requestedSegmentRef",
                    type="Element",
                    required=True
                )
            )
            flight_info: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo"] = field(
                default=None,
                metadata=dict(
                    name="flightInfo",
                    type="Element"
                )
            )

            @dataclass
            class RequestedSegmentRef:
                """
                :ivar seg_ref:
                :ivar location_forcing:
                """
                seg_ref: Optional[float] = field(
                    default=None,
                    metadata=dict(
                        name="segRef",
                        type="Element",
                        required=True
                    )
                )
                location_forcing: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.RequestedSegmentRef.LocationForcing"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="locationForcing",
                        type="Element",
                        min_occurs=0,
                        max_occurs=2
                    )
                )

                @dataclass
                class LocationForcing:
                    """
                    :ivar airport_city_qualifier:
                    :ivar segment_number:
                    """
                    airport_city_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="airportCityQualifier",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=1.0
                        )
                    )
                    segment_number: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="segmentNumber",
                            type="Element",
                            required=True
                        )
                    )

            @dataclass
            class FlightInfo:
                """
                :ivar cabin_id:
                :ivar company_identity:
                :ivar flight_detail:
                :ivar inclusion_detail:
                :ivar exclusion_detail:
                :ivar unit_number_detail:
                """
                cabin_id: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.CabinId"] = field(
                    default=None,
                    metadata=dict(
                        name="cabinId",
                        type="Element"
                    )
                )
                company_identity: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.CompanyIdentity"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="companyIdentity",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )
                flight_detail: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.FlightDetail"] = field(
                    default=None,
                    metadata=dict(
                        name="flightDetail",
                        type="Element"
                    )
                )
                inclusion_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.InclusionDetail"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="inclusionDetail",
                        type="Element",
                        min_occurs=0,
                        max_occurs=20
                    )
                )
                exclusion_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.ExclusionDetail"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="exclusionDetail",
                        type="Element",
                        min_occurs=0,
                        max_occurs=2
                    )
                )
                unit_number_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.UnitNumberDetail"] = field(
                    default_factory=list,
                    metadata=dict(
                        name="unitNumberDetail",
                        type="Element",
                        min_occurs=0,
                        max_occurs=9
                    )
                )

                @dataclass
                class CabinId:
                    """
                    :ivar cabin_qualifier:
                    :ivar cabin:
                    """
                    cabin_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="cabinQualifier",
                            type="Element",
                            min_length=1.0,
                            max_length=2.0
                        )
                    )
                    cabin: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="cabin",
                            type="Element",
                            min_occurs=1,
                            max_occurs=3,
                            min_length=0.0,
                            max_length=1.0
                        )
                    )

                @dataclass
                class CompanyIdentity:
                    """
                    :ivar carrier_qualifier:
                    :ivar carrier_id:
                    """
                    carrier_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="carrierQualifier",
                            type="Element",
                            required=True,
                            min_length=0.0,
                            max_length=1.0
                        )
                    )
                    carrier_id: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="carrierId",
                            type="Element",
                            min_occurs=1,
                            max_occurs=99,
                            min_length=2.0,
                            max_length=3.0
                        )
                    )

                @dataclass
                class FlightDetail:
                    """
                    :ivar flight_type:
                    """
                    flight_type: List[str] = field(
                        default_factory=list,
                        metadata=dict(
                            name="flightType",
                            type="Element",
                            min_occurs=0,
                            max_occurs=9,
                            min_length=1.0,
                            max_length=2.0
                        )
                    )

                @dataclass
                class InclusionDetail:
                    """
                    :ivar inclusion_identifier:
                    :ivar location_id:
                    :ivar airport_city_qualifier:
                    """
                    inclusion_identifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="inclusionIdentifier",
                            type="Element",
                            required=True,
                            min_length=0.0,
                            max_length=1.0
                        )
                    )
                    location_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="locationId",
                            type="Element",
                            required=True,
                            min_length=3.0,
                            max_length=5.0
                        )
                    )
                    airport_city_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="airportCityQualifier",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

                @dataclass
                class ExclusionDetail:
                    """
                    :ivar exclusion_identifier:
                    :ivar location_id:
                    :ivar airport_city_qualifier:
                    """
                    exclusion_identifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="exclusionIdentifier",
                            type="Element",
                            required=True,
                            min_length=0.0,
                            max_length=1.0
                        )
                    )
                    location_id: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="locationId",
                            type="Element",
                            required=True,
                            min_length=3.0,
                            max_length=5.0
                        )
                    )
                    airport_city_qualifier: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="airportCityQualifier",
                            type="Element",
                            min_length=1.0,
                            max_length=1.0
                        )
                    )

                @dataclass
                class UnitNumberDetail:
                    """
                    :ivar number_of_units:
                    :ivar type_of_unit:
                    """
                    number_of_units: Optional[float] = field(
                        default=None,
                        metadata=dict(
                            name="numberOfUnits",
                            type="Element",
                            required=True
                        )
                    )
                    type_of_unit: Optional[str] = field(
                        default=None,
                        metadata=dict(
                            name="typeOfUnit",
                            type="Element",
                            required=True,
                            min_length=1.0,
                            max_length=3.0
                        )
                    )
