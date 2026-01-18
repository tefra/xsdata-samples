from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://xml.amadeus.com/FMPTBQ_15_3_1A"


@dataclass(kw_only=True)
class FareMasterPricerTravelBoardSearch:
    class Meta:
        name = "Fare_MasterPricerTravelBoardSearch"
        namespace = "http://xml.amadeus.com/FMPTBQ_15_3_1A"

    number_of_unit: None | FareMasterPricerTravelBoardSearch.NumberOfUnit = (
        field(
            default=None,
            metadata={
                "name": "numberOfUnit",
                "type": "Element",
            },
        )
    )
    global_options: None | FareMasterPricerTravelBoardSearch.GlobalOptions = (
        field(
            default=None,
            metadata={
                "name": "globalOptions",
                "type": "Element",
            },
        )
    )
    pax_reference: list[FareMasterPricerTravelBoardSearch.PaxReference] = (
        field(
            default_factory=list,
            metadata={
                "name": "paxReference",
                "type": "Element",
                "max_occurs": 6,
            },
        )
    )
    customer_ref: None | FareMasterPricerTravelBoardSearch.CustomerRef = field(
        default=None,
        metadata={
            "name": "customerRef",
            "type": "Element",
        },
    )
    form_of_payment_by_passenger: list[
        FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger
    ] = field(
        default_factory=list,
        metadata={
            "name": "formOfPaymentByPassenger",
            "type": "Element",
            "max_occurs": 60,
        },
    )
    solution_family: list[FareMasterPricerTravelBoardSearch.SolutionFamily] = (
        field(
            default_factory=list,
            metadata={
                "name": "solutionFamily",
                "type": "Element",
                "max_occurs": 20,
            },
        )
    )
    passenger_info_grp: list[
        FareMasterPricerTravelBoardSearch.PassengerInfoGrp
    ] = field(
        default_factory=list,
        metadata={
            "name": "passengerInfoGrp",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    fare_families: list[FareMasterPricerTravelBoardSearch.FareFamilies] = (
        field(
            default_factory=list,
            metadata={
                "name": "fareFamilies",
                "type": "Element",
                "max_occurs": 20,
            },
        )
    )
    fare_options: None | FareMasterPricerTravelBoardSearch.FareOptions = field(
        default=None,
        metadata={
            "name": "fareOptions",
            "type": "Element",
        },
    )
    price_to_beat: None | FareMasterPricerTravelBoardSearch.PriceToBeat = (
        field(
            default=None,
            metadata={
                "name": "priceToBeat",
                "type": "Element",
            },
        )
    )
    tax_info: list[FareMasterPricerTravelBoardSearch.TaxInfo] = field(
        default_factory=list,
        metadata={
            "name": "taxInfo",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    travel_flight_info: (
        None | FareMasterPricerTravelBoardSearch.TravelFlightInfo
    ) = field(
        default=None,
        metadata={
            "name": "travelFlightInfo",
            "type": "Element",
        },
    )
    value_search: list[FareMasterPricerTravelBoardSearch.ValueSearch] = field(
        default_factory=list,
        metadata={
            "name": "valueSearch",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    buckets: list[FareMasterPricerTravelBoardSearch.Buckets] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )
    itinerary: list[FareMasterPricerTravelBoardSearch.Itinerary] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 18,
        },
    )
    ticket_change_info: (
        None | FareMasterPricerTravelBoardSearch.TicketChangeInfo
    ) = field(
        default=None,
        metadata={
            "name": "ticketChangeInfo",
            "type": "Element",
        },
    )
    combination_fare_families: list[
        FareMasterPricerTravelBoardSearch.CombinationFareFamilies
    ] = field(
        default_factory=list,
        metadata={
            "name": "combinationFareFamilies",
            "type": "Element",
            "max_occurs": 2000,
        },
    )
    fee_option: list[FareMasterPricerTravelBoardSearch.FeeOption] = field(
        default_factory=list,
        metadata={
            "name": "feeOption",
            "type": "Element",
            "max_occurs": 9,
        },
    )
    office_id_details: list[
        FareMasterPricerTravelBoardSearch.OfficeIdDetails
    ] = field(
        default_factory=list,
        metadata={
            "name": "officeIdDetails",
            "type": "Element",
            "max_occurs": 20,
        },
    )

    @dataclass(kw_only=True)
    class NumberOfUnit:
        unit_number_detail: list[
            FareMasterPricerTravelBoardSearch.NumberOfUnit.UnitNumberDetail
        ] = field(
            default_factory=list,
            metadata={
                "name": "unitNumberDetail",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 20,
            },
        )

        @dataclass(kw_only=True)
        class UnitNumberDetail:
            number_of_units: Decimal = field(
                metadata={
                    "name": "numberOfUnits",
                    "type": "Element",
                    "required": True,
                }
            )
            type_of_unit: str = field(
                metadata={
                    "name": "typeOfUnit",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )

    @dataclass(kw_only=True)
    class GlobalOptions:
        selection_details: list[
            FareMasterPricerTravelBoardSearch.GlobalOptions.SelectionDetails
        ] = field(
            default_factory=list,
            metadata={
                "name": "selectionDetails",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 10,
            },
        )

        @dataclass(kw_only=True)
        class SelectionDetails:
            option: str = field(
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            option_information: None | str = field(
                default=None,
                metadata={
                    "name": "optionInformation",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                },
            )

    @dataclass(kw_only=True)
    class PaxReference:
        ptc: list[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 3,
                "min_length": 1,
                "max_length": 6,
            },
        )
        traveller: list[
            FareMasterPricerTravelBoardSearch.PaxReference.Traveller
        ] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 9,
            },
        )

        @dataclass(kw_only=True)
        class Traveller:
            ref: Decimal = field(
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            infant_indicator: None | str = field(
                default=None,
                metadata={
                    "name": "infantIndicator",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 1,
                },
            )

    @dataclass(kw_only=True)
    class CustomerRef:
        customer_references: list[
            FareMasterPricerTravelBoardSearch.CustomerRef.CustomerReferences
        ] = field(
            default_factory=list,
            metadata={
                "name": "customerReferences",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 20,
            },
        )

        @dataclass(kw_only=True)
        class CustomerReferences:
            reference_qualifier: str = field(
                metadata={
                    "name": "referenceQualifier",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            reference_number: None | str = field(
                default=None,
                metadata={
                    "name": "referenceNumber",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                },
            )
            reference_party_name: None | str = field(
                default=None,
                metadata={
                    "name": "referencePartyName",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                },
            )
            traveller_reference_nbr: None | str = field(
                default=None,
                metadata={
                    "name": "travellerReferenceNbr",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                },
            )

    @dataclass(kw_only=True)
    class FormOfPaymentByPassenger:
        form_of_payment_details: FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.FormOfPaymentDetails = field(
            metadata={
                "name": "formOfPaymentDetails",
                "type": "Element",
                "required": True,
            }
        )
        passenger_fee_reference: (
            None
            | FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.PassengerFeeReference
        ) = field(
            default=None,
            metadata={
                "name": "passengerFeeReference",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class FormOfPaymentDetails:
            form_of_payment_details: list[
                FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.FormOfPaymentDetails.FormOfPaymentDetailsInner
            ] = field(
                default_factory=list,
                metadata={
                    "name": "formOfPaymentDetails",
                    "type": "Element",
                    "max_occurs": 9,
                },
            )

            @dataclass(kw_only=True)
            class FormOfPaymentDetailsInner:
                type_value: str = field(
                    metadata={
                        "name": "type",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                charged_amount: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "chargedAmount",
                        "type": "Element",
                    },
                )
                credit_card_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "creditCardNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20,
                    },
                )

        @dataclass(kw_only=True)
        class PassengerFeeReference:
            passenger_fee_ref_type: None | str = field(
                default=None,
                metadata={
                    "name": "passengerFeeRefType",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            passenger_fee_ref_number: None | Decimal = field(
                default=None,
                metadata={
                    "name": "passengerFeeRefNumber",
                    "type": "Element",
                },
            )
            other_characteristics: (
                None
                | FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.PassengerFeeReference.OtherCharacteristics
            ) = field(
                default=None,
                metadata={
                    "name": "otherCharacteristics",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class OtherCharacteristics:
                passenger_fee_ref_qualif: None | str = field(
                    default=None,
                    metadata={
                        "name": "passengerFeeRefQualif",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

    @dataclass(kw_only=True)
    class SolutionFamily:
        value_qualifier: None | str = field(
            default=None,
            metadata={
                "name": "valueQualifier",
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
            },
        )
        value: None | Decimal = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        fare_details: (
            None | FareMasterPricerTravelBoardSearch.SolutionFamily.FareDetails
        ) = field(
            default=None,
            metadata={
                "name": "fareDetails",
                "type": "Element",
            },
        )
        identity_number: None | str = field(
            default=None,
            metadata={
                "name": "identityNumber",
                "type": "Element",
                "min_length": 1,
                "max_length": 35,
            },
        )
        fare_type_grouping: (
            None
            | FareMasterPricerTravelBoardSearch.SolutionFamily.FareTypeGrouping
        ) = field(
            default=None,
            metadata={
                "name": "fareTypeGrouping",
                "type": "Element",
            },
        )
        rate_category: None | str = field(
            default=None,
            metadata={
                "name": "rateCategory",
                "type": "Element",
                "min_length": 1,
                "max_length": 35,
            },
        )

        @dataclass(kw_only=True)
        class FareDetails:
            qualifier: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            rate: None | Decimal = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            country: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            fare_category: None | str = field(
                default=None,
                metadata={
                    "name": "fareCategory",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )

        @dataclass(kw_only=True)
        class FareTypeGrouping:
            pricing_group: None | str = field(
                default=None,
                metadata={
                    "name": "pricingGroup",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                },
            )

    @dataclass(kw_only=True)
    class PassengerInfoGrp:
        passenger_reference: FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PassengerReference = field(
            metadata={
                "name": "passengerReference",
                "type": "Element",
                "required": True,
            }
        )
        psg_details_info: list[
            FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo
        ] = field(
            default_factory=list,
            metadata={
                "name": "psgDetailsInfo",
                "type": "Element",
                "max_occurs": 2,
            },
        )

        @dataclass(kw_only=True)
        class PassengerReference:
            segment_control_details: list[
                FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PassengerReference.SegmentControlDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "segmentControlDetails",
                    "type": "Element",
                    "max_occurs": 9,
                },
            )

            @dataclass(kw_only=True)
            class SegmentControlDetails:
                quantity: None | Decimal = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

        @dataclass(kw_only=True)
        class PsgDetailsInfo:
            discount_ptc: FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo.DiscountPtc = field(
                metadata={
                    "name": "discountPtc",
                    "type": "Element",
                    "required": True,
                }
            )
            flequent_flyer_details: (
                None
                | FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo.FlequentFlyerDetails
            ) = field(
                default=None,
                metadata={
                    "name": "flequentFlyerDetails",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class DiscountPtc:
                value_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "valueQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                value: None | Decimal = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class FlequentFlyerDetails:
                frequent_traveller_details: list[
                    FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo.FlequentFlyerDetails.FrequentTravellerDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "frequentTravellerDetails",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 99,
                    },
                )

                @dataclass(kw_only=True)
                class FrequentTravellerDetails:
                    carrier: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        },
                    )
                    number: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 28,
                        },
                    )
                    customer_reference: None | str = field(
                        default=None,
                        metadata={
                            "name": "customerReference",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 10,
                        },
                    )
                    status: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    tier_level: None | str = field(
                        default=None,
                        metadata={
                            "name": "tierLevel",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        },
                    )
                    priority_code: None | str = field(
                        default=None,
                        metadata={
                            "name": "priorityCode",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 12,
                        },
                    )
                    tier_description: None | str = field(
                        default=None,
                        metadata={
                            "name": "tierDescription",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        },
                    )
                    company_code: None | str = field(
                        default=None,
                        metadata={
                            "name": "companyCode",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        },
                    )
                    customer_value: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "customerValue",
                            "type": "Element",
                        },
                    )
                    type_value: None | str = field(
                        default=None,
                        metadata={
                            "name": "type",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

    @dataclass(kw_only=True)
    class FareFamilies:
        family_information: FareMasterPricerTravelBoardSearch.FareFamilies.FamilyInformation = field(
            metadata={
                "name": "familyInformation",
                "type": "Element",
                "required": True,
            }
        )
        family_criteria: (
            None
            | FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria
        ) = field(
            default=None,
            metadata={
                "name": "familyCriteria",
                "type": "Element",
            },
        )
        fare_family_segment: list[
            FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment
        ] = field(
            default_factory=list,
            metadata={
                "name": "fareFamilySegment",
                "type": "Element",
                "max_occurs": 6,
            },
        )
        other_possible_criteria: list[
            FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria
        ] = field(
            default_factory=list,
            metadata={
                "name": "otherPossibleCriteria",
                "type": "Element",
                "max_occurs": 20,
            },
        )

        @dataclass(kw_only=True)
        class FamilyInformation:
            ref_number: None | Decimal = field(
                default=None,
                metadata={
                    "name": "refNumber",
                    "type": "Element",
                },
            )
            fare_familyname: None | str = field(
                default=None,
                metadata={
                    "name": "fareFamilyname",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                },
            )
            hierarchy: None | Decimal = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            commercial_family_details: list[
                FareMasterPricerTravelBoardSearch.FareFamilies.FamilyInformation.CommercialFamilyDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "commercialFamilyDetails",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class CommercialFamilyDetails:
                commercial_family: str = field(
                    metadata={
                        "name": "commercialFamily",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 10,
                    }
                )

        @dataclass(kw_only=True)
        class FamilyCriteria:
            carrier_id: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "carrierId",
                    "type": "Element",
                    "max_occurs": 20,
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            rdb: list[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 20,
                    "min_length": 1,
                    "max_length": 2,
                },
            )
            fare_family_info: (
                None
                | FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.FareFamilyInfo
            ) = field(
                default=None,
                metadata={
                    "name": "fareFamilyInfo",
                    "type": "Element",
                },
            )
            fare_product_detail: list[
                FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.FareProductDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "fareProductDetail",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            corporate_info: list[
                FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.CorporateInfo
            ] = field(
                default_factory=list,
                metadata={
                    "name": "corporateInfo",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            cabin_product: list[
                FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.CabinProduct
            ] = field(
                default_factory=list,
                metadata={
                    "name": "cabinProduct",
                    "type": "Element",
                    "max_occurs": 6,
                },
            )
            cabin_processing_identifier: None | str = field(
                default=None,
                metadata={
                    "name": "cabinProcessingIdentifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            date_time_details: list[
                FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.DateTimeDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "dateTimeDetails",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            other_criteria: list[
                FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.OtherCriteria
            ] = field(
                default_factory=list,
                metadata={
                    "name": "otherCriteria",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class FareFamilyInfo:
                fare_family_qual: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "fareFamilyQual",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 9,
                        "min_length": 0,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class FareProductDetail:
                fare_basis: None | str = field(
                    default=None,
                    metadata={
                        "name": "fareBasis",
                        "type": "Element",
                        "min_length": 0,
                        "max_length": 18,
                    },
                )
                fare_type: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "fareType",
                        "type": "Element",
                        "max_occurs": 3,
                        "min_length": 0,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class CorporateInfo:
                corporate_number_identifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "corporateNumberIdentifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    },
                )
                corporate_name: None | str = field(
                    default=None,
                    metadata={
                        "name": "corporateName",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20,
                    },
                )

            @dataclass(kw_only=True)
            class CabinProduct:
                cabin_designator: str = field(
                    metadata={
                        "name": "cabinDesignator",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

            @dataclass(kw_only=True)
            class DateTimeDetails:
                date: str = field(
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 6,
                        "max_length": 6,
                    }
                )
                other_date: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "otherDate",
                        "type": "Element",
                    },
                )

            @dataclass(kw_only=True)
            class OtherCriteria:
                name: str = field(
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                value: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 10,
                        "min_length": 1,
                        "max_length": 20,
                    },
                )

        @dataclass(kw_only=True)
        class FareFamilySegment:
            reference_info: FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.ReferenceInfo = field(
                metadata={
                    "name": "referenceInfo",
                    "type": "Element",
                    "required": True,
                }
            )
            family_criteria: (
                None
                | FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria
            ) = field(
                default=None,
                metadata={
                    "name": "familyCriteria",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class ReferenceInfo:
                referencing_detail: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.ReferenceInfo.ReferencingDetail
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "referencingDetail",
                        "type": "Element",
                        "max_occurs": 9,
                    },
                )

                @dataclass(kw_only=True)
                class ReferencingDetail:
                    ref_qualifier: None | str = field(
                        default=None,
                        metadata={
                            "name": "refQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    ref_number: Decimal = field(
                        metadata={
                            "name": "refNumber",
                            "type": "Element",
                            "required": True,
                        }
                    )

            @dataclass(kw_only=True)
            class FamilyCriteria:
                carrier_id: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "carrierId",
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                rdb: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 2,
                    },
                )
                fare_family_info: (
                    None
                    | FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.FareFamilyInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "fareFamilyInfo",
                        "type": "Element",
                    },
                )
                fare_product_detail: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.FareProductDetail
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "fareProductDetail",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )
                corporate_info: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.CorporateInfo
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "corporateInfo",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )
                cabin_product: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.CabinProduct
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "cabinProduct",
                        "type": "Element",
                        "max_occurs": 6,
                    },
                )
                cabin_processing_identifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "cabinProcessingIdentifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                date_time_details: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.DateTimeDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "dateTimeDetails",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )
                other_criteria: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.OtherCriteria
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "otherCriteria",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )

                @dataclass(kw_only=True)
                class FareFamilyInfo:
                    fare_family_qual: list[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareFamilyQual",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 9,
                            "min_length": 0,
                            "max_length": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class FareProductDetail:
                    fare_basis: None | str = field(
                        default=None,
                        metadata={
                            "name": "fareBasis",
                            "type": "Element",
                            "min_length": 0,
                            "max_length": 18,
                        },
                    )
                    fare_type: list[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareType",
                            "type": "Element",
                            "max_occurs": 3,
                            "min_length": 0,
                            "max_length": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class CorporateInfo:
                    corporate_number_identifier: None | str = field(
                        default=None,
                        metadata={
                            "name": "corporateNumberIdentifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 12,
                        },
                    )
                    corporate_name: None | str = field(
                        default=None,
                        metadata={
                            "name": "corporateName",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 20,
                        },
                    )

                @dataclass(kw_only=True)
                class CabinProduct:
                    cabin_designator: str = field(
                        metadata={
                            "name": "cabinDesignator",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass(kw_only=True)
                class DateTimeDetails:
                    date: str = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 6,
                            "max_length": 6,
                        }
                    )
                    other_date: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "otherDate",
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class OtherCriteria:
                    name: str = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 5,
                        }
                    )
                    value: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 10,
                            "min_length": 1,
                            "max_length": 20,
                        },
                    )

        @dataclass(kw_only=True)
        class OtherPossibleCriteria:
            logical_link: FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.LogicalLink = field(
                metadata={
                    "name": "logicalLink",
                    "type": "Element",
                    "required": True,
                }
            )
            family_criteria: (
                None
                | FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria
            ) = field(
                default=None,
                metadata={
                    "name": "familyCriteria",
                    "type": "Element",
                },
            )
            fare_family_segment: list[
                FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment
            ] = field(
                default_factory=list,
                metadata={
                    "name": "fareFamilySegment",
                    "type": "Element",
                    "max_occurs": 6,
                },
            )

            @dataclass(kw_only=True)
            class LogicalLink:
                boolean_expression: FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.LogicalLink.BooleanExpression = field(
                    metadata={
                        "name": "booleanExpression",
                        "type": "Element",
                        "required": True,
                    }
                )

                @dataclass(kw_only=True)
                class BooleanExpression:
                    code_operator: None | str = field(
                        default=None,
                        metadata={
                            "name": "codeOperator",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

            @dataclass(kw_only=True)
            class FamilyCriteria:
                carrier_id: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "carrierId",
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                rdb: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 2,
                    },
                )
                fare_family_info: (
                    None
                    | FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.FareFamilyInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "fareFamilyInfo",
                        "type": "Element",
                    },
                )
                fare_product_detail: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.FareProductDetail
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "fareProductDetail",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )
                corporate_info: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.CorporateInfo
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "corporateInfo",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )
                cabin_product: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.CabinProduct
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "cabinProduct",
                        "type": "Element",
                        "max_occurs": 6,
                    },
                )
                cabin_processing_identifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "cabinProcessingIdentifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                date_time_details: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.DateTimeDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "dateTimeDetails",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )
                other_criteria: list[
                    FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.OtherCriteria
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "otherCriteria",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )

                @dataclass(kw_only=True)
                class FareFamilyInfo:
                    fare_family_qual: list[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareFamilyQual",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 9,
                            "min_length": 0,
                            "max_length": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class FareProductDetail:
                    fare_basis: None | str = field(
                        default=None,
                        metadata={
                            "name": "fareBasis",
                            "type": "Element",
                            "min_length": 0,
                            "max_length": 18,
                        },
                    )
                    fare_type: list[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareType",
                            "type": "Element",
                            "max_occurs": 3,
                            "min_length": 0,
                            "max_length": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class CorporateInfo:
                    corporate_number_identifier: None | str = field(
                        default=None,
                        metadata={
                            "name": "corporateNumberIdentifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 12,
                        },
                    )
                    corporate_name: None | str = field(
                        default=None,
                        metadata={
                            "name": "corporateName",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 20,
                        },
                    )

                @dataclass(kw_only=True)
                class CabinProduct:
                    cabin_designator: str = field(
                        metadata={
                            "name": "cabinDesignator",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass(kw_only=True)
                class DateTimeDetails:
                    date: str = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 6,
                            "max_length": 6,
                        }
                    )
                    other_date: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "otherDate",
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class OtherCriteria:
                    name: str = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 5,
                        }
                    )
                    value: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 10,
                            "min_length": 1,
                            "max_length": 20,
                        },
                    )

            @dataclass(kw_only=True)
            class FareFamilySegment:
                reference_info: FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.ReferenceInfo = field(
                    metadata={
                        "name": "referenceInfo",
                        "type": "Element",
                        "required": True,
                    }
                )
                family_criteria: (
                    None
                    | FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria
                ) = field(
                    default=None,
                    metadata={
                        "name": "familyCriteria",
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class ReferenceInfo:
                    referencing_detail: list[
                        FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.ReferenceInfo.ReferencingDetail
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "referencingDetail",
                            "type": "Element",
                            "max_occurs": 9,
                        },
                    )

                    @dataclass(kw_only=True)
                    class ReferencingDetail:
                        ref_qualifier: None | str = field(
                            default=None,
                            metadata={
                                "name": "refQualifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        ref_number: Decimal = field(
                            metadata={
                                "name": "refNumber",
                                "type": "Element",
                                "required": True,
                            }
                        )

                @dataclass(kw_only=True)
                class FamilyCriteria:
                    carrier_id: list[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "carrierId",
                            "type": "Element",
                            "max_occurs": 20,
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    rdb: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 20,
                            "min_length": 1,
                            "max_length": 2,
                        },
                    )
                    fare_family_info: (
                        None
                        | FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.FareFamilyInfo
                    ) = field(
                        default=None,
                        metadata={
                            "name": "fareFamilyInfo",
                            "type": "Element",
                        },
                    )
                    fare_product_detail: list[
                        FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.FareProductDetail
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareProductDetail",
                            "type": "Element",
                            "max_occurs": 20,
                        },
                    )
                    corporate_info: list[
                        FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.CorporateInfo
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "corporateInfo",
                            "type": "Element",
                            "max_occurs": 20,
                        },
                    )
                    cabin_product: list[
                        FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.CabinProduct
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "cabinProduct",
                            "type": "Element",
                            "max_occurs": 6,
                        },
                    )
                    cabin_processing_identifier: None | str = field(
                        default=None,
                        metadata={
                            "name": "cabinProcessingIdentifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    date_time_details: list[
                        FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.DateTimeDetails
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "dateTimeDetails",
                            "type": "Element",
                            "max_occurs": 20,
                        },
                    )
                    other_criteria: list[
                        FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.OtherCriteria
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "otherCriteria",
                            "type": "Element",
                            "max_occurs": 20,
                        },
                    )

                    @dataclass(kw_only=True)
                    class FareFamilyInfo:
                        fare_family_qual: list[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "fareFamilyQual",
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 9,
                                "min_length": 0,
                                "max_length": 3,
                            },
                        )

                    @dataclass(kw_only=True)
                    class FareProductDetail:
                        fare_basis: None | str = field(
                            default=None,
                            metadata={
                                "name": "fareBasis",
                                "type": "Element",
                                "min_length": 0,
                                "max_length": 18,
                            },
                        )
                        fare_type: list[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "fareType",
                                "type": "Element",
                                "max_occurs": 3,
                                "min_length": 0,
                                "max_length": 3,
                            },
                        )

                    @dataclass(kw_only=True)
                    class CorporateInfo:
                        corporate_number_identifier: None | str = field(
                            default=None,
                            metadata={
                                "name": "corporateNumberIdentifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 12,
                            },
                        )
                        corporate_name: None | str = field(
                            default=None,
                            metadata={
                                "name": "corporateName",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 20,
                            },
                        )

                    @dataclass(kw_only=True)
                    class CabinProduct:
                        cabin_designator: str = field(
                            metadata={
                                "name": "cabinDesignator",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )

                    @dataclass(kw_only=True)
                    class DateTimeDetails:
                        date: str = field(
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 6,
                                "max_length": 6,
                            }
                        )
                        other_date: None | Decimal = field(
                            default=None,
                            metadata={
                                "name": "otherDate",
                                "type": "Element",
                            },
                        )

                    @dataclass(kw_only=True)
                    class OtherCriteria:
                        name: str = field(
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 5,
                            }
                        )
                        value: list[str] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 10,
                                "min_length": 1,
                                "max_length": 20,
                            },
                        )

    @dataclass(kw_only=True)
    class FareOptions:
        pricing_tick_info: FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo = field(
            metadata={
                "name": "pricingTickInfo",
                "type": "Element",
                "required": True,
            }
        )
        corporate: (
            None | FareMasterPricerTravelBoardSearch.FareOptions.Corporate
        ) = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        ticketing_price_scheme: (
            None
            | FareMasterPricerTravelBoardSearch.FareOptions.TicketingPriceScheme
        ) = field(
            default=None,
            metadata={
                "name": "ticketingPriceScheme",
                "type": "Element",
            },
        )
        fee_id_description: (
            None
            | FareMasterPricerTravelBoardSearch.FareOptions.FeeIdDescription
        ) = field(
            default=None,
            metadata={
                "name": "feeIdDescription",
                "type": "Element",
            },
        )
        conversion_rate: (
            None | FareMasterPricerTravelBoardSearch.FareOptions.ConversionRate
        ) = field(
            default=None,
            metadata={
                "name": "conversionRate",
                "type": "Element",
            },
        )
        form_of_payment: (
            None | FareMasterPricerTravelBoardSearch.FareOptions.FormOfPayment
        ) = field(
            default=None,
            metadata={
                "name": "formOfPayment",
                "type": "Element",
            },
        )
        frequent_traveller_info: (
            None
            | FareMasterPricerTravelBoardSearch.FareOptions.FrequentTravellerInfo
        ) = field(
            default=None,
            metadata={
                "name": "frequentTravellerInfo",
                "type": "Element",
            },
        )
        monetary_cabin_info: (
            None
            | FareMasterPricerTravelBoardSearch.FareOptions.MonetaryCabinInfo
        ) = field(
            default=None,
            metadata={
                "name": "monetaryCabinInfo",
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class PricingTickInfo:
            pricing_ticketing: (
                None
                | FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.PricingTicketing
            ) = field(
                default=None,
                metadata={
                    "name": "pricingTicketing",
                    "type": "Element",
                },
            )
            ticketing_date: (
                None
                | FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.TicketingDate
            ) = field(
                default=None,
                metadata={
                    "name": "ticketingDate",
                    "type": "Element",
                },
            )
            company_id: None | object = field(
                default=None,
                metadata={
                    "name": "companyId",
                    "type": "Element",
                },
            )
            selling_point: (
                None
                | FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.SellingPoint
            ) = field(
                default=None,
                metadata={
                    "name": "sellingPoint",
                    "type": "Element",
                },
            )
            ticketing_point: (
                None
                | FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.TicketingPoint
            ) = field(
                default=None,
                metadata={
                    "name": "ticketingPoint",
                    "type": "Element",
                },
            )
            journey_origin_point: (
                None
                | FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.JourneyOriginPoint
            ) = field(
                default=None,
                metadata={
                    "name": "journeyOriginPoint",
                    "type": "Element",
                },
            )
            corporate_id: (
                None
                | FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.CorporateId
            ) = field(
                default=None,
                metadata={
                    "name": "corporateId",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class PricingTicketing:
                price_type: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "priceType",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 50,
                        "min_length": 0,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class TicketingDate:
                date: str = field(
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 6,
                        "max_length": 6,
                    }
                )
                rtc_date: None | str = field(
                    default=None,
                    metadata={
                        "name": "rtcDate",
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    },
                )

            @dataclass(kw_only=True)
            class SellingPoint:
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class TicketingPoint:
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class JourneyOriginPoint:
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class CorporateId:
                arc_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "arcNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    },
                )
                ersp_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "erspNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    },
                )
                iata_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "iataNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    },
                )

        @dataclass(kw_only=True)
        class Corporate:
            corporate_id: list[
                FareMasterPricerTravelBoardSearch.FareOptions.Corporate.CorporateId
            ] = field(
                default_factory=list,
                metadata={
                    "name": "corporateId",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class CorporateId:
                corporate_qualifier: str = field(
                    metadata={
                        "name": "corporateQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 3,
                    }
                )
                identity: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 9,
                        "min_length": 1,
                        "max_length": 20,
                    },
                )

        @dataclass(kw_only=True)
        class TicketingPriceScheme:
            reference_number: str = field(
                metadata={
                    "name": "referenceNumber",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 35,
                }
            )
            name: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                },
            )
            status: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            description: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 250,
                },
            )

        @dataclass(kw_only=True)
        class FeeIdDescription:
            fee_id: list[
                FareMasterPricerTravelBoardSearch.FareOptions.FeeIdDescription.FeeId
            ] = field(
                default_factory=list,
                metadata={
                    "name": "feeId",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class FeeId:
                fee_type: str = field(
                    metadata={
                        "name": "feeType",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                fee_id_number: str = field(
                    metadata={
                        "name": "feeIdNumber",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 50,
                    }
                )

        @dataclass(kw_only=True)
        class ConversionRate:
            conversion_rate_detail: list[
                FareMasterPricerTravelBoardSearch.FareOptions.ConversionRate.ConversionRateDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "conversionRateDetail",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 2,
                },
            )

            @dataclass(kw_only=True)
            class ConversionRateDetail:
                conversion_type: None | str = field(
                    default=None,
                    metadata={
                        "name": "conversionType",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                currency: str = field(
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass(kw_only=True)
        class FormOfPayment:
            form_of_payment_details: list[
                FareMasterPricerTravelBoardSearch.FareOptions.FormOfPayment.FormOfPaymentDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "formOfPaymentDetails",
                    "type": "Element",
                    "max_occurs": 9,
                },
            )

            @dataclass(kw_only=True)
            class FormOfPaymentDetails:
                type_value: str = field(
                    metadata={
                        "name": "type",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                charged_amount: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "chargedAmount",
                        "type": "Element",
                    },
                )
                credit_card_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "creditCardNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20,
                    },
                )

        @dataclass(kw_only=True)
        class FrequentTravellerInfo:
            frequent_traveller_details: list[
                FareMasterPricerTravelBoardSearch.FareOptions.FrequentTravellerInfo.FrequentTravellerDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "frequentTravellerDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class FrequentTravellerDetails:
                carrier: str = field(
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                number: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 25,
                    },
                )
                customer_reference: None | str = field(
                    default=None,
                    metadata={
                        "name": "customerReference",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 10,
                    },
                )
                tier_level: None | str = field(
                    default=None,
                    metadata={
                        "name": "tierLevel",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 35,
                    },
                )
                priority_code: None | str = field(
                    default=None,
                    metadata={
                        "name": "priorityCode",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    },
                )
                tier_description: None | str = field(
                    default=None,
                    metadata={
                        "name": "tierDescription",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 35,
                    },
                )
                type_value: None | str = field(
                    default=None,
                    metadata={
                        "name": "type",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

        @dataclass(kw_only=True)
        class MonetaryCabinInfo:
            money_and_cabin_info: list[
                FareMasterPricerTravelBoardSearch.FareOptions.MonetaryCabinInfo.MoneyAndCabinInfo
            ] = field(
                default_factory=list,
                metadata={
                    "name": "moneyAndCabinInfo",
                    "type": "Element",
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class MoneyAndCabinInfo:
                amount_type: None | str = field(
                    default=None,
                    metadata={
                        "name": "amountType",
                        "type": "Element",
                        "min_length": 0,
                        "max_length": 3,
                    },
                )
                amount: Decimal = field(
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                currency: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                location_id: None | str = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "min_length": 3,
                        "max_length": 5,
                    },
                )
                cabin_class_designator: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "cabinClassDesignator",
                        "type": "Element",
                        "max_occurs": 9,
                        "min_length": 1,
                        "max_length": 1,
                    },
                )

    @dataclass(kw_only=True)
    class PriceToBeat:
        money_info: FareMasterPricerTravelBoardSearch.PriceToBeat.MoneyInfo = (
            field(
                metadata={
                    "name": "moneyInfo",
                    "type": "Element",
                    "required": True,
                }
            )
        )
        additional_money_info: list[
            FareMasterPricerTravelBoardSearch.PriceToBeat.AdditionalMoneyInfo
        ] = field(
            default_factory=list,
            metadata={
                "name": "additionalMoneyInfo",
                "type": "Element",
                "max_occurs": 19,
            },
        )

        @dataclass(kw_only=True)
        class MoneyInfo:
            qualifier: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            amount: Decimal = field(
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            currency: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )

        @dataclass(kw_only=True)
        class AdditionalMoneyInfo:
            qualifier: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            amount: Decimal = field(
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            currency: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            location_id: None | str = field(
                default=None,
                metadata={
                    "name": "locationId",
                    "type": "Element",
                    "min_length": 3,
                    "max_length": 3,
                },
            )

    @dataclass(kw_only=True)
    class TaxInfo:
        withhold_tax_surcharge: None | str = field(
            default=None,
            metadata={
                "name": "withholdTaxSurcharge",
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
            },
        )
        tax_detail: list[
            FareMasterPricerTravelBoardSearch.TaxInfo.TaxDetail
        ] = field(
            default_factory=list,
            metadata={
                "name": "taxDetail",
                "type": "Element",
                "max_occurs": 99,
            },
        )

        @dataclass(kw_only=True)
        class TaxDetail:
            rate: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 18,
                },
            )
            country: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            currency: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            type_value: None | str = field(
                default=None,
                metadata={
                    "name": "type",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            amount_qualifier: None | str = field(
                default=None,
                metadata={
                    "name": "amountQualifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )

    @dataclass(kw_only=True)
    class TravelFlightInfo:
        cabin_id: (
            None | FareMasterPricerTravelBoardSearch.TravelFlightInfo.CabinId
        ) = field(
            default=None,
            metadata={
                "name": "cabinId",
                "type": "Element",
            },
        )
        company_identity: list[
            FareMasterPricerTravelBoardSearch.TravelFlightInfo.CompanyIdentity
        ] = field(
            default_factory=list,
            metadata={
                "name": "companyIdentity",
                "type": "Element",
                "max_occurs": 20,
            },
        )
        flight_detail: (
            None
            | FareMasterPricerTravelBoardSearch.TravelFlightInfo.FlightDetail
        ) = field(
            default=None,
            metadata={
                "name": "flightDetail",
                "type": "Element",
            },
        )
        inclusion_detail: list[
            FareMasterPricerTravelBoardSearch.TravelFlightInfo.InclusionDetail
        ] = field(
            default_factory=list,
            metadata={
                "name": "inclusionDetail",
                "type": "Element",
                "max_occurs": 20,
            },
        )
        exclusion_detail: list[
            FareMasterPricerTravelBoardSearch.TravelFlightInfo.ExclusionDetail
        ] = field(
            default_factory=list,
            metadata={
                "name": "exclusionDetail",
                "type": "Element",
                "max_occurs": 20,
            },
        )
        unit_number_detail: list[
            FareMasterPricerTravelBoardSearch.TravelFlightInfo.UnitNumberDetail
        ] = field(
            default_factory=list,
            metadata={
                "name": "unitNumberDetail",
                "type": "Element",
                "max_occurs": 20,
            },
        )

        @dataclass(kw_only=True)
        class CabinId:
            cabin_qualifier: None | str = field(
                default=None,
                metadata={
                    "name": "cabinQualifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 2,
                },
            )
            cabin: list[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 5,
                    "min_length": 0,
                    "max_length": 1,
                },
            )

        @dataclass(kw_only=True)
        class CompanyIdentity:
            carrier_qualifier: str = field(
                metadata={
                    "name": "carrierQualifier",
                    "type": "Element",
                    "required": True,
                    "min_length": 0,
                    "max_length": 1,
                }
            )
            carrier_id: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "carrierId",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 999,
                    "min_length": 2,
                    "max_length": 3,
                },
            )

        @dataclass(kw_only=True)
        class FlightDetail:
            flight_type: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "flightType",
                    "type": "Element",
                    "max_occurs": 9,
                    "min_length": 1,
                    "max_length": 2,
                },
            )

        @dataclass(kw_only=True)
        class InclusionDetail:
            inclusion_identifier: str = field(
                metadata={
                    "name": "inclusionIdentifier",
                    "type": "Element",
                    "required": True,
                    "min_length": 0,
                    "max_length": 1,
                }
            )
            location_id: str = field(
                metadata={
                    "name": "locationId",
                    "type": "Element",
                    "required": True,
                    "min_length": 3,
                    "max_length": 5,
                }
            )
            airport_city_qualifier: None | str = field(
                default=None,
                metadata={
                    "name": "airportCityQualifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 1,
                },
            )

        @dataclass(kw_only=True)
        class ExclusionDetail:
            exclusion_identifier: str = field(
                metadata={
                    "name": "exclusionIdentifier",
                    "type": "Element",
                    "required": True,
                    "min_length": 0,
                    "max_length": 1,
                }
            )
            location_id: str = field(
                metadata={
                    "name": "locationId",
                    "type": "Element",
                    "required": True,
                    "min_length": 3,
                    "max_length": 5,
                }
            )
            airport_city_qualifier: None | str = field(
                default=None,
                metadata={
                    "name": "airportCityQualifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 1,
                },
            )

        @dataclass(kw_only=True)
        class UnitNumberDetail:
            number_of_units: Decimal = field(
                metadata={
                    "name": "numberOfUnits",
                    "type": "Element",
                    "required": True,
                }
            )
            type_of_unit: str = field(
                metadata={
                    "name": "typeOfUnit",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )

    @dataclass(kw_only=True)
    class ValueSearch:
        criteria_name: None | str = field(
            default=None,
            metadata={
                "name": "criteriaName",
                "type": "Element",
                "min_length": 1,
                "max_length": 50,
            },
        )
        criteria_code: None | str = field(
            default=None,
            metadata={
                "name": "criteriaCode",
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
            },
        )
        value: None | str = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 1,
                "max_length": 18,
            },
        )
        criteria_details: list[
            FareMasterPricerTravelBoardSearch.ValueSearch.CriteriaDetails
        ] = field(
            default_factory=list,
            metadata={
                "name": "criteriaDetails",
                "type": "Element",
                "max_occurs": 10,
            },
        )

        @dataclass(kw_only=True)
        class CriteriaDetails:
            type_value: None | str = field(
                default=None,
                metadata={
                    "name": "type",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            value: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 18,
                },
            )
            attribute: list[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                    "min_length": 1,
                    "max_length": 9,
                },
            )

    @dataclass(kw_only=True)
    class Buckets:
        bucket_info: FareMasterPricerTravelBoardSearch.Buckets.BucketInfo = (
            field(
                metadata={
                    "name": "bucketInfo",
                    "type": "Element",
                    "required": True,
                }
            )
        )
        bucket_details: list[
            FareMasterPricerTravelBoardSearch.Buckets.BucketDetails
        ] = field(
            default_factory=list,
            metadata={
                "name": "bucketDetails",
                "type": "Element",
                "max_occurs": 15,
            },
        )

        @dataclass(kw_only=True)
        class BucketInfo:
            number: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            name: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 20,
                },
            )
            completion: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            mode: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            value_ref: None | str = field(
                default=None,
                metadata={
                    "name": "valueRef",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            weight: None | Decimal = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            count: None | Decimal = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            attribute_count: None | Decimal = field(
                default=None,
                metadata={
                    "name": "attributeCount",
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class BucketDetails:
            code: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            type_value: None | str = field(
                default=None,
                metadata={
                    "name": "type",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            attribute: list[
                FareMasterPricerTravelBoardSearch.Buckets.BucketDetails.Attribute
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 10,
                },
            )

            @dataclass(kw_only=True)
            class Attribute:
                requested_sgt: None | str = field(
                    default=None,
                    metadata={
                        "name": "requestedSgt",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                value: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 50,
                        "min_length": 1,
                        "max_length": 20,
                    },
                )

    @dataclass(kw_only=True)
    class Itinerary:
        requested_segment_ref: FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentRef = field(
            metadata={
                "name": "requestedSegmentRef",
                "type": "Element",
                "required": True,
            }
        )
        departure_localization: (
            None
            | FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization
        ) = field(
            default=None,
            metadata={
                "name": "departureLocalization",
                "type": "Element",
            },
        )
        arrival_localization: (
            None
            | FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization
        ) = field(
            default=None,
            metadata={
                "name": "arrivalLocalization",
                "type": "Element",
            },
        )
        time_details: (
            None | FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails
        ) = field(
            default=None,
            metadata={
                "name": "timeDetails",
                "type": "Element",
            },
        )
        flight_info: (
            None | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo
        ) = field(
            default=None,
            metadata={
                "name": "flightInfo",
                "type": "Element",
            },
        )
        family_information: (
            None
            | FareMasterPricerTravelBoardSearch.Itinerary.FamilyInformation
        ) = field(
            default=None,
            metadata={
                "name": "familyInformation",
                "type": "Element",
            },
        )
        value_search: list[
            FareMasterPricerTravelBoardSearch.Itinerary.ValueSearch
        ] = field(
            default_factory=list,
            metadata={
                "name": "valueSearch",
                "type": "Element",
                "max_occurs": 99,
            },
        )
        group_of_flights: list[
            FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights
        ] = field(
            default_factory=list,
            metadata={
                "name": "groupOfFlights",
                "type": "Element",
                "max_occurs": 6,
            },
        )
        flight_info_pnr: list[
            FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr
        ] = field(
            default_factory=list,
            metadata={
                "name": "flightInfoPNR",
                "type": "Element",
                "max_occurs": 4,
            },
        )
        requested_segment_action: (
            None
            | FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentAction
        ) = field(
            default=None,
            metadata={
                "name": "requestedSegmentAction",
                "type": "Element",
            },
        )
        attributes: (
            None | FareMasterPricerTravelBoardSearch.Itinerary.Attributes
        ) = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class RequestedSegmentRef:
            seg_ref: Decimal = field(
                metadata={
                    "name": "segRef",
                    "type": "Element",
                    "required": True,
                }
            )
            location_forcing: list[
                FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentRef.LocationForcing
            ] = field(
                default_factory=list,
                metadata={
                    "name": "locationForcing",
                    "type": "Element",
                    "max_occurs": 2,
                },
            )

            @dataclass(kw_only=True)
            class LocationForcing:
                airport_city_qualifier: str = field(
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 1,
                    }
                )
                segment_number: Decimal = field(
                    metadata={
                        "name": "segmentNumber",
                        "type": "Element",
                        "required": True,
                    }
                )

        @dataclass(kw_only=True)
        class DepartureLocalization:
            departure_point: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.DeparturePoint
            ) = field(
                default=None,
                metadata={
                    "name": "departurePoint",
                    "type": "Element",
                },
            )
            dep_multi_city: list[
                FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.DepMultiCity
            ] = field(
                default_factory=list,
                metadata={
                    "name": "depMultiCity",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            first_pnr_segment_ref: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.FirstPnrSegmentRef
            ) = field(
                default=None,
                metadata={
                    "name": "firstPnrSegmentRef",
                    "type": "Element",
                },
            )
            attribute_details: list[
                FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.AttributeDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "attributeDetails",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class DeparturePoint:
                distance: None | Decimal = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                distance_unit: None | str = field(
                    default=None,
                    metadata={
                        "name": "distanceUnit",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                location_id: None | str = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "min_length": 3,
                        "max_length": 5,
                    },
                )
                airport_city_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )
                latitude: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    },
                )
                longitude: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    },
                )

            @dataclass(kw_only=True)
            class DepMultiCity:
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )

            @dataclass(kw_only=True)
            class FirstPnrSegmentRef:
                pnr_segment_tattoo: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "pnrSegmentTattoo",
                        "type": "Element",
                    },
                )
                pnr_segment_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "pnrSegmentQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )

            @dataclass(kw_only=True)
            class AttributeDetails:
                type_value: None | str = field(
                    default=None,
                    metadata={
                        "name": "type",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 5,
                    },
                )
                value: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 10,
                        "min_length": 1,
                        "max_length": 20,
                    },
                )

        @dataclass(kw_only=True)
        class ArrivalLocalization:
            arrival_point_details: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization.ArrivalPointDetails
            ) = field(
                default=None,
                metadata={
                    "name": "arrivalPointDetails",
                    "type": "Element",
                },
            )
            arrival_multi_city: list[
                FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization.ArrivalMultiCity
            ] = field(
                default_factory=list,
                metadata={
                    "name": "arrivalMultiCity",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            attribute_details: list[
                FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization.AttributeDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "attributeDetails",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class ArrivalPointDetails:
                distance: None | Decimal = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )
                distance_unit: None | str = field(
                    default=None,
                    metadata={
                        "name": "distanceUnit",
                        "type": "Element",
                        "min_length": 0,
                        "max_length": 3,
                    },
                )
                location_id: None | str = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "min_length": 3,
                        "max_length": 5,
                    },
                )
                airport_city_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )
                latitude: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    },
                )
                longitude: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    },
                )

            @dataclass(kw_only=True)
            class ArrivalMultiCity:
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )

            @dataclass(kw_only=True)
            class AttributeDetails:
                type_value: None | str = field(
                    default=None,
                    metadata={
                        "name": "type",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 5,
                    },
                )
                value: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 10,
                        "min_length": 1,
                        "max_length": 20,
                    },
                )

        @dataclass(kw_only=True)
        class TimeDetails:
            first_date_time_detail: FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails.FirstDateTimeDetail = field(
                metadata={
                    "name": "firstDateTimeDetail",
                    "type": "Element",
                    "required": True,
                }
            )
            range_of_date: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails.RangeOfDate
            ) = field(
                default=None,
                metadata={
                    "name": "rangeOfDate",
                    "type": "Element",
                },
            )
            trip_details: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails.TripDetails
            ) = field(
                default=None,
                metadata={
                    "name": "tripDetails",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class FirstDateTimeDetail:
                time_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "timeQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                date: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    },
                )
                time: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 4,
                        "max_length": 4,
                    },
                )
                time_window: None | str = field(
                    default=None,
                    metadata={
                        "name": "timeWindow",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class RangeOfDate:
                range_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "rangeQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                day_interval: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "dayInterval",
                        "type": "Element",
                    },
                )
                time_atdestination: None | str = field(
                    default=None,
                    metadata={
                        "name": "timeAtdestination",
                        "type": "Element",
                        "min_length": 4,
                        "max_length": 4,
                    },
                )

            @dataclass(kw_only=True)
            class TripDetails:
                flexibility_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "flexibilityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                trip_interval: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "tripInterval",
                        "type": "Element",
                    },
                )
                trip_duration: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "tripDuration",
                        "type": "Element",
                    },
                )

        @dataclass(kw_only=True)
        class FlightInfo:
            cabin_id: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.CabinId
            ) = field(
                default=None,
                metadata={
                    "name": "cabinId",
                    "type": "Element",
                },
            )
            company_identity: list[
                FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.CompanyIdentity
            ] = field(
                default_factory=list,
                metadata={
                    "name": "companyIdentity",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            flight_detail: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.FlightDetail
            ) = field(
                default=None,
                metadata={
                    "name": "flightDetail",
                    "type": "Element",
                },
            )
            inclusion_detail: list[
                FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.InclusionDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "inclusionDetail",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            exclusion_detail: list[
                FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.ExclusionDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "exclusionDetail",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            unit_number_detail: list[
                FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.UnitNumberDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "unitNumberDetail",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class CabinId:
                cabin_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "cabinQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 2,
                    },
                )
                cabin: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 5,
                        "min_length": 0,
                        "max_length": 1,
                    },
                )

            @dataclass(kw_only=True)
            class CompanyIdentity:
                carrier_qualifier: str = field(
                    metadata={
                        "name": "carrierQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                carrier_id: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "carrierId",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 99,
                        "min_length": 2,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class FlightDetail:
                flight_type: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "flightType",
                        "type": "Element",
                        "max_occurs": 9,
                        "min_length": 1,
                        "max_length": 2,
                    },
                )

            @dataclass(kw_only=True)
            class InclusionDetail:
                inclusion_identifier: str = field(
                    metadata={
                        "name": "inclusionIdentifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )

            @dataclass(kw_only=True)
            class ExclusionDetail:
                exclusion_identifier: str = field(
                    metadata={
                        "name": "exclusionIdentifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )

            @dataclass(kw_only=True)
            class UnitNumberDetail:
                number_of_units: Decimal = field(
                    metadata={
                        "name": "numberOfUnits",
                        "type": "Element",
                        "required": True,
                    }
                )
                type_of_unit: str = field(
                    metadata={
                        "name": "typeOfUnit",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass(kw_only=True)
        class FamilyInformation:
            commercial_family_details: list[
                FareMasterPricerTravelBoardSearch.Itinerary.FamilyInformation.CommercialFamilyDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "commercialFamilyDetails",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class CommercialFamilyDetails:
                commercial_family: str = field(
                    metadata={
                        "name": "commercialFamily",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 10,
                    }
                )

        @dataclass(kw_only=True)
        class ValueSearch:
            criteria_name: None | str = field(
                default=None,
                metadata={
                    "name": "criteriaName",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 50,
                },
            )
            criteria_code: None | str = field(
                default=None,
                metadata={
                    "name": "criteriaCode",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                },
            )
            value: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 18,
                },
            )
            criteria_details: list[
                FareMasterPricerTravelBoardSearch.Itinerary.ValueSearch.CriteriaDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "criteriaDetails",
                    "type": "Element",
                    "max_occurs": 10,
                },
            )

            @dataclass(kw_only=True)
            class CriteriaDetails:
                type_value: None | str = field(
                    default=None,
                    metadata={
                        "name": "type",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                value: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 18,
                    },
                )
                attribute: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                        "min_length": 1,
                        "max_length": 9,
                    },
                )

        @dataclass(kw_only=True)
        class GroupOfFlights:
            prop_flight_gr_detail: FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PropFlightGrDetail = field(
                metadata={
                    "name": "propFlightGrDetail",
                    "type": "Element",
                    "required": True,
                }
            )
            price_to_beat: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PriceToBeat
            ) = field(
                default=None,
                metadata={
                    "name": "priceToBeat",
                    "type": "Element",
                },
            )
            flight_details: list[
                FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "flightDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 4,
                },
            )

            @dataclass(kw_only=True)
            class PropFlightGrDetail:
                flight_proposal: list[
                    FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PropFlightGrDetail.FlightProposal
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "flightProposal",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 9,
                    },
                )
                flight_characteristic: None | str = field(
                    default=None,
                    metadata={
                        "name": "flightCharacteristic",
                        "type": "Element",
                        "min_length": 0,
                        "max_length": 3,
                    },
                )
                maj_cabin: None | str = field(
                    default=None,
                    metadata={
                        "name": "majCabin",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )

                @dataclass(kw_only=True)
                class FlightProposal:
                    ref: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 6,
                        },
                    )
                    unit_qualifier: None | str = field(
                        default=None,
                        metadata={
                            "name": "unitQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

            @dataclass(kw_only=True)
            class PriceToBeat:
                money_info: FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PriceToBeat.MoneyInfo = field(
                    metadata={
                        "name": "moneyInfo",
                        "type": "Element",
                        "required": True,
                    }
                )
                additional_money_info: list[
                    FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PriceToBeat.AdditionalMoneyInfo
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "additionalMoneyInfo",
                        "type": "Element",
                        "max_occurs": 19,
                    },
                )

                @dataclass(kw_only=True)
                class MoneyInfo:
                    qualifier: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    amount: Decimal = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    currency: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class AdditionalMoneyInfo:
                    qualifier: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    amount: Decimal = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    currency: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    location_id: None | str = field(
                        default=None,
                        metadata={
                            "name": "locationId",
                            "type": "Element",
                            "min_length": 3,
                            "max_length": 3,
                        },
                    )

            @dataclass(kw_only=True)
            class FlightDetails:
                flight_information: FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation = field(
                    metadata={
                        "name": "flightInformation",
                        "type": "Element",
                        "required": True,
                    }
                )
                avl_info: list[
                    FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AvlInfo
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "avlInfo",
                        "type": "Element",
                        "max_occurs": 6,
                    },
                )
                technical_stop: list[
                    FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TechnicalStop
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "technicalStop",
                        "type": "Element",
                        "max_occurs": 5,
                    },
                )
                commercial_agreement: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.CommercialAgreement
                ) = field(
                    default=None,
                    metadata={
                        "name": "commercialAgreement",
                        "type": "Element",
                    },
                )
                add_info: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AddInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "addInfo",
                        "type": "Element",
                    },
                )
                terminal_equipment_details: list[
                    FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "terminalEquipmentDetails",
                        "type": "Element",
                        "max_occurs": 2,
                    },
                )
                reservation_info: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.ReservationInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "reservationInfo",
                        "type": "Element",
                    },
                )
                price_to_beat: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.PriceToBeat
                ) = field(
                    default=None,
                    metadata={
                        "name": "priceToBeat",
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class FlightInformation:
                    product_date_time: FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.ProductDateTime = field(
                        metadata={
                            "name": "productDateTime",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    location: list[
                        FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.Location
                    ] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 2,
                        },
                    )
                    company_id: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.CompanyId
                    ) = field(
                        default=None,
                        metadata={
                            "name": "companyId",
                            "type": "Element",
                        },
                    )
                    flight_ortrain_number: None | str = field(
                        default=None,
                        metadata={
                            "name": "flightOrtrainNumber",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 8,
                        },
                    )
                    product_detail: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.ProductDetail
                    ) = field(
                        default=None,
                        metadata={
                            "name": "productDetail",
                            "type": "Element",
                        },
                    )
                    add_product_detail: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.AddProductDetail
                    ) = field(
                        default=None,
                        metadata={
                            "name": "addProductDetail",
                            "type": "Element",
                        },
                    )
                    attribute_details: list[
                        FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.AttributeDetails
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "attributeDetails",
                            "type": "Element",
                            "max_occurs": 20,
                        },
                    )

                    @dataclass(kw_only=True)
                    class ProductDateTime:
                        date_of_departure: str = field(
                            metadata={
                                "name": "dateOfDeparture",
                                "type": "Element",
                                "required": True,
                                "min_length": 6,
                                "max_length": 6,
                            }
                        )
                        time_of_departure: None | str = field(
                            default=None,
                            metadata={
                                "name": "timeOfDeparture",
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            },
                        )
                        date_of_arrival: None | str = field(
                            default=None,
                            metadata={
                                "name": "dateOfArrival",
                                "type": "Element",
                                "min_length": 6,
                                "max_length": 6,
                            },
                        )
                        time_of_arrival: None | str = field(
                            default=None,
                            metadata={
                                "name": "timeOfArrival",
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            },
                        )
                        date_variation: None | str = field(
                            default=None,
                            metadata={
                                "name": "dateVariation",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )

                    @dataclass(kw_only=True)
                    class Location:
                        location_id: str = field(
                            metadata={
                                "name": "locationId",
                                "type": "Element",
                                "required": True,
                                "min_length": 3,
                                "max_length": 5,
                            }
                        )
                        airport_city_qualifier: None | str = field(
                            default=None,
                            metadata={
                                "name": "airportCityQualifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )
                        terminal: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 5,
                            },
                        )

                    @dataclass(kw_only=True)
                    class CompanyId:
                        marketing_carrier: str = field(
                            metadata={
                                "name": "marketingCarrier",
                                "type": "Element",
                                "required": True,
                                "min_length": 2,
                                "max_length": 3,
                            }
                        )
                        operating_carrier: None | str = field(
                            default=None,
                            metadata={
                                "name": "operatingCarrier",
                                "type": "Element",
                                "min_length": 2,
                                "max_length": 3,
                            },
                        )

                    @dataclass(kw_only=True)
                    class ProductDetail:
                        equipment_type: None | str = field(
                            default=None,
                            metadata={
                                "name": "equipmentType",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        operating_day: None | str = field(
                            default=None,
                            metadata={
                                "name": "operatingDay",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 7,
                            },
                        )
                        tech_stop_number: None | Decimal = field(
                            default=None,
                            metadata={
                                "name": "techStopNumber",
                                "type": "Element",
                            },
                        )
                        location_id: list[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "locationId",
                                "type": "Element",
                                "max_occurs": 3,
                                "min_length": 3,
                                "max_length": 5,
                            },
                        )

                    @dataclass(kw_only=True)
                    class AddProductDetail:
                        last_seat_available: None | str = field(
                            default=None,
                            metadata={
                                "name": "lastSeatAvailable",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )
                        level_of_access: None | str = field(
                            default=None,
                            metadata={
                                "name": "levelOfAccess",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        electronic_ticketing: None | str = field(
                            default=None,
                            metadata={
                                "name": "electronicTicketing",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )
                        operational_suffix: None | str = field(
                            default=None,
                            metadata={
                                "name": "operationalSuffix",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )
                        product_detail_qualifier: None | str = field(
                            default=None,
                            metadata={
                                "name": "productDetailQualifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        flight_characteristic: list[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "flightCharacteristic",
                                "type": "Element",
                                "max_occurs": 9,
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )

                    @dataclass(kw_only=True)
                    class AttributeDetails:
                        attribute_type: str = field(
                            metadata={
                                "name": "attributeType",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 5,
                            }
                        )
                        attribute_description: None | str = field(
                            default=None,
                            metadata={
                                "name": "attributeDescription",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 10,
                            },
                        )

                @dataclass(kw_only=True)
                class AvlInfo:
                    cabin_product: list[
                        FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AvlInfo.CabinProduct
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "cabinProduct",
                            "type": "Element",
                            "max_occurs": 26,
                        },
                    )
                    context_details: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AvlInfo.ContextDetails
                    ) = field(
                        default=None,
                        metadata={
                            "name": "contextDetails",
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class CabinProduct:
                        rbd: str = field(
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        booking_modifier: None | str = field(
                            default=None,
                            metadata={
                                "name": "bookingModifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )
                        cabin: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )
                        avl_status: None | str = field(
                            default=None,
                            metadata={
                                "name": "avlStatus",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )

                    @dataclass(kw_only=True)
                    class ContextDetails:
                        avl: list[str] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 9,
                                "min_length": 1,
                                "max_length": 6,
                            },
                        )

                @dataclass(kw_only=True)
                class TechnicalStop:
                    stop_details: list[
                        FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TechnicalStop.StopDetails
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "stopDetails",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 2,
                        },
                    )

                    @dataclass(kw_only=True)
                    class StopDetails:
                        date_qualifier: None | str = field(
                            default=None,
                            metadata={
                                "name": "dateQualifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        date: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 6,
                                "max_length": 6,
                            },
                        )
                        first_time: None | str = field(
                            default=None,
                            metadata={
                                "name": "firstTime",
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            },
                        )
                        equipement_type: None | str = field(
                            default=None,
                            metadata={
                                "name": "equipementType",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        location_id: None | str = field(
                            default=None,
                            metadata={
                                "name": "locationId",
                                "type": "Element",
                                "min_length": 3,
                                "max_length": 5,
                            },
                        )

                @dataclass(kw_only=True)
                class CommercialAgreement:
                    codeshare_details: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.CommercialAgreement.CodeshareDetails
                    ) = field(
                        default=None,
                        metadata={
                            "name": "codeshareDetails",
                            "type": "Element",
                        },
                    )
                    other_codeshare_details: list[
                        FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.CommercialAgreement.OtherCodeshareDetails
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "otherCodeshareDetails",
                            "type": "Element",
                            "max_occurs": 9,
                        },
                    )

                    @dataclass(kw_only=True)
                    class CodeshareDetails:
                        code_share_type: None | str = field(
                            default=None,
                            metadata={
                                "name": "codeShareType",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )
                        airline_designator: None | str = field(
                            default=None,
                            metadata={
                                "name": "airlineDesignator",
                                "type": "Element",
                                "min_length": 2,
                                "max_length": 3,
                            },
                        )
                        flight_number: None | Decimal = field(
                            default=None,
                            metadata={
                                "name": "flightNumber",
                                "type": "Element",
                            },
                        )

                    @dataclass(kw_only=True)
                    class OtherCodeshareDetails:
                        code_share_type: None | str = field(
                            default=None,
                            metadata={
                                "name": "codeShareType",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )
                        airline_designator: None | str = field(
                            default=None,
                            metadata={
                                "name": "airlineDesignator",
                                "type": "Element",
                                "min_length": 2,
                                "max_length": 3,
                            },
                        )
                        flight_number: None | Decimal = field(
                            default=None,
                            metadata={
                                "name": "flightNumber",
                                "type": "Element",
                            },
                        )

                @dataclass(kw_only=True)
                class AddInfo:
                    status: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 2,
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    date_time_period_details: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AddInfo.DateTimePeriodDetails
                    ) = field(
                        default=None,
                        metadata={
                            "name": "dateTimePeriodDetails",
                            "type": "Element",
                        },
                    )
                    reference_number: None | str = field(
                        default=None,
                        metadata={
                            "name": "referenceNumber",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        },
                    )
                    product_identification: list[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "productIdentification",
                            "type": "Element",
                            "max_occurs": 2,
                            "min_length": 1,
                            "max_length": 35,
                        },
                    )

                    @dataclass(kw_only=True)
                    class DateTimePeriodDetails:
                        qualifier: str = field(
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        value: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 35,
                            },
                        )

                @dataclass(kw_only=True)
                class TerminalEquipmentDetails:
                    leg_details: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.LegDetails
                    ) = field(
                        default=None,
                        metadata={
                            "name": "legDetails",
                            "type": "Element",
                        },
                    )
                    departure_station_info: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.DepartureStationInfo
                    ) = field(
                        default=None,
                        metadata={
                            "name": "departureStationInfo",
                            "type": "Element",
                        },
                    )
                    arrival_station_info: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.ArrivalStationInfo
                    ) = field(
                        default=None,
                        metadata={
                            "name": "arrivalStationInfo",
                            "type": "Element",
                        },
                    )
                    mileage_time_details: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.MileageTimeDetails
                    ) = field(
                        default=None,
                        metadata={
                            "name": "mileageTimeDetails",
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class LegDetails:
                        equipment: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        duration: None | Decimal = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            },
                        )
                        complexing_flight_indicator: None | str = field(
                            default=None,
                            metadata={
                                "name": "complexingFlightIndicator",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            },
                        )

                    @dataclass(kw_only=True)
                    class DepartureStationInfo:
                        terminal: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )

                    @dataclass(kw_only=True)
                    class ArrivalStationInfo:
                        terminal: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )

                    @dataclass(kw_only=True)
                    class MileageTimeDetails:
                        elapsed_ground_time: None | Decimal = field(
                            default=None,
                            metadata={
                                "name": "elapsedGroundTime",
                                "type": "Element",
                            },
                        )

                @dataclass(kw_only=True)
                class ReservationInfo:
                    booking: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )
                    identifier: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )
                    status: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    item_number: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "itemNumber",
                            "type": "Element",
                        },
                    )
                    date_time_details: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.ReservationInfo.DateTimeDetails
                    ) = field(
                        default=None,
                        metadata={
                            "name": "dateTimeDetails",
                            "type": "Element",
                        },
                    )
                    designator: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )
                    movement_type: None | str = field(
                        default=None,
                        metadata={
                            "name": "movementType",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    product_type_details: (
                        None
                        | FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.ReservationInfo.ProductTypeDetails
                    ) = field(
                        default=None,
                        metadata={
                            "name": "productTypeDetails",
                            "type": "Element",
                        },
                    )

                    @dataclass(kw_only=True)
                    class DateTimeDetails:
                        date: str = field(
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 6,
                                "max_length": 6,
                            }
                        )
                        time: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            },
                        )

                    @dataclass(kw_only=True)
                    class ProductTypeDetails:
                        sequence_number: None | str = field(
                            default=None,
                            metadata={
                                "name": "sequenceNumber",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 6,
                            },
                        )
                        availability_context: None | str = field(
                            default=None,
                            metadata={
                                "name": "availabilityContext",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 6,
                            },
                        )

                @dataclass(kw_only=True)
                class PriceToBeat:
                    money_info: FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.PriceToBeat.MoneyInfo = field(
                        metadata={
                            "name": "moneyInfo",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    additional_money_info: list[
                        FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.PriceToBeat.AdditionalMoneyInfo
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "additionalMoneyInfo",
                            "type": "Element",
                            "max_occurs": 19,
                        },
                    )

                    @dataclass(kw_only=True)
                    class MoneyInfo:
                        qualifier: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        amount: Decimal = field(
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        currency: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )

                    @dataclass(kw_only=True)
                    class AdditionalMoneyInfo:
                        qualifier: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        amount: Decimal = field(
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        currency: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        location_id: None | str = field(
                            default=None,
                            metadata={
                                "name": "locationId",
                                "type": "Element",
                                "min_length": 3,
                                "max_length": 3,
                            },
                        )

        @dataclass(kw_only=True)
        class FlightInfoPnr:
            travel_response_details: FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails = field(
                metadata={
                    "name": "travelResponseDetails",
                    "type": "Element",
                    "required": True,
                }
            )
            time_table_date: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate
            ) = field(
                default=None,
                metadata={
                    "name": "timeTableDate",
                    "type": "Element",
                },
            )
            terminal_equipment_details: list[
                FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "terminalEquipmentDetails",
                    "type": "Element",
                    "max_occurs": 2,
                },
            )
            codeshare_data: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.CodeshareData
            ) = field(
                default=None,
                metadata={
                    "name": "codeshareData",
                    "type": "Element",
                },
            )
            disclosure: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.Disclosure
            ) = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            stop_details: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.StopDetails
            ) = field(
                default=None,
                metadata={
                    "name": "stopDetails",
                    "type": "Element",
                },
            )
            traffic_restriction_data: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TrafficRestrictionData
            ) = field(
                default=None,
                metadata={
                    "name": "trafficRestrictionData",
                    "type": "Element",
                },
            )
            reservation_info: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.ReservationInfo
            ) = field(
                default=None,
                metadata={
                    "name": "reservationInfo",
                    "type": "Element",
                },
            )
            incidental_stop_info: list[
                FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo
            ] = field(
                default_factory=list,
                metadata={
                    "name": "incidentalStopInfo",
                    "type": "Element",
                    "max_occurs": 8,
                },
            )

            @dataclass(kw_only=True)
            class TravelResponseDetails:
                flight_date: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.FlightDate
                ) = field(
                    default=None,
                    metadata={
                        "name": "flightDate",
                        "type": "Element",
                    },
                )
                board_point_details: FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.BoardPointDetails = field(
                    metadata={
                        "name": "boardPointDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                offpoint_details: FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.OffpointDetails = field(
                    metadata={
                        "name": "offpointDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                company_details: FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.CompanyDetails = field(
                    metadata={
                        "name": "companyDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                flight_identification: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.FlightIdentification
                ) = field(
                    default=None,
                    metadata={
                        "name": "flightIdentification",
                        "type": "Element",
                    },
                )
                flight_type_details: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.FlightTypeDetails
                ) = field(
                    default=None,
                    metadata={
                        "name": "flightTypeDetails",
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class FlightDate:
                    departure_date: None | str = field(
                        default=None,
                        metadata={
                            "name": "departureDate",
                            "type": "Element",
                            "min_length": 8,
                            "max_length": 8,
                        },
                    )
                    departure_time: None | str = field(
                        default=None,
                        metadata={
                            "name": "departureTime",
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        },
                    )
                    arrival_date: None | str = field(
                        default=None,
                        metadata={
                            "name": "arrivalDate",
                            "type": "Element",
                            "min_length": 8,
                            "max_length": 8,
                        },
                    )
                    arrival_time: None | str = field(
                        default=None,
                        metadata={
                            "name": "arrivalTime",
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        },
                    )
                    date_variation: None | str = field(
                        default=None,
                        metadata={
                            "name": "dateVariation",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )

                @dataclass(kw_only=True)
                class BoardPointDetails:
                    true_location_id: str = field(
                        metadata={
                            "name": "trueLocationId",
                            "type": "Element",
                            "required": True,
                            "min_length": 3,
                            "max_length": 3,
                        }
                    )

                @dataclass(kw_only=True)
                class OffpointDetails:
                    true_location_id: str = field(
                        metadata={
                            "name": "trueLocationId",
                            "type": "Element",
                            "required": True,
                            "min_length": 3,
                            "max_length": 3,
                        }
                    )

                @dataclass(kw_only=True)
                class CompanyDetails:
                    marketing_company: str = field(
                        metadata={
                            "name": "marketingCompany",
                            "type": "Element",
                            "required": True,
                            "min_length": 2,
                            "max_length": 3,
                        }
                    )

                @dataclass(kw_only=True)
                class FlightIdentification:
                    flight_number: Decimal = field(
                        metadata={
                            "name": "flightNumber",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    operational_suffix: None | str = field(
                        default=None,
                        metadata={
                            "name": "operationalSuffix",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )

                @dataclass(kw_only=True)
                class FlightTypeDetails:
                    flight_indicator: list[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "flightIndicator",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 5,
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

            @dataclass(kw_only=True)
            class TimeTableDate:
                begin_date_time: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate.BeginDateTime
                ) = field(
                    default=None,
                    metadata={
                        "name": "beginDateTime",
                        "type": "Element",
                    },
                )
                end_date_time: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate.EndDateTime
                ) = field(
                    default=None,
                    metadata={
                        "name": "endDateTime",
                        "type": "Element",
                    },
                )
                frequency: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate.Frequency
                ) = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class BeginDateTime:
                    year: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        },
                    )
                    month: None | Decimal = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    day: None | Decimal = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class EndDateTime:
                    year: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        },
                    )
                    month: None | Decimal = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    day: None | Decimal = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )

                @dataclass(kw_only=True)
                class Frequency:
                    qualifier: str = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    value: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 7,
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )

            @dataclass(kw_only=True)
            class TerminalEquipmentDetails:
                leg_details: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.LegDetails
                ) = field(
                    default=None,
                    metadata={
                        "name": "legDetails",
                        "type": "Element",
                    },
                )
                departure_station_info: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.DepartureStationInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "departureStationInfo",
                        "type": "Element",
                    },
                )
                arrival_station_info: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.ArrivalStationInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "arrivalStationInfo",
                        "type": "Element",
                    },
                )
                mileage_time_details: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.MileageTimeDetails
                ) = field(
                    default=None,
                    metadata={
                        "name": "mileageTimeDetails",
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class LegDetails:
                    equipment: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    duration: None | Decimal = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        },
                    )
                    complexing_flight_indicator: None | str = field(
                        default=None,
                        metadata={
                            "name": "complexingFlightIndicator",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )

                @dataclass(kw_only=True)
                class DepartureStationInfo:
                    terminal: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class ArrivalStationInfo:
                    terminal: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class MileageTimeDetails:
                    elapsed_ground_time: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "elapsedGroundTime",
                            "type": "Element",
                        },
                    )

            @dataclass(kw_only=True)
            class CodeshareData:
                codeshare_details: FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.CodeshareData.CodeshareDetails = field(
                    metadata={
                        "name": "codeshareDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                other_codeshare_details: list[
                    FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.CodeshareData.OtherCodeshareDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "otherCodeshareDetails",
                        "type": "Element",
                        "max_occurs": 8,
                    },
                )

                @dataclass(kw_only=True)
                class CodeshareDetails:
                    transport_stage_qualifier: str = field(
                        metadata={
                            "name": "transportStageQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )
                    airline_designator: None | str = field(
                        default=None,
                        metadata={
                            "name": "airlineDesignator",
                            "type": "Element",
                            "min_length": 2,
                            "max_length": 3,
                        },
                    )
                    flight_number: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "flightNumber",
                            "type": "Element",
                        },
                    )
                    operational_suffix: None | str = field(
                        default=None,
                        metadata={
                            "name": "operationalSuffix",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )

                @dataclass(kw_only=True)
                class OtherCodeshareDetails:
                    transport_stage_qualifier: str = field(
                        metadata={
                            "name": "transportStageQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )
                    airline_designator: None | str = field(
                        default=None,
                        metadata={
                            "name": "airlineDesignator",
                            "type": "Element",
                            "min_length": 2,
                            "max_length": 3,
                        },
                    )
                    flight_number: None | Decimal = field(
                        default=None,
                        metadata={
                            "name": "flightNumber",
                            "type": "Element",
                        },
                    )
                    operational_suffix: None | str = field(
                        default=None,
                        metadata={
                            "name": "operationalSuffix",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )

            @dataclass(kw_only=True)
            class Disclosure:
                free_text_details: FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.Disclosure.FreeTextDetails = field(
                    metadata={
                        "name": "freeTextDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                free_text: str = field(
                    metadata={
                        "name": "freeText",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 70,
                    }
                )

                @dataclass(kw_only=True)
                class FreeTextDetails:
                    text_subject_qualifier: str = field(
                        metadata={
                            "name": "textSubjectQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    information_type: None | str = field(
                        default=None,
                        metadata={
                            "name": "informationType",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 4,
                        },
                    )
                    source: str = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    encoding: str = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

            @dataclass(kw_only=True)
            class StopDetails:
                routing_details: list[
                    FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.StopDetails.RoutingDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "routingDetails",
                        "type": "Element",
                        "max_occurs": 9,
                    },
                )

                @dataclass(kw_only=True)
                class RoutingDetails:
                    station: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 3,
                            "max_length": 3,
                        },
                    )

            @dataclass(kw_only=True)
            class TrafficRestrictionData:
                traffic_restriction_details: list[
                    FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TrafficRestrictionData.TrafficRestrictionDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "trafficRestrictionDetails",
                        "type": "Element",
                        "max_occurs": 5,
                    },
                )

                @dataclass(kw_only=True)
                class TrafficRestrictionDetails:
                    code: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

            @dataclass(kw_only=True)
            class ReservationInfo:
                booking: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )
                identifier: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )
                status: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                item_number: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "itemNumber",
                        "type": "Element",
                    },
                )
                date_time_details: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.ReservationInfo.DateTimeDetails
                ) = field(
                    default=None,
                    metadata={
                        "name": "dateTimeDetails",
                        "type": "Element",
                    },
                )
                designator: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )
                movement_type: None | str = field(
                    default=None,
                    metadata={
                        "name": "movementType",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                product_type_details: (
                    None
                    | FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.ReservationInfo.ProductTypeDetails
                ) = field(
                    default=None,
                    metadata={
                        "name": "productTypeDetails",
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class DateTimeDetails:
                    date: str = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 6,
                            "max_length": 6,
                        }
                    )
                    time: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        },
                    )

                @dataclass(kw_only=True)
                class ProductTypeDetails:
                    sequence_number: None | str = field(
                        default=None,
                        metadata={
                            "name": "sequenceNumber",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 6,
                        },
                    )
                    availability_context: None | str = field(
                        default=None,
                        metadata={
                            "name": "availabilityContext",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 6,
                        },
                    )

            @dataclass(kw_only=True)
            class IncidentalStopInfo:
                date_time_info: FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo.DateTimeInfo = field(
                    metadata={
                        "name": "dateTimeInfo",
                        "type": "Element",
                        "required": True,
                    }
                )

                @dataclass(kw_only=True)
                class DateTimeInfo:
                    date_time_details: list[
                        FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo.DateTimeInfo.DateTimeDetails
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "dateTimeDetails",
                            "type": "Element",
                            "max_occurs": 2,
                        },
                    )

                    @dataclass(kw_only=True)
                    class DateTimeDetails:
                        qualifier: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        date: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 6,
                                "max_length": 6,
                            },
                        )
                        time: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            },
                        )
                        qualifier2: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        reserved1: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        reserved2: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 3,
                                "max_length": 5,
                            },
                        )

        @dataclass(kw_only=True)
        class RequestedSegmentAction:
            action_request_code: str = field(
                metadata={
                    "name": "actionRequestCode",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            product_details: (
                None
                | FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentAction.ProductDetails
            ) = field(
                default=None,
                metadata={
                    "name": "productDetails",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class ProductDetails:
                flight_number: str = field(
                    metadata={
                        "name": "flightNumber",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                booking_class: None | str = field(
                    default=None,
                    metadata={
                        "name": "bookingClass",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 2,
                    },
                )
                operational_suffix: None | str = field(
                    default=None,
                    metadata={
                        "name": "operationalSuffix",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                modifier: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 3,
                        "min_length": 1,
                        "max_length": 7,
                    },
                )

        @dataclass(kw_only=True)
        class Attributes:
            attribute_details: list[
                FareMasterPricerTravelBoardSearch.Itinerary.Attributes.AttributeDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "attributeDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 9,
                },
            )

            @dataclass(kw_only=True)
            class AttributeDetails:
                attribute_type: str = field(
                    metadata={
                        "name": "attributeType",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                attribute_description: None | str = field(
                    default=None,
                    metadata={
                        "name": "attributeDescription",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 50,
                    },
                )

    @dataclass(kw_only=True)
    class TicketChangeInfo:
        ticket_number_details: FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketNumberDetails = field(
            metadata={
                "name": "ticketNumberDetails",
                "type": "Element",
                "required": True,
            }
        )
        ticket_requested_segments: list[
            FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments
        ] = field(
            default_factory=list,
            metadata={
                "name": "ticketRequestedSegments",
                "type": "Element",
                "max_occurs": 6,
            },
        )

        @dataclass(kw_only=True)
        class TicketNumberDetails:
            document_details: list[
                FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketNumberDetails.DocumentDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "documentDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 99,
                },
            )

            @dataclass(kw_only=True)
            class DocumentDetails:
                number: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 35,
                    },
                )

        @dataclass(kw_only=True)
        class TicketRequestedSegments:
            action_identification: FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ActionIdentification = field(
                metadata={
                    "name": "actionIdentification",
                    "type": "Element",
                    "required": True,
                }
            )
            connect_point_details: (
                None
                | FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ConnectPointDetails
            ) = field(
                default=None,
                metadata={
                    "name": "connectPointDetails",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class ActionIdentification:
                action_request_code: str = field(
                    metadata={
                        "name": "actionRequestCode",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                product_details: (
                    None
                    | FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ActionIdentification.ProductDetails
                ) = field(
                    default=None,
                    metadata={
                        "name": "productDetails",
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class ProductDetails:
                    flight_number: str = field(
                        metadata={
                            "name": "flightNumber",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 5,
                        }
                    )
                    booking_class: None | str = field(
                        default=None,
                        metadata={
                            "name": "bookingClass",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 2,
                        },
                    )
                    operational_suffix: None | str = field(
                        default=None,
                        metadata={
                            "name": "operationalSuffix",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    modifier: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 3,
                            "min_length": 1,
                            "max_length": 7,
                        },
                    )

            @dataclass(kw_only=True)
            class ConnectPointDetails:
                connection_details: list[
                    FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ConnectPointDetails.ConnectionDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "connectionDetails",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 17,
                    },
                )

                @dataclass(kw_only=True)
                class ConnectionDetails:
                    location: str = field(
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

    @dataclass(kw_only=True)
    class CombinationFareFamilies:
        item_ffcnumber: FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ItemFfcnumber = field(
            metadata={
                "name": "itemFFCNumber",
                "type": "Element",
                "required": True,
            }
        )
        nb_of_units: (
            None
            | FareMasterPricerTravelBoardSearch.CombinationFareFamilies.NbOfUnits
        ) = field(
            default=None,
            metadata={
                "name": "nbOfUnits",
                "type": "Element",
            },
        )
        reference_info: list[
            FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ReferenceInfo
        ] = field(
            default_factory=list,
            metadata={
                "name": "referenceInfo",
                "type": "Element",
                "max_occurs": 6,
            },
        )

        @dataclass(kw_only=True)
        class ItemFfcnumber:
            item_number_id: FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ItemFfcnumber.ItemNumberId = field(
                metadata={
                    "name": "itemNumberId",
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass(kw_only=True)
            class ItemNumberId:
                number: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 4,
                    },
                )
                type_value: None | str = field(
                    default=None,
                    metadata={
                        "name": "type",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                qualifier: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                responsible_agency: None | str = field(
                    default=None,
                    metadata={
                        "name": "responsibleAgency",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

        @dataclass(kw_only=True)
        class NbOfUnits:
            unit_number_detail: list[
                FareMasterPricerTravelBoardSearch.CombinationFareFamilies.NbOfUnits.UnitNumberDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "unitNumberDetail",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class UnitNumberDetail:
                number_of_units: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "numberOfUnits",
                        "type": "Element",
                    },
                )
                type_of_unit: str = field(
                    metadata={
                        "name": "typeOfUnit",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass(kw_only=True)
        class ReferenceInfo:
            referencing_detail: list[
                FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ReferenceInfo.ReferencingDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "referencingDetail",
                    "type": "Element",
                    "max_occurs": 9,
                },
            )

            @dataclass(kw_only=True)
            class ReferencingDetail:
                ref_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "refQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                ref_number: Decimal = field(
                    metadata={
                        "name": "refNumber",
                        "type": "Element",
                        "required": True,
                    }
                )

    @dataclass(kw_only=True)
    class FeeOption:
        fee_type_info: FareMasterPricerTravelBoardSearch.FeeOption.FeeTypeInfo = field(
            metadata={
                "name": "feeTypeInfo",
                "type": "Element",
                "required": True,
            }
        )
        rate_tax: (
            None | FareMasterPricerTravelBoardSearch.FeeOption.RateTax
        ) = field(
            default=None,
            metadata={
                "name": "rateTax",
                "type": "Element",
            },
        )
        fee_details: list[
            FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails
        ] = field(
            default_factory=list,
            metadata={
                "name": "feeDetails",
                "type": "Element",
                "max_occurs": 99,
            },
        )

        @dataclass(kw_only=True)
        class FeeTypeInfo:
            carrier_fee_details: FareMasterPricerTravelBoardSearch.FeeOption.FeeTypeInfo.CarrierFeeDetails = field(
                metadata={
                    "name": "carrierFeeDetails",
                    "type": "Element",
                    "required": True,
                }
            )
            other_selection_details: list[
                FareMasterPricerTravelBoardSearch.FeeOption.FeeTypeInfo.OtherSelectionDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "otherSelectionDetails",
                    "type": "Element",
                    "max_occurs": 98,
                },
            )

            @dataclass(kw_only=True)
            class CarrierFeeDetails:
                type_value: str = field(
                    metadata={
                        "name": "type",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                option_information: None | str = field(
                    default=None,
                    metadata={
                        "name": "optionInformation",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class OtherSelectionDetails:
                option: str = field(
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                option_information: None | str = field(
                    default=None,
                    metadata={
                        "name": "optionInformation",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 35,
                    },
                )

        @dataclass(kw_only=True)
        class RateTax:
            monetary_details: list[
                FareMasterPricerTravelBoardSearch.FeeOption.RateTax.MonetaryDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "monetaryDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class MonetaryDetails:
                type_qualifier: str = field(
                    metadata={
                        "name": "typeQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                amount: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    },
                )
                currency: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

        @dataclass(kw_only=True)
        class FeeDetails:
            fee_info: FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeInfo = field(
                metadata={
                    "name": "feeInfo",
                    "type": "Element",
                    "required": True,
                }
            )
            associated_amounts: (
                None
                | FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.AssociatedAmounts
            ) = field(
                default=None,
                metadata={
                    "name": "associatedAmounts",
                    "type": "Element",
                },
            )
            fee_description_grp: (
                None
                | FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp
            ) = field(
                default=None,
                metadata={
                    "name": "feeDescriptionGrp",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class FeeInfo:
                data_type_information: FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeInfo.DataTypeInformation = field(
                    metadata={
                        "name": "dataTypeInformation",
                        "type": "Element",
                        "required": True,
                    }
                )
                data_information: list[
                    FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeInfo.DataInformation
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "dataInformation",
                        "type": "Element",
                        "max_occurs": 99,
                    },
                )

                @dataclass(kw_only=True)
                class DataTypeInformation:
                    sub_type: str = field(
                        metadata={
                            "name": "subType",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    option: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class DataInformation:
                    indicator: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

            @dataclass(kw_only=True)
            class AssociatedAmounts:
                monetary_details: list[
                    FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.AssociatedAmounts.MonetaryDetails
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "monetaryDetails",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 20,
                    },
                )

                @dataclass(kw_only=True)
                class MonetaryDetails:
                    type_qualifier: str = field(
                        metadata={
                            "name": "typeQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    amount: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 12,
                        },
                    )
                    currency: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    location: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )

            @dataclass(kw_only=True)
            class FeeDescriptionGrp:
                item_number_info: FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ItemNumberInfo = field(
                    metadata={
                        "name": "itemNumberInfo",
                        "type": "Element",
                        "required": True,
                    }
                )
                service_attributes_info: (
                    None
                    | FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceAttributesInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "serviceAttributesInfo",
                        "type": "Element",
                    },
                )
                service_description_info: (
                    None
                    | FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceDescriptionInfo
                ) = field(
                    default=None,
                    metadata={
                        "name": "serviceDescriptionInfo",
                        "type": "Element",
                    },
                )

                @dataclass(kw_only=True)
                class ItemNumberInfo:
                    item_number_details: FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ItemNumberInfo.ItemNumberDetails = field(
                        metadata={
                            "name": "itemNumberDetails",
                            "type": "Element",
                            "required": True,
                        }
                    )

                    @dataclass(kw_only=True)
                    class ItemNumberDetails:
                        number: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 4,
                            },
                        )
                        type_value: None | str = field(
                            default=None,
                            metadata={
                                "name": "type",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        qualifier: None | str = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        responsible_agency: None | str = field(
                            default=None,
                            metadata={
                                "name": "responsibleAgency",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )

                @dataclass(kw_only=True)
                class ServiceAttributesInfo:
                    attribute_qualifier: None | str = field(
                        default=None,
                        metadata={
                            "name": "attributeQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        },
                    )
                    attribute_details: list[
                        FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceAttributesInfo.AttributeDetails
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "attributeDetails",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 99,
                        },
                    )

                    @dataclass(kw_only=True)
                    class AttributeDetails:
                        attribute_type: str = field(
                            metadata={
                                "name": "attributeType",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 25,
                            }
                        )
                        attribute_description: None | str = field(
                            default=None,
                            metadata={
                                "name": "attributeDescription",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 256,
                            },
                        )

                @dataclass(kw_only=True)
                class ServiceDescriptionInfo:
                    service_requirements_info: FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceDescriptionInfo.ServiceRequirementsInfo = field(
                        metadata={
                            "name": "serviceRequirementsInfo",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    seat_details: list[
                        FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceDescriptionInfo.SeatDetails
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "seatDetails",
                            "type": "Element",
                            "max_occurs": 999,
                        },
                    )

                    @dataclass(kw_only=True)
                    class ServiceRequirementsInfo:
                        service_classification: str = field(
                            metadata={
                                "name": "serviceClassification",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 4,
                            }
                        )
                        service_status: None | str = field(
                            default=None,
                            metadata={
                                "name": "serviceStatus",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        service_number_of_instances: None | Decimal = field(
                            default=None,
                            metadata={
                                "name": "serviceNumberOfInstances",
                                "type": "Element",
                            },
                        )
                        service_marketing_carrier: None | str = field(
                            default=None,
                            metadata={
                                "name": "serviceMarketingCarrier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        service_group: None | str = field(
                            default=None,
                            metadata={
                                "name": "serviceGroup",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        service_sub_group: None | str = field(
                            default=None,
                            metadata={
                                "name": "serviceSubGroup",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            },
                        )
                        service_free_text: list[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "serviceFreeText",
                                "type": "Element",
                                "max_occurs": 99,
                                "min_length": 1,
                                "max_length": 70,
                            },
                        )

                    @dataclass(kw_only=True)
                    class SeatDetails:
                        seat_characteristics: list[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "seatCharacteristics",
                                "type": "Element",
                                "max_occurs": 5,
                                "min_length": 1,
                                "max_length": 2,
                            },
                        )

    @dataclass(kw_only=True)
    class OfficeIdDetails:
        office_id_information: FareMasterPricerTravelBoardSearch.OfficeIdDetails.OfficeIdInformation = field(
            metadata={
                "name": "officeIdInformation",
                "type": "Element",
                "required": True,
            }
        )
        nb_of_units: (
            None | FareMasterPricerTravelBoardSearch.OfficeIdDetails.NbOfUnits
        ) = field(
            default=None,
            metadata={
                "name": "nbOfUnits",
                "type": "Element",
            },
        )
        uid_option: (
            None | FareMasterPricerTravelBoardSearch.OfficeIdDetails.UidOption
        ) = field(
            default=None,
            metadata={
                "name": "uidOption",
                "type": "Element",
            },
        )
        pricing_tick_info: (
            None
            | FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo
        ) = field(
            default=None,
            metadata={
                "name": "pricingTickInfo",
                "type": "Element",
            },
        )
        corporate_fare_info: (
            None
            | FareMasterPricerTravelBoardSearch.OfficeIdDetails.CorporateFareInfo
        ) = field(
            default=None,
            metadata={
                "name": "corporateFareInfo",
                "type": "Element",
            },
        )
        travel_flight_info: (
            None
            | FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo
        ) = field(
            default=None,
            metadata={
                "name": "travelFlightInfo",
                "type": "Element",
            },
        )
        airline_distribution_details: list[
            FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails
        ] = field(
            default_factory=list,
            metadata={
                "name": "airlineDistributionDetails",
                "type": "Element",
                "max_occurs": 6,
            },
        )

        @dataclass(kw_only=True)
        class OfficeIdInformation:
            office_identification: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.OfficeIdInformation.OfficeIdentification
            ) = field(
                default=None,
                metadata={
                    "name": "officeIdentification",
                    "type": "Element",
                },
            )
            office_type: None | str = field(
                default=None,
                metadata={
                    "name": "officeType",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 1,
                },
            )
            office_code: None | str = field(
                default=None,
                metadata={
                    "name": "officeCode",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 30,
                },
            )

            @dataclass(kw_only=True)
            class OfficeIdentification:
                office_name: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "officeName",
                        "type": "Element",
                    },
                )
                agent_signin: None | str = field(
                    default=None,
                    metadata={
                        "name": "agentSignin",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 9,
                    },
                )
                confidential_office: None | str = field(
                    default=None,
                    metadata={
                        "name": "confidentialOffice",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 9,
                    },
                )
                other_office: None | str = field(
                    default=None,
                    metadata={
                        "name": "otherOffice",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 9,
                    },
                )

        @dataclass(kw_only=True)
        class NbOfUnits:
            unit_number_detail: list[
                FareMasterPricerTravelBoardSearch.OfficeIdDetails.NbOfUnits.UnitNumberDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "unitNumberDetail",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class UnitNumberDetail:
                number_of_units: None | Decimal = field(
                    default=None,
                    metadata={
                        "name": "numberOfUnits",
                        "type": "Element",
                    },
                )
                type_of_unit: str = field(
                    metadata={
                        "name": "typeOfUnit",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass(kw_only=True)
        class UidOption:
            attribute_details: list[
                FareMasterPricerTravelBoardSearch.OfficeIdDetails.UidOption.AttributeDetails
            ] = field(
                default_factory=list,
                metadata={
                    "name": "attributeDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                },
            )

            @dataclass(kw_only=True)
            class AttributeDetails:
                attribute_type: str = field(
                    metadata={
                        "name": "attributeType",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                attribute_description: None | str = field(
                    default=None,
                    metadata={
                        "name": "attributeDescription",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20,
                    },
                )

        @dataclass(kw_only=True)
        class PricingTickInfo:
            pricing_ticketing: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.PricingTicketing
            ) = field(
                default=None,
                metadata={
                    "name": "pricingTicketing",
                    "type": "Element",
                },
            )
            ticketing_date: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.TicketingDate
            ) = field(
                default=None,
                metadata={
                    "name": "ticketingDate",
                    "type": "Element",
                },
            )
            company_id: None | object = field(
                default=None,
                metadata={
                    "name": "companyId",
                    "type": "Element",
                },
            )
            selling_point: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.SellingPoint
            ) = field(
                default=None,
                metadata={
                    "name": "sellingPoint",
                    "type": "Element",
                },
            )
            ticketing_point: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.TicketingPoint
            ) = field(
                default=None,
                metadata={
                    "name": "ticketingPoint",
                    "type": "Element",
                },
            )
            journey_origin_point: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.JourneyOriginPoint
            ) = field(
                default=None,
                metadata={
                    "name": "journeyOriginPoint",
                    "type": "Element",
                },
            )
            corporate_id: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.CorporateId
            ) = field(
                default=None,
                metadata={
                    "name": "corporateId",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class PricingTicketing:
                price_type: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "priceType",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 50,
                        "min_length": 0,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class TicketingDate:
                date: str = field(
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 6,
                        "max_length": 6,
                    }
                )
                rtc_date: None | str = field(
                    default=None,
                    metadata={
                        "name": "rtcDate",
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    },
                )

            @dataclass(kw_only=True)
            class SellingPoint:
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class TicketingPoint:
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class JourneyOriginPoint:
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: None | str = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class CorporateId:
                arc_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "arcNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    },
                )
                ersp_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "erspNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    },
                )
                iata_number: None | str = field(
                    default=None,
                    metadata={
                        "name": "iataNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    },
                )

        @dataclass(kw_only=True)
        class CorporateFareInfo:
            corporate_fare_identifiers: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.CorporateFareInfo.CorporateFareIdentifiers
            ) = field(
                default=None,
                metadata={
                    "name": "corporateFareIdentifiers",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class CorporateFareIdentifiers:
                fare_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "fareQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    },
                )
                identify_number: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "identifyNumber",
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 35,
                    },
                )

        @dataclass(kw_only=True)
        class TravelFlightInfo:
            cabin_id: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.CabinId
            ) = field(
                default=None,
                metadata={
                    "name": "cabinId",
                    "type": "Element",
                },
            )
            company_identity: list[
                FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.CompanyIdentity
            ] = field(
                default_factory=list,
                metadata={
                    "name": "companyIdentity",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            flight_detail: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.FlightDetail
            ) = field(
                default=None,
                metadata={
                    "name": "flightDetail",
                    "type": "Element",
                },
            )
            inclusion_detail: list[
                FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.InclusionDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "inclusionDetail",
                    "type": "Element",
                    "max_occurs": 20,
                },
            )
            exclusion_detail: list[
                FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.ExclusionDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "exclusionDetail",
                    "type": "Element",
                    "max_occurs": 2,
                },
            )
            unit_number_detail: list[
                FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.UnitNumberDetail
            ] = field(
                default_factory=list,
                metadata={
                    "name": "unitNumberDetail",
                    "type": "Element",
                    "max_occurs": 9,
                },
            )

            @dataclass(kw_only=True)
            class CabinId:
                cabin_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "cabinQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 2,
                    },
                )
                cabin: list[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 3,
                        "min_length": 0,
                        "max_length": 1,
                    },
                )

            @dataclass(kw_only=True)
            class CompanyIdentity:
                carrier_qualifier: str = field(
                    metadata={
                        "name": "carrierQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                carrier_id: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "carrierId",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 99,
                        "min_length": 2,
                        "max_length": 3,
                    },
                )

            @dataclass(kw_only=True)
            class FlightDetail:
                flight_type: list[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "flightType",
                        "type": "Element",
                        "max_occurs": 9,
                        "min_length": 1,
                        "max_length": 2,
                    },
                )

            @dataclass(kw_only=True)
            class InclusionDetail:
                inclusion_identifier: str = field(
                    metadata={
                        "name": "inclusionIdentifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )

            @dataclass(kw_only=True)
            class ExclusionDetail:
                exclusion_identifier: str = field(
                    metadata={
                        "name": "exclusionIdentifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                location_id: str = field(
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: None | str = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    },
                )

            @dataclass(kw_only=True)
            class UnitNumberDetail:
                number_of_units: Decimal = field(
                    metadata={
                        "name": "numberOfUnits",
                        "type": "Element",
                        "required": True,
                    }
                )
                type_of_unit: str = field(
                    metadata={
                        "name": "typeOfUnit",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass(kw_only=True)
        class AirlineDistributionDetails:
            requested_segment_ref: FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.RequestedSegmentRef = field(
                metadata={
                    "name": "requestedSegmentRef",
                    "type": "Element",
                    "required": True,
                }
            )
            flight_info: (
                None
                | FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo
            ) = field(
                default=None,
                metadata={
                    "name": "flightInfo",
                    "type": "Element",
                },
            )

            @dataclass(kw_only=True)
            class RequestedSegmentRef:
                seg_ref: Decimal = field(
                    metadata={
                        "name": "segRef",
                        "type": "Element",
                        "required": True,
                    }
                )
                location_forcing: list[
                    FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.RequestedSegmentRef.LocationForcing
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "locationForcing",
                        "type": "Element",
                        "max_occurs": 2,
                    },
                )

                @dataclass(kw_only=True)
                class LocationForcing:
                    airport_city_qualifier: str = field(
                        metadata={
                            "name": "airportCityQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )
                    segment_number: Decimal = field(
                        metadata={
                            "name": "segmentNumber",
                            "type": "Element",
                            "required": True,
                        }
                    )

            @dataclass(kw_only=True)
            class FlightInfo:
                cabin_id: (
                    None
                    | FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.CabinId
                ) = field(
                    default=None,
                    metadata={
                        "name": "cabinId",
                        "type": "Element",
                    },
                )
                company_identity: list[
                    FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.CompanyIdentity
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "companyIdentity",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )
                flight_detail: (
                    None
                    | FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.FlightDetail
                ) = field(
                    default=None,
                    metadata={
                        "name": "flightDetail",
                        "type": "Element",
                    },
                )
                inclusion_detail: list[
                    FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.InclusionDetail
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "inclusionDetail",
                        "type": "Element",
                        "max_occurs": 20,
                    },
                )
                exclusion_detail: list[
                    FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.ExclusionDetail
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "exclusionDetail",
                        "type": "Element",
                        "max_occurs": 2,
                    },
                )
                unit_number_detail: list[
                    FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.UnitNumberDetail
                ] = field(
                    default_factory=list,
                    metadata={
                        "name": "unitNumberDetail",
                        "type": "Element",
                        "max_occurs": 9,
                    },
                )

                @dataclass(kw_only=True)
                class CabinId:
                    cabin_qualifier: None | str = field(
                        default=None,
                        metadata={
                            "name": "cabinQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 2,
                        },
                    )
                    cabin: list[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 3,
                            "min_length": 0,
                            "max_length": 1,
                        },
                    )

                @dataclass(kw_only=True)
                class CompanyIdentity:
                    carrier_qualifier: str = field(
                        metadata={
                            "name": "carrierQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 0,
                            "max_length": 1,
                        }
                    )
                    carrier_id: list[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "carrierId",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 99,
                            "min_length": 2,
                            "max_length": 3,
                        },
                    )

                @dataclass(kw_only=True)
                class FlightDetail:
                    flight_type: list[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "flightType",
                            "type": "Element",
                            "max_occurs": 9,
                            "min_length": 1,
                            "max_length": 2,
                        },
                    )

                @dataclass(kw_only=True)
                class InclusionDetail:
                    inclusion_identifier: str = field(
                        metadata={
                            "name": "inclusionIdentifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 0,
                            "max_length": 1,
                        }
                    )
                    location_id: str = field(
                        metadata={
                            "name": "locationId",
                            "type": "Element",
                            "required": True,
                            "min_length": 3,
                            "max_length": 5,
                        }
                    )
                    airport_city_qualifier: None | str = field(
                        default=None,
                        metadata={
                            "name": "airportCityQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )

                @dataclass(kw_only=True)
                class ExclusionDetail:
                    exclusion_identifier: str = field(
                        metadata={
                            "name": "exclusionIdentifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 0,
                            "max_length": 1,
                        }
                    )
                    location_id: str = field(
                        metadata={
                            "name": "locationId",
                            "type": "Element",
                            "required": True,
                            "min_length": 3,
                            "max_length": 5,
                        }
                    )
                    airport_city_qualifier: None | str = field(
                        default=None,
                        metadata={
                            "name": "airportCityQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        },
                    )

                @dataclass(kw_only=True)
                class UnitNumberDetail:
                    number_of_units: Decimal = field(
                        metadata={
                            "name": "numberOfUnits",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    type_of_unit: str = field(
                        metadata={
                            "name": "typeOfUnit",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
