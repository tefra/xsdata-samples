from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xcbl.models.auction_create import (
    Agency,
    Contact,
    CorrespondenceLanguage,
    Country,
    Currency,
    DeliveryDetail,
    Identifier,
    Language,
    ListOfAttachment,
    ListOfDimension,
    ListOfIdentifier,
    ListOfPrice,
    ListOfReferenceCoded,
    Location,
    Measurement,
    NameAddress,
    NameValuePair,
    OrderContact,
    OrderDates,
    OtherContacts,
    PartNum,
    PartNumbers,
    Party,
    PartyId,
    Purpose,
    Quantity,
    QuantityRange,
    QuantityValue,
    RateOfExchangeDetail,
    ReceivingContact,
    Reference,
    Region,
    ShippingContact,
    TermsOfDelivery,
    Transport,
    UnitOfMeasurement,
    UnitPrice,
    ValidityDates,
)


@dataclass(kw_only=True)
class CardInfo:
    card_num: str = field(
        metadata={
            "name": "CardNum",
            "type": "Element",
            "required": True,
        }
    )
    card_auth_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardAuthCode",
            "type": "Element",
        }
    )
    card_ref_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardRefNum",
            "type": "Element",
        }
    )
    card_expiration_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardExpirationDate",
            "type": "Element",
        }
    )
    card_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardType",
            "type": "Element",
        }
    )
    card_type_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardTypeOther",
            "type": "Element",
        }
    )
    card_holder_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CardHolderName",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CatalogReference:
    catalog_url: str = field(
        metadata={
            "name": "CatalogURL",
            "type": "Element",
            "required": True,
        }
    )
    catalog_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CatalogID",
            "type": "Element",
        }
    )
    catalog_item_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CatalogItemID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ContractType:
    contract_type_coded: str = field(
        metadata={
            "name": "ContractTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    contract_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class HazardousIdentifiers:
    hazardous_regulations_coded: str = field(
        metadata={
            "name": "HazardousRegulationsCoded",
            "type": "Element",
            "required": True,
        }
    )
    hazardous_regulations_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousRegulationsCodedOther",
            "type": "Element",
        }
    )
    hazard_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardCode",
            "type": "Element",
        }
    )
    code_extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeExtension",
            "type": "Element",
        }
    )
    code_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "CodeVersion",
            "type": "Element",
        }
    )
    hazard_official_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardOfficialText",
            "type": "Element",
        }
    )
    trem_card_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "TremCardNum",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class HazardousPlacardInformation:
    hazardous_placard_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousPlacardIdentification",
            "type": "Element",
        }
    )
    hazardous_placard_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousPlacardText",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class HazardousShipmentInformation:
    hazard_packing_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardPackingCoded",
            "type": "Element",
        }
    )
    hazard_packing_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardPackingCodedOther",
            "type": "Element",
        }
    )
    hazardous_shipment_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousShipmentCoded",
            "type": "Element",
        }
    )
    hazardous_shipment_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousShipmentCodedOther",
            "type": "Element",
        }
    )
    hazardous_shipment_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousShipmentNote",
            "type": "Element",
        }
    )
    hazardous_zone_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousZoneCoded",
            "type": "Element",
        }
    )
    hazardous_zone_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardousZoneCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class IdassignedBy:
    class Meta:
        name = "IDAssignedBy"

    idassigned_by_coded: str = field(
        metadata={
            "name": "IDAssignedByCoded",
            "type": "Element",
            "required": True,
        }
    )
    idassigned_by_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDAssignedByCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class LineItemNum:
    buyer_line_item_num: str = field(
        metadata={
            "name": "BuyerLineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    seller_line_item_num: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerLineItemNum",
            "type": "Element",
        }
    )


class LineItemNumberReferenceLineItemNumTypeCoded(Enum):
    BUYER = "Buyer"
    SELLER = "Seller"


@dataclass(kw_only=True)
class LineItemType:
    line_item_type_coded: str = field(
        metadata={
            "name": "LineItemTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemTypeCodedOther",
            "type": "Element",
        }
    )


class MonetaryLimitSignificanceCoded(Enum):
    OTHER = "Other"
    APPROXIMATELY = "Approximately"
    EQUAL_TO = "EqualTo"
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL_TO = "LessThanOrEqualTo"
    NOT_EQUAL_TO = "NotEqualTo"
    TRACE = "Trace"
    TRUE_VALUE = "TrueValue"
    OBSERVED_VALUE = "ObservedValue"
    OUT_OF_RANGE = "OutOfRange"


class PackageDocDocumentTypeCoded(Enum):
    OTHER = "Other"
    CERTIFICATE_OF_ANALYSIS = "CertificateOfAnalysis"
    CERTIFICATE_OF_CONFORMITY = "CertificateOfConformity"
    CERTIFICATE_OF_QUALITY = "CertificateOfQuality"
    TEST_REPORT = "TestReport"
    PRODUCT_PERFORMANCE_REPORT = "ProductPerformanceReport"
    PRODUCT_SPECIFICATION_REPORT = "ProductSpecificationReport"
    PROCESS_DATA_REPORT = "ProcessDataReport"
    FIRST_SAMPLE_TEST_REPORT = "FirstSampleTestReport"
    PRICE_SALES_CATALOGUE = "PriceSalesCatalogue"
    PARTY_INFORMATION = "PartyInformation"
    FEDERAL_LABEL_APPROVAL = "FederalLabelApproval"
    MILL_CERTIFICATE = "MillCertificate"
    POST_RECEIPT = "PostReceipt"
    WEIGHT_CERTIFICATE = "WeightCertificate"
    WEIGHT_LIST = "WeightList"
    CERTIFICATE = "Certificate"
    COMBINED_CERTIFICATE_OF_VALUE_AND_ORIGIN = "CombinedCertificateOfValueAndOrigin"
    MOVEMENT_CERTIFICATE_ATR1 = "MovementCertificateATr1"
    CERTIFICATE_OF_QUANTITY = "CertificateOfQuantity"
    QUALITY_DATA_MESSAGE = "QualityDataMessage"
    QUERY = "Query"
    RESPONSE_TO_QUERY = "ResponseToQuery"
    STATUS_INFORMATION = "StatusInformation"
    RESTOW = "Restow"
    CONTAINER_DISCHARGE_LIST = "ContainerDischargeList"
    CORPORATE_SUPERANNUATION_CONTRIBUTIONS_ADVICE = "CorporateSuperannuationContributionsAdvice"
    INDUSTRY_SUPERANNUATION_CONTRIBUTIONS_ADVICE = "IndustrySuperannuationContributionsAdvice"
    CORPORATE_SUPERANNUATION_MEMBER_MAINTENANCE_MESSAGE = "CorporateSuperannuationMemberMaintenanceMessage"
    INDUSTRY_SUPERANNUATION_MEMBER_MAINTENANCE_MESSAGE = "IndustrySuperannuationMemberMaintenanceMessage"
    LIFE_INSURANCE_PAYROLL_DEDUCTIONS_ADVICE = "LifeInsurancePayrollDeductionsAdvice"
    UNDERBOND_REQUEST = "UnderbondRequest"
    UNDERBOND_APPROVAL = "UnderbondApproval"
    CERTIFICATE_OF_SEALING_OF_EXPORT_MEAT_LOCKERS = "CertificateOfSealingOfExportMeatLockers"
    CARGO_STATUS = "CargoStatus"
    INVENTORY_REPORT = "InventoryReport"
    IDENTITY_CARD = "IdentityCard"
    RESPONSE_TO_ATRADE_STATISTICS_MESSAGE = "ResponseToATradeStatisticsMessage"
    VACCINATION_CERTIFICATE = "VaccinationCertificate"
    PASSPORT = "Passport"
    DRIVING_LICENCE_NATIONAL = "DrivingLicenceNational"
    DRIVING_LICENCE_INTERNATIONAL = "DrivingLicenceInternational"
    FREE_PASS = "FreePass"
    SEASON_TICKET = "SeasonTicket"
    TRANSPORT_STATUS_REPORT = "TransportStatusReport"
    TRANSPORT_STATUS_REQUEST = "TransportStatusRequest"
    BANKING_STATUS = "BankingStatus"
    EXTRA_COMMUNITY_TRADE_STATISTICAL_DECLARATION = "Extra-CommunityTradeStatisticalDeclaration"
    WRITTEN_INSTRUCTIONS_IN_CONFORMANCE_WITH_ADR_ARTICLE_NUMBER = "WrittenInstructionsInConformanceWithAdrArticleNumber"
    DAMAGE_CERTIFICATION = "DamageCertification"
    VALIDATED_PRICED_TENDER = "ValidatedPricedTender"
    PRICE_SALES_CATALOGUE_RESPONSE = "PriceSalesCatalogueResponse"
    PRICE_NEGOTIATION_RESULT = "PriceNegotiationResult"
    SAFETY_AND_HAZARD_DATA_SHEET = "SafetyAndHazardDataSheet"
    LEGAL_STATEMENT_OF_AN_ACCOUNT = "LegalStatementOfAnAccount"
    LISTING_STATEMENT_OF_AN_ACCOUNT = "ListingStatementOfAnAccount"
    CLOSING_STATEMENT_OF_AN_ACCOUNT = "ClosingStatementOfAnAccount"
    TRANSPORT_EQUIPMENT_ON_HIRE_REPORT = "TransportEquipmentOn-HireReport"
    TRANSPORT_EQUIPMENT_OFF_HIRE_REPORT = "TransportEquipmentOff-HireReport"
    TREATMENT_NIL_OUTTURN = "Treatment-NilOutturn"
    TREATMENT_TIME_UP_UNDERBOND = "Treatment-Time-UpUnderbond"
    TREATMENT_UNDERBOND_BY_SEA = "Treatment-UnderbondBySea"
    TREATMENT_PERSONAL_EFFECT = "Treatment-PersonalEffect"
    TREATMENT_TIMBER = "Treatment-Timber"
    PRELIMINARY_CREDIT_ASSESSMENT = "PreliminaryCreditAssessment"
    CREDIT_COVER = "CreditCover"
    CURRENT_ACCOUNT = "CurrentAccount"
    COMMERCIAL_DISPUTE = "CommercialDispute"
    CHARGEBACK = "Chargeback"
    REASSIGNMENT = "Reassignment"
    COLLATERAL_ACCOUNT = "CollateralAccount"
    REQUEST_FOR_PAYMENT = "RequestForPayment"
    UNSHIP_PERMIT = "UnshipPermit"
    STATISTICAL_DEFINITIONS = "StatisticalDefinitions"
    STATISTICAL_DATA = "StatisticalData"
    REQUEST_FOR_STATISTICAL_DATA = "RequestForStatisticalData"
    CALL_OFF_DELIVERY = "Call-OffDelivery"
    CONSIGNMENT_STATUS_REPORT = "ConsignmentStatusReport"
    INVENTORY_MOVEMENT_ADVICE = "InventoryMovementAdvice"
    INVENTORY_STATUS_ADVICE = "InventoryStatusAdvice"
    DEBIT_NOTE_RELATED_TO_GOODS_OR_SERVICES = "DebitNoteRelatedToGoodsOrServices"
    CREDIT_NOTE_RELATED_TO_GOODS_OR_SERVICES = "CreditNoteRelatedToGoodsOrServices"
    METERED_SERVICES_INVOICE = "MeteredServicesInvoice"
    CREDIT_NOTE_RELATED_TO_FINANCIAL_ADJUSTMENTS = "CreditNoteRelatedToFinancialAdjustments"
    DEBIT_NOTE_RELATED_TO_FINANCIAL_ADJUSTMENTS = "DebitNoteRelatedToFinancialAdjustments"
    CUSTOMS_MANIFEST = "CustomsManifest"
    VESSEL_UNPACK_REPORT = "VesselUnpackReport"
    GENERAL_CARGO_SUMMARY_MANIFEST_REPORT = "GeneralCargoSummaryManifestReport"
    CONSIGNMENT_UNPACK_REPORT = "ConsignmentUnpackReport"
    MEAT_AND_MEAT_BY_PRODUCTS_SANITARY_CERTIFICATE = "MeatAndMeatBy-ProductsSanitaryCertificate"
    MEAT_FOOD_PRODUCTS_SANITARY_CERTIFICATE = "MeatFoodProductsSanitaryCertificate"
    POULTRY_SANITARY_CERTIFICATE = "PoultrySanitaryCertificate"
    HORSEMEAT_SANITARY_CERTIFICATE = "HorsemeatSanitaryCertificate"
    CASING_SANITARY_CERTIFICATE = "CasingSanitaryCertificate"
    PHARMACEUTICAL_SANITARY_CERTIFICATE = "PharmaceuticalSanitaryCertificate"
    INEDIBLE_SANITARY_CERTIFICATE = "InedibleSanitaryCertificate"
    IMPENDING_ARRIVAL = "ImpendingArrival"
    MEANS_OF_TRANSPORT_ADVICE = "MeansOfTransportAdvice"
    ARRIVAL_INFORMATION = "ArrivalInformation"
    CARGO_RELEASE_NOTIFICATION = "CargoReleaseNotification"
    EXCISE_CERTIFICATE = "ExciseCertificate"
    REGISTRATION_DOCUMENT = "RegistrationDocument"
    TAX_NOTIFICATION = "TaxNotification"
    TRANSPORT_EQUIPMENT_DIRECT_INTERCHANGE_REPORT = "TransportEquipmentDirectInterchangeReport"
    TRANSPORT_EQUIPMENT_IMPENDING_ARRIVAL_ADVICE = "TransportEquipmentImpendingArrivalAdvice"
    PURCHASE_ORDER = "PurchaseOrder"
    TRANSPORT_EQUIPMENT_DAMAGE_REPORT = "TransportEquipmentDamageReport"
    TRANSPORT_EQUIPMENT_MAINTENANCE_AND_REPAIR_WORK_ESTIMATE_ADVICE = "TransportEquipmentMaintenanceAndRepairWorkEstimateAdvice"
    TRANSPORT_EQUIPMENT_EMPTY_RELEASE_INSTRUCTION = "TransportEquipmentEmptyReleaseInstruction"
    TRANSPORT_MOVEMENT_GATE_IN_REPORT = "TransportMovementGateInReport"
    MANUFACTURING_INSTRUCTIONS = "ManufacturingInstructions"
    TRANSPORT_MOVEMENT_GATE_OUT_REPORT = "TransportMovementGateOutReport"
    TRANSPORT_EQUIPMENT_UNPACKING_INSTRUCTION = "TransportEquipmentUnpackingInstruction"
    TRANSPORT_EQUIPMENT_UNPACKING_REPORT = "TransportEquipmentUnpackingReport"
    TRANSPORT_EQUIPMENT_PICK_UP_AVAILABILITY_REQUEST = "TransportEquipmentPick-UpAvailabilityRequest"
    TRANSPORT_EQUIPMENT_PICK_UP_AVAILABILITY_CONFIRMATION = "TransportEquipmentPick-UpAvailabilityConfirmation"
    TRANSPORT_EQUIPMENT_PICK_UP_REPORT = "TransportEquipmentPick-UpReport"
    TRANSPORT_EQUIPMENT_SHIFT_REPORT = "TransportEquipmentShiftReport"
    TRANSPORT_DISCHARGE_INSTRUCTION = "TransportDischargeInstruction"
    TRANSPORT_DISCHARGE_REPORT = "TransportDischargeReport"
    STORES_REQUISITION = "StoresRequisition"
    TRANSPORT_LOADING_INSTRUCTION = "TransportLoadingInstruction"
    TRANSPORT_LOADING_REPORT = "TransportLoadingReport"
    TRANSPORT_EQUIPMENT_MAINTENANCE_AND_REPAIR_WORK = "TransportEquipmentMaintenanceAndRepairWork"
    TRANSPORT_DEPARTURE_REPORT = "TransportDepartureReport"
    TRANSPORT_EMPTY_EQUIPMENT_ADVICE = "TransportEmptyEquipmentAdvice"
    TRANSPORT_EQUIPMENT_ACCEPTANCE_ORDER = "TransportEquipmentAcceptanceOrder"
    TRANSPORT_EQUIPMENT_SPECIAL_SERVICE_INSTRUCTION = "TransportEquipmentSpecialServiceInstruction"
    TRANSPORT_EQUIPMENT_STOCK_REPORT = "TransportEquipmentStockReport"
    TRANSPORT_CARGO_RELEASE_ORDER = "TransportCargoReleaseOrder"
    INVOICING_DATA_SHEET = "InvoicingDataSheet"
    TRANSPORT_EQUIPMENT_PACKING_INSTRUCTION = "TransportEquipmentPackingInstruction"
    CUSTOMS_CLEARANCE_NOTICE = "CustomsClearanceNotice"
    CUSTOMS_DOCUMENTS_EXPIRATION_NOTICE = "CustomsDocumentsExpirationNotice"
    TRANSPORT_EQUIPMENT_ON_HIRE_REQUEST = "TransportEquipmentOn-HireRequest"
    TRANSPORT_EQUIPMENT_ON_HIRE_ORDER = "TransportEquipmentOn-HireOrder"
    TRANSPORT_EQUIPMENT_OFF_HIRE_REQUEST = "TransportEquipmentOff-HireRequest"
    TRANSPORT_EQUIPMENT_SURVEY_ORDER = "TransportEquipmentSurveyOrder"
    TRANSPORT_EQUIPMENT_SURVEY_ORDER_RESPONSE = "TransportEquipmentSurveyOrderResponse"
    TRANSPORT_EQUIPMENT_SURVEY_REPORT = "TransportEquipmentSurveyReport"
    PACKING_INSTRUCTIONS = "PackingInstructions"
    ADVISING_ITEMS_TO_BE_BOOKED_TO_AFINANCIAL_ACCOUNT = "AdvisingItemsToBeBookedToAFinancialAccount"
    TRANSPORT_EQUIPMENT_MAINTENANCE_AND_REPAIR_WORK_ESTIMATE_ORDER = "TransportEquipmentMaintenanceAndRepairWorkEstimateOrder"
    TRANSPORT_EQUIPMENT_MAINTENANCE_AND_REPAIR_NOTICE = "TransportEquipmentMaintenanceAndRepairNotice"
    EMPTY_CONTAINER_DISPOSITION_ORDER = "EmptyContainerDispositionOrder"
    CARGO_VESSEL_DISCHARGE_ORDER = "CargoVesselDischargeOrder"
    CARGO_VESSEL_LOADING_ORDER = "CargoVesselLoadingOrder"
    MULTIDROP_ORDER = "MultidropOrder"
    BAILMENT_CONTRACT = "BailmentContract"
    BASIC_AGREEMENT = "BasicAgreement"
    INTERNAL_TRANSPORT_ORDER = "InternalTransportOrder"
    GRANT = "Grant"
    INDEFINITE_DELIVERY_INDEFINITE_QUANTITY_CONTRACT = "IndefiniteDeliveryIndefiniteQuantityContract"
    INDEFINITE_DELIVERY_DEFINITE_QUANTITY_CONTRACT = "IndefiniteDeliveryDefiniteQuantityContract"
    REQUIREMENTS_CONTRACT = "RequirementsContract"
    TASK_ORDER = "TaskOrder"
    MAKE_OR_BUY_PLAN = "MakeOrBuyPlan"
    SUBCONTRACTOR_PLAN = "SubcontractorPlan"
    COST_DATA_SUMMARY = "CostDataSummary"
    CERTIFIED_COST_AND_PRICE_DATA = "CertifiedCostAndPriceData"
    WAGE_DETERMINATION = "WageDetermination"
    CONTRACT_FUNDS_STATUS_REPORT_CFSR = "ContractFundsStatusReportCfsr"
    CERTIFIED_INSPECTION_AND_TEST_RESULTS = "CertifiedInspectionAndTestResults"
    MATERIAL_INSPECTION_AND_RECEIVING_REPORT = "MaterialInspectionAndReceivingReport"
    PURCHASING_SPECIFICATION = "PurchasingSpecification"
    PAYMENT_OR_PERFORMANCE_BOND = "PaymentOrPerformanceBond"
    CONTRACT_SECURITY_CLASSIFICATION_SPECIFICATION = "ContractSecurityClassificationSpecification"
    MANUFACTURING_SPECIFICATION = "ManufacturingSpecification"
    BUY_AMERICA_CERTIFICATE_OF_COMPLIANCE = "BuyAmericaCertificateOfCompliance"
    CONTAINER_OFF_HIRE_NOTICE = "ContainerOff-HireNotice"
    CARGO_ACCEPTANCE_ORDER = "CargoAcceptanceOrder"
    PICK_UP_NOTICE = "Pick-UpNotice"
    AUTHORISATION_TO_PLAN_AND_SUGGEST_ORDERS = "AuthorisationToPlanAndSuggestOrders"
    AUTHORISATION_TO_PLAN_AND_SHIP_ORDERS = "AuthorisationToPlanAndShipOrders"
    DRAWING = "Drawing"
    COST_PERFORMANCE_REPORT_CPR_FORMAT2 = "CostPerformanceReportCprFormat2"
    COST_SCHEDULE_STATUS_REPORT_CSSR = "CostScheduleStatusReportCssr"
    COST_PERFORMANCE_REPORT_CPR_FORMAT1 = "CostPerformanceReportCprFormat1"
    COST_PERFORMANCE_REPORT_CPR_FORMAT3 = "CostPerformanceReportCprFormat3"
    COST_PERFORMANCE_REPORT_CPR_FORMAT4 = "CostPerformanceReportCprFormat4"
    COST_PERFORMANCE_REPORT_CPR_FORMAT5 = "CostPerformanceReportCprFormat5"
    PROGRESSIVE_DISCHARGE_REPORT = "ProgressiveDischargeReport"
    BALANCE_CONFIRMATION = "BalanceConfirmation"
    CONTAINER_STRIPPING_ORDER = "ContainerStrippingOrder"
    CONTAINER_STUFFING_ORDER = "ContainerStuffingOrder"
    CONVEYANCE_DECLARATION_ARRIVAL = "ConveyanceDeclarationArrival"
    CONVEYANCE_DECLARATION_DEPARTURE = "ConveyanceDeclarationDeparture"
    CONVEYANCE_DECLARATION_COMBINED = "ConveyanceDeclarationCombined"
    PROJECT_RECOVERY_PLAN = "ProjectRecoveryPlan"
    PROJECT_PRODUCTION_PLAN = "ProjectProductionPlan"
    STATISTICAL_AND_OTHER_ADMINISTRATIVE_INTERNAL_DOCUMENTS = "StatisticalAndOtherAdministrativeInternalDocuments"
    PROJECT_MASTER_SCHEDULE = "ProjectMasterSchedule"
    PRICED_ALTERNATE_TENDER_BILL_OF_QUANTITY = "PricedAlternateTenderBillOfQuantity"
    ESTIMATED_PRICED_BILL_OF_QUANTITY = "EstimatedPricedBillOfQuantity"
    DRAFT_BILL_OF_QUANTITY = "DraftBillOfQuantity"
    DOCUMENTARY_CREDIT_COLLECTION_INSTRUCTION = "DocumentaryCreditCollectionInstruction"
    REQUEST_FOR_AN_AMENDMENT_OF_ADOCUMENTARY_CREDIT = "RequestForAnAmendmentOfADocumentaryCredit"
    DOCUMENTARY_CREDIT_AMENDMENT_INFORMATION = "DocumentaryCreditAmendmentInformation"
    ADVICE_OF_AN_AMENDMENT_OF_ADOCUMENTARY_CREDIT = "AdviceOfAnAmendmentOfADocumentaryCredit"
    RESPONSE_TO_AN_AMENDMENT_OF_ADOCUMENTARY_CREDIT = "ResponseToAnAmendmentOfADocumentaryCredit"
    DOCUMENTARY_CREDIT_ISSUANCE_INFORMATION = "DocumentaryCreditIssuanceInformation"
    DIRECT_PAYMENT_VALUATION_REQUEST = "DirectPaymentValuationRequest"
    DIRECT_PAYMENT_VALUATION = "DirectPaymentValuation"
    PROVISIONAL_PAYMENT_VALUATION = "ProvisionalPaymentValuation"
    PAYMENT_VALUATION = "PaymentValuation"
    QUANTITY_VALUATION = "QuantityValuation"
    QUANTITY_VALUATION_REQUEST = "QuantityValuationRequest"
    CONTRACT_BILL_OF_QUANTITIES_BOQ = "ContractBillOfQuantities-Boq"
    UNPRICED_BILL_OF_QUANTITY = "UnpricedBillOfQuantity"
    PRICED_TENDER_BOQ = "PricedTenderBoq"
    ENQUIRY = "Enquiry"
    INTERIM_APPLICATION_FOR_PAYMENT = "InterimApplicationForPayment"
    AGREEMENT_TO_PAY = "AgreementToPay"
    REQUEST_FOR_FINANCIAL_CANCELLATION = "RequestForFinancialCancellation"
    PRE_AUTHORISED_DIRECT_DEBITS = "Pre-AuthorisedDirectDebits"
    LETTER_OF_INTENT = "LetterOfIntent"
    APPROVED_UNPRICED_BILL_OF_QUANTITY = "ApprovedUnpricedBillOfQuantity"
    PAYMENT_VALUATION_FOR_UNSCHEDULED_ITEMS = "PaymentValuationForUnscheduledItems"
    FINAL_PAYMENT_REQUEST_BASED_ON_COMPLETION_OF_WORK = "FinalPaymentRequestBasedOnCompletionOfWork"
    PAYMENT_REQUEST_FOR_COMPLETED_UNITS = "PaymentRequestForCompletedUnits"
    ORDER = "Order"
    BLANKET_ORDER = "BlanketOrder"
    SPOT_ORDER = "SpotOrder"
    LEASE_ORDER = "LeaseOrder"
    RUSH_ORDER = "RushOrder"
    REPAIR_ORDER = "RepairOrder"
    CALL_OFF_ORDER = "CallOffOrder"
    CONSIGNMENT_ORDER = "ConsignmentOrder"
    SAMPLE_ORDER = "SampleOrder"
    SWAP_ORDER = "SwapOrder"
    PURCHASE_ORDER_CHANGE_REQUEST = "PurchaseOrderChangeRequest"
    PURCHASE_ORDER_RESPONSE = "PurchaseOrderResponse"
    HIRE_ORDER = "HireOrder"
    SPARE_PARTS_ORDER = "SparePartsOrder"
    CAMPAIGN_PRICE_SALES_CATALOGUE = "CampaignPriceSalesCatalogue"
    CONTAINER_LIST = "ContainerList"
    DELIVERY_FORECAST = "DeliveryForecast"
    CROSS_DOCKING_SERVICES_ORDER = "CrossDockingServicesOrder"
    NON_PRE_AUTHORISED_DIRECT_DEBITS = "Non-Pre-AuthorisedDirectDebits"
    REJECTED_DIRECT_DEBITS = "RejectedDirectDebits"
    DELIVERY_INSTRUCTIONS = "DeliveryInstructions"
    DELIVERY_SCHEDULE = "DeliverySchedule"
    DELIVERY_JUST_IN_TIME = "DeliveryJust-In-Time"
    PRE_AUTHORISED_DIRECT_DEBIT_REQUESTS = "Pre-AuthorisedDirectDebitRequests"
    NON_PRE_AUTHORISED_DIRECT_DEBIT_REQUESTS = "Non-Pre-AuthorisedDirectDebitRequests"
    DELIVERY_RELEASE = "DeliveryRelease"
    SETTLEMENT_OF_ALETTER_OF_CREDIT = "SettlementOfALetterOfCredit"
    BANK_TO_BANK_FUNDS_TRANSFER = "BankToBankFundsTransfer"
    CUSTOMER_PAYMENT_ORDERS = "CustomerPaymentOrders"
    LOW_VALUE_PAYMENT_ORDERS = "LowValuePaymentOrders"
    CREW_LIST_DECLARATION = "CrewListDeclaration"
    INQUIRY = "Inquiry"
    RESPONSE_TO_PREVIOUS_BANKING_STATUS_MESSAGE = "ResponseToPreviousBankingStatusMessage"
    PROJECT_MASTER_PLAN = "ProjectMasterPlan"
    PROJECT_PLAN = "ProjectPlan"
    PROJECT_SCHEDULE = "ProjectSchedule"
    PROJECT_PLANNING_AVAILABLE_RESOURCES = "ProjectPlanningAvailableResources"
    PROJECT_PLANNING_CALENDAR = "ProjectPlanningCalendar"
    STANDING_ORDER = "StandingOrder"
    CARGO_MOVEMENT_EVENT_LOG = "CargoMovementEventLog"
    CARGO_ANALYSIS_VOYAGE_REPORT = "CargoAnalysisVoyageReport"
    SELF_BILLED_CREDIT_NOTE = "SelfBilledCreditNote"
    CONSOLIDATED_CREDIT_NOTE_GOODS_AND_SERVICES = "ConsolidatedCreditNote-GoodsAndServices"
    INVENTORY_ADJUSTMENT_STATUS_REPORT = "InventoryAdjustmentStatusReport"
    TRANSPORT_EQUIPMENT_MOVEMENT_INSTRUCTION = "TransportEquipmentMovementInstruction"
    TRANSPORT_EQUIPMENT_MOVEMENT_REPORT = "TransportEquipmentMovementReport"
    TRANSPORT_EQUIPMENT_STATUS_CHANGE_REPORT = "TransportEquipmentStatusChangeReport"
    FUMIGATION_CERTIFICATE = "FumigationCertificate"
    WINE_CERTIFICATE = "WineCertificate"
    WOOL_HEALTH_CERTIFICATE = "WoolHealthCertificate"
    DELIVERY_NOTE = "DeliveryNote"
    PACKING_LIST = "PackingList"
    NEW_CODE_REQUEST = "NewCodeRequest"
    CODE_CHANGE_REQUEST = "CodeChangeRequest"
    SIMPLE_DATA_ELEMENT_REQUEST = "SimpleDataElementRequest"
    SIMPLE_DATA_ELEMENT_CHANGE_REQUEST = "SimpleDataElementChangeRequest"
    COMPOSITE_DATA_ELEMENT_REQUEST = "CompositeDataElementRequest"
    COMPOSITE_DATA_ELEMENT_CHANGE_REQUEST = "CompositeDataElementChangeRequest"
    SEGMENT_REQUEST = "SegmentRequest"
    SEGMENT_CHANGE_REQUEST = "SegmentChangeRequest"
    NEW_MESSAGE_REQUEST = "NewMessageRequest"
    MESSAGE_IN_DEVELOPMENT_REQUEST = "MessageInDevelopmentRequest"
    MODIFICATION_OF_EXISTING_MESSAGE = "ModificationOfExistingMessage"
    TRACKING_NUMBER_ASSIGNMENT_REPORT = "TrackingNumberAssignmentReport"
    USER_DIRECTORY_DEFINITION = "UserDirectoryDefinition"
    UNITED_NATIONS_STANDARD_MESSAGE_REQUEST = "UnitedNationsStandardMessageRequest"
    SERVICE_DIRECTORY_DEFINITION = "ServiceDirectoryDefinition"
    STATUS_REPORT = "StatusReport"
    KANBAN_SCHEDULE = "KanbanSchedule"
    PRODUCT_DATA_MESSAGE = "ProductDataMessage"
    ACLAIM_FOR_PARTS_AND_OR_LABOUR_CHARGES = "AClaimForPartsAndOrLabourCharges"
    DELIVERY_SCHEDULE_RESPONSE = "DeliveryScheduleResponse"
    INSPECTION_REQUEST = "InspectionRequest"
    INSPECTION_REPORT = "InspectionReport"
    APPLICATION_ACKNOWLEDGEMENT_AND_ERROR_REPORT = "ApplicationAcknowledgementAndErrorReport"
    PRICE_VARIATION_INVOICE = "PriceVariationInvoice"
    CREDIT_NOTE_FOR_PRICE_VARIATION = "CreditNoteForPriceVariation"
    INSTRUCTION_TO_COLLECT = "InstructionToCollect"
    DANGEROUS_GOODS_LIST = "DangerousGoodsList"
    REGISTRATION_RENEWAL = "RegistrationRenewal"
    REGISTRATION_CHANGE = "RegistrationChange"
    RESPONSE_TO_REGISTRATION = "ResponseToRegistration"
    IMPLEMENTATION_GUIDELINE = "ImplementationGuideline"
    REQUEST_FOR_TRANSFER = "RequestForTransfer"
    COST_PERFORMANCE_REPORT = "CostPerformanceReport"
    APPLICATION_ERROR_AND_ACKNOWLEDGEMENT = "ApplicationErrorAndAcknowledgement"
    CASH_POOL_FINANCIAL_STATEMENT = "CashPoolFinancialStatement"
    SEQUENCED_DELIVERY_SCHEDULE = "SequencedDeliverySchedule"
    DELCREDERE_CREDIT_NOTE = "DelcredereCreditNote"
    OFFER_QUOTATION = "OfferQuotation"
    REQUEST_FOR_QUOTE = "RequestForQuote"
    ACKNOWLEDGEMENT_MESSAGE = "AcknowledgementMessage"
    APPLICATION_ERROR_MESSAGE = "ApplicationErrorMessage"
    CARGO_MOVEMENT_VOYAGE_SUMMARY = "CargoMovementVoyageSummary"
    CONTRACT = "Contract"
    APPLICATION_FOR_USAGE_OF_BERTH_OR_MOORING_FACILITIES = "ApplicationForUsageOfBerthOrMooringFacilities"
    APPLICATION_FOR_DESIGNATION_OF_BERTHING_PLACES = "ApplicationForDesignationOfBerthingPlaces"
    APPLICATION_FOR_SHIFTING_FROM_THE_DESIGNATED_PLACE_IN_PORT = "ApplicationForShiftingFromTheDesignatedPlaceInPort"
    SUPPLEMENTARY_DOCUMENT_FOR_APPLICATION_FOR_CARGO_OPERATION_OF_DANGEROUS_GOODS = "SupplementaryDocumentForApplicationForCargoOperationOfDangerousGoods"
    ACKNOWLEDGEMENT_OF_ORDER = "AcknowledgementOfOrder"
    SUPPLEMENTARY_DOCUMENT_FOR_APPLICATION_FOR_TRANSPORT_OF_DANGEROUS_GOODS = "SupplementaryDocumentForApplicationForTransportOfDangerousGoods"
    OPTICAL_CHARACTER_READING_OCR_PAYMENT = "OpticalCharacterReadingOcrPayment"
    PRELIMINARY_SALES_REPORT = "PreliminarySalesReport"
    TRANSPORT_EMERGENCY_CARD = "TransportEmergencyCard"
    PROFORMA_INVOICE = "ProformaInvoice"
    PARTIAL_INVOICE = "PartialInvoice"
    OPERATING_INSTRUCTIONS = "OperatingInstructions"
    NAME_PRODUCT_PLATE = "NameProductPlate"
    CO_INSURANCE_CEDING_BORDEREAU = "Co-InsuranceCedingBordereau"
    REQUEST_FOR_DELIVERY_INSTRUCTIONS = "RequestForDeliveryInstructions"
    COMMERCIAL_INVOICE_WHICH_INCLUDES_APACKING_LIST = "CommercialInvoiceWhichIncludesAPackingList"
    TRADE_DATA = "TradeData"
    CUSTOMS_DECLARATION_FOR_CARGO_EXAMINATION = "CustomsDeclarationForCargoExamination"
    CUSTOMS_DECLARATION_FOR_CARGO_EXAMINATION_ALTERNATE = "CustomsDeclarationForCargoExaminationAlternate"
    BOOKING_REQUEST = "BookingRequest"
    CUSTOMS_CREW_AND_CONVEYANCE = "CustomsCrewAndConveyance"
    CUSTOMS_SUMMARY_DECLARATION_WITH_COMMERCIAL_DETAIL_ALTERNATE = "CustomsSummaryDeclarationWithCommercialDetailAlternate"
    ITEMS_BOOKED_TO_AFINANCIAL_ACCOUNT_REPORT = "ItemsBookedToAFinancialAccountReport"
    REPORT_OF_TRANSACTIONS_WHICH_NEED_FURTHER_INFORMATION_FROM_THE_RECEIVER = "ReportOfTransactionsWhichNeedFurtherInformationFromTheReceiver"
    SHIPPING_INSTRUCTIONS = "ShippingInstructions"
    SHIPPERS_LETTER_OF_INSTRUCTIONS_AIR = "ShippersLetterOfInstructionsAir"
    REPORT_OF_TRANSACTIONS_FOR_INFORMATION_ONLY = "ReportOfTransactionsForInformationOnly"
    CARTAGE_ORDER_LOCAL_TRANSPORT = "CartageOrderLocalTransport"
    EDI_ASSOCIATED_OBJECT_ADMINISTRATION_MESSAGE = "EdiAssociatedObjectAdministrationMessage"
    READY_FOR_DESPATCH_ADVICE = "ReadyForDespatchAdvice"
    SUMMARY_SALES_REPORT = "SummarySalesReport"
    ORDER_STATUS_ENQUIRY = "OrderStatusEnquiry"
    ORDER_STATUS_REPORT = "OrderStatusReport"
    DECLARATION_REGARDING_THE_INWARD_AND_OUTWARD_MOVEMENT_OF_VESSEL = "DeclarationRegardingTheInwardAndOutwardMovementOfVessel"
    DESPATCH_ORDER = "DespatchOrder"
    DESPATCH_ADVICE = "DespatchAdvice"
    NOTIFICATION_OF_USAGE_OF_BERTH_OR_MOORING_FACILITIES = "NotificationOfUsageOfBerthOrMooringFacilities"
    APPLICATION_FOR_VESSELS_ENTERING_INTO_PORT_AREA_IN_NIGHT_TIME = "ApplicationForVesselsEnteringIntoPortAreaInNight-Time"
    NOTIFICATION_OF_EMERGENCY_SHIFTING_FROM_THE_DESIGNATED_PLACE_IN_PORT = "NotificationOfEmergencyShiftingFromTheDesignatedPlaceInPort"
    CUSTOMS_SUMMARY_DECLARATION_WITHOUT_COMMERCIAL_DETAIL_ALTERNATE = "CustomsSummaryDeclarationWithoutCommercialDetailAlternate"
    PERFORMANCE_BOND = "PerformanceBond"
    PAYMENT_BOND = "PaymentBond"
    ADVICE_OF_DISTRIBUTION_OF_DOCUMENTS = "AdviceOfDistributionOfDocuments"
    COMMERCIAL_INVOICE = "CommercialInvoice"
    CREDIT_NOTE = "CreditNote"
    COMMISSION_NOTE = "CommissionNote"
    DEBIT_NOTE = "DebitNote"
    CORRECTED_INVOICE = "CorrectedInvoice"
    CONSOLIDATED_INVOICE = "ConsolidatedInvoice"
    PREPAYMENT_INVOICE = "PrepaymentInvoice"
    HIRE_INVOICE = "HireInvoice"
    TAX_INVOICE = "TaxInvoice"
    SELF_BILLED_INVOICE = "Self-BilledInvoice"
    DELCREDERE_INVOICE = "DelcredereInvoice"
    FACTORED_INVOICE = "FactoredInvoice"
    LEASE_INVOICE = "LeaseInvoice"
    CONSIGNMENT_INVOICE = "ConsignmentInvoice"
    FACTORED_CREDIT_NOTE = "FactoredCreditNote"
    COMMERCIAL_ACCOUNT_SUMMARY_RESPONSE = "CommercialAccountSummaryResponse"
    CROSS_DOCKING_DESPATCH_ADVICE = "CrossDockingDespatchAdvice"
    TRANSSHIPMENT_DESPATCH_ADVICE = "TransshipmentDespatchAdvice"
    EXCEPTIONAL_ORDER = "ExceptionalOrder"
    TRANSSHIPMENT_ORDER = "TransshipmentOrder"
    CROSS_DOCKING_ORDER = "CrossDockingOrder"
    MEANS_OF_TRANSPORTATION_AVAILABILITY_INFORMATION = "MeansOfTransportationAvailabilityInformation"
    MEANS_OF_TRANSPORTATION_SCHEDULE_INFORMATION = "MeansOfTransportationScheduleInformation"
    TRANSPORT_EQUIPMENT_DELIVERY_NOTICE = "TransportEquipmentDeliveryNotice"
    INSTRUCTIONS_FOR_BANK_TRANSFER = "InstructionsForBankTransfer"
    APPLICATION_FOR_BANKERS_DRAFT = "ApplicationForBankersDraft"
    COLLECTION_PAYMENT_ADVICE = "CollectionPaymentAdvice"
    DOCUMENTARY_CREDIT_PAYMENT_ADVICE = "DocumentaryCreditPaymentAdvice"
    DOCUMENTARY_CREDIT_ACCEPTANCE_ADVICE = "DocumentaryCreditAcceptanceAdvice"
    DOCUMENTARY_CREDIT_NEGOTIATION_ADVICE = "DocumentaryCreditNegotiationAdvice"
    APPLICATION_FOR_BANKERS_GUARANTEE = "ApplicationForBankersGuarantee"
    BANKERS_GUARANTEE = "BankersGuarantee"
    DOCUMENTARY_CREDIT_LETTER_OF_INDEMNITY = "DocumentaryCreditLetterOfIndemnity"
    PREADVICE_OF_ACREDIT = "PreadviceOfACredit"
    COLLECTION_ORDER = "CollectionOrder"
    DOCUMENTS_PRESENTATION_FORM = "DocumentsPresentationForm"
    PAYMENT_ORDER = "PaymentOrder"
    EXTENDED_PAYMENT_ORDER = "ExtendedPaymentOrder"
    MULTIPLE_PAYMENT_ORDER = "MultiplePaymentOrder"
    CREDIT_ADVICE = "CreditAdvice"
    EXTENDED_CREDIT_ADVICE = "ExtendedCreditAdvice"
    DEBIT_ADVICE = "DebitAdvice"
    REVERSAL_OF_DEBIT = "ReversalOfDebit"
    REVERSAL_OF_CREDIT = "ReversalOfCredit"
    DOCUMENTARY_CREDIT_APPLICATION = "DocumentaryCreditApplication"
    DOCUMENTARY_CREDIT = "DocumentaryCredit"
    DOCUMENTARY_CREDIT_NOTIFICATION = "DocumentaryCreditNotification"
    DOCUMENTARY_CREDIT_TRANSFER_ADVICE = "DocumentaryCreditTransferAdvice"
    DOCUMENTARY_CREDIT_AMENDMENT_NOTIFICATION = "DocumentaryCreditAmendmentNotification"
    DOCUMENTARY_CREDIT_AMENDMENT = "DocumentaryCreditAmendment"
    REMITTANCE_ADVICE = "RemittanceAdvice"
    BANKERS_DRAFT = "BankersDraft"
    BILL_OF_EXCHANGE = "BillOfExchange"
    PROMISSORY_NOTE = "PromissoryNote"
    FINANCIAL_STATEMENT_OF_ACCOUNT = "FinancialStatementOfAccount"
    STATEMENT_OF_ACCOUNT_MESSAGE = "StatementOfAccountMessage"
    INSURANCE_CERTIFICATE = "InsuranceCertificate"
    INSURANCE_POLICY = "InsurancePolicy"
    INSURANCE_DECLARATION_SHEET_BORDEREAU = "InsuranceDeclarationSheetBordereau"
    INSURERS_INVOICE = "InsurersInvoice"
    COVER_NOTE = "CoverNote"
    FORWARDING_INSTRUCTIONS = "ForwardingInstructions"
    FORWARDERS_ADVICE_TO_IMPORT_AGENT = "ForwardersAdviceToImportAgent"
    FORWARDERS_ADVICE_TO_EXPORTER = "ForwardersAdviceToExporter"
    FORWARDERS_INVOICE = "ForwardersInvoice"
    FORWARDERS_CERTIFICATE_OF_RECEIPT = "ForwardersCertificateOfReceipt"
    SHIPPING_NOTE = "ShippingNote"
    FORWARDERS_WAREHOUSE_RECEIPT = "ForwardersWarehouseReceipt"
    GOODS_RECEIPT = "GoodsReceipt"
    PORT_CHARGES_DOCUMENTS = "PortChargesDocuments"
    WAREHOUSE_WARRANT = "WarehouseWarrant"
    DELIVERY_ORDER = "DeliveryOrder"
    HANDLING_ORDER = "HandlingOrder"
    GATE_PASS = "GatePass"
    WAYBILL = "Waybill"
    UNIVERSAL_MULTIPURPOSE_TRANSPORT_DOCUMENT = "UniversalMultipurposeTransportDocument"
    GOODS_RECEIPT_CARRIAGE = "GoodsReceiptCarriage"
    HOUSE_WAYBILL = "HouseWaybill"
    MASTER_BILL_OF_LADING = "MasterBillOfLading"
    BILL_OF_LADING = "BillOfLading"
    BILL_OF_LADING_ORIGINAL = "BillOfLadingOriginal"
    BILL_OF_LADING_COPY = "BillOfLadingCopy"
    EMPTY_CONTAINER_BILL = "EmptyContainerBill"
    TANKER_BILL_OF_LADING = "TankerBillOfLading"
    SEA_WAYBILL = "SeaWaybill"
    INLAND_WATERWAY_BILL_OF_LADING = "InlandWaterwayBillOfLading"
    NON_NEGOTIABLE_MARITIME_TRANSPORT_DOCUMENT_GENERIC = "Non-NegotiableMaritimeTransportDocumentGeneric"
    MATES_RECEIPT = "MatesReceipt"
    HOUSE_BILL_OF_LADING = "HouseBillOfLading"
    LETTER_OF_INDEMNITY_FOR_NON_SURRENDER_OF_BILL_OF_LADING = "LetterOfIndemnityForNon-SurrenderOfBillOfLading"
    FORWARDERS_BILL_OF_LADING = "ForwardersBillOfLading"
    RAIL_CONSIGNMENT_NOTE_GENERIC_TERM = "RailConsignmentNoteGenericTerm"
    ROAD_LIST_SMGS = "RoadList-Smgs"
    ESCORT_OFFICIAL_RECOGNITION = "EscortOfficialRecognition"
    RECHARGING_DOCUMENT = "RechargingDocument"
    ROAD_CONSIGNMENT_NOTE = "RoadConsignmentNote"
    AIR_WAYBILL = "AirWaybill"
    MASTER_AIR_WAYBILL = "MasterAirWaybill"
    SUBSTITUTE_AIR_WAYBILL = "SubstituteAirWaybill"
    CREWS_EFFECTS_DECLARATION = "CrewsEffectsDeclaration"
    PASSENGER_LIST = "PassengerList"
    DELIVERY_NOTICE_RAIL_TRANSPORT = "DeliveryNoticeRailTransport"
    DESPATCH_NOTE_POST_PARCELS = "DespatchNotePostParcels"
    MULTIMODAL_COMBINED_TRANSPORT_DOCUMENT_GENERIC = "MultimodalCombinedTransportDocumentGeneric"
    THROUGH_BILL_OF_LADING = "ThroughBillOfLading"
    FORWARDERS_CERTIFICATE_OF_TRANSPORT = "ForwardersCertificateOfTransport"
    COMBINED_TRANSPORT_DOCUMENT_GENERIC = "CombinedTransportDocumentGeneric"
    MULTIMODAL_TRANSPORT_DOCUMENT_GENERIC = "MultimodalTransportDocumentGeneric"
    COMBINED_TRANSPORT_BILL_OF_LADING_MULTIMODAL_BILL_OF_LADING = "CombinedTransportBillOfLadingMultimodalBillOfLading"
    BOOKING_CONFIRMATION = "BookingConfirmation"
    CALLING_FORWARD_NOTICE = "CallingForwardNotice"
    FREIGHT_INVOICE = "FreightInvoice"
    ARRIVAL_NOTICE_GOODS = "ArrivalNoticeGoods"
    NOTICE_OF_CIRCUMSTANCES_PREVENTING_DELIVERY_GOODS = "NoticeOfCircumstancesPreventingDeliveryGoods"
    NOTICE_OF_CIRCUMSTANCES_PREVENTING_TRANSPORT_GOODS = "NoticeOfCircumstancesPreventingTransportGoods"
    DELIVERY_NOTICE_GOODS = "DeliveryNoticeGoods"
    CARGO_MANIFEST = "CargoManifest"
    FREIGHT_MANIFEST = "FreightManifest"
    BORDEREAU = "Bordereau"
    CONTAINER_MANIFEST_UNIT_PACKING_LIST = "ContainerManifestUnitPackingList"
    CHARGES_NOTE = "ChargesNote"
    ADVICE_OF_COLLECTION = "AdviceOfCollection"
    SAFETY_OF_SHIP_CERTIFICATE = "SafetyOfShipCertificate"
    SAFETY_OF_RADIO_CERTIFICATE = "SafetyOfRadioCertificate"
    SAFETY_OF_EQUIPMENT_CERTIFICATE = "SafetyOfEquipmentCertificate"
    CIVIL_LIABILITY_FOR_OIL_CERTIFICATE = "CivilLiabilityForOilCertificate"
    LOADLINE_DOCUMENT = "LoadlineDocument"
    DERAT_DOCUMENT = "DeratDocument"
    MARITIME_DECLARATION_OF_HEALTH = "MaritimeDeclarationOfHealth"
    CERTIFICATE_OF_REGISTRY = "CertificateOfRegistry"
    SHIPS_STORES_DECLARATION = "ShipsStoresDeclaration"
    EXPORT_LICENCE_APPLICATION_FOR = "ExportLicenceApplicationFor"
    EXPORT_LICENCE = "ExportLicence"
    EXCHANGE_CONTROL_DECLARATION_EXPORT = "ExchangeControlDeclarationExport"
    DESPATCH_NOTE_MODEL_T = "DespatchNoteModelT"
    DESPATCH_NOTE_MODEL_T1 = "DespatchNoteModelT1"
    DESPATCH_NOTE_MODEL_T2 = "DespatchNoteModelT2"
    CONTROL_DOCUMENT_T5 = "ControlDocumentT5"
    RE_SENDING_CONSIGNMENT_NOTE = "Re-SendingConsignmentNote"
    DESPATCH_NOTE_MODEL_T2_L = "DespatchNoteModelT2L"
    GOODS_DECLARATION_FOR_EXPORTATION = "GoodsDeclarationForExportation"
    CARGO_DECLARATION_DEPARTURE = "CargoDeclarationDeparture"
    APPLICATION_FOR_GOODS_CONTROL_CERTIFICATE = "ApplicationForGoodsControlCertificate"
    GOODS_CONTROL_CERTIFICATE = "GoodsControlCertificate"
    APPLICATION_FOR_PHYTOSANITARY_CERTIFICATE = "ApplicationForPhytosanitaryCertificate"
    PHYTOSANITARY_CERTIFICATE = "PhytosanitaryCertificate"
    SANITARY_CERTIFICATE = "SanitaryCertificate"
    VETERINARY_CERTIFICATE = "VeterinaryCertificate"
    APPLICATION_FOR_INSPECTION_CERTIFICATE = "ApplicationForInspectionCertificate"
    INSPECTION_CERTIFICATE = "InspectionCertificate"
    CERTIFICATE_OF_ORIGIN_APPLICATION_FOR = "CertificateOfOriginApplicationFor"
    CERTIFICATE_OF_ORIGIN = "CertificateOfOrigin"
    DECLARATION_OF_ORIGIN = "DeclarationOfOrigin"
    REGIONAL_APPELLATION_CERTIFICATE = "RegionalAppellationCertificate"
    PREFERENCE_CERTIFICATE_OF_ORIGIN = "PreferenceCertificateOfOrigin"
    CERTIFICATE_OF_ORIGIN_FORM_GSP = "CertificateOfOriginFormGsp"
    CONSULAR_INVOICE = "ConsularInvoice"
    DANGEROUS_GOODS_DECLARATION = "DangerousGoodsDeclaration"
    STATISTICAL_DOCUMENT_EXPORT = "StatisticalDocumentExport"
    INTRASTAT_DECLARATION = "IntrastatDeclaration"
    DELIVERY_VERIFICATION_CERTIFICATE = "DeliveryVerificationCertificate"
    IMPORT_LICENCE_APPLICATION_FOR = "ImportLicenceApplicationFor"
    IMPORT_LICENCE = "ImportLicence"
    CUSTOMS_DECLARATION_WITHOUT_COMMERCIAL_DETAIL = "CustomsDeclarationWithoutCommercialDetail"
    CUSTOMS_DECLARATION_WITH_COMMERCIAL_AND_ITEM_DETAIL = "CustomsDeclarationWithCommercialAndItemDetail"
    CUSTOMS_DECLARATION_WITHOUT_ITEM_DETAIL = "CustomsDeclarationWithoutItemDetail"
    RELATED_DOCUMENT = "RelatedDocument"
    RECEIPT_CUSTOMS = "ReceiptCustoms"
    APPLICATION_FOR_EXCHANGE_ALLOCATION = "ApplicationForExchangeAllocation"
    FOREIGN_EXCHANGE_PERMIT = "ForeignExchangePermit"
    EXCHANGE_CONTROL_DECLARATION_IMPORT = "ExchangeControlDeclarationImport"
    GOODS_DECLARATION_FOR_IMPORTATION = "GoodsDeclarationForImportation"
    GOODS_DECLARATION_FOR_HOME_USE = "GoodsDeclarationForHomeUse"
    CUSTOMS_IMMEDIATE_RELEASE_DECLARATION = "CustomsImmediateReleaseDeclaration"
    CUSTOMS_DELIVERY_NOTE = "CustomsDeliveryNote"
    CARGO_DECLARATION_ARRIVAL = "CargoDeclarationArrival"
    VALUE_DECLARATION = "ValueDeclaration"
    CUSTOMS_INVOICE = "CustomsInvoice"
    CUSTOMS_DECLARATION_POST_PARCELS = "CustomsDeclarationPostParcels"
    TAX_DECLARATION_VALUE_ADDED_TAX = "TaxDeclarationValueAddedTax"
    TAX_DECLARATION_GENERAL = "TaxDeclarationGeneral"
    TAX_DEMAND = "TaxDemand"
    EMBARGO_PERMIT = "EmbargoPermit"
    GOODS_DECLARATION_FOR_CUSTOMS_TRANSIT = "GoodsDeclarationForCustomsTransit"
    TIF_FORM = "TifForm"
    TIR_CARNET = "TirCarnet"
    EC_CARNET = "EcCarnet"
    EUR1_CERTIFICATE_OF_ORIGIN = "Eur1CertificateOfOrigin"
    ATA_CARNET = "AtaCarnet"
    SINGLE_ADMINISTRATIVE_DOCUMENT = "SingleAdministrativeDocument"
    GENERAL_RESPONSE_CUSTOMS = "GeneralResponseCustoms"
    DOCUMENT_RESPONSE_CUSTOMS = "DocumentResponseCustoms"
    ERROR_RESPONSE_CUSTOMS = "ErrorResponseCustoms"
    PACKAGE_RESPONSE_CUSTOMS = "PackageResponseCustoms"
    TAX_CALCULATION_CONFIRMATION_RESPONSE_CUSTOMS = "TaxCalculationConfirmationResponseCustoms"
    QUOTA_PRIOR_ALLOCATION_CERTIFICATE = "QuotaPriorAllocationCertificate"
    END_USE_AUTHORIZATION = "EndUseAuthorization"
    GOVERNMENT_CONTRACT = "GovernmentContract"
    STATISTICAL_DOCUMENT_IMPORT = "StatisticalDocumentImport"
    APPLICATION_FOR_DOCUMENTARY_CREDIT = "ApplicationForDocumentaryCredit"
    PREVIOUS_CUSTOMS_DOCUMENT_MESSAGE = "PreviousCustomsDocumentMessage"


@dataclass(kw_only=True)
class PackageIdentifier:
    package_identifier_coded: str = field(
        metadata={
            "name": "PackageIdentifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_identifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageIdentifierCodedOther",
            "type": "Element",
        }
    )
    package_identifier_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageIdentifierValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PackageMark:
    package_mark_coded: str = field(
        metadata={
            "name": "PackageMarkCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_mark_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageMarkCodedOther",
            "type": "Element",
        }
    )
    package_mark_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageMarkValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PercentQualifier:
    percent_qualifier_coded: str = field(
        metadata={
            "name": "PercentQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    percent_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PercentQualifierCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class RequestedResponse:
    requested_response_coded: str = field(
        metadata={
            "name": "RequestedResponseCoded",
            "type": "Element",
            "required": True,
        }
    )
    requested_response_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequestedResponseCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class RoundTripInformation:
    round_trip_order: str = field(
        init=False,
        default="true",
        metadata={
            "name": "RoundTripOrder",
            "type": "Attribute",
            "required": True,
        }
    )
    immutable: Optional[str] = field(
        default=None,
        metadata={
            "name": "Immutable",
            "type": "Element",
        }
    )
    re_link: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReLink",
            "type": "Element",
        }
    )
    supplier_shopping_cart_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierShoppingCartID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class SalesRequirement:
    sales_requirement_coded: str = field(
        metadata={
            "name": "SalesRequirementCoded",
            "type": "Element",
            "required": True,
        }
    )
    sales_requirement_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SalesRequirementCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class SpecialHandling:
    special_handling_coded: str = field(
        metadata={
            "name": "SpecialHandlingCoded",
            "type": "Element",
            "required": True,
        }
    )
    special_handling_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialHandlingCodedOther",
            "type": "Element",
        }
    )
    special_handling_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpecialHandlingNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class StandardCategoryId:
    class Meta:
        name = "StandardCategoryID"

    standard_category_type: str = field(
        metadata={
            "name": "StandardCategoryType",
            "type": "Element",
            "required": True,
        }
    )
    classification_id: str = field(
        metadata={
            "name": "ClassificationID",
            "type": "Element",
            "required": True,
        }
    )
    technical_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "TechnicalID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AccountCode:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AccountReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BasisQuantityRange:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BillToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BuyerParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Category:
    category_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "CategoryID",
            "type": "Element",
        }
    )
    standard_category_id: Optional[StandardCategoryId] = field(
        default=None,
        metadata={
            "name": "StandardCategoryID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CommodityCode:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ConditionsOfSale:
    sales_requirement: List[SalesRequirement] = field(
        default_factory=list,
        metadata={
            "name": "SalesRequirement",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    sales_action_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SalesActionCoded",
            "type": "Element",
        }
    )
    sales_action_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SalesActionCodedOther",
            "type": "Element",
        }
    )
    sales_action_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "SalesActionValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ContractId:
    class Meta:
        name = "ContractID"

    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Control:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CountryOfDestination:
    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CountryOfOrigin:
    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Description:
    description_text: str = field(
        metadata={
            "name": "DescriptionText",
            "type": "Element",
            "required": True,
        }
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Emergency:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FibranchCountry:
    class Meta:
        name = "FIBranchCountry"

    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FibranchRegion:
    class Meta:
        name = "FIBranchRegion"

    region: Region = field(
        metadata={
            "name": "Region",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FinalRecipient:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Flashpoint:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GrossVolume:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class HazardousContact:
    contact: Contact = field(
        metadata={
            "name": "Contact",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class HazardousReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ItemCharacteristic:
    item_characteristic_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemCharacteristicCoded",
            "type": "Element",
        }
    )
    item_characteristic_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemCharacteristicCodedOther",
            "type": "Element",
        }
    )
    surface_layer_position_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurfaceLayerPositionCoded",
            "type": "Element",
        }
    )
    surface_layer_position_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SurfaceLayerPositionCodedOther",
            "type": "Element",
        }
    )
    item_characteristic_value: str = field(
        metadata={
            "name": "ItemCharacteristicValue",
            "type": "Element",
            "required": True,
        }
    )
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
        }
    )
    unit_of_measurement: Optional[UnitOfMeasurement] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
        }
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class LineItemAttachments:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LineItemNumberReference:
    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    line_item_num_type_coded: LineItemNumberReferenceLineItemNumTypeCoded = field(
        default=LineItemNumberReferenceLineItemNumTypeCoded.BUYER,
        metadata={
            "name": "LineItemNumTypeCoded",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfHazardousIdentifiers:
    hazardous_identifiers: List[HazardousIdentifiers] = field(
        default_factory=list,
        metadata={
            "name": "HazardousIdentifiers",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfItemReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfNameValuePair:
    name_value_pair: List[NameValuePair] = field(
        default_factory=list,
        metadata={
            "name": "NameValuePair",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfPackageIdentifier:
    package_identifier: List[PackageIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "PackageIdentifier",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfPackageMark:
    package_mark: List[PackageMark] = field(
        default_factory=list,
        metadata={
            "name": "PackageMark",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfTemperatureCoded:
    list_of_dimension: ListOfDimension = field(
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfTransport:
    transport: List[Transport] = field(
        default_factory=list,
        metadata={
            "name": "Transport",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class MaxBackOrderQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MessageId:
    class Meta:
        name = "MessageID"

    idnumber: str = field(
        metadata={
            "name": "IDNumber",
            "type": "Element",
            "required": True,
        }
    )
    idassigned_by: IdassignedBy = field(
        metadata={
            "name": "IDAssignedBy",
            "type": "Element",
            "required": True,
        }
    )
    idassigned_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "IDAssignedDate",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class MonetaryLimit:
    significance_coded: Optional[MonetaryLimitSignificanceCoded] = field(
        default=None,
        metadata={
            "name": "SignificanceCoded",
            "type": "Attribute",
        }
    )
    significance_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "SignificanceCodedOther",
            "type": "Attribute",
        }
    )
    monetary_limit_value: str = field(
        metadata={
            "name": "MonetaryLimitValue",
            "type": "Element",
            "required": True,
        }
    )
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MonetaryRange:
    minimum_monetary_value: str = field(
        metadata={
            "name": "MinimumMonetaryValue",
            "type": "Element",
            "required": True,
        }
    )
    maximum_monetary_value: str = field(
        metadata={
            "name": "MaximumMonetaryValue",
            "type": "Element",
            "required": True,
        }
    )
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class MonetaryValue:
    monetary_amount: str = field(
        metadata={
            "name": "MonetaryAmount",
            "type": "Element",
            "required": True,
        }
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
        }
    )
    rate_of_exchange_detail: Optional[RateOfExchangeDetail] = field(
        default=None,
        metadata={
            "name": "RateOfExchangeDetail",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class OrderHeaderAttachments:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderHeaderPrice:
    list_of_price: ListOfPrice = field(
        metadata={
            "name": "ListOfPrice",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequestCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequestDates:
    order_dates: OrderDates = field(
        metadata={
            "name": "OrderDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequestLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderTermsOfDelivery:
    terms_of_delivery: TermsOfDelivery = field(
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherOrderReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PackageCharacteristicDescription:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PackageDoc:
    document_type_coded: PackageDocDocumentTypeCoded = field(
        metadata={
            "name": "DocumentTypeCoded",
            "type": "Attribute",
            "required": True,
        }
    )
    document_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentTypeCodedOther",
            "type": "Attribute",
        }
    )
    document_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "DocumentTitle",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PartyCoded:
    party_id: PartyId = field(
        metadata={
            "name": "PartyID",
            "type": "Element",
            "required": True,
        }
    )
    list_of_identifier: Optional[ListOfIdentifier] = field(
        default=None,
        metadata={
            "name": "ListOfIdentifier",
            "type": "Element",
        }
    )
    mdfbusiness: Optional[str] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        }
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        }
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        }
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        }
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        }
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        }
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        }
    )
    party_role_coded: str = field(
        metadata={
            "name": "PartyRoleCoded",
            "type": "Element",
            "required": True,
        }
    )
    party_role_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartyRoleCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PaymentMeanReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuantityCoded:
    quantity_value: Optional[QuantityValue] = field(
        default=None,
        metadata={
            "name": "QuantityValue",
            "type": "Element",
        }
    )
    quantity_range: Optional[QuantityRange] = field(
        default=None,
        metadata={
            "name": "QuantityRange",
            "type": "Element",
        }
    )
    unit_of_measurement: UnitOfMeasurement = field(
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
            "required": True,
        }
    )
    quantity_qualifier_coded: str = field(
        metadata={
            "name": "QuantityQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    quantity_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantityQualifierCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class QuoteReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RatePerUnit:
    unit_price: UnitPrice = field(
        metadata={
            "name": "UnitPrice",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemitToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ReturnableContainerPartNumber:
    part_num: PartNum = field(
        metadata={
            "name": "PartNum",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SellerParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShipFromParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShipToParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class StructuredNote:
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )
    note_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoteID",
            "type": "Element",
        }
    )
    agency: Optional[Agency] = field(
        default=None,
        metadata={
            "name": "Agency",
            "type": "Element",
        }
    )
    note_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "NoteURL",
            "type": "Element",
        }
    )
    text_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextTypeCoded",
            "type": "Element",
        }
    )
    text_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TextTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TaxAccountingCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxIdentifier:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxLocation:
    location: Location = field(
        metadata={
            "name": "Location",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxTypeCodedOther:
    identifier: Identifier = field(
        metadata={
            "name": "Identifier",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalGrossWeight:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalNetNetWeight:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalNetWeight:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalQuantity:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalTareWeight:
    measurement: Measurement = field(
        metadata={
            "name": "Measurement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AccountDetail:
    account_id: str = field(
        metadata={
            "name": "AccountID",
            "type": "Element",
            "required": True,
        }
    )
    secondary_account_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SecondaryAccountID",
            "type": "Element",
        }
    )
    iban: Optional[str] = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
        }
    )
    account_control_key: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountControlKey",
            "type": "Element",
        }
    )
    account_type_coded: str = field(
        metadata={
            "name": "AccountTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    account_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountTypeCodedOther",
            "type": "Element",
        }
    )
    account_name1: str = field(
        metadata={
            "name": "AccountName1",
            "type": "Element",
            "required": True,
        }
    )
    account_name2: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountName2",
            "type": "Element",
        }
    )
    currency: Optional[Currency] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
        }
    )
    account_references: Optional[AccountReferences] = field(
        default=None,
        metadata={
            "name": "AccountReferences",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class BasisMonetaryRange:
    monetary_range: Optional[MonetaryRange] = field(
        default=None,
        metadata={
            "name": "MonetaryRange",
            "type": "Element",
        }
    )
    monetary_limit: Optional[MonetaryLimit] = field(
        default=None,
        metadata={
            "name": "MonetaryLimit",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Contract:
    contract_id: ContractId = field(
        metadata={
            "name": "ContractID",
            "type": "Element",
            "required": True,
        }
    )
    contract_type: Optional[ContractType] = field(
        default=None,
        metadata={
            "name": "ContractType",
            "type": "Element",
        }
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )
    system_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class DiscountAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DocumentAttached:
    package_doc: PackageDoc = field(
        metadata={
            "name": "PackageDoc",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DocumentLoose:
    package_doc: PackageDoc = field(
        metadata={
            "name": "PackageDoc",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FinancialInstitution:
    financial_institution_id: str = field(
        metadata={
            "name": "FinancialInstitutionID",
            "type": "Element",
            "required": True,
        }
    )
    financial_institution_name: str = field(
        metadata={
            "name": "FinancialInstitutionName",
            "type": "Element",
            "required": True,
        }
    )
    fibranch_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIBranchID",
            "type": "Element",
        }
    )
    fibranch_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIBranchName",
            "type": "Element",
        }
    )
    fibranch_street: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIBranchStreet",
            "type": "Element",
        }
    )
    fibranch_house_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIBranchHouseNumber",
            "type": "Element",
        }
    )
    fibranch_street_supplement1: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIBranchStreetSupplement1",
            "type": "Element",
        }
    )
    fibranch_street_supplement2: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIBranchStreetSupplement2",
            "type": "Element",
        }
    )
    fibranch_postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIBranchPostalCode",
            "type": "Element",
        }
    )
    fibranch_city: Optional[str] = field(
        default=None,
        metadata={
            "name": "FIBranchCity",
            "type": "Element",
        }
    )
    fibranch_region: Optional[FibranchRegion] = field(
        default=None,
        metadata={
            "name": "FIBranchRegion",
            "type": "Element",
        }
    )
    fibranch_country: Optional[FibranchCountry] = field(
        default=None,
        metadata={
            "name": "FIBranchCountry",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class HazardousTemperatures:
    flashpoint: Optional[Flashpoint] = field(
        default=None,
        metadata={
            "name": "Flashpoint",
            "type": "Element",
        }
    )
    emergency: Optional[Emergency] = field(
        default=None,
        metadata={
            "name": "Emergency",
            "type": "Element",
        }
    )
    control: Optional[Control] = field(
        default=None,
        metadata={
            "name": "Control",
            "type": "Element",
        }
    )
    list_of_temperature_coded: Optional[ListOfTemperatureCoded] = field(
        default=None,
        metadata={
            "name": "ListOfTemperatureCoded",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfDescription:
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfItemCharacteristic:
    item_characteristic: List[ItemCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "ItemCharacteristic",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfMessageId:
    class Meta:
        name = "ListOfMessageID"

    message_id: List[MessageId] = field(
        default_factory=list,
        metadata={
            "name": "MessageID",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfPartyCoded:
    party_coded: List[PartyCoded] = field(
        default_factory=list,
        metadata={
            "name": "PartyCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfQuantityCoded:
    quantity_coded: List[QuantityCoded] = field(
        default_factory=list,
        metadata={
            "name": "QuantityCoded",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfStructuredNote:
    structured_note: List[StructuredNote] = field(
        default_factory=list,
        metadata={
            "name": "StructuredNote",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class NameValueSet:
    set_name: str = field(
        metadata={
            "name": "SetName",
            "type": "Element",
            "required": True,
        }
    )
    set_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SetID",
            "type": "Element",
        }
    )
    list_of_name_value_pair: ListOfNameValuePair = field(
        metadata={
            "name": "ListOfNameValuePair",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PackageCharacteristic:
    package_characteristic_coded: str = field(
        metadata={
            "name": "PackageCharacteristicCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_characteristic_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageCharacteristicCodedOther",
            "type": "Element",
        }
    )
    package_characteristic_description: PackageCharacteristicDescription = field(
        metadata={
            "name": "PackageCharacteristicDescription",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PackageDescription:
    list_of_package_identifier: Optional[ListOfPackageIdentifier] = field(
        default=None,
        metadata={
            "name": "ListOfPackageIdentifier",
            "type": "Element",
        }
    )
    container_counter: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContainerCounter",
            "type": "Element",
        }
    )
    load_order_counter: Optional[str] = field(
        default=None,
        metadata={
            "name": "LoadOrderCounter",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ParentItemNumber:
    line_item_number_reference: LineItemNumberReference = field(
        metadata={
            "name": "LineItemNumberReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PartyTaxInformation:
    tax_identifier: Optional[TaxIdentifier] = field(
        default=None,
        metadata={
            "name": "TaxIdentifier",
            "type": "Element",
        }
    )
    registered_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegisteredName",
            "type": "Element",
        }
    )
    registered_office: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegisteredOffice",
            "type": "Element",
        }
    )
    tax_location: Optional[TaxLocation] = field(
        default=None,
        metadata={
            "name": "TaxLocation",
            "type": "Element",
        }
    )
    company_registration_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CompanyRegistrationNumber",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PercentageMonetaryValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class QuantityMonetaryValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Rate:
    rate_per_unit: RatePerUnit = field(
        metadata={
            "name": "RatePerUnit",
            "type": "Element",
            "required": True,
        }
    )
    unit_price_basis: str = field(
        metadata={
            "name": "UnitPriceBasis",
            "type": "Element",
            "required": True,
        }
    )
    unit_of_measurement: Optional[UnitOfMeasurement] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasurement",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ReturnableContainerInfo:
    returnable_container_part_number: Optional[ReturnableContainerPartNumber] = field(
        default=None,
        metadata={
            "name": "ReturnableContainerPartNumber",
            "type": "Element",
        }
    )
    payment_responsibility_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentResponsibilityCoded",
            "type": "Element",
        }
    )
    payment_responsibility_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentResponsibilityCodedOther",
            "type": "Element",
        }
    )
    return_load_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnLoadCoded",
            "type": "Element",
        }
    )
    return_load_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnLoadCodedOther",
            "type": "Element",
        }
    )
    return_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReturnNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Tax:
    tax_function_qualifier_coded: str = field(
        metadata={
            "name": "TaxFunctionQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_function_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxFunctionQualifierCodedOther",
            "type": "Element",
        }
    )
    tax_category_coded: str = field(
        metadata={
            "name": "TaxCategoryCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_category_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxCategoryCodedOther",
            "type": "Element",
        }
    )
    reason_tax_exempt_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCoded",
            "type": "Element",
        }
    )
    reason_tax_exempt_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCodedOther",
            "type": "Element",
        }
    )
    tax_type_coded: str = field(
        metadata={
            "name": "TaxTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_type_coded_other: Optional[TaxTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "TaxTypeCodedOther",
            "type": "Element",
        }
    )
    tax_percent: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPercent",
            "type": "Element",
        }
    )
    tax_payment_method_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCoded",
            "type": "Element",
        }
    )
    tax_payment_method_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCodedOther",
            "type": "Element",
        }
    )
    taxable_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
        }
    )
    taxable_amount_in_tax_accounting_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxableAmountInTaxAccountingCurrency",
            "type": "Element",
        }
    )
    tax_amount: str = field(
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "required": True,
        }
    )
    tax_amount_in_tax_accounting_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxAmountInTaxAccountingCurrency",
            "type": "Element",
        }
    )
    tax_location: Optional[TaxLocation] = field(
        default=None,
        metadata={
            "name": "TaxLocation",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TaxReference:
    tax_function_qualifier_coded: str = field(
        metadata={
            "name": "TaxFunctionQualifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_function_qualifier_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxFunctionQualifierCodedOther",
            "type": "Element",
        }
    )
    tax_category_coded: str = field(
        metadata={
            "name": "TaxCategoryCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_category_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxCategoryCodedOther",
            "type": "Element",
        }
    )
    reason_tax_exempt_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCoded",
            "type": "Element",
        }
    )
    reason_tax_exempt_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTaxExemptCodedOther",
            "type": "Element",
        }
    )
    tax_type_coded: str = field(
        metadata={
            "name": "TaxTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_type_coded_other: Optional[TaxTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "TaxTypeCodedOther",
            "type": "Element",
        }
    )
    tax_percent: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPercent",
            "type": "Element",
        }
    )
    tax_payment_method_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCoded",
            "type": "Element",
        }
    )
    tax_payment_method_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPaymentMethodCodedOther",
            "type": "Element",
        }
    )
    taxable_amount: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
        }
    )
    taxable_amount_in_tax_accounting_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxableAmountInTaxAccountingCurrency",
            "type": "Element",
        }
    )
    tax_amount: str = field(
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "required": True,
        }
    )
    tax_amount_in_tax_accounting_currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxAmountInTaxAccountingCurrency",
            "type": "Element",
        }
    )
    tax_location: Optional[TaxLocation] = field(
        default=None,
        metadata={
            "name": "TaxLocation",
            "type": "Element",
        }
    )
    tax_treatment_coded: str = field(
        metadata={
            "name": "TaxTreatmentCoded",
            "type": "Element",
            "required": True,
        }
    )
    tax_treatment_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxTreatmentCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TotalAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalTax:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TransportPackagingTotals:
    total_packages: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPackages",
            "type": "Element",
        }
    )
    total_package_depth: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPackageDepth",
            "type": "Element",
        }
    )
    total_transport: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalTransport",
            "type": "Element",
        }
    )
    total_gross_weight: Optional[TotalGrossWeight] = field(
        default=None,
        metadata={
            "name": "TotalGrossWeight",
            "type": "Element",
        }
    )
    total_net_weight: Optional[TotalNetWeight] = field(
        default=None,
        metadata={
            "name": "TotalNetWeight",
            "type": "Element",
        }
    )
    total_net_net_weight: Optional[TotalNetNetWeight] = field(
        default=None,
        metadata={
            "name": "TotalNetNetWeight",
            "type": "Element",
        }
    )
    total_tare_weight: Optional[TotalTareWeight] = field(
        default=None,
        metadata={
            "name": "TotalTareWeight",
            "type": "Element",
        }
    )
    gross_volume: Optional[GrossVolume] = field(
        default=None,
        metadata={
            "name": "GrossVolume",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AllowOrChgDesc:
    ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefID",
            "type": "Element",
        }
    )
    list_of_description: Optional[ListOfDescription] = field(
        default=None,
        metadata={
            "name": "ListOfDescription",
            "type": "Element",
        }
    )
    service_coded: str = field(
        metadata={
            "name": "ServiceCoded",
            "type": "Element",
            "required": True,
        }
    )
    service_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class BuyerTaxInformation:
    party_tax_information: PartyTaxInformation = field(
        metadata={
            "name": "PartyTaxInformation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContractItem:
    contract: Contract = field(
        metadata={
            "name": "Contract",
            "type": "Element",
            "required": True,
        }
    )
    contract_item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContractItemNumber",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Discounts:
    discount_percent: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountPercent",
            "type": "Element",
        }
    )
    discount_amount: Optional[DiscountAmount] = field(
        default=None,
        metadata={
            "name": "DiscountAmount",
            "type": "Element",
        }
    )
    discount_days_due: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountDaysDue",
            "type": "Element",
        }
    )
    discount_due_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountDueDate",
            "type": "Element",
        }
    )
    discount_day_of_month: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountDayOfMonth",
            "type": "Element",
        }
    )
    discount_date_time_ref_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountDateTimeRefCoded",
            "type": "Element",
        }
    )
    discount_date_time_ref_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "DiscountDateTimeRefCodedOther",
            "type": "Element",
        }
    )
    net_days_due: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetDaysDue",
            "type": "Element",
        }
    )
    net_due_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetDueDate",
            "type": "Element",
        }
    )
    net_date_time_ref_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetDateTimeRefCoded",
            "type": "Element",
        }
    )
    net_date_time_ref_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetDateTimeRefCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Fiaccount:
    class Meta:
        name = "FIAccount"

    account_detail: Optional[AccountDetail] = field(
        default=None,
        metadata={
            "name": "AccountDetail",
            "type": "Element",
        }
    )
    financial_institution: FinancialInstitution = field(
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Hazardous:
    list_of_hazardous_identifiers: Optional[ListOfHazardousIdentifiers] = field(
        default=None,
        metadata={
            "name": "ListOfHazardousIdentifiers",
            "type": "Element",
        }
    )
    hazard_class_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardClassCoded",
            "type": "Element",
        }
    )
    hazard_class_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardClassCodedOther",
            "type": "Element",
        }
    )
    hazardous_placard_information: Optional[HazardousPlacardInformation] = field(
        default=None,
        metadata={
            "name": "HazardousPlacardInformation",
            "type": "Element",
        }
    )
    hazardous_references: Optional[HazardousReferences] = field(
        default=None,
        metadata={
            "name": "HazardousReferences",
            "type": "Element",
        }
    )
    hazardous_contact: Optional[HazardousContact] = field(
        default=None,
        metadata={
            "name": "HazardousContact",
            "type": "Element",
        }
    )
    hazard_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "HazardNote",
            "type": "Element",
        }
    )
    undgnum: Optional[str] = field(
        default=None,
        metadata={
            "name": "UNDGNum",
            "type": "Element",
        }
    )
    hazardous_temperatures: Optional[HazardousTemperatures] = field(
        default=None,
        metadata={
            "name": "HazardousTemperatures",
            "type": "Element",
        }
    )
    hazardous_shipment_information: Optional[HazardousShipmentInformation] = field(
        default=None,
        metadata={
            "name": "HazardousShipmentInformation",
            "type": "Element",
        }
    )
    emsnum: Optional[str] = field(
        default=None,
        metadata={
            "name": "EMSNum",
            "type": "Element",
        }
    )
    mfag: Optional[str] = field(
        default=None,
        metadata={
            "name": "Mfag",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ItemIdentifiers:
    part_numbers: Optional[PartNumbers] = field(
        default=None,
        metadata={
            "name": "PartNumbers",
            "type": "Element",
        }
    )
    service: Optional[str] = field(
        default=None,
        metadata={
            "name": "Service",
            "type": "Element",
        }
    )
    item_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ItemDescription",
            "type": "Element",
        }
    )
    list_of_item_characteristic: Optional[ListOfItemCharacteristic] = field(
        default=None,
        metadata={
            "name": "ListOfItemCharacteristic",
            "type": "Element",
        }
    )
    commodity_code: Optional[CommodityCode] = field(
        default=None,
        metadata={
            "name": "CommodityCode",
            "type": "Element",
        }
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfContract:
    contract: List[Contract] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfDocumentAttached:
    document_attached: List[DocumentAttached] = field(
        default_factory=list,
        metadata={
            "name": "DocumentAttached",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfDocumentLoose:
    document_loose: List[DocumentLoose] = field(
        default_factory=list,
        metadata={
            "name": "DocumentLoose",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfNameValueSet:
    name_value_set: List[NameValueSet] = field(
        default_factory=list,
        metadata={
            "name": "NameValueSet",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfPackageCharacteristic:
    package_characteristic: List[PackageCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "PackageCharacteristic",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfPackageDescription:
    package_description: List[PackageDescription] = field(
        default_factory=list,
        metadata={
            "name": "PackageDescription",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class OrderRequestNumber:
    buyer_order_request_number: str = field(
        metadata={
            "name": "BuyerOrderRequestNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_request_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerOrderRequestNumber",
            "type": "Element",
        }
    )
    list_of_message_id: Optional[ListOfMessageId] = field(
        default=None,
        metadata={
            "name": "ListOfMessageID",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class OrderRequestTaxReference:
    tax_reference: TaxReference = field(
        metadata={
            "name": "TaxReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderSummary:
    number_of_lines: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfLines",
            "type": "Element",
        }
    )
    total_tax: Optional[TotalTax] = field(
        default=None,
        metadata={
            "name": "TotalTax",
            "type": "Element",
        }
    )
    total_amount: Optional[TotalAmount] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
        }
    )
    transport_packaging_totals: Optional[TransportPackagingTotals] = field(
        default=None,
        metadata={
            "name": "TransportPackagingTotals",
            "type": "Element",
        }
    )
    summary_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummaryNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PackageTypeDescription:
    list_of_description: ListOfDescription = field(
        metadata={
            "name": "ListOfDescription",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PercentageAllowanceOrCharge:
    percent_qualifier: PercentQualifier = field(
        metadata={
            "name": "PercentQualifier",
            "type": "Element",
            "required": True,
        }
    )
    percent: str = field(
        metadata={
            "name": "Percent",
            "type": "Element",
            "required": True,
        }
    )
    percentage_monetary_value: Optional[PercentageMonetaryValue] = field(
        default=None,
        metadata={
            "name": "PercentageMonetaryValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class QuantityAllowanceOrCharge:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )
    rate: Rate = field(
        metadata={
            "name": "Rate",
            "type": "Element",
            "required": True,
        }
    )
    quantity_monetary_value: Optional[QuantityMonetaryValue] = field(
        default=None,
        metadata={
            "name": "QuantityMonetaryValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class SellerTaxInformation:
    party_tax_information: PartyTaxInformation = field(
        metadata={
            "name": "PartyTaxInformation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AllowanceOrChargeDescription:
    allow_or_chg_desc: AllowOrChgDesc = field(
        metadata={
            "name": "AllowOrChgDesc",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AssociatedDocuments:
    list_of_document_loose: Optional[ListOfDocumentLoose] = field(
        default=None,
        metadata={
            "name": "ListOfDocumentLoose",
            "type": "Element",
        }
    )
    list_of_document_attached: Optional[ListOfDocumentAttached] = field(
        default=None,
        metadata={
            "name": "ListOfDocumentAttached",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ContractReferences:
    list_of_contract: ListOfContract = field(
        metadata={
            "name": "ListOfContract",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class HazardousMaterials:
    hazardous: Hazardous = field(
        metadata={
            "name": "Hazardous",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class HazardousPackaging:
    hazardous: Hazardous = field(
        metadata={
            "name": "Hazardous",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfContractItem:
    contract_item: List[ContractItem] = field(
        default_factory=list,
        metadata={
            "name": "ContractItem",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class OrderRequestParty:
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
        }
    )
    buyer_tax_information: Optional[BuyerTaxInformation] = field(
        default=None,
        metadata={
            "name": "BuyerTaxInformation",
            "type": "Element",
        }
    )
    seller_party: SellerParty = field(
        metadata={
            "name": "SellerParty",
            "type": "Element",
            "required": True,
        }
    )
    seller_tax_information: Optional[SellerTaxInformation] = field(
        default=None,
        metadata={
            "name": "SellerTaxInformation",
            "type": "Element",
        }
    )
    ship_to_party: Optional[ShipToParty] = field(
        default=None,
        metadata={
            "name": "ShipToParty",
            "type": "Element",
        }
    )
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        }
    )
    remit_to_party: Optional[RemitToParty] = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        }
    )
    ship_from_party: Optional[ShipFromParty] = field(
        default=None,
        metadata={
            "name": "ShipFromParty",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class OrderRequestSummary:
    order_summary: OrderSummary = field(
        metadata={
            "name": "OrderSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OriginatingFiaccount:
    class Meta:
        name = "OriginatingFIAccount"

    fiaccount: Fiaccount = field(
        metadata={
            "name": "FIAccount",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PackageType:
    package_type_coded: str = field(
        metadata={
            "name": "PackageTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackageTypeCodedOther",
            "type": "Element",
        }
    )
    package_type_description: Optional[PackageTypeDescription] = field(
        default=None,
        metadata={
            "name": "PackageTypeDescription",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PaymentTermDetails:
    discounts: Discounts = field(
        metadata={
            "name": "Discounts",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ReceivingFiaccount:
    class Meta:
        name = "ReceivingFIAccount"

    fiaccount: Fiaccount = field(
        metadata={
            "name": "FIAccount",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TypeOfAllowanceOrCharge:
    quantity_allowance_or_charge: Optional[QuantityAllowanceOrCharge] = field(
        default=None,
        metadata={
            "name": "QuantityAllowanceOrCharge",
            "type": "Element",
        }
    )
    percentage_allowance_or_charge: Optional[PercentageAllowanceOrCharge] = field(
        default=None,
        metadata={
            "name": "PercentageAllowanceOrCharge",
            "type": "Element",
        }
    )
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AllowOrCharge:
    seq_no: str = field(
        default="1",
        metadata={
            "name": "SeqNo",
            "type": "Attribute",
            "required": True,
        }
    )
    indicator_coded: str = field(
        metadata={
            "name": "IndicatorCoded",
            "type": "Element",
            "required": True,
        }
    )
    indicator_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "IndicatorCodedOther",
            "type": "Element",
        }
    )
    basis_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasisCoded",
            "type": "Element",
        }
    )
    basis_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "BasisCodedOther",
            "type": "Element",
        }
    )
    method_of_handling_coded: str = field(
        metadata={
            "name": "MethodOfHandlingCoded",
            "type": "Element",
            "required": True,
        }
    )
    method_of_handling_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "MethodOfHandlingCodedOther",
            "type": "Element",
        }
    )
    allowance_or_charge_description: AllowanceOrChargeDescription = field(
        metadata={
            "name": "AllowanceOrChargeDescription",
            "type": "Element",
            "required": True,
        }
    )
    validity_dates: Optional[ValidityDates] = field(
        default=None,
        metadata={
            "name": "ValidityDates",
            "type": "Element",
        }
    )
    basis_quantity_range: Optional[BasisQuantityRange] = field(
        default=None,
        metadata={
            "name": "BasisQuantityRange",
            "type": "Element",
        }
    )
    basis_monetary_range: Optional[BasisMonetaryRange] = field(
        default=None,
        metadata={
            "name": "BasisMonetaryRange",
            "type": "Element",
        }
    )
    type_of_allowance_or_charge: TypeOfAllowanceOrCharge = field(
        metadata={
            "name": "TypeOfAllowanceOrCharge",
            "type": "Element",
            "required": True,
        }
    )
    tax: List[Tax] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ItemContractReferences:
    list_of_contract_item: ListOfContractItem = field(
        metadata={
            "name": "ListOfContractItem",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderReferences:
    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
        }
    )
    contract_references: Optional[ContractReferences] = field(
        default=None,
        metadata={
            "name": "ContractReferences",
            "type": "Element",
        }
    )
    quote_reference: Optional[QuoteReference] = field(
        default=None,
        metadata={
            "name": "QuoteReference",
            "type": "Element",
        }
    )
    other_order_references: Optional[OtherOrderReferences] = field(
        default=None,
        metadata={
            "name": "OtherOrderReferences",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PaymentMethod:
    payment_mean_coded: str = field(
        metadata={
            "name": "PaymentMeanCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_mean_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentMeanCodedOther",
            "type": "Element",
        }
    )
    payment_mean_reference: Optional[PaymentMeanReference] = field(
        default=None,
        metadata={
            "name": "PaymentMeanReference",
            "type": "Element",
        }
    )
    payment_system_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSystemCoded",
            "type": "Element",
        }
    )
    payment_system_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSystemCodedOther",
            "type": "Element",
        }
    )
    originating_fiaccount: Optional[OriginatingFiaccount] = field(
        default=None,
        metadata={
            "name": "OriginatingFIAccount",
            "type": "Element",
        }
    )
    receiving_fiaccount: Optional[ReceivingFiaccount] = field(
        default=None,
        metadata={
            "name": "ReceivingFIAccount",
            "type": "Element",
        }
    )
    card_info: Optional[CardInfo] = field(
        default=None,
        metadata={
            "name": "CardInfo",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PaymentTerm:
    payment_term_coded: str = field(
        metadata={
            "name": "PaymentTermCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_term_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentTermCodedOther",
            "type": "Element",
        }
    )
    payment_term_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentTermValue",
            "type": "Element",
        }
    )
    payment_term_details: Optional[PaymentTermDetails] = field(
        default=None,
        metadata={
            "name": "PaymentTermDetails",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class BaseItemDetail:
    line_item_num: LineItemNum = field(
        metadata={
            "name": "LineItemNum",
            "type": "Element",
            "required": True,
        }
    )
    line_item_type: Optional[LineItemType] = field(
        default=None,
        metadata={
            "name": "LineItemType",
            "type": "Element",
        }
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        }
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
            "type": "Element",
        }
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        }
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        }
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        }
    )
    off_catalog_flag: Optional[str] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        }
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        }
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        }
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        }
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        }
    )
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        }
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        }
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        }
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfAllowOrCharge:
    allow_or_charge: List[AllowOrCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowOrCharge",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfOrderReferences:
    order_references: List[OrderReferences] = field(
        default_factory=list,
        metadata={
            "name": "OrderReferences",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class OrderRequestReferences:
    order_references: OrderReferences = field(
        metadata={
            "name": "OrderReferences",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentTerms:
    payment_term: List[PaymentTerm] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerm",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    discounts: List[Discounts] = field(
        default_factory=list,
        metadata={
            "name": "Discounts",
            "type": "Element",
        }
    )
    payment_terms_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentTermsNote",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ItemAllowancesOrCharges:
    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfItemReference:
    list_of_order_references: ListOfOrderReferences = field(
        metadata={
            "name": "ListOfOrderReferences",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderAllowancesOrCharges:
    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentInstructions:
    payment_terms: List[PaymentTerms] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    payment_method: List[PaymentMethod] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class OrderPaymentInstructions:
    payment_instructions: PaymentInstructions = field(
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Package:
    package_id: str = field(
        metadata={
            "name": "PackageID",
            "type": "Element",
            "required": True,
        }
    )
    list_of_item_reference: Optional[ListOfItemReference] = field(
        default=None,
        metadata={
            "name": "ListOfItemReference",
            "type": "Element",
        }
    )
    list_of_package_mark: Optional[ListOfPackageMark] = field(
        default=None,
        metadata={
            "name": "ListOfPackageMark",
            "type": "Element",
        }
    )
    list_of_package_characteristic: Optional[ListOfPackageCharacteristic] = field(
        default=None,
        metadata={
            "name": "ListOfPackageCharacteristic",
            "type": "Element",
        }
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        }
    )
    list_of_package_description: Optional[ListOfPackageDescription] = field(
        default=None,
        metadata={
            "name": "ListOfPackageDescription",
            "type": "Element",
        }
    )
    transport_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportReference",
            "type": "Element",
        }
    )
    special_handling: Optional[SpecialHandling] = field(
        default=None,
        metadata={
            "name": "SpecialHandling",
            "type": "Element",
        }
    )
    hazardous_packaging: Optional[HazardousPackaging] = field(
        default=None,
        metadata={
            "name": "HazardousPackaging",
            "type": "Element",
        }
    )
    associated_documents: Optional[AssociatedDocuments] = field(
        default=None,
        metadata={
            "name": "AssociatedDocuments",
            "type": "Element",
        }
    )
    shipping_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "ShippingInstructions",
            "type": "Element",
        }
    )
    returnable_container_info: Optional[ReturnableContainerInfo] = field(
        default=None,
        metadata={
            "name": "ReturnableContainerInfo",
            "type": "Element",
        }
    )
    package_detail: List["PackageDetail"] = field(
        default_factory=list,
        metadata={
            "name": "PackageDetail",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PricingDetail:
    list_of_price: ListOfPrice = field(
        metadata={
            "name": "ListOfPrice",
            "type": "Element",
            "required": True,
        }
    )
    tax: List[Tax] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
        }
    )
    item_allowances_or_charges: Optional[ItemAllowancesOrCharges] = field(
        default=None,
        metadata={
            "name": "ItemAllowancesOrCharges",
            "type": "Element",
        }
    )
    total_value: Optional[TotalValue] = field(
        default=None,
        metadata={
            "name": "TotalValue",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ItemDetail:
    base_item_detail: BaseItemDetail = field(
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    pricing_detail: Optional[PricingDetail] = field(
        default=None,
        metadata={
            "name": "PricingDetail",
            "type": "Element",
        }
    )
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
        }
    )
    round_trip_information: Optional[RoundTripInformation] = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        }
    )
    line_item_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        }
    )
    line_item_attachments: Optional[LineItemAttachments] = field(
        default=None,
        metadata={
            "name": "LineItemAttachments",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfPackage:
    package: List[Package] = field(
        default_factory=list,
        metadata={
            "name": "Package",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class OrderRequestHeader:
    order_request_number: Optional[OrderRequestNumber] = field(
        default=None,
        metadata={
            "name": "OrderRequestNumber",
            "type": "Element",
        }
    )
    order_request_issue_date: str = field(
        metadata={
            "name": "OrderRequestIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    order_request_references: Optional[OrderRequestReferences] = field(
        default=None,
        metadata={
            "name": "OrderRequestReferences",
            "type": "Element",
        }
    )
    purpose: Optional[Purpose] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
        }
    )
    requested_response: Optional[RequestedResponse] = field(
        default=None,
        metadata={
            "name": "RequestedResponse",
            "type": "Element",
        }
    )
    order_request_currency: OrderRequestCurrency = field(
        metadata={
            "name": "OrderRequestCurrency",
            "type": "Element",
            "required": True,
        }
    )
    tax_accounting_currency: Optional[TaxAccountingCurrency] = field(
        default=None,
        metadata={
            "name": "TaxAccountingCurrency",
            "type": "Element",
        }
    )
    order_request_language: OrderRequestLanguage = field(
        metadata={
            "name": "OrderRequestLanguage",
            "type": "Element",
            "required": True,
        }
    )
    order_request_tax_reference: Optional[OrderRequestTaxReference] = field(
        default=None,
        metadata={
            "name": "OrderRequestTaxReference",
            "type": "Element",
        }
    )
    order_invoice_medium_type_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderInvoiceMediumTypeCoded",
            "type": "Element",
        }
    )
    order_invoice_medium_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderInvoiceMediumTypeCodedOther",
            "type": "Element",
        }
    )
    order_request_dates: Optional[OrderRequestDates] = field(
        default=None,
        metadata={
            "name": "OrderRequestDates",
            "type": "Element",
        }
    )
    partial_shipment_allowed: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialShipmentAllowed",
            "type": "Element",
        }
    )
    order_request_party: OrderRequestParty = field(
        metadata={
            "name": "OrderRequestParty",
            "type": "Element",
            "required": True,
        }
    )
    list_of_transport: Optional[ListOfTransport] = field(
        default=None,
        metadata={
            "name": "ListOfTransport",
            "type": "Element",
        }
    )
    order_terms_of_delivery: List[OrderTermsOfDelivery] = field(
        default_factory=list,
        metadata={
            "name": "OrderTermsOfDelivery",
            "type": "Element",
        }
    )
    order_header_price: Optional[OrderHeaderPrice] = field(
        default=None,
        metadata={
            "name": "OrderHeaderPrice",
            "type": "Element",
        }
    )
    order_payment_instructions: Optional[OrderPaymentInstructions] = field(
        default=None,
        metadata={
            "name": "OrderPaymentInstructions",
            "type": "Element",
        }
    )
    order_allowances_or_charges: Optional[OrderAllowancesOrCharges] = field(
        default=None,
        metadata={
            "name": "OrderAllowancesOrCharges",
            "type": "Element",
        }
    )
    round_trip_information: Optional[RoundTripInformation] = field(
        default=None,
        metadata={
            "name": "RoundTripInformation",
            "type": "Element",
        }
    )
    order_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "OrderHeaderNote",
            "type": "Element",
        }
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        }
    )
    order_header_attachments: Optional[OrderHeaderAttachments] = field(
        default=None,
        metadata={
            "name": "OrderHeaderAttachments",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfItemDetail:
    item_detail: List[ItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "ItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class PackageDetail:
    package_type: PackageType = field(
        metadata={
            "name": "PackageType",
            "type": "Element",
            "required": True,
        }
    )
    number_of_packages: str = field(
        metadata={
            "name": "NumberOfPackages",
            "type": "Element",
            "required": True,
        }
    )
    list_of_package: Optional[ListOfPackage] = field(
        default=None,
        metadata={
            "name": "ListOfPackage",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfPackageDetail:
    package_detail: List[PackageDetail] = field(
        default_factory=list,
        metadata={
            "name": "PackageDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class OrderDetail:
    list_of_item_detail: ListOfItemDetail = field(
        metadata={
            "name": "ListOfItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    list_of_package_detail: Optional[ListOfPackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class OrderRequestDetail:
    order_detail: OrderDetail = field(
        metadata={
            "name": "OrderDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OrderRequest:
    order_request_header: OrderRequestHeader = field(
        metadata={
            "name": "OrderRequestHeader",
            "type": "Element",
            "required": True,
        }
    )
    order_request_detail: Optional[OrderRequestDetail] = field(
        default=None,
        metadata={
            "name": "OrderRequestDetail",
            "type": "Element",
        }
    )
    order_request_summary: Optional[OrderRequestSummary] = field(
        default=None,
        metadata={
            "name": "OrderRequestSummary",
            "type": "Element",
        }
    )
