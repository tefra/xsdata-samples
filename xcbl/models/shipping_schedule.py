from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xcbl.models.shipping_schedule_response import (
    ContractReferences,
    LocationGroupedShippingDetail,
    MaterialGroupedShippingDetail,
    ShippingScheduleHeader,
    ShippingScheduleSummary,
)
from xcbl.models.sourcing_result import (
    Hazardous,
    ListOfDescription,
    ListOfReferenceCoded,
    PartNum,
    ShippingInstructions,
    TransportReference,
)
from xcbl.models.time_series_response import ListOfDimension
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import Identifier


@dataclass(kw_only=True)
class ContainerCounter:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DocumentTitle:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LoadOrderCounter:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NumberOfPackages:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageCharacteristicCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageCharacteristicCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


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
    COMBINED_CERTIFICATE_OF_VALUE_AND_ORIGIN = (
        "CombinedCertificateOfValueAndOrigin"
    )
    MOVEMENT_CERTIFICATE_ATR1 = "MovementCertificateATr1"
    CERTIFICATE_OF_QUANTITY = "CertificateOfQuantity"
    QUALITY_DATA_MESSAGE = "QualityDataMessage"
    QUERY = "Query"
    RESPONSE_TO_QUERY = "ResponseToQuery"
    STATUS_INFORMATION = "StatusInformation"
    RESTOW = "Restow"
    CONTAINER_DISCHARGE_LIST = "ContainerDischargeList"
    CORPORATE_SUPERANNUATION_CONTRIBUTIONS_ADVICE = (
        "CorporateSuperannuationContributionsAdvice"
    )
    INDUSTRY_SUPERANNUATION_CONTRIBUTIONS_ADVICE = (
        "IndustrySuperannuationContributionsAdvice"
    )
    CORPORATE_SUPERANNUATION_MEMBER_MAINTENANCE_MESSAGE = (
        "CorporateSuperannuationMemberMaintenanceMessage"
    )
    INDUSTRY_SUPERANNUATION_MEMBER_MAINTENANCE_MESSAGE = (
        "IndustrySuperannuationMemberMaintenanceMessage"
    )
    LIFE_INSURANCE_PAYROLL_DEDUCTIONS_ADVICE = (
        "LifeInsurancePayrollDeductionsAdvice"
    )
    UNDERBOND_REQUEST = "UnderbondRequest"
    UNDERBOND_APPROVAL = "UnderbondApproval"
    CERTIFICATE_OF_SEALING_OF_EXPORT_MEAT_LOCKERS = (
        "CertificateOfSealingOfExportMeatLockers"
    )
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
    EXTRA_COMMUNITY_TRADE_STATISTICAL_DECLARATION = (
        "Extra-CommunityTradeStatisticalDeclaration"
    )
    WRITTEN_INSTRUCTIONS_IN_CONFORMANCE_WITH_ADR_ARTICLE_NUMBER = (
        "WrittenInstructionsInConformanceWithAdrArticleNumber"
    )
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
    DEBIT_NOTE_RELATED_TO_GOODS_OR_SERVICES = (
        "DebitNoteRelatedToGoodsOrServices"
    )
    CREDIT_NOTE_RELATED_TO_GOODS_OR_SERVICES = (
        "CreditNoteRelatedToGoodsOrServices"
    )
    METERED_SERVICES_INVOICE = "MeteredServicesInvoice"
    CREDIT_NOTE_RELATED_TO_FINANCIAL_ADJUSTMENTS = (
        "CreditNoteRelatedToFinancialAdjustments"
    )
    DEBIT_NOTE_RELATED_TO_FINANCIAL_ADJUSTMENTS = (
        "DebitNoteRelatedToFinancialAdjustments"
    )
    CUSTOMS_MANIFEST = "CustomsManifest"
    VESSEL_UNPACK_REPORT = "VesselUnpackReport"
    GENERAL_CARGO_SUMMARY_MANIFEST_REPORT = "GeneralCargoSummaryManifestReport"
    CONSIGNMENT_UNPACK_REPORT = "ConsignmentUnpackReport"
    MEAT_AND_MEAT_BY_PRODUCTS_SANITARY_CERTIFICATE = (
        "MeatAndMeatBy-ProductsSanitaryCertificate"
    )
    MEAT_FOOD_PRODUCTS_SANITARY_CERTIFICATE = (
        "MeatFoodProductsSanitaryCertificate"
    )
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
    TRANSPORT_EQUIPMENT_DIRECT_INTERCHANGE_REPORT = (
        "TransportEquipmentDirectInterchangeReport"
    )
    TRANSPORT_EQUIPMENT_IMPENDING_ARRIVAL_ADVICE = (
        "TransportEquipmentImpendingArrivalAdvice"
    )
    PURCHASE_ORDER = "PurchaseOrder"
    TRANSPORT_EQUIPMENT_DAMAGE_REPORT = "TransportEquipmentDamageReport"
    TRANSPORT_EQUIPMENT_MAINTENANCE_AND_REPAIR_WORK_ESTIMATE_ADVICE = (
        "TransportEquipmentMaintenanceAndRepairWorkEstimateAdvice"
    )
    TRANSPORT_EQUIPMENT_EMPTY_RELEASE_INSTRUCTION = (
        "TransportEquipmentEmptyReleaseInstruction"
    )
    TRANSPORT_MOVEMENT_GATE_IN_REPORT = "TransportMovementGateInReport"
    MANUFACTURING_INSTRUCTIONS = "ManufacturingInstructions"
    TRANSPORT_MOVEMENT_GATE_OUT_REPORT = "TransportMovementGateOutReport"
    TRANSPORT_EQUIPMENT_UNPACKING_INSTRUCTION = (
        "TransportEquipmentUnpackingInstruction"
    )
    TRANSPORT_EQUIPMENT_UNPACKING_REPORT = "TransportEquipmentUnpackingReport"
    TRANSPORT_EQUIPMENT_PICK_UP_AVAILABILITY_REQUEST = (
        "TransportEquipmentPick-UpAvailabilityRequest"
    )
    TRANSPORT_EQUIPMENT_PICK_UP_AVAILABILITY_CONFIRMATION = (
        "TransportEquipmentPick-UpAvailabilityConfirmation"
    )
    TRANSPORT_EQUIPMENT_PICK_UP_REPORT = "TransportEquipmentPick-UpReport"
    TRANSPORT_EQUIPMENT_SHIFT_REPORT = "TransportEquipmentShiftReport"
    TRANSPORT_DISCHARGE_INSTRUCTION = "TransportDischargeInstruction"
    TRANSPORT_DISCHARGE_REPORT = "TransportDischargeReport"
    STORES_REQUISITION = "StoresRequisition"
    TRANSPORT_LOADING_INSTRUCTION = "TransportLoadingInstruction"
    TRANSPORT_LOADING_REPORT = "TransportLoadingReport"
    TRANSPORT_EQUIPMENT_MAINTENANCE_AND_REPAIR_WORK = (
        "TransportEquipmentMaintenanceAndRepairWork"
    )
    TRANSPORT_DEPARTURE_REPORT = "TransportDepartureReport"
    TRANSPORT_EMPTY_EQUIPMENT_ADVICE = "TransportEmptyEquipmentAdvice"
    TRANSPORT_EQUIPMENT_ACCEPTANCE_ORDER = "TransportEquipmentAcceptanceOrder"
    TRANSPORT_EQUIPMENT_SPECIAL_SERVICE_INSTRUCTION = (
        "TransportEquipmentSpecialServiceInstruction"
    )
    TRANSPORT_EQUIPMENT_STOCK_REPORT = "TransportEquipmentStockReport"
    TRANSPORT_CARGO_RELEASE_ORDER = "TransportCargoReleaseOrder"
    INVOICING_DATA_SHEET = "InvoicingDataSheet"
    TRANSPORT_EQUIPMENT_PACKING_INSTRUCTION = (
        "TransportEquipmentPackingInstruction"
    )
    CUSTOMS_CLEARANCE_NOTICE = "CustomsClearanceNotice"
    CUSTOMS_DOCUMENTS_EXPIRATION_NOTICE = "CustomsDocumentsExpirationNotice"
    TRANSPORT_EQUIPMENT_ON_HIRE_REQUEST = "TransportEquipmentOn-HireRequest"
    TRANSPORT_EQUIPMENT_ON_HIRE_ORDER = "TransportEquipmentOn-HireOrder"
    TRANSPORT_EQUIPMENT_OFF_HIRE_REQUEST = "TransportEquipmentOff-HireRequest"
    TRANSPORT_EQUIPMENT_SURVEY_ORDER = "TransportEquipmentSurveyOrder"
    TRANSPORT_EQUIPMENT_SURVEY_ORDER_RESPONSE = (
        "TransportEquipmentSurveyOrderResponse"
    )
    TRANSPORT_EQUIPMENT_SURVEY_REPORT = "TransportEquipmentSurveyReport"
    PACKING_INSTRUCTIONS = "PackingInstructions"
    ADVISING_ITEMS_TO_BE_BOOKED_TO_AFINANCIAL_ACCOUNT = (
        "AdvisingItemsToBeBookedToAFinancialAccount"
    )
    TRANSPORT_EQUIPMENT_MAINTENANCE_AND_REPAIR_WORK_ESTIMATE_ORDER = (
        "TransportEquipmentMaintenanceAndRepairWorkEstimateOrder"
    )
    TRANSPORT_EQUIPMENT_MAINTENANCE_AND_REPAIR_NOTICE = (
        "TransportEquipmentMaintenanceAndRepairNotice"
    )
    EMPTY_CONTAINER_DISPOSITION_ORDER = "EmptyContainerDispositionOrder"
    CARGO_VESSEL_DISCHARGE_ORDER = "CargoVesselDischargeOrder"
    CARGO_VESSEL_LOADING_ORDER = "CargoVesselLoadingOrder"
    MULTIDROP_ORDER = "MultidropOrder"
    BAILMENT_CONTRACT = "BailmentContract"
    BASIC_AGREEMENT = "BasicAgreement"
    INTERNAL_TRANSPORT_ORDER = "InternalTransportOrder"
    GRANT = "Grant"
    INDEFINITE_DELIVERY_INDEFINITE_QUANTITY_CONTRACT = (
        "IndefiniteDeliveryIndefiniteQuantityContract"
    )
    INDEFINITE_DELIVERY_DEFINITE_QUANTITY_CONTRACT = (
        "IndefiniteDeliveryDefiniteQuantityContract"
    )
    REQUIREMENTS_CONTRACT = "RequirementsContract"
    TASK_ORDER = "TaskOrder"
    MAKE_OR_BUY_PLAN = "MakeOrBuyPlan"
    SUBCONTRACTOR_PLAN = "SubcontractorPlan"
    COST_DATA_SUMMARY = "CostDataSummary"
    CERTIFIED_COST_AND_PRICE_DATA = "CertifiedCostAndPriceData"
    WAGE_DETERMINATION = "WageDetermination"
    CONTRACT_FUNDS_STATUS_REPORT_CFSR = "ContractFundsStatusReportCfsr"
    CERTIFIED_INSPECTION_AND_TEST_RESULTS = "CertifiedInspectionAndTestResults"
    MATERIAL_INSPECTION_AND_RECEIVING_REPORT = (
        "MaterialInspectionAndReceivingReport"
    )
    PURCHASING_SPECIFICATION = "PurchasingSpecification"
    PAYMENT_OR_PERFORMANCE_BOND = "PaymentOrPerformanceBond"
    CONTRACT_SECURITY_CLASSIFICATION_SPECIFICATION = (
        "ContractSecurityClassificationSpecification"
    )
    MANUFACTURING_SPECIFICATION = "ManufacturingSpecification"
    BUY_AMERICA_CERTIFICATE_OF_COMPLIANCE = "BuyAmericaCertificateOfCompliance"
    CONTAINER_OFF_HIRE_NOTICE = "ContainerOff-HireNotice"
    CARGO_ACCEPTANCE_ORDER = "CargoAcceptanceOrder"
    PICK_UP_NOTICE = "Pick-UpNotice"
    AUTHORISATION_TO_PLAN_AND_SUGGEST_ORDERS = (
        "AuthorisationToPlanAndSuggestOrders"
    )
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
    STATISTICAL_AND_OTHER_ADMINISTRATIVE_INTERNAL_DOCUMENTS = (
        "StatisticalAndOtherAdministrativeInternalDocuments"
    )
    PROJECT_MASTER_SCHEDULE = "ProjectMasterSchedule"
    PRICED_ALTERNATE_TENDER_BILL_OF_QUANTITY = (
        "PricedAlternateTenderBillOfQuantity"
    )
    ESTIMATED_PRICED_BILL_OF_QUANTITY = "EstimatedPricedBillOfQuantity"
    DRAFT_BILL_OF_QUANTITY = "DraftBillOfQuantity"
    DOCUMENTARY_CREDIT_COLLECTION_INSTRUCTION = (
        "DocumentaryCreditCollectionInstruction"
    )
    REQUEST_FOR_AN_AMENDMENT_OF_ADOCUMENTARY_CREDIT = (
        "RequestForAnAmendmentOfADocumentaryCredit"
    )
    DOCUMENTARY_CREDIT_AMENDMENT_INFORMATION = (
        "DocumentaryCreditAmendmentInformation"
    )
    ADVICE_OF_AN_AMENDMENT_OF_ADOCUMENTARY_CREDIT = (
        "AdviceOfAnAmendmentOfADocumentaryCredit"
    )
    RESPONSE_TO_AN_AMENDMENT_OF_ADOCUMENTARY_CREDIT = (
        "ResponseToAnAmendmentOfADocumentaryCredit"
    )
    DOCUMENTARY_CREDIT_ISSUANCE_INFORMATION = (
        "DocumentaryCreditIssuanceInformation"
    )
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
    PAYMENT_VALUATION_FOR_UNSCHEDULED_ITEMS = (
        "PaymentValuationForUnscheduledItems"
    )
    FINAL_PAYMENT_REQUEST_BASED_ON_COMPLETION_OF_WORK = (
        "FinalPaymentRequestBasedOnCompletionOfWork"
    )
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
    NON_PRE_AUTHORISED_DIRECT_DEBIT_REQUESTS = (
        "Non-Pre-AuthorisedDirectDebitRequests"
    )
    DELIVERY_RELEASE = "DeliveryRelease"
    SETTLEMENT_OF_ALETTER_OF_CREDIT = "SettlementOfALetterOfCredit"
    BANK_TO_BANK_FUNDS_TRANSFER = "BankToBankFundsTransfer"
    CUSTOMER_PAYMENT_ORDERS = "CustomerPaymentOrders"
    LOW_VALUE_PAYMENT_ORDERS = "LowValuePaymentOrders"
    CREW_LIST_DECLARATION = "CrewListDeclaration"
    INQUIRY = "Inquiry"
    RESPONSE_TO_PREVIOUS_BANKING_STATUS_MESSAGE = (
        "ResponseToPreviousBankingStatusMessage"
    )
    PROJECT_MASTER_PLAN = "ProjectMasterPlan"
    PROJECT_PLAN = "ProjectPlan"
    PROJECT_SCHEDULE = "ProjectSchedule"
    PROJECT_PLANNING_AVAILABLE_RESOURCES = "ProjectPlanningAvailableResources"
    PROJECT_PLANNING_CALENDAR = "ProjectPlanningCalendar"
    STANDING_ORDER = "StandingOrder"
    CARGO_MOVEMENT_EVENT_LOG = "CargoMovementEventLog"
    CARGO_ANALYSIS_VOYAGE_REPORT = "CargoAnalysisVoyageReport"
    SELF_BILLED_CREDIT_NOTE = "SelfBilledCreditNote"
    CONSOLIDATED_CREDIT_NOTE_GOODS_AND_SERVICES = (
        "ConsolidatedCreditNote-GoodsAndServices"
    )
    INVENTORY_ADJUSTMENT_STATUS_REPORT = "InventoryAdjustmentStatusReport"
    TRANSPORT_EQUIPMENT_MOVEMENT_INSTRUCTION = (
        "TransportEquipmentMovementInstruction"
    )
    TRANSPORT_EQUIPMENT_MOVEMENT_REPORT = "TransportEquipmentMovementReport"
    TRANSPORT_EQUIPMENT_STATUS_CHANGE_REPORT = (
        "TransportEquipmentStatusChangeReport"
    )
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
    UNITED_NATIONS_STANDARD_MESSAGE_REQUEST = (
        "UnitedNationsStandardMessageRequest"
    )
    SERVICE_DIRECTORY_DEFINITION = "ServiceDirectoryDefinition"
    STATUS_REPORT = "StatusReport"
    KANBAN_SCHEDULE = "KanbanSchedule"
    PRODUCT_DATA_MESSAGE = "ProductDataMessage"
    ACLAIM_FOR_PARTS_AND_OR_LABOUR_CHARGES = "AClaimForPartsAndOrLabourCharges"
    DELIVERY_SCHEDULE_RESPONSE = "DeliveryScheduleResponse"
    INSPECTION_REQUEST = "InspectionRequest"
    INSPECTION_REPORT = "InspectionReport"
    APPLICATION_ACKNOWLEDGEMENT_AND_ERROR_REPORT = (
        "ApplicationAcknowledgementAndErrorReport"
    )
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
    APPLICATION_ERROR_AND_ACKNOWLEDGEMENT = (
        "ApplicationErrorAndAcknowledgement"
    )
    CASH_POOL_FINANCIAL_STATEMENT = "CashPoolFinancialStatement"
    SEQUENCED_DELIVERY_SCHEDULE = "SequencedDeliverySchedule"
    DELCREDERE_CREDIT_NOTE = "DelcredereCreditNote"
    OFFER_QUOTATION = "OfferQuotation"
    REQUEST_FOR_QUOTE = "RequestForQuote"
    ACKNOWLEDGEMENT_MESSAGE = "AcknowledgementMessage"
    APPLICATION_ERROR_MESSAGE = "ApplicationErrorMessage"
    CARGO_MOVEMENT_VOYAGE_SUMMARY = "CargoMovementVoyageSummary"
    CONTRACT = "Contract"
    APPLICATION_FOR_USAGE_OF_BERTH_OR_MOORING_FACILITIES = (
        "ApplicationForUsageOfBerthOrMooringFacilities"
    )
    APPLICATION_FOR_DESIGNATION_OF_BERTHING_PLACES = (
        "ApplicationForDesignationOfBerthingPlaces"
    )
    APPLICATION_FOR_SHIFTING_FROM_THE_DESIGNATED_PLACE_IN_PORT = (
        "ApplicationForShiftingFromTheDesignatedPlaceInPort"
    )
    SUPPLEMENTARY_DOCUMENT_FOR_APPLICATION_FOR_CARGO_OPERATION_OF_DANGEROUS_GOODS = "SupplementaryDocumentForApplicationForCargoOperationOfDangerousGoods"
    ACKNOWLEDGEMENT_OF_ORDER = "AcknowledgementOfOrder"
    SUPPLEMENTARY_DOCUMENT_FOR_APPLICATION_FOR_TRANSPORT_OF_DANGEROUS_GOODS = (
        "SupplementaryDocumentForApplicationForTransportOfDangerousGoods"
    )
    OPTICAL_CHARACTER_READING_OCR_PAYMENT = "OpticalCharacterReadingOcrPayment"
    PRELIMINARY_SALES_REPORT = "PreliminarySalesReport"
    TRANSPORT_EMERGENCY_CARD = "TransportEmergencyCard"
    PROFORMA_INVOICE = "ProformaInvoice"
    PARTIAL_INVOICE = "PartialInvoice"
    OPERATING_INSTRUCTIONS = "OperatingInstructions"
    NAME_PRODUCT_PLATE = "NameProductPlate"
    CO_INSURANCE_CEDING_BORDEREAU = "Co-InsuranceCedingBordereau"
    REQUEST_FOR_DELIVERY_INSTRUCTIONS = "RequestForDeliveryInstructions"
    COMMERCIAL_INVOICE_WHICH_INCLUDES_APACKING_LIST = (
        "CommercialInvoiceWhichIncludesAPackingList"
    )
    TRADE_DATA = "TradeData"
    CUSTOMS_DECLARATION_FOR_CARGO_EXAMINATION = (
        "CustomsDeclarationForCargoExamination"
    )
    CUSTOMS_DECLARATION_FOR_CARGO_EXAMINATION_ALTERNATE = (
        "CustomsDeclarationForCargoExaminationAlternate"
    )
    BOOKING_REQUEST = "BookingRequest"
    CUSTOMS_CREW_AND_CONVEYANCE = "CustomsCrewAndConveyance"
    CUSTOMS_SUMMARY_DECLARATION_WITH_COMMERCIAL_DETAIL_ALTERNATE = (
        "CustomsSummaryDeclarationWithCommercialDetailAlternate"
    )
    ITEMS_BOOKED_TO_AFINANCIAL_ACCOUNT_REPORT = (
        "ItemsBookedToAFinancialAccountReport"
    )
    REPORT_OF_TRANSACTIONS_WHICH_NEED_FURTHER_INFORMATION_FROM_THE_RECEIVER = (
        "ReportOfTransactionsWhichNeedFurtherInformationFromTheReceiver"
    )
    SHIPPING_INSTRUCTIONS = "ShippingInstructions"
    SHIPPERS_LETTER_OF_INSTRUCTIONS_AIR = "ShippersLetterOfInstructionsAir"
    REPORT_OF_TRANSACTIONS_FOR_INFORMATION_ONLY = (
        "ReportOfTransactionsForInformationOnly"
    )
    CARTAGE_ORDER_LOCAL_TRANSPORT = "CartageOrderLocalTransport"
    EDI_ASSOCIATED_OBJECT_ADMINISTRATION_MESSAGE = (
        "EdiAssociatedObjectAdministrationMessage"
    )
    READY_FOR_DESPATCH_ADVICE = "ReadyForDespatchAdvice"
    SUMMARY_SALES_REPORT = "SummarySalesReport"
    ORDER_STATUS_ENQUIRY = "OrderStatusEnquiry"
    ORDER_STATUS_REPORT = "OrderStatusReport"
    DECLARATION_REGARDING_THE_INWARD_AND_OUTWARD_MOVEMENT_OF_VESSEL = (
        "DeclarationRegardingTheInwardAndOutwardMovementOfVessel"
    )
    DESPATCH_ORDER = "DespatchOrder"
    DESPATCH_ADVICE = "DespatchAdvice"
    NOTIFICATION_OF_USAGE_OF_BERTH_OR_MOORING_FACILITIES = (
        "NotificationOfUsageOfBerthOrMooringFacilities"
    )
    APPLICATION_FOR_VESSELS_ENTERING_INTO_PORT_AREA_IN_NIGHT_TIME = (
        "ApplicationForVesselsEnteringIntoPortAreaInNight-Time"
    )
    NOTIFICATION_OF_EMERGENCY_SHIFTING_FROM_THE_DESIGNATED_PLACE_IN_PORT = (
        "NotificationOfEmergencyShiftingFromTheDesignatedPlaceInPort"
    )
    CUSTOMS_SUMMARY_DECLARATION_WITHOUT_COMMERCIAL_DETAIL_ALTERNATE = (
        "CustomsSummaryDeclarationWithoutCommercialDetailAlternate"
    )
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
    MEANS_OF_TRANSPORTATION_AVAILABILITY_INFORMATION = (
        "MeansOfTransportationAvailabilityInformation"
    )
    MEANS_OF_TRANSPORTATION_SCHEDULE_INFORMATION = (
        "MeansOfTransportationScheduleInformation"
    )
    TRANSPORT_EQUIPMENT_DELIVERY_NOTICE = "TransportEquipmentDeliveryNotice"
    INSTRUCTIONS_FOR_BANK_TRANSFER = "InstructionsForBankTransfer"
    APPLICATION_FOR_BANKERS_DRAFT = "ApplicationForBankersDraft"
    COLLECTION_PAYMENT_ADVICE = "CollectionPaymentAdvice"
    DOCUMENTARY_CREDIT_PAYMENT_ADVICE = "DocumentaryCreditPaymentAdvice"
    DOCUMENTARY_CREDIT_ACCEPTANCE_ADVICE = "DocumentaryCreditAcceptanceAdvice"
    DOCUMENTARY_CREDIT_NEGOTIATION_ADVICE = (
        "DocumentaryCreditNegotiationAdvice"
    )
    APPLICATION_FOR_BANKERS_GUARANTEE = "ApplicationForBankersGuarantee"
    BANKERS_GUARANTEE = "BankersGuarantee"
    DOCUMENTARY_CREDIT_LETTER_OF_INDEMNITY = (
        "DocumentaryCreditLetterOfIndemnity"
    )
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
    DOCUMENTARY_CREDIT_AMENDMENT_NOTIFICATION = (
        "DocumentaryCreditAmendmentNotification"
    )
    DOCUMENTARY_CREDIT_AMENDMENT = "DocumentaryCreditAmendment"
    REMITTANCE_ADVICE = "RemittanceAdvice"
    BANKERS_DRAFT = "BankersDraft"
    BILL_OF_EXCHANGE = "BillOfExchange"
    PROMISSORY_NOTE = "PromissoryNote"
    FINANCIAL_STATEMENT_OF_ACCOUNT = "FinancialStatementOfAccount"
    STATEMENT_OF_ACCOUNT_MESSAGE = "StatementOfAccountMessage"
    INSURANCE_CERTIFICATE = "InsuranceCertificate"
    INSURANCE_POLICY = "InsurancePolicy"
    INSURANCE_DECLARATION_SHEET_BORDEREAU = (
        "InsuranceDeclarationSheetBordereau"
    )
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
    UNIVERSAL_MULTIPURPOSE_TRANSPORT_DOCUMENT = (
        "UniversalMultipurposeTransportDocument"
    )
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
    NON_NEGOTIABLE_MARITIME_TRANSPORT_DOCUMENT_GENERIC = (
        "Non-NegotiableMaritimeTransportDocumentGeneric"
    )
    MATES_RECEIPT = "MatesReceipt"
    HOUSE_BILL_OF_LADING = "HouseBillOfLading"
    LETTER_OF_INDEMNITY_FOR_NON_SURRENDER_OF_BILL_OF_LADING = (
        "LetterOfIndemnityForNon-SurrenderOfBillOfLading"
    )
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
    MULTIMODAL_COMBINED_TRANSPORT_DOCUMENT_GENERIC = (
        "MultimodalCombinedTransportDocumentGeneric"
    )
    THROUGH_BILL_OF_LADING = "ThroughBillOfLading"
    FORWARDERS_CERTIFICATE_OF_TRANSPORT = "ForwardersCertificateOfTransport"
    COMBINED_TRANSPORT_DOCUMENT_GENERIC = "CombinedTransportDocumentGeneric"
    MULTIMODAL_TRANSPORT_DOCUMENT_GENERIC = (
        "MultimodalTransportDocumentGeneric"
    )
    COMBINED_TRANSPORT_BILL_OF_LADING_MULTIMODAL_BILL_OF_LADING = (
        "CombinedTransportBillOfLadingMultimodalBillOfLading"
    )
    BOOKING_CONFIRMATION = "BookingConfirmation"
    CALLING_FORWARD_NOTICE = "CallingForwardNotice"
    FREIGHT_INVOICE = "FreightInvoice"
    ARRIVAL_NOTICE_GOODS = "ArrivalNoticeGoods"
    NOTICE_OF_CIRCUMSTANCES_PREVENTING_DELIVERY_GOODS = (
        "NoticeOfCircumstancesPreventingDeliveryGoods"
    )
    NOTICE_OF_CIRCUMSTANCES_PREVENTING_TRANSPORT_GOODS = (
        "NoticeOfCircumstancesPreventingTransportGoods"
    )
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
    APPLICATION_FOR_GOODS_CONTROL_CERTIFICATE = (
        "ApplicationForGoodsControlCertificate"
    )
    GOODS_CONTROL_CERTIFICATE = "GoodsControlCertificate"
    APPLICATION_FOR_PHYTOSANITARY_CERTIFICATE = (
        "ApplicationForPhytosanitaryCertificate"
    )
    PHYTOSANITARY_CERTIFICATE = "PhytosanitaryCertificate"
    SANITARY_CERTIFICATE = "SanitaryCertificate"
    VETERINARY_CERTIFICATE = "VeterinaryCertificate"
    APPLICATION_FOR_INSPECTION_CERTIFICATE = (
        "ApplicationForInspectionCertificate"
    )
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
    CUSTOMS_DECLARATION_WITHOUT_COMMERCIAL_DETAIL = (
        "CustomsDeclarationWithoutCommercialDetail"
    )
    CUSTOMS_DECLARATION_WITH_COMMERCIAL_AND_ITEM_DETAIL = (
        "CustomsDeclarationWithCommercialAndItemDetail"
    )
    CUSTOMS_DECLARATION_WITHOUT_ITEM_DETAIL = (
        "CustomsDeclarationWithoutItemDetail"
    )
    RELATED_DOCUMENT = "RelatedDocument"
    RECEIPT_CUSTOMS = "ReceiptCustoms"
    APPLICATION_FOR_EXCHANGE_ALLOCATION = "ApplicationForExchangeAllocation"
    FOREIGN_EXCHANGE_PERMIT = "ForeignExchangePermit"
    EXCHANGE_CONTROL_DECLARATION_IMPORT = "ExchangeControlDeclarationImport"
    GOODS_DECLARATION_FOR_IMPORTATION = "GoodsDeclarationForImportation"
    GOODS_DECLARATION_FOR_HOME_USE = "GoodsDeclarationForHomeUse"
    CUSTOMS_IMMEDIATE_RELEASE_DECLARATION = (
        "CustomsImmediateReleaseDeclaration"
    )
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
    TAX_CALCULATION_CONFIRMATION_RESPONSE_CUSTOMS = (
        "TaxCalculationConfirmationResponseCustoms"
    )
    QUOTA_PRIOR_ALLOCATION_CERTIFICATE = "QuotaPriorAllocationCertificate"
    END_USE_AUTHORIZATION = "EndUseAuthorization"
    GOVERNMENT_CONTRACT = "GovernmentContract"
    STATISTICAL_DOCUMENT_IMPORT = "StatisticalDocumentImport"
    APPLICATION_FOR_DOCUMENTARY_CREDIT = "ApplicationForDocumentaryCredit"
    PREVIOUS_CUSTOMS_DOCUMENT_MESSAGE = "PreviousCustomsDocumentMessage"


@dataclass(kw_only=True)
class PackageId:
    class Meta:
        name = "PackageID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageIdentifierCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageIdentifierCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageIdentifierValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageMarkCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageMarkCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageMarkValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PackageTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentResponsibilityCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentResponsibilityCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ReturnLoadCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ReturnLoadCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ReturnNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SpecialHandlingCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SpecialHandlingCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SpecialHandlingNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
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
class HazardousPackaging:
    hazardous: Hazardous = field(
        metadata={
            "name": "Hazardous",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfLocationGroupedShippingDetail:
    location_grouped_shipping_detail: List[
        LocationGroupedShippingDetail
    ] = field(
        default_factory=list,
        metadata={
            "name": "LocationGroupedShippingDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfMaterialGroupedShippingDetail:
    material_grouped_shipping_detail: List[
        MaterialGroupedShippingDetail
    ] = field(
        default_factory=list,
        metadata={
            "name": "MaterialGroupedShippingDetail",
            "type": "Element",
            "min_occurs": 1,
        },
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
        },
    )
    document_title: Optional[DocumentTitle] = field(
        default=None,
        metadata={
            "name": "DocumentTitle",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PackageIdentifier:
    package_identifier_coded: PackageIdentifierCoded = field(
        metadata={
            "name": "PackageIdentifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_identifier_coded_other: Optional[
        PackageIdentifierCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "PackageIdentifierCodedOther",
            "type": "Element",
        },
    )
    package_identifier_value: Optional[PackageIdentifierValue] = field(
        default=None,
        metadata={
            "name": "PackageIdentifierValue",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PackageMark:
    package_mark_coded: PackageMarkCoded = field(
        metadata={
            "name": "PackageMarkCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_mark_coded_other: Optional[PackageMarkCodedOther] = field(
        default=None,
        metadata={
            "name": "PackageMarkCodedOther",
            "type": "Element",
        },
    )
    package_mark_value: Optional[PackageMarkValue] = field(
        default=None,
        metadata={
            "name": "PackageMarkValue",
            "type": "Element",
        },
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
class QuoteReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
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
class SpecialHandling:
    special_handling_coded: SpecialHandlingCoded = field(
        metadata={
            "name": "SpecialHandlingCoded",
            "type": "Element",
            "required": True,
        }
    )
    special_handling_coded_other: Optional[SpecialHandlingCodedOther] = field(
        default=None,
        metadata={
            "name": "SpecialHandlingCodedOther",
            "type": "Element",
        },
    )
    special_handling_note: Optional[SpecialHandlingNote] = field(
        default=None,
        metadata={
            "name": "SpecialHandlingNote",
            "type": "Element",
        },
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
class ListOfPackageIdentifier:
    package_identifier: List[PackageIdentifier] = field(
        default_factory=list,
        metadata={
            "name": "PackageIdentifier",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfPackageMark:
    package_mark: List[PackageMark] = field(
        default_factory=list,
        metadata={
            "name": "PackageMark",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class OrderReferences:
    account_code: Optional[AccountCode] = field(
        default=None,
        metadata={
            "name": "AccountCode",
            "type": "Element",
        },
    )
    contract_references: Optional[ContractReferences] = field(
        default=None,
        metadata={
            "name": "ContractReferences",
            "type": "Element",
        },
    )
    quote_reference: Optional[QuoteReference] = field(
        default=None,
        metadata={
            "name": "QuoteReference",
            "type": "Element",
        },
    )
    other_order_references: Optional[OtherOrderReferences] = field(
        default=None,
        metadata={
            "name": "OtherOrderReferences",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PackageCharacteristic:
    package_characteristic_coded: PackageCharacteristicCoded = field(
        metadata={
            "name": "PackageCharacteristicCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_characteristic_coded_other: Optional[
        PackageCharacteristicCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "PackageCharacteristicCodedOther",
            "type": "Element",
        },
    )
    package_characteristic_description: PackageCharacteristicDescription = (
        field(
            metadata={
                "name": "PackageCharacteristicDescription",
                "type": "Element",
                "required": True,
            }
        )
    )


@dataclass(kw_only=True)
class PackageType:
    package_type_coded: PackageTypeCoded = field(
        metadata={
            "name": "PackageTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    package_type_coded_other: Optional[PackageTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "PackageTypeCodedOther",
            "type": "Element",
        },
    )
    package_type_description: Optional[PackageTypeDescription] = field(
        default=None,
        metadata={
            "name": "PackageTypeDescription",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ReturnableContainerInfo:
    returnable_container_part_number: Optional[
        ReturnableContainerPartNumber
    ] = field(
        default=None,
        metadata={
            "name": "ReturnableContainerPartNumber",
            "type": "Element",
        },
    )
    payment_responsibility_coded: Optional[PaymentResponsibilityCoded] = field(
        default=None,
        metadata={
            "name": "PaymentResponsibilityCoded",
            "type": "Element",
        },
    )
    payment_responsibility_coded_other: Optional[
        PaymentResponsibilityCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "PaymentResponsibilityCodedOther",
            "type": "Element",
        },
    )
    return_load_coded: Optional[ReturnLoadCoded] = field(
        default=None,
        metadata={
            "name": "ReturnLoadCoded",
            "type": "Element",
        },
    )
    return_load_coded_other: Optional[ReturnLoadCodedOther] = field(
        default=None,
        metadata={
            "name": "ReturnLoadCodedOther",
            "type": "Element",
        },
    )
    return_note: Optional[ReturnNote] = field(
        default=None,
        metadata={
            "name": "ReturnNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfDocumentAttached:
    document_attached: List[DocumentAttached] = field(
        default_factory=list,
        metadata={
            "name": "DocumentAttached",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfDocumentLoose:
    document_loose: List[DocumentLoose] = field(
        default_factory=list,
        metadata={
            "name": "DocumentLoose",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfOrderReferences:
    order_references: List[OrderReferences] = field(
        default_factory=list,
        metadata={
            "name": "OrderReferences",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfPackageCharacteristic:
    package_characteristic: List[PackageCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "PackageCharacteristic",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PackageDescription:
    list_of_package_identifier: Optional[ListOfPackageIdentifier] = field(
        default=None,
        metadata={
            "name": "ListOfPackageIdentifier",
            "type": "Element",
        },
    )
    container_counter: Optional[ContainerCounter] = field(
        default=None,
        metadata={
            "name": "ContainerCounter",
            "type": "Element",
        },
    )
    load_order_counter: Optional[LoadOrderCounter] = field(
        default=None,
        metadata={
            "name": "LoadOrderCounter",
            "type": "Element",
        },
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
    number_of_packages: NumberOfPackages = field(
        metadata={
            "name": "NumberOfPackages",
            "type": "Element",
            "required": True,
        }
    )
    list_of_package: Optional["ListOfPackage"] = field(
        default=None,
        metadata={
            "name": "ListOfPackage",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AssociatedDocuments:
    list_of_document_loose: Optional[ListOfDocumentLoose] = field(
        default=None,
        metadata={
            "name": "ListOfDocumentLoose",
            "type": "Element",
        },
    )
    list_of_document_attached: Optional[ListOfDocumentAttached] = field(
        default=None,
        metadata={
            "name": "ListOfDocumentAttached",
            "type": "Element",
        },
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
class ListOfPackageDescription:
    package_description: List[PackageDescription] = field(
        default_factory=list,
        metadata={
            "name": "PackageDescription",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfPackageDetail:
    package_detail: List[PackageDetail] = field(
        default_factory=list,
        metadata={
            "name": "PackageDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Package:
    package_id: PackageId = field(
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
        },
    )
    list_of_package_mark: Optional[ListOfPackageMark] = field(
        default=None,
        metadata={
            "name": "ListOfPackageMark",
            "type": "Element",
        },
    )
    list_of_package_characteristic: Optional[
        ListOfPackageCharacteristic
    ] = field(
        default=None,
        metadata={
            "name": "ListOfPackageCharacteristic",
            "type": "Element",
        },
    )
    list_of_dimension: Optional[ListOfDimension] = field(
        default=None,
        metadata={
            "name": "ListOfDimension",
            "type": "Element",
        },
    )
    list_of_package_description: Optional[ListOfPackageDescription] = field(
        default=None,
        metadata={
            "name": "ListOfPackageDescription",
            "type": "Element",
        },
    )
    transport_reference: Optional[TransportReference] = field(
        default=None,
        metadata={
            "name": "TransportReference",
            "type": "Element",
        },
    )
    special_handling: Optional[SpecialHandling] = field(
        default=None,
        metadata={
            "name": "SpecialHandling",
            "type": "Element",
        },
    )
    hazardous_packaging: Optional[HazardousPackaging] = field(
        default=None,
        metadata={
            "name": "HazardousPackaging",
            "type": "Element",
        },
    )
    associated_documents: Optional[AssociatedDocuments] = field(
        default=None,
        metadata={
            "name": "AssociatedDocuments",
            "type": "Element",
        },
    )
    shipping_instructions: Optional[ShippingInstructions] = field(
        default=None,
        metadata={
            "name": "ShippingInstructions",
            "type": "Element",
        },
    )
    returnable_container_info: Optional[ReturnableContainerInfo] = field(
        default=None,
        metadata={
            "name": "ReturnableContainerInfo",
            "type": "Element",
        },
    )
    package_detail: List[PackageDetail] = field(
        default_factory=list,
        metadata={
            "name": "PackageDetail",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ShippingSchedule:
    shipping_schedule_header: ShippingScheduleHeader = field(
        metadata={
            "name": "ShippingScheduleHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_location_grouped_shipping_detail: Optional[
        ListOfLocationGroupedShippingDetail
    ] = field(
        default=None,
        metadata={
            "name": "ListOfLocationGroupedShippingDetail",
            "type": "Element",
        },
    )
    list_of_material_grouped_shipping_detail: Optional[
        ListOfMaterialGroupedShippingDetail
    ] = field(
        default=None,
        metadata={
            "name": "ListOfMaterialGroupedShippingDetail",
            "type": "Element",
        },
    )
    list_of_package_detail: Optional[ListOfPackageDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
        },
    )
    shipping_schedule_summary: Optional[ShippingScheduleSummary] = field(
        default=None,
        metadata={
            "name": "ShippingScheduleSummary",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfPackage:
    package: List[Package] = field(
        default_factory=list,
        metadata={
            "name": "Package",
            "type": "Element",
            "min_occurs": 1,
        },
    )
