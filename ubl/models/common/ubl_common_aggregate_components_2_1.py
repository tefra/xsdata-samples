from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime
from ubl.models.common.ubl_common_basic_components_2_1 import (
    AcceptedVariantsDescription,
    AccountFormatCode,
    AccountId,
    AccountTypeCode,
    AccountingCost,
    AccountingCostCode,
    ActionCode,
    ActivityType,
    ActivityTypeCode,
    ActualTemperatureReductionQuantity,
    AdditionalAccountId,
    AdditionalConditions,
    AdditionalInformation,
    AdditionalStreetName,
    AddressFormatCode,
    AddressTypeCode,
    AdjustmentReasonCode,
    AdmissionCode,
    AdvertisementAmount,
    AgencyId,
    AgencyName,
    AirFlowPercent,
    AircraftId,
    AliasName,
    AllowanceChargeReason,
    AllowanceChargeReasonCode,
    AllowanceTotalAmount,
    AltitudeMeasure,
    Amount,
    AmountRate,
    AnnualAverageAmount,
    ApplicationStatusCode,
    ApprovalStatus,
    AttributeId,
    AuctionUri,
    AvailabilityStatusCode,
    AverageAmount,
    AverageSubsequentContractAmount,
    AwardingCriterionDescription,
    AwardingCriterionId,
    AwardingCriterionTypeCode,
    AwardingMethodTypeCode,
    BackorderQuantity,
    BackorderReason,
    BalanceAmount,
    BarcodeSymbologyId,
    BaseAmount,
    BaseQuantity,
    BaseUnitMeasure,
    BasicConsumedQuantity,
    BatchQuantity,
    BirthplaceName,
    BlockName,
    BrandName,
    BrokerAssignedId,
    BudgetYearNumeric,
    BuildingName,
    BuildingNumber,
    BusinessClassificationEvidenceId,
    BusinessIdentityEvidenceId,
    BuyerProfileUri,
    Cv2Id,
    CalculationExpression,
    CalculationExpressionCode,
    CalculationMethodCode,
    CalculationRate,
    CalculationSequenceNumeric,
    CallBaseAmount,
    CallExtensionAmount,
    CandidateStatement,
    CanonicalizationMethod,
    CapabilityTypeCode,
    CardChipCode,
    CardTypeCode,
    CargoTypeCode,
    CarrierAssignedId,
    CarrierServiceInstructions,
    CategoryName,
    CertificateType as UblCommonBasicComponents21CertificateType,
    CertificateTypeCode,
    ChangeConditions,
    Channel,
    ChannelCode,
    CharacterSetCode,
    Characteristics,
    ChargeTotalAmount,
    ChargeableQuantity,
    ChargeableWeightMeasure,
    ChildConsignmentQuantity,
    ChipApplicationId,
    CityName,
    CitySubdivisionName,
    CodeValue,
    CollaborationPriorityCode,
    Comment,
    CommodityCode,
    CompanyId,
    CompanyLegalForm,
    CompanyLegalFormCode,
    CompanyLiquidationStatusCode,
    ComparedValueMeasure,
    ComparisonDataCode,
    ComparisonDataSourceCode,
    Condition as UblCommonBasicComponents21Condition,
    ConditionCode,
    Conditions,
    ConditionsDescription,
    ConsigneeAssignedId,
    ConsignmentQuantity,
    ConsignorAssignedId,
    ConsumerIncentiveTacticTypeCode,
    ConsumerUnitQuantity,
    ConsumersEnergyLevel,
    ConsumersEnergyLevelCode,
    ConsumptionEnergyQuantity,
    ConsumptionId,
    ConsumptionLevel,
    ConsumptionLevelCode,
    ConsumptionReportId,
    ConsumptionType as UblCommonBasicComponents21ConsumptionType,
    ConsumptionTypeCode,
    ConsumptionWaterQuantity,
    Content,
    ContentUnitQuantity,
    ContractSubdivision,
    ContractType as UblCommonBasicComponents21ContractType,
    ContractTypeCode,
    ContractedCarrierAssignedId,
    ContractingSystemCode,
    CoordinateSystemCode,
    CorporateRegistrationTypeCode,
    CorporateStockAmount,
    CorrectionAmount,
    CorrectionType,
    CorrectionTypeCode,
    CorrectionUnitAmount,
    CountrySubentity,
    CountrySubentityCode,
    CreditLineAmount,
    CreditedQuantity,
    CrewQuantity,
    CurrencyCode,
    CurrentChargeType,
    CurrentChargeTypeCode,
    CustomerAssignedAccountId,
    CustomerReference,
    CustomsClearanceServiceInstructions,
    CustomsStatusCode,
    CustomsTariffQuantity,
    DamageRemarks,
    DataSendingCapability,
    DataSourceCode,
    DebitLineAmount,
    DebitedQuantity,
    DeclarationTypeCode,
    DeclaredCustomsValueAmount,
    DeclaredForCarriageValueAmount,
    DeclaredStatisticsValueAmount,
    DeliveredQuantity,
    DeliveryInstructions,
    DemurrageInstructions,
    Department,
    Description,
    DescriptionCode,
    DifferenceTemperatureReductionQuantity,
    DirectionCode,
    DisplayTacticTypeCode,
    DispositionCode,
    District,
    DocumentDescription,
    DocumentHash,
    DocumentId,
    DocumentStatusCode,
    DocumentType,
    DocumentTypeCode,
    DocumentationFeeAmount,
    DurationMeasure,
    Duty as UblCommonBasicComponents21Duty,
    DutyCode,
    EconomicOperatorRegistryUri,
    ElectronicDeviceDescription,
    ElectronicMail,
    EmbeddedDocumentBinaryObject,
    EmergencyProceduresCode,
    EmployeeQuantity,
    EncodingCode,
    EndpointId,
    EnvironmentalEmissionTypeCode,
    EstimatedAmount,
    EstimatedConsumedQuantity,
    EstimatedOverallContractAmount,
    EstimatedOverallContractQuantity,
    EvaluationCriterionTypeCode,
    EvidenceTypeCode,
    ExceptionResolutionCode,
    ExceptionStatusCode,
    ExchangeMarketId,
    ExclusionReason,
    ExecutionRequirementCode,
    ExemptionReason,
    ExemptionReasonCode,
    ExpectedOperatorQuantity,
    ExpectedQuantity,
    ExpenseCode,
    Expression,
    ExpressionCode,
    ExtendedId,
    Extension,
    FaceValueAmount,
    FamilyName,
    FeatureTacticTypeCode,
    FeeAmount,
    FeeDescription,
    FileName,
    FinancingInstrumentCode,
    FirstName,
    Floor,
    ForecastPurposeCode,
    ForecastTypeCode,
    FormatCode,
    ForwarderServiceInstructions,
    FreeOnBoardValueAmount,
    FreightForwarderAssignedId,
    FreightRateClassCode,
    Frequency,
    FrozenPeriodDaysNumeric,
    FullnessIndicationCode,
    FundingProgram,
    FundingProgramCode,
    GasPressureQuantity,
    GenderCode,
    GrossTonnageMeasure,
    GrossVolumeMeasure,
    GrossWeightMeasure,
    GuaranteeTypeCode,
    HandlingCode,
    HandlingInstructions,
    HashAlgorithmMethod,
    HaulageInstructions,
    HazardClassId,
    HazardousCategoryCode,
    HazardousRegulationCode,
    HeatingType,
    HeatingTypeCode,
    HigherTenderAmount,
    HolderName,
    HumidityPercent,
    Id,
    IdentificationCode,
    IdentificationId,
    ImmobilizationCertificateId,
    ImportanceCode,
    IndustryClassificationCode,
    Information,
    InformationUri,
    InhalationToxicityZoneCode,
    InhouseMail,
    InspectionMethodCode,
    InstructionId,
    InstructionNote,
    Instructions,
    InsurancePremiumAmount,
    InsuranceValueAmount,
    InventoryValueAmount,
    InvoicedQuantity,
    InvoicingPartyReference,
    IssueNumberId,
    IssuerId,
    ItemClassificationCode,
    JobTitle,
    JourneyId,
    Justification,
    JustificationDescription,
    Keyword,
    LanguageId,
    LatestMeterQuantity,
    LatestMeterReadingMethod,
    LatestMeterReadingMethodCode,
    LatitudeDegreesMeasure,
    LatitudeDirectionCode,
    LatitudeMinutesMeasure,
    LeadTimeMeasure,
    LegalReference,
    LiabilityAmount,
    LicensePlateId,
    LifeCycleStatusCode,
    LimitationDescription,
    Line,
    LineExtensionAmount,
    LineId,
    LineNumberNumeric,
    LineStatusCode,
    ListValue,
    LoadingLengthMeasure,
    LoadingSequenceId,
    LocaleCode,
    Location as UblCommonBasicComponents21Location,
    LocationId,
    LocationTypeCode,
    Login,
    LogoReferenceId,
    LongitudeDegreesMeasure,
    LongitudeDirectionCode,
    LongitudeMinutesMeasure,
    LossRisk,
    LossRiskResponsibilityCode,
    LotNumberId,
    LowTendersDescription,
    LowerOrangeHazardPlacardId,
    LowerTenderAmount,
    MandateTypeCode,
    MarkAttention,
    MarkCare,
    MarketValueAmount,
    MarkingId,
    MathematicOperatorCode,
    MaximumAdvertisementAmount,
    MaximumAmount,
    MaximumBackorderQuantity,
    MaximumCopiesNumeric,
    MaximumMeasure,
    MaximumNumberNumeric,
    MaximumOperatorQuantity,
    MaximumOrderQuantity,
    MaximumPaidAmount,
    MaximumPaymentInstructionsNumeric,
    MaximumPercent,
    MaximumQuantity,
    MaximumValue,
    MaximumVariantQuantity,
    Measure,
    MedicalFirstAidGuideCode,
    MeterConstant,
    MeterConstantCode,
    MeterName,
    MeterNumber,
    MeterReadingComments,
    MeterReadingType as UblCommonBasicComponents21MeterReadingType,
    MeterReadingTypeCode,
    MiddleName,
    MimeCode,
    MinimumAmount,
    MinimumBackorderQuantity,
    MinimumImprovementBid,
    MinimumInventoryQuantity,
    MinimumMeasure,
    MinimumNumberNumeric,
    MinimumOrderQuantity,
    MinimumPercent,
    MinimumQuantity,
    MinimumValue,
    MiscellaneousEventTypeCode,
    ModelName,
    MonetaryScope,
    MovieTitle,
    MultipleOrderQuantity,
    MultiplierFactorNumeric,
    Name,
    NameCode,
    NameSuffix,
    NationalityId,
    NatureCode,
    NegotiationDescription,
    NetNetWeightMeasure,
    NetTonnageMeasure,
    NetVolumeMeasure,
    NetWeightMeasure,
    NetworkId,
    NormalTemperatureReductionQuantity,
    Note,
    NotificationTypeCode,
    OneTimeChargeType,
    OneTimeChargeTypeCode,
    OntologyUri,
    OpenTenderId,
    OperatingYearsQuantity,
    OptionsDescription,
    OrderIntervalDaysNumeric,
    OrderQuantityIncrementNumeric,
    OrderTypeCode,
    OrderableUnit,
    OrderableUnitFactorRate,
    OrganizationDepartment,
    OriginalContractingSystemId,
    OriginalJobId,
    OtherName,
    OutstandingQuantity,
    OutstandingReason,
    OversupplyQuantity,
    OwnerTypeCode,
    PackLevelCode,
    PackQuantity,
    PackSizeNumeric,
    PackageLevelCode,
    PackagingTypeCode,
    PackingCriteriaCode,
    PackingMaterial,
    PaidAmount,
    ParentDocumentLineReferenceId,
    PartPresentationCode,
    PartecipationPercent,
    ParticipationPercent,
    PartyCapacityAmount,
    PartyType as UblCommonBasicComponents21PartyType,
    PartyTypeCode,
    PassengerQuantity,
    Password,
    PayPerView,
    PayableAlternativeAmount,
    PayableAmount,
    PayableRoundingAmount,
    PaymentChannelCode,
    PaymentDescription,
    PaymentFrequencyCode,
    PaymentId,
    PaymentMeansCode,
    PaymentMeansId,
    PaymentNote,
    PaymentPercent,
    PaymentPurposeCode,
    PaymentTermsDetailsUri,
    PenaltyAmount,
    PenaltySurchargePercent,
    PerUnitAmount,
    Percent,
    PerformanceMetricTypeCode,
    PerformanceValueQuantity,
    PerformingCarrierAssignedId,
    PersonalSituation,
    PhoneNumber,
    PlacardEndorsement,
    PlacardNotation,
    PlotIdentification,
    PositionCode,
    PostEventNotificationDurationMeasure,
    PostalZone,
    Postbox,
    PreEventNotificationDurationMeasure,
    PreferenceCriterionCode,
    PrepaidAmount,
    PrepaidPaymentReferenceId,
    PreviousCancellationReasonCode,
    PreviousJobId,
    PreviousMeterQuantity,
    PreviousMeterReadingMethod,
    PreviousMeterReadingMethodCode,
    PreviousVersionId,
    PriceAmount,
    PriceChangeReason,
    PriceEvaluationCode,
    PriceRevisionFormulaDescription,
    PriceType as UblCommonBasicComponents21PriceType,
    PriceTypeCode,
    PrimaryAccountNumberId,
    PrintQualifier,
    Priority,
    PrivacyCode,
    PrizeDescription,
    ProcedureCode,
    ProcessDescription,
    ProcessReason,
    ProcessReasonCode,
    ProcurementSubTypeCode,
    ProcurementTypeCode,
    ProductTraceId,
    ProgressPercent,
    PromotionalEventTypeCode,
    ProviderTypeCode,
    QualityControlCode,
    Quantity,
    QuantityDiscrepancyCode,
    RadioCallSignId,
    RailCarId,
    Rank,
    Rate,
    ReceivedElectronicTenderQuantity,
    ReceivedForeignTenderQuantity,
    ReceivedQuantity,
    ReceivedTenderQuantity,
    Reference,
    ReferenceEventCode,
    ReferenceId,
    ReferencedConsignmentId,
    Region,
    RegistrationId,
    RegistrationName,
    RegistrationNationality,
    RegistrationNationalityId,
    RejectActionCode,
    RejectReason,
    RejectReasonCode,
    RejectedQuantity,
    ReleaseId,
    ReliabilityPercent,
    Remarks,
    ReplenishmentOwnerDescription,
    RequestForQuotationLineId,
    RequiredCustomsId,
    RequiredFeeAmount,
    ResidenceType,
    ResidenceTypeCode,
    ResidentOccupantsNumeric,
    Resolution,
    ResolutionCode,
    ResponseCode,
    ReturnableQuantity,
    RevisedForecastLineId,
    RoamingPartnerName,
    RoleCode,
    RoleDescription,
    Room,
    RoundingAmount,
    SalesOrderId,
    SalesOrderLineId,
    SchemeUri,
    SealIssuerTypeCode,
    SealStatusCode,
    SealingPartyType,
    SecurityClassificationCode,
    SecurityId,
    SequenceId,
    SequenceNumberId,
    SequenceNumeric,
    SerialId,
    ServiceNumberCalled,
    ServiceType,
    ServiceTypeCode,
    SettlementDiscountAmount,
    SettlementDiscountPercent,
    SharesNumberQuantity,
    ShippingMarks,
    ShippingPriorityLevelCode,
    ShipsRequirements,
    ShortQuantity,
    ShortageActionCode,
    SignatureId,
    SignatureMethod,
    SizeTypeCode,
    SourceCurrencyBaseRate,
    SourceCurrencyCode,
    SourceValueMeasure,
    SpecialInstructions,
    SpecialServiceInstructions,
    SpecialTerms,
    SpecialTransportRequirements,
    SpecificationId,
    SpecificationTypeCode,
    StatusCode,
    StatusReason,
    StatusReasonCode,
    StreetName,
    SubcontractingConditionsCode,
    SubmissionMethodCode,
    SubscriberId,
    SubscriberType,
    SubscriberTypeCode,
    SubstitutionStatusCode,
    SuccessiveSequenceId,
    SummaryDescription,
    SupplierAssignedAccountId,
    SupplyChainActivityTypeCode,
    TareWeightMeasure,
    TargetCurrencyBaseRate,
    TargetCurrencyCode,
    TargetInventoryQuantity,
    TargetServicePercent,
    TariffClassCode,
    TariffCode,
    TariffDescription,
    TaxAmount,
    TaxEnergyAmount,
    TaxEnergyBalanceAmount,
    TaxEnergyOnAccountAmount,
    TaxExclusiveAmount,
    TaxExemptionReason,
    TaxExemptionReasonCode,
    TaxInclusiveAmount,
    TaxLevelCode,
    TaxTypeCode,
    TaxableAmount,
    TechnicalCommitteeDescription,
    TechnicalName,
    TelecommunicationsServiceCall,
    TelecommunicationsServiceCallCode,
    TelecommunicationsServiceCategory,
    TelecommunicationsServiceCategoryCode,
    TelecommunicationsSupplyType as UblCommonBasicComponents21TelecommunicationsSupplyType,
    TelecommunicationsSupplyTypeCode,
    Telefax,
    Telephone,
    TenderEnvelopeId,
    TenderEnvelopeTypeCode,
    TenderResultCode,
    TendererRequirementTypeCode,
    TendererRoleCode,
    TestMethod,
    Text,
    ThresholdAmount,
    ThresholdQuantity,
    ThresholdValueComparisonCode,
    TierRange,
    TierRatePercent,
    TimeAmount,
    TimeDeltaDaysQuantity,
    TimeFrequencyCode,
    TimezoneOffset,
    TimingComplaint,
    TimingComplaintCode,
    Title,
    TotalAmount,
    TotalConsumedQuantity,
    TotalDeliveredQuantity,
    TotalGoodsItemQuantity,
    TotalInvoiceAmount,
    TotalMeteredQuantity,
    TotalPackageQuantity,
    TotalPackagesQuantity,
    TotalTaskAmount,
    TotalTaxAmount,
    TotalTransportHandlingUnitQuantity,
    TraceId,
    TrackingDeviceCode,
    TrackingId,
    TradeItemPackingLabelingTypeCode,
    TradeServiceCode,
    TradingRestrictions,
    TrainId,
    TransactionCurrencyTaxAmount,
    TransitDirectionCode,
    TransportAuthorizationCode,
    TransportEmergencyCardCode,
    TransportEquipmentTypeCode,
    TransportEventTypeCode,
    TransportExecutionPlanReferenceId,
    TransportHandlingUnitTypeCode,
    TransportMeansTypeCode,
    TransportModeCode,
    TransportServiceCode,
    TransportServiceProviderSpecialTerms,
    TransportUserSpecialTerms,
    TransportationServiceDescription,
    TransportationServiceDetailsUri,
    TypeCode,
    Undgcode,
    Uri,
    Uuid,
    UpperOrangeHazardPlacardId,
    UrgencyCode,
    UtilityStatementTypeCode,
    ValidateProcess,
    ValidateTool,
    ValidateToolVersion,
    ValidationResultCode,
    ValidatorId,
    Value,
    ValueAmount,
    ValueMeasure,
    ValueQualifier,
    ValueQuantity,
    VarianceQuantity,
    VariantId,
    VersionId,
    VesselId,
    VesselName,
    WarrantyInformation,
    WebsiteUri,
    WeekDayCode,
    Weight,
    WeightNumeric,
    WeightingAlgorithmCode,
    WorkPhase,
    WorkPhaseCode,
    Xpath,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ActivityPropertyType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class AddressLineType:
    line: Optional[Line] = field(
        default=None,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class AirTransportType:
    aircraft_id: Optional[AircraftId] = field(
        default=None,
        metadata={
            "name": "AircraftID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class AuctionTermsType:
    auction_constraint_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AuctionConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    justification_description: List[JustificationDescription] = field(
        default_factory=list,
        metadata={
            "name": "JustificationDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    process_description: List[ProcessDescription] = field(
        default_factory=list,
        metadata={
            "name": "ProcessDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    conditions_description: List[ConditionsDescription] = field(
        default_factory=list,
        metadata={
            "name": "ConditionsDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    electronic_device_description: List[ElectronicDeviceDescription] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicDeviceDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    auction_uri: Optional[AuctionUri] = field(
        default=None,
        metadata={
            "name": "AuctionURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class AwardingCriterionResponseType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    awarding_criterion_id: Optional[AwardingCriterionId] = field(
        default=None,
        metadata={
            "name": "AwardingCriterionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    awarding_criterion_description: List[AwardingCriterionDescription] = field(
        default_factory=list,
        metadata={
            "name": "AwardingCriterionDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    subordinate_awarding_criterion_response: List["SubordinateAwardingCriterionResponse"] = field(
        default_factory=list,
        metadata={
            "name": "SubordinateAwardingCriterionResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AwardingCriterionType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    awarding_criterion_type_code: Optional[AwardingCriterionTypeCode] = field(
        default=None,
        metadata={
            "name": "AwardingCriterionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    weight_numeric: Optional[WeightNumeric] = field(
        default=None,
        metadata={
            "name": "WeightNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    weight: List[Weight] = field(
        default_factory=list,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    calculation_expression: List[CalculationExpression] = field(
        default_factory=list,
        metadata={
            "name": "CalculationExpression",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    calculation_expression_code: Optional[CalculationExpressionCode] = field(
        default=None,
        metadata={
            "name": "CalculationExpressionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_amount: Optional[MinimumAmount] = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_amount: Optional[MaximumAmount] = field(
        default=None,
        metadata={
            "name": "MaximumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_improvement_bid: List[MinimumImprovementBid] = field(
        default_factory=list,
        metadata={
            "name": "MinimumImprovementBid",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    subordinate_awarding_criterion: List["SubordinateAwardingCriterion"] = field(
        default_factory=list,
        metadata={
            "name": "SubordinateAwardingCriterion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CardAccountType:
    primary_account_number_id: Optional[PrimaryAccountNumberId] = field(
        default=None,
        metadata={
            "name": "PrimaryAccountNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    network_id: Optional[NetworkId] = field(
        default=None,
        metadata={
            "name": "NetworkID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    card_type_code: Optional[CardTypeCode] = field(
        default=None,
        metadata={
            "name": "CardTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validity_start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValidityStartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    expiry_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issuer_id: Optional[IssuerId] = field(
        default=None,
        metadata={
            "name": "IssuerID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_number_id: Optional[IssueNumberId] = field(
        default=None,
        metadata={
            "name": "IssueNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    cv2_id: Optional[Cv2Id] = field(
        default=None,
        metadata={
            "name": "CV2ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    card_chip_code: Optional[CardChipCode] = field(
        default=None,
        metadata={
            "name": "CardChipCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    chip_application_id: Optional[ChipApplicationId] = field(
        default=None,
        metadata={
            "name": "ChipApplicationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    holder_name: Optional[HolderName] = field(
        default=None,
        metadata={
            "name": "HolderName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class CatalogueReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    revision_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RevisionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    revision_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "RevisionTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    version_id: Optional[VersionId] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    previous_version_id: Optional[PreviousVersionId] = field(
        default=None,
        metadata={
            "name": "PreviousVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ClassificationCategoryType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    code_value: Optional[CodeValue] = field(
        default=None,
        metadata={
            "name": "CodeValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    categorizes_classification_category: List["CategorizesClassificationCategory"] = field(
        default_factory=list,
        metadata={
            "name": "CategorizesClassificationCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ClauseType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    content: List[Content] = field(
        default_factory=list,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class CommodityClassificationType:
    nature_code: Optional[NatureCode] = field(
        default=None,
        metadata={
            "name": "NatureCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    cargo_type_code: Optional[CargoTypeCode] = field(
        default=None,
        metadata={
            "name": "CargoTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    commodity_code: Optional[CommodityCode] = field(
        default=None,
        metadata={
            "name": "CommodityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    item_classification_code: Optional[ItemClassificationCode] = field(
        default=None,
        metadata={
            "name": "ItemClassificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class CommunicationType:
    channel_code: Optional[ChannelCode] = field(
        default=None,
        metadata={
            "name": "ChannelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    channel: Optional[Channel] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ConditionType:
    attribute_id: Optional[AttributeId] = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    measure: Optional[Measure] = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_measure: Optional[MinimumMeasure] = field(
        default=None,
        metadata={
            "name": "MinimumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_measure: Optional[MaximumMeasure] = field(
        default=None,
        metadata={
            "name": "MaximumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ConsumptionAverageType:
    average_amount: Optional[AverageAmount] = field(
        default=None,
        metadata={
            "name": "AverageAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ConsumptionCorrectionType:
    correction_type: Optional[CorrectionType] = field(
        default=None,
        metadata={
            "name": "CorrectionType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    correction_type_code: Optional[CorrectionTypeCode] = field(
        default=None,
        metadata={
            "name": "CorrectionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    meter_number: Optional[MeterNumber] = field(
        default=None,
        metadata={
            "name": "MeterNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gas_pressure_quantity: Optional[GasPressureQuantity] = field(
        default=None,
        metadata={
            "name": "GasPressureQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    actual_temperature_reduction_quantity: Optional[ActualTemperatureReductionQuantity] = field(
        default=None,
        metadata={
            "name": "ActualTemperatureReductionQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    normal_temperature_reduction_quantity: Optional[NormalTemperatureReductionQuantity] = field(
        default=None,
        metadata={
            "name": "NormalTemperatureReductionQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    difference_temperature_reduction_quantity: Optional[DifferenceTemperatureReductionQuantity] = field(
        default=None,
        metadata={
            "name": "DifferenceTemperatureReductionQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    correction_unit_amount: Optional[CorrectionUnitAmount] = field(
        default=None,
        metadata={
            "name": "CorrectionUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumption_energy_quantity: Optional[ConsumptionEnergyQuantity] = field(
        default=None,
        metadata={
            "name": "ConsumptionEnergyQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumption_water_quantity: Optional[ConsumptionWaterQuantity] = field(
        default=None,
        metadata={
            "name": "ConsumptionWaterQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    correction_amount: Optional[CorrectionAmount] = field(
        default=None,
        metadata={
            "name": "CorrectionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ContractExecutionRequirementType:
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    execution_requirement_code: Optional[ExecutionRequirementCode] = field(
        default=None,
        metadata={
            "name": "ExecutionRequirementCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ContractingActivityType:
    activity_type_code: Optional[ActivityTypeCode] = field(
        default=None,
        metadata={
            "name": "ActivityTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    activity_type: Optional[ActivityType] = field(
        default=None,
        metadata={
            "name": "ActivityType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ContractingPartyTypeType:
    party_type_code: Optional[PartyTypeCode] = field(
        default=None,
        metadata={
            "name": "PartyTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    party_type: Optional[UblCommonBasicComponents21PartyType] = field(
        default=None,
        metadata={
            "name": "PartyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class CountryType:
    identification_code: Optional[IdentificationCode] = field(
        default=None,
        metadata={
            "name": "IdentificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class CreditAccountType:
    account_id: Optional[AccountId] = field(
        default=None,
        metadata={
            "name": "AccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class DeliveryUnitType:
    batch_quantity: Optional[BatchQuantity] = field(
        default=None,
        metadata={
            "name": "BatchQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    consumer_unit_quantity: Optional[ConsumerUnitQuantity] = field(
        default=None,
        metadata={
            "name": "ConsumerUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hazardous_risk_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class DimensionType:
    attribute_id: Optional[AttributeId] = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    measure: Optional[Measure] = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_measure: Optional[MinimumMeasure] = field(
        default=None,
        metadata={
            "name": "MinimumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_measure: Optional[MaximumMeasure] = field(
        default=None,
        metadata={
            "name": "MaximumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class EconomicOperatorRoleType:
    role_code: Optional[RoleCode] = field(
        default=None,
        metadata={
            "name": "RoleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    role_description: List[RoleDescription] = field(
        default_factory=list,
        metadata={
            "name": "RoleDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class EventCommentType:
    comment: Optional[Comment] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class EventTacticEnumerationType:
    consumer_incentive_tactic_type_code: Optional[ConsumerIncentiveTacticTypeCode] = field(
        default=None,
        metadata={
            "name": "ConsumerIncentiveTacticTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    display_tactic_type_code: Optional[DisplayTacticTypeCode] = field(
        default=None,
        metadata={
            "name": "DisplayTacticTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    feature_tactic_type_code: Optional[FeatureTacticTypeCode] = field(
        default=None,
        metadata={
            "name": "FeatureTacticTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    trade_item_packing_labeling_type_code: Optional[TradeItemPackingLabelingTypeCode] = field(
        default=None,
        metadata={
            "name": "TradeItemPackingLabelingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class EvidenceSuppliedType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class ExternalReferenceType:
    uri: Optional[Uri] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_hash: Optional[DocumentHash] = field(
        default=None,
        metadata={
            "name": "DocumentHash",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hash_algorithm_method: Optional[HashAlgorithmMethod] = field(
        default=None,
        metadata={
            "name": "HashAlgorithmMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    expiry_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    expiry_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ExpiryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    mime_code: Optional[MimeCode] = field(
        default=None,
        metadata={
            "name": "MimeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    format_code: Optional[FormatCode] = field(
        default=None,
        metadata={
            "name": "FormatCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    encoding_code: Optional[EncodingCode] = field(
        default=None,
        metadata={
            "name": "EncodingCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    character_set_code: Optional[CharacterSetCode] = field(
        default=None,
        metadata={
            "name": "CharacterSetCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    file_name: Optional[FileName] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ForecastExceptionCriterionLineType:
    forecast_purpose_code: Optional[ForecastPurposeCode] = field(
        default=None,
        metadata={
            "name": "ForecastPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    comparison_data_source_code: Optional[ComparisonDataSourceCode] = field(
        default=None,
        metadata={
            "name": "ComparisonDataSourceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    data_source_code: Optional[DataSourceCode] = field(
        default=None,
        metadata={
            "name": "DataSourceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    time_delta_days_quantity: Optional[TimeDeltaDaysQuantity] = field(
        default=None,
        metadata={
            "name": "TimeDeltaDaysQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ForecastExceptionType:
    forecast_purpose_code: Optional[ForecastPurposeCode] = field(
        default=None,
        metadata={
            "name": "ForecastPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    data_source_code: Optional[DataSourceCode] = field(
        default=None,
        metadata={
            "name": "DataSourceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    comparison_data_code: Optional[ComparisonDataCode] = field(
        default=None,
        metadata={
            "name": "ComparisonDataCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    comparison_forecast_issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ComparisonForecastIssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    comparison_forecast_issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ComparisonForecastIssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class GoodsItemContainerType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_equipment: List["TransportEquipment"] = field(
        default_factory=list,
        metadata={
            "name": "TransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ItemComparisonType:
    price_amount: Optional[PriceAmount] = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ItemPropertyGroupType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    importance_code: Optional[ImportanceCode] = field(
        default=None,
        metadata={
            "name": "ImportanceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ItemPropertyRangeType:
    minimum_value: Optional[MinimumValue] = field(
        default=None,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_value: Optional[MaximumValue] = field(
        default=None,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class LanguageType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    locale_code: Optional[LocaleCode] = field(
        default=None,
        metadata={
            "name": "LocaleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class LocationCoordinateType:
    coordinate_system_code: Optional[CoordinateSystemCode] = field(
        default=None,
        metadata={
            "name": "CoordinateSystemCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latitude_degrees_measure: Optional[LatitudeDegreesMeasure] = field(
        default=None,
        metadata={
            "name": "LatitudeDegreesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latitude_minutes_measure: Optional[LatitudeMinutesMeasure] = field(
        default=None,
        metadata={
            "name": "LatitudeMinutesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latitude_direction_code: Optional[LatitudeDirectionCode] = field(
        default=None,
        metadata={
            "name": "LatitudeDirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    longitude_degrees_measure: Optional[LongitudeDegreesMeasure] = field(
        default=None,
        metadata={
            "name": "LongitudeDegreesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    longitude_minutes_measure: Optional[LongitudeMinutesMeasure] = field(
        default=None,
        metadata={
            "name": "LongitudeMinutesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    longitude_direction_code: Optional[LongitudeDirectionCode] = field(
        default=None,
        metadata={
            "name": "LongitudeDirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    altitude_measure: Optional[AltitudeMeasure] = field(
        default=None,
        metadata={
            "name": "AltitudeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class MeterPropertyType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name_code: Optional[NameCode] = field(
        default=None,
        metadata={
            "name": "NameCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value_quantity: Optional[ValueQuantity] = field(
        default=None,
        metadata={
            "name": "ValueQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value_qualifier: List[ValueQualifier] = field(
        default_factory=list,
        metadata={
            "name": "ValueQualifier",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class MeterReadingType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    meter_reading_type: Optional[UblCommonBasicComponents21MeterReadingType] = field(
        default=None,
        metadata={
            "name": "MeterReadingType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    meter_reading_type_code: Optional[MeterReadingTypeCode] = field(
        default=None,
        metadata={
            "name": "MeterReadingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    previous_meter_reading_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PreviousMeterReadingDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    previous_meter_quantity: Optional[PreviousMeterQuantity] = field(
        default=None,
        metadata={
            "name": "PreviousMeterQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    latest_meter_reading_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatestMeterReadingDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    latest_meter_quantity: Optional[LatestMeterQuantity] = field(
        default=None,
        metadata={
            "name": "LatestMeterQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    previous_meter_reading_method: Optional[PreviousMeterReadingMethod] = field(
        default=None,
        metadata={
            "name": "PreviousMeterReadingMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    previous_meter_reading_method_code: Optional[PreviousMeterReadingMethodCode] = field(
        default=None,
        metadata={
            "name": "PreviousMeterReadingMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latest_meter_reading_method: Optional[LatestMeterReadingMethod] = field(
        default=None,
        metadata={
            "name": "LatestMeterReadingMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latest_meter_reading_method_code: Optional[LatestMeterReadingMethodCode] = field(
        default=None,
        metadata={
            "name": "LatestMeterReadingMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    meter_reading_comments: List[MeterReadingComments] = field(
        default_factory=list,
        metadata={
            "name": "MeterReadingComments",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    delivered_quantity: Optional[DeliveredQuantity] = field(
        default=None,
        metadata={
            "name": "DeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class MonetaryTotalType:
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_exclusive_amount: Optional[TaxExclusiveAmount] = field(
        default=None,
        metadata={
            "name": "TaxExclusiveAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_inclusive_amount: Optional[TaxInclusiveAmount] = field(
        default=None,
        metadata={
            "name": "TaxInclusiveAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    allowance_total_amount: Optional[AllowanceTotalAmount] = field(
        default=None,
        metadata={
            "name": "AllowanceTotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    charge_total_amount: Optional[ChargeTotalAmount] = field(
        default=None,
        metadata={
            "name": "ChargeTotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    prepaid_amount: Optional[PrepaidAmount] = field(
        default=None,
        metadata={
            "name": "PrepaidAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payable_rounding_amount: Optional[PayableRoundingAmount] = field(
        default=None,
        metadata={
            "name": "PayableRoundingAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payable_amount: Optional[PayableAmount] = field(
        default=None,
        metadata={
            "name": "PayableAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    payable_alternative_amount: Optional[PayableAlternativeAmount] = field(
        default=None,
        metadata={
            "name": "PayableAlternativeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class PartyIdentificationType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class PartyNameType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class PaymentType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    paid_amount: Optional[PaidAmount] = field(
        default=None,
        metadata={
            "name": "PaidAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    received_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    paid_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PaidDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    paid_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "PaidTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    instruction_id: Optional[InstructionId] = field(
        default=None,
        metadata={
            "name": "InstructionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class PeriodType:
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    duration_measure: Optional[DurationMeasure] = field(
        default=None,
        metadata={
            "name": "DurationMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description_code: List[DescriptionCode] = field(
        default_factory=list,
        metadata={
            "name": "DescriptionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class PhysicalAttributeType:
    attribute_id: Optional[AttributeId] = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    position_code: Optional[PositionCode] = field(
        default=None,
        metadata={
            "name": "PositionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description_code: Optional[DescriptionCode] = field(
        default=None,
        metadata={
            "name": "DescriptionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ProcessJustificationType:
    previous_cancellation_reason_code: Optional[PreviousCancellationReasonCode] = field(
        default=None,
        metadata={
            "name": "PreviousCancellationReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    process_reason_code: Optional[ProcessReasonCode] = field(
        default=None,
        metadata={
            "name": "ProcessReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    process_reason: List[ProcessReason] = field(
        default_factory=list,
        metadata={
            "name": "ProcessReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class RailTransportType:
    train_id: Optional[TrainId] = field(
        default=None,
        metadata={
            "name": "TrainID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    rail_car_id: Optional[RailCarId] = field(
        default=None,
        metadata={
            "name": "RailCarID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class RegulationType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    legal_reference: Optional[LegalReference] = field(
        default=None,
        metadata={
            "name": "LegalReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    ontology_uri: Optional[OntologyUri] = field(
        default=None,
        metadata={
            "name": "OntologyURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class RelatedItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ResultOfVerificationType:
    validator_id: Optional[ValidatorId] = field(
        default=None,
        metadata={
            "name": "ValidatorID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validation_result_code: Optional[ValidationResultCode] = field(
        default=None,
        metadata={
            "name": "ValidationResultCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validation_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValidationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validation_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ValidationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validate_process: Optional[ValidateProcess] = field(
        default=None,
        metadata={
            "name": "ValidateProcess",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validate_tool: Optional[ValidateTool] = field(
        default=None,
        metadata={
            "name": "ValidateTool",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validate_tool_version: Optional[ValidateToolVersion] = field(
        default=None,
        metadata={
            "name": "ValidateToolVersion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    signatory_party: Optional["SignatoryParty"] = field(
        default=None,
        metadata={
            "name": "SignatoryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class RoadTransportType:
    license_plate_id: Optional[LicensePlateId] = field(
        default=None,
        metadata={
            "name": "LicensePlateID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class SecondaryHazardType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    placard_notation: Optional[PlacardNotation] = field(
        default=None,
        metadata={
            "name": "PlacardNotation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    placard_endorsement: Optional[PlacardEndorsement] = field(
        default=None,
        metadata={
            "name": "PlacardEndorsement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    emergency_procedures_code: Optional[EmergencyProceduresCode] = field(
        default=None,
        metadata={
            "name": "EmergencyProceduresCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    extension: List[Extension] = field(
        default_factory=list,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class ServiceFrequencyType:
    week_day_code: Optional[WeekDayCode] = field(
        default=None,
        metadata={
            "name": "WeekDayCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class ShareholderPartyType:
    partecipation_percent: Optional[PartecipationPercent] = field(
        default=None,
        metadata={
            "name": "PartecipationPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    party: Optional["Party"] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class SubcontractTermsType:
    rate: Optional[Rate] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    unknown_price_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UnknownPriceIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    subcontracting_conditions_code: Optional[SubcontractingConditionsCode] = field(
        default=None,
        metadata={
            "name": "SubcontractingConditionsCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_percent: Optional[MaximumPercent] = field(
        default=None,
        metadata={
            "name": "MaximumPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_percent: Optional[MinimumPercent] = field(
        default=None,
        metadata={
            "name": "MinimumPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class TemperatureType:
    attribute_id: Optional[AttributeId] = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    measure: Optional[Measure] = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class TransportEquipmentSealType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    seal_issuer_type_code: Optional[SealIssuerTypeCode] = field(
        default=None,
        metadata={
            "name": "SealIssuerTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    condition: Optional[UblCommonBasicComponents21Condition] = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    seal_status_code: Optional[SealStatusCode] = field(
        default=None,
        metadata={
            "name": "SealStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    sealing_party_type: Optional[SealingPartyType] = field(
        default=None,
        metadata={
            "name": "SealingPartyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class UnstructuredPriceType:
    price_amount: Optional[PriceAmount] = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    time_amount: Optional[TimeAmount] = field(
        default=None,
        metadata={
            "name": "TimeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )


@dataclass
class WebSiteAccessType:
    uri: Optional[Uri] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    password: Optional[Password] = field(
        default=None,
        metadata={
            "name": "Password",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    login: Optional[Login] = field(
        default=None,
        metadata={
            "name": "Login",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )


@dataclass
class AccessoryRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ActivityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ActivityProperty(ActivityPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AdditionalCommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AdditionalTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AddressLine(AddressLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AirTransport(AirTransportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AllowedSubcontractTerms(SubcontractTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AnticipatedMonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ApplicablePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ApplicableRegulation(RegulationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AuctionTerms(AuctionTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AwardingCriterion(AwardingCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AwardingCriterionResponse(AwardingCriterionResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CardAccount(CardAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CategorizesClassificationCategory(ClassificationCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ClassificationCategory(ClassificationCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Clause(ClauseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CollectedPayment(PaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Communication(CommunicationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ComplementaryRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ComponentRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Condition(ConditionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConstitutionPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsumptionAverage(ConsumptionAverageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsumptionCorrection(ConsumptionCorrectionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractAcceptancePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractExecutionRequirement(ContractExecutionRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractFormalizationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractingActivity(ContractingActivityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractingPartyType(ContractingPartyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Country(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CreditAccount(CreditAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DefaultLanguage(LanguageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeletedCatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeliveryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeliveryUnit(DeliveryUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DestinationCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Dimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DocumentAvailabilityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DurationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EconomicOperatorRole(EconomicOperatorRoleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EffectivePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EmergencyTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EnergyWaterConsumptionCorrection(ConsumptionCorrectionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EstimatedDeliveryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EstimatedDespatchPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EstimatedDurationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EstimatedTransitPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EventComment(EventCommentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EventTacticEnumeration(EventTacticEnumerationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EvidenceSupplied(EvidenceSuppliedType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExceptionObservationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExportCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExternalReference(ExternalReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinalDestinationCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FlashpointTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FloorSpaceMeasurementDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ForecastException(ForecastExceptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ForecastExceptionCriterionLine(ForecastExceptionCriterionLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ForecastPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FrequencyPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class GoodsItemContainer(GoodsItemContainerType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InventoryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InvitationSubmissionPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InvoicePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class IssuingCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemComparison(ItemComparisonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemPropertyGroup(ItemPropertyGroupType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemPropertyRange(ItemPropertyRangeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Language(LanguageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LegalMonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LineValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LocationCoordinate(LocationCoordinateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MainCommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MainPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MaximumDeliveryUnit(DeliveryUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MaximumTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MeasurementDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MeterProperty(MeterPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MeterReading(MeterReadingType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MinimumDeliveryUnit(DeliveryUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MinimumTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class NominationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class NotificationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OptionValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginalDepartureCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OtherCommunication(CommunicationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PalletSpaceMeasurementDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ParticipationRequestReceptionPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PartyIdentification(PartyIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PartyName(PartyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Payment(PaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PaymentReversalPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PenaltyClause(ClauseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PenaltyPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Period(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PhysicalAttribute(PhysicalAttributeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PlannedPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PrepaidPayment(PaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PresentationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ProcessJustification(ProcessJustificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PromisedDeliveryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class QuotedMonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RailTransport(RailTransportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RangeDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Regulation(RegulationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RelatedCatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReminderPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReplacedRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReplacementRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedCatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedDeliveryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedDespatchPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedLanguage(LanguageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedMonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedStatusPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequiredRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ResultOfVerification(ResultOfVerificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RoadTransport(RoadTransportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ScheduledServiceFrequency(ServiceFrequencyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SecondaryHazard(SecondaryHazardType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ServiceEndTimePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ServiceFrequency(ServiceFrequencyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ServiceStartTimePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SettlementPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ShareholderParty(ShareholderPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SourceCatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class StatementPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class StatusPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubcontractTerms(SubcontractTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubordinateAwardingCriterion(AwardingCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubordinateAwardingCriterionResponse(AwardingCriterionResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SupportedCommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Temperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderSubmissionDeadlinePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TotalCapacityDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransitCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransitPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportEquipmentSeal(TransportEquipmentSealType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportServiceProviderResponseDeadlinePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportServiceProviderResponseRequiredPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportUserResponseRequiredPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UnstructuredPrice(UnstructuredPriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UnsupportedCommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UsabilityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class WarrantyValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class WebSiteAccess(WebSiteAccessType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AddressType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    address_type_code: Optional[AddressTypeCode] = field(
        default=None,
        metadata={
            "name": "AddressTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    address_format_code: Optional[AddressFormatCode] = field(
        default=None,
        metadata={
            "name": "AddressFormatCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    postbox: Optional[Postbox] = field(
        default=None,
        metadata={
            "name": "Postbox",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    floor: Optional[Floor] = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    room: Optional[Room] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    street_name: Optional[StreetName] = field(
        default=None,
        metadata={
            "name": "StreetName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    additional_street_name: Optional[AdditionalStreetName] = field(
        default=None,
        metadata={
            "name": "AdditionalStreetName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    block_name: Optional[BlockName] = field(
        default=None,
        metadata={
            "name": "BlockName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    building_name: Optional[BuildingName] = field(
        default=None,
        metadata={
            "name": "BuildingName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    building_number: Optional[BuildingNumber] = field(
        default=None,
        metadata={
            "name": "BuildingNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    inhouse_mail: Optional[InhouseMail] = field(
        default=None,
        metadata={
            "name": "InhouseMail",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    department: Optional[Department] = field(
        default=None,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    mark_attention: Optional[MarkAttention] = field(
        default=None,
        metadata={
            "name": "MarkAttention",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    mark_care: Optional[MarkCare] = field(
        default=None,
        metadata={
            "name": "MarkCare",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    plot_identification: Optional[PlotIdentification] = field(
        default=None,
        metadata={
            "name": "PlotIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    city_subdivision_name: Optional[CitySubdivisionName] = field(
        default=None,
        metadata={
            "name": "CitySubdivisionName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    city_name: Optional[CityName] = field(
        default=None,
        metadata={
            "name": "CityName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    postal_zone: Optional[PostalZone] = field(
        default=None,
        metadata={
            "name": "PostalZone",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    country_subentity: Optional[CountrySubentity] = field(
        default=None,
        metadata={
            "name": "CountrySubentity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    country_subentity_code: Optional[CountrySubentityCode] = field(
        default=None,
        metadata={
            "name": "CountrySubentityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    region: Optional[Region] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    district: Optional[District] = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    timezone_offset: Optional[TimezoneOffset] = field(
        default=None,
        metadata={
            "name": "TimezoneOffset",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    address_line: List[AddressLine] = field(
        default_factory=list,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    location_coordinate: List[LocationCoordinate] = field(
        default_factory=list,
        metadata={
            "name": "LocationCoordinate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AttachmentType:
    embedded_document_binary_object: Optional[EmbeddedDocumentBinaryObject] = field(
        default=None,
        metadata={
            "name": "EmbeddedDocumentBinaryObject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    external_reference: Optional[ExternalReference] = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CapabilityType:
    capability_type_code: Optional[CapabilityTypeCode] = field(
        default=None,
        metadata={
            "name": "CapabilityTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value_amount: Optional[ValueAmount] = field(
        default=None,
        metadata={
            "name": "ValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value_quantity: Optional[ValueQuantity] = field(
        default=None,
        metadata={
            "name": "ValueQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    evidence_supplied: List[EvidenceSupplied] = field(
        default_factory=list,
        metadata={
            "name": "EvidenceSupplied",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ClassificationSchemeType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    last_revision_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LastRevisionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    last_revision_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LastRevisionTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    agency_id: Optional[AgencyId] = field(
        default=None,
        metadata={
            "name": "AgencyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    agency_name: Optional[AgencyName] = field(
        default=None,
        metadata={
            "name": "AgencyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    version_id: Optional[VersionId] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uri: Optional[Uri] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    scheme_uri: Optional[SchemeUri] = field(
        default=None,
        metadata={
            "name": "SchemeURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    language_id: Optional[LanguageId] = field(
        default=None,
        metadata={
            "name": "LanguageID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    classification_category: List[ClassificationCategory] = field(
        default_factory=list,
        metadata={
            "name": "ClassificationCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class ConsumptionHistoryType:
    meter_number: Optional[MeterNumber] = field(
        default=None,
        metadata={
            "name": "MeterNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumption_level_code: Optional[ConsumptionLevelCode] = field(
        default=None,
        metadata={
            "name": "ConsumptionLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumption_level: Optional[ConsumptionLevel] = field(
        default=None,
        metadata={
            "name": "ConsumptionLevel",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class ConsumptionReportReferenceType:
    consumption_report_id: Optional[ConsumptionReportId] = field(
        default=None,
        metadata={
            "name": "ConsumptionReportID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    consumption_type: Optional[UblCommonBasicComponents21ConsumptionType] = field(
        default=None,
        metadata={
            "name": "ConsumptionType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumption_type_code: Optional[ConsumptionTypeCode] = field(
        default=None,
        metadata={
            "name": "ConsumptionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_consumed_quantity: Optional[TotalConsumedQuantity] = field(
        default=None,
        metadata={
            "name": "TotalConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class ContactType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    telephone: Optional[Telephone] = field(
        default=None,
        metadata={
            "name": "Telephone",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    telefax: Optional[Telefax] = field(
        default=None,
        metadata={
            "name": "Telefax",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    electronic_mail: Optional[ElectronicMail] = field(
        default=None,
        metadata={
            "name": "ElectronicMail",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    other_communication: List[OtherCommunication] = field(
        default_factory=list,
        metadata={
            "name": "OtherCommunication",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class DeclarationType:
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declaration_type_code: Optional[DeclarationTypeCode] = field(
        default=None,
        metadata={
            "name": "DeclarationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    evidence_supplied: List[EvidenceSupplied] = field(
        default_factory=list,
        metadata={
            "name": "EvidenceSupplied",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EventTacticType:
    comment: Optional[Comment] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    event_tactic_enumeration: Optional[EventTacticEnumeration] = field(
        default=None,
        metadata={
            "name": "EventTacticEnumeration",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class FinancialGuaranteeType:
    guarantee_type_code: Optional[GuaranteeTypeCode] = field(
        default=None,
        metadata={
            "name": "GuaranteeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    liability_amount: Optional[LiabilityAmount] = field(
        default=None,
        metadata={
            "name": "LiabilityAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    amount_rate: Optional[AmountRate] = field(
        default=None,
        metadata={
            "name": "AmountRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    constitution_period: Optional[ConstitutionPeriod] = field(
        default=None,
        metadata={
            "name": "ConstitutionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class HazardousGoodsTransitType:
    transport_emergency_card_code: Optional[TransportEmergencyCardCode] = field(
        default=None,
        metadata={
            "name": "TransportEmergencyCardCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    packing_criteria_code: Optional[PackingCriteriaCode] = field(
        default=None,
        metadata={
            "name": "PackingCriteriaCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hazardous_regulation_code: Optional[HazardousRegulationCode] = field(
        default=None,
        metadata={
            "name": "HazardousRegulationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    inhalation_toxicity_zone_code: Optional[InhalationToxicityZoneCode] = field(
        default=None,
        metadata={
            "name": "InhalationToxicityZoneCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_authorization_code: Optional[TransportAuthorizationCode] = field(
        default=None,
        metadata={
            "name": "TransportAuthorizationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_temperature: Optional[MaximumTemperature] = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    minimum_temperature: Optional[MinimumTemperature] = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ItemPropertyType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    name_code: Optional[NameCode] = field(
        default=None,
        metadata={
            "name": "NameCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    test_method: Optional[TestMethod] = field(
        default=None,
        metadata={
            "name": "TestMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value_quantity: Optional[ValueQuantity] = field(
        default=None,
        metadata={
            "name": "ValueQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value_qualifier: List[ValueQualifier] = field(
        default_factory=list,
        metadata={
            "name": "ValueQualifier",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    importance_code: Optional[ImportanceCode] = field(
        default=None,
        metadata={
            "name": "ImportanceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    list_value: List[ListValue] = field(
        default_factory=list,
        metadata={
            "name": "ListValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    usability_period: Optional[UsabilityPeriod] = field(
        default=None,
        metadata={
            "name": "UsabilityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item_property_group: List[ItemPropertyGroup] = field(
        default_factory=list,
        metadata={
            "name": "ItemPropertyGroup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    range_dimension: Optional[RangeDimension] = field(
        default=None,
        metadata={
            "name": "RangeDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item_property_range: Optional[ItemPropertyRange] = field(
        default=None,
        metadata={
            "name": "ItemPropertyRange",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class MeterType:
    meter_number: Optional[MeterNumber] = field(
        default=None,
        metadata={
            "name": "MeterNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    meter_name: Optional[MeterName] = field(
        default=None,
        metadata={
            "name": "MeterName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    meter_constant: Optional[MeterConstant] = field(
        default=None,
        metadata={
            "name": "MeterConstant",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    meter_constant_code: Optional[MeterConstantCode] = field(
        default=None,
        metadata={
            "name": "MeterConstantCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_delivered_quantity: Optional[TotalDeliveredQuantity] = field(
        default=None,
        metadata={
            "name": "TotalDeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    meter_reading: List[MeterReading] = field(
        default_factory=list,
        metadata={
            "name": "MeterReading",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    meter_property: List[MeterProperty] = field(
        default_factory=list,
        metadata={
            "name": "MeterProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PaymentTermsType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_means_id: List[PaymentMeansId] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMeansID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    prepaid_payment_reference_id: Optional[PrepaidPaymentReferenceId] = field(
        default=None,
        metadata={
            "name": "PrepaidPaymentReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reference_event_code: Optional[ReferenceEventCode] = field(
        default=None,
        metadata={
            "name": "ReferenceEventCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    settlement_discount_percent: Optional[SettlementDiscountPercent] = field(
        default=None,
        metadata={
            "name": "SettlementDiscountPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    penalty_surcharge_percent: Optional[PenaltySurchargePercent] = field(
        default=None,
        metadata={
            "name": "PenaltySurchargePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_percent: Optional[PaymentPercent] = field(
        default=None,
        metadata={
            "name": "PaymentPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    settlement_discount_amount: Optional[SettlementDiscountAmount] = field(
        default=None,
        metadata={
            "name": "SettlementDiscountAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    penalty_amount: Optional[PenaltyAmount] = field(
        default=None,
        metadata={
            "name": "PenaltyAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_terms_details_uri: Optional[PaymentTermsDetailsUri] = field(
        default=None,
        metadata={
            "name": "PaymentTermsDetailsURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_due_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PaymentDueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    installment_due_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "InstallmentDueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    invoicing_party_reference: Optional[InvoicingPartyReference] = field(
        default=None,
        metadata={
            "name": "InvoicingPartyReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    settlement_period: Optional[SettlementPeriod] = field(
        default=None,
        metadata={
            "name": "SettlementPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    penalty_period: Optional[PenaltyPeriod] = field(
        default=None,
        metadata={
            "name": "PenaltyPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    exchange_rate: Optional["ExchangeRate"] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PriceListType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    status_code: Optional[StatusCode] = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validity_period: List[ValidityPeriod] = field(
        default_factory=list,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    previous_price_list: Optional["PreviousPriceList"] = field(
        default=None,
        metadata={
            "name": "PreviousPriceList",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class RenewalType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class RetailPlannedImpactType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    forecast_purpose_code: Optional[ForecastPurposeCode] = field(
        default=None,
        metadata={
            "name": "ForecastPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class StatusType:
    condition_code: Optional[ConditionCode] = field(
        default=None,
        metadata={
            "name": "ConditionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reference_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReferenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reference_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ReferenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    status_reason_code: Optional[StatusReasonCode] = field(
        default=None,
        metadata={
            "name": "StatusReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    status_reason: List[StatusReason] = field(
        default_factory=list,
        metadata={
            "name": "StatusReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    sequence_id: Optional[SequenceId] = field(
        default=None,
        metadata={
            "name": "SequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    text: List[Text] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    indication_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IndicationIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reliability_percent: Optional[ReliabilityPercent] = field(
        default=None,
        metadata={
            "name": "ReliabilityPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    condition: List[Condition] = field(
        default_factory=list,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class StowageType:
    location_id: Optional[LocationId] = field(
        default=None,
        metadata={
            "name": "LocationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    location: List[UblCommonBasicComponents21Location] = field(
        default_factory=list,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    measurement_dimension: List[MeasurementDimension] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AccountingContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AdditionalItemProperty(ItemPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Address(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ApplicableAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ApplicableTerritoryAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Attachment(AttachmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BonusPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BusinessClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BuyerContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Capability(CapabilityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CollectPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CommissionPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsumptionHistory(ConsumptionHistoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsumptionReportReference(ConsumptionReportReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Contact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CurrentStatus(StatusType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Declaration(DeclarationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeliveryAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeliveryContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DespatchAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DespatchContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DigitalSignatureAttachment(AttachmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DisbursementPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EventTactic(EventTacticType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinalFinancialGuarantee(FinancialGuaranteeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinancialCapability(CapabilityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinancialGuarantee(FinancialGuaranteeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class HazardousGoodsTransit(HazardousGoodsTransitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemProperty(ItemPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class JurisdictionRegionAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class KeywordItemProperty(ItemPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LocationAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Meter(MeterType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PenaltyPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PostalAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PrepaidPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PreviousPriceList(PriceListType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PriceList(PriceListType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RegistrationAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Renewal(RenewalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequiredBusinessClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequiredClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequiredFinancialGuarantee(FinancialGuaranteeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ResidenceAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RetailPlannedImpact(RetailPlannedImpactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReturnAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SellerContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ServiceChargePaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SignatoryContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Status(StatusType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Stowage(StowageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TechnicalCapability(CapabilityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UtilityMeter(MeterType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BudgetAccountType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    budget_year_numeric: Optional[BudgetYearNumeric] = field(
        default=None,
        metadata={
            "name": "BudgetYearNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    required_classification_scheme: Optional[RequiredClassificationScheme] = field(
        default=None,
        metadata={
            "name": "RequiredClassificationScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ConsumptionPointType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    subscriber_id: Optional[SubscriberId] = field(
        default=None,
        metadata={
            "name": "SubscriberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    subscriber_type: Optional[SubscriberType] = field(
        default=None,
        metadata={
            "name": "SubscriberType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    subscriber_type_code: Optional[SubscriberTypeCode] = field(
        default=None,
        metadata={
            "name": "SubscriberTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_delivered_quantity: Optional[TotalDeliveredQuantity] = field(
        default=None,
        metadata={
            "name": "TotalDeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    web_site_access: Optional[WebSiteAccess] = field(
        default=None,
        metadata={
            "name": "WebSiteAccess",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    utility_meter: List[UtilityMeter] = field(
        default_factory=list,
        metadata={
            "name": "UtilityMeter",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ContractExtensionType:
    options_description: List[OptionsDescription] = field(
        default_factory=list,
        metadata={
            "name": "OptionsDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_number_numeric: Optional[MinimumNumberNumeric] = field(
        default=None,
        metadata={
            "name": "MinimumNumberNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_number_numeric: Optional[MaximumNumberNumeric] = field(
        default=None,
        metadata={
            "name": "MaximumNumberNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    option_validity_period: Optional[OptionValidityPeriod] = field(
        default=None,
        metadata={
            "name": "OptionValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    renewal: List[Renewal] = field(
        default_factory=list,
        metadata={
            "name": "Renewal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CorporateRegistrationSchemeType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    corporate_registration_type_code: Optional[CorporateRegistrationTypeCode] = field(
        default=None,
        metadata={
            "name": "CorporateRegistrationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    jurisdiction_region_address: List[JurisdictionRegionAddress] = field(
        default_factory=list,
        metadata={
            "name": "JurisdictionRegionAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class DocumentReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    copy_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_type_code: Optional[DocumentTypeCode] = field(
        default=None,
        metadata={
            "name": "DocumentTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_type: Optional[DocumentType] = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    xpath: List[Xpath] = field(
        default_factory=list,
        metadata={
            "name": "XPath",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    language_id: Optional[LanguageId] = field(
        default=None,
        metadata={
            "name": "LanguageID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    locale_code: Optional[LocaleCode] = field(
        default=None,
        metadata={
            "name": "LocaleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    version_id: Optional[VersionId] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_status_code: Optional[DocumentStatusCode] = field(
        default=None,
        metadata={
            "name": "DocumentStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_description: List[DocumentDescription] = field(
        default_factory=list,
        metadata={
            "name": "DocumentDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    attachment: Optional[Attachment] = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    issuer_party: Optional["IssuerParty"] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    result_of_verification: Optional[ResultOfVerification] = field(
        default=None,
        metadata={
            "name": "ResultOfVerification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class FinancialInstitutionType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class LocationType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    conditions: List[Conditions] = field(
        default_factory=list,
        metadata={
            "name": "Conditions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    country_subentity: Optional[CountrySubentity] = field(
        default=None,
        metadata={
            "name": "CountrySubentity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    country_subentity_code: Optional[CountrySubentityCode] = field(
        default=None,
        metadata={
            "name": "CountrySubentityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    location_type_code: Optional[LocationTypeCode] = field(
        default=None,
        metadata={
            "name": "LocationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    information_uri: Optional[InformationUri] = field(
        default=None,
        metadata={
            "name": "InformationURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validity_period: List[ValidityPeriod] = field(
        default_factory=list,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    subsidiary_location: List["SubsidiaryLocation"] = field(
        default_factory=list,
        metadata={
            "name": "SubsidiaryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    location_coordinate: List[LocationCoordinate] = field(
        default_factory=list,
        metadata={
            "name": "LocationCoordinate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class LotIdentificationType:
    lot_number_id: Optional[LotNumberId] = field(
        default=None,
        metadata={
            "name": "LotNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    expiry_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    additional_item_property: List[AdditionalItemProperty] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalItemProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class OnAccountPaymentType:
    estimated_consumed_quantity: Optional[EstimatedConsumedQuantity] = field(
        default=None,
        metadata={
            "name": "EstimatedConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_terms: List[PaymentTerms] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class ResponseType:
    reference_id: Optional[ReferenceId] = field(
        default=None,
        metadata={
            "name": "ReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    response_code: Optional[ResponseCode] = field(
        default=None,
        metadata={
            "name": "ResponseCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    effective_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    effective_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EffectiveTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    status: List[Status] = field(
        default_factory=list,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ServiceProviderPartyType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    service_type_code: Optional[ServiceTypeCode] = field(
        default=None,
        metadata={
            "name": "ServiceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    service_type: List[ServiceType] = field(
        default_factory=list,
        metadata={
            "name": "ServiceType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    party: Optional["Party"] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    seller_contact: Optional[SellerContact] = field(
        default=None,
        metadata={
            "name": "SellerContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TaxSchemeType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_type_code: Optional[TaxTypeCode] = field(
        default=None,
        metadata={
            "name": "TaxTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    currency_code: Optional[CurrencyCode] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    jurisdiction_region_address: List[JurisdictionRegionAddress] = field(
        default_factory=list,
        metadata={
            "name": "JurisdictionRegionAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TradingTermsType:
    information: List[Information] = field(
        default_factory=list,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    applicable_address: Optional[ApplicableAddress] = field(
        default=None,
        metadata={
            "name": "ApplicableAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ActivityFinalLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ActivityOriginLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AdditionalDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AlternativeDeliveryLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AtLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BudgetAccount(BudgetAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CallForTendersDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CatalogueDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsumptionPoint(ConsumptionPointType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractExtension(ContractExtensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractualDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CorporateRegistrationScheme(CorporateRegistrationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CreditNoteDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DebitNoteDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeliveryLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DespatchDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DespatchLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DiscrepancyResponse(ResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EmploymentLegislationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EnvironmentalLegislationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EvidenceDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinancialInstitution(FinancialInstitutionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FirstArrivalPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FiscalLegislationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FreightChargeLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FromLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class GuaranteeDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class GuidanceDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class HaulageTradingTerms(TradingTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class IdentityDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InventoryLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InvoiceDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemSpecificationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LastExitPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LegalDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LoadingLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LoadingPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Location(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LotIdentification(LotIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MainOnAccountPayment(OnAccountPaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MandateDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MeasurementFromLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MeasurementToLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MinutesDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class NoticeDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class NotificationLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OccurenceLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OnAccountPayment(OnAccountPaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OrderDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginalDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginatorDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ParentDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ParticipatingLocationsLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PhysicalLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PickupLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PreviousDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ProcurementLegislationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class QuotationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RealizedLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReceiptDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RegistryCertificateDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RegistryPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReminderDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReplacedNoticeDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestForQuotationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedStatusLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ResolutionDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Response(ResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SelfBilledCreditNoteDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SelfBilledInvoiceDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ServiceProviderParty(ServiceProviderPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ShipmentDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class StatementDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class StatusLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class StorageLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubsidiaryLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SupportingDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TaxScheme(TaxSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TechnicalDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TemplateDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TendererQualificationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ToLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TradingTerms(TradingTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportExecutionPlanDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportExecutionPlanRequestDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportProgressStatusRequestDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportServiceDescriptionDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportServiceDescriptionRequestDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportationStatusRequestDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransshipPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UnloadingLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UnloadingPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UtilityConsumptionPoint(ConsumptionPointType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class WorkOrderDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BranchType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    financial_institution: Optional[FinancialInstitution] = field(
        default=None,
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class BudgetAccountLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_amount: Optional[TotalAmount] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    budget_account: List[BudgetAccount] = field(
        default_factory=list,
        metadata={
            "name": "BudgetAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ConsumptionReportType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    consumption_type: Optional[UblCommonBasicComponents21ConsumptionType] = field(
        default=None,
        metadata={
            "name": "ConsumptionType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumption_type_code: Optional[ConsumptionTypeCode] = field(
        default=None,
        metadata={
            "name": "ConsumptionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_consumed_quantity: Optional[TotalConsumedQuantity] = field(
        default=None,
        metadata={
            "name": "TotalConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    basic_consumed_quantity: Optional[BasicConsumedQuantity] = field(
        default=None,
        metadata={
            "name": "BasicConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    resident_occupants_numeric: Optional[ResidentOccupantsNumeric] = field(
        default=None,
        metadata={
            "name": "ResidentOccupantsNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumers_energy_level_code: Optional[ConsumersEnergyLevelCode] = field(
        default=None,
        metadata={
            "name": "ConsumersEnergyLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumers_energy_level: Optional[ConsumersEnergyLevel] = field(
        default=None,
        metadata={
            "name": "ConsumersEnergyLevel",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    residence_type: Optional[ResidenceType] = field(
        default=None,
        metadata={
            "name": "ResidenceType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    residence_type_code: Optional[ResidenceTypeCode] = field(
        default=None,
        metadata={
            "name": "ResidenceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    heating_type: Optional[HeatingType] = field(
        default=None,
        metadata={
            "name": "HeatingType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    heating_type_code: Optional[HeatingTypeCode] = field(
        default=None,
        metadata={
            "name": "HeatingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    guidance_document_reference: Optional[GuidanceDocumentReference] = field(
        default=None,
        metadata={
            "name": "GuidanceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: Optional[DocumentReference] = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    consumption_report_reference: List[ConsumptionReportReference] = field(
        default_factory=list,
        metadata={
            "name": "ConsumptionReportReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    consumption_history: List[ConsumptionHistory] = field(
        default_factory=list,
        metadata={
            "name": "ConsumptionHistory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EmissionCalculationMethodType:
    calculation_method_code: Optional[CalculationMethodCode] = field(
        default=None,
        metadata={
            "name": "CalculationMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    fullness_indication_code: Optional[FullnessIndicationCode] = field(
        default=None,
        metadata={
            "name": "FullnessIndicationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    measurement_from_location: Optional[MeasurementFromLocation] = field(
        default=None,
        metadata={
            "name": "MeasurementFromLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    measurement_to_location: Optional[MeasurementToLocation] = field(
        default=None,
        metadata={
            "name": "MeasurementToLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EnergyTaxReportType:
    tax_energy_amount: Optional[TaxEnergyAmount] = field(
        default=None,
        metadata={
            "name": "TaxEnergyAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_energy_on_account_amount: Optional[TaxEnergyOnAccountAmount] = field(
        default=None,
        metadata={
            "name": "TaxEnergyOnAccountAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_energy_balance_amount: Optional[TaxEnergyBalanceAmount] = field(
        default=None,
        metadata={
            "name": "TaxEnergyBalanceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_scheme: Optional[TaxScheme] = field(
        default=None,
        metadata={
            "name": "TaxScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class EventType:
    identification_id: Optional[IdentificationId] = field(
        default=None,
        metadata={
            "name": "IdentificationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    occurrence_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OccurrenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    occurrence_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "OccurrenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    type_code: Optional[TypeCode] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    completion_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CompletionIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    current_status: List[CurrentStatus] = field(
        default_factory=list,
        metadata={
            "name": "CurrentStatus",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contact: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    occurence_location: Optional[OccurenceLocation] = field(
        default=None,
        metadata={
            "name": "OccurenceLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ItemInstanceType:
    product_trace_id: Optional[ProductTraceId] = field(
        default=None,
        metadata={
            "name": "ProductTraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    manufacture_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ManufactureDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    manufacture_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ManufactureTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    best_before_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BestBeforeDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    registration_id: Optional[RegistrationId] = field(
        default=None,
        metadata={
            "name": "RegistrationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    serial_id: Optional[SerialId] = field(
        default=None,
        metadata={
            "name": "SerialID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    additional_item_property: List[AdditionalItemProperty] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalItemProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    lot_identification: Optional[LotIdentification] = field(
        default=None,
        metadata={
            "name": "LotIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class LineReferenceType:
    line_id: Optional[LineId] = field(
        default=None,
        metadata={
            "name": "LineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_status_code: Optional[LineStatusCode] = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_reference: Optional[DocumentReference] = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class MaritimeTransportType:
    vessel_id: Optional[VesselId] = field(
        default=None,
        metadata={
            "name": "VesselID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    vessel_name: Optional[VesselName] = field(
        default=None,
        metadata={
            "name": "VesselName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    radio_call_sign_id: Optional[RadioCallSignId] = field(
        default=None,
        metadata={
            "name": "RadioCallSignID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    ships_requirements: List[ShipsRequirements] = field(
        default_factory=list,
        metadata={
            "name": "ShipsRequirements",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gross_tonnage_measure: Optional[GrossTonnageMeasure] = field(
        default=None,
        metadata={
            "name": "GrossTonnageMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_tonnage_measure: Optional[NetTonnageMeasure] = field(
        default=None,
        metadata={
            "name": "NetTonnageMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    registry_certificate_document_reference: Optional[RegistryCertificateDocumentReference] = field(
        default=None,
        metadata={
            "name": "RegistryCertificateDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    registry_port_location: Optional[RegistryPortLocation] = field(
        default=None,
        metadata={
            "name": "RegistryPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class OrderReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    sales_order_id: Optional[SalesOrderId] = field(
        default=None,
        metadata={
            "name": "SalesOrderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    copy_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    customer_reference: Optional[CustomerReference] = field(
        default=None,
        metadata={
            "name": "CustomerReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    order_type_code: Optional[OrderTypeCode] = field(
        default=None,
        metadata={
            "name": "OrderTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_reference: Optional[DocumentReference] = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PartyLegalEntityType:
    registration_name: Optional[RegistrationName] = field(
        default=None,
        metadata={
            "name": "RegistrationName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    company_id: Optional[CompanyId] = field(
        default=None,
        metadata={
            "name": "CompanyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    registration_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegistrationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    registration_expiration_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegistrationExpirationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    company_legal_form_code: Optional[CompanyLegalFormCode] = field(
        default=None,
        metadata={
            "name": "CompanyLegalFormCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    company_legal_form: Optional[CompanyLegalForm] = field(
        default=None,
        metadata={
            "name": "CompanyLegalForm",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    sole_proprietorship_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SoleProprietorshipIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    company_liquidation_status_code: Optional[CompanyLiquidationStatusCode] = field(
        default=None,
        metadata={
            "name": "CompanyLiquidationStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    corporate_stock_amount: Optional[CorporateStockAmount] = field(
        default=None,
        metadata={
            "name": "CorporateStockAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    fully_paid_shares_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FullyPaidSharesIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    registration_address: Optional[RegistrationAddress] = field(
        default=None,
        metadata={
            "name": "RegistrationAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    corporate_registration_scheme: Optional[CorporateRegistrationScheme] = field(
        default=None,
        metadata={
            "name": "CorporateRegistrationScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    head_office_party: Optional["HeadOfficeParty"] = field(
        default=None,
        metadata={
            "name": "HeadOfficeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shareholder_party: List[ShareholderParty] = field(
        default_factory=list,
        metadata={
            "name": "ShareholderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PartyTaxSchemeType:
    registration_name: Optional[RegistrationName] = field(
        default=None,
        metadata={
            "name": "RegistrationName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    company_id: Optional[CompanyId] = field(
        default=None,
        metadata={
            "name": "CompanyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_level_code: Optional[TaxLevelCode] = field(
        default=None,
        metadata={
            "name": "TaxLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    exemption_reason_code: Optional[ExemptionReasonCode] = field(
        default=None,
        metadata={
            "name": "ExemptionReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    exemption_reason: List[ExemptionReason] = field(
        default_factory=list,
        metadata={
            "name": "ExemptionReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    registration_address: Optional[RegistrationAddress] = field(
        default=None,
        metadata={
            "name": "RegistrationAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_scheme: Optional[TaxScheme] = field(
        default=None,
        metadata={
            "name": "TaxScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class PowerOfAttorneyType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    notary_party: Optional["NotaryParty"] = field(
        default=None,
        metadata={
            "name": "NotaryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    agent_party: Optional["AgentParty"] = field(
        default=None,
        metadata={
            "name": "AgentParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    witness_party: List["WitnessParty"] = field(
        default_factory=list,
        metadata={
            "name": "WitnessParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    mandate_document_reference: List[MandateDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "MandateDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TaxCategoryType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    base_unit_measure: Optional[BaseUnitMeasure] = field(
        default=None,
        metadata={
            "name": "BaseUnitMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    per_unit_amount: Optional[PerUnitAmount] = field(
        default=None,
        metadata={
            "name": "PerUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_exemption_reason_code: Optional[TaxExemptionReasonCode] = field(
        default=None,
        metadata={
            "name": "TaxExemptionReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_exemption_reason: List[TaxExemptionReason] = field(
        default_factory=list,
        metadata={
            "name": "TaxExemptionReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tier_range: Optional[TierRange] = field(
        default=None,
        metadata={
            "name": "TierRange",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tier_rate_percent: Optional[TierRatePercent] = field(
        default=None,
        metadata={
            "name": "TierRatePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_scheme: Optional[TaxScheme] = field(
        default=None,
        metadata={
            "name": "TaxScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class TenderRequirementType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    template_document_reference: Optional[TemplateDocumentReference] = field(
        default=None,
        metadata={
            "name": "TemplateDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TransactionConditionsType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    action_code: Optional[ActionCode] = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class WorkPhaseReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    work_phase_code: Optional[WorkPhaseCode] = field(
        default=None,
        metadata={
            "name": "WorkPhaseCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    work_phase: List[WorkPhase] = field(
        default_factory=list,
        metadata={
            "name": "WorkPhase",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    progress_percent: Optional[ProgressPercent] = field(
        default=None,
        metadata={
            "name": "ProgressPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    work_order_document_reference: List[WorkOrderDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "WorkOrderDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ApplicableTaxCategory(TaxCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Branch(BranchType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BudgetAccountLine(BudgetAccountLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CallForTendersLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CatalogueLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ClassifiedTaxCategory(TaxCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsumptionReport(ConsumptionReportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DependentLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DespatchLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DocumentTenderRequirement(TenderRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EmissionCalculationMethod(EmissionCalculationMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EnergyTaxReport(EnergyTaxReportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Event(EventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinancialInstitutionBranch(BranchType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemInstance(ItemInstanceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MaritimeTransport(MaritimeTransportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OpenTenderEvent(EventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OrderReference(OrderReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ParentDocumentLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PartyLegalEntity(PartyLegalEntityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PartyTaxScheme(PartyTaxSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PowerOfAttorney(PowerOfAttorneyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class QuotationLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReceiptLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubsequentProcessTenderRequirement(TenderRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TaxCategory(TaxCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderRequirement(TenderRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransactionConditions(TransactionConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class WorkPhaseReference(WorkPhaseReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DependentPriceReferenceType:
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    location_address: Optional[LocationAddress] = field(
        default=None,
        metadata={
            "name": "LocationAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    dependent_line_reference: Optional[DependentLineReference] = field(
        default=None,
        metadata={
            "name": "DependentLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class DutyType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    duty: Optional[UblCommonBasicComponents21Duty] = field(
        default=None,
        metadata={
            "name": "Duty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    duty_code: Optional[DutyCode] = field(
        default=None,
        metadata={
            "name": "DutyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_category: Optional[TaxCategory] = field(
        default=None,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EnergyWaterSupplyType:
    consumption_report: List[ConsumptionReport] = field(
        default_factory=list,
        metadata={
            "name": "ConsumptionReport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    energy_tax_report: List[EnergyTaxReport] = field(
        default_factory=list,
        metadata={
            "name": "EnergyTaxReport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    consumption_average: List[ConsumptionAverage] = field(
        default_factory=list,
        metadata={
            "name": "ConsumptionAverage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    energy_water_consumption_correction: List[EnergyWaterConsumptionCorrection] = field(
        default_factory=list,
        metadata={
            "name": "EnergyWaterConsumptionCorrection",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EnvironmentalEmissionType:
    environmental_emission_type_code: Optional[EnvironmentalEmissionTypeCode] = field(
        default=None,
        metadata={
            "name": "EnvironmentalEmissionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    value_measure: Optional[ValueMeasure] = field(
        default=None,
        metadata={
            "name": "ValueMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    emission_calculation_method: List[EmissionCalculationMethod] = field(
        default_factory=list,
        metadata={
            "name": "EmissionCalculationMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class FinancialAccountType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    alias_name: Optional[AliasName] = field(
        default=None,
        metadata={
            "name": "AliasName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    account_type_code: Optional[AccountTypeCode] = field(
        default=None,
        metadata={
            "name": "AccountTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    account_format_code: Optional[AccountFormatCode] = field(
        default=None,
        metadata={
            "name": "AccountFormatCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    currency_code: Optional[CurrencyCode] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_note: List[PaymentNote] = field(
        default_factory=list,
        metadata={
            "name": "PaymentNote",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    financial_institution_branch: Optional[FinancialInstitutionBranch] = field(
        default=None,
        metadata={
            "name": "FinancialInstitutionBranch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class FrameworkAgreementType:
    expected_operator_quantity: Optional[ExpectedOperatorQuantity] = field(
        default=None,
        metadata={
            "name": "ExpectedOperatorQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_operator_quantity: Optional[MaximumOperatorQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumOperatorQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    justification: List[Justification] = field(
        default_factory=list,
        metadata={
            "name": "Justification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    frequency: List[Frequency] = field(
        default_factory=list,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    duration_period: Optional[DurationPeriod] = field(
        default=None,
        metadata={
            "name": "DurationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    subsequent_process_tender_requirement: List[SubsequentProcessTenderRequirement] = field(
        default_factory=list,
        metadata={
            "name": "SubsequentProcessTenderRequirement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class LineResponseType:
    line_reference: Optional[LineReference] = field(
        default=None,
        metadata={
            "name": "LineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    response: List[Response] = field(
        default_factory=list,
        metadata={
            "name": "Response",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderLineReferenceType:
    line_id: Optional[LineId] = field(
        default=None,
        metadata={
            "name": "LineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    sales_order_line_id: Optional[SalesOrderLineId] = field(
        default=None,
        metadata={
            "name": "SalesOrderLineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_status_code: Optional[LineStatusCode] = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    order_reference: Optional[OrderReference] = field(
        default=None,
        metadata={
            "name": "OrderReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ProjectReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    work_phase_reference: List[WorkPhaseReference] = field(
        default_factory=list,
        metadata={
            "name": "WorkPhaseReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class RequestedTenderTotalType:
    estimated_overall_contract_amount: Optional[EstimatedOverallContractAmount] = field(
        default=None,
        metadata={
            "name": "EstimatedOverallContractAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_amount: Optional[TotalAmount] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_included_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxIncludedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_amount: Optional[MinimumAmount] = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_amount: Optional[MaximumAmount] = field(
        default=None,
        metadata={
            "name": "MaximumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    monetary_scope: List[MonetaryScope] = field(
        default_factory=list,
        metadata={
            "name": "MonetaryScope",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    average_subsequent_contract_amount: Optional[AverageSubsequentContractAmount] = field(
        default=None,
        metadata={
            "name": "AverageSubsequentContractAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    applicable_tax_category: List[ApplicableTaxCategory] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableTaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TaxSubtotalType:
    taxable_amount: Optional[TaxableAmount] = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_amount: Optional[TaxAmount] = field(
        default=None,
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    calculation_sequence_numeric: Optional[CalculationSequenceNumeric] = field(
        default=None,
        metadata={
            "name": "CalculationSequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transaction_currency_tax_amount: Optional[TransactionCurrencyTaxAmount] = field(
        default=None,
        metadata={
            "name": "TransactionCurrencyTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    base_unit_measure: Optional[BaseUnitMeasure] = field(
        default=None,
        metadata={
            "name": "BaseUnitMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    per_unit_amount: Optional[PerUnitAmount] = field(
        default=None,
        metadata={
            "name": "PerUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tier_range: Optional[TierRange] = field(
        default=None,
        metadata={
            "name": "TierRange",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tier_rate_percent: Optional[TierRatePercent] = field(
        default=None,
        metadata={
            "name": "TierRatePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_category: Optional[TaxCategory] = field(
        default=None,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class TenderPreparationType:
    tender_envelope_id: Optional[TenderEnvelopeId] = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    tender_envelope_type_code: Optional[TenderEnvelopeTypeCode] = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    open_tender_id: Optional[OpenTenderId] = field(
        default=None,
        metadata={
            "name": "OpenTenderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    procurement_project_lot: List["ProcurementProjectLot"] = field(
        default_factory=list,
        metadata={
            "name": "ProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_tender_requirement: List[DocumentTenderRequirement] = field(
        default_factory=list,
        metadata={
            "name": "DocumentTenderRequirement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CallDuty(DutyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DependentPriceReference(DependentPriceReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Duty(DutyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EnergyWaterSupply(EnergyWaterSupplyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EnvironmentalEmission(EnvironmentalEmissionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinancialAccount(FinancialAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinancingFinancialAccount(FinancialAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FrameworkAgreement(FrameworkAgreementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LineResponse(LineResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OrderLineReference(OrderLineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PayeeFinancialAccount(FinancialAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PayerFinancialAccount(FinancialAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ProjectReference(ProjectReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedTenderTotal(RequestedTenderTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TaxSubtotal(TaxSubtotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderPreparation(TenderPreparationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TimeDuty(DutyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PersonType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    first_name: Optional[FirstName] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    family_name: Optional[FamilyName] = field(
        default=None,
        metadata={
            "name": "FamilyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    middle_name: Optional[MiddleName] = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    other_name: Optional[OtherName] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name_suffix: Optional[NameSuffix] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    job_title: Optional[JobTitle] = field(
        default=None,
        metadata={
            "name": "JobTitle",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    nationality_id: Optional[NationalityId] = field(
        default=None,
        metadata={
            "name": "NationalityID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gender_code: Optional[GenderCode] = field(
        default=None,
        metadata={
            "name": "GenderCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    birth_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    birthplace_name: Optional[BirthplaceName] = field(
        default=None,
        metadata={
            "name": "BirthplaceName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    organization_department: Optional[OrganizationDepartment] = field(
        default=None,
        metadata={
            "name": "OrganizationDepartment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    financial_account: Optional[FinancialAccount] = field(
        default=None,
        metadata={
            "name": "FinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    identity_document_reference: List[IdentityDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "IdentityDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    residence_address: Optional[ResidenceAddress] = field(
        default=None,
        metadata={
            "name": "ResidenceAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TaxTotalType:
    tax_amount: Optional[TaxAmount] = field(
        default=None,
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    rounding_amount: Optional[RoundingAmount] = field(
        default=None,
        metadata={
            "name": "RoundingAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_evidence_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxEvidenceIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_included_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxIncludedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_subtotal: List[TaxSubtotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxSubtotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CrewMemberPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DriverPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MasterPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PassengerPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Person(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReportingPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SecurityOfficerPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ShipsSurgeonPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TaxTotal(TaxTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TechnicalCommitteePerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class WithholdingTaxTotal(TaxTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AwardingTermsType:
    weighting_algorithm_code: Optional[WeightingAlgorithmCode] = field(
        default=None,
        metadata={
            "name": "WeightingAlgorithmCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    technical_committee_description: List[TechnicalCommitteeDescription] = field(
        default_factory=list,
        metadata={
            "name": "TechnicalCommitteeDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    low_tenders_description: List[LowTendersDescription] = field(
        default_factory=list,
        metadata={
            "name": "LowTendersDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    prize_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrizeIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    prize_description: List[PrizeDescription] = field(
        default_factory=list,
        metadata={
            "name": "PrizeDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_description: List[PaymentDescription] = field(
        default_factory=list,
        metadata={
            "name": "PaymentDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    followup_contract_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FollowupContractIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    binding_on_buyer_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BindingOnBuyerIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    awarding_criterion: List[AwardingCriterion] = field(
        default_factory=list,
        metadata={
            "name": "AwardingCriterion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    technical_committee_person: List[TechnicalCommitteePerson] = field(
        default_factory=list,
        metadata={
            "name": "TechnicalCommitteePerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PartyType:
    mark_care_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MarkCareIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    mark_attention_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MarkAttentionIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    website_uri: Optional[WebsiteUri] = field(
        default=None,
        metadata={
            "name": "WebsiteURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    logo_reference_id: Optional[LogoReferenceId] = field(
        default=None,
        metadata={
            "name": "LogoReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    endpoint_id: Optional[EndpointId] = field(
        default=None,
        metadata={
            "name": "EndpointID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    industry_classification_code: Optional[IndustryClassificationCode] = field(
        default=None,
        metadata={
            "name": "IndustryClassificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    party_identification: List[PartyIdentification] = field(
        default_factory=list,
        metadata={
            "name": "PartyIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    party_name: List[PartyName] = field(
        default_factory=list,
        metadata={
            "name": "PartyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    physical_location: Optional[PhysicalLocation] = field(
        default=None,
        metadata={
            "name": "PhysicalLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    party_tax_scheme: List[PartyTaxScheme] = field(
        default_factory=list,
        metadata={
            "name": "PartyTaxScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    party_legal_entity: List[PartyLegalEntity] = field(
        default_factory=list,
        metadata={
            "name": "PartyLegalEntity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    person: List[Person] = field(
        default_factory=list,
        metadata={
            "name": "Person",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    agent_party: Optional["AgentParty"] = field(
        default=None,
        metadata={
            "name": "AgentParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    service_provider_party: List[ServiceProviderParty] = field(
        default_factory=list,
        metadata={
            "name": "ServiceProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    power_of_attorney: List[PowerOfAttorney] = field(
        default_factory=list,
        metadata={
            "name": "PowerOfAttorney",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    financial_account: Optional[FinancialAccount] = field(
        default=None,
        metadata={
            "name": "FinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PriceExtensionType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AdditionalInformationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AgentParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AppealInformationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AppealReceiverParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AwardingTerms(AwardingTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BeneficiaryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BillOfLadingHolderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BillToParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CarrierParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsigneeParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsignorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContactParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractResponsibleParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CustomsAgentParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeliveryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DespatchParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DocumentProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EvidenceIssuingParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExporterParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinalDeliveryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinancingParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FreightForwarderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class GuarantorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class HazardousItemNotificationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class HeadOfficeParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ImporterParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InformationContentProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InsuranceParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InterestedParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InventoryReportingParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class IssuerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemPriceExtension(PriceExtensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LoadingProofParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LogisticsOperatorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ManufacturerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MediationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MortgageHolderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class NotaryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class NotifyParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OperatingParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginalDespatchParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginatorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OwnerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Party(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PayeeParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PayerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PerformingCarrierParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PickupParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PreSelectedParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PreparationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PriceExtension(PriceExtensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReceiverParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RecipientParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ResponsibleTransportServiceProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SenderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SignatoryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SourceIssuerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubcontractorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubscriberParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubstituteCarrierParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TaxRepresentativeParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderEvaluationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderRecipientParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TendererParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TerminalOperatorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportAdvisorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportServiceProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportUserParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UtilityCustomerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UtilitySupplierParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class WarrantyParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class WitnessParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AppealTermsType:
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    presentation_period: Optional[PresentationPeriod] = field(
        default=None,
        metadata={
            "name": "PresentationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    appeal_information_party: Optional[AppealInformationParty] = field(
        default=None,
        metadata={
            "name": "AppealInformationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    appeal_receiver_party: Optional[AppealReceiverParty] = field(
        default=None,
        metadata={
            "name": "AppealReceiverParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    mediation_party: Optional[MediationParty] = field(
        default=None,
        metadata={
            "name": "MediationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ContractingPartyType1:
    class Meta:
        name = "ContractingPartyType"

    buyer_profile_uri: Optional[BuyerProfileUri] = field(
        default=None,
        metadata={
            "name": "BuyerProfileURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contracting_party_type: List[ContractingPartyType] = field(
        default_factory=list,
        metadata={
            "name": "ContractingPartyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contracting_activity: List[ContractingActivity] = field(
        default_factory=list,
        metadata={
            "name": "ContractingActivity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class CustomerPartyType:
    customer_assigned_account_id: Optional[CustomerAssignedAccountId] = field(
        default=None,
        metadata={
            "name": "CustomerAssignedAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    supplier_assigned_account_id: Optional[SupplierAssignedAccountId] = field(
        default=None,
        metadata={
            "name": "SupplierAssignedAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    additional_account_id: List[AdditionalAccountId] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_contact: Optional[DeliveryContact] = field(
        default=None,
        metadata={
            "name": "DeliveryContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    accounting_contact: Optional[AccountingContact] = field(
        default=None,
        metadata={
            "name": "AccountingContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    buyer_contact: Optional[BuyerContact] = field(
        default=None,
        metadata={
            "name": "BuyerContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CustomsDeclarationType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class DespatchType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    requested_despatch_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RequestedDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    requested_despatch_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "RequestedDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    estimated_despatch_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EstimatedDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    estimated_despatch_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EstimatedDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    actual_despatch_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ActualDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    actual_despatch_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ActualDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    guaranteed_despatch_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "GuaranteedDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    guaranteed_despatch_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "GuaranteedDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    release_id: Optional[ReleaseId] = field(
        default=None,
        metadata={
            "name": "ReleaseID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    instructions: List[Instructions] = field(
        default_factory=list,
        metadata={
            "name": "Instructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    despatch_address: Optional[DespatchAddress] = field(
        default=None,
        metadata={
            "name": "DespatchAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch_location: Optional[DespatchLocation] = field(
        default=None,
        metadata={
            "name": "DespatchLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch_party: Optional[DespatchParty] = field(
        default=None,
        metadata={
            "name": "DespatchParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    carrier_party: Optional[CarrierParty] = field(
        default=None,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    notify_party: List[NotifyParty] = field(
        default_factory=list,
        metadata={
            "name": "NotifyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    estimated_despatch_period: Optional[EstimatedDespatchPeriod] = field(
        default=None,
        metadata={
            "name": "EstimatedDespatchPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    requested_despatch_period: Optional[RequestedDespatchPeriod] = field(
        default=None,
        metadata={
            "name": "RequestedDespatchPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class DocumentDistributionType:
    print_qualifier: Optional[PrintQualifier] = field(
        default=None,
        metadata={
            "name": "PrintQualifier",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    maximum_copies_numeric: Optional[MaximumCopiesNumeric] = field(
        default=None,
        metadata={
            "name": "MaximumCopiesNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class DocumentResponseType:
    response: Optional[Response] = field(
        default=None,
        metadata={
            "name": "Response",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    recipient_party: Optional[RecipientParty] = field(
        default=None,
        metadata={
            "name": "RecipientParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    line_response: List[LineResponse] = field(
        default_factory=list,
        metadata={
            "name": "LineResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EconomicOperatorShortListType:
    limitation_description: List[LimitationDescription] = field(
        default_factory=list,
        metadata={
            "name": "LimitationDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    expected_quantity: Optional[ExpectedQuantity] = field(
        default=None,
        metadata={
            "name": "ExpectedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pre_selected_party: List[PreSelectedParty] = field(
        default_factory=list,
        metadata={
            "name": "PreSelectedParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EndorserPartyType:
    role_code: Optional[RoleCode] = field(
        default=None,
        metadata={
            "name": "RoleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    signatory_contact: Optional[SignatoryContact] = field(
        default=None,
        metadata={
            "name": "SignatoryContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class EvidenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    evidence_type_code: Optional[EvidenceTypeCode] = field(
        default=None,
        metadata={
            "name": "EvidenceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    candidate_statement: List[CandidateStatement] = field(
        default_factory=list,
        metadata={
            "name": "CandidateStatement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    evidence_issuing_party: Optional[EvidenceIssuingParty] = field(
        default=None,
        metadata={
            "name": "EvidenceIssuingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: Optional[DocumentReference] = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class HazardousItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    placard_notation: Optional[PlacardNotation] = field(
        default=None,
        metadata={
            "name": "PlacardNotation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    placard_endorsement: Optional[PlacardEndorsement] = field(
        default=None,
        metadata={
            "name": "PlacardEndorsement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    additional_information: List[AdditionalInformation] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    undgcode: Optional[Undgcode] = field(
        default=None,
        metadata={
            "name": "UNDGCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    emergency_procedures_code: Optional[EmergencyProceduresCode] = field(
        default=None,
        metadata={
            "name": "EmergencyProceduresCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    medical_first_aid_guide_code: Optional[MedicalFirstAidGuideCode] = field(
        default=None,
        metadata={
            "name": "MedicalFirstAidGuideCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    technical_name: Optional[TechnicalName] = field(
        default=None,
        metadata={
            "name": "TechnicalName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    category_name: Optional[CategoryName] = field(
        default=None,
        metadata={
            "name": "CategoryName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hazardous_category_code: Optional[HazardousCategoryCode] = field(
        default=None,
        metadata={
            "name": "HazardousCategoryCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    upper_orange_hazard_placard_id: Optional[UpperOrangeHazardPlacardId] = field(
        default=None,
        metadata={
            "name": "UpperOrangeHazardPlacardID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    lower_orange_hazard_placard_id: Optional[LowerOrangeHazardPlacardId] = field(
        default=None,
        metadata={
            "name": "LowerOrangeHazardPlacardID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    marking_id: Optional[MarkingId] = field(
        default=None,
        metadata={
            "name": "MarkingID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hazard_class_id: Optional[HazardClassId] = field(
        default=None,
        metadata={
            "name": "HazardClassID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_weight_measure: Optional[NetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_volume_measure: Optional[NetVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contact_party: Optional[ContactParty] = field(
        default=None,
        metadata={
            "name": "ContactParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    secondary_hazard: List[SecondaryHazard] = field(
        default_factory=list,
        metadata={
            "name": "SecondaryHazard",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    hazardous_goods_transit: List[HazardousGoodsTransit] = field(
        default_factory=list,
        metadata={
            "name": "HazardousGoodsTransit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    emergency_temperature: Optional[EmergencyTemperature] = field(
        default=None,
        metadata={
            "name": "EmergencyTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    flashpoint_temperature: Optional[FlashpointTemperature] = field(
        default=None,
        metadata={
            "name": "FlashpointTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    additional_temperature: List[AdditionalTemperature] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ImmobilizedSecurityType:
    immobilization_certificate_id: Optional[ImmobilizationCertificateId] = field(
        default=None,
        metadata={
            "name": "ImmobilizationCertificateID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    security_id: Optional[SecurityId] = field(
        default=None,
        metadata={
            "name": "SecurityID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    face_value_amount: Optional[FaceValueAmount] = field(
        default=None,
        metadata={
            "name": "FaceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    market_value_amount: Optional[MarketValueAmount] = field(
        default=None,
        metadata={
            "name": "MarketValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    shares_number_quantity: Optional[SharesNumberQuantity] = field(
        default=None,
        metadata={
            "name": "SharesNumberQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ItemIdentificationType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    extended_id: Optional[ExtendedId] = field(
        default=None,
        metadata={
            "name": "ExtendedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    barcode_symbology_id: Optional[BarcodeSymbologyId] = field(
        default=None,
        metadata={
            "name": "BarcodeSymbologyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    physical_attribute: List[PhysicalAttribute] = field(
        default_factory=list,
        metadata={
            "name": "PhysicalAttribute",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    measurement_dimension: List[MeasurementDimension] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class NotificationRequirementType:
    notification_type_code: Optional[NotificationTypeCode] = field(
        default=None,
        metadata={
            "name": "NotificationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    post_event_notification_duration_measure: Optional[PostEventNotificationDurationMeasure] = field(
        default=None,
        metadata={
            "name": "PostEventNotificationDurationMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pre_event_notification_duration_measure: Optional[PreEventNotificationDurationMeasure] = field(
        default=None,
        metadata={
            "name": "PreEventNotificationDurationMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    notify_party: List[NotifyParty] = field(
        default_factory=list,
        metadata={
            "name": "NotifyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    notification_period: List[NotificationPeriod] = field(
        default_factory=list,
        metadata={
            "name": "NotificationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    notification_location: List[NotificationLocation] = field(
        default_factory=list,
        metadata={
            "name": "NotificationLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PaymentMandateType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    mandate_type_code: Optional[MandateTypeCode] = field(
        default=None,
        metadata={
            "name": "MandateTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_payment_instructions_numeric: Optional[MaximumPaymentInstructionsNumeric] = field(
        default=None,
        metadata={
            "name": "MaximumPaymentInstructionsNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_paid_amount: Optional[MaximumPaidAmount] = field(
        default=None,
        metadata={
            "name": "MaximumPaidAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    signature_id: Optional[SignatureId] = field(
        default=None,
        metadata={
            "name": "SignatureID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payer_party: Optional[PayerParty] = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payer_financial_account: Optional[PayerFinancialAccount] = field(
        default=None,
        metadata={
            "name": "PayerFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_reversal_period: Optional[PaymentReversalPeriod] = field(
        default=None,
        metadata={
            "name": "PaymentReversalPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    clause: List[Clause] = field(
        default_factory=list,
        metadata={
            "name": "Clause",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PickupType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    actual_pickup_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ActualPickupDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    actual_pickup_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ActualPickupTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    earliest_pickup_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EarliestPickupDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    earliest_pickup_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestPickupTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latest_pickup_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatestPickupDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latest_pickup_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestPickupTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pickup_location: Optional[PickupLocation] = field(
        default=None,
        metadata={
            "name": "PickupLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pickup_party: Optional[PickupParty] = field(
        default=None,
        metadata={
            "name": "PickupParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class SignatureType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validation_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ValidationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validation_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ValidationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validator_id: Optional[ValidatorId] = field(
        default=None,
        metadata={
            "name": "ValidatorID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    canonicalization_method: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    signature_method: Optional[SignatureMethod] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    signatory_party: Optional[SignatoryParty] = field(
        default=None,
        metadata={
            "name": "SignatoryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    digital_signature_attachment: Optional[DigitalSignatureAttachment] = field(
        default=None,
        metadata={
            "name": "DigitalSignatureAttachment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    original_document_reference: Optional[OriginalDocumentReference] = field(
        default=None,
        metadata={
            "name": "OriginalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class SupplierPartyType:
    customer_assigned_account_id: Optional[CustomerAssignedAccountId] = field(
        default=None,
        metadata={
            "name": "CustomerAssignedAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    additional_account_id: List[AdditionalAccountId] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    data_sending_capability: Optional[DataSendingCapability] = field(
        default=None,
        metadata={
            "name": "DataSendingCapability",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch_contact: Optional[DespatchContact] = field(
        default=None,
        metadata={
            "name": "DespatchContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    accounting_contact: Optional[AccountingContact] = field(
        default=None,
        metadata={
            "name": "AccountingContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    seller_contact: Optional[SellerContact] = field(
        default=None,
        metadata={
            "name": "SellerContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TradeFinancingType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    financing_instrument_code: Optional[FinancingInstrumentCode] = field(
        default=None,
        metadata={
            "name": "FinancingInstrumentCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contract_document_reference: Optional[ContractDocumentReference] = field(
        default=None,
        metadata={
            "name": "ContractDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    financing_party: Optional[FinancingParty] = field(
        default=None,
        metadata={
            "name": "FinancingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    financing_financial_account: Optional[FinancingFinancialAccount] = field(
        default=None,
        metadata={
            "name": "FinancingFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    clause: List[Clause] = field(
        default_factory=list,
        metadata={
            "name": "Clause",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TransportMeansType:
    journey_id: Optional[JourneyId] = field(
        default=None,
        metadata={
            "name": "JourneyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    registration_nationality_id: Optional[RegistrationNationalityId] = field(
        default=None,
        metadata={
            "name": "RegistrationNationalityID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    registration_nationality: List[RegistrationNationality] = field(
        default_factory=list,
        metadata={
            "name": "RegistrationNationality",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    direction_code: Optional[DirectionCode] = field(
        default=None,
        metadata={
            "name": "DirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_means_type_code: Optional[TransportMeansTypeCode] = field(
        default=None,
        metadata={
            "name": "TransportMeansTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    trade_service_code: Optional[TradeServiceCode] = field(
        default=None,
        metadata={
            "name": "TradeServiceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    stowage: Optional[Stowage] = field(
        default=None,
        metadata={
            "name": "Stowage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    air_transport: Optional[AirTransport] = field(
        default=None,
        metadata={
            "name": "AirTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    road_transport: Optional[RoadTransport] = field(
        default=None,
        metadata={
            "name": "RoadTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    rail_transport: Optional[RailTransport] = field(
        default=None,
        metadata={
            "name": "RailTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    maritime_transport: Optional[MaritimeTransport] = field(
        default=None,
        metadata={
            "name": "MaritimeTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    owner_party: Optional[OwnerParty] = field(
        default=None,
        metadata={
            "name": "OwnerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    measurement_dimension: List[MeasurementDimension] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class WinningPartyType:
    rank: Optional[Rank] = field(
        default=None,
        metadata={
            "name": "Rank",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class AccountingCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AccountingSupplierParty(SupplierPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AdditionalDocumentResponse(DocumentResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AdditionalItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AppealTerms(AppealTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ApplicableTransportMeans(TransportMeansType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BuyerCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BuyersItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CatalogueItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractingParty(ContractingPartyType1):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractorCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CustomsDeclaration(CustomsDeclarationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeliveryCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Despatch(DespatchType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DespatchSupplierParty(SupplierPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DocumentDistribution(DocumentDistributionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DocumentResponse(DocumentResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EconomicOperatorShortList(EconomicOperatorShortListType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EndorserParty(EndorserPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Evidence(EvidenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class HazardousItem(HazardousItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ImmobilizedSecurity(ImmobilizedSecurityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ManufacturersItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class NotificationRequirement(NotificationRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginatorCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PaymentMandate(PaymentMandateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Pickup(PickupType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RecipientCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RetailerCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SellerSupplierParty(SupplierPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SellersItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Signature(SignatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class StandardItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SuggestedEvidence(EvidenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SupplierParty(SupplierPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TradeFinancing(TradeFinancingType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportMeans(TransportMeansType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class WinningParty(WinningPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CertificateType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    certificate_type_code: Optional[CertificateTypeCode] = field(
        default=None,
        metadata={
            "name": "CertificateTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    certificate_type: Optional[UblCommonBasicComponents21CertificateType] = field(
        default=None,
        metadata={
            "name": "CertificateType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    remarks: List[Remarks] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CompletedTaskType:
    annual_average_amount: Optional[AnnualAverageAmount] = field(
        default=None,
        metadata={
            "name": "AnnualAverageAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_task_amount: Optional[TotalTaskAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaskAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    party_capacity_amount: Optional[PartyCapacityAmount] = field(
        default=None,
        metadata={
            "name": "PartyCapacityAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    evidence_supplied: List[EvidenceSupplied] = field(
        default_factory=list,
        metadata={
            "name": "EvidenceSupplied",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    recipient_customer_party: Optional[RecipientCustomerParty] = field(
        default=None,
        metadata={
            "name": "RecipientCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EndorsementType:
    document_id: Optional[DocumentId] = field(
        default=None,
        metadata={
            "name": "DocumentID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    approval_status: Optional[ApprovalStatus] = field(
        default=None,
        metadata={
            "name": "ApprovalStatus",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    remarks: List[Remarks] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    endorser_party: Optional[EndorserParty] = field(
        default=None,
        metadata={
            "name": "EndorserParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EvaluationCriterionType:
    evaluation_criterion_type_code: Optional[EvaluationCriterionTypeCode] = field(
        default=None,
        metadata={
            "name": "EvaluationCriterionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    threshold_amount: Optional[ThresholdAmount] = field(
        default=None,
        metadata={
            "name": "ThresholdAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    threshold_quantity: Optional[ThresholdQuantity] = field(
        default=None,
        metadata={
            "name": "ThresholdQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    expression_code: Optional[ExpressionCode] = field(
        default=None,
        metadata={
            "name": "ExpressionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    expression: List[Expression] = field(
        default_factory=list,
        metadata={
            "name": "Expression",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    duration_period: Optional[DurationPeriod] = field(
        default=None,
        metadata={
            "name": "DurationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    suggested_evidence: List[SuggestedEvidence] = field(
        default_factory=list,
        metadata={
            "name": "SuggestedEvidence",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PaymentMeansType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_means_code: Optional[PaymentMeansCode] = field(
        default=None,
        metadata={
            "name": "PaymentMeansCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    payment_due_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PaymentDueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_channel_code: Optional[PaymentChannelCode] = field(
        default=None,
        metadata={
            "name": "PaymentChannelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    instruction_id: Optional[InstructionId] = field(
        default=None,
        metadata={
            "name": "InstructionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    instruction_note: List[InstructionNote] = field(
        default_factory=list,
        metadata={
            "name": "InstructionNote",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_id: List[PaymentId] = field(
        default_factory=list,
        metadata={
            "name": "PaymentID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    card_account: Optional[CardAccount] = field(
        default=None,
        metadata={
            "name": "CardAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payer_financial_account: Optional[PayerFinancialAccount] = field(
        default=None,
        metadata={
            "name": "PayerFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payee_financial_account: Optional[PayeeFinancialAccount] = field(
        default=None,
        metadata={
            "name": "PayeeFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    credit_account: Optional[CreditAccount] = field(
        default=None,
        metadata={
            "name": "CreditAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_mandate: Optional[PaymentMandate] = field(
        default=None,
        metadata={
            "name": "PaymentMandate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    trade_financing: Optional[TradeFinancing] = field(
        default=None,
        metadata={
            "name": "TradeFinancing",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TendererRequirementType:
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tenderer_requirement_type_code: Optional[TendererRequirementTypeCode] = field(
        default=None,
        metadata={
            "name": "TendererRequirementTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    legal_reference: Optional[LegalReference] = field(
        default=None,
        metadata={
            "name": "LegalReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    suggested_evidence: List[SuggestedEvidence] = field(
        default_factory=list,
        metadata={
            "name": "SuggestedEvidence",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TenderingProcessType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    original_contracting_system_id: Optional[OriginalContractingSystemId] = field(
        default=None,
        metadata={
            "name": "OriginalContractingSystemID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    negotiation_description: List[NegotiationDescription] = field(
        default_factory=list,
        metadata={
            "name": "NegotiationDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    procedure_code: Optional[ProcedureCode] = field(
        default=None,
        metadata={
            "name": "ProcedureCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    urgency_code: Optional[UrgencyCode] = field(
        default=None,
        metadata={
            "name": "UrgencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    expense_code: Optional[ExpenseCode] = field(
        default=None,
        metadata={
            "name": "ExpenseCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    part_presentation_code: Optional[PartPresentationCode] = field(
        default=None,
        metadata={
            "name": "PartPresentationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contracting_system_code: Optional[ContractingSystemCode] = field(
        default=None,
        metadata={
            "name": "ContractingSystemCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    submission_method_code: Optional[SubmissionMethodCode] = field(
        default=None,
        metadata={
            "name": "SubmissionMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    candidate_reduction_constraint_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CandidateReductionConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    government_agreement_constraint_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GovernmentAgreementConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_availability_period: Optional[DocumentAvailabilityPeriod] = field(
        default=None,
        metadata={
            "name": "DocumentAvailabilityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tender_submission_deadline_period: Optional[TenderSubmissionDeadlinePeriod] = field(
        default=None,
        metadata={
            "name": "TenderSubmissionDeadlinePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    invitation_submission_period: Optional[InvitationSubmissionPeriod] = field(
        default=None,
        metadata={
            "name": "InvitationSubmissionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    participation_request_reception_period: Optional[ParticipationRequestReceptionPeriod] = field(
        default=None,
        metadata={
            "name": "ParticipationRequestReceptionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    notice_document_reference: List[NoticeDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "NoticeDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    additional_document_reference: List[AdditionalDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    process_justification: List[ProcessJustification] = field(
        default_factory=list,
        metadata={
            "name": "ProcessJustification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    economic_operator_short_list: Optional[EconomicOperatorShortList] = field(
        default=None,
        metadata={
            "name": "EconomicOperatorShortList",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    open_tender_event: List[OpenTenderEvent] = field(
        default_factory=list,
        metadata={
            "name": "OpenTenderEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    auction_terms: Optional[AuctionTerms] = field(
        default=None,
        metadata={
            "name": "AuctionTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    framework_agreement: Optional[FrameworkAgreement] = field(
        default=None,
        metadata={
            "name": "FrameworkAgreement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TransportEventType:
    identification_id: Optional[IdentificationId] = field(
        default=None,
        metadata={
            "name": "IdentificationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    occurrence_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "OccurrenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    occurrence_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "OccurrenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_event_type_code: Optional[TransportEventTypeCode] = field(
        default=None,
        metadata={
            "name": "TransportEventTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    completion_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CompletionIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reported_shipment: Optional["ReportedShipment"] = field(
        default=None,
        metadata={
            "name": "ReportedShipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    current_status: List[CurrentStatus] = field(
        default_factory=list,
        metadata={
            "name": "CurrentStatus",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contact: List[Contact] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    period: List[Period] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AcceptanceTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ActualArrivalTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ActualDepartureTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ActualPickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ActualWaypointTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AvailabilityTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Certificate(CertificateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CompletedTask(CompletedTaskType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeliveryTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DetentionTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DischargeTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DropoffTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EmbassyEndorsement(EndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Endorsement(EndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EstimatedArrivalTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EstimatedDepartureTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EvaluationCriterion(EvaluationCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExaminationTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExportationTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinancialEvaluationCriterion(EvaluationCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class HandlingTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InsuranceEndorsement(EndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class IssuerEndorsement(EndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LoadingTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OptionalTakeoverTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PaymentMeans(PaymentMeansType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PlannedArrivalTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PlannedDeliveryTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PlannedDepartureTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PlannedPickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PlannedWaypointTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PositioningTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class QuarantineTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReceiptTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedArrivalTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedDeliveryTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedDepartureTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedPickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestedWaypointTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SpecificTendererRequirement(TendererRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class StorageTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TakeoverTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TechnicalEvaluationCriterion(EvaluationCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TendererRequirement(TendererRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderingProcess(TenderingProcessType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UpdatedDeliveryTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UpdatedPickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class WarehousingTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AllowanceChargeType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    charge_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChargeIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    allowance_charge_reason_code: Optional[AllowanceChargeReasonCode] = field(
        default=None,
        metadata={
            "name": "AllowanceChargeReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    allowance_charge_reason: List[AllowanceChargeReason] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceChargeReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    multiplier_factor_numeric: Optional[MultiplierFactorNumeric] = field(
        default=None,
        metadata={
            "name": "MultiplierFactorNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    prepaid_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PrepaidIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    base_amount: Optional[BaseAmount] = field(
        default=None,
        metadata={
            "name": "BaseAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    per_unit_amount: Optional[PerUnitAmount] = field(
        default=None,
        metadata={
            "name": "PerUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_category: List[TaxCategory] = field(
        default_factory=list,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: Optional[TaxTotal] = field(
        default=None,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_means: List[PaymentMeans] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ItemType:
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pack_quantity: Optional[PackQuantity] = field(
        default=None,
        metadata={
            "name": "PackQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pack_size_numeric: Optional[PackSizeNumeric] = field(
        default=None,
        metadata={
            "name": "PackSizeNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    catalogue_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CatalogueIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hazardous_risk_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    additional_information: List[AdditionalInformation] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    keyword: List[Keyword] = field(
        default_factory=list,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    brand_name: List[BrandName] = field(
        default_factory=list,
        metadata={
            "name": "BrandName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    model_name: List[ModelName] = field(
        default_factory=list,
        metadata={
            "name": "ModelName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    buyers_item_identification: Optional[BuyersItemIdentification] = field(
        default=None,
        metadata={
            "name": "BuyersItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    sellers_item_identification: Optional[SellersItemIdentification] = field(
        default=None,
        metadata={
            "name": "SellersItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    manufacturers_item_identification: List[ManufacturersItemIdentification] = field(
        default_factory=list,
        metadata={
            "name": "ManufacturersItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    standard_item_identification: Optional[StandardItemIdentification] = field(
        default=None,
        metadata={
            "name": "StandardItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    catalogue_item_identification: Optional[CatalogueItemIdentification] = field(
        default=None,
        metadata={
            "name": "CatalogueItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    additional_item_identification: List[AdditionalItemIdentification] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    catalogue_document_reference: Optional[CatalogueDocumentReference] = field(
        default=None,
        metadata={
            "name": "CatalogueDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item_specification_document_reference: List[ItemSpecificationDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "ItemSpecificationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    origin_country: Optional[OriginCountry] = field(
        default=None,
        metadata={
            "name": "OriginCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    commodity_classification: List[CommodityClassification] = field(
        default_factory=list,
        metadata={
            "name": "CommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transaction_conditions: List[TransactionConditions] = field(
        default_factory=list,
        metadata={
            "name": "TransactionConditions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    hazardous_item: List[HazardousItem] = field(
        default_factory=list,
        metadata={
            "name": "HazardousItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    classified_tax_category: List[ClassifiedTaxCategory] = field(
        default_factory=list,
        metadata={
            "name": "ClassifiedTaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    additional_item_property: List[AdditionalItemProperty] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalItemProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    manufacturer_party: List[ManufacturerParty] = field(
        default_factory=list,
        metadata={
            "name": "ManufacturerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    information_content_provider_party: Optional[InformationContentProviderParty] = field(
        default=None,
        metadata={
            "name": "InformationContentProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    origin_address: List[OriginAddress] = field(
        default_factory=list,
        metadata={
            "name": "OriginAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item_instance: List[ItemInstance] = field(
        default_factory=list,
        metadata={
            "name": "ItemInstance",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    certificate: List[Certificate] = field(
        default_factory=list,
        metadata={
            "name": "Certificate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    dimension: List[Dimension] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class QualifyingPartyType:
    participation_percent: Optional[ParticipationPercent] = field(
        default=None,
        metadata={
            "name": "ParticipationPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    personal_situation: List[PersonalSituation] = field(
        default_factory=list,
        metadata={
            "name": "PersonalSituation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    operating_years_quantity: Optional[OperatingYearsQuantity] = field(
        default=None,
        metadata={
            "name": "OperatingYearsQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    employee_quantity: Optional[EmployeeQuantity] = field(
        default=None,
        metadata={
            "name": "EmployeeQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    business_classification_evidence_id: Optional[BusinessClassificationEvidenceId] = field(
        default=None,
        metadata={
            "name": "BusinessClassificationEvidenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    business_identity_evidence_id: Optional[BusinessIdentityEvidenceId] = field(
        default=None,
        metadata={
            "name": "BusinessIdentityEvidenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tenderer_role_code: Optional[TendererRoleCode] = field(
        default=None,
        metadata={
            "name": "TendererRoleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    business_classification_scheme: Optional[BusinessClassificationScheme] = field(
        default=None,
        metadata={
            "name": "BusinessClassificationScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    technical_capability: List[TechnicalCapability] = field(
        default_factory=list,
        metadata={
            "name": "TechnicalCapability",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    financial_capability: List[FinancialCapability] = field(
        default_factory=list,
        metadata={
            "name": "FinancialCapability",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    completed_task: List[CompletedTask] = field(
        default_factory=list,
        metadata={
            "name": "CompletedTask",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    declaration: List[Declaration] = field(
        default_factory=list,
        metadata={
            "name": "Declaration",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    economic_operator_role: Optional[EconomicOperatorRole] = field(
        default=None,
        metadata={
            "name": "EconomicOperatorRole",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TendererQualificationRequestType:
    company_legal_form_code: Optional[CompanyLegalFormCode] = field(
        default=None,
        metadata={
            "name": "CompanyLegalFormCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    company_legal_form: Optional[CompanyLegalForm] = field(
        default=None,
        metadata={
            "name": "CompanyLegalForm",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    personal_situation: List[PersonalSituation] = field(
        default_factory=list,
        metadata={
            "name": "PersonalSituation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    operating_years_quantity: Optional[OperatingYearsQuantity] = field(
        default=None,
        metadata={
            "name": "OperatingYearsQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    employee_quantity: Optional[EmployeeQuantity] = field(
        default=None,
        metadata={
            "name": "EmployeeQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    required_business_classification_scheme: List[RequiredBusinessClassificationScheme] = field(
        default_factory=list,
        metadata={
            "name": "RequiredBusinessClassificationScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    technical_evaluation_criterion: List[TechnicalEvaluationCriterion] = field(
        default_factory=list,
        metadata={
            "name": "TechnicalEvaluationCriterion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    financial_evaluation_criterion: List[FinancialEvaluationCriterion] = field(
        default_factory=list,
        metadata={
            "name": "FinancialEvaluationCriterion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    specific_tenderer_requirement: List[SpecificTendererRequirement] = field(
        default_factory=list,
        metadata={
            "name": "SpecificTendererRequirement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    economic_operator_role: List[EconomicOperatorRole] = field(
        default_factory=list,
        metadata={
            "name": "EconomicOperatorRole",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TransportScheduleType:
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    reference_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReferenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reference_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ReferenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reliability_percent: Optional[ReliabilityPercent] = field(
        default=None,
        metadata={
            "name": "ReliabilityPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    remarks: List[Remarks] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    status_location: Optional[StatusLocation] = field(
        default=None,
        metadata={
            "name": "StatusLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    actual_arrival_transport_event: Optional[ActualArrivalTransportEvent] = field(
        default=None,
        metadata={
            "name": "ActualArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    actual_departure_transport_event: Optional[ActualDepartureTransportEvent] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    estimated_departure_transport_event: Optional[EstimatedDepartureTransportEvent] = field(
        default=None,
        metadata={
            "name": "EstimatedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    estimated_arrival_transport_event: Optional[EstimatedArrivalTransportEvent] = field(
        default=None,
        metadata={
            "name": "EstimatedArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    planned_departure_transport_event: Optional[PlannedDepartureTransportEvent] = field(
        default=None,
        metadata={
            "name": "PlannedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    planned_arrival_transport_event: Optional[PlannedArrivalTransportEvent] = field(
        default=None,
        metadata={
            "name": "PlannedArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AdditionalQualifyingParty(QualifyingPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AllowanceCharge(AllowanceChargeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExtraAllowanceCharge(AllowanceChargeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FreightAllowanceCharge(AllowanceChargeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Item(ItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MainQualifyingParty(QualifyingPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class QualifyingParty(QualifyingPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ServiceAllowanceCharge(AllowanceChargeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SupplyItem(ItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TendererQualificationRequest(TendererQualificationRequestType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportSchedule(TransportScheduleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BillingReferenceLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CatalogueItemSpecificationUpdateLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    contractor_customer_party: Optional[ContractorCustomerParty] = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class DeliveryTermsType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    special_terms: List[SpecialTerms] = field(
        default_factory=list,
        metadata={
            "name": "SpecialTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    loss_risk_responsibility_code: Optional[LossRiskResponsibilityCode] = field(
        default=None,
        metadata={
            "name": "LossRiskResponsibilityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    loss_risk: List[LossRisk] = field(
        default_factory=list,
        metadata={
            "name": "LossRisk",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    delivery_location: Optional[DeliveryLocation] = field(
        default=None,
        metadata={
            "name": "DeliveryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: Optional[AllowanceCharge] = field(
        default=None,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class DespatchLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_status_code: Optional[LineStatusCode] = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    delivered_quantity: Optional[DeliveredQuantity] = field(
        default=None,
        metadata={
            "name": "DeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    backorder_quantity: Optional[BackorderQuantity] = field(
        default=None,
        metadata={
            "name": "BackorderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    backorder_reason: List[BackorderReason] = field(
        default_factory=list,
        metadata={
            "name": "BackorderReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    outstanding_quantity: Optional[OutstandingQuantity] = field(
        default=None,
        metadata={
            "name": "OutstandingQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    outstanding_reason: List[OutstandingReason] = field(
        default_factory=list,
        metadata={
            "name": "OutstandingReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    oversupply_quantity: Optional[OversupplyQuantity] = field(
        default=None,
        metadata={
            "name": "OversupplyQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    order_line_reference: List[OrderLineReference] = field(
        default_factory=list,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    shipment: List["Shipment"] = field(
        default_factory=list,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class EventLineItemType:
    line_number_numeric: Optional[LineNumberNumeric] = field(
        default=None,
        metadata={
            "name": "LineNumberNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    participating_locations_location: Optional[ParticipatingLocationsLocation] = field(
        default=None,
        metadata={
            "name": "ParticipatingLocationsLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    retail_planned_impact: List[RetailPlannedImpact] = field(
        default_factory=list,
        metadata={
            "name": "RetailPlannedImpact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    supply_item: Optional[SupplyItem] = field(
        default=None,
        metadata={
            "name": "SupplyItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class ExceptionCriteriaLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    threshold_value_comparison_code: Optional[ThresholdValueComparisonCode] = field(
        default=None,
        metadata={
            "name": "ThresholdValueComparisonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    threshold_quantity: Optional[ThresholdQuantity] = field(
        default=None,
        metadata={
            "name": "ThresholdQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    exception_status_code: Optional[ExceptionStatusCode] = field(
        default=None,
        metadata={
            "name": "ExceptionStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    collaboration_priority_code: Optional[CollaborationPriorityCode] = field(
        default=None,
        metadata={
            "name": "CollaborationPriorityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    exception_resolution_code: Optional[ExceptionResolutionCode] = field(
        default=None,
        metadata={
            "name": "ExceptionResolutionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    supply_chain_activity_type_code: Optional[SupplyChainActivityTypeCode] = field(
        default=None,
        metadata={
            "name": "SupplyChainActivityTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    performance_metric_type_code: Optional[PerformanceMetricTypeCode] = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    effective_period: Optional[EffectivePeriod] = field(
        default=None,
        metadata={
            "name": "EffectivePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    supply_item: List[SupplyItem] = field(
        default_factory=list,
        metadata={
            "name": "SupplyItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )
    forecast_exception_criterion_line: Optional[ForecastExceptionCriterionLine] = field(
        default=None,
        metadata={
            "name": "ForecastExceptionCriterionLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ExceptionNotificationLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    exception_status_code: Optional[ExceptionStatusCode] = field(
        default=None,
        metadata={
            "name": "ExceptionStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    collaboration_priority_code: Optional[CollaborationPriorityCode] = field(
        default=None,
        metadata={
            "name": "CollaborationPriorityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    resolution_code: Optional[ResolutionCode] = field(
        default=None,
        metadata={
            "name": "ResolutionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    compared_value_measure: Optional[ComparedValueMeasure] = field(
        default=None,
        metadata={
            "name": "ComparedValueMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    source_value_measure: Optional[SourceValueMeasure] = field(
        default=None,
        metadata={
            "name": "SourceValueMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    variance_quantity: Optional[VarianceQuantity] = field(
        default=None,
        metadata={
            "name": "VarianceQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    supply_chain_activity_type_code: Optional[SupplyChainActivityTypeCode] = field(
        default=None,
        metadata={
            "name": "SupplyChainActivityTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    performance_metric_type_code: Optional[PerformanceMetricTypeCode] = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    exception_observation_period: Optional[ExceptionObservationPeriod] = field(
        default=None,
        metadata={
            "name": "ExceptionObservationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    forecast_exception: Optional[ForecastException] = field(
        default=None,
        metadata={
            "name": "ForecastException",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    supply_item: Optional[SupplyItem] = field(
        default=None,
        metadata={
            "name": "SupplyItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class InstructionForReturnsLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    manufacturer_party: Optional[ManufacturerParty] = field(
        default=None,
        metadata={
            "name": "ManufacturerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class InventoryReportLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    inventory_value_amount: Optional[InventoryValueAmount] = field(
        default=None,
        metadata={
            "name": "InventoryValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    availability_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AvailabilityDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    availability_status_code: Optional[AvailabilityStatusCode] = field(
        default=None,
        metadata={
            "name": "AvailabilityStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    inventory_location: Optional[InventoryLocation] = field(
        default=None,
        metadata={
            "name": "InventoryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ItemLocationQuantityType:
    lead_time_measure: Optional[LeadTimeMeasure] = field(
        default=None,
        metadata={
            "name": "LeadTimeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hazardous_risk_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    trading_restrictions: List[TradingRestrictions] = field(
        default_factory=list,
        metadata={
            "name": "TradingRestrictions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    applicable_territory_address: List[ApplicableTerritoryAddress] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableTerritoryAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    price: Optional["Price"] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_unit: List[DeliveryUnit] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    applicable_tax_category: List[ApplicableTaxCategory] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableTaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    package: Optional["Package"] = field(
        default=None,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    dependent_price_reference: Optional[DependentPriceReference] = field(
        default=None,
        metadata={
            "name": "DependentPriceReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PerformanceDataLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    performance_value_quantity: Optional[PerformanceValueQuantity] = field(
        default=None,
        metadata={
            "name": "PerformanceValueQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    performance_metric_type_code: Optional[PerformanceMetricTypeCode] = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ReceiptLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    received_quantity: Optional[ReceivedQuantity] = field(
        default=None,
        metadata={
            "name": "ReceivedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    short_quantity: Optional[ShortQuantity] = field(
        default=None,
        metadata={
            "name": "ShortQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    shortage_action_code: Optional[ShortageActionCode] = field(
        default=None,
        metadata={
            "name": "ShortageActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    rejected_quantity: Optional[RejectedQuantity] = field(
        default=None,
        metadata={
            "name": "RejectedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reject_reason_code: Optional[RejectReasonCode] = field(
        default=None,
        metadata={
            "name": "RejectReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reject_reason: List[RejectReason] = field(
        default_factory=list,
        metadata={
            "name": "RejectReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reject_action_code: Optional[RejectActionCode] = field(
        default=None,
        metadata={
            "name": "RejectActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity_discrepancy_code: Optional[QuantityDiscrepancyCode] = field(
        default=None,
        metadata={
            "name": "QuantityDiscrepancyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    oversupply_quantity: Optional[OversupplyQuantity] = field(
        default=None,
        metadata={
            "name": "OversupplyQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    received_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    timing_complaint_code: Optional[TimingComplaintCode] = field(
        default=None,
        metadata={
            "name": "TimingComplaintCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    timing_complaint: Optional[TimingComplaint] = field(
        default=None,
        metadata={
            "name": "TimingComplaint",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    order_line_reference: Optional[OrderLineReference] = field(
        default=None,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch_line_reference: List[DespatchLineReference] = field(
        default_factory=list,
        metadata={
            "name": "DespatchLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: List[Item] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shipment: List["Shipment"] = field(
        default_factory=list,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ShipmentStageType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_mode_code: Optional[TransportModeCode] = field(
        default=None,
        metadata={
            "name": "TransportModeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_means_type_code: Optional[TransportMeansTypeCode] = field(
        default=None,
        metadata={
            "name": "TransportMeansTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transit_direction_code: Optional[TransitDirectionCode] = field(
        default=None,
        metadata={
            "name": "TransitDirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pre_carriage_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PreCarriageIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    on_carriage_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OnCarriageIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    estimated_delivery_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EstimatedDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    estimated_delivery_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EstimatedDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    required_delivery_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RequiredDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    required_delivery_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "RequiredDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    loading_sequence_id: Optional[LoadingSequenceId] = field(
        default=None,
        metadata={
            "name": "LoadingSequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    successive_sequence_id: Optional[SuccessiveSequenceId] = field(
        default=None,
        metadata={
            "name": "SuccessiveSequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    instructions: List[Instructions] = field(
        default_factory=list,
        metadata={
            "name": "Instructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    demurrage_instructions: List[DemurrageInstructions] = field(
        default_factory=list,
        metadata={
            "name": "DemurrageInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    crew_quantity: Optional[CrewQuantity] = field(
        default=None,
        metadata={
            "name": "CrewQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    passenger_quantity: Optional[PassengerQuantity] = field(
        default=None,
        metadata={
            "name": "PassengerQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transit_period: Optional[TransitPeriod] = field(
        default=None,
        metadata={
            "name": "TransitPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    carrier_party: List[CarrierParty] = field(
        default_factory=list,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_means: Optional[TransportMeans] = field(
        default=None,
        metadata={
            "name": "TransportMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    loading_port_location: Optional[LoadingPortLocation] = field(
        default=None,
        metadata={
            "name": "LoadingPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    unloading_port_location: Optional[UnloadingPortLocation] = field(
        default=None,
        metadata={
            "name": "UnloadingPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transship_port_location: Optional[TransshipPortLocation] = field(
        default=None,
        metadata={
            "name": "TransshipPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    loading_transport_event: Optional[LoadingTransportEvent] = field(
        default=None,
        metadata={
            "name": "LoadingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    examination_transport_event: Optional[ExaminationTransportEvent] = field(
        default=None,
        metadata={
            "name": "ExaminationTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    availability_transport_event: Optional[AvailabilityTransportEvent] = field(
        default=None,
        metadata={
            "name": "AvailabilityTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    exportation_transport_event: Optional[ExportationTransportEvent] = field(
        default=None,
        metadata={
            "name": "ExportationTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    discharge_transport_event: Optional[DischargeTransportEvent] = field(
        default=None,
        metadata={
            "name": "DischargeTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    warehousing_transport_event: Optional[WarehousingTransportEvent] = field(
        default=None,
        metadata={
            "name": "WarehousingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    takeover_transport_event: Optional[TakeoverTransportEvent] = field(
        default=None,
        metadata={
            "name": "TakeoverTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    optional_takeover_transport_event: Optional[OptionalTakeoverTransportEvent] = field(
        default=None,
        metadata={
            "name": "OptionalTakeoverTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    dropoff_transport_event: Optional[DropoffTransportEvent] = field(
        default=None,
        metadata={
            "name": "DropoffTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    actual_pickup_transport_event: Optional[ActualPickupTransportEvent] = field(
        default=None,
        metadata={
            "name": "ActualPickupTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_transport_event: Optional[DeliveryTransportEvent] = field(
        default=None,
        metadata={
            "name": "DeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    receipt_transport_event: Optional[ReceiptTransportEvent] = field(
        default=None,
        metadata={
            "name": "ReceiptTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    storage_transport_event: Optional[StorageTransportEvent] = field(
        default=None,
        metadata={
            "name": "StorageTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    acceptance_transport_event: Optional[AcceptanceTransportEvent] = field(
        default=None,
        metadata={
            "name": "AcceptanceTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    terminal_operator_party: Optional[TerminalOperatorParty] = field(
        default=None,
        metadata={
            "name": "TerminalOperatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    customs_agent_party: Optional[CustomsAgentParty] = field(
        default=None,
        metadata={
            "name": "CustomsAgentParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    estimated_transit_period: Optional[EstimatedTransitPeriod] = field(
        default=None,
        metadata={
            "name": "EstimatedTransitPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    freight_allowance_charge: List[FreightAllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    freight_charge_location: Optional[FreightChargeLocation] = field(
        default=None,
        metadata={
            "name": "FreightChargeLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    detention_transport_event: List[DetentionTransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "DetentionTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    requested_departure_transport_event: Optional[RequestedDepartureTransportEvent] = field(
        default=None,
        metadata={
            "name": "RequestedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    requested_arrival_transport_event: Optional[RequestedArrivalTransportEvent] = field(
        default=None,
        metadata={
            "name": "RequestedArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    requested_waypoint_transport_event: List[RequestedWaypointTransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "RequestedWaypointTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    planned_departure_transport_event: Optional[PlannedDepartureTransportEvent] = field(
        default=None,
        metadata={
            "name": "PlannedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    planned_arrival_transport_event: Optional[PlannedArrivalTransportEvent] = field(
        default=None,
        metadata={
            "name": "PlannedArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    planned_waypoint_transport_event: List[PlannedWaypointTransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "PlannedWaypointTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    actual_departure_transport_event: Optional[ActualDepartureTransportEvent] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    actual_waypoint_transport_event: Optional[ActualWaypointTransportEvent] = field(
        default=None,
        metadata={
            "name": "ActualWaypointTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    actual_arrival_transport_event: Optional[ActualArrivalTransportEvent] = field(
        default=None,
        metadata={
            "name": "ActualArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_event: List[TransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "TransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    estimated_departure_transport_event: Optional[EstimatedDepartureTransportEvent] = field(
        default=None,
        metadata={
            "name": "EstimatedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    estimated_arrival_transport_event: Optional[EstimatedArrivalTransportEvent] = field(
        default=None,
        metadata={
            "name": "EstimatedArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    passenger_person: List[PassengerPerson] = field(
        default_factory=list,
        metadata={
            "name": "PassengerPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    driver_person: List[DriverPerson] = field(
        default_factory=list,
        metadata={
            "name": "DriverPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    reporting_person: Optional[ReportingPerson] = field(
        default=None,
        metadata={
            "name": "ReportingPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    crew_member_person: List[CrewMemberPerson] = field(
        default_factory=list,
        metadata={
            "name": "CrewMemberPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    security_officer_person: Optional[SecurityOfficerPerson] = field(
        default=None,
        metadata={
            "name": "SecurityOfficerPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    master_person: Optional[MasterPerson] = field(
        default=None,
        metadata={
            "name": "MasterPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    ships_surgeon_person: Optional[ShipsSurgeonPerson] = field(
        default=None,
        metadata={
            "name": "ShipsSurgeonPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class StockAvailabilityReportLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    value_amount: Optional[ValueAmount] = field(
        default=None,
        metadata={
            "name": "ValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    availability_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AvailabilityDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    availability_status_code: Optional[AvailabilityStatusCode] = field(
        default=None,
        metadata={
            "name": "AvailabilityStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class TenderingTermsType:
    awarding_method_type_code: Optional[AwardingMethodTypeCode] = field(
        default=None,
        metadata={
            "name": "AwardingMethodTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    price_evaluation_code: Optional[PriceEvaluationCode] = field(
        default=None,
        metadata={
            "name": "PriceEvaluationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_variant_quantity: Optional[MaximumVariantQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumVariantQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    variant_constraint_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VariantConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accepted_variants_description: List[AcceptedVariantsDescription] = field(
        default_factory=list,
        metadata={
            "name": "AcceptedVariantsDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    price_revision_formula_description: List[PriceRevisionFormulaDescription] = field(
        default_factory=list,
        metadata={
            "name": "PriceRevisionFormulaDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    funding_program_code: Optional[FundingProgramCode] = field(
        default=None,
        metadata={
            "name": "FundingProgramCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    funding_program: List[FundingProgram] = field(
        default_factory=list,
        metadata={
            "name": "FundingProgram",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_advertisement_amount: Optional[MaximumAdvertisementAmount] = field(
        default=None,
        metadata={
            "name": "MaximumAdvertisementAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_frequency_code: Optional[PaymentFrequencyCode] = field(
        default=None,
        metadata={
            "name": "PaymentFrequencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    economic_operator_registry_uri: Optional[EconomicOperatorRegistryUri] = field(
        default=None,
        metadata={
            "name": "EconomicOperatorRegistryURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    required_curricula_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiredCurriculaIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    other_conditions_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OtherConditionsIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    additional_conditions: List[AdditionalConditions] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalConditions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latest_security_clearance_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatestSecurityClearanceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    documentation_fee_amount: Optional[DocumentationFeeAmount] = field(
        default=None,
        metadata={
            "name": "DocumentationFeeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    penalty_clause: List[PenaltyClause] = field(
        default_factory=list,
        metadata={
            "name": "PenaltyClause",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    required_financial_guarantee: List[RequiredFinancialGuarantee] = field(
        default_factory=list,
        metadata={
            "name": "RequiredFinancialGuarantee",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    procurement_legislation_document_reference: Optional[ProcurementLegislationDocumentReference] = field(
        default=None,
        metadata={
            "name": "ProcurementLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    fiscal_legislation_document_reference: Optional[FiscalLegislationDocumentReference] = field(
        default=None,
        metadata={
            "name": "FiscalLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    environmental_legislation_document_reference: Optional[EnvironmentalLegislationDocumentReference] = field(
        default=None,
        metadata={
            "name": "EnvironmentalLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    employment_legislation_document_reference: Optional[EmploymentLegislationDocumentReference] = field(
        default=None,
        metadata={
            "name": "EmploymentLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contractual_document_reference: List[ContractualDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "ContractualDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    call_for_tenders_document_reference: Optional[CallForTendersDocumentReference] = field(
        default=None,
        metadata={
            "name": "CallForTendersDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_terms: List[PaymentTerms] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tenderer_qualification_request: List[TendererQualificationRequest] = field(
        default_factory=list,
        metadata={
            "name": "TendererQualificationRequest",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowed_subcontract_terms: List[AllowedSubcontractTerms] = field(
        default_factory=list,
        metadata={
            "name": "AllowedSubcontractTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tender_preparation: List[TenderPreparation] = field(
        default_factory=list,
        metadata={
            "name": "TenderPreparation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contract_execution_requirement: List[ContractExecutionRequirement] = field(
        default_factory=list,
        metadata={
            "name": "ContractExecutionRequirement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    awarding_terms: Optional[AwardingTerms] = field(
        default=None,
        metadata={
            "name": "AwardingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    additional_information_party: Optional[AdditionalInformationParty] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_provider_party: Optional[DocumentProviderParty] = field(
        default=None,
        metadata={
            "name": "DocumentProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tender_recipient_party: Optional[TenderRecipientParty] = field(
        default=None,
        metadata={
            "name": "TenderRecipientParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contract_responsible_party: Optional[ContractResponsibleParty] = field(
        default=None,
        metadata={
            "name": "ContractResponsibleParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tender_evaluation_party: List[TenderEvaluationParty] = field(
        default_factory=list,
        metadata={
            "name": "TenderEvaluationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tender_validity_period: Optional[TenderValidityPeriod] = field(
        default=None,
        metadata={
            "name": "TenderValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contract_acceptance_period: Optional[ContractAcceptancePeriod] = field(
        default=None,
        metadata={
            "name": "ContractAcceptancePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    appeal_terms: Optional[AppealTerms] = field(
        default=None,
        metadata={
            "name": "AppealTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    language: List[Language] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    budget_account_line: List[BudgetAccountLine] = field(
        default_factory=list,
        metadata={
            "name": "BudgetAccountLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    replaced_notice_document_reference: Optional[ReplacedNoticeDocumentReference] = field(
        default=None,
        metadata={
            "name": "ReplacedNoticeDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class BillingReferenceLine(BillingReferenceLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CatalogueItemSpecificationUpdateLine(CatalogueItemSpecificationUpdateLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DeliveryTerms(DeliveryTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DespatchLine(DespatchLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class EventLineItem(EventLineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExceptionCriteriaLine(ExceptionCriteriaLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExceptionNotificationLine(ExceptionNotificationLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class HandlingUnitDespatchLine(DespatchLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InstructionForReturnsLine(InstructionForReturnsLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InventoryReportLine(InventoryReportLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemLocationQuantity(ItemLocationQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MainCarriageShipmentStage(ShipmentStageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OfferedItemLocationQuantity(ItemLocationQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OnCarriageShipmentStage(ShipmentStageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginalItemLocationQuantity(ItemLocationQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PerformanceDataLine(PerformanceDataLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PreCarriageShipmentStage(ShipmentStageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReceiptLine(ReceiptLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReceivedHandlingUnitReceiptLine(ReceiptLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequiredItemLocationQuantity(ItemLocationQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ShipmentStage(ShipmentStageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class StockAvailabilityReportLine(StockAvailabilityReportLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderingTerms(TenderingTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BillingReferenceType:
    invoice_document_reference: Optional[InvoiceDocumentReference] = field(
        default=None,
        metadata={
            "name": "InvoiceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    self_billed_invoice_document_reference: Optional[SelfBilledInvoiceDocumentReference] = field(
        default=None,
        metadata={
            "name": "SelfBilledInvoiceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    credit_note_document_reference: Optional[CreditNoteDocumentReference] = field(
        default=None,
        metadata={
            "name": "CreditNoteDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    self_billed_credit_note_document_reference: Optional[SelfBilledCreditNoteDocumentReference] = field(
        default=None,
        metadata={
            "name": "SelfBilledCreditNoteDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    debit_note_document_reference: Optional[DebitNoteDocumentReference] = field(
        default=None,
        metadata={
            "name": "DebitNoteDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    reminder_document_reference: Optional[ReminderDocumentReference] = field(
        default=None,
        metadata={
            "name": "ReminderDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    additional_document_reference: Optional[AdditionalDocumentReference] = field(
        default=None,
        metadata={
            "name": "AdditionalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    billing_reference_line: List[BillingReferenceLine] = field(
        default_factory=list,
        metadata={
            "name": "BillingReferenceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CatalogueLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    action_code: Optional[ActionCode] = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    life_cycle_status_code: Optional[LifeCycleStatusCode] = field(
        default=None,
        metadata={
            "name": "LifeCycleStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contract_subdivision: Optional[ContractSubdivision] = field(
        default=None,
        metadata={
            "name": "ContractSubdivision",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    orderable_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OrderableIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    orderable_unit: Optional[OrderableUnit] = field(
        default=None,
        metadata={
            "name": "OrderableUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    content_unit_quantity: Optional[ContentUnitQuantity] = field(
        default=None,
        metadata={
            "name": "ContentUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    order_quantity_increment_numeric: Optional[OrderQuantityIncrementNumeric] = field(
        default=None,
        metadata={
            "name": "OrderQuantityIncrementNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_order_quantity: Optional[MinimumOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_order_quantity: Optional[MaximumOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    warranty_information: List[WarrantyInformation] = field(
        default_factory=list,
        metadata={
            "name": "WarrantyInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pack_level_code: Optional[PackLevelCode] = field(
        default=None,
        metadata={
            "name": "PackLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contractor_customer_party: Optional[ContractorCustomerParty] = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    warranty_party: Optional[WarrantyParty] = field(
        default=None,
        metadata={
            "name": "WarrantyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    line_validity_period: Optional[LineValidityPeriod] = field(
        default=None,
        metadata={
            "name": "LineValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item_comparison: List[ItemComparison] = field(
        default_factory=list,
        metadata={
            "name": "ItemComparison",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    component_related_item: List[ComponentRelatedItem] = field(
        default_factory=list,
        metadata={
            "name": "ComponentRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    accessory_related_item: List[AccessoryRelatedItem] = field(
        default_factory=list,
        metadata={
            "name": "AccessoryRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    required_related_item: List[RequiredRelatedItem] = field(
        default_factory=list,
        metadata={
            "name": "RequiredRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    replacement_related_item: List[ReplacementRelatedItem] = field(
        default_factory=list,
        metadata={
            "name": "ReplacementRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    complementary_related_item: List[ComplementaryRelatedItem] = field(
        default_factory=list,
        metadata={
            "name": "ComplementaryRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    replaced_related_item: List[ReplacedRelatedItem] = field(
        default_factory=list,
        metadata={
            "name": "ReplacedRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    required_item_location_quantity: List[RequiredItemLocationQuantity] = field(
        default_factory=list,
        metadata={
            "name": "RequiredItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    keyword_item_property: List[KeywordItemProperty] = field(
        default_factory=list,
        metadata={
            "name": "KeywordItemProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    call_for_tenders_line_reference: Optional[CallForTendersLineReference] = field(
        default=None,
        metadata={
            "name": "CallForTendersLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    call_for_tenders_document_reference: Optional[CallForTendersDocumentReference] = field(
        default=None,
        metadata={
            "name": "CallForTendersDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CataloguePricingUpdateLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    contractor_customer_party: Optional[ContractorCustomerParty] = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    required_item_location_quantity: List[RequiredItemLocationQuantity] = field(
        default_factory=list,
        metadata={
            "name": "RequiredItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CatalogueRequestLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    contract_subdivision: Optional[ContractSubdivision] = field(
        default=None,
        metadata={
            "name": "ContractSubdivision",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_validity_period: Optional[LineValidityPeriod] = field(
        default=None,
        metadata={
            "name": "LineValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    required_item_location_quantity: List[RequiredItemLocationQuantity] = field(
        default_factory=list,
        metadata={
            "name": "RequiredItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class ItemManagementProfileType:
    frozen_period_days_numeric: Optional[FrozenPeriodDaysNumeric] = field(
        default=None,
        metadata={
            "name": "FrozenPeriodDaysNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_inventory_quantity: Optional[MinimumInventoryQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumInventoryQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    multiple_order_quantity: Optional[MultipleOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MultipleOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    order_interval_days_numeric: Optional[OrderIntervalDaysNumeric] = field(
        default=None,
        metadata={
            "name": "OrderIntervalDaysNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    replenishment_owner_description: List[ReplenishmentOwnerDescription] = field(
        default_factory=list,
        metadata={
            "name": "ReplenishmentOwnerDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    target_service_percent: Optional[TargetServicePercent] = field(
        default=None,
        metadata={
            "name": "TargetServicePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    target_inventory_quantity: Optional[TargetInventoryQuantity] = field(
        default=None,
        metadata={
            "name": "TargetInventoryQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    effective_period: Optional[EffectivePeriod] = field(
        default=None,
        metadata={
            "name": "EffectivePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    item_location_quantity: Optional[ItemLocationQuantity] = field(
        default=None,
        metadata={
            "name": "ItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class MiscellaneousEventType:
    miscellaneous_event_type_code: Optional[MiscellaneousEventTypeCode] = field(
        default=None,
        metadata={
            "name": "MiscellaneousEventTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    event_line_item: List[EventLineItem] = field(
        default_factory=list,
        metadata={
            "name": "EventLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class PricingReferenceType:
    original_item_location_quantity: Optional[OriginalItemLocationQuantity] = field(
        default=None,
        metadata={
            "name": "OriginalItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    alternative_condition_price: List["AlternativeConditionPrice"] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeConditionPrice",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PromotionalEventLineItemType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    event_line_item: Optional[EventLineItem] = field(
        default=None,
        metadata={
            "name": "EventLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class RequestForTenderLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_included_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TaxIncludedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_amount: Optional[MinimumAmount] = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_amount: Optional[MaximumAmount] = field(
        default=None,
        metadata={
            "name": "MaximumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    estimated_amount: Optional[EstimatedAmount] = field(
        default=None,
        metadata={
            "name": "EstimatedAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_period: List[DeliveryPeriod] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    required_item_location_quantity: List[RequiredItemLocationQuantity] = field(
        default_factory=list,
        metadata={
            "name": "RequiredItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    sub_request_for_tender_line: List["SubRequestForTenderLine"] = field(
        default_factory=list,
        metadata={
            "name": "SubRequestForTenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TenderLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_tax_amount: Optional[TotalTaxAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    orderable_unit: Optional[OrderableUnit] = field(
        default=None,
        metadata={
            "name": "OrderableUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    content_unit_quantity: Optional[ContentUnitQuantity] = field(
        default=None,
        metadata={
            "name": "ContentUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    order_quantity_increment_numeric: Optional[OrderQuantityIncrementNumeric] = field(
        default=None,
        metadata={
            "name": "OrderQuantityIncrementNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_order_quantity: Optional[MinimumOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_order_quantity: Optional[MaximumOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    warranty_information: List[WarrantyInformation] = field(
        default_factory=list,
        metadata={
            "name": "WarrantyInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pack_level_code: Optional[PackLevelCode] = field(
        default=None,
        metadata={
            "name": "PackLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    offered_item_location_quantity: List[OfferedItemLocationQuantity] = field(
        default_factory=list,
        metadata={
            "name": "OfferedItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    replacement_related_item: List[ReplacementRelatedItem] = field(
        default_factory=list,
        metadata={
            "name": "ReplacementRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    warranty_party: Optional[WarrantyParty] = field(
        default=None,
        metadata={
            "name": "WarrantyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    sub_tender_line: List["SubTenderLine"] = field(
        default_factory=list,
        metadata={
            "name": "SubTenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    call_for_tenders_line_reference: Optional[CallForTendersLineReference] = field(
        default=None,
        metadata={
            "name": "CallForTendersLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    call_for_tenders_document_reference: Optional[CallForTendersDocumentReference] = field(
        default=None,
        metadata={
            "name": "CallForTendersDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TransportExecutionTermsType:
    transport_user_special_terms: List[TransportUserSpecialTerms] = field(
        default_factory=list,
        metadata={
            "name": "TransportUserSpecialTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_service_provider_special_terms: List[TransportServiceProviderSpecialTerms] = field(
        default_factory=list,
        metadata={
            "name": "TransportServiceProviderSpecialTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    change_conditions: List[ChangeConditions] = field(
        default_factory=list,
        metadata={
            "name": "ChangeConditions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_terms: List[PaymentTerms] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_terms: List[DeliveryTerms] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    bonus_payment_terms: Optional[BonusPaymentTerms] = field(
        default=None,
        metadata={
            "name": "BonusPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    commission_payment_terms: Optional[CommissionPaymentTerms] = field(
        default=None,
        metadata={
            "name": "CommissionPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    penalty_payment_terms: Optional[PenaltyPaymentTerms] = field(
        default=None,
        metadata={
            "name": "PenaltyPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    environmental_emission: List[EnvironmentalEmission] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalEmission",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    notification_requirement: List[NotificationRequirement] = field(
        default_factory=list,
        metadata={
            "name": "NotificationRequirement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    service_charge_payment_terms: Optional[ServiceChargePaymentTerms] = field(
        default=None,
        metadata={
            "name": "ServiceChargePaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class BillingReference(BillingReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CatalogueLine(CatalogueLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CataloguePricingUpdateLine(CataloguePricingUpdateLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CatalogueRequestLine(CatalogueRequestLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemManagementProfile(ItemManagementProfileType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MiscellaneousEvent(MiscellaneousEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PricingReference(PricingReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PromotionalEventLineItem(PromotionalEventLineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestForTenderLine(RequestForTenderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubRequestForTenderLine(RequestForTenderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubTenderLine(TenderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderLine(TenderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportExecutionTerms(TransportExecutionTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InvoiceLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    invoiced_quantity: Optional[InvoicedQuantity] = field(
        default=None,
        metadata={
            "name": "InvoicedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    tax_point_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    free_of_charge_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeOfChargeIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    invoice_period: List[InvoicePeriod] = field(
        default_factory=list,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    order_line_reference: List[OrderLineReference] = field(
        default_factory=list,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch_line_reference: List[DespatchLineReference] = field(
        default_factory=list,
        metadata={
            "name": "DespatchLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    receipt_line_reference: List[ReceiptLineReference] = field(
        default_factory=list,
        metadata={
            "name": "ReceiptLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    billing_reference: List[BillingReference] = field(
        default_factory=list,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pricing_reference: Optional[PricingReference] = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    originator_party: Optional[OriginatorParty] = field(
        default=None,
        metadata={
            "name": "OriginatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery: List["Delivery"] = field(
        default_factory=list,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_terms: List[PaymentTerms] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    withholding_tax_total: List[WithholdingTaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "WithholdingTaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    price: Optional["Price"] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_terms: Optional[DeliveryTerms] = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    sub_invoice_line: List["SubInvoiceLine"] = field(
        default_factory=list,
        metadata={
            "name": "SubInvoiceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item_price_extension: Optional[ItemPriceExtension] = field(
        default=None,
        metadata={
            "name": "ItemPriceExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ProcurementProjectType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "min_occurs": 1,
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    procurement_type_code: Optional[ProcurementTypeCode] = field(
        default=None,
        metadata={
            "name": "ProcurementTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    procurement_sub_type_code: Optional[ProcurementSubTypeCode] = field(
        default=None,
        metadata={
            "name": "ProcurementSubTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quality_control_code: Optional[QualityControlCode] = field(
        default=None,
        metadata={
            "name": "QualityControlCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    required_fee_amount: Optional[RequiredFeeAmount] = field(
        default=None,
        metadata={
            "name": "RequiredFeeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    fee_description: List[FeeDescription] = field(
        default_factory=list,
        metadata={
            "name": "FeeDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    requested_delivery_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    estimated_overall_contract_quantity: Optional[EstimatedOverallContractQuantity] = field(
        default=None,
        metadata={
            "name": "EstimatedOverallContractQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    requested_tender_total: Optional[RequestedTenderTotal] = field(
        default=None,
        metadata={
            "name": "RequestedTenderTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    main_commodity_classification: Optional[MainCommodityClassification] = field(
        default=None,
        metadata={
            "name": "MainCommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    additional_commodity_classification: List[AdditionalCommodityClassification] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalCommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    realized_location: List[RealizedLocation] = field(
        default_factory=list,
        metadata={
            "name": "RealizedLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    planned_period: Optional[PlannedPeriod] = field(
        default=None,
        metadata={
            "name": "PlannedPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contract_extension: Optional[ContractExtension] = field(
        default=None,
        metadata={
            "name": "ContractExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    request_for_tender_line: List[RequestForTenderLine] = field(
        default_factory=list,
        metadata={
            "name": "RequestForTenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PromotionalSpecificationType:
    specification_id: Optional[SpecificationId] = field(
        default=None,
        metadata={
            "name": "SpecificationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    promotional_event_line_item: List[PromotionalEventLineItem] = field(
        default_factory=list,
        metadata={
            "name": "PromotionalEventLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )
    event_tactic: List[EventTactic] = field(
        default_factory=list,
        metadata={
            "name": "EventTactic",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class InvoiceLine(InvoiceLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ProcurementProject(ProcurementProjectType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PromotionalSpecification(PromotionalSpecificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubInvoiceLine(InvoiceLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class GoodsItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    sequence_number_id: Optional[SequenceNumberId] = field(
        default=None,
        metadata={
            "name": "SequenceNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hazardous_risk_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declared_customs_value_amount: Optional[DeclaredCustomsValueAmount] = field(
        default=None,
        metadata={
            "name": "DeclaredCustomsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declared_for_carriage_value_amount: Optional[DeclaredForCarriageValueAmount] = field(
        default=None,
        metadata={
            "name": "DeclaredForCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declared_statistics_value_amount: Optional[DeclaredStatisticsValueAmount] = field(
        default=None,
        metadata={
            "name": "DeclaredStatisticsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    free_on_board_value_amount: Optional[FreeOnBoardValueAmount] = field(
        default=None,
        metadata={
            "name": "FreeOnBoardValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    insurance_value_amount: Optional[InsuranceValueAmount] = field(
        default=None,
        metadata={
            "name": "InsuranceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    value_amount: Optional[ValueAmount] = field(
        default=None,
        metadata={
            "name": "ValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gross_weight_measure: Optional[GrossWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_weight_measure: Optional[NetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_net_weight_measure: Optional[NetNetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    chargeable_weight_measure: Optional[ChargeableWeightMeasure] = field(
        default=None,
        metadata={
            "name": "ChargeableWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gross_volume_measure: Optional[GrossVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_volume_measure: Optional[NetVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    preference_criterion_code: Optional[PreferenceCriterionCode] = field(
        default=None,
        metadata={
            "name": "PreferenceCriterionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    required_customs_id: Optional[RequiredCustomsId] = field(
        default=None,
        metadata={
            "name": "RequiredCustomsID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    customs_status_code: Optional[CustomsStatusCode] = field(
        default=None,
        metadata={
            "name": "CustomsStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    customs_tariff_quantity: Optional[CustomsTariffQuantity] = field(
        default=None,
        metadata={
            "name": "CustomsTariffQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    customs_import_classified_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CustomsImportClassifiedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    chargeable_quantity: Optional[ChargeableQuantity] = field(
        default=None,
        metadata={
            "name": "ChargeableQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    returnable_quantity: Optional[ReturnableQuantity] = field(
        default=None,
        metadata={
            "name": "ReturnableQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    trace_id: Optional[TraceId] = field(
        default=None,
        metadata={
            "name": "TraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    item: List[Item] = field(
        default_factory=list,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    goods_item_container: List[GoodsItemContainer] = field(
        default_factory=list,
        metadata={
            "name": "GoodsItemContainer",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    freight_allowance_charge: List[FreightAllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    invoice_line: List[InvoiceLine] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    temperature: List[Temperature] = field(
        default_factory=list,
        metadata={
            "name": "Temperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contained_goods_item: List["ContainedGoodsItem"] = field(
        default_factory=list,
        metadata={
            "name": "ContainedGoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    origin_address: Optional[OriginAddress] = field(
        default=None,
        metadata={
            "name": "OriginAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery: Optional["Delivery"] = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pickup: Optional[Pickup] = field(
        default=None,
        metadata={
            "name": "Pickup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch: Optional[Despatch] = field(
        default=None,
        metadata={
            "name": "Despatch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    measurement_dimension: List[MeasurementDimension] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    containing_package: List["ContainingPackage"] = field(
        default_factory=list,
        metadata={
            "name": "ContainingPackage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shipment_document_reference: Optional[ShipmentDocumentReference] = field(
        default=None,
        metadata={
            "name": "ShipmentDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    minimum_temperature: Optional[MinimumTemperature] = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    maximum_temperature: Optional[MaximumTemperature] = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ProcurementProjectLotType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    tendering_terms: Optional[TenderingTerms] = field(
        default=None,
        metadata={
            "name": "TenderingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    procurement_project: Optional[ProcurementProject] = field(
        default=None,
        metadata={
            "name": "ProcurementProject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PromotionalEventType:
    promotional_event_type_code: Optional[PromotionalEventTypeCode] = field(
        default=None,
        metadata={
            "name": "PromotionalEventTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    submission_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SubmissionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    first_shipment_availibility_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FirstShipmentAvailibilityDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latest_proposal_acceptance_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatestProposalAcceptanceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    promotional_specification: List[PromotionalSpecification] = field(
        default_factory=list,
        metadata={
            "name": "PromotionalSpecification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class ContainedGoodsItem(GoodsItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class GoodsItem(GoodsItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class InterestedProcurementProjectLot(ProcurementProjectLotType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ProcurementProjectLot(ProcurementProjectLotType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PromotionalEvent(PromotionalEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReferencedGoodsItem(GoodsItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PackageType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    returnable_material_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnableMaterialIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    package_level_code: Optional[PackageLevelCode] = field(
        default=None,
        metadata={
            "name": "PackageLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    packaging_type_code: Optional[PackagingTypeCode] = field(
        default=None,
        metadata={
            "name": "PackagingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    packing_material: List[PackingMaterial] = field(
        default_factory=list,
        metadata={
            "name": "PackingMaterial",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    trace_id: Optional[TraceId] = field(
        default=None,
        metadata={
            "name": "TraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contained_package: List["ContainedPackage"] = field(
        default_factory=list,
        metadata={
            "name": "ContainedPackage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    containing_transport_equipment: Optional["ContainingTransportEquipment"] = field(
        default=None,
        metadata={
            "name": "ContainingTransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    goods_item: List[GoodsItem] = field(
        default_factory=list,
        metadata={
            "name": "GoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    measurement_dimension: List[MeasurementDimension] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_unit: List[DeliveryUnit] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery: Optional["Delivery"] = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pickup: Optional[Pickup] = field(
        default=None,
        metadata={
            "name": "Pickup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch: Optional[Despatch] = field(
        default=None,
        metadata={
            "name": "Despatch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class QualificationResolutionType:
    admission_code: Optional[AdmissionCode] = field(
        default=None,
        metadata={
            "name": "AdmissionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    exclusion_reason: List[ExclusionReason] = field(
        default_factory=list,
        metadata={
            "name": "ExclusionReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    resolution: List[Resolution] = field(
        default_factory=list,
        metadata={
            "name": "Resolution",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    resolution_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ResolutionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    resolution_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ResolutionTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    procurement_project_lot: Optional[ProcurementProjectLot] = field(
        default=None,
        metadata={
            "name": "ProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TenderedProjectType:
    variant_id: Optional[VariantId] = field(
        default=None,
        metadata={
            "name": "VariantID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    fee_amount: Optional[FeeAmount] = field(
        default=None,
        metadata={
            "name": "FeeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    fee_description: List[FeeDescription] = field(
        default_factory=list,
        metadata={
            "name": "FeeDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tender_envelope_id: Optional[TenderEnvelopeId] = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tender_envelope_type_code: Optional[TenderEnvelopeTypeCode] = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    procurement_project_lot: Optional[ProcurementProjectLot] = field(
        default=None,
        metadata={
            "name": "ProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    evidence_document_reference: List[EvidenceDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "EvidenceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    legal_monetary_total: Optional[LegalMonetaryTotal] = field(
        default=None,
        metadata={
            "name": "LegalMonetaryTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tender_line: List[TenderLine] = field(
        default_factory=list,
        metadata={
            "name": "TenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    awarding_criterion_response: List[AwardingCriterionResponse] = field(
        default_factory=list,
        metadata={
            "name": "AwardingCriterionResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TendererPartyQualificationType:
    interested_procurement_project_lot: List[InterestedProcurementProjectLot] = field(
        default_factory=list,
        metadata={
            "name": "InterestedProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    main_qualifying_party: Optional[MainQualifyingParty] = field(
        default=None,
        metadata={
            "name": "MainQualifyingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    additional_qualifying_party: List[AdditionalQualifyingParty] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalQualifyingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ActualPackage(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class AwardedTenderedProject(TenderedProjectType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContainedPackage(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContainingPackage(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Package(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class QualificationResolution(QualificationResolutionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReferencedPackage(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderedProject(TenderedProjectType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TendererPartyQualification(TendererPartyQualificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportHandlingUnitType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_handling_unit_type_code: Optional[TransportHandlingUnitTypeCode] = field(
        default=None,
        metadata={
            "name": "TransportHandlingUnitTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    handling_code: Optional[HandlingCode] = field(
        default=None,
        metadata={
            "name": "HandlingCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    handling_instructions: List[HandlingInstructions] = field(
        default_factory=list,
        metadata={
            "name": "HandlingInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hazardous_risk_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_goods_item_quantity: Optional[TotalGoodsItemQuantity] = field(
        default=None,
        metadata={
            "name": "TotalGoodsItemQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_package_quantity: Optional[TotalPackageQuantity] = field(
        default=None,
        metadata={
            "name": "TotalPackageQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    damage_remarks: List[DamageRemarks] = field(
        default_factory=list,
        metadata={
            "name": "DamageRemarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    shipping_marks: List[ShippingMarks] = field(
        default_factory=list,
        metadata={
            "name": "ShippingMarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    trace_id: Optional[TraceId] = field(
        default=None,
        metadata={
            "name": "TraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    handling_unit_despatch_line: List[HandlingUnitDespatchLine] = field(
        default_factory=list,
        metadata={
            "name": "HandlingUnitDespatchLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    actual_package: List[ActualPackage] = field(
        default_factory=list,
        metadata={
            "name": "ActualPackage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    received_handling_unit_receipt_line: List[ReceivedHandlingUnitReceiptLine] = field(
        default_factory=list,
        metadata={
            "name": "ReceivedHandlingUnitReceiptLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_equipment: List["TransportEquipment"] = field(
        default_factory=list,
        metadata={
            "name": "TransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_means: List[TransportMeans] = field(
        default_factory=list,
        metadata={
            "name": "TransportMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    hazardous_goods_transit: List[HazardousGoodsTransit] = field(
        default_factory=list,
        metadata={
            "name": "HazardousGoodsTransit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    measurement_dimension: List[MeasurementDimension] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    minimum_temperature: Optional[MinimumTemperature] = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    maximum_temperature: Optional[MaximumTemperature] = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    goods_item: List[GoodsItem] = field(
        default_factory=list,
        metadata={
            "name": "GoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    floor_space_measurement_dimension: Optional[FloorSpaceMeasurementDimension] = field(
        default=None,
        metadata={
            "name": "FloorSpaceMeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pallet_space_measurement_dimension: Optional[PalletSpaceMeasurementDimension] = field(
        default=None,
        metadata={
            "name": "PalletSpaceMeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shipment_document_reference: List[ShipmentDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "ShipmentDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    status: List[Status] = field(
        default_factory=list,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    customs_declaration: List[CustomsDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "CustomsDeclaration",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    referenced_shipment: List["ReferencedShipment"] = field(
        default_factory=list,
        metadata={
            "name": "ReferencedShipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    package: List[Package] = field(
        default_factory=list,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class PackagedTransportHandlingUnit(TransportHandlingUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportHandlingUnit(TransportHandlingUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportEquipmentType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    referenced_consignment_id: List[ReferencedConsignmentId] = field(
        default_factory=list,
        metadata={
            "name": "ReferencedConsignmentID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_equipment_type_code: Optional[TransportEquipmentTypeCode] = field(
        default=None,
        metadata={
            "name": "TransportEquipmentTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    provider_type_code: Optional[ProviderTypeCode] = field(
        default=None,
        metadata={
            "name": "ProviderTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    owner_type_code: Optional[OwnerTypeCode] = field(
        default=None,
        metadata={
            "name": "OwnerTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    size_type_code: Optional[SizeTypeCode] = field(
        default=None,
        metadata={
            "name": "SizeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    disposition_code: Optional[DispositionCode] = field(
        default=None,
        metadata={
            "name": "DispositionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    fullness_indication_code: Optional[FullnessIndicationCode] = field(
        default=None,
        metadata={
            "name": "FullnessIndicationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    refrigeration_on_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RefrigerationOnIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    information: List[Information] = field(
        default_factory=list,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    returnability_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnabilityIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    legal_status_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LegalStatusIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    air_flow_percent: Optional[AirFlowPercent] = field(
        default=None,
        metadata={
            "name": "AirFlowPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    humidity_percent: Optional[HumidityPercent] = field(
        default=None,
        metadata={
            "name": "HumidityPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    animal_food_approved_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AnimalFoodApprovedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    human_food_approved_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HumanFoodApprovedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    dangerous_goods_approved_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DangerousGoodsApprovedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    refrigerated_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RefrigeratedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    characteristics: Optional[Characteristics] = field(
        default=None,
        metadata={
            "name": "Characteristics",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    damage_remarks: List[DamageRemarks] = field(
        default_factory=list,
        metadata={
            "name": "DamageRemarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    special_transport_requirements: List[SpecialTransportRequirements] = field(
        default_factory=list,
        metadata={
            "name": "SpecialTransportRequirements",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gross_weight_measure: Optional[GrossWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gross_volume_measure: Optional[GrossVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tare_weight_measure: Optional[TareWeightMeasure] = field(
        default=None,
        metadata={
            "name": "TareWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tracking_device_code: Optional[TrackingDeviceCode] = field(
        default=None,
        metadata={
            "name": "TrackingDeviceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    power_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PowerIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    trace_id: Optional[TraceId] = field(
        default=None,
        metadata={
            "name": "TraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    measurement_dimension: List[MeasurementDimension] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_equipment_seal: List[TransportEquipmentSeal] = field(
        default_factory=list,
        metadata={
            "name": "TransportEquipmentSeal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    minimum_temperature: Optional[MinimumTemperature] = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    maximum_temperature: Optional[MaximumTemperature] = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    provider_party: Optional[ProviderParty] = field(
        default=None,
        metadata={
            "name": "ProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    loading_proof_party: Optional[LoadingProofParty] = field(
        default=None,
        metadata={
            "name": "LoadingProofParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    supplier_party: Optional[SupplierParty] = field(
        default=None,
        metadata={
            "name": "SupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    owner_party: Optional[OwnerParty] = field(
        default=None,
        metadata={
            "name": "OwnerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    operating_party: Optional[OperatingParty] = field(
        default=None,
        metadata={
            "name": "OperatingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    loading_location: Optional[LoadingLocation] = field(
        default=None,
        metadata={
            "name": "LoadingLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    unloading_location: Optional[UnloadingLocation] = field(
        default=None,
        metadata={
            "name": "UnloadingLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    storage_location: Optional[StorageLocation] = field(
        default=None,
        metadata={
            "name": "StorageLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    positioning_transport_event: List[PositioningTransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "PositioningTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    quarantine_transport_event: List[QuarantineTransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "QuarantineTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_transport_event: List[DeliveryTransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pickup_transport_event: List[PickupTransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "PickupTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    handling_transport_event: List[HandlingTransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "HandlingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    loading_transport_event: List[LoadingTransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "LoadingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_event: List[TransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "TransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    applicable_transport_means: Optional[ApplicableTransportMeans] = field(
        default=None,
        metadata={
            "name": "ApplicableTransportMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    haulage_trading_terms: List[HaulageTradingTerms] = field(
        default_factory=list,
        metadata={
            "name": "HaulageTradingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    hazardous_goods_transit: List[HazardousGoodsTransit] = field(
        default_factory=list,
        metadata={
            "name": "HazardousGoodsTransit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    packaged_transport_handling_unit: List[PackagedTransportHandlingUnit] = field(
        default_factory=list,
        metadata={
            "name": "PackagedTransportHandlingUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    service_allowance_charge: List[ServiceAllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "ServiceAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    freight_allowance_charge: List[FreightAllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    attached_transport_equipment: List["AttachedTransportEquipment"] = field(
        default_factory=list,
        metadata={
            "name": "AttachedTransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery: Optional["Delivery"] = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pickup: Optional[Pickup] = field(
        default=None,
        metadata={
            "name": "Pickup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch: Optional[Despatch] = field(
        default=None,
        metadata={
            "name": "Despatch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shipment_document_reference: List[ShipmentDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "ShipmentDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contained_in_transport_equipment: List["ContainedInTransportEquipment"] = field(
        default_factory=list,
        metadata={
            "name": "ContainedInTransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    package: List[Package] = field(
        default_factory=list,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    goods_item: List[GoodsItem] = field(
        default_factory=list,
        metadata={
            "name": "GoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AttachedTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContainedInTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContainingTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReferencedTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SupportedTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UnsupportedTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportationServiceType:
    transport_service_code: Optional[TransportServiceCode] = field(
        default=None,
        metadata={
            "name": "TransportServiceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    tariff_class_code: Optional[TariffClassCode] = field(
        default=None,
        metadata={
            "name": "TariffClassCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    priority: Optional[Priority] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    freight_rate_class_code: Optional[FreightRateClassCode] = field(
        default=None,
        metadata={
            "name": "FreightRateClassCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transportation_service_description: List[TransportationServiceDescription] = field(
        default_factory=list,
        metadata={
            "name": "TransportationServiceDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transportation_service_details_uri: Optional[TransportationServiceDetailsUri] = field(
        default=None,
        metadata={
            "name": "TransportationServiceDetailsURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    nomination_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NominationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    nomination_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "NominationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transport_equipment: List[TransportEquipment] = field(
        default_factory=list,
        metadata={
            "name": "TransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    supported_transport_equipment: List[SupportedTransportEquipment] = field(
        default_factory=list,
        metadata={
            "name": "SupportedTransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    unsupported_transport_equipment: List[UnsupportedTransportEquipment] = field(
        default_factory=list,
        metadata={
            "name": "UnsupportedTransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    commodity_classification: List[CommodityClassification] = field(
        default_factory=list,
        metadata={
            "name": "CommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    supported_commodity_classification: List[SupportedCommodityClassification] = field(
        default_factory=list,
        metadata={
            "name": "SupportedCommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    unsupported_commodity_classification: List[UnsupportedCommodityClassification] = field(
        default_factory=list,
        metadata={
            "name": "UnsupportedCommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    total_capacity_dimension: Optional[TotalCapacityDimension] = field(
        default=None,
        metadata={
            "name": "TotalCapacityDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shipment_stage: List[ShipmentStage] = field(
        default_factory=list,
        metadata={
            "name": "ShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_event: List[TransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "TransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    responsible_transport_service_provider_party: Optional[ResponsibleTransportServiceProviderParty] = field(
        default=None,
        metadata={
            "name": "ResponsibleTransportServiceProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    environmental_emission: List[EnvironmentalEmission] = field(
        default_factory=list,
        metadata={
            "name": "EnvironmentalEmission",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    estimated_duration_period: Optional[EstimatedDurationPeriod] = field(
        default=None,
        metadata={
            "name": "EstimatedDurationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    scheduled_service_frequency: List[ScheduledServiceFrequency] = field(
        default_factory=list,
        metadata={
            "name": "ScheduledServiceFrequency",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AdditionalTransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class FinalDeliveryTransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class MainTransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OriginalDespatchTransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsignmentType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    carrier_assigned_id: Optional[CarrierAssignedId] = field(
        default=None,
        metadata={
            "name": "CarrierAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consignee_assigned_id: Optional[ConsigneeAssignedId] = field(
        default=None,
        metadata={
            "name": "ConsigneeAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consignor_assigned_id: Optional[ConsignorAssignedId] = field(
        default=None,
        metadata={
            "name": "ConsignorAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    freight_forwarder_assigned_id: Optional[FreightForwarderAssignedId] = field(
        default=None,
        metadata={
            "name": "FreightForwarderAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    broker_assigned_id: Optional[BrokerAssignedId] = field(
        default=None,
        metadata={
            "name": "BrokerAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contracted_carrier_assigned_id: Optional[ContractedCarrierAssignedId] = field(
        default=None,
        metadata={
            "name": "ContractedCarrierAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    performing_carrier_assigned_id: Optional[PerformingCarrierAssignedId] = field(
        default=None,
        metadata={
            "name": "PerformingCarrierAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    summary_description: List[SummaryDescription] = field(
        default_factory=list,
        metadata={
            "name": "SummaryDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_invoice_amount: Optional[TotalInvoiceAmount] = field(
        default=None,
        metadata={
            "name": "TotalInvoiceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declared_customs_value_amount: Optional[DeclaredCustomsValueAmount] = field(
        default=None,
        metadata={
            "name": "DeclaredCustomsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tariff_description: List[TariffDescription] = field(
        default_factory=list,
        metadata={
            "name": "TariffDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tariff_code: Optional[TariffCode] = field(
        default=None,
        metadata={
            "name": "TariffCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    insurance_premium_amount: Optional[InsurancePremiumAmount] = field(
        default=None,
        metadata={
            "name": "InsurancePremiumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gross_weight_measure: Optional[GrossWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_weight_measure: Optional[NetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_net_weight_measure: Optional[NetNetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    chargeable_weight_measure: Optional[ChargeableWeightMeasure] = field(
        default=None,
        metadata={
            "name": "ChargeableWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gross_volume_measure: Optional[GrossVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_volume_measure: Optional[NetVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    loading_length_measure: Optional[LoadingLengthMeasure] = field(
        default=None,
        metadata={
            "name": "LoadingLengthMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    remarks: List[Remarks] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    hazardous_risk_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    animal_food_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AnimalFoodIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    human_food_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HumanFoodIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    livestock_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LivestockIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    bulk_cargo_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BulkCargoIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    containerized_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContainerizedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    general_cargo_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GeneralCargoIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    special_security_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SpecialSecurityIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    third_party_payer_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ThirdPartyPayerIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    carrier_service_instructions: List[CarrierServiceInstructions] = field(
        default_factory=list,
        metadata={
            "name": "CarrierServiceInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    customs_clearance_service_instructions: List[CustomsClearanceServiceInstructions] = field(
        default_factory=list,
        metadata={
            "name": "CustomsClearanceServiceInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    forwarder_service_instructions: List[ForwarderServiceInstructions] = field(
        default_factory=list,
        metadata={
            "name": "ForwarderServiceInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    special_service_instructions: List[SpecialServiceInstructions] = field(
        default_factory=list,
        metadata={
            "name": "SpecialServiceInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    sequence_id: Optional[SequenceId] = field(
        default=None,
        metadata={
            "name": "SequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    shipping_priority_level_code: Optional[ShippingPriorityLevelCode] = field(
        default=None,
        metadata={
            "name": "ShippingPriorityLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    handling_code: Optional[HandlingCode] = field(
        default=None,
        metadata={
            "name": "HandlingCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    handling_instructions: List[HandlingInstructions] = field(
        default_factory=list,
        metadata={
            "name": "HandlingInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    information: List[Information] = field(
        default_factory=list,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_goods_item_quantity: Optional[TotalGoodsItemQuantity] = field(
        default=None,
        metadata={
            "name": "TotalGoodsItemQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_transport_handling_unit_quantity: Optional[TotalTransportHandlingUnitQuantity] = field(
        default=None,
        metadata={
            "name": "TotalTransportHandlingUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    insurance_value_amount: Optional[InsuranceValueAmount] = field(
        default=None,
        metadata={
            "name": "InsuranceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declared_for_carriage_value_amount: Optional[DeclaredForCarriageValueAmount] = field(
        default=None,
        metadata={
            "name": "DeclaredForCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declared_statistics_value_amount: Optional[DeclaredStatisticsValueAmount] = field(
        default=None,
        metadata={
            "name": "DeclaredStatisticsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    free_on_board_value_amount: Optional[FreeOnBoardValueAmount] = field(
        default=None,
        metadata={
            "name": "FreeOnBoardValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    special_instructions: List[SpecialInstructions] = field(
        default_factory=list,
        metadata={
            "name": "SpecialInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    split_consignment_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SplitConsignmentIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    delivery_instructions: List[DeliveryInstructions] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consignment_quantity: Optional[ConsignmentQuantity] = field(
        default=None,
        metadata={
            "name": "ConsignmentQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consolidatable_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConsolidatableIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    haulage_instructions: List[HaulageInstructions] = field(
        default_factory=list,
        metadata={
            "name": "HaulageInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    loading_sequence_id: Optional[LoadingSequenceId] = field(
        default=None,
        metadata={
            "name": "LoadingSequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    child_consignment_quantity: Optional[ChildConsignmentQuantity] = field(
        default=None,
        metadata={
            "name": "ChildConsignmentQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_packages_quantity: Optional[TotalPackagesQuantity] = field(
        default=None,
        metadata={
            "name": "TotalPackagesQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consolidated_shipment: List["ConsolidatedShipment"] = field(
        default_factory=list,
        metadata={
            "name": "ConsolidatedShipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    customs_declaration: List[CustomsDeclaration] = field(
        default_factory=list,
        metadata={
            "name": "CustomsDeclaration",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    requested_pickup_transport_event: Optional[RequestedPickupTransportEvent] = field(
        default=None,
        metadata={
            "name": "RequestedPickupTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    requested_delivery_transport_event: Optional[RequestedDeliveryTransportEvent] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    planned_pickup_transport_event: Optional[PlannedPickupTransportEvent] = field(
        default=None,
        metadata={
            "name": "PlannedPickupTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    planned_delivery_transport_event: Optional[PlannedDeliveryTransportEvent] = field(
        default=None,
        metadata={
            "name": "PlannedDeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    status: List[Status] = field(
        default_factory=list,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    child_consignment: List["ChildConsignment"] = field(
        default_factory=list,
        metadata={
            "name": "ChildConsignment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    consignee_party: Optional[ConsigneeParty] = field(
        default=None,
        metadata={
            "name": "ConsigneeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    exporter_party: Optional[ExporterParty] = field(
        default=None,
        metadata={
            "name": "ExporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    consignor_party: Optional[ConsignorParty] = field(
        default=None,
        metadata={
            "name": "ConsignorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    importer_party: Optional[ImporterParty] = field(
        default=None,
        metadata={
            "name": "ImporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    carrier_party: Optional[CarrierParty] = field(
        default=None,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    freight_forwarder_party: Optional[FreightForwarderParty] = field(
        default=None,
        metadata={
            "name": "FreightForwarderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    notify_party: Optional[NotifyParty] = field(
        default=None,
        metadata={
            "name": "NotifyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    original_despatch_party: Optional[OriginalDespatchParty] = field(
        default=None,
        metadata={
            "name": "OriginalDespatchParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    final_delivery_party: Optional[FinalDeliveryParty] = field(
        default=None,
        metadata={
            "name": "FinalDeliveryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    performing_carrier_party: Optional[PerformingCarrierParty] = field(
        default=None,
        metadata={
            "name": "PerformingCarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    substitute_carrier_party: Optional[SubstituteCarrierParty] = field(
        default=None,
        metadata={
            "name": "SubstituteCarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    logistics_operator_party: Optional[LogisticsOperatorParty] = field(
        default=None,
        metadata={
            "name": "LogisticsOperatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_advisor_party: Optional[TransportAdvisorParty] = field(
        default=None,
        metadata={
            "name": "TransportAdvisorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    hazardous_item_notification_party: Optional[HazardousItemNotificationParty] = field(
        default=None,
        metadata={
            "name": "HazardousItemNotificationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    insurance_party: Optional[InsuranceParty] = field(
        default=None,
        metadata={
            "name": "InsuranceParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    mortgage_holder_party: Optional[MortgageHolderParty] = field(
        default=None,
        metadata={
            "name": "MortgageHolderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    bill_of_lading_holder_party: Optional[BillOfLadingHolderParty] = field(
        default=None,
        metadata={
            "name": "BillOfLadingHolderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    original_departure_country: Optional[OriginalDepartureCountry] = field(
        default=None,
        metadata={
            "name": "OriginalDepartureCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    final_destination_country: Optional[FinalDestinationCountry] = field(
        default=None,
        metadata={
            "name": "FinalDestinationCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transit_country: List[TransitCountry] = field(
        default_factory=list,
        metadata={
            "name": "TransitCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_contract: Optional["TransportContract"] = field(
        default=None,
        metadata={
            "name": "TransportContract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_event: List[TransportEvent] = field(
        default_factory=list,
        metadata={
            "name": "TransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    original_despatch_transportation_service: Optional[OriginalDespatchTransportationService] = field(
        default=None,
        metadata={
            "name": "OriginalDespatchTransportationService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    final_delivery_transportation_service: Optional[FinalDeliveryTransportationService] = field(
        default=None,
        metadata={
            "name": "FinalDeliveryTransportationService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_terms: Optional[DeliveryTerms] = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_terms: Optional[PaymentTerms] = field(
        default=None,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    collect_payment_terms: Optional[CollectPaymentTerms] = field(
        default=None,
        metadata={
            "name": "CollectPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    disbursement_payment_terms: Optional[DisbursementPaymentTerms] = field(
        default=None,
        metadata={
            "name": "DisbursementPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    prepaid_payment_terms: Optional[PrepaidPaymentTerms] = field(
        default=None,
        metadata={
            "name": "PrepaidPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    freight_allowance_charge: List[FreightAllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    extra_allowance_charge: List[ExtraAllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "ExtraAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    main_carriage_shipment_stage: List[MainCarriageShipmentStage] = field(
        default_factory=list,
        metadata={
            "name": "MainCarriageShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pre_carriage_shipment_stage: List[PreCarriageShipmentStage] = field(
        default_factory=list,
        metadata={
            "name": "PreCarriageShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    on_carriage_shipment_stage: List[OnCarriageShipmentStage] = field(
        default_factory=list,
        metadata={
            "name": "OnCarriageShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_handling_unit: List[TransportHandlingUnit] = field(
        default_factory=list,
        metadata={
            "name": "TransportHandlingUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    first_arrival_port_location: Optional[FirstArrivalPortLocation] = field(
        default=None,
        metadata={
            "name": "FirstArrivalPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    last_exit_port_location: Optional[LastExitPortLocation] = field(
        default=None,
        metadata={
            "name": "LastExitPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ChildConsignment(ConsignmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Consignment(ConsignmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReferencedConsignment(ConsignmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ShipmentType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    shipping_priority_level_code: Optional[ShippingPriorityLevelCode] = field(
        default=None,
        metadata={
            "name": "ShippingPriorityLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    handling_code: Optional[HandlingCode] = field(
        default=None,
        metadata={
            "name": "HandlingCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    handling_instructions: List[HandlingInstructions] = field(
        default_factory=list,
        metadata={
            "name": "HandlingInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    information: List[Information] = field(
        default_factory=list,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gross_weight_measure: Optional[GrossWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_weight_measure: Optional[NetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_net_weight_measure: Optional[NetNetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    gross_volume_measure: Optional[GrossVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    net_volume_measure: Optional[NetVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_goods_item_quantity: Optional[TotalGoodsItemQuantity] = field(
        default=None,
        metadata={
            "name": "TotalGoodsItemQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_transport_handling_unit_quantity: Optional[TotalTransportHandlingUnitQuantity] = field(
        default=None,
        metadata={
            "name": "TotalTransportHandlingUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    insurance_value_amount: Optional[InsuranceValueAmount] = field(
        default=None,
        metadata={
            "name": "InsuranceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declared_customs_value_amount: Optional[DeclaredCustomsValueAmount] = field(
        default=None,
        metadata={
            "name": "DeclaredCustomsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declared_for_carriage_value_amount: Optional[DeclaredForCarriageValueAmount] = field(
        default=None,
        metadata={
            "name": "DeclaredForCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    declared_statistics_value_amount: Optional[DeclaredStatisticsValueAmount] = field(
        default=None,
        metadata={
            "name": "DeclaredStatisticsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    free_on_board_value_amount: Optional[FreeOnBoardValueAmount] = field(
        default=None,
        metadata={
            "name": "FreeOnBoardValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    special_instructions: List[SpecialInstructions] = field(
        default_factory=list,
        metadata={
            "name": "SpecialInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    delivery_instructions: List[DeliveryInstructions] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    split_consignment_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SplitConsignmentIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consignment_quantity: Optional[ConsignmentQuantity] = field(
        default=None,
        metadata={
            "name": "ConsignmentQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consignment: List[Consignment] = field(
        default_factory=list,
        metadata={
            "name": "Consignment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    goods_item: List[GoodsItem] = field(
        default_factory=list,
        metadata={
            "name": "GoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shipment_stage: List[ShipmentStage] = field(
        default_factory=list,
        metadata={
            "name": "ShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery: Optional["Delivery"] = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    transport_handling_unit: List[TransportHandlingUnit] = field(
        default_factory=list,
        metadata={
            "name": "TransportHandlingUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    return_address: Optional[ReturnAddress] = field(
        default=None,
        metadata={
            "name": "ReturnAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    origin_address: Optional[OriginAddress] = field(
        default=None,
        metadata={
            "name": "OriginAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    first_arrival_port_location: Optional[FirstArrivalPortLocation] = field(
        default=None,
        metadata={
            "name": "FirstArrivalPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    last_exit_port_location: Optional[LastExitPortLocation] = field(
        default=None,
        metadata={
            "name": "LastExitPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    export_country: Optional[ExportCountry] = field(
        default=None,
        metadata={
            "name": "ExportCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    freight_allowance_charge: List[FreightAllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TransportationSegmentType:
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    transport_execution_plan_reference_id: Optional[TransportExecutionPlanReferenceId] = field(
        default=None,
        metadata={
            "name": "TransportExecutionPlanReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    transportation_service: Optional[TransportationService] = field(
        default=None,
        metadata={
            "name": "TransportationService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    transport_service_provider_party: Optional[TransportServiceProviderParty] = field(
        default=None,
        metadata={
            "name": "TransportServiceProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    referenced_consignment: Optional[ReferencedConsignment] = field(
        default=None,
        metadata={
            "name": "ReferencedConsignment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shipment_stage: List[ShipmentStage] = field(
        default_factory=list,
        metadata={
            "name": "ShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ConsolidatedShipment(ShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReferencedShipment(ShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReportedShipment(ShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Shipment(ShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportationSegment(TransportationSegmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CertificateOfOriginApplicationType:
    reference_id: Optional[ReferenceId] = field(
        default=None,
        metadata={
            "name": "ReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    certificate_type: Optional[UblCommonBasicComponents21CertificateType] = field(
        default=None,
        metadata={
            "name": "CertificateType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    application_status_code: Optional[ApplicationStatusCode] = field(
        default=None,
        metadata={
            "name": "ApplicationStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    original_job_id: Optional[OriginalJobId] = field(
        default=None,
        metadata={
            "name": "OriginalJobID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    previous_job_id: Optional[PreviousJobId] = field(
        default=None,
        metadata={
            "name": "PreviousJobID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    remarks: List[Remarks] = field(
        default_factory=list,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    shipment: Optional[Shipment] = field(
        default=None,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    endorser_party: List[EndorserParty] = field(
        default_factory=list,
        metadata={
            "name": "EndorserParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )
    preparation_party: Optional[PreparationParty] = field(
        default=None,
        metadata={
            "name": "PreparationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    exporter_party: Optional[ExporterParty] = field(
        default=None,
        metadata={
            "name": "ExporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    importer_party: Optional[ImporterParty] = field(
        default=None,
        metadata={
            "name": "ImporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    issuing_country: Optional[IssuingCountry] = field(
        default=None,
        metadata={
            "name": "IssuingCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    document_distribution: List[DocumentDistribution] = field(
        default_factory=list,
        metadata={
            "name": "DocumentDistribution",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    supporting_document_reference: List[SupportingDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "SupportingDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    signature: List[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class DeliveryType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    actual_delivery_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ActualDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    actual_delivery_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ActualDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latest_delivery_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LatestDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    latest_delivery_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    release_id: Optional[ReleaseId] = field(
        default=None,
        metadata={
            "name": "ReleaseID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tracking_id: Optional[TrackingId] = field(
        default=None,
        metadata={
            "name": "TrackingID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    delivery_address: Optional[DeliveryAddress] = field(
        default=None,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_location: Optional[DeliveryLocation] = field(
        default=None,
        metadata={
            "name": "DeliveryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    alternative_delivery_location: Optional[AlternativeDeliveryLocation] = field(
        default=None,
        metadata={
            "name": "AlternativeDeliveryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    requested_delivery_period: Optional[RequestedDeliveryPeriod] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    promised_delivery_period: Optional[PromisedDeliveryPeriod] = field(
        default=None,
        metadata={
            "name": "PromisedDeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    estimated_delivery_period: Optional[EstimatedDeliveryPeriod] = field(
        default=None,
        metadata={
            "name": "EstimatedDeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    carrier_party: Optional[CarrierParty] = field(
        default=None,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_party: Optional[DeliveryParty] = field(
        default=None,
        metadata={
            "name": "DeliveryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    notify_party: List[NotifyParty] = field(
        default_factory=list,
        metadata={
            "name": "NotifyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch: Optional[Despatch] = field(
        default=None,
        metadata={
            "name": "Despatch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_terms: List[DeliveryTerms] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    minimum_delivery_unit: Optional[MinimumDeliveryUnit] = field(
        default=None,
        metadata={
            "name": "MinimumDeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    maximum_delivery_unit: Optional[MaximumDeliveryUnit] = field(
        default=None,
        metadata={
            "name": "MaximumDeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    shipment: Optional[Shipment] = field(
        default=None,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class OrderedShipmentType:
    shipment: Optional[Shipment] = field(
        default=None,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    package: List[Package] = field(
        default_factory=list,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CertificateOfOriginApplication(CertificateOfOriginApplicationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractualDelivery(DeliveryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Delivery(DeliveryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OrderedShipment(OrderedShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ContractType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    nomination_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "NominationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    nomination_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "NominationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contract_type_code: Optional[ContractTypeCode] = field(
        default=None,
        metadata={
            "name": "ContractTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contract_type: Optional[UblCommonBasicComponents21ContractType] = field(
        default=None,
        metadata={
            "name": "ContractType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    version_id: Optional[VersionId] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contract_document_reference: List[ContractDocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "ContractDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    nomination_period: Optional[NominationPeriod] = field(
        default=None,
        metadata={
            "name": "NominationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contractual_delivery: Optional[ContractualDelivery] = field(
        default=None,
        metadata={
            "name": "ContractualDelivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class Contract(ContractType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ForeignExchangeContract(ContractType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReferencedContract(ContractType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TransportContract(ContractType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ExchangeRateType:
    source_currency_code: Optional[SourceCurrencyCode] = field(
        default=None,
        metadata={
            "name": "SourceCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    source_currency_base_rate: Optional[SourceCurrencyBaseRate] = field(
        default=None,
        metadata={
            "name": "SourceCurrencyBaseRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    target_currency_code: Optional[TargetCurrencyCode] = field(
        default=None,
        metadata={
            "name": "TargetCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    target_currency_base_rate: Optional[TargetCurrencyBaseRate] = field(
        default=None,
        metadata={
            "name": "TargetCurrencyBaseRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    exchange_market_id: Optional[ExchangeMarketId] = field(
        default=None,
        metadata={
            "name": "ExchangeMarketID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    calculation_rate: Optional[CalculationRate] = field(
        default=None,
        metadata={
            "name": "CalculationRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    mathematic_operator_code: Optional[MathematicOperatorCode] = field(
        default=None,
        metadata={
            "name": "MathematicOperatorCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    foreign_exchange_contract: Optional[ForeignExchangeContract] = field(
        default=None,
        metadata={
            "name": "ForeignExchangeContract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class TenderResultType:
    tender_result_code: Optional[TenderResultCode] = field(
        default=None,
        metadata={
            "name": "TenderResultCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    advertisement_amount: Optional[AdvertisementAmount] = field(
        default=None,
        metadata={
            "name": "AdvertisementAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    award_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "AwardDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    award_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "AwardTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    received_tender_quantity: Optional[ReceivedTenderQuantity] = field(
        default=None,
        metadata={
            "name": "ReceivedTenderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    lower_tender_amount: Optional[LowerTenderAmount] = field(
        default=None,
        metadata={
            "name": "LowerTenderAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    higher_tender_amount: Optional[HigherTenderAmount] = field(
        default=None,
        metadata={
            "name": "HigherTenderAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    received_electronic_tender_quantity: Optional[ReceivedElectronicTenderQuantity] = field(
        default=None,
        metadata={
            "name": "ReceivedElectronicTenderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    received_foreign_tender_quantity: Optional[ReceivedForeignTenderQuantity] = field(
        default=None,
        metadata={
            "name": "ReceivedForeignTenderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    contract: Optional[Contract] = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    awarded_tendered_project: Optional[AwardedTenderedProject] = field(
        default=None,
        metadata={
            "name": "AwardedTenderedProject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contract_formalization_period: Optional[ContractFormalizationPeriod] = field(
        default=None,
        metadata={
            "name": "ContractFormalizationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    subcontract_terms: List[SubcontractTerms] = field(
        default_factory=list,
        metadata={
            "name": "SubcontractTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    winning_party: List[WinningParty] = field(
        default_factory=list,
        metadata={
            "name": "WinningParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class UtilityItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    subscriber_id: Optional[SubscriberId] = field(
        default=None,
        metadata={
            "name": "SubscriberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    subscriber_type: Optional[SubscriberType] = field(
        default=None,
        metadata={
            "name": "SubscriberType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    subscriber_type_code: Optional[SubscriberTypeCode] = field(
        default=None,
        metadata={
            "name": "SubscriberTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pack_quantity: Optional[PackQuantity] = field(
        default=None,
        metadata={
            "name": "PackQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pack_size_numeric: Optional[PackSizeNumeric] = field(
        default=None,
        metadata={
            "name": "PackSizeNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumption_type: Optional[UblCommonBasicComponents21ConsumptionType] = field(
        default=None,
        metadata={
            "name": "ConsumptionType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    consumption_type_code: Optional[ConsumptionTypeCode] = field(
        default=None,
        metadata={
            "name": "ConsumptionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    current_charge_type: Optional[CurrentChargeType] = field(
        default=None,
        metadata={
            "name": "CurrentChargeType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    current_charge_type_code: Optional[CurrentChargeTypeCode] = field(
        default=None,
        metadata={
            "name": "CurrentChargeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    one_time_charge_type: Optional[OneTimeChargeType] = field(
        default=None,
        metadata={
            "name": "OneTimeChargeType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    one_time_charge_type_code: Optional[OneTimeChargeTypeCode] = field(
        default=None,
        metadata={
            "name": "OneTimeChargeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_category: Optional[TaxCategory] = field(
        default=None,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    contract: Optional[Contract] = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PaymentAlternativeExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PaymentExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PricingExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TaxExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TenderResult(TenderResultType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class UtilityItem(UtilityItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class PriceType:
    price_amount: Optional[PriceAmount] = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    base_quantity: Optional[BaseQuantity] = field(
        default=None,
        metadata={
            "name": "BaseQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    price_change_reason: List[PriceChangeReason] = field(
        default_factory=list,
        metadata={
            "name": "PriceChangeReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    price_type_code: Optional[PriceTypeCode] = field(
        default=None,
        metadata={
            "name": "PriceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    price_type: Optional[UblCommonBasicComponents21PriceType] = field(
        default=None,
        metadata={
            "name": "PriceType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    orderable_unit_factor_rate: Optional[OrderableUnitFactorRate] = field(
        default=None,
        metadata={
            "name": "OrderableUnitFactorRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    validity_period: List[ValidityPeriod] = field(
        default_factory=list,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    price_list: Optional[PriceList] = field(
        default=None,
        metadata={
            "name": "PriceList",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pricing_exchange_rate: Optional[PricingExchangeRate] = field(
        default=None,
        metadata={
            "name": "PricingExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ReminderLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    balance_brought_forward_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BalanceBroughtForwardIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    debit_line_amount: Optional[DebitLineAmount] = field(
        default=None,
        metadata={
            "name": "DebitLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    credit_line_amount: Optional[CreditLineAmount] = field(
        default=None,
        metadata={
            "name": "CreditLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    penalty_surcharge_percent: Optional[PenaltySurchargePercent] = field(
        default=None,
        metadata={
            "name": "PenaltySurchargePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    reminder_period: List[ReminderPeriod] = field(
        default_factory=list,
        metadata={
            "name": "ReminderPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    billing_reference: List[BillingReference] = field(
        default_factory=list,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    exchange_rate: Optional[ExchangeRate] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class RemittanceAdviceLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    debit_line_amount: Optional[DebitLineAmount] = field(
        default=None,
        metadata={
            "name": "DebitLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    credit_line_amount: Optional[CreditLineAmount] = field(
        default=None,
        metadata={
            "name": "CreditLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    balance_amount: Optional[BalanceAmount] = field(
        default=None,
        metadata={
            "name": "BalanceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    invoicing_party_reference: Optional[InvoicingPartyReference] = field(
        default=None,
        metadata={
            "name": "InvoicingPartyReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_supplier_party: Optional[AccountingSupplierParty] = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    accounting_customer_party: Optional[AccountingCustomerParty] = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    buyer_customer_party: Optional[BuyerCustomerParty] = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    originator_customer_party: Optional[OriginatorCustomerParty] = field(
        default=None,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payee_party: Optional[PayeeParty] = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    invoice_period: List[InvoicePeriod] = field(
        default_factory=list,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    billing_reference: List[BillingReference] = field(
        default_factory=list,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    exchange_rate: Optional[ExchangeRate] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class StatementLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    balance_brought_forward_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BalanceBroughtForwardIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    debit_line_amount: Optional[DebitLineAmount] = field(
        default=None,
        metadata={
            "name": "DebitLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    credit_line_amount: Optional[CreditLineAmount] = field(
        default=None,
        metadata={
            "name": "CreditLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    balance_amount: Optional[BalanceAmount] = field(
        default=None,
        metadata={
            "name": "BalanceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_means: Optional[PaymentMeans] = field(
        default=None,
        metadata={
            "name": "PaymentMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_terms: List[PaymentTerms] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    buyer_customer_party: Optional[BuyerCustomerParty] = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    originator_customer_party: Optional[OriginatorCustomerParty] = field(
        default=None,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    accounting_customer_party: Optional[AccountingCustomerParty] = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    accounting_supplier_party: Optional[AccountingSupplierParty] = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payee_party: Optional[PayeeParty] = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    invoice_period: List[InvoicePeriod] = field(
        default_factory=list,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    billing_reference: List[BillingReference] = field(
        default_factory=list,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    exchange_rate: Optional[ExchangeRate] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    collected_payment: List[CollectedPayment] = field(
        default_factory=list,
        metadata={
            "name": "CollectedPayment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AlternativeConditionPrice(PriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class Price(PriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ReminderLine(ReminderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RemittanceAdviceLine(RemittanceAdviceLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class StatementLine(StatementLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TaxExclusivePrice(PriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TaxInclusivePrice(PriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsumptionLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    parent_document_line_reference_id: Optional[ParentDocumentLineReferenceId] = field(
        default=None,
        metadata={
            "name": "ParentDocumentLineReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    invoiced_quantity: Optional[InvoicedQuantity] = field(
        default=None,
        metadata={
            "name": "InvoicedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery: List[Delivery] = field(
        default_factory=list,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    utility_item: Optional[UtilityItem] = field(
        default=None,
        metadata={
            "name": "UtilityItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    unstructured_price: Optional[UnstructuredPrice] = field(
        default=None,
        metadata={
            "name": "UnstructuredPrice",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class CreditNoteLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    credited_quantity: Optional[CreditedQuantity] = field(
        default=None,
        metadata={
            "name": "CreditedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    tax_point_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    free_of_charge_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeOfChargeIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    invoice_period: List[InvoicePeriod] = field(
        default_factory=list,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    order_line_reference: List[OrderLineReference] = field(
        default_factory=list,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    discrepancy_response: List[DiscrepancyResponse] = field(
        default_factory=list,
        metadata={
            "name": "DiscrepancyResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch_line_reference: List[DespatchLineReference] = field(
        default_factory=list,
        metadata={
            "name": "DespatchLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    receipt_line_reference: List[ReceiptLineReference] = field(
        default_factory=list,
        metadata={
            "name": "ReceiptLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    billing_reference: List[BillingReference] = field(
        default_factory=list,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pricing_reference: Optional[PricingReference] = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    originator_party: Optional[OriginatorParty] = field(
        default=None,
        metadata={
            "name": "OriginatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery: List[Delivery] = field(
        default_factory=list,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    payment_terms: List[PaymentTerms] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_terms: List[DeliveryTerms] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    sub_credit_note_line: List["SubCreditNoteLine"] = field(
        default_factory=list,
        metadata={
            "name": "SubCreditNoteLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item_price_extension: Optional[ItemPriceExtension] = field(
        default=None,
        metadata={
            "name": "ItemPriceExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class DebitNoteLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    debited_quantity: Optional[DebitedQuantity] = field(
        default=None,
        metadata={
            "name": "DebitedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    tax_point_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    discrepancy_response: List[DiscrepancyResponse] = field(
        default_factory=list,
        metadata={
            "name": "DiscrepancyResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    despatch_line_reference: List[DespatchLineReference] = field(
        default_factory=list,
        metadata={
            "name": "DespatchLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    receipt_line_reference: List[ReceiptLineReference] = field(
        default_factory=list,
        metadata={
            "name": "ReceiptLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    billing_reference: List[BillingReference] = field(
        default_factory=list,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pricing_reference: Optional[PricingReference] = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery: List[Delivery] = field(
        default_factory=list,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    sub_debit_note_line: List["SubDebitNoteLine"] = field(
        default_factory=list,
        metadata={
            "name": "SubDebitNoteLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class LineItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    sales_order_id: Optional[SalesOrderId] = field(
        default=None,
        metadata={
            "name": "SalesOrderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_status_code: Optional[LineStatusCode] = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_tax_amount: Optional[TotalTaxAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    minimum_backorder_quantity: Optional[MinimumBackorderQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumBackorderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    maximum_backorder_quantity: Optional[MaximumBackorderQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumBackorderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    inspection_method_code: Optional[InspectionMethodCode] = field(
        default=None,
        metadata={
            "name": "InspectionMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    partial_delivery_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PartialDeliveryIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    back_order_allowed_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BackOrderAllowedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    warranty_information: List[WarrantyInformation] = field(
        default_factory=list,
        metadata={
            "name": "WarrantyInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    delivery: List[Delivery] = field(
        default_factory=list,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    delivery_terms: Optional[DeliveryTerms] = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    originator_party: Optional[OriginatorParty] = field(
        default=None,
        metadata={
            "name": "OriginatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    ordered_shipment: List[OrderedShipment] = field(
        default_factory=list,
        metadata={
            "name": "OrderedShipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    pricing_reference: Optional[PricingReference] = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    sub_line_item: List["SubLineItem"] = field(
        default_factory=list,
        metadata={
            "name": "SubLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    warranty_party: Optional[WarrantyParty] = field(
        default=None,
        metadata={
            "name": "WarrantyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item_price_extension: Optional[ItemPriceExtension] = field(
        default=None,
        metadata={
            "name": "ItemPriceExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    line_reference: List[LineReference] = field(
        default_factory=list,
        metadata={
            "name": "LineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class SalesItemType:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    activity_property: List[ActivityProperty] = field(
        default_factory=list,
        metadata={
            "name": "ActivityProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_exclusive_price: List[TaxExclusivePrice] = field(
        default_factory=list,
        metadata={
            "name": "TaxExclusivePrice",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_inclusive_price: List[TaxInclusivePrice] = field(
        default_factory=list,
        metadata={
            "name": "TaxInclusivePrice",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class TelecommunicationsServiceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    call_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CallDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    call_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "CallTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    service_number_called: Optional[ServiceNumberCalled] = field(
        default=None,
        metadata={
            "name": "ServiceNumberCalled",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    telecommunications_service_category: Optional[TelecommunicationsServiceCategory] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    telecommunications_service_category_code: Optional[TelecommunicationsServiceCategoryCode] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCategoryCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    movie_title: Optional[MovieTitle] = field(
        default=None,
        metadata={
            "name": "MovieTitle",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    roaming_partner_name: Optional[RoamingPartnerName] = field(
        default=None,
        metadata={
            "name": "RoamingPartnerName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    pay_per_view: Optional[PayPerView] = field(
        default=None,
        metadata={
            "name": "PayPerView",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    telecommunications_service_call: Optional[TelecommunicationsServiceCall] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCall",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    telecommunications_service_call_code: Optional[TelecommunicationsServiceCallCode] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCallCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    call_base_amount: Optional[CallBaseAmount] = field(
        default=None,
        metadata={
            "name": "CallBaseAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    call_extension_amount: Optional[CallExtensionAmount] = field(
        default=None,
        metadata={
            "name": "CallExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    exchange_rate: List[ExchangeRate] = field(
        default_factory=list,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    call_duty: List[CallDuty] = field(
        default_factory=list,
        metadata={
            "name": "CallDuty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    time_duty: List[TimeDuty] = field(
        default_factory=list,
        metadata={
            "name": "TimeDuty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class AlternativeLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class BuyerProposedSubstituteLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsumptionLine(ConsumptionLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class CreditNoteLine(CreditNoteLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class DebitNoteLine(DebitNoteLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class LineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SalesItem(SalesItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SellerProposedSubstituteLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SellerSubstitutedLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubCreditNoteLine(CreditNoteLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubDebitNoteLine(DebitNoteLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TelecommunicationsService(TelecommunicationsServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ActivityDataLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    supply_chain_activity_type_code: Optional[SupplyChainActivityTypeCode] = field(
        default=None,
        metadata={
            "name": "SupplyChainActivityTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    buyer_customer_party: Optional[BuyerCustomerParty] = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    activity_period: Optional[ActivityPeriod] = field(
        default=None,
        metadata={
            "name": "ActivityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    activity_origin_location: Optional[ActivityOriginLocation] = field(
        default=None,
        metadata={
            "name": "ActivityOriginLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    activity_final_location: Optional[ActivityFinalLocation] = field(
        default=None,
        metadata={
            "name": "ActivityFinalLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    sales_item: List[SalesItem] = field(
        default_factory=list,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class ForecastLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    frozen_document_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FrozenDocumentIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    forecast_period: Optional[ForecastPeriod] = field(
        default=None,
        metadata={
            "name": "ForecastPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    sales_item: Optional[SalesItem] = field(
        default=None,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ForecastRevisionLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    revised_forecast_line_id: Optional[RevisedForecastLineId] = field(
        default=None,
        metadata={
            "name": "RevisedForecastLineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    source_forecast_issue_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SourceForecastIssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    source_forecast_issue_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "SourceForecastIssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    adjustment_reason_code: Optional[AdjustmentReasonCode] = field(
        default=None,
        metadata={
            "name": "AdjustmentReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    forecast_period: Optional[ForecastPeriod] = field(
        default=None,
        metadata={
            "name": "ForecastPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    sales_item: Optional[SalesItem] = field(
        default=None,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class ItemInformationRequestLineType:
    time_frequency_code: Optional[TimeFrequencyCode] = field(
        default=None,
        metadata={
            "name": "TimeFrequencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    supply_chain_activity_type_code: Optional[SupplyChainActivityTypeCode] = field(
        default=None,
        metadata={
            "name": "SupplyChainActivityTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    performance_metric_type_code: Optional[PerformanceMetricTypeCode] = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    period: List[Period] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )
    sales_item: List[SalesItem] = field(
        default_factory=list,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderLineType:
    substitution_status_code: Optional[SubstitutionStatusCode] = field(
        default=None,
        metadata={
            "name": "SubstitutionStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_item: Optional[LineItem] = field(
        default=None,
        metadata={
            "name": "LineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    seller_proposed_substitute_line_item: List[SellerProposedSubstituteLineItem] = field(
        default_factory=list,
        metadata={
            "name": "SellerProposedSubstituteLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    seller_substituted_line_item: List[SellerSubstitutedLineItem] = field(
        default_factory=list,
        metadata={
            "name": "SellerSubstitutedLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    buyer_proposed_substitute_line_item: List[BuyerProposedSubstituteLineItem] = field(
        default_factory=list,
        metadata={
            "name": "BuyerProposedSubstituteLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    catalogue_line_reference: Optional[CatalogueLineReference] = field(
        default=None,
        metadata={
            "name": "CatalogueLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    quotation_line_reference: Optional[QuotationLineReference] = field(
        default=None,
        metadata={
            "name": "QuotationLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    order_line_reference: List[OrderLineReference] = field(
        default_factory=list,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class QuotationLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_tax_amount: Optional[TotalTaxAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    request_for_quotation_line_id: Optional[RequestForQuotationLineId] = field(
        default=None,
        metadata={
            "name": "RequestForQuotationLineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    line_item: Optional[LineItem] = field(
        default=None,
        metadata={
            "name": "LineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    seller_proposed_substitute_line_item: List[SellerProposedSubstituteLineItem] = field(
        default_factory=list,
        metadata={
            "name": "SellerProposedSubstituteLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    alternative_line_item: List[AlternativeLineItem] = field(
        default_factory=list,
        metadata={
            "name": "AlternativeLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    request_line_reference: Optional[RequestLineReference] = field(
        default=None,
        metadata={
            "name": "RequestLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class RequestForQuotationLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    optional_line_item_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OptionalLineItemIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    privacy_code: Optional[PrivacyCode] = field(
        default=None,
        metadata={
            "name": "PrivacyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    security_classification_code: Optional[SecurityClassificationCode] = field(
        default=None,
        metadata={
            "name": "SecurityClassificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    document_reference: List[DocumentReference] = field(
        default_factory=list,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    line_item: Optional[LineItem] = field(
        default=None,
        metadata={
            "name": "LineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class TelecommunicationsSupplyLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    exchange_rate: List[ExchangeRate] = field(
        default_factory=list,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    telecommunications_service: List[TelecommunicationsService] = field(
        default_factory=list,
        metadata={
            "name": "TelecommunicationsService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class ActivityDataLine(ActivityDataLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ForecastLine(ForecastLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ForecastRevisionLine(ForecastRevisionLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ItemInformationRequestLine(ItemInformationRequestLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class OrderLine(OrderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class QuotationLine(QuotationLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class RequestForQuotationLine(RequestForQuotationLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SupplyChainActivityDataLine(ActivityDataLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TelecommunicationsSupplyLine(TelecommunicationsSupplyLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class TelecommunicationsSupplyType:
    telecommunications_supply_type: Optional[UblCommonBasicComponents21TelecommunicationsSupplyType] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsSupplyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    telecommunications_supply_type_code: Optional[TelecommunicationsSupplyTypeCode] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsSupplyTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    privacy_code: Optional[PrivacyCode] = field(
        default=None,
        metadata={
            "name": "PrivacyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        }
    )
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_amount: Optional[TotalAmount] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    telecommunications_supply_line: List[TelecommunicationsSupplyLine] = field(
        default_factory=list,
        metadata={
            "name": "TelecommunicationsSupplyLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class TelecommunicationsSupply(TelecommunicationsSupplyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class ConsumptionType:
    utility_statement_type_code: Optional[UtilityStatementTypeCode] = field(
        default=None,
        metadata={
            "name": "UtilityStatementTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    main_period: Optional[MainPeriod] = field(
        default=None,
        metadata={
            "name": "MainPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    allowance_charge: List[AllowanceCharge] = field(
        default_factory=list,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    tax_total: List[TaxTotal] = field(
        default_factory=list,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    energy_water_supply: Optional[EnergyWaterSupply] = field(
        default=None,
        metadata={
            "name": "EnergyWaterSupply",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    telecommunications_supply: Optional[TelecommunicationsSupply] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsSupply",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    legal_monetary_total: Optional[LegalMonetaryTotal] = field(
        default=None,
        metadata={
            "name": "LegalMonetaryTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )


@dataclass
class Consumption(ConsumptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SupplierConsumptionType:
    description: List[Description] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    utility_supplier_party: Optional[UtilitySupplierParty] = field(
        default=None,
        metadata={
            "name": "UtilitySupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    utility_customer_party: Optional[UtilityCustomerParty] = field(
        default=None,
        metadata={
            "name": "UtilityCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    consumption: Optional[Consumption] = field(
        default=None,
        metadata={
            "name": "Consumption",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    contract: Optional[Contract] = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    consumption_line: List[ConsumptionLine] = field(
        default_factory=list,
        metadata={
            "name": "ConsumptionLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        }
    )


@dataclass
class SupplierConsumption(SupplierConsumptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass
class SubscriberConsumptionType:
    consumption_id: Optional[ConsumptionId] = field(
        default=None,
        metadata={
            "name": "ConsumptionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    specification_type_code: Optional[SpecificationTypeCode] = field(
        default=None,
        metadata={
            "name": "SpecificationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    note: List[Note] = field(
        default_factory=list,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    total_metered_quantity: Optional[TotalMeteredQuantity] = field(
        default=None,
        metadata={
            "name": "TotalMeteredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        }
    )
    subscriber_party: Optional[SubscriberParty] = field(
        default=None,
        metadata={
            "name": "SubscriberParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    utility_consumption_point: Optional[UtilityConsumptionPoint] = field(
        default=None,
        metadata={
            "name": "UtilityConsumptionPoint",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        }
    )
    on_account_payment: List[OnAccountPayment] = field(
        default_factory=list,
        metadata={
            "name": "OnAccountPayment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    consumption: Optional[Consumption] = field(
        default=None,
        metadata={
            "name": "Consumption",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )
    supplier_consumption: List[SupplierConsumption] = field(
        default_factory=list,
        metadata={
            "name": "SupplierConsumption",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        }
    )


@dataclass
class SubscriberConsumption(SubscriberConsumptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
