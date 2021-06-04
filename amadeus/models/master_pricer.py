from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://xml.amadeus.com/FMPTBQ_15_3_1A"


@dataclass
class FareMasterPricerTravelBoardSearch:
    class Meta:
        name = "Fare_MasterPricerTravelBoardSearch"
        namespace = "http://xml.amadeus.com/FMPTBQ_15_3_1A"

    number_of_unit: Optional["FareMasterPricerTravelBoardSearch.NumberOfUnit"] = field(
        default=None,
        metadata={
            "name": "numberOfUnit",
            "type": "Element",
        }
    )
    global_options: Optional["FareMasterPricerTravelBoardSearch.GlobalOptions"] = field(
        default=None,
        metadata={
            "name": "globalOptions",
            "type": "Element",
        }
    )
    pax_reference: List["FareMasterPricerTravelBoardSearch.PaxReference"] = field(
        default_factory=list,
        metadata={
            "name": "paxReference",
            "type": "Element",
            "max_occurs": 6,
        }
    )
    customer_ref: Optional["FareMasterPricerTravelBoardSearch.CustomerRef"] = field(
        default=None,
        metadata={
            "name": "customerRef",
            "type": "Element",
        }
    )
    form_of_payment_by_passenger: List["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger"] = field(
        default_factory=list,
        metadata={
            "name": "formOfPaymentByPassenger",
            "type": "Element",
            "max_occurs": 60,
        }
    )
    solution_family: List["FareMasterPricerTravelBoardSearch.SolutionFamily"] = field(
        default_factory=list,
        metadata={
            "name": "solutionFamily",
            "type": "Element",
            "max_occurs": 20,
        }
    )
    passenger_info_grp: List["FareMasterPricerTravelBoardSearch.PassengerInfoGrp"] = field(
        default_factory=list,
        metadata={
            "name": "passengerInfoGrp",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    fare_families: List["FareMasterPricerTravelBoardSearch.FareFamilies"] = field(
        default_factory=list,
        metadata={
            "name": "fareFamilies",
            "type": "Element",
            "max_occurs": 20,
        }
    )
    fare_options: Optional["FareMasterPricerTravelBoardSearch.FareOptions"] = field(
        default=None,
        metadata={
            "name": "fareOptions",
            "type": "Element",
        }
    )
    price_to_beat: Optional["FareMasterPricerTravelBoardSearch.PriceToBeat"] = field(
        default=None,
        metadata={
            "name": "priceToBeat",
            "type": "Element",
        }
    )
    tax_info: List["FareMasterPricerTravelBoardSearch.TaxInfo"] = field(
        default_factory=list,
        metadata={
            "name": "taxInfo",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    travel_flight_info: Optional["FareMasterPricerTravelBoardSearch.TravelFlightInfo"] = field(
        default=None,
        metadata={
            "name": "travelFlightInfo",
            "type": "Element",
        }
    )
    value_search: List["FareMasterPricerTravelBoardSearch.ValueSearch"] = field(
        default_factory=list,
        metadata={
            "name": "valueSearch",
            "type": "Element",
            "max_occurs": 99,
        }
    )
    buckets: List["FareMasterPricerTravelBoardSearch.Buckets"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        }
    )
    itinerary: List["FareMasterPricerTravelBoardSearch.Itinerary"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 18,
        }
    )
    ticket_change_info: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo"] = field(
        default=None,
        metadata={
            "name": "ticketChangeInfo",
            "type": "Element",
        }
    )
    combination_fare_families: List["FareMasterPricerTravelBoardSearch.CombinationFareFamilies"] = field(
        default_factory=list,
        metadata={
            "name": "combinationFareFamilies",
            "type": "Element",
            "max_occurs": 2000,
        }
    )
    fee_option: List["FareMasterPricerTravelBoardSearch.FeeOption"] = field(
        default_factory=list,
        metadata={
            "name": "feeOption",
            "type": "Element",
            "max_occurs": 9,
        }
    )
    office_id_details: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails"] = field(
        default_factory=list,
        metadata={
            "name": "officeIdDetails",
            "type": "Element",
            "max_occurs": 20,
        }
    )

    @dataclass
    class NumberOfUnit:
        unit_number_detail: List["FareMasterPricerTravelBoardSearch.NumberOfUnit.UnitNumberDetail"] = field(
            default_factory=list,
            metadata={
                "name": "unitNumberDetail",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 20,
            }
        )

        @dataclass
        class UnitNumberDetail:
            number_of_units: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "numberOfUnits",
                    "type": "Element",
                    "required": True,
                }
            )
            type_of_unit: Optional[str] = field(
                default=None,
                metadata={
                    "name": "typeOfUnit",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )

    @dataclass
    class GlobalOptions:
        selection_details: List["FareMasterPricerTravelBoardSearch.GlobalOptions.SelectionDetails"] = field(
            default_factory=list,
            metadata={
                "name": "selectionDetails",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 10,
            }
        )

        @dataclass
        class SelectionDetails:
            option: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            option_information: Optional[str] = field(
                default=None,
                metadata={
                    "name": "optionInformation",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                }
            )

    @dataclass
    class PaxReference:
        ptc: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 3,
                "min_length": 1,
                "max_length": 6,
            }
        )
        traveller: List["FareMasterPricerTravelBoardSearch.PaxReference.Traveller"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 9,
            }
        )

        @dataclass
        class Traveller:
            ref: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            infant_indicator: Optional[str] = field(
                default=None,
                metadata={
                    "name": "infantIndicator",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 1,
                }
            )

    @dataclass
    class CustomerRef:
        customer_references: List["FareMasterPricerTravelBoardSearch.CustomerRef.CustomerReferences"] = field(
            default_factory=list,
            metadata={
                "name": "customerReferences",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 20,
            }
        )

        @dataclass
        class CustomerReferences:
            reference_qualifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "referenceQualifier",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            reference_number: Optional[str] = field(
                default=None,
                metadata={
                    "name": "referenceNumber",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                }
            )
            reference_party_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "referencePartyName",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                }
            )
            traveller_reference_nbr: Optional[str] = field(
                default=None,
                metadata={
                    "name": "travellerReferenceNbr",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                }
            )

    @dataclass
    class FormOfPaymentByPassenger:
        form_of_payment_details: Optional["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.FormOfPaymentDetails"] = field(
            default=None,
            metadata={
                "name": "formOfPaymentDetails",
                "type": "Element",
                "required": True,
            }
        )
        passenger_fee_reference: Optional["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.PassengerFeeReference"] = field(
            default=None,
            metadata={
                "name": "passengerFeeReference",
                "type": "Element",
            }
        )

        @dataclass
        class FormOfPaymentDetails:
            form_of_payment_details: List["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.FormOfPaymentDetails.FormOfPaymentDetailsInner"] = field(
                default_factory=list,
                metadata={
                    "name": "formOfPaymentDetails",
                    "type": "Element",
                    "max_occurs": 9,
                }
            )

            @dataclass
            class FormOfPaymentDetailsInner:
                type: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                charged_amount: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "chargedAmount",
                        "type": "Element",
                    }
                )
                credit_card_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "creditCardNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20,
                    }
                )

        @dataclass
        class PassengerFeeReference:
            passenger_fee_ref_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "passengerFeeRefType",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            passenger_fee_ref_number: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "passengerFeeRefNumber",
                    "type": "Element",
                }
            )
            other_characteristics: Optional["FareMasterPricerTravelBoardSearch.FormOfPaymentByPassenger.PassengerFeeReference.OtherCharacteristics"] = field(
                default=None,
                metadata={
                    "name": "otherCharacteristics",
                    "type": "Element",
                }
            )

            @dataclass
            class OtherCharacteristics:
                passenger_fee_ref_qualif: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "passengerFeeRefQualif",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

    @dataclass
    class SolutionFamily:
        value_qualifier: Optional[str] = field(
            default=None,
            metadata={
                "name": "valueQualifier",
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
            }
        )
        value: Optional[Decimal] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        fare_details: Optional["FareMasterPricerTravelBoardSearch.SolutionFamily.FareDetails"] = field(
            default=None,
            metadata={
                "name": "fareDetails",
                "type": "Element",
            }
        )
        identity_number: Optional[str] = field(
            default=None,
            metadata={
                "name": "identityNumber",
                "type": "Element",
                "min_length": 1,
                "max_length": 35,
            }
        )
        fare_type_grouping: Optional["FareMasterPricerTravelBoardSearch.SolutionFamily.FareTypeGrouping"] = field(
            default=None,
            metadata={
                "name": "fareTypeGrouping",
                "type": "Element",
            }
        )
        rate_category: Optional[str] = field(
            default=None,
            metadata={
                "name": "rateCategory",
                "type": "Element",
                "min_length": 1,
                "max_length": 35,
            }
        )

        @dataclass
        class FareDetails:
            qualifier: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            rate: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            country: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            fare_category: Optional[str] = field(
                default=None,
                metadata={
                    "name": "fareCategory",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )

        @dataclass
        class FareTypeGrouping:
            pricing_group: Optional[str] = field(
                default=None,
                metadata={
                    "name": "pricingGroup",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                }
            )

    @dataclass
    class PassengerInfoGrp:
        passenger_reference: Optional["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PassengerReference"] = field(
            default=None,
            metadata={
                "name": "passengerReference",
                "type": "Element",
                "required": True,
            }
        )
        psg_details_info: List["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo"] = field(
            default_factory=list,
            metadata={
                "name": "psgDetailsInfo",
                "type": "Element",
                "max_occurs": 2,
            }
        )

        @dataclass
        class PassengerReference:
            segment_control_details: List["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PassengerReference.SegmentControlDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "segmentControlDetails",
                    "type": "Element",
                    "max_occurs": 9,
                }
            )

            @dataclass
            class SegmentControlDetails:
                quantity: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )

        @dataclass
        class PsgDetailsInfo:
            discount_ptc: Optional["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo.DiscountPtc"] = field(
                default=None,
                metadata={
                    "name": "discountPtc",
                    "type": "Element",
                    "required": True,
                }
            )
            flequent_flyer_details: Optional["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo.FlequentFlyerDetails"] = field(
                default=None,
                metadata={
                    "name": "flequentFlyerDetails",
                    "type": "Element",
                }
            )

            @dataclass
            class DiscountPtc:
                value_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "valueQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                value: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )

            @dataclass
            class FlequentFlyerDetails:
                frequent_traveller_details: List["FareMasterPricerTravelBoardSearch.PassengerInfoGrp.PsgDetailsInfo.FlequentFlyerDetails.FrequentTravellerDetails"] = field(
                    default_factory=list,
                    metadata={
                        "name": "frequentTravellerDetails",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 99,
                    }
                )

                @dataclass
                class FrequentTravellerDetails:
                    carrier: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        }
                    )
                    number: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 28,
                        }
                    )
                    customer_reference: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "customerReference",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 10,
                        }
                    )
                    status: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    tier_level: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "tierLevel",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        }
                    )
                    priority_code: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "priorityCode",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 12,
                        }
                    )
                    tier_description: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "tierDescription",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        }
                    )
                    company_code: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "companyCode",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        }
                    )
                    customer_value: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "customerValue",
                            "type": "Element",
                        }
                    )
                    type: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

    @dataclass
    class FareFamilies:
        family_information: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyInformation"] = field(
            default=None,
            metadata={
                "name": "familyInformation",
                "type": "Element",
                "required": True,
            }
        )
        family_criteria: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria"] = field(
            default=None,
            metadata={
                "name": "familyCriteria",
                "type": "Element",
            }
        )
        fare_family_segment: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment"] = field(
            default_factory=list,
            metadata={
                "name": "fareFamilySegment",
                "type": "Element",
                "max_occurs": 6,
            }
        )
        other_possible_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria"] = field(
            default_factory=list,
            metadata={
                "name": "otherPossibleCriteria",
                "type": "Element",
                "max_occurs": 20,
            }
        )

        @dataclass
        class FamilyInformation:
            ref_number: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "refNumber",
                    "type": "Element",
                }
            )
            fare_familyname: Optional[str] = field(
                default=None,
                metadata={
                    "name": "fareFamilyname",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                }
            )
            hierarchy: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            commercial_family_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyInformation.CommercialFamilyDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "commercialFamilyDetails",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )

            @dataclass
            class CommercialFamilyDetails:
                commercial_family: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "commercialFamily",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 10,
                    }
                )

        @dataclass
        class FamilyCriteria:
            carrier_id: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "carrierId",
                    "type": "Element",
                    "max_occurs": 20,
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            rdb: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 20,
                    "min_length": 1,
                    "max_length": 2,
                }
            )
            fare_family_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.FareFamilyInfo"] = field(
                default=None,
                metadata={
                    "name": "fareFamilyInfo",
                    "type": "Element",
                }
            )
            fare_product_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.FareProductDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "fareProductDetail",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            corporate_info: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.CorporateInfo"] = field(
                default_factory=list,
                metadata={
                    "name": "corporateInfo",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            cabin_product: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.CabinProduct"] = field(
                default_factory=list,
                metadata={
                    "name": "cabinProduct",
                    "type": "Element",
                    "max_occurs": 6,
                }
            )
            cabin_processing_identifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cabinProcessingIdentifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            date_time_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.DateTimeDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "dateTimeDetails",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            other_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.FamilyCriteria.OtherCriteria"] = field(
                default_factory=list,
                metadata={
                    "name": "otherCriteria",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )

            @dataclass
            class FareFamilyInfo:
                fare_family_qual: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "fareFamilyQual",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 9,
                        "min_length": 0,
                        "max_length": 3,
                    }
                )

            @dataclass
            class FareProductDetail:
                fare_basis: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "fareBasis",
                        "type": "Element",
                        "min_length": 0,
                        "max_length": 18,
                    }
                )
                fare_type: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "fareType",
                        "type": "Element",
                        "max_occurs": 3,
                        "min_length": 0,
                        "max_length": 3,
                    }
                )

            @dataclass
            class CorporateInfo:
                corporate_number_identifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "corporateNumberIdentifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    }
                )
                corporate_name: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "corporateName",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20,
                    }
                )

            @dataclass
            class CabinProduct:
                cabin_designator: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cabinDesignator",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

            @dataclass
            class DateTimeDetails:
                date: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 6,
                        "max_length": 6,
                    }
                )
                other_date: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "otherDate",
                        "type": "Element",
                    }
                )

            @dataclass
            class OtherCriteria:
                name: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                value: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 10,
                        "min_length": 1,
                        "max_length": 20,
                    }
                )

        @dataclass
        class FareFamilySegment:
            reference_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.ReferenceInfo"] = field(
                default=None,
                metadata={
                    "name": "referenceInfo",
                    "type": "Element",
                    "required": True,
                }
            )
            family_criteria: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria"] = field(
                default=None,
                metadata={
                    "name": "familyCriteria",
                    "type": "Element",
                }
            )

            @dataclass
            class ReferenceInfo:
                referencing_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.ReferenceInfo.ReferencingDetail"] = field(
                    default_factory=list,
                    metadata={
                        "name": "referencingDetail",
                        "type": "Element",
                        "max_occurs": 9,
                    }
                )

                @dataclass
                class ReferencingDetail:
                    ref_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "refQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    ref_number: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "refNumber",
                            "type": "Element",
                            "required": True,
                        }
                    )

            @dataclass
            class FamilyCriteria:
                carrier_id: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "carrierId",
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                rdb: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 2,
                    }
                )
                fare_family_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.FareFamilyInfo"] = field(
                    default=None,
                    metadata={
                        "name": "fareFamilyInfo",
                        "type": "Element",
                    }
                )
                fare_product_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.FareProductDetail"] = field(
                    default_factory=list,
                    metadata={
                        "name": "fareProductDetail",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )
                corporate_info: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.CorporateInfo"] = field(
                    default_factory=list,
                    metadata={
                        "name": "corporateInfo",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )
                cabin_product: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.CabinProduct"] = field(
                    default_factory=list,
                    metadata={
                        "name": "cabinProduct",
                        "type": "Element",
                        "max_occurs": 6,
                    }
                )
                cabin_processing_identifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cabinProcessingIdentifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                date_time_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.DateTimeDetails"] = field(
                    default_factory=list,
                    metadata={
                        "name": "dateTimeDetails",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )
                other_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.FareFamilySegment.FamilyCriteria.OtherCriteria"] = field(
                    default_factory=list,
                    metadata={
                        "name": "otherCriteria",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )

                @dataclass
                class FareFamilyInfo:
                    fare_family_qual: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareFamilyQual",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 9,
                            "min_length": 0,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class FareProductDetail:
                    fare_basis: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "fareBasis",
                            "type": "Element",
                            "min_length": 0,
                            "max_length": 18,
                        }
                    )
                    fare_type: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareType",
                            "type": "Element",
                            "max_occurs": 3,
                            "min_length": 0,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class CorporateInfo:
                    corporate_number_identifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "corporateNumberIdentifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 12,
                        }
                    )
                    corporate_name: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "corporateName",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 20,
                        }
                    )

                @dataclass
                class CabinProduct:
                    cabin_designator: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cabinDesignator",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass
                class DateTimeDetails:
                    date: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 6,
                            "max_length": 6,
                        }
                    )
                    other_date: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "otherDate",
                            "type": "Element",
                        }
                    )

                @dataclass
                class OtherCriteria:
                    name: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 5,
                        }
                    )
                    value: List[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 10,
                            "min_length": 1,
                            "max_length": 20,
                        }
                    )

        @dataclass
        class OtherPossibleCriteria:
            logical_link: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.LogicalLink"] = field(
                default=None,
                metadata={
                    "name": "logicalLink",
                    "type": "Element",
                    "required": True,
                }
            )
            family_criteria: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria"] = field(
                default=None,
                metadata={
                    "name": "familyCriteria",
                    "type": "Element",
                }
            )
            fare_family_segment: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment"] = field(
                default_factory=list,
                metadata={
                    "name": "fareFamilySegment",
                    "type": "Element",
                    "max_occurs": 6,
                }
            )

            @dataclass
            class LogicalLink:
                boolean_expression: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.LogicalLink.BooleanExpression"] = field(
                    default=None,
                    metadata={
                        "name": "booleanExpression",
                        "type": "Element",
                        "required": True,
                    }
                )

                @dataclass
                class BooleanExpression:
                    code_operator: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "codeOperator",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

            @dataclass
            class FamilyCriteria:
                carrier_id: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "carrierId",
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                rdb: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 2,
                    }
                )
                fare_family_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.FareFamilyInfo"] = field(
                    default=None,
                    metadata={
                        "name": "fareFamilyInfo",
                        "type": "Element",
                    }
                )
                fare_product_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.FareProductDetail"] = field(
                    default_factory=list,
                    metadata={
                        "name": "fareProductDetail",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )
                corporate_info: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.CorporateInfo"] = field(
                    default_factory=list,
                    metadata={
                        "name": "corporateInfo",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )
                cabin_product: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.CabinProduct"] = field(
                    default_factory=list,
                    metadata={
                        "name": "cabinProduct",
                        "type": "Element",
                        "max_occurs": 6,
                    }
                )
                cabin_processing_identifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cabinProcessingIdentifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                date_time_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.DateTimeDetails"] = field(
                    default_factory=list,
                    metadata={
                        "name": "dateTimeDetails",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )
                other_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FamilyCriteria.OtherCriteria"] = field(
                    default_factory=list,
                    metadata={
                        "name": "otherCriteria",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )

                @dataclass
                class FareFamilyInfo:
                    fare_family_qual: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareFamilyQual",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 9,
                            "min_length": 0,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class FareProductDetail:
                    fare_basis: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "fareBasis",
                            "type": "Element",
                            "min_length": 0,
                            "max_length": 18,
                        }
                    )
                    fare_type: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareType",
                            "type": "Element",
                            "max_occurs": 3,
                            "min_length": 0,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class CorporateInfo:
                    corporate_number_identifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "corporateNumberIdentifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 12,
                        }
                    )
                    corporate_name: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "corporateName",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 20,
                        }
                    )

                @dataclass
                class CabinProduct:
                    cabin_designator: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cabinDesignator",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass
                class DateTimeDetails:
                    date: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 6,
                            "max_length": 6,
                        }
                    )
                    other_date: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "otherDate",
                            "type": "Element",
                        }
                    )

                @dataclass
                class OtherCriteria:
                    name: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 5,
                        }
                    )
                    value: List[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 10,
                            "min_length": 1,
                            "max_length": 20,
                        }
                    )

            @dataclass
            class FareFamilySegment:
                reference_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.ReferenceInfo"] = field(
                    default=None,
                    metadata={
                        "name": "referenceInfo",
                        "type": "Element",
                        "required": True,
                    }
                )
                family_criteria: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria"] = field(
                    default=None,
                    metadata={
                        "name": "familyCriteria",
                        "type": "Element",
                    }
                )

                @dataclass
                class ReferenceInfo:
                    referencing_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.ReferenceInfo.ReferencingDetail"] = field(
                        default_factory=list,
                        metadata={
                            "name": "referencingDetail",
                            "type": "Element",
                            "max_occurs": 9,
                        }
                    )

                    @dataclass
                    class ReferencingDetail:
                        ref_qualifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "refQualifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        ref_number: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "name": "refNumber",
                                "type": "Element",
                                "required": True,
                            }
                        )

                @dataclass
                class FamilyCriteria:
                    carrier_id: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "carrierId",
                            "type": "Element",
                            "max_occurs": 20,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    rdb: List[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 20,
                            "min_length": 1,
                            "max_length": 2,
                        }
                    )
                    fare_family_info: Optional["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.FareFamilyInfo"] = field(
                        default=None,
                        metadata={
                            "name": "fareFamilyInfo",
                            "type": "Element",
                        }
                    )
                    fare_product_detail: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.FareProductDetail"] = field(
                        default_factory=list,
                        metadata={
                            "name": "fareProductDetail",
                            "type": "Element",
                            "max_occurs": 20,
                        }
                    )
                    corporate_info: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.CorporateInfo"] = field(
                        default_factory=list,
                        metadata={
                            "name": "corporateInfo",
                            "type": "Element",
                            "max_occurs": 20,
                        }
                    )
                    cabin_product: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.CabinProduct"] = field(
                        default_factory=list,
                        metadata={
                            "name": "cabinProduct",
                            "type": "Element",
                            "max_occurs": 6,
                        }
                    )
                    cabin_processing_identifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cabinProcessingIdentifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    date_time_details: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.DateTimeDetails"] = field(
                        default_factory=list,
                        metadata={
                            "name": "dateTimeDetails",
                            "type": "Element",
                            "max_occurs": 20,
                        }
                    )
                    other_criteria: List["FareMasterPricerTravelBoardSearch.FareFamilies.OtherPossibleCriteria.FareFamilySegment.FamilyCriteria.OtherCriteria"] = field(
                        default_factory=list,
                        metadata={
                            "name": "otherCriteria",
                            "type": "Element",
                            "max_occurs": 20,
                        }
                    )

                    @dataclass
                    class FareFamilyInfo:
                        fare_family_qual: List[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "fareFamilyQual",
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 9,
                                "min_length": 0,
                                "max_length": 3,
                            }
                        )

                    @dataclass
                    class FareProductDetail:
                        fare_basis: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "fareBasis",
                                "type": "Element",
                                "min_length": 0,
                                "max_length": 18,
                            }
                        )
                        fare_type: List[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "fareType",
                                "type": "Element",
                                "max_occurs": 3,
                                "min_length": 0,
                                "max_length": 3,
                            }
                        )

                    @dataclass
                    class CorporateInfo:
                        corporate_number_identifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "corporateNumberIdentifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 12,
                            }
                        )
                        corporate_name: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "corporateName",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 20,
                            }
                        )

                    @dataclass
                    class CabinProduct:
                        cabin_designator: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "cabinDesignator",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )

                    @dataclass
                    class DateTimeDetails:
                        date: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 6,
                                "max_length": 6,
                            }
                        )
                        other_date: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "name": "otherDate",
                                "type": "Element",
                            }
                        )

                    @dataclass
                    class OtherCriteria:
                        name: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 5,
                            }
                        )
                        value: List[str] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "max_occurs": 10,
                                "min_length": 1,
                                "max_length": 20,
                            }
                        )

    @dataclass
    class FareOptions:
        pricing_tick_info: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo"] = field(
            default=None,
            metadata={
                "name": "pricingTickInfo",
                "type": "Element",
                "required": True,
            }
        )
        corporate: Optional["FareMasterPricerTravelBoardSearch.FareOptions.Corporate"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        ticketing_price_scheme: Optional["FareMasterPricerTravelBoardSearch.FareOptions.TicketingPriceScheme"] = field(
            default=None,
            metadata={
                "name": "ticketingPriceScheme",
                "type": "Element",
            }
        )
        fee_id_description: Optional["FareMasterPricerTravelBoardSearch.FareOptions.FeeIdDescription"] = field(
            default=None,
            metadata={
                "name": "feeIdDescription",
                "type": "Element",
            }
        )
        conversion_rate: Optional["FareMasterPricerTravelBoardSearch.FareOptions.ConversionRate"] = field(
            default=None,
            metadata={
                "name": "conversionRate",
                "type": "Element",
            }
        )
        form_of_payment: Optional["FareMasterPricerTravelBoardSearch.FareOptions.FormOfPayment"] = field(
            default=None,
            metadata={
                "name": "formOfPayment",
                "type": "Element",
            }
        )
        frequent_traveller_info: Optional["FareMasterPricerTravelBoardSearch.FareOptions.FrequentTravellerInfo"] = field(
            default=None,
            metadata={
                "name": "frequentTravellerInfo",
                "type": "Element",
            }
        )
        monetary_cabin_info: Optional["FareMasterPricerTravelBoardSearch.FareOptions.MonetaryCabinInfo"] = field(
            default=None,
            metadata={
                "name": "monetaryCabinInfo",
                "type": "Element",
            }
        )

        @dataclass
        class PricingTickInfo:
            pricing_ticketing: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.PricingTicketing"] = field(
                default=None,
                metadata={
                    "name": "pricingTicketing",
                    "type": "Element",
                }
            )
            ticketing_date: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.TicketingDate"] = field(
                default=None,
                metadata={
                    "name": "ticketingDate",
                    "type": "Element",
                }
            )
            company_id: Optional[object] = field(
                default=None,
                metadata={
                    "name": "companyId",
                    "type": "Element",
                }
            )
            selling_point: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.SellingPoint"] = field(
                default=None,
                metadata={
                    "name": "sellingPoint",
                    "type": "Element",
                }
            )
            ticketing_point: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.TicketingPoint"] = field(
                default=None,
                metadata={
                    "name": "ticketingPoint",
                    "type": "Element",
                }
            )
            journey_origin_point: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.JourneyOriginPoint"] = field(
                default=None,
                metadata={
                    "name": "journeyOriginPoint",
                    "type": "Element",
                }
            )
            corporate_id: Optional["FareMasterPricerTravelBoardSearch.FareOptions.PricingTickInfo.CorporateId"] = field(
                default=None,
                metadata={
                    "name": "corporateId",
                    "type": "Element",
                }
            )

            @dataclass
            class PricingTicketing:
                price_type: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "priceType",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 50,
                        "min_length": 0,
                        "max_length": 3,
                    }
                )

            @dataclass
            class TicketingDate:
                date: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 6,
                        "max_length": 6,
                    }
                )
                rtc_date: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "rtcDate",
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    }
                )

            @dataclass
            class SellingPoint:
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

            @dataclass
            class TicketingPoint:
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

            @dataclass
            class JourneyOriginPoint:
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

            @dataclass
            class CorporateId:
                arc_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "arcNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    }
                )
                ersp_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "erspNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    }
                )
                iata_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "iataNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    }
                )

        @dataclass
        class Corporate:
            corporate_id: List["FareMasterPricerTravelBoardSearch.FareOptions.Corporate.CorporateId"] = field(
                default_factory=list,
                metadata={
                    "name": "corporateId",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )

            @dataclass
            class CorporateId:
                corporate_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "corporateQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 3,
                    }
                )
                identity: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 9,
                        "min_length": 1,
                        "max_length": 20,
                    }
                )

        @dataclass
        class TicketingPriceScheme:
            reference_number: Optional[str] = field(
                default=None,
                metadata={
                    "name": "referenceNumber",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 35,
                }
            )
            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 35,
                }
            )
            status: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            description: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 250,
                }
            )

        @dataclass
        class FeeIdDescription:
            fee_id: List["FareMasterPricerTravelBoardSearch.FareOptions.FeeIdDescription.FeeId"] = field(
                default_factory=list,
                metadata={
                    "name": "feeId",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )

            @dataclass
            class FeeId:
                fee_type: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "feeType",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                fee_id_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "feeIdNumber",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 50,
                    }
                )

        @dataclass
        class ConversionRate:
            conversion_rate_detail: List["FareMasterPricerTravelBoardSearch.FareOptions.ConversionRate.ConversionRateDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "conversionRateDetail",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 2,
                }
            )

            @dataclass
            class ConversionRateDetail:
                conversion_type: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "conversionType",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                currency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass
        class FormOfPayment:
            form_of_payment_details: List["FareMasterPricerTravelBoardSearch.FareOptions.FormOfPayment.FormOfPaymentDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "formOfPaymentDetails",
                    "type": "Element",
                    "max_occurs": 9,
                }
            )

            @dataclass
            class FormOfPaymentDetails:
                type: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                charged_amount: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "chargedAmount",
                        "type": "Element",
                    }
                )
                credit_card_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "creditCardNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20,
                    }
                )

        @dataclass
        class FrequentTravellerInfo:
            frequent_traveller_details: List["FareMasterPricerTravelBoardSearch.FareOptions.FrequentTravellerInfo.FrequentTravellerDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "frequentTravellerDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 99,
                }
            )

            @dataclass
            class FrequentTravellerDetails:
                carrier: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                number: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 25,
                    }
                )
                customer_reference: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "customerReference",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 10,
                    }
                )
                tier_level: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "tierLevel",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 35,
                    }
                )
                priority_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "priorityCode",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    }
                )
                tier_description: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "tierDescription",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 35,
                    }
                )
                type: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass
        class MonetaryCabinInfo:
            money_and_cabin_info: List["FareMasterPricerTravelBoardSearch.FareOptions.MonetaryCabinInfo.MoneyAndCabinInfo"] = field(
                default_factory=list,
                metadata={
                    "name": "moneyAndCabinInfo",
                    "type": "Element",
                    "max_occurs": 99,
                }
            )

            @dataclass
            class MoneyAndCabinInfo:
                amount_type: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "amountType",
                        "type": "Element",
                        "min_length": 0,
                        "max_length": 3,
                    }
                )
                amount: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                    }
                )
                currency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                cabin_class_designator: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "cabinClassDesignator",
                        "type": "Element",
                        "max_occurs": 9,
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

    @dataclass
    class PriceToBeat:
        money_info: Optional["FareMasterPricerTravelBoardSearch.PriceToBeat.MoneyInfo"] = field(
            default=None,
            metadata={
                "name": "moneyInfo",
                "type": "Element",
                "required": True,
            }
        )
        additional_money_info: List["FareMasterPricerTravelBoardSearch.PriceToBeat.AdditionalMoneyInfo"] = field(
            default_factory=list,
            metadata={
                "name": "additionalMoneyInfo",
                "type": "Element",
                "max_occurs": 19,
            }
        )

        @dataclass
        class MoneyInfo:
            qualifier: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            amount: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            currency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )

        @dataclass
        class AdditionalMoneyInfo:
            qualifier: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            amount: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            currency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            location_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "locationId",
                    "type": "Element",
                    "min_length": 3,
                    "max_length": 3,
                }
            )

    @dataclass
    class TaxInfo:
        withhold_tax_surcharge: Optional[str] = field(
            default=None,
            metadata={
                "name": "withholdTaxSurcharge",
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
            }
        )
        tax_detail: List["FareMasterPricerTravelBoardSearch.TaxInfo.TaxDetail"] = field(
            default_factory=list,
            metadata={
                "name": "taxDetail",
                "type": "Element",
                "max_occurs": 99,
            }
        )

        @dataclass
        class TaxDetail:
            rate: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 18,
                }
            )
            country: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            currency: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            amount_qualifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "amountQualifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )

    @dataclass
    class TravelFlightInfo:
        cabin_id: Optional["FareMasterPricerTravelBoardSearch.TravelFlightInfo.CabinId"] = field(
            default=None,
            metadata={
                "name": "cabinId",
                "type": "Element",
            }
        )
        company_identity: List["FareMasterPricerTravelBoardSearch.TravelFlightInfo.CompanyIdentity"] = field(
            default_factory=list,
            metadata={
                "name": "companyIdentity",
                "type": "Element",
                "max_occurs": 20,
            }
        )
        flight_detail: Optional["FareMasterPricerTravelBoardSearch.TravelFlightInfo.FlightDetail"] = field(
            default=None,
            metadata={
                "name": "flightDetail",
                "type": "Element",
            }
        )
        inclusion_detail: List["FareMasterPricerTravelBoardSearch.TravelFlightInfo.InclusionDetail"] = field(
            default_factory=list,
            metadata={
                "name": "inclusionDetail",
                "type": "Element",
                "max_occurs": 20,
            }
        )
        exclusion_detail: List["FareMasterPricerTravelBoardSearch.TravelFlightInfo.ExclusionDetail"] = field(
            default_factory=list,
            metadata={
                "name": "exclusionDetail",
                "type": "Element",
                "max_occurs": 20,
            }
        )
        unit_number_detail: List["FareMasterPricerTravelBoardSearch.TravelFlightInfo.UnitNumberDetail"] = field(
            default_factory=list,
            metadata={
                "name": "unitNumberDetail",
                "type": "Element",
                "max_occurs": 20,
            }
        )

        @dataclass
        class CabinId:
            cabin_qualifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cabinQualifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 2,
                }
            )
            cabin: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 5,
                    "min_length": 0,
                    "max_length": 1,
                }
            )

        @dataclass
        class CompanyIdentity:
            carrier_qualifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "carrierQualifier",
                    "type": "Element",
                    "required": True,
                    "min_length": 0,
                    "max_length": 1,
                }
            )
            carrier_id: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "carrierId",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 999,
                    "min_length": 2,
                    "max_length": 3,
                }
            )

        @dataclass
        class FlightDetail:
            flight_type: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "flightType",
                    "type": "Element",
                    "max_occurs": 9,
                    "min_length": 1,
                    "max_length": 2,
                }
            )

        @dataclass
        class InclusionDetail:
            inclusion_identifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "inclusionIdentifier",
                    "type": "Element",
                    "required": True,
                    "min_length": 0,
                    "max_length": 1,
                }
            )
            location_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "locationId",
                    "type": "Element",
                    "required": True,
                    "min_length": 3,
                    "max_length": 5,
                }
            )
            airport_city_qualifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "airportCityQualifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 1,
                }
            )

        @dataclass
        class ExclusionDetail:
            exclusion_identifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "exclusionIdentifier",
                    "type": "Element",
                    "required": True,
                    "min_length": 0,
                    "max_length": 1,
                }
            )
            location_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "locationId",
                    "type": "Element",
                    "required": True,
                    "min_length": 3,
                    "max_length": 5,
                }
            )
            airport_city_qualifier: Optional[str] = field(
                default=None,
                metadata={
                    "name": "airportCityQualifier",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 1,
                }
            )

        @dataclass
        class UnitNumberDetail:
            number_of_units: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "numberOfUnits",
                    "type": "Element",
                    "required": True,
                }
            )
            type_of_unit: Optional[str] = field(
                default=None,
                metadata={
                    "name": "typeOfUnit",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )

    @dataclass
    class ValueSearch:
        criteria_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "criteriaName",
                "type": "Element",
                "min_length": 1,
                "max_length": 50,
            }
        )
        criteria_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "criteriaCode",
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
            }
        )
        value: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 1,
                "max_length": 18,
            }
        )
        criteria_details: List["FareMasterPricerTravelBoardSearch.ValueSearch.CriteriaDetails"] = field(
            default_factory=list,
            metadata={
                "name": "criteriaDetails",
                "type": "Element",
                "max_occurs": 10,
            }
        )

        @dataclass
        class CriteriaDetails:
            type: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            value: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 18,
                }
            )
            attribute: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 99,
                    "min_length": 1,
                    "max_length": 9,
                }
            )

    @dataclass
    class Buckets:
        bucket_info: Optional["FareMasterPricerTravelBoardSearch.Buckets.BucketInfo"] = field(
            default=None,
            metadata={
                "name": "bucketInfo",
                "type": "Element",
                "required": True,
            }
        )
        bucket_details: List["FareMasterPricerTravelBoardSearch.Buckets.BucketDetails"] = field(
            default_factory=list,
            metadata={
                "name": "bucketDetails",
                "type": "Element",
                "max_occurs": 15,
            }
        )

        @dataclass
        class BucketInfo:
            number: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            name: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 20,
                }
            )
            completion: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            mode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            value_ref: Optional[str] = field(
                default=None,
                metadata={
                    "name": "valueRef",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            weight: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            count: Optional[Decimal] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            attribute_count: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "attributeCount",
                    "type": "Element",
                }
            )

        @dataclass
        class BucketDetails:
            code: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            type: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            attribute: List["FareMasterPricerTravelBoardSearch.Buckets.BucketDetails.Attribute"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "max_occurs": 10,
                }
            )

            @dataclass
            class Attribute:
                requested_sgt: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "requestedSgt",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                value: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 50,
                        "min_length": 1,
                        "max_length": 20,
                    }
                )

    @dataclass
    class Itinerary:
        requested_segment_ref: Optional["FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentRef"] = field(
            default=None,
            metadata={
                "name": "requestedSegmentRef",
                "type": "Element",
                "required": True,
            }
        )
        departure_localization: Optional["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization"] = field(
            default=None,
            metadata={
                "name": "departureLocalization",
                "type": "Element",
            }
        )
        arrival_localization: Optional["FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization"] = field(
            default=None,
            metadata={
                "name": "arrivalLocalization",
                "type": "Element",
            }
        )
        time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails"] = field(
            default=None,
            metadata={
                "name": "timeDetails",
                "type": "Element",
            }
        )
        flight_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo"] = field(
            default=None,
            metadata={
                "name": "flightInfo",
                "type": "Element",
            }
        )
        family_information: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FamilyInformation"] = field(
            default=None,
            metadata={
                "name": "familyInformation",
                "type": "Element",
            }
        )
        value_search: List["FareMasterPricerTravelBoardSearch.Itinerary.ValueSearch"] = field(
            default_factory=list,
            metadata={
                "name": "valueSearch",
                "type": "Element",
                "max_occurs": 99,
            }
        )
        group_of_flights: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights"] = field(
            default_factory=list,
            metadata={
                "name": "groupOfFlights",
                "type": "Element",
                "max_occurs": 6,
            }
        )
        flight_info_pnr: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr"] = field(
            default_factory=list,
            metadata={
                "name": "flightInfoPNR",
                "type": "Element",
                "max_occurs": 4,
            }
        )
        requested_segment_action: Optional["FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentAction"] = field(
            default=None,
            metadata={
                "name": "requestedSegmentAction",
                "type": "Element",
            }
        )
        attributes: Optional["FareMasterPricerTravelBoardSearch.Itinerary.Attributes"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )

        @dataclass
        class RequestedSegmentRef:
            seg_ref: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "segRef",
                    "type": "Element",
                    "required": True,
                }
            )
            location_forcing: List["FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentRef.LocationForcing"] = field(
                default_factory=list,
                metadata={
                    "name": "locationForcing",
                    "type": "Element",
                    "max_occurs": 2,
                }
            )

            @dataclass
            class LocationForcing:
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 1,
                    }
                )
                segment_number: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "segmentNumber",
                        "type": "Element",
                        "required": True,
                    }
                )

        @dataclass
        class DepartureLocalization:
            departure_point: Optional["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.DeparturePoint"] = field(
                default=None,
                metadata={
                    "name": "departurePoint",
                    "type": "Element",
                }
            )
            dep_multi_city: List["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.DepMultiCity"] = field(
                default_factory=list,
                metadata={
                    "name": "depMultiCity",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            first_pnr_segment_ref: Optional["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.FirstPnrSegmentRef"] = field(
                default=None,
                metadata={
                    "name": "firstPnrSegmentRef",
                    "type": "Element",
                }
            )
            attribute_details: List["FareMasterPricerTravelBoardSearch.Itinerary.DepartureLocalization.AttributeDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "attributeDetails",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )

            @dataclass
            class DeparturePoint:
                distance: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                distance_unit: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "distanceUnit",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )
                latitude: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    }
                )
                longitude: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    }
                )

            @dataclass
            class DepMultiCity:
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

            @dataclass
            class FirstPnrSegmentRef:
                pnr_segment_tattoo: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "pnrSegmentTattoo",
                        "type": "Element",
                    }
                )
                pnr_segment_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pnrSegmentQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

            @dataclass
            class AttributeDetails:
                type: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                value: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 10,
                        "min_length": 1,
                        "max_length": 20,
                    }
                )

        @dataclass
        class ArrivalLocalization:
            arrival_point_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization.ArrivalPointDetails"] = field(
                default=None,
                metadata={
                    "name": "arrivalPointDetails",
                    "type": "Element",
                }
            )
            arrival_multi_city: List["FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization.ArrivalMultiCity"] = field(
                default_factory=list,
                metadata={
                    "name": "arrivalMultiCity",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            attribute_details: List["FareMasterPricerTravelBoardSearch.Itinerary.ArrivalLocalization.AttributeDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "attributeDetails",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )

            @dataclass
            class ArrivalPointDetails:
                distance: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )
                distance_unit: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "distanceUnit",
                        "type": "Element",
                        "min_length": 0,
                        "max_length": 3,
                    }
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )
                latitude: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    }
                )
                longitude: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    }
                )

            @dataclass
            class ArrivalMultiCity:
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

            @dataclass
            class AttributeDetails:
                type: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                value: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 10,
                        "min_length": 1,
                        "max_length": 20,
                    }
                )

        @dataclass
        class TimeDetails:
            first_date_time_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails.FirstDateTimeDetail"] = field(
                default=None,
                metadata={
                    "name": "firstDateTimeDetail",
                    "type": "Element",
                    "required": True,
                }
            )
            range_of_date: Optional["FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails.RangeOfDate"] = field(
                default=None,
                metadata={
                    "name": "rangeOfDate",
                    "type": "Element",
                }
            )
            trip_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.TimeDetails.TripDetails"] = field(
                default=None,
                metadata={
                    "name": "tripDetails",
                    "type": "Element",
                }
            )

            @dataclass
            class FirstDateTimeDetail:
                time_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "timeQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                date: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    }
                )
                time: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 4,
                        "max_length": 4,
                    }
                )
                time_window: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "timeWindow",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

            @dataclass
            class RangeOfDate:
                range_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "rangeQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                day_interval: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "dayInterval",
                        "type": "Element",
                    }
                )
                time_atdestination: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "timeAtdestination",
                        "type": "Element",
                        "min_length": 4,
                        "max_length": 4,
                    }
                )

            @dataclass
            class TripDetails:
                flexibility_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "flexibilityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                trip_interval: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "tripInterval",
                        "type": "Element",
                    }
                )
                trip_duration: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "tripDuration",
                        "type": "Element",
                    }
                )

        @dataclass
        class FlightInfo:
            cabin_id: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.CabinId"] = field(
                default=None,
                metadata={
                    "name": "cabinId",
                    "type": "Element",
                }
            )
            company_identity: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.CompanyIdentity"] = field(
                default_factory=list,
                metadata={
                    "name": "companyIdentity",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            flight_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.FlightDetail"] = field(
                default=None,
                metadata={
                    "name": "flightDetail",
                    "type": "Element",
                }
            )
            inclusion_detail: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.InclusionDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "inclusionDetail",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            exclusion_detail: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.ExclusionDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "exclusionDetail",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            unit_number_detail: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfo.UnitNumberDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "unitNumberDetail",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )

            @dataclass
            class CabinId:
                cabin_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cabinQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 2,
                    }
                )
                cabin: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 5,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )

            @dataclass
            class CompanyIdentity:
                carrier_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "carrierQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                carrier_id: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "carrierId",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 99,
                        "min_length": 2,
                        "max_length": 3,
                    }
                )

            @dataclass
            class FlightDetail:
                flight_type: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "flightType",
                        "type": "Element",
                        "max_occurs": 9,
                        "min_length": 1,
                        "max_length": 2,
                    }
                )

            @dataclass
            class InclusionDetail:
                inclusion_identifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "inclusionIdentifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

            @dataclass
            class ExclusionDetail:
                exclusion_identifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "exclusionIdentifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

            @dataclass
            class UnitNumberDetail:
                number_of_units: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "numberOfUnits",
                        "type": "Element",
                        "required": True,
                    }
                )
                type_of_unit: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "typeOfUnit",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass
        class FamilyInformation:
            commercial_family_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FamilyInformation.CommercialFamilyDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "commercialFamilyDetails",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )

            @dataclass
            class CommercialFamilyDetails:
                commercial_family: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "commercialFamily",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 10,
                    }
                )

        @dataclass
        class ValueSearch:
            criteria_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "criteriaName",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 50,
                }
            )
            criteria_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "criteriaCode",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            value: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 18,
                }
            )
            criteria_details: List["FareMasterPricerTravelBoardSearch.Itinerary.ValueSearch.CriteriaDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "criteriaDetails",
                    "type": "Element",
                    "max_occurs": 10,
                }
            )

            @dataclass
            class CriteriaDetails:
                type: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                value: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 18,
                    }
                )
                attribute: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 99,
                        "min_length": 1,
                        "max_length": 9,
                    }
                )

        @dataclass
        class GroupOfFlights:
            prop_flight_gr_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PropFlightGrDetail"] = field(
                default=None,
                metadata={
                    "name": "propFlightGrDetail",
                    "type": "Element",
                    "required": True,
                }
            )
            price_to_beat: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PriceToBeat"] = field(
                default=None,
                metadata={
                    "name": "priceToBeat",
                    "type": "Element",
                }
            )
            flight_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "flightDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 4,
                }
            )

            @dataclass
            class PropFlightGrDetail:
                flight_proposal: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PropFlightGrDetail.FlightProposal"] = field(
                    default_factory=list,
                    metadata={
                        "name": "flightProposal",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 9,
                    }
                )
                flight_characteristic: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "flightCharacteristic",
                        "type": "Element",
                        "min_length": 0,
                        "max_length": 3,
                    }
                )
                maj_cabin: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "majCabin",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

                @dataclass
                class FlightProposal:
                    ref: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 6,
                        }
                    )
                    unit_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "unitQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

            @dataclass
            class PriceToBeat:
                money_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PriceToBeat.MoneyInfo"] = field(
                    default=None,
                    metadata={
                        "name": "moneyInfo",
                        "type": "Element",
                        "required": True,
                    }
                )
                additional_money_info: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.PriceToBeat.AdditionalMoneyInfo"] = field(
                    default_factory=list,
                    metadata={
                        "name": "additionalMoneyInfo",
                        "type": "Element",
                        "max_occurs": 19,
                    }
                )

                @dataclass
                class MoneyInfo:
                    qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    amount: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    currency: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class AdditionalMoneyInfo:
                    qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    amount: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                        }
                    )
                    currency: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    location_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "locationId",
                            "type": "Element",
                            "min_length": 3,
                            "max_length": 3,
                        }
                    )

            @dataclass
            class FlightDetails:
                flight_information: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation"] = field(
                    default=None,
                    metadata={
                        "name": "flightInformation",
                        "type": "Element",
                        "required": True,
                    }
                )
                avl_info: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AvlInfo"] = field(
                    default_factory=list,
                    metadata={
                        "name": "avlInfo",
                        "type": "Element",
                        "max_occurs": 6,
                    }
                )
                technical_stop: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TechnicalStop"] = field(
                    default_factory=list,
                    metadata={
                        "name": "technicalStop",
                        "type": "Element",
                        "max_occurs": 5,
                    }
                )
                commercial_agreement: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.CommercialAgreement"] = field(
                    default=None,
                    metadata={
                        "name": "commercialAgreement",
                        "type": "Element",
                    }
                )
                add_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AddInfo"] = field(
                    default=None,
                    metadata={
                        "name": "addInfo",
                        "type": "Element",
                    }
                )
                terminal_equipment_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails"] = field(
                    default_factory=list,
                    metadata={
                        "name": "terminalEquipmentDetails",
                        "type": "Element",
                        "max_occurs": 2,
                    }
                )
                reservation_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.ReservationInfo"] = field(
                    default=None,
                    metadata={
                        "name": "reservationInfo",
                        "type": "Element",
                    }
                )
                price_to_beat: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.PriceToBeat"] = field(
                    default=None,
                    metadata={
                        "name": "priceToBeat",
                        "type": "Element",
                    }
                )

                @dataclass
                class FlightInformation:
                    product_date_time: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.ProductDateTime"] = field(
                        default=None,
                        metadata={
                            "name": "productDateTime",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    location: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.Location"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 2,
                        }
                    )
                    company_id: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.CompanyId"] = field(
                        default=None,
                        metadata={
                            "name": "companyId",
                            "type": "Element",
                        }
                    )
                    flight_ortrain_number: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "flightOrtrainNumber",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 8,
                        }
                    )
                    product_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.ProductDetail"] = field(
                        default=None,
                        metadata={
                            "name": "productDetail",
                            "type": "Element",
                        }
                    )
                    add_product_detail: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.AddProductDetail"] = field(
                        default=None,
                        metadata={
                            "name": "addProductDetail",
                            "type": "Element",
                        }
                    )
                    attribute_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.FlightInformation.AttributeDetails"] = field(
                        default_factory=list,
                        metadata={
                            "name": "attributeDetails",
                            "type": "Element",
                            "max_occurs": 20,
                        }
                    )

                    @dataclass
                    class ProductDateTime:
                        date_of_departure: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "dateOfDeparture",
                                "type": "Element",
                                "required": True,
                                "min_length": 6,
                                "max_length": 6,
                            }
                        )
                        time_of_departure: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "timeOfDeparture",
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            }
                        )
                        date_of_arrival: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "dateOfArrival",
                                "type": "Element",
                                "min_length": 6,
                                "max_length": 6,
                            }
                        )
                        time_of_arrival: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "timeOfArrival",
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            }
                        )
                        date_variation: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "dateVariation",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )

                    @dataclass
                    class Location:
                        location_id: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "locationId",
                                "type": "Element",
                                "required": True,
                                "min_length": 3,
                                "max_length": 5,
                            }
                        )
                        airport_city_qualifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "airportCityQualifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        terminal: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 5,
                            }
                        )

                    @dataclass
                    class CompanyId:
                        marketing_carrier: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "marketingCarrier",
                                "type": "Element",
                                "required": True,
                                "min_length": 2,
                                "max_length": 3,
                            }
                        )
                        operating_carrier: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "operatingCarrier",
                                "type": "Element",
                                "min_length": 2,
                                "max_length": 3,
                            }
                        )

                    @dataclass
                    class ProductDetail:
                        equipment_type: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "equipmentType",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        operating_day: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "operatingDay",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 7,
                            }
                        )
                        tech_stop_number: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "name": "techStopNumber",
                                "type": "Element",
                            }
                        )
                        location_id: List[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "locationId",
                                "type": "Element",
                                "max_occurs": 3,
                                "min_length": 3,
                                "max_length": 5,
                            }
                        )

                    @dataclass
                    class AddProductDetail:
                        last_seat_available: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "lastSeatAvailable",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        level_of_access: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "levelOfAccess",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        electronic_ticketing: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "electronicTicketing",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        operational_suffix: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "operationalSuffix",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        product_detail_qualifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "productDetailQualifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        flight_characteristic: List[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "flightCharacteristic",
                                "type": "Element",
                                "max_occurs": 9,
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )

                    @dataclass
                    class AttributeDetails:
                        attribute_type: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "attributeType",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 5,
                            }
                        )
                        attribute_description: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "attributeDescription",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 10,
                            }
                        )

                @dataclass
                class AvlInfo:
                    cabin_product: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AvlInfo.CabinProduct"] = field(
                        default_factory=list,
                        metadata={
                            "name": "cabinProduct",
                            "type": "Element",
                            "max_occurs": 26,
                        }
                    )
                    context_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AvlInfo.ContextDetails"] = field(
                        default=None,
                        metadata={
                            "name": "contextDetails",
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class CabinProduct:
                        rbd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        booking_modifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "bookingModifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        cabin: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        avl_status: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "avlStatus",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )

                    @dataclass
                    class ContextDetails:
                        avl: List[str] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "min_occurs": 1,
                                "max_occurs": 9,
                                "min_length": 1,
                                "max_length": 6,
                            }
                        )

                @dataclass
                class TechnicalStop:
                    stop_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TechnicalStop.StopDetails"] = field(
                        default_factory=list,
                        metadata={
                            "name": "stopDetails",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 2,
                        }
                    )

                    @dataclass
                    class StopDetails:
                        date_qualifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "dateQualifier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        date: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 6,
                                "max_length": 6,
                            }
                        )
                        first_time: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "firstTime",
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            }
                        )
                        equipement_type: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "equipementType",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        location_id: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "locationId",
                                "type": "Element",
                                "min_length": 3,
                                "max_length": 5,
                            }
                        )

                @dataclass
                class CommercialAgreement:
                    codeshare_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.CommercialAgreement.CodeshareDetails"] = field(
                        default=None,
                        metadata={
                            "name": "codeshareDetails",
                            "type": "Element",
                        }
                    )
                    other_codeshare_details: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.CommercialAgreement.OtherCodeshareDetails"] = field(
                        default_factory=list,
                        metadata={
                            "name": "otherCodeshareDetails",
                            "type": "Element",
                            "max_occurs": 9,
                        }
                    )

                    @dataclass
                    class CodeshareDetails:
                        code_share_type: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "codeShareType",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        airline_designator: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "airlineDesignator",
                                "type": "Element",
                                "min_length": 2,
                                "max_length": 3,
                            }
                        )
                        flight_number: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "name": "flightNumber",
                                "type": "Element",
                            }
                        )

                    @dataclass
                    class OtherCodeshareDetails:
                        code_share_type: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "codeShareType",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )
                        airline_designator: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "airlineDesignator",
                                "type": "Element",
                                "min_length": 2,
                                "max_length": 3,
                            }
                        )
                        flight_number: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "name": "flightNumber",
                                "type": "Element",
                            }
                        )

                @dataclass
                class AddInfo:
                    status: List[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 2,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    date_time_period_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.AddInfo.DateTimePeriodDetails"] = field(
                        default=None,
                        metadata={
                            "name": "dateTimePeriodDetails",
                            "type": "Element",
                        }
                    )
                    reference_number: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "referenceNumber",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 35,
                        }
                    )
                    product_identification: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "productIdentification",
                            "type": "Element",
                            "max_occurs": 2,
                            "min_length": 1,
                            "max_length": 35,
                        }
                    )

                    @dataclass
                    class DateTimePeriodDetails:
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        value: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 35,
                            }
                        )

                @dataclass
                class TerminalEquipmentDetails:
                    leg_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.LegDetails"] = field(
                        default=None,
                        metadata={
                            "name": "legDetails",
                            "type": "Element",
                        }
                    )
                    departure_station_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.DepartureStationInfo"] = field(
                        default=None,
                        metadata={
                            "name": "departureStationInfo",
                            "type": "Element",
                        }
                    )
                    arrival_station_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.ArrivalStationInfo"] = field(
                        default=None,
                        metadata={
                            "name": "arrivalStationInfo",
                            "type": "Element",
                        }
                    )
                    mileage_time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.TerminalEquipmentDetails.MileageTimeDetails"] = field(
                        default=None,
                        metadata={
                            "name": "mileageTimeDetails",
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class LegDetails:
                        equipment: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        duration: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                            }
                        )
                        complexing_flight_indicator: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "complexingFlightIndicator",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 1,
                            }
                        )

                    @dataclass
                    class DepartureStationInfo:
                        terminal: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )

                    @dataclass
                    class ArrivalStationInfo:
                        terminal: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )

                    @dataclass
                    class MileageTimeDetails:
                        elapsed_ground_time: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "name": "elapsedGroundTime",
                                "type": "Element",
                            }
                        )

                @dataclass
                class ReservationInfo:
                    booking: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )
                    identifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )
                    status: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    item_number: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "itemNumber",
                            "type": "Element",
                        }
                    )
                    date_time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.ReservationInfo.DateTimeDetails"] = field(
                        default=None,
                        metadata={
                            "name": "dateTimeDetails",
                            "type": "Element",
                        }
                    )
                    designator: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )
                    movement_type: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "movementType",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    product_type_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.ReservationInfo.ProductTypeDetails"] = field(
                        default=None,
                        metadata={
                            "name": "productTypeDetails",
                            "type": "Element",
                        }
                    )

                    @dataclass
                    class DateTimeDetails:
                        date: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                                "min_length": 6,
                                "max_length": 6,
                            }
                        )
                        time: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            }
                        )

                    @dataclass
                    class ProductTypeDetails:
                        sequence_number: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "sequenceNumber",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 6,
                            }
                        )
                        availability_context: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "availabilityContext",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 6,
                            }
                        )

                @dataclass
                class PriceToBeat:
                    money_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.PriceToBeat.MoneyInfo"] = field(
                        default=None,
                        metadata={
                            "name": "moneyInfo",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    additional_money_info: List["FareMasterPricerTravelBoardSearch.Itinerary.GroupOfFlights.FlightDetails.PriceToBeat.AdditionalMoneyInfo"] = field(
                        default_factory=list,
                        metadata={
                            "name": "additionalMoneyInfo",
                            "type": "Element",
                            "max_occurs": 19,
                        }
                    )

                    @dataclass
                    class MoneyInfo:
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        amount: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        currency: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )

                    @dataclass
                    class AdditionalMoneyInfo:
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        amount: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "required": True,
                            }
                        )
                        currency: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        location_id: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "locationId",
                                "type": "Element",
                                "min_length": 3,
                                "max_length": 3,
                            }
                        )

        @dataclass
        class FlightInfoPnr:
            travel_response_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails"] = field(
                default=None,
                metadata={
                    "name": "travelResponseDetails",
                    "type": "Element",
                    "required": True,
                }
            )
            time_table_date: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate"] = field(
                default=None,
                metadata={
                    "name": "timeTableDate",
                    "type": "Element",
                }
            )
            terminal_equipment_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "terminalEquipmentDetails",
                    "type": "Element",
                    "max_occurs": 2,
                }
            )
            codeshare_data: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.CodeshareData"] = field(
                default=None,
                metadata={
                    "name": "codeshareData",
                    "type": "Element",
                }
            )
            disclosure: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.Disclosure"] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            stop_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.StopDetails"] = field(
                default=None,
                metadata={
                    "name": "stopDetails",
                    "type": "Element",
                }
            )
            traffic_restriction_data: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TrafficRestrictionData"] = field(
                default=None,
                metadata={
                    "name": "trafficRestrictionData",
                    "type": "Element",
                }
            )
            reservation_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.ReservationInfo"] = field(
                default=None,
                metadata={
                    "name": "reservationInfo",
                    "type": "Element",
                }
            )
            incidental_stop_info: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo"] = field(
                default_factory=list,
                metadata={
                    "name": "incidentalStopInfo",
                    "type": "Element",
                    "max_occurs": 8,
                }
            )

            @dataclass
            class TravelResponseDetails:
                flight_date: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.FlightDate"] = field(
                    default=None,
                    metadata={
                        "name": "flightDate",
                        "type": "Element",
                    }
                )
                board_point_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.BoardPointDetails"] = field(
                    default=None,
                    metadata={
                        "name": "boardPointDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                offpoint_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.OffpointDetails"] = field(
                    default=None,
                    metadata={
                        "name": "offpointDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                company_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.CompanyDetails"] = field(
                    default=None,
                    metadata={
                        "name": "companyDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                flight_identification: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.FlightIdentification"] = field(
                    default=None,
                    metadata={
                        "name": "flightIdentification",
                        "type": "Element",
                    }
                )
                flight_type_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TravelResponseDetails.FlightTypeDetails"] = field(
                    default=None,
                    metadata={
                        "name": "flightTypeDetails",
                        "type": "Element",
                    }
                )

                @dataclass
                class FlightDate:
                    departure_date: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "departureDate",
                            "type": "Element",
                            "min_length": 8,
                            "max_length": 8,
                        }
                    )
                    departure_time: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "departureTime",
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        }
                    )
                    arrival_date: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "arrivalDate",
                            "type": "Element",
                            "min_length": 8,
                            "max_length": 8,
                        }
                    )
                    arrival_time: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "arrivalTime",
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        }
                    )
                    date_variation: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dateVariation",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass
                class BoardPointDetails:
                    true_location_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "trueLocationId",
                            "type": "Element",
                            "required": True,
                            "min_length": 3,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class OffpointDetails:
                    true_location_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "trueLocationId",
                            "type": "Element",
                            "required": True,
                            "min_length": 3,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class CompanyDetails:
                    marketing_company: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "marketingCompany",
                            "type": "Element",
                            "required": True,
                            "min_length": 2,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class FlightIdentification:
                    flight_number: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "flightNumber",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    operational_suffix: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "operationalSuffix",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass
                class FlightTypeDetails:
                    flight_indicator: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "flightIndicator",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 5,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

            @dataclass
            class TimeTableDate:
                begin_date_time: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate.BeginDateTime"] = field(
                    default=None,
                    metadata={
                        "name": "beginDateTime",
                        "type": "Element",
                    }
                )
                end_date_time: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate.EndDateTime"] = field(
                    default=None,
                    metadata={
                        "name": "endDateTime",
                        "type": "Element",
                    }
                )
                frequency: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TimeTableDate.Frequency"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                    }
                )

                @dataclass
                class BeginDateTime:
                    year: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        }
                    )
                    month: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    day: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass
                class EndDateTime:
                    year: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        }
                    )
                    month: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    day: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )

                @dataclass
                class Frequency:
                    qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    value: List[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 7,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

            @dataclass
            class TerminalEquipmentDetails:
                leg_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.LegDetails"] = field(
                    default=None,
                    metadata={
                        "name": "legDetails",
                        "type": "Element",
                    }
                )
                departure_station_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.DepartureStationInfo"] = field(
                    default=None,
                    metadata={
                        "name": "departureStationInfo",
                        "type": "Element",
                    }
                )
                arrival_station_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.ArrivalStationInfo"] = field(
                    default=None,
                    metadata={
                        "name": "arrivalStationInfo",
                        "type": "Element",
                    }
                )
                mileage_time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TerminalEquipmentDetails.MileageTimeDetails"] = field(
                    default=None,
                    metadata={
                        "name": "mileageTimeDetails",
                        "type": "Element",
                    }
                )

                @dataclass
                class LegDetails:
                    equipment: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    duration: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                        }
                    )
                    complexing_flight_indicator: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "complexingFlightIndicator",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass
                class DepartureStationInfo:
                    terminal: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class ArrivalStationInfo:
                    terminal: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class MileageTimeDetails:
                    elapsed_ground_time: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "elapsedGroundTime",
                            "type": "Element",
                        }
                    )

            @dataclass
            class CodeshareData:
                codeshare_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.CodeshareData.CodeshareDetails"] = field(
                    default=None,
                    metadata={
                        "name": "codeshareDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                other_codeshare_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.CodeshareData.OtherCodeshareDetails"] = field(
                    default_factory=list,
                    metadata={
                        "name": "otherCodeshareDetails",
                        "type": "Element",
                        "max_occurs": 8,
                    }
                )

                @dataclass
                class CodeshareDetails:
                    transport_stage_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "transportStageQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )
                    airline_designator: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "airlineDesignator",
                            "type": "Element",
                            "min_length": 2,
                            "max_length": 3,
                        }
                    )
                    flight_number: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "flightNumber",
                            "type": "Element",
                        }
                    )
                    operational_suffix: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "operationalSuffix",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass
                class OtherCodeshareDetails:
                    transport_stage_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "transportStageQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )
                    airline_designator: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "airlineDesignator",
                            "type": "Element",
                            "min_length": 2,
                            "max_length": 3,
                        }
                    )
                    flight_number: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "flightNumber",
                            "type": "Element",
                        }
                    )
                    operational_suffix: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "operationalSuffix",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

            @dataclass
            class Disclosure:
                free_text_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.Disclosure.FreeTextDetails"] = field(
                    default=None,
                    metadata={
                        "name": "freeTextDetails",
                        "type": "Element",
                        "required": True,
                    }
                )
                free_text: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "freeText",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 70,
                    }
                )

                @dataclass
                class FreeTextDetails:
                    text_subject_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "textSubjectQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    information_type: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "informationType",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 4,
                        }
                    )
                    source: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    encoding: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

            @dataclass
            class StopDetails:
                routing_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.StopDetails.RoutingDetails"] = field(
                    default_factory=list,
                    metadata={
                        "name": "routingDetails",
                        "type": "Element",
                        "max_occurs": 9,
                    }
                )

                @dataclass
                class RoutingDetails:
                    station: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 3,
                            "max_length": 3,
                        }
                    )

            @dataclass
            class TrafficRestrictionData:
                traffic_restriction_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.TrafficRestrictionData.TrafficRestrictionDetails"] = field(
                    default_factory=list,
                    metadata={
                        "name": "trafficRestrictionDetails",
                        "type": "Element",
                        "max_occurs": 5,
                    }
                )

                @dataclass
                class TrafficRestrictionDetails:
                    code: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

            @dataclass
            class ReservationInfo:
                booking: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )
                identifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )
                status: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                item_number: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "itemNumber",
                        "type": "Element",
                    }
                )
                date_time_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.ReservationInfo.DateTimeDetails"] = field(
                    default=None,
                    metadata={
                        "name": "dateTimeDetails",
                        "type": "Element",
                    }
                )
                designator: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )
                movement_type: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "movementType",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                product_type_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.ReservationInfo.ProductTypeDetails"] = field(
                    default=None,
                    metadata={
                        "name": "productTypeDetails",
                        "type": "Element",
                    }
                )

                @dataclass
                class DateTimeDetails:
                    date: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 6,
                            "max_length": 6,
                        }
                    )
                    time: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 4,
                            "max_length": 4,
                        }
                    )

                @dataclass
                class ProductTypeDetails:
                    sequence_number: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "sequenceNumber",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 6,
                        }
                    )
                    availability_context: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "availabilityContext",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 6,
                        }
                    )

            @dataclass
            class IncidentalStopInfo:
                date_time_info: Optional["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo.DateTimeInfo"] = field(
                    default=None,
                    metadata={
                        "name": "dateTimeInfo",
                        "type": "Element",
                        "required": True,
                    }
                )

                @dataclass
                class DateTimeInfo:
                    date_time_details: List["FareMasterPricerTravelBoardSearch.Itinerary.FlightInfoPnr.IncidentalStopInfo.DateTimeInfo.DateTimeDetails"] = field(
                        default_factory=list,
                        metadata={
                            "name": "dateTimeDetails",
                            "type": "Element",
                            "max_occurs": 2,
                        }
                    )

                    @dataclass
                    class DateTimeDetails:
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        date: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 6,
                                "max_length": 6,
                            }
                        )
                        time: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 4,
                                "max_length": 4,
                            }
                        )
                        qualifier2: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        reserved1: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        reserved2: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 3,
                                "max_length": 5,
                            }
                        )

        @dataclass
        class RequestedSegmentAction:
            action_request_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "actionRequestCode",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 3,
                }
            )
            product_details: Optional["FareMasterPricerTravelBoardSearch.Itinerary.RequestedSegmentAction.ProductDetails"] = field(
                default=None,
                metadata={
                    "name": "productDetails",
                    "type": "Element",
                }
            )

            @dataclass
            class ProductDetails:
                flight_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "flightNumber",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                booking_class: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "bookingClass",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 2,
                    }
                )
                operational_suffix: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "operationalSuffix",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                modifier: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "max_occurs": 3,
                        "min_length": 1,
                        "max_length": 7,
                    }
                )

        @dataclass
        class Attributes:
            attribute_details: List["FareMasterPricerTravelBoardSearch.Itinerary.Attributes.AttributeDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "attributeDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 9,
                }
            )

            @dataclass
            class AttributeDetails:
                attribute_type: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "attributeType",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                attribute_description: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "attributeDescription",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 50,
                    }
                )

    @dataclass
    class TicketChangeInfo:
        ticket_number_details: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketNumberDetails"] = field(
            default=None,
            metadata={
                "name": "ticketNumberDetails",
                "type": "Element",
                "required": True,
            }
        )
        ticket_requested_segments: List["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments"] = field(
            default_factory=list,
            metadata={
                "name": "ticketRequestedSegments",
                "type": "Element",
                "max_occurs": 6,
            }
        )

        @dataclass
        class TicketNumberDetails:
            document_details: List["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketNumberDetails.DocumentDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "documentDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 99,
                }
            )

            @dataclass
            class DocumentDetails:
                number: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 35,
                    }
                )

        @dataclass
        class TicketRequestedSegments:
            action_identification: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ActionIdentification"] = field(
                default=None,
                metadata={
                    "name": "actionIdentification",
                    "type": "Element",
                    "required": True,
                }
            )
            connect_point_details: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ConnectPointDetails"] = field(
                default=None,
                metadata={
                    "name": "connectPointDetails",
                    "type": "Element",
                }
            )

            @dataclass
            class ActionIdentification:
                action_request_code: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "actionRequestCode",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                product_details: Optional["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ActionIdentification.ProductDetails"] = field(
                    default=None,
                    metadata={
                        "name": "productDetails",
                        "type": "Element",
                    }
                )

                @dataclass
                class ProductDetails:
                    flight_number: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "flightNumber",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 5,
                        }
                    )
                    booking_class: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "bookingClass",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 2,
                        }
                    )
                    operational_suffix: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "operationalSuffix",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    modifier: List[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "max_occurs": 3,
                            "min_length": 1,
                            "max_length": 7,
                        }
                    )

            @dataclass
            class ConnectPointDetails:
                connection_details: List["FareMasterPricerTravelBoardSearch.TicketChangeInfo.TicketRequestedSegments.ConnectPointDetails.ConnectionDetails"] = field(
                    default_factory=list,
                    metadata={
                        "name": "connectionDetails",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 17,
                    }
                )

                @dataclass
                class ConnectionDetails:
                    location: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

    @dataclass
    class CombinationFareFamilies:
        item_ffcnumber: Optional["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ItemFfcnumber"] = field(
            default=None,
            metadata={
                "name": "itemFFCNumber",
                "type": "Element",
                "required": True,
            }
        )
        nb_of_units: Optional["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.NbOfUnits"] = field(
            default=None,
            metadata={
                "name": "nbOfUnits",
                "type": "Element",
            }
        )
        reference_info: List["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ReferenceInfo"] = field(
            default_factory=list,
            metadata={
                "name": "referenceInfo",
                "type": "Element",
                "max_occurs": 6,
            }
        )

        @dataclass
        class ItemFfcnumber:
            item_number_id: Optional["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ItemFfcnumber.ItemNumberId"] = field(
                default=None,
                metadata={
                    "name": "itemNumberId",
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass
            class ItemNumberId:
                number: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 4,
                    }
                )
                type: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                responsible_agency: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "responsibleAgency",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass
        class NbOfUnits:
            unit_number_detail: List["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.NbOfUnits.UnitNumberDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "unitNumberDetail",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                }
            )

            @dataclass
            class UnitNumberDetail:
                number_of_units: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "numberOfUnits",
                        "type": "Element",
                    }
                )
                type_of_unit: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "typeOfUnit",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass
        class ReferenceInfo:
            referencing_detail: List["FareMasterPricerTravelBoardSearch.CombinationFareFamilies.ReferenceInfo.ReferencingDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "referencingDetail",
                    "type": "Element",
                    "max_occurs": 9,
                }
            )

            @dataclass
            class ReferencingDetail:
                ref_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "refQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                ref_number: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "refNumber",
                        "type": "Element",
                        "required": True,
                    }
                )

    @dataclass
    class FeeOption:
        fee_type_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeTypeInfo"] = field(
            default=None,
            metadata={
                "name": "feeTypeInfo",
                "type": "Element",
                "required": True,
            }
        )
        rate_tax: Optional["FareMasterPricerTravelBoardSearch.FeeOption.RateTax"] = field(
            default=None,
            metadata={
                "name": "rateTax",
                "type": "Element",
            }
        )
        fee_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails"] = field(
            default_factory=list,
            metadata={
                "name": "feeDetails",
                "type": "Element",
                "max_occurs": 99,
            }
        )

        @dataclass
        class FeeTypeInfo:
            carrier_fee_details: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeTypeInfo.CarrierFeeDetails"] = field(
                default=None,
                metadata={
                    "name": "carrierFeeDetails",
                    "type": "Element",
                    "required": True,
                }
            )
            other_selection_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeTypeInfo.OtherSelectionDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "otherSelectionDetails",
                    "type": "Element",
                    "max_occurs": 98,
                }
            )

            @dataclass
            class CarrierFeeDetails:
                type: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                option_information: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "optionInformation",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

            @dataclass
            class OtherSelectionDetails:
                option: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                option_information: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "optionInformation",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 35,
                    }
                )

        @dataclass
        class RateTax:
            monetary_details: List["FareMasterPricerTravelBoardSearch.FeeOption.RateTax.MonetaryDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "monetaryDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                }
            )

            @dataclass
            class MonetaryDetails:
                type_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "typeQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                amount: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    }
                )
                currency: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass
        class FeeDetails:
            fee_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeInfo"] = field(
                default=None,
                metadata={
                    "name": "feeInfo",
                    "type": "Element",
                    "required": True,
                }
            )
            associated_amounts: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.AssociatedAmounts"] = field(
                default=None,
                metadata={
                    "name": "associatedAmounts",
                    "type": "Element",
                }
            )
            fee_description_grp: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp"] = field(
                default=None,
                metadata={
                    "name": "feeDescriptionGrp",
                    "type": "Element",
                }
            )

            @dataclass
            class FeeInfo:
                data_type_information: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeInfo.DataTypeInformation"] = field(
                    default=None,
                    metadata={
                        "name": "dataTypeInformation",
                        "type": "Element",
                        "required": True,
                    }
                )
                data_information: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeInfo.DataInformation"] = field(
                    default_factory=list,
                    metadata={
                        "name": "dataInformation",
                        "type": "Element",
                        "max_occurs": 99,
                    }
                )

                @dataclass
                class DataTypeInformation:
                    sub_type: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "subType",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    option: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class DataInformation:
                    indicator: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

            @dataclass
            class AssociatedAmounts:
                monetary_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.AssociatedAmounts.MonetaryDetails"] = field(
                    default_factory=list,
                    metadata={
                        "name": "monetaryDetails",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 20,
                    }
                )

                @dataclass
                class MonetaryDetails:
                    type_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "typeQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    amount: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 12,
                        }
                    )
                    currency: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    location: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )

            @dataclass
            class FeeDescriptionGrp:
                item_number_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ItemNumberInfo"] = field(
                    default=None,
                    metadata={
                        "name": "itemNumberInfo",
                        "type": "Element",
                        "required": True,
                    }
                )
                service_attributes_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceAttributesInfo"] = field(
                    default=None,
                    metadata={
                        "name": "serviceAttributesInfo",
                        "type": "Element",
                    }
                )
                service_description_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceDescriptionInfo"] = field(
                    default=None,
                    metadata={
                        "name": "serviceDescriptionInfo",
                        "type": "Element",
                    }
                )

                @dataclass
                class ItemNumberInfo:
                    item_number_details: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ItemNumberInfo.ItemNumberDetails"] = field(
                        default=None,
                        metadata={
                            "name": "itemNumberDetails",
                            "type": "Element",
                            "required": True,
                        }
                    )

                    @dataclass
                    class ItemNumberDetails:
                        number: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 4,
                            }
                        )
                        type: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        qualifier: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        responsible_agency: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "responsibleAgency",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )

                @dataclass
                class ServiceAttributesInfo:
                    attribute_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "attributeQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
                    attribute_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceAttributesInfo.AttributeDetails"] = field(
                        default_factory=list,
                        metadata={
                            "name": "attributeDetails",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 99,
                        }
                    )

                    @dataclass
                    class AttributeDetails:
                        attribute_type: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "attributeType",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 25,
                            }
                        )
                        attribute_description: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "attributeDescription",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 256,
                            }
                        )

                @dataclass
                class ServiceDescriptionInfo:
                    service_requirements_info: Optional["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceDescriptionInfo.ServiceRequirementsInfo"] = field(
                        default=None,
                        metadata={
                            "name": "serviceRequirementsInfo",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    seat_details: List["FareMasterPricerTravelBoardSearch.FeeOption.FeeDetails.FeeDescriptionGrp.ServiceDescriptionInfo.SeatDetails"] = field(
                        default_factory=list,
                        metadata={
                            "name": "seatDetails",
                            "type": "Element",
                            "max_occurs": 999,
                        }
                    )

                    @dataclass
                    class ServiceRequirementsInfo:
                        service_classification: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "serviceClassification",
                                "type": "Element",
                                "required": True,
                                "min_length": 1,
                                "max_length": 4,
                            }
                        )
                        service_status: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "serviceStatus",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        service_number_of_instances: Optional[Decimal] = field(
                            default=None,
                            metadata={
                                "name": "serviceNumberOfInstances",
                                "type": "Element",
                            }
                        )
                        service_marketing_carrier: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "serviceMarketingCarrier",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        service_group: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "serviceGroup",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        service_sub_group: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "serviceSubGroup",
                                "type": "Element",
                                "min_length": 1,
                                "max_length": 3,
                            }
                        )
                        service_free_text: List[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "serviceFreeText",
                                "type": "Element",
                                "max_occurs": 99,
                                "min_length": 1,
                                "max_length": 70,
                            }
                        )

                    @dataclass
                    class SeatDetails:
                        seat_characteristics: List[str] = field(
                            default_factory=list,
                            metadata={
                                "name": "seatCharacteristics",
                                "type": "Element",
                                "max_occurs": 5,
                                "min_length": 1,
                                "max_length": 2,
                            }
                        )

    @dataclass
    class OfficeIdDetails:
        office_id_information: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.OfficeIdInformation"] = field(
            default=None,
            metadata={
                "name": "officeIdInformation",
                "type": "Element",
                "required": True,
            }
        )
        nb_of_units: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.NbOfUnits"] = field(
            default=None,
            metadata={
                "name": "nbOfUnits",
                "type": "Element",
            }
        )
        uid_option: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.UidOption"] = field(
            default=None,
            metadata={
                "name": "uidOption",
                "type": "Element",
            }
        )
        pricing_tick_info: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo"] = field(
            default=None,
            metadata={
                "name": "pricingTickInfo",
                "type": "Element",
            }
        )
        corporate_fare_info: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.CorporateFareInfo"] = field(
            default=None,
            metadata={
                "name": "corporateFareInfo",
                "type": "Element",
            }
        )
        travel_flight_info: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo"] = field(
            default=None,
            metadata={
                "name": "travelFlightInfo",
                "type": "Element",
            }
        )
        airline_distribution_details: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails"] = field(
            default_factory=list,
            metadata={
                "name": "airlineDistributionDetails",
                "type": "Element",
                "max_occurs": 6,
            }
        )

        @dataclass
        class OfficeIdInformation:
            office_identification: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.OfficeIdInformation.OfficeIdentification"] = field(
                default=None,
                metadata={
                    "name": "officeIdentification",
                    "type": "Element",
                }
            )
            office_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "officeType",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 1,
                }
            )
            office_code: Optional[str] = field(
                default=None,
                metadata={
                    "name": "officeCode",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 30,
                }
            )

            @dataclass
            class OfficeIdentification:
                office_name: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "officeName",
                        "type": "Element",
                    }
                )
                agent_signin: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "agentSignin",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 9,
                    }
                )
                confidential_office: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "confidentialOffice",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 9,
                    }
                )
                other_office: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "otherOffice",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 9,
                    }
                )

        @dataclass
        class NbOfUnits:
            unit_number_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.NbOfUnits.UnitNumberDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "unitNumberDetail",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                }
            )

            @dataclass
            class UnitNumberDetail:
                number_of_units: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "numberOfUnits",
                        "type": "Element",
                    }
                )
                type_of_unit: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "typeOfUnit",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass
        class UidOption:
            attribute_details: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.UidOption.AttributeDetails"] = field(
                default_factory=list,
                metadata={
                    "name": "attributeDetails",
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 20,
                }
            )

            @dataclass
            class AttributeDetails:
                attribute_type: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "attributeType",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 5,
                    }
                )
                attribute_description: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "attributeDescription",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 20,
                    }
                )

        @dataclass
        class PricingTickInfo:
            pricing_ticketing: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.PricingTicketing"] = field(
                default=None,
                metadata={
                    "name": "pricingTicketing",
                    "type": "Element",
                }
            )
            ticketing_date: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.TicketingDate"] = field(
                default=None,
                metadata={
                    "name": "ticketingDate",
                    "type": "Element",
                }
            )
            company_id: Optional[object] = field(
                default=None,
                metadata={
                    "name": "companyId",
                    "type": "Element",
                }
            )
            selling_point: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.SellingPoint"] = field(
                default=None,
                metadata={
                    "name": "sellingPoint",
                    "type": "Element",
                }
            )
            ticketing_point: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.TicketingPoint"] = field(
                default=None,
                metadata={
                    "name": "ticketingPoint",
                    "type": "Element",
                }
            )
            journey_origin_point: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.JourneyOriginPoint"] = field(
                default=None,
                metadata={
                    "name": "journeyOriginPoint",
                    "type": "Element",
                }
            )
            corporate_id: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.PricingTickInfo.CorporateId"] = field(
                default=None,
                metadata={
                    "name": "corporateId",
                    "type": "Element",
                }
            )

            @dataclass
            class PricingTicketing:
                price_type: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "priceType",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 50,
                        "min_length": 0,
                        "max_length": 3,
                    }
                )

            @dataclass
            class TicketingDate:
                date: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 6,
                        "max_length": 6,
                    }
                )
                rtc_date: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "rtcDate",
                        "type": "Element",
                        "min_length": 6,
                        "max_length": 6,
                    }
                )

            @dataclass
            class SellingPoint:
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

            @dataclass
            class TicketingPoint:
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

            @dataclass
            class JourneyOriginPoint:
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                country: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

            @dataclass
            class CorporateId:
                arc_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "arcNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    }
                )
                ersp_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "erspNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    }
                )
                iata_number: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "iataNumber",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 12,
                    }
                )

        @dataclass
        class CorporateFareInfo:
            corporate_fare_identifiers: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.CorporateFareInfo.CorporateFareIdentifiers"] = field(
                default=None,
                metadata={
                    "name": "corporateFareIdentifiers",
                    "type": "Element",
                }
            )

            @dataclass
            class CorporateFareIdentifiers:
                fare_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "fareQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 3,
                    }
                )
                identify_number: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "identifyNumber",
                        "type": "Element",
                        "max_occurs": 20,
                        "min_length": 1,
                        "max_length": 35,
                    }
                )

        @dataclass
        class TravelFlightInfo:
            cabin_id: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.CabinId"] = field(
                default=None,
                metadata={
                    "name": "cabinId",
                    "type": "Element",
                }
            )
            company_identity: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.CompanyIdentity"] = field(
                default_factory=list,
                metadata={
                    "name": "companyIdentity",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            flight_detail: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.FlightDetail"] = field(
                default=None,
                metadata={
                    "name": "flightDetail",
                    "type": "Element",
                }
            )
            inclusion_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.InclusionDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "inclusionDetail",
                    "type": "Element",
                    "max_occurs": 20,
                }
            )
            exclusion_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.ExclusionDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "exclusionDetail",
                    "type": "Element",
                    "max_occurs": 2,
                }
            )
            unit_number_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.TravelFlightInfo.UnitNumberDetail"] = field(
                default_factory=list,
                metadata={
                    "name": "unitNumberDetail",
                    "type": "Element",
                    "max_occurs": 9,
                }
            )

            @dataclass
            class CabinId:
                cabin_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cabinQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 2,
                    }
                )
                cabin: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 3,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )

            @dataclass
            class CompanyIdentity:
                carrier_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "carrierQualifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                carrier_id: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "carrierId",
                        "type": "Element",
                        "min_occurs": 1,
                        "max_occurs": 99,
                        "min_length": 2,
                        "max_length": 3,
                    }
                )

            @dataclass
            class FlightDetail:
                flight_type: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "flightType",
                        "type": "Element",
                        "max_occurs": 9,
                        "min_length": 1,
                        "max_length": 2,
                    }
                )

            @dataclass
            class InclusionDetail:
                inclusion_identifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "inclusionIdentifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

            @dataclass
            class ExclusionDetail:
                exclusion_identifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "exclusionIdentifier",
                        "type": "Element",
                        "required": True,
                        "min_length": 0,
                        "max_length": 1,
                    }
                )
                location_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "locationId",
                        "type": "Element",
                        "required": True,
                        "min_length": 3,
                        "max_length": 5,
                    }
                )
                airport_city_qualifier: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "airportCityQualifier",
                        "type": "Element",
                        "min_length": 1,
                        "max_length": 1,
                    }
                )

            @dataclass
            class UnitNumberDetail:
                number_of_units: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "numberOfUnits",
                        "type": "Element",
                        "required": True,
                    }
                )
                type_of_unit: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "typeOfUnit",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                    }
                )

        @dataclass
        class AirlineDistributionDetails:
            requested_segment_ref: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.RequestedSegmentRef"] = field(
                default=None,
                metadata={
                    "name": "requestedSegmentRef",
                    "type": "Element",
                    "required": True,
                }
            )
            flight_info: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo"] = field(
                default=None,
                metadata={
                    "name": "flightInfo",
                    "type": "Element",
                }
            )

            @dataclass
            class RequestedSegmentRef:
                seg_ref: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "segRef",
                        "type": "Element",
                        "required": True,
                    }
                )
                location_forcing: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.RequestedSegmentRef.LocationForcing"] = field(
                    default_factory=list,
                    metadata={
                        "name": "locationForcing",
                        "type": "Element",
                        "max_occurs": 2,
                    }
                )

                @dataclass
                class LocationForcing:
                    airport_city_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "airportCityQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )
                    segment_number: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "segmentNumber",
                            "type": "Element",
                            "required": True,
                        }
                    )

            @dataclass
            class FlightInfo:
                cabin_id: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.CabinId"] = field(
                    default=None,
                    metadata={
                        "name": "cabinId",
                        "type": "Element",
                    }
                )
                company_identity: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.CompanyIdentity"] = field(
                    default_factory=list,
                    metadata={
                        "name": "companyIdentity",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )
                flight_detail: Optional["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.FlightDetail"] = field(
                    default=None,
                    metadata={
                        "name": "flightDetail",
                        "type": "Element",
                    }
                )
                inclusion_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.InclusionDetail"] = field(
                    default_factory=list,
                    metadata={
                        "name": "inclusionDetail",
                        "type": "Element",
                        "max_occurs": 20,
                    }
                )
                exclusion_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.ExclusionDetail"] = field(
                    default_factory=list,
                    metadata={
                        "name": "exclusionDetail",
                        "type": "Element",
                        "max_occurs": 2,
                    }
                )
                unit_number_detail: List["FareMasterPricerTravelBoardSearch.OfficeIdDetails.AirlineDistributionDetails.FlightInfo.UnitNumberDetail"] = field(
                    default_factory=list,
                    metadata={
                        "name": "unitNumberDetail",
                        "type": "Element",
                        "max_occurs": 9,
                    }
                )

                @dataclass
                class CabinId:
                    cabin_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cabinQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 2,
                        }
                    )
                    cabin: List[str] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 3,
                            "min_length": 0,
                            "max_length": 1,
                        }
                    )

                @dataclass
                class CompanyIdentity:
                    carrier_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "carrierQualifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 0,
                            "max_length": 1,
                        }
                    )
                    carrier_id: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "carrierId",
                            "type": "Element",
                            "min_occurs": 1,
                            "max_occurs": 99,
                            "min_length": 2,
                            "max_length": 3,
                        }
                    )

                @dataclass
                class FlightDetail:
                    flight_type: List[str] = field(
                        default_factory=list,
                        metadata={
                            "name": "flightType",
                            "type": "Element",
                            "max_occurs": 9,
                            "min_length": 1,
                            "max_length": 2,
                        }
                    )

                @dataclass
                class InclusionDetail:
                    inclusion_identifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "inclusionIdentifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 0,
                            "max_length": 1,
                        }
                    )
                    location_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "locationId",
                            "type": "Element",
                            "required": True,
                            "min_length": 3,
                            "max_length": 5,
                        }
                    )
                    airport_city_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "airportCityQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass
                class ExclusionDetail:
                    exclusion_identifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "exclusionIdentifier",
                            "type": "Element",
                            "required": True,
                            "min_length": 0,
                            "max_length": 1,
                        }
                    )
                    location_id: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "locationId",
                            "type": "Element",
                            "required": True,
                            "min_length": 3,
                            "max_length": 5,
                        }
                    )
                    airport_city_qualifier: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "airportCityQualifier",
                            "type": "Element",
                            "min_length": 1,
                            "max_length": 1,
                        }
                    )

                @dataclass
                class UnitNumberDetail:
                    number_of_units: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "numberOfUnits",
                            "type": "Element",
                            "required": True,
                        }
                    )
                    type_of_unit: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "typeOfUnit",
                            "type": "Element",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                        }
                    )
