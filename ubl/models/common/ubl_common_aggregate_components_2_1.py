from dataclasses import dataclass, field
from typing import Optional

from ubl.models.common.ubl_common_basic_components_2_1 import (
    AcceptedVariantsDescription,
    AccountFormatCode,
    AccountId,
    AccountingCost,
    AccountingCostCode,
    AccountTypeCode,
    ActionCode,
    ActivityType,
    ActivityTypeCode,
    ActualDeliveryDate,
    ActualDeliveryTime,
    ActualDespatchDate,
    ActualDespatchTime,
    ActualPickupDate,
    ActualPickupTime,
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
    AircraftId,
    AirFlowPercent,
    AliasName,
    AllowanceChargeReason,
    AllowanceChargeReasonCode,
    AllowanceTotalAmount,
    AltitudeMeasure,
    Amount,
    AmountRate,
    AnimalFoodApprovedIndicator,
    AnimalFoodIndicator,
    AnnualAverageAmount,
    ApplicationStatusCode,
    ApprovalStatus,
    AttributeId,
    AuctionConstraintIndicator,
    AuctionUri,
    AvailabilityDate,
    AvailabilityStatusCode,
    AverageAmount,
    AverageSubsequentContractAmount,
    AwardDate,
    AwardingCriterionDescription,
    AwardingCriterionId,
    AwardingCriterionTypeCode,
    AwardingMethodTypeCode,
    AwardTime,
    BackOrderAllowedIndicator,
    BackorderQuantity,
    BackorderReason,
    BalanceAmount,
    BalanceBroughtForwardIndicator,
    BarcodeSymbologyId,
    BaseAmount,
    BaseQuantity,
    BaseUnitMeasure,
    BasicConsumedQuantity,
    BatchQuantity,
    BestBeforeDate,
    BindingOnBuyerIndicator,
    BirthDate,
    BirthplaceName,
    BlockName,
    BrandName,
    BrokerAssignedId,
    BudgetYearNumeric,
    BuildingName,
    BuildingNumber,
    BulkCargoIndicator,
    BusinessClassificationEvidenceId,
    BusinessIdentityEvidenceId,
    BuyerProfileUri,
    CalculationExpression,
    CalculationExpressionCode,
    CalculationMethodCode,
    CalculationRate,
    CalculationSequenceNumeric,
    CallBaseAmount,
    CallDate,
    CallExtensionAmount,
    CallTime,
    CandidateReductionConstraintIndicator,
    CandidateStatement,
    CanonicalizationMethod,
    CapabilityTypeCode,
    CardChipCode,
    CardTypeCode,
    CargoTypeCode,
    CarrierAssignedId,
    CarrierServiceInstructions,
    CatalogueIndicator,
    CategoryName,
    CertificateTypeCode,
    ChangeConditions,
    Channel,
    ChannelCode,
    Characteristics,
    CharacterSetCode,
    ChargeableQuantity,
    ChargeableWeightMeasure,
    ChargeIndicator,
    ChargeTotalAmount,
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
    ComparisonForecastIssueDate,
    ComparisonForecastIssueTime,
    CompletionIndicator,
    ConditionCode,
    Conditions,
    ConditionsDescription,
    ConsigneeAssignedId,
    ConsignmentQuantity,
    ConsignorAssignedId,
    ConsolidatableIndicator,
    ConsumerIncentiveTacticTypeCode,
    ConsumersEnergyLevel,
    ConsumersEnergyLevelCode,
    ConsumerUnitQuantity,
    ConsumptionEnergyQuantity,
    ConsumptionId,
    ConsumptionLevel,
    ConsumptionLevelCode,
    ConsumptionReportId,
    ConsumptionTypeCode,
    ConsumptionWaterQuantity,
    ContainerizedIndicator,
    Content,
    ContentUnitQuantity,
    ContractedCarrierAssignedId,
    ContractingSystemCode,
    ContractSubdivision,
    ContractTypeCode,
    CoordinateSystemCode,
    CopyIndicator,
    CorporateRegistrationTypeCode,
    CorporateStockAmount,
    CorrectionAmount,
    CorrectionType,
    CorrectionTypeCode,
    CorrectionUnitAmount,
    CountrySubentity,
    CountrySubentityCode,
    CreditedQuantity,
    CreditLineAmount,
    CrewQuantity,
    CurrencyCode,
    CurrentChargeType,
    CurrentChargeTypeCode,
    CustomerAssignedAccountId,
    CustomerReference,
    CustomsClearanceServiceInstructions,
    CustomsImportClassifiedIndicator,
    CustomsStatusCode,
    CustomsTariffQuantity,
    Cv2Id,
    DamageRemarks,
    DangerousGoodsApprovedIndicator,
    DataSendingCapability,
    DataSourceCode,
    Date,
    DebitedQuantity,
    DebitLineAmount,
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
    DocumentationFeeAmount,
    DocumentDescription,
    DocumentHash,
    DocumentId,
    DocumentStatusCode,
    DocumentType,
    DocumentTypeCode,
    DurationMeasure,
    DutyCode,
    EarliestPickupDate,
    EarliestPickupTime,
    EconomicOperatorRegistryUri,
    EffectiveDate,
    EffectiveTime,
    ElectronicDeviceDescription,
    ElectronicMail,
    EmbeddedDocumentBinaryObject,
    EmergencyProceduresCode,
    EmployeeQuantity,
    EncodingCode,
    EndDate,
    EndpointId,
    EndTime,
    EnvironmentalEmissionTypeCode,
    EstimatedAmount,
    EstimatedConsumedQuantity,
    EstimatedDeliveryDate,
    EstimatedDeliveryTime,
    EstimatedDespatchDate,
    EstimatedDespatchTime,
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
    ExpiryDate,
    ExpiryTime,
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
    FirstShipmentAvailibilityDate,
    Floor,
    FollowupContractIndicator,
    ForecastPurposeCode,
    ForecastTypeCode,
    FormatCode,
    ForwarderServiceInstructions,
    FreeOfChargeIndicator,
    FreeOnBoardValueAmount,
    FreightForwarderAssignedId,
    FreightRateClassCode,
    Frequency,
    FrozenDocumentIndicator,
    FrozenPeriodDaysNumeric,
    FullnessIndicationCode,
    FullyPaidSharesIndicator,
    FundingProgram,
    FundingProgramCode,
    GasPressureQuantity,
    GenderCode,
    GeneralCargoIndicator,
    GovernmentAgreementConstraintIndicator,
    GrossTonnageMeasure,
    GrossVolumeMeasure,
    GrossWeightMeasure,
    GuaranteedDespatchDate,
    GuaranteedDespatchTime,
    GuaranteeTypeCode,
    HandlingCode,
    HandlingInstructions,
    HashAlgorithmMethod,
    HaulageInstructions,
    HazardClassId,
    HazardousCategoryCode,
    HazardousRegulationCode,
    HazardousRiskIndicator,
    HeatingType,
    HeatingTypeCode,
    HigherTenderAmount,
    HolderName,
    HumanFoodApprovedIndicator,
    HumanFoodIndicator,
    HumidityPercent,
    Id,
    IdentificationCode,
    IdentificationId,
    ImmobilizationCertificateId,
    ImportanceCode,
    IndicationIndicator,
    IndustryClassificationCode,
    Information,
    InformationUri,
    InhalationToxicityZoneCode,
    InhouseMail,
    InspectionMethodCode,
    InstallmentDueDate,
    InstructionId,
    InstructionNote,
    Instructions,
    InsurancePremiumAmount,
    InsuranceValueAmount,
    InventoryValueAmount,
    InvoicedQuantity,
    InvoicingPartyReference,
    IssueDate,
    IssueNumberId,
    IssuerId,
    IssueTime,
    ItemClassificationCode,
    JobTitle,
    JourneyId,
    Justification,
    JustificationDescription,
    Keyword,
    LanguageId,
    LastRevisionDate,
    LastRevisionTime,
    LatestDeliveryDate,
    LatestDeliveryTime,
    LatestMeterQuantity,
    LatestMeterReadingDate,
    LatestMeterReadingMethod,
    LatestMeterReadingMethodCode,
    LatestPickupDate,
    LatestPickupTime,
    LatestProposalAcceptanceDate,
    LatestSecurityClearanceDate,
    LatitudeDegreesMeasure,
    LatitudeDirectionCode,
    LatitudeMinutesMeasure,
    LeadTimeMeasure,
    LegalReference,
    LegalStatusIndicator,
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
    LivestockIndicator,
    LoadingLengthMeasure,
    LoadingSequenceId,
    LocaleCode,
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
    LowerOrangeHazardPlacardId,
    LowerTenderAmount,
    LowTendersDescription,
    MandateTypeCode,
    ManufactureDate,
    ManufactureTime,
    MarkAttention,
    MarkAttentionIndicator,
    MarkCare,
    MarkCareIndicator,
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
    NominationDate,
    NominationTime,
    NormalTemperatureReductionQuantity,
    Note,
    NotificationTypeCode,
    OccurrenceDate,
    OccurrenceTime,
    OnCarriageIndicator,
    OneTimeChargeType,
    OneTimeChargeTypeCode,
    OntologyUri,
    OpenTenderId,
    OperatingYearsQuantity,
    OptionalLineItemIndicator,
    OptionsDescription,
    OrderableIndicator,
    OrderableUnit,
    OrderableUnitFactorRate,
    OrderIntervalDaysNumeric,
    OrderQuantityIncrementNumeric,
    OrderTypeCode,
    OrganizationDepartment,
    OriginalContractingSystemId,
    OriginalJobId,
    OtherConditionsIndicator,
    OtherName,
    OutstandingQuantity,
    OutstandingReason,
    OversupplyQuantity,
    OwnerTypeCode,
    PackageLevelCode,
    PackagingTypeCode,
    PackingCriteriaCode,
    PackingMaterial,
    PackLevelCode,
    PackQuantity,
    PackSizeNumeric,
    PaidAmount,
    PaidDate,
    PaidTime,
    ParentDocumentLineReferenceId,
    PartecipationPercent,
    PartialDeliveryIndicator,
    ParticipationPercent,
    PartPresentationCode,
    PartyCapacityAmount,
    PartyTypeCode,
    PassengerQuantity,
    Password,
    PayableAlternativeAmount,
    PayableAmount,
    PayableRoundingAmount,
    PaymentChannelCode,
    PaymentDescription,
    PaymentDueDate,
    PaymentFrequencyCode,
    PaymentId,
    PaymentMeansCode,
    PaymentMeansId,
    PaymentNote,
    PaymentPercent,
    PaymentPurposeCode,
    PaymentTermsDetailsUri,
    PayPerView,
    PenaltyAmount,
    PenaltySurchargePercent,
    Percent,
    PerformanceMetricTypeCode,
    PerformanceValueQuantity,
    PerformingCarrierAssignedId,
    PersonalSituation,
    PerUnitAmount,
    PhoneNumber,
    PlacardEndorsement,
    PlacardNotation,
    PlotIdentification,
    PositionCode,
    PostalZone,
    Postbox,
    PostEventNotificationDurationMeasure,
    PowerIndicator,
    PreCarriageIndicator,
    PreEventNotificationDurationMeasure,
    PreferenceCriterionCode,
    PrepaidAmount,
    PrepaidIndicator,
    PrepaidPaymentReferenceId,
    PreviousCancellationReasonCode,
    PreviousJobId,
    PreviousMeterQuantity,
    PreviousMeterReadingDate,
    PreviousMeterReadingMethod,
    PreviousMeterReadingMethodCode,
    PreviousVersionId,
    PriceAmount,
    PriceChangeReason,
    PriceEvaluationCode,
    PriceRevisionFormulaDescription,
    PriceTypeCode,
    PrimaryAccountNumberId,
    PrintQualifier,
    Priority,
    PrivacyCode,
    PrizeDescription,
    PrizeIndicator,
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
    ReceivedDate,
    ReceivedElectronicTenderQuantity,
    ReceivedForeignTenderQuantity,
    ReceivedQuantity,
    ReceivedTenderQuantity,
    Reference,
    ReferenceDate,
    ReferencedConsignmentId,
    ReferenceEventCode,
    ReferenceId,
    ReferenceTime,
    RefrigeratedIndicator,
    RefrigerationOnIndicator,
    Region,
    RegistrationDate,
    RegistrationExpirationDate,
    RegistrationId,
    RegistrationName,
    RegistrationNationality,
    RegistrationNationalityId,
    RejectActionCode,
    RejectedQuantity,
    RejectReason,
    RejectReasonCode,
    ReleaseId,
    ReliabilityPercent,
    Remarks,
    ReplenishmentOwnerDescription,
    RequestedDeliveryDate,
    RequestedDespatchDate,
    RequestedDespatchTime,
    RequestForQuotationLineId,
    RequiredCurriculaIndicator,
    RequiredCustomsId,
    RequiredDeliveryDate,
    RequiredDeliveryTime,
    RequiredFeeAmount,
    ResidenceType,
    ResidenceTypeCode,
    ResidentOccupantsNumeric,
    Resolution,
    ResolutionCode,
    ResolutionDate,
    ResolutionTime,
    ResponseCode,
    ReturnabilityIndicator,
    ReturnableMaterialIndicator,
    ReturnableQuantity,
    RevisedForecastLineId,
    RevisionDate,
    RevisionTime,
    RoamingPartnerName,
    RoleCode,
    RoleDescription,
    Room,
    RoundingAmount,
    SalesOrderId,
    SalesOrderLineId,
    SchemeUri,
    SealingPartyType,
    SealIssuerTypeCode,
    SealStatusCode,
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
    ShortageActionCode,
    ShortQuantity,
    SignatureId,
    SignatureMethod,
    SizeTypeCode,
    SoleProprietorshipIndicator,
    SourceCurrencyBaseRate,
    SourceCurrencyCode,
    SourceForecastIssueDate,
    SourceForecastIssueTime,
    SourceValueMeasure,
    SpecialInstructions,
    SpecialSecurityIndicator,
    SpecialServiceInstructions,
    SpecialTerms,
    SpecialTransportRequirements,
    SpecificationId,
    SpecificationTypeCode,
    SplitConsignmentIndicator,
    StartDate,
    StartTime,
    StatusCode,
    StatusReason,
    StatusReasonCode,
    StreetName,
    SubcontractingConditionsCode,
    SubmissionDate,
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
    TaxableAmount,
    TaxAmount,
    TaxEnergyAmount,
    TaxEnergyBalanceAmount,
    TaxEnergyOnAccountAmount,
    TaxEvidenceIndicator,
    TaxExclusiveAmount,
    TaxExemptionReason,
    TaxExemptionReasonCode,
    TaxIncludedIndicator,
    TaxInclusiveAmount,
    TaxLevelCode,
    TaxPointDate,
    TaxTypeCode,
    TechnicalCommitteeDescription,
    TechnicalName,
    TelecommunicationsServiceCall,
    TelecommunicationsServiceCallCode,
    TelecommunicationsServiceCategory,
    TelecommunicationsServiceCategoryCode,
    TelecommunicationsSupplyTypeCode,
    Telefax,
    Telephone,
    TenderEnvelopeId,
    TenderEnvelopeTypeCode,
    TendererRequirementTypeCode,
    TendererRoleCode,
    TenderResultCode,
    TestMethod,
    Text,
    ThirdPartyPayerIndicator,
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
    TransportationServiceDescription,
    TransportationServiceDetailsUri,
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
    TypeCode,
    Undgcode,
    UnknownPriceIndicator,
    UpperOrangeHazardPlacardId,
    UrgencyCode,
    Uri,
    UtilityStatementTypeCode,
    Uuid,
    ValidateProcess,
    ValidateTool,
    ValidateToolVersion,
    ValidationDate,
    ValidationResultCode,
    ValidationTime,
    ValidatorId,
    ValidityStartDate,
    Value,
    ValueAmount,
    ValueMeasure,
    ValueQualifier,
    ValueQuantity,
    VarianceQuantity,
    VariantConstraintIndicator,
    VariantId,
    VersionId,
    VesselId,
    VesselName,
    WarrantyInformation,
    WebsiteUri,
    WeekDayCode,
    Weight,
    WeightingAlgorithmCode,
    WeightNumeric,
    WorkPhase,
    WorkPhaseCode,
    Xpath,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    CertificateType as UblCommonBasicComponents21CertificateType,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    Condition as UblCommonBasicComponents21Condition,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    ConsumptionType as UblCommonBasicComponents21ConsumptionType,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    ContractType as UblCommonBasicComponents21ContractType,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    Duty as UblCommonBasicComponents21Duty,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    Location as UblCommonBasicComponents21Location,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    MeterReadingType as UblCommonBasicComponents21MeterReadingType,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    PartyType as UblCommonBasicComponents21PartyType,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    PriceType as UblCommonBasicComponents21PriceType,
)
from ubl.models.common.ubl_common_basic_components_2_1 import (
    TelecommunicationsSupplyType as UblCommonBasicComponents21TelecommunicationsSupplyType,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
)


@dataclass(frozen=True)
class ActivityPropertyType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class AddressLineType:
    line: Optional[Line] = field(
        default=None,
        metadata={
            "name": "Line",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class AirTransportType:
    aircraft_id: Optional[AircraftId] = field(
        default=None,
        metadata={
            "name": "AircraftID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class AuctionTermsType:
    auction_constraint_indicator: Optional[AuctionConstraintIndicator] = field(
        default=None,
        metadata={
            "name": "AuctionConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    justification_description: tuple[JustificationDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "JustificationDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    process_description: tuple[ProcessDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ProcessDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    conditions_description: tuple[ConditionsDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConditionsDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    electronic_device_description: tuple[ElectronicDeviceDescription, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "ElectronicDeviceDescription",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    auction_uri: Optional[AuctionUri] = field(
        default=None,
        metadata={
            "name": "AuctionURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class AwardingCriterionResponseType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    awarding_criterion_id: Optional[AwardingCriterionId] = field(
        default=None,
        metadata={
            "name": "AwardingCriterionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    awarding_criterion_description: tuple[
        AwardingCriterionDescription, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "AwardingCriterionDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subordinate_awarding_criterion_response: tuple[
        "SubordinateAwardingCriterionResponse", ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "SubordinateAwardingCriterionResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class AwardingCriterionType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    awarding_criterion_type_code: Optional[AwardingCriterionTypeCode] = field(
        default=None,
        metadata={
            "name": "AwardingCriterionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    weight_numeric: Optional[WeightNumeric] = field(
        default=None,
        metadata={
            "name": "WeightNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    weight: tuple[Weight, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Weight",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    calculation_expression: tuple[CalculationExpression, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CalculationExpression",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    calculation_expression_code: Optional[CalculationExpressionCode] = field(
        default=None,
        metadata={
            "name": "CalculationExpressionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_amount: Optional[MinimumAmount] = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_amount: Optional[MaximumAmount] = field(
        default=None,
        metadata={
            "name": "MaximumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_improvement_bid: tuple[MinimumImprovementBid, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MinimumImprovementBid",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subordinate_awarding_criterion: tuple[
        "SubordinateAwardingCriterion", ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "SubordinateAwardingCriterion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CardAccountType:
    primary_account_number_id: Optional[PrimaryAccountNumberId] = field(
        default=None,
        metadata={
            "name": "PrimaryAccountNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    network_id: Optional[NetworkId] = field(
        default=None,
        metadata={
            "name": "NetworkID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    card_type_code: Optional[CardTypeCode] = field(
        default=None,
        metadata={
            "name": "CardTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validity_start_date: Optional[ValidityStartDate] = field(
        default=None,
        metadata={
            "name": "ValidityStartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expiry_date: Optional[ExpiryDate] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issuer_id: Optional[IssuerId] = field(
        default=None,
        metadata={
            "name": "IssuerID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_number_id: Optional[IssueNumberId] = field(
        default=None,
        metadata={
            "name": "IssueNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    cv2_id: Optional[Cv2Id] = field(
        default=None,
        metadata={
            "name": "CV2ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    card_chip_code: Optional[CardChipCode] = field(
        default=None,
        metadata={
            "name": "CardChipCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    chip_application_id: Optional[ChipApplicationId] = field(
        default=None,
        metadata={
            "name": "ChipApplicationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    holder_name: Optional[HolderName] = field(
        default=None,
        metadata={
            "name": "HolderName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class CatalogueReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: Optional[IssueTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    revision_date: Optional[RevisionDate] = field(
        default=None,
        metadata={
            "name": "RevisionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    revision_time: Optional[RevisionTime] = field(
        default=None,
        metadata={
            "name": "RevisionTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    version_id: Optional[VersionId] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    previous_version_id: Optional[PreviousVersionId] = field(
        default=None,
        metadata={
            "name": "PreviousVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ClassificationCategoryType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    code_value: Optional[CodeValue] = field(
        default=None,
        metadata={
            "name": "CodeValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    categorizes_classification_category: tuple[
        "CategorizesClassificationCategory", ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "CategorizesClassificationCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ClauseType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    content: tuple[Content, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Content",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class CommodityClassificationType:
    nature_code: Optional[NatureCode] = field(
        default=None,
        metadata={
            "name": "NatureCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    cargo_type_code: Optional[CargoTypeCode] = field(
        default=None,
        metadata={
            "name": "CargoTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    commodity_code: Optional[CommodityCode] = field(
        default=None,
        metadata={
            "name": "CommodityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    item_classification_code: Optional[ItemClassificationCode] = field(
        default=None,
        metadata={
            "name": "ItemClassificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class CommunicationType:
    channel_code: Optional[ChannelCode] = field(
        default=None,
        metadata={
            "name": "ChannelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    channel: Optional[Channel] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ConditionType:
    attribute_id: Optional[AttributeId] = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    measure: Optional[Measure] = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_measure: Optional[MinimumMeasure] = field(
        default=None,
        metadata={
            "name": "MinimumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_measure: Optional[MaximumMeasure] = field(
        default=None,
        metadata={
            "name": "MaximumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ConsumptionAverageType:
    average_amount: Optional[AverageAmount] = field(
        default=None,
        metadata={
            "name": "AverageAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ConsumptionCorrectionType:
    correction_type: Optional[CorrectionType] = field(
        default=None,
        metadata={
            "name": "CorrectionType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    correction_type_code: Optional[CorrectionTypeCode] = field(
        default=None,
        metadata={
            "name": "CorrectionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_number: Optional[MeterNumber] = field(
        default=None,
        metadata={
            "name": "MeterNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gas_pressure_quantity: Optional[GasPressureQuantity] = field(
        default=None,
        metadata={
            "name": "GasPressureQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_temperature_reduction_quantity: Optional[
        ActualTemperatureReductionQuantity
    ] = field(
        default=None,
        metadata={
            "name": "ActualTemperatureReductionQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    normal_temperature_reduction_quantity: Optional[
        NormalTemperatureReductionQuantity
    ] = field(
        default=None,
        metadata={
            "name": "NormalTemperatureReductionQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    difference_temperature_reduction_quantity: Optional[
        DifferenceTemperatureReductionQuantity
    ] = field(
        default=None,
        metadata={
            "name": "DifferenceTemperatureReductionQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    correction_unit_amount: Optional[CorrectionUnitAmount] = field(
        default=None,
        metadata={
            "name": "CorrectionUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_energy_quantity: Optional[ConsumptionEnergyQuantity] = field(
        default=None,
        metadata={
            "name": "ConsumptionEnergyQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_water_quantity: Optional[ConsumptionWaterQuantity] = field(
        default=None,
        metadata={
            "name": "ConsumptionWaterQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    correction_amount: Optional[CorrectionAmount] = field(
        default=None,
        metadata={
            "name": "CorrectionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ContractExecutionRequirementType:
    name: tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    execution_requirement_code: Optional[ExecutionRequirementCode] = field(
        default=None,
        metadata={
            "name": "ExecutionRequirementCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ContractingActivityType:
    activity_type_code: Optional[ActivityTypeCode] = field(
        default=None,
        metadata={
            "name": "ActivityTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    activity_type: Optional[ActivityType] = field(
        default=None,
        metadata={
            "name": "ActivityType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ContractingPartyTypeType:
    party_type_code: Optional[PartyTypeCode] = field(
        default=None,
        metadata={
            "name": "PartyTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party_type: Optional[UblCommonBasicComponents21PartyType] = field(
        default=None,
        metadata={
            "name": "PartyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class CountryType:
    identification_code: Optional[IdentificationCode] = field(
        default=None,
        metadata={
            "name": "IdentificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class CreditAccountType:
    account_id: Optional[AccountId] = field(
        default=None,
        metadata={
            "name": "AccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class DeliveryUnitType:
    batch_quantity: Optional[BatchQuantity] = field(
        default=None,
        metadata={
            "name": "BatchQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    consumer_unit_quantity: Optional[ConsumerUnitQuantity] = field(
        default=None,
        metadata={
            "name": "ConsumerUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_risk_indicator: Optional[HazardousRiskIndicator] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class DimensionType:
    attribute_id: Optional[AttributeId] = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    measure: Optional[Measure] = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_measure: Optional[MinimumMeasure] = field(
        default=None,
        metadata={
            "name": "MinimumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_measure: Optional[MaximumMeasure] = field(
        default=None,
        metadata={
            "name": "MaximumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class EconomicOperatorRoleType:
    role_code: Optional[RoleCode] = field(
        default=None,
        metadata={
            "name": "RoleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    role_description: tuple[RoleDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RoleDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class EventCommentType:
    comment: Optional[Comment] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: Optional[IssueTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class EventTacticEnumerationType:
    consumer_incentive_tactic_type_code: Optional[
        ConsumerIncentiveTacticTypeCode
    ] = field(
        default=None,
        metadata={
            "name": "ConsumerIncentiveTacticTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    display_tactic_type_code: Optional[DisplayTacticTypeCode] = field(
        default=None,
        metadata={
            "name": "DisplayTacticTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    feature_tactic_type_code: Optional[FeatureTacticTypeCode] = field(
        default=None,
        metadata={
            "name": "FeatureTacticTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trade_item_packing_labeling_type_code: Optional[
        TradeItemPackingLabelingTypeCode
    ] = field(
        default=None,
        metadata={
            "name": "TradeItemPackingLabelingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class EvidenceSuppliedType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class ExternalReferenceType:
    uri: Optional[Uri] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_hash: Optional[DocumentHash] = field(
        default=None,
        metadata={
            "name": "DocumentHash",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hash_algorithm_method: Optional[HashAlgorithmMethod] = field(
        default=None,
        metadata={
            "name": "HashAlgorithmMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expiry_date: Optional[ExpiryDate] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expiry_time: Optional[ExpiryTime] = field(
        default=None,
        metadata={
            "name": "ExpiryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mime_code: Optional[MimeCode] = field(
        default=None,
        metadata={
            "name": "MimeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    format_code: Optional[FormatCode] = field(
        default=None,
        metadata={
            "name": "FormatCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    encoding_code: Optional[EncodingCode] = field(
        default=None,
        metadata={
            "name": "EncodingCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    character_set_code: Optional[CharacterSetCode] = field(
        default=None,
        metadata={
            "name": "CharacterSetCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    file_name: Optional[FileName] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ForecastExceptionCriterionLineType:
    forecast_purpose_code: Optional[ForecastPurposeCode] = field(
        default=None,
        metadata={
            "name": "ForecastPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    comparison_data_source_code: Optional[ComparisonDataSourceCode] = field(
        default=None,
        metadata={
            "name": "ComparisonDataSourceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    data_source_code: Optional[DataSourceCode] = field(
        default=None,
        metadata={
            "name": "DataSourceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    time_delta_days_quantity: Optional[TimeDeltaDaysQuantity] = field(
        default=None,
        metadata={
            "name": "TimeDeltaDaysQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ForecastExceptionType:
    forecast_purpose_code: Optional[ForecastPurposeCode] = field(
        default=None,
        metadata={
            "name": "ForecastPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_time: Optional[IssueTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    data_source_code: Optional[DataSourceCode] = field(
        default=None,
        metadata={
            "name": "DataSourceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    comparison_data_code: Optional[ComparisonDataCode] = field(
        default=None,
        metadata={
            "name": "ComparisonDataCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    comparison_forecast_issue_time: Optional[ComparisonForecastIssueTime] = (
        field(
            default=None,
            metadata={
                "name": "ComparisonForecastIssueTime",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    comparison_forecast_issue_date: Optional[ComparisonForecastIssueDate] = (
        field(
            default=None,
            metadata={
                "name": "ComparisonForecastIssueDate",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )


@dataclass(frozen=True)
class ItemComparisonType:
    price_amount: Optional[PriceAmount] = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemPropertyGroupType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    importance_code: Optional[ImportanceCode] = field(
        default=None,
        metadata={
            "name": "ImportanceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemPropertyRangeType:
    minimum_value: Optional[MinimumValue] = field(
        default=None,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_value: Optional[MaximumValue] = field(
        default=None,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class LanguageType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    locale_code: Optional[LocaleCode] = field(
        default=None,
        metadata={
            "name": "LocaleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class LocationCoordinateType:
    coordinate_system_code: Optional[CoordinateSystemCode] = field(
        default=None,
        metadata={
            "name": "CoordinateSystemCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latitude_degrees_measure: Optional[LatitudeDegreesMeasure] = field(
        default=None,
        metadata={
            "name": "LatitudeDegreesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latitude_minutes_measure: Optional[LatitudeMinutesMeasure] = field(
        default=None,
        metadata={
            "name": "LatitudeMinutesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latitude_direction_code: Optional[LatitudeDirectionCode] = field(
        default=None,
        metadata={
            "name": "LatitudeDirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    longitude_degrees_measure: Optional[LongitudeDegreesMeasure] = field(
        default=None,
        metadata={
            "name": "LongitudeDegreesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    longitude_minutes_measure: Optional[LongitudeMinutesMeasure] = field(
        default=None,
        metadata={
            "name": "LongitudeMinutesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    longitude_direction_code: Optional[LongitudeDirectionCode] = field(
        default=None,
        metadata={
            "name": "LongitudeDirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    altitude_measure: Optional[AltitudeMeasure] = field(
        default=None,
        metadata={
            "name": "AltitudeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class MeterPropertyType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name_code: Optional[NameCode] = field(
        default=None,
        metadata={
            "name": "NameCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_quantity: Optional[ValueQuantity] = field(
        default=None,
        metadata={
            "name": "ValueQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_qualifier: tuple[ValueQualifier, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ValueQualifier",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class MeterReadingType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_reading_type: Optional[
        UblCommonBasicComponents21MeterReadingType
    ] = field(
        default=None,
        metadata={
            "name": "MeterReadingType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_reading_type_code: Optional[MeterReadingTypeCode] = field(
        default=None,
        metadata={
            "name": "MeterReadingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    previous_meter_reading_date: Optional[PreviousMeterReadingDate] = field(
        default=None,
        metadata={
            "name": "PreviousMeterReadingDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    previous_meter_quantity: Optional[PreviousMeterQuantity] = field(
        default=None,
        metadata={
            "name": "PreviousMeterQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    latest_meter_reading_date: Optional[LatestMeterReadingDate] = field(
        default=None,
        metadata={
            "name": "LatestMeterReadingDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    latest_meter_quantity: Optional[LatestMeterQuantity] = field(
        default=None,
        metadata={
            "name": "LatestMeterQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    previous_meter_reading_method: Optional[PreviousMeterReadingMethod] = (
        field(
            default=None,
            metadata={
                "name": "PreviousMeterReadingMethod",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    previous_meter_reading_method_code: Optional[
        PreviousMeterReadingMethodCode
    ] = field(
        default=None,
        metadata={
            "name": "PreviousMeterReadingMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_meter_reading_method: Optional[LatestMeterReadingMethod] = field(
        default=None,
        metadata={
            "name": "LatestMeterReadingMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_meter_reading_method_code: Optional[
        LatestMeterReadingMethodCode
    ] = field(
        default=None,
        metadata={
            "name": "LatestMeterReadingMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_reading_comments: tuple[MeterReadingComments, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeterReadingComments",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivered_quantity: Optional[DeliveredQuantity] = field(
        default=None,
        metadata={
            "name": "DeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class MonetaryTotalType:
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_exclusive_amount: Optional[TaxExclusiveAmount] = field(
        default=None,
        metadata={
            "name": "TaxExclusiveAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_inclusive_amount: Optional[TaxInclusiveAmount] = field(
        default=None,
        metadata={
            "name": "TaxInclusiveAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    allowance_total_amount: Optional[AllowanceTotalAmount] = field(
        default=None,
        metadata={
            "name": "AllowanceTotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    charge_total_amount: Optional[ChargeTotalAmount] = field(
        default=None,
        metadata={
            "name": "ChargeTotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    prepaid_amount: Optional[PrepaidAmount] = field(
        default=None,
        metadata={
            "name": "PrepaidAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payable_rounding_amount: Optional[PayableRoundingAmount] = field(
        default=None,
        metadata={
            "name": "PayableRoundingAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payable_amount: Optional[PayableAmount] = field(
        default=None,
        metadata={
            "name": "PayableAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    payable_alternative_amount: Optional[PayableAlternativeAmount] = field(
        default=None,
        metadata={
            "name": "PayableAlternativeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class PartyIdentificationType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class PartyNameType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class PaymentType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    paid_amount: Optional[PaidAmount] = field(
        default=None,
        metadata={
            "name": "PaidAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_date: Optional[ReceivedDate] = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    paid_date: Optional[PaidDate] = field(
        default=None,
        metadata={
            "name": "PaidDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    paid_time: Optional[PaidTime] = field(
        default=None,
        metadata={
            "name": "PaidTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    instruction_id: Optional[InstructionId] = field(
        default=None,
        metadata={
            "name": "InstructionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class PeriodType:
    start_date: Optional[StartDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    start_time: Optional[StartTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    end_date: Optional[EndDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    end_time: Optional[EndTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    duration_measure: Optional[DurationMeasure] = field(
        default=None,
        metadata={
            "name": "DurationMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description_code: tuple[DescriptionCode, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DescriptionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class PhysicalAttributeType:
    attribute_id: Optional[AttributeId] = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    position_code: Optional[PositionCode] = field(
        default=None,
        metadata={
            "name": "PositionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description_code: Optional[DescriptionCode] = field(
        default=None,
        metadata={
            "name": "DescriptionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ProcessJustificationType:
    previous_cancellation_reason_code: Optional[
        PreviousCancellationReasonCode
    ] = field(
        default=None,
        metadata={
            "name": "PreviousCancellationReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    process_reason_code: Optional[ProcessReasonCode] = field(
        default=None,
        metadata={
            "name": "ProcessReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    process_reason: tuple[ProcessReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ProcessReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class RailTransportType:
    train_id: Optional[TrainId] = field(
        default=None,
        metadata={
            "name": "TrainID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    rail_car_id: Optional[RailCarId] = field(
        default=None,
        metadata={
            "name": "RailCarID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class RegulationType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    legal_reference: Optional[LegalReference] = field(
        default=None,
        metadata={
            "name": "LegalReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    ontology_uri: Optional[OntologyUri] = field(
        default=None,
        metadata={
            "name": "OntologyURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class RelatedItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class RoadTransportType:
    license_plate_id: Optional[LicensePlateId] = field(
        default=None,
        metadata={
            "name": "LicensePlateID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class SecondaryHazardType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    placard_notation: Optional[PlacardNotation] = field(
        default=None,
        metadata={
            "name": "PlacardNotation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    placard_endorsement: Optional[PlacardEndorsement] = field(
        default=None,
        metadata={
            "name": "PlacardEndorsement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    emergency_procedures_code: Optional[EmergencyProceduresCode] = field(
        default=None,
        metadata={
            "name": "EmergencyProceduresCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    extension: tuple[Extension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Extension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ServiceFrequencyType:
    week_day_code: Optional[WeekDayCode] = field(
        default=None,
        metadata={
            "name": "WeekDayCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class SubcontractTermsType:
    rate: Optional[Rate] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    unknown_price_indicator: Optional[UnknownPriceIndicator] = field(
        default=None,
        metadata={
            "name": "UnknownPriceIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subcontracting_conditions_code: Optional[SubcontractingConditionsCode] = (
        field(
            default=None,
            metadata={
                "name": "SubcontractingConditionsCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    maximum_percent: Optional[MaximumPercent] = field(
        default=None,
        metadata={
            "name": "MaximumPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_percent: Optional[MinimumPercent] = field(
        default=None,
        metadata={
            "name": "MinimumPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class TemperatureType:
    attribute_id: Optional[AttributeId] = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    measure: Optional[Measure] = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class TransportEquipmentSealType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    seal_issuer_type_code: Optional[SealIssuerTypeCode] = field(
        default=None,
        metadata={
            "name": "SealIssuerTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    condition: Optional[UblCommonBasicComponents21Condition] = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    seal_status_code: Optional[SealStatusCode] = field(
        default=None,
        metadata={
            "name": "SealStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sealing_party_type: Optional[SealingPartyType] = field(
        default=None,
        metadata={
            "name": "SealingPartyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class UnstructuredPriceType:
    price_amount: Optional[PriceAmount] = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    time_amount: Optional[TimeAmount] = field(
        default=None,
        metadata={
            "name": "TimeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class WebSiteAccessType:
    uri: Optional[Uri] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    password: Optional[Password] = field(
        default=None,
        metadata={
            "name": "Password",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    login: Optional[Login] = field(
        default=None,
        metadata={
            "name": "Login",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class AccessoryRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ActivityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ActivityProperty(ActivityPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AdditionalCommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AdditionalTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AddressLine(AddressLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AirTransport(AirTransportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AllowedSubcontractTerms(SubcontractTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AnticipatedMonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ApplicablePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ApplicableRegulation(RegulationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AuctionTerms(AuctionTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AwardingCriterion(AwardingCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AwardingCriterionResponse(AwardingCriterionResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CardAccount(CardAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CategorizesClassificationCategory(ClassificationCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ClassificationCategory(ClassificationCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Clause(ClauseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CollectedPayment(PaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Communication(CommunicationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ComplementaryRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ComponentRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Condition(ConditionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConstitutionPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsumptionAverage(ConsumptionAverageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsumptionCorrection(ConsumptionCorrectionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractAcceptancePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractExecutionRequirement(ContractExecutionRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractFormalizationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractingActivity(ContractingActivityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractingPartyType(ContractingPartyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Country(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CreditAccount(CreditAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DefaultLanguage(LanguageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeletedCatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeliveryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeliveryUnit(DeliveryUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DestinationCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Dimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DocumentAvailabilityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DurationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EconomicOperatorRole(EconomicOperatorRoleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EffectivePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EmergencyTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EnergyWaterConsumptionCorrection(ConsumptionCorrectionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EstimatedDeliveryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EstimatedDespatchPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EstimatedDurationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EstimatedTransitPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EventComment(EventCommentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EventTacticEnumeration(EventTacticEnumerationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EvidenceSupplied(EvidenceSuppliedType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExceptionObservationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExportCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExternalReference(ExternalReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinalDestinationCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FlashpointTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FloorSpaceMeasurementDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ForecastException(ForecastExceptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ForecastExceptionCriterionLine(ForecastExceptionCriterionLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ForecastPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FrequencyPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InventoryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InvitationSubmissionPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InvoicePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class IssuingCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemComparison(ItemComparisonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemPropertyGroup(ItemPropertyGroupType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemPropertyRange(ItemPropertyRangeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Language(LanguageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LegalMonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LineValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LocationCoordinate(LocationCoordinateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MainCommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MainPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MaximumDeliveryUnit(DeliveryUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MaximumTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MeasurementDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MeterProperty(MeterPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MeterReading(MeterReadingType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MinimumDeliveryUnit(DeliveryUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MinimumTemperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class NominationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class NotificationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OptionValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginalDepartureCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OtherCommunication(CommunicationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PalletSpaceMeasurementDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ParticipationRequestReceptionPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PartyIdentification(PartyIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PartyName(PartyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Payment(PaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PaymentReversalPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PenaltyClause(ClauseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PenaltyPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Period(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PhysicalAttribute(PhysicalAttributeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PlannedPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PrepaidPayment(PaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PresentationPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ProcessJustification(ProcessJustificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PromisedDeliveryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class QuotedMonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RailTransport(RailTransportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RangeDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Regulation(RegulationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RelatedCatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReminderPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReplacedRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReplacementRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedCatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedDeliveryPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedDespatchPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedLanguage(LanguageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedMonetaryTotal(MonetaryTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedStatusPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequiredRelatedItem(RelatedItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RoadTransport(RoadTransportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ScheduledServiceFrequency(ServiceFrequencyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SecondaryHazard(SecondaryHazardType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ServiceEndTimePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ServiceFrequency(ServiceFrequencyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ServiceStartTimePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SettlementPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SourceCatalogueReference(CatalogueReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class StatementPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class StatusPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubcontractTerms(SubcontractTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubordinateAwardingCriterion(AwardingCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubordinateAwardingCriterionResponse(AwardingCriterionResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SupportedCommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Temperature(TemperatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderSubmissionDeadlinePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TotalCapacityDimension(DimensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransitCountry(CountryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransitPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportEquipmentSeal(TransportEquipmentSealType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportServiceProviderResponseDeadlinePeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportServiceProviderResponseRequiredPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportUserResponseRequiredPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UnstructuredPrice(UnstructuredPriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UnsupportedCommodityClassification(CommodityClassificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UsabilityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class WarrantyValidityPeriod(PeriodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class WebSiteAccess(WebSiteAccessType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AddressType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    address_type_code: Optional[AddressTypeCode] = field(
        default=None,
        metadata={
            "name": "AddressTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    address_format_code: Optional[AddressFormatCode] = field(
        default=None,
        metadata={
            "name": "AddressFormatCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    postbox: Optional[Postbox] = field(
        default=None,
        metadata={
            "name": "Postbox",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    floor: Optional[Floor] = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    room: Optional[Room] = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    street_name: Optional[StreetName] = field(
        default=None,
        metadata={
            "name": "StreetName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    additional_street_name: Optional[AdditionalStreetName] = field(
        default=None,
        metadata={
            "name": "AdditionalStreetName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    block_name: Optional[BlockName] = field(
        default=None,
        metadata={
            "name": "BlockName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    building_name: Optional[BuildingName] = field(
        default=None,
        metadata={
            "name": "BuildingName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    building_number: Optional[BuildingNumber] = field(
        default=None,
        metadata={
            "name": "BuildingNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    inhouse_mail: Optional[InhouseMail] = field(
        default=None,
        metadata={
            "name": "InhouseMail",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    department: Optional[Department] = field(
        default=None,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mark_attention: Optional[MarkAttention] = field(
        default=None,
        metadata={
            "name": "MarkAttention",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mark_care: Optional[MarkCare] = field(
        default=None,
        metadata={
            "name": "MarkCare",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    plot_identification: Optional[PlotIdentification] = field(
        default=None,
        metadata={
            "name": "PlotIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    city_subdivision_name: Optional[CitySubdivisionName] = field(
        default=None,
        metadata={
            "name": "CitySubdivisionName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    city_name: Optional[CityName] = field(
        default=None,
        metadata={
            "name": "CityName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    postal_zone: Optional[PostalZone] = field(
        default=None,
        metadata={
            "name": "PostalZone",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    country_subentity: Optional[CountrySubentity] = field(
        default=None,
        metadata={
            "name": "CountrySubentity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    country_subentity_code: Optional[CountrySubentityCode] = field(
        default=None,
        metadata={
            "name": "CountrySubentityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    region: Optional[Region] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    district: Optional[District] = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    timezone_offset: Optional[TimezoneOffset] = field(
        default=None,
        metadata={
            "name": "TimezoneOffset",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    address_line: tuple[AddressLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AddressLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    location_coordinate: tuple[LocationCoordinate, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "LocationCoordinate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class AttachmentType:
    embedded_document_binary_object: Optional[EmbeddedDocumentBinaryObject] = (
        field(
            default=None,
            metadata={
                "name": "EmbeddedDocumentBinaryObject",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    external_reference: Optional[ExternalReference] = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CapabilityType:
    capability_type_code: Optional[CapabilityTypeCode] = field(
        default=None,
        metadata={
            "name": "CapabilityTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_amount: Optional[ValueAmount] = field(
        default=None,
        metadata={
            "name": "ValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_quantity: Optional[ValueQuantity] = field(
        default=None,
        metadata={
            "name": "ValueQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    evidence_supplied: tuple[EvidenceSupplied, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EvidenceSupplied",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ClassificationSchemeType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    last_revision_date: Optional[LastRevisionDate] = field(
        default=None,
        metadata={
            "name": "LastRevisionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    last_revision_time: Optional[LastRevisionTime] = field(
        default=None,
        metadata={
            "name": "LastRevisionTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    agency_id: Optional[AgencyId] = field(
        default=None,
        metadata={
            "name": "AgencyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    agency_name: Optional[AgencyName] = field(
        default=None,
        metadata={
            "name": "AgencyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    version_id: Optional[VersionId] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uri: Optional[Uri] = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    scheme_uri: Optional[SchemeUri] = field(
        default=None,
        metadata={
            "name": "SchemeURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    language_id: Optional[LanguageId] = field(
        default=None,
        metadata={
            "name": "LanguageID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    classification_category: tuple[ClassificationCategory, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ClassificationCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class ConsumptionHistoryType:
    meter_number: Optional[MeterNumber] = field(
        default=None,
        metadata={
            "name": "MeterNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_level_code: Optional[ConsumptionLevelCode] = field(
        default=None,
        metadata={
            "name": "ConsumptionLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_level: Optional[ConsumptionLevel] = field(
        default=None,
        metadata={
            "name": "ConsumptionLevel",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class ConsumptionReportReferenceType:
    consumption_report_id: Optional[ConsumptionReportId] = field(
        default=None,
        metadata={
            "name": "ConsumptionReportID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    consumption_type: Optional[UblCommonBasicComponents21ConsumptionType] = (
        field(
            default=None,
            metadata={
                "name": "ConsumptionType",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    consumption_type_code: Optional[ConsumptionTypeCode] = field(
        default=None,
        metadata={
            "name": "ConsumptionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_consumed_quantity: Optional[TotalConsumedQuantity] = field(
        default=None,
        metadata={
            "name": "TotalConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class ContactType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telephone: Optional[Telephone] = field(
        default=None,
        metadata={
            "name": "Telephone",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telefax: Optional[Telefax] = field(
        default=None,
        metadata={
            "name": "Telefax",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    electronic_mail: Optional[ElectronicMail] = field(
        default=None,
        metadata={
            "name": "ElectronicMail",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    other_communication: tuple[OtherCommunication, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OtherCommunication",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DeclarationType:
    name: tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declaration_type_code: Optional[DeclarationTypeCode] = field(
        default=None,
        metadata={
            "name": "DeclarationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    evidence_supplied: tuple[EvidenceSupplied, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EvidenceSupplied",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EventTacticType:
    comment: Optional[Comment] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    event_tactic_enumeration: Optional[EventTacticEnumeration] = field(
        default=None,
        metadata={
            "name": "EventTacticEnumeration",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class FinancialGuaranteeType:
    guarantee_type_code: Optional[GuaranteeTypeCode] = field(
        default=None,
        metadata={
            "name": "GuaranteeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    liability_amount: Optional[LiabilityAmount] = field(
        default=None,
        metadata={
            "name": "LiabilityAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount_rate: Optional[AmountRate] = field(
        default=None,
        metadata={
            "name": "AmountRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    constitution_period: Optional[ConstitutionPeriod] = field(
        default=None,
        metadata={
            "name": "ConstitutionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class HazardousGoodsTransitType:
    transport_emergency_card_code: Optional[TransportEmergencyCardCode] = (
        field(
            default=None,
            metadata={
                "name": "TransportEmergencyCardCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    packing_criteria_code: Optional[PackingCriteriaCode] = field(
        default=None,
        metadata={
            "name": "PackingCriteriaCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_regulation_code: Optional[HazardousRegulationCode] = field(
        default=None,
        metadata={
            "name": "HazardousRegulationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    inhalation_toxicity_zone_code: Optional[InhalationToxicityZoneCode] = (
        field(
            default=None,
            metadata={
                "name": "InhalationToxicityZoneCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    transport_authorization_code: Optional[TransportAuthorizationCode] = field(
        default=None,
        metadata={
            "name": "TransportAuthorizationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_temperature: Optional[MaximumTemperature] = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    minimum_temperature: Optional[MinimumTemperature] = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemPropertyType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    name_code: Optional[NameCode] = field(
        default=None,
        metadata={
            "name": "NameCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    test_method: Optional[TestMethod] = field(
        default=None,
        metadata={
            "name": "TestMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value: Optional[Value] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_quantity: Optional[ValueQuantity] = field(
        default=None,
        metadata={
            "name": "ValueQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_qualifier: tuple[ValueQualifier, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ValueQualifier",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    importance_code: Optional[ImportanceCode] = field(
        default=None,
        metadata={
            "name": "ImportanceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    list_value: tuple[ListValue, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ListValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    usability_period: Optional[UsabilityPeriod] = field(
        default=None,
        metadata={
            "name": "UsabilityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_property_group: tuple[ItemPropertyGroup, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ItemPropertyGroup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    range_dimension: Optional[RangeDimension] = field(
        default=None,
        metadata={
            "name": "RangeDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_property_range: Optional[ItemPropertyRange] = field(
        default=None,
        metadata={
            "name": "ItemPropertyRange",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class MeterType:
    meter_number: Optional[MeterNumber] = field(
        default=None,
        metadata={
            "name": "MeterNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_name: Optional[MeterName] = field(
        default=None,
        metadata={
            "name": "MeterName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_constant: Optional[MeterConstant] = field(
        default=None,
        metadata={
            "name": "MeterConstant",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_constant_code: Optional[MeterConstantCode] = field(
        default=None,
        metadata={
            "name": "MeterConstantCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_delivered_quantity: Optional[TotalDeliveredQuantity] = field(
        default=None,
        metadata={
            "name": "TotalDeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_reading: tuple[MeterReading, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeterReading",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    meter_property: tuple[MeterProperty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeterProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PriceListType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    status_code: Optional[StatusCode] = field(
        default=None,
        metadata={
            "name": "StatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validity_period: tuple[ValidityPeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    previous_price_list: Optional["PreviousPriceList"] = field(
        default=None,
        metadata={
            "name": "PreviousPriceList",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RenewalType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RetailPlannedImpactType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_purpose_code: Optional[ForecastPurposeCode] = field(
        default=None,
        metadata={
            "name": "ForecastPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class StatusType:
    condition_code: Optional[ConditionCode] = field(
        default=None,
        metadata={
            "name": "ConditionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reference_date: Optional[ReferenceDate] = field(
        default=None,
        metadata={
            "name": "ReferenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reference_time: Optional[ReferenceTime] = field(
        default=None,
        metadata={
            "name": "ReferenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    status_reason_code: Optional[StatusReasonCode] = field(
        default=None,
        metadata={
            "name": "StatusReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    status_reason: tuple[StatusReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "StatusReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sequence_id: Optional[SequenceId] = field(
        default=None,
        metadata={
            "name": "SequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    text: tuple[Text, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    indication_indicator: Optional[IndicationIndicator] = field(
        default=None,
        metadata={
            "name": "IndicationIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reliability_percent: Optional[ReliabilityPercent] = field(
        default=None,
        metadata={
            "name": "ReliabilityPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    condition: tuple[Condition, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class StowageType:
    location_id: Optional[LocationId] = field(
        default=None,
        metadata={
            "name": "LocationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    location: tuple[UblCommonBasicComponents21Location, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    measurement_dimension: tuple[MeasurementDimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class AccountingContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AdditionalItemProperty(ItemPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Address(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ApplicableAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ApplicableTerritoryAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Attachment(AttachmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BusinessClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BuyerContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Capability(CapabilityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsumptionHistory(ConsumptionHistoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsumptionReportReference(ConsumptionReportReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Contact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CurrentStatus(StatusType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Declaration(DeclarationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeliveryAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeliveryContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DespatchAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DespatchContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DigitalSignatureAttachment(AttachmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EventTactic(EventTacticType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinalFinancialGuarantee(FinancialGuaranteeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinancialCapability(CapabilityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinancialGuarantee(FinancialGuaranteeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class HazardousGoodsTransit(HazardousGoodsTransitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemProperty(ItemPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class JurisdictionRegionAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class KeywordItemProperty(ItemPropertyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LocationAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Meter(MeterType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PostalAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PreviousPriceList(PriceListType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PriceList(PriceListType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RegistrationAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Renewal(RenewalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequiredBusinessClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequiredClassificationScheme(ClassificationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequiredFinancialGuarantee(FinancialGuaranteeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ResidenceAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RetailPlannedImpact(RetailPlannedImpactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReturnAddress(AddressType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SellerContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SignatoryContact(ContactType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Status(StatusType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Stowage(StowageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TechnicalCapability(CapabilityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UtilityMeter(MeterType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BudgetAccountType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    budget_year_numeric: Optional[BudgetYearNumeric] = field(
        default=None,
        metadata={
            "name": "BudgetYearNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_classification_scheme: Optional[RequiredClassificationScheme] = (
        field(
            default=None,
            metadata={
                "name": "RequiredClassificationScheme",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )


@dataclass(frozen=True)
class ConsumptionPointType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_id: Optional[SubscriberId] = field(
        default=None,
        metadata={
            "name": "SubscriberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_type: Optional[SubscriberType] = field(
        default=None,
        metadata={
            "name": "SubscriberType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_type_code: Optional[SubscriberTypeCode] = field(
        default=None,
        metadata={
            "name": "SubscriberTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_delivered_quantity: Optional[TotalDeliveredQuantity] = field(
        default=None,
        metadata={
            "name": "TotalDeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    web_site_access: Optional[WebSiteAccess] = field(
        default=None,
        metadata={
            "name": "WebSiteAccess",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    utility_meter: tuple[UtilityMeter, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "UtilityMeter",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ContractExtensionType:
    options_description: tuple[OptionsDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OptionsDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_number_numeric: Optional[MinimumNumberNumeric] = field(
        default=None,
        metadata={
            "name": "MinimumNumberNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_number_numeric: Optional[MaximumNumberNumeric] = field(
        default=None,
        metadata={
            "name": "MaximumNumberNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    option_validity_period: Optional[OptionValidityPeriod] = field(
        default=None,
        metadata={
            "name": "OptionValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    renewal: tuple[Renewal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Renewal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CorporateRegistrationSchemeType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    corporate_registration_type_code: Optional[
        CorporateRegistrationTypeCode
    ] = field(
        default=None,
        metadata={
            "name": "CorporateRegistrationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    jurisdiction_region_address: tuple[JurisdictionRegionAddress, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "JurisdictionRegionAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DocumentReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    copy_indicator: Optional[CopyIndicator] = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: Optional[IssueTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_type_code: Optional[DocumentTypeCode] = field(
        default=None,
        metadata={
            "name": "DocumentTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_type: Optional[DocumentType] = field(
        default=None,
        metadata={
            "name": "DocumentType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    xpath: tuple[Xpath, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "XPath",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    language_id: Optional[LanguageId] = field(
        default=None,
        metadata={
            "name": "LanguageID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    locale_code: Optional[LocaleCode] = field(
        default=None,
        metadata={
            "name": "LocaleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    version_id: Optional[VersionId] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_status_code: Optional[DocumentStatusCode] = field(
        default=None,
        metadata={
            "name": "DocumentStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_description: tuple[DocumentDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    attachment: Optional[Attachment] = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    issuer_party: Optional["IssuerParty"] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    result_of_verification: Optional["ResultOfVerification"] = field(
        default=None,
        metadata={
            "name": "ResultOfVerification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class FinancialInstitutionType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class LocationType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    conditions: tuple[Conditions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Conditions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    country_subentity: Optional[CountrySubentity] = field(
        default=None,
        metadata={
            "name": "CountrySubentity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    country_subentity_code: Optional[CountrySubentityCode] = field(
        default=None,
        metadata={
            "name": "CountrySubentityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    location_type_code: Optional[LocationTypeCode] = field(
        default=None,
        metadata={
            "name": "LocationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    information_uri: Optional[InformationUri] = field(
        default=None,
        metadata={
            "name": "InformationURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validity_period: tuple[ValidityPeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    subsidiary_location: tuple["SubsidiaryLocation", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubsidiaryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    location_coordinate: tuple[LocationCoordinate, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "LocationCoordinate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class LotIdentificationType:
    lot_number_id: Optional[LotNumberId] = field(
        default=None,
        metadata={
            "name": "LotNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expiry_date: Optional[ExpiryDate] = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    additional_item_property: tuple[AdditionalItemProperty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalItemProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ResponseType:
    reference_id: Optional[ReferenceId] = field(
        default=None,
        metadata={
            "name": "ReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    response_code: Optional[ResponseCode] = field(
        default=None,
        metadata={
            "name": "ResponseCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    effective_date: Optional[EffectiveDate] = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    effective_time: Optional[EffectiveTime] = field(
        default=None,
        metadata={
            "name": "EffectiveTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    status: tuple[Status, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TaxSchemeType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_type_code: Optional[TaxTypeCode] = field(
        default=None,
        metadata={
            "name": "TaxTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    currency_code: Optional[CurrencyCode] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    jurisdiction_region_address: tuple[JurisdictionRegionAddress, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "JurisdictionRegionAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TradingTermsType:
    information: tuple[Information, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    applicable_address: Optional[ApplicableAddress] = field(
        default=None,
        metadata={
            "name": "ApplicableAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ActivityFinalLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ActivityOriginLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AdditionalDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AlternativeDeliveryLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AtLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BudgetAccount(BudgetAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CallForTendersDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CatalogueDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsumptionPoint(ConsumptionPointType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractExtension(ContractExtensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractualDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CorporateRegistrationScheme(CorporateRegistrationSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CreditNoteDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DebitNoteDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeliveryLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DespatchDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DespatchLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DiscrepancyResponse(ResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EmploymentLegislationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EnvironmentalLegislationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EvidenceDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinancialInstitution(FinancialInstitutionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FirstArrivalPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FiscalLegislationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FreightChargeLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FromLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class GuaranteeDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class GuidanceDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class HaulageTradingTerms(TradingTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class IdentityDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InventoryLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InvoiceDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemSpecificationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LastExitPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LegalDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LoadingLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LoadingPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Location(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LotIdentification(LotIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MandateDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MeasurementFromLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MeasurementToLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MinutesDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class NoticeDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class NotificationLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OccurenceLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OrderDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginalDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginatorDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ParentDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ParticipatingLocationsLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PhysicalLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PickupLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PreviousDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ProcurementLegislationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class QuotationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RealizedLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReceiptDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RegistryCertificateDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RegistryPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReminderDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReplacedNoticeDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestForQuotationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedStatusLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ResolutionDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Response(ResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SelfBilledCreditNoteDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SelfBilledInvoiceDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ShipmentDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class StatementDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class StatusLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class StorageLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubsidiaryLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SupportingDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TaxScheme(TaxSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TechnicalDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TemplateDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TendererQualificationDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ToLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TradingTerms(TradingTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportExecutionPlanDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportExecutionPlanRequestDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportProgressStatusRequestDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportServiceDescriptionDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportServiceDescriptionRequestDocumentReference(
    DocumentReferenceType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportationStatusRequestDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransshipPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UnloadingLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UnloadingPortLocation(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UtilityConsumptionPoint(ConsumptionPointType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class WorkOrderDocumentReference(DocumentReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BranchType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    financial_institution: Optional[FinancialInstitution] = field(
        default=None,
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    address: Optional[Address] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class BudgetAccountLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_amount: Optional[TotalAmount] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    budget_account: tuple[BudgetAccount, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BudgetAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ConsumptionReportType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    consumption_type: Optional[UblCommonBasicComponents21ConsumptionType] = (
        field(
            default=None,
            metadata={
                "name": "ConsumptionType",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    consumption_type_code: Optional[ConsumptionTypeCode] = field(
        default=None,
        metadata={
            "name": "ConsumptionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_consumed_quantity: Optional[TotalConsumedQuantity] = field(
        default=None,
        metadata={
            "name": "TotalConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    basic_consumed_quantity: Optional[BasicConsumedQuantity] = field(
        default=None,
        metadata={
            "name": "BasicConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    resident_occupants_numeric: Optional[ResidentOccupantsNumeric] = field(
        default=None,
        metadata={
            "name": "ResidentOccupantsNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumers_energy_level_code: Optional[ConsumersEnergyLevelCode] = field(
        default=None,
        metadata={
            "name": "ConsumersEnergyLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumers_energy_level: Optional[ConsumersEnergyLevel] = field(
        default=None,
        metadata={
            "name": "ConsumersEnergyLevel",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    residence_type: Optional[ResidenceType] = field(
        default=None,
        metadata={
            "name": "ResidenceType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    residence_type_code: Optional[ResidenceTypeCode] = field(
        default=None,
        metadata={
            "name": "ResidenceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    heating_type: Optional[HeatingType] = field(
        default=None,
        metadata={
            "name": "HeatingType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    heating_type_code: Optional[HeatingTypeCode] = field(
        default=None,
        metadata={
            "name": "HeatingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    guidance_document_reference: Optional[GuidanceDocumentReference] = field(
        default=None,
        metadata={
            "name": "GuidanceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: Optional[DocumentReference] = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consumption_report_reference: tuple[ConsumptionReportReference, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "ConsumptionReportReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    consumption_history: tuple[ConsumptionHistory, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConsumptionHistory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ContractType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: Optional[IssueTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nomination_date: Optional[NominationDate] = field(
        default=None,
        metadata={
            "name": "NominationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nomination_time: Optional[NominationTime] = field(
        default=None,
        metadata={
            "name": "NominationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract_type_code: Optional[ContractTypeCode] = field(
        default=None,
        metadata={
            "name": "ContractTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract_type: Optional[UblCommonBasicComponents21ContractType] = field(
        default=None,
        metadata={
            "name": "ContractType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    version_id: Optional[VersionId] = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_document_reference: tuple[ContractDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContractDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    nomination_period: Optional[NominationPeriod] = field(
        default=None,
        metadata={
            "name": "NominationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contractual_delivery: Optional["ContractualDelivery"] = field(
        default=None,
        metadata={
            "name": "ContractualDelivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EmissionCalculationMethodType:
    calculation_method_code: Optional[CalculationMethodCode] = field(
        default=None,
        metadata={
            "name": "CalculationMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fullness_indication_code: Optional[FullnessIndicationCode] = field(
        default=None,
        metadata={
            "name": "FullnessIndicationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    measurement_from_location: Optional[MeasurementFromLocation] = field(
        default=None,
        metadata={
            "name": "MeasurementFromLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    measurement_to_location: Optional[MeasurementToLocation] = field(
        default=None,
        metadata={
            "name": "MeasurementToLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EnergyTaxReportType:
    tax_energy_amount: Optional[TaxEnergyAmount] = field(
        default=None,
        metadata={
            "name": "TaxEnergyAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_energy_on_account_amount: Optional[TaxEnergyOnAccountAmount] = field(
        default=None,
        metadata={
            "name": "TaxEnergyOnAccountAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_energy_balance_amount: Optional[TaxEnergyBalanceAmount] = field(
        default=None,
        metadata={
            "name": "TaxEnergyBalanceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_scheme: Optional[TaxScheme] = field(
        default=None,
        metadata={
            "name": "TaxScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class EventType:
    identification_id: Optional[IdentificationId] = field(
        default=None,
        metadata={
            "name": "IdentificationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    occurrence_date: Optional[OccurrenceDate] = field(
        default=None,
        metadata={
            "name": "OccurrenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    occurrence_time: Optional[OccurrenceTime] = field(
        default=None,
        metadata={
            "name": "OccurrenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    type_code: Optional[TypeCode] = field(
        default=None,
        metadata={
            "name": "TypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    completion_indicator: Optional[CompletionIndicator] = field(
        default=None,
        metadata={
            "name": "CompletionIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    current_status: tuple[CurrentStatus, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CurrentStatus",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contact: tuple[Contact, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    occurence_location: Optional[OccurenceLocation] = field(
        default=None,
        metadata={
            "name": "OccurenceLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemInstanceType:
    product_trace_id: Optional[ProductTraceId] = field(
        default=None,
        metadata={
            "name": "ProductTraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    manufacture_date: Optional[ManufactureDate] = field(
        default=None,
        metadata={
            "name": "ManufactureDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    manufacture_time: Optional[ManufactureTime] = field(
        default=None,
        metadata={
            "name": "ManufactureTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    best_before_date: Optional[BestBeforeDate] = field(
        default=None,
        metadata={
            "name": "BestBeforeDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_id: Optional[RegistrationId] = field(
        default=None,
        metadata={
            "name": "RegistrationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    serial_id: Optional[SerialId] = field(
        default=None,
        metadata={
            "name": "SerialID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    additional_item_property: tuple[AdditionalItemProperty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalItemProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    lot_identification: Optional[LotIdentification] = field(
        default=None,
        metadata={
            "name": "LotIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class LineReferenceType:
    line_id: Optional[LineId] = field(
        default=None,
        metadata={
            "name": "LineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_status_code: Optional[LineStatusCode] = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_reference: Optional[DocumentReference] = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class MaritimeTransportType:
    vessel_id: Optional[VesselId] = field(
        default=None,
        metadata={
            "name": "VesselID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    vessel_name: Optional[VesselName] = field(
        default=None,
        metadata={
            "name": "VesselName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    radio_call_sign_id: Optional[RadioCallSignId] = field(
        default=None,
        metadata={
            "name": "RadioCallSignID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    ships_requirements: tuple[ShipsRequirements, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ShipsRequirements",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_tonnage_measure: Optional[GrossTonnageMeasure] = field(
        default=None,
        metadata={
            "name": "GrossTonnageMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_tonnage_measure: Optional[NetTonnageMeasure] = field(
        default=None,
        metadata={
            "name": "NetTonnageMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registry_certificate_document_reference: Optional[
        RegistryCertificateDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "RegistryCertificateDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    registry_port_location: Optional[RegistryPortLocation] = field(
        default=None,
        metadata={
            "name": "RegistryPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class OrderReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    sales_order_id: Optional[SalesOrderId] = field(
        default=None,
        metadata={
            "name": "SalesOrderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    copy_indicator: Optional[CopyIndicator] = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: Optional[IssueTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customer_reference: Optional[CustomerReference] = field(
        default=None,
        metadata={
            "name": "CustomerReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_type_code: Optional[OrderTypeCode] = field(
        default=None,
        metadata={
            "name": "OrderTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_reference: Optional[DocumentReference] = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PartyTaxSchemeType:
    registration_name: Optional[RegistrationName] = field(
        default=None,
        metadata={
            "name": "RegistrationName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_id: Optional[CompanyId] = field(
        default=None,
        metadata={
            "name": "CompanyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_level_code: Optional[TaxLevelCode] = field(
        default=None,
        metadata={
            "name": "TaxLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exemption_reason_code: Optional[ExemptionReasonCode] = field(
        default=None,
        metadata={
            "name": "ExemptionReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exemption_reason: tuple[ExemptionReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ExemptionReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_address: Optional[RegistrationAddress] = field(
        default=None,
        metadata={
            "name": "RegistrationAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_scheme: Optional[TaxScheme] = field(
        default=None,
        metadata={
            "name": "TaxScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class TaxCategoryType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    base_unit_measure: Optional[BaseUnitMeasure] = field(
        default=None,
        metadata={
            "name": "BaseUnitMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    per_unit_amount: Optional[PerUnitAmount] = field(
        default=None,
        metadata={
            "name": "PerUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_exemption_reason_code: Optional[TaxExemptionReasonCode] = field(
        default=None,
        metadata={
            "name": "TaxExemptionReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_exemption_reason: tuple[TaxExemptionReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxExemptionReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tier_range: Optional[TierRange] = field(
        default=None,
        metadata={
            "name": "TierRange",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tier_rate_percent: Optional[TierRatePercent] = field(
        default=None,
        metadata={
            "name": "TierRatePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_scheme: Optional[TaxScheme] = field(
        default=None,
        metadata={
            "name": "TaxScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class TenderRequirementType:
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    template_document_reference: Optional[TemplateDocumentReference] = field(
        default=None,
        metadata={
            "name": "TemplateDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransactionConditionsType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    action_code: Optional[ActionCode] = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class WorkPhaseReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    work_phase_code: Optional[WorkPhaseCode] = field(
        default=None,
        metadata={
            "name": "WorkPhaseCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    work_phase: tuple[WorkPhase, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "WorkPhase",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    progress_percent: Optional[ProgressPercent] = field(
        default=None,
        metadata={
            "name": "ProgressPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    start_date: Optional[StartDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    end_date: Optional[EndDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    work_order_document_reference: tuple[WorkOrderDocumentReference, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "WorkOrderDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )


@dataclass(frozen=True)
class ApplicableTaxCategory(TaxCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Branch(BranchType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BudgetAccountLine(BudgetAccountLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CallForTendersLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CatalogueLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ClassifiedTaxCategory(TaxCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsumptionReport(ConsumptionReportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Contract(ContractType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DependentLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DespatchLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DocumentTenderRequirement(TenderRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EmissionCalculationMethod(EmissionCalculationMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EnergyTaxReport(EnergyTaxReportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Event(EventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinancialInstitutionBranch(BranchType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ForeignExchangeContract(ContractType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemInstance(ItemInstanceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MaritimeTransport(MaritimeTransportType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OpenTenderEvent(EventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OrderReference(OrderReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ParentDocumentLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PartyTaxScheme(PartyTaxSchemeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class QuotationLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReceiptLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReferencedContract(ContractType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestLineReference(LineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubsequentProcessTenderRequirement(TenderRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TaxCategory(TaxCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderRequirement(TenderRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransactionConditions(TransactionConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportContract(ContractType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class WorkPhaseReference(WorkPhaseReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DependentPriceReferenceType:
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    location_address: Optional[LocationAddress] = field(
        default=None,
        metadata={
            "name": "LocationAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    dependent_line_reference: Optional[DependentLineReference] = field(
        default=None,
        metadata={
            "name": "DependentLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DutyType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    duty: Optional[UblCommonBasicComponents21Duty] = field(
        default=None,
        metadata={
            "name": "Duty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    duty_code: Optional[DutyCode] = field(
        default=None,
        metadata={
            "name": "DutyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_category: Optional[TaxCategory] = field(
        default=None,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EnergyWaterSupplyType:
    consumption_report: tuple[ConsumptionReport, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConsumptionReport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    energy_tax_report: tuple[EnergyTaxReport, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EnergyTaxReport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consumption_average: tuple[ConsumptionAverage, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConsumptionAverage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    energy_water_consumption_correction: tuple[
        EnergyWaterConsumptionCorrection, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "EnergyWaterConsumptionCorrection",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EnvironmentalEmissionType:
    environmental_emission_type_code: Optional[
        EnvironmentalEmissionTypeCode
    ] = field(
        default=None,
        metadata={
            "name": "EnvironmentalEmissionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    value_measure: Optional[ValueMeasure] = field(
        default=None,
        metadata={
            "name": "ValueMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    emission_calculation_method: tuple[EmissionCalculationMethod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EmissionCalculationMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ExchangeRateType:
    source_currency_code: Optional[SourceCurrencyCode] = field(
        default=None,
        metadata={
            "name": "SourceCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    source_currency_base_rate: Optional[SourceCurrencyBaseRate] = field(
        default=None,
        metadata={
            "name": "SourceCurrencyBaseRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    target_currency_code: Optional[TargetCurrencyCode] = field(
        default=None,
        metadata={
            "name": "TargetCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    target_currency_base_rate: Optional[TargetCurrencyBaseRate] = field(
        default=None,
        metadata={
            "name": "TargetCurrencyBaseRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exchange_market_id: Optional[ExchangeMarketId] = field(
        default=None,
        metadata={
            "name": "ExchangeMarketID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    calculation_rate: Optional[CalculationRate] = field(
        default=None,
        metadata={
            "name": "CalculationRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mathematic_operator_code: Optional[MathematicOperatorCode] = field(
        default=None,
        metadata={
            "name": "MathematicOperatorCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    date: Optional[Date] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    foreign_exchange_contract: Optional[ForeignExchangeContract] = field(
        default=None,
        metadata={
            "name": "ForeignExchangeContract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class FinancialAccountType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    alias_name: Optional[AliasName] = field(
        default=None,
        metadata={
            "name": "AliasName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    account_type_code: Optional[AccountTypeCode] = field(
        default=None,
        metadata={
            "name": "AccountTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    account_format_code: Optional[AccountFormatCode] = field(
        default=None,
        metadata={
            "name": "AccountFormatCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    currency_code: Optional[CurrencyCode] = field(
        default=None,
        metadata={
            "name": "CurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_note: tuple[PaymentNote, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentNote",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    financial_institution_branch: Optional[FinancialInstitutionBranch] = field(
        default=None,
        metadata={
            "name": "FinancialInstitutionBranch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class FrameworkAgreementType:
    expected_operator_quantity: Optional[ExpectedOperatorQuantity] = field(
        default=None,
        metadata={
            "name": "ExpectedOperatorQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_operator_quantity: Optional[MaximumOperatorQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumOperatorQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    justification: tuple[Justification, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Justification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    frequency: tuple[Frequency, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Frequency",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    duration_period: Optional[DurationPeriod] = field(
        default=None,
        metadata={
            "name": "DurationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    subsequent_process_tender_requirement: tuple[
        SubsequentProcessTenderRequirement, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "SubsequentProcessTenderRequirement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class LineResponseType:
    line_reference: Optional[LineReference] = field(
        default=None,
        metadata={
            "name": "LineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    response: tuple[Response, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Response",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class OrderLineReferenceType:
    line_id: Optional[LineId] = field(
        default=None,
        metadata={
            "name": "LineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    sales_order_line_id: Optional[SalesOrderLineId] = field(
        default=None,
        metadata={
            "name": "SalesOrderLineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_status_code: Optional[LineStatusCode] = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_reference: Optional[OrderReference] = field(
        default=None,
        metadata={
            "name": "OrderReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ProjectReferenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    work_phase_reference: tuple[WorkPhaseReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "WorkPhaseReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RequestedTenderTotalType:
    estimated_overall_contract_amount: Optional[
        EstimatedOverallContractAmount
    ] = field(
        default=None,
        metadata={
            "name": "EstimatedOverallContractAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_amount: Optional[TotalAmount] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_included_indicator: Optional[TaxIncludedIndicator] = field(
        default=None,
        metadata={
            "name": "TaxIncludedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_amount: Optional[MinimumAmount] = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_amount: Optional[MaximumAmount] = field(
        default=None,
        metadata={
            "name": "MaximumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    monetary_scope: tuple[MonetaryScope, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MonetaryScope",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    average_subsequent_contract_amount: Optional[
        AverageSubsequentContractAmount
    ] = field(
        default=None,
        metadata={
            "name": "AverageSubsequentContractAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    applicable_tax_category: tuple[ApplicableTaxCategory, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ApplicableTaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TaxSubtotalType:
    taxable_amount: Optional[TaxableAmount] = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_amount: Optional[TaxAmount] = field(
        default=None,
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    calculation_sequence_numeric: Optional[CalculationSequenceNumeric] = field(
        default=None,
        metadata={
            "name": "CalculationSequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transaction_currency_tax_amount: Optional[TransactionCurrencyTaxAmount] = (
        field(
            default=None,
            metadata={
                "name": "TransactionCurrencyTaxAmount",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    percent: Optional[Percent] = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    base_unit_measure: Optional[BaseUnitMeasure] = field(
        default=None,
        metadata={
            "name": "BaseUnitMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    per_unit_amount: Optional[PerUnitAmount] = field(
        default=None,
        metadata={
            "name": "PerUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tier_range: Optional[TierRange] = field(
        default=None,
        metadata={
            "name": "TierRange",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tier_rate_percent: Optional[TierRatePercent] = field(
        default=None,
        metadata={
            "name": "TierRatePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_category: Optional[TaxCategory] = field(
        default=None,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class UtilityItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    subscriber_id: Optional[SubscriberId] = field(
        default=None,
        metadata={
            "name": "SubscriberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_type: Optional[SubscriberType] = field(
        default=None,
        metadata={
            "name": "SubscriberType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_type_code: Optional[SubscriberTypeCode] = field(
        default=None,
        metadata={
            "name": "SubscriberTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pack_quantity: Optional[PackQuantity] = field(
        default=None,
        metadata={
            "name": "PackQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pack_size_numeric: Optional[PackSizeNumeric] = field(
        default=None,
        metadata={
            "name": "PackSizeNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_type: Optional[UblCommonBasicComponents21ConsumptionType] = (
        field(
            default=None,
            metadata={
                "name": "ConsumptionType",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    consumption_type_code: Optional[ConsumptionTypeCode] = field(
        default=None,
        metadata={
            "name": "ConsumptionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    current_charge_type: Optional[CurrentChargeType] = field(
        default=None,
        metadata={
            "name": "CurrentChargeType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    current_charge_type_code: Optional[CurrentChargeTypeCode] = field(
        default=None,
        metadata={
            "name": "CurrentChargeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    one_time_charge_type: Optional[OneTimeChargeType] = field(
        default=None,
        metadata={
            "name": "OneTimeChargeType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    one_time_charge_type_code: Optional[OneTimeChargeTypeCode] = field(
        default=None,
        metadata={
            "name": "OneTimeChargeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_category: Optional[TaxCategory] = field(
        default=None,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract: Optional[Contract] = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CallDuty(DutyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DependentPriceReference(DependentPriceReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Duty(DutyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EnergyWaterSupply(EnergyWaterSupplyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EnvironmentalEmission(EnvironmentalEmissionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinancialAccount(FinancialAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinancingFinancialAccount(FinancialAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FrameworkAgreement(FrameworkAgreementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LineResponse(LineResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OrderLineReference(OrderLineReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PayeeFinancialAccount(FinancialAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PayerFinancialAccount(FinancialAccountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PaymentAlternativeExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PaymentExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PricingExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ProjectReference(ProjectReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedTenderTotal(RequestedTenderTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TaxExchangeRate(ExchangeRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TaxSubtotal(TaxSubtotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TimeDuty(DutyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UtilityItem(UtilityItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PaymentTermsType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_means_id: tuple[PaymentMeansId, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentMeansID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    prepaid_payment_reference_id: Optional[PrepaidPaymentReferenceId] = field(
        default=None,
        metadata={
            "name": "PrepaidPaymentReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reference_event_code: Optional[ReferenceEventCode] = field(
        default=None,
        metadata={
            "name": "ReferenceEventCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    settlement_discount_percent: Optional[SettlementDiscountPercent] = field(
        default=None,
        metadata={
            "name": "SettlementDiscountPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    penalty_surcharge_percent: Optional[PenaltySurchargePercent] = field(
        default=None,
        metadata={
            "name": "PenaltySurchargePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_percent: Optional[PaymentPercent] = field(
        default=None,
        metadata={
            "name": "PaymentPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    settlement_discount_amount: Optional[SettlementDiscountAmount] = field(
        default=None,
        metadata={
            "name": "SettlementDiscountAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    penalty_amount: Optional[PenaltyAmount] = field(
        default=None,
        metadata={
            "name": "PenaltyAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_terms_details_uri: Optional[PaymentTermsDetailsUri] = field(
        default=None,
        metadata={
            "name": "PaymentTermsDetailsURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_due_date: Optional[PaymentDueDate] = field(
        default=None,
        metadata={
            "name": "PaymentDueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    installment_due_date: Optional[InstallmentDueDate] = field(
        default=None,
        metadata={
            "name": "InstallmentDueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoicing_party_reference: Optional[InvoicingPartyReference] = field(
        default=None,
        metadata={
            "name": "InvoicingPartyReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    settlement_period: Optional[SettlementPeriod] = field(
        default=None,
        metadata={
            "name": "SettlementPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    penalty_period: Optional[PenaltyPeriod] = field(
        default=None,
        metadata={
            "name": "PenaltyPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exchange_rate: Optional[ExchangeRate] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PersonType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    first_name: Optional[FirstName] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    family_name: Optional[FamilyName] = field(
        default=None,
        metadata={
            "name": "FamilyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    middle_name: Optional[MiddleName] = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    other_name: Optional[OtherName] = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name_suffix: Optional[NameSuffix] = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    job_title: Optional[JobTitle] = field(
        default=None,
        metadata={
            "name": "JobTitle",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nationality_id: Optional[NationalityId] = field(
        default=None,
        metadata={
            "name": "NationalityID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gender_code: Optional[GenderCode] = field(
        default=None,
        metadata={
            "name": "GenderCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    birth_date: Optional[BirthDate] = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    birthplace_name: Optional[BirthplaceName] = field(
        default=None,
        metadata={
            "name": "BirthplaceName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    organization_department: Optional[OrganizationDepartment] = field(
        default=None,
        metadata={
            "name": "OrganizationDepartment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    financial_account: Optional[FinancialAccount] = field(
        default=None,
        metadata={
            "name": "FinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    identity_document_reference: tuple[IdentityDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "IdentityDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    residence_address: Optional[ResidenceAddress] = field(
        default=None,
        metadata={
            "name": "ResidenceAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TaxTotalType:
    tax_amount: Optional[TaxAmount] = field(
        default=None,
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    rounding_amount: Optional[RoundingAmount] = field(
        default=None,
        metadata={
            "name": "RoundingAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_evidence_indicator: Optional[TaxEvidenceIndicator] = field(
        default=None,
        metadata={
            "name": "TaxEvidenceIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_included_indicator: Optional[TaxIncludedIndicator] = field(
        default=None,
        metadata={
            "name": "TaxIncludedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_subtotal: tuple[TaxSubtotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxSubtotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class BonusPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CollectPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CommissionPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CrewMemberPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DisbursementPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DriverPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MasterPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PassengerPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PenaltyPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Person(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PrepaidPaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReportingPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SecurityOfficerPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ServiceChargePaymentTerms(PaymentTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ShipsSurgeonPerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TaxTotal(TaxTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TechnicalCommitteePerson(PersonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class WithholdingTaxTotal(TaxTotalType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AwardingTermsType:
    weighting_algorithm_code: Optional[WeightingAlgorithmCode] = field(
        default=None,
        metadata={
            "name": "WeightingAlgorithmCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    technical_committee_description: tuple[
        TechnicalCommitteeDescription, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "TechnicalCommitteeDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    low_tenders_description: tuple[LowTendersDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "LowTendersDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    prize_indicator: Optional[PrizeIndicator] = field(
        default=None,
        metadata={
            "name": "PrizeIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    prize_description: tuple[PrizeDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PrizeDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_description: tuple[PaymentDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    followup_contract_indicator: Optional[FollowupContractIndicator] = field(
        default=None,
        metadata={
            "name": "FollowupContractIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    binding_on_buyer_indicator: Optional[BindingOnBuyerIndicator] = field(
        default=None,
        metadata={
            "name": "BindingOnBuyerIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    awarding_criterion: tuple[AwardingCriterion, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AwardingCriterion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    technical_committee_person: tuple[TechnicalCommitteePerson, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TechnicalCommitteePerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class OnAccountPaymentType:
    estimated_consumed_quantity: Optional[EstimatedConsumedQuantity] = field(
        default=None,
        metadata={
            "name": "EstimatedConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_terms: tuple[PaymentTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class PartyType:
    mark_care_indicator: Optional[MarkCareIndicator] = field(
        default=None,
        metadata={
            "name": "MarkCareIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mark_attention_indicator: Optional[MarkAttentionIndicator] = field(
        default=None,
        metadata={
            "name": "MarkAttentionIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    website_uri: Optional[WebsiteUri] = field(
        default=None,
        metadata={
            "name": "WebsiteURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    logo_reference_id: Optional[LogoReferenceId] = field(
        default=None,
        metadata={
            "name": "LogoReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    endpoint_id: Optional[EndpointId] = field(
        default=None,
        metadata={
            "name": "EndpointID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    industry_classification_code: Optional[IndustryClassificationCode] = field(
        default=None,
        metadata={
            "name": "IndustryClassificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party_identification: tuple[PartyIdentification, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PartyIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    party_name: tuple[PartyName, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PartyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    physical_location: Optional[PhysicalLocation] = field(
        default=None,
        metadata={
            "name": "PhysicalLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    party_tax_scheme: tuple[PartyTaxScheme, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PartyTaxScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    party_legal_entity: tuple["PartyLegalEntity", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PartyLegalEntity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    person: tuple[Person, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Person",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    agent_party: Optional["AgentParty"] = field(
        default=None,
        metadata={
            "name": "AgentParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    service_provider_party: tuple["ServiceProviderParty", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ServiceProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    power_of_attorney: tuple["PowerOfAttorney", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PowerOfAttorney",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    financial_account: Optional[FinancialAccount] = field(
        default=None,
        metadata={
            "name": "FinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PriceExtensionType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class AdditionalInformationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AgentParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AppealInformationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AppealReceiverParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AwardingTerms(AwardingTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BeneficiaryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BillOfLadingHolderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BillToParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CarrierParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsigneeParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsignorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContactParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractResponsibleParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CustomsAgentParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeliveryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DespatchParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DocumentProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EvidenceIssuingParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExporterParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinalDeliveryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinancingParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FreightForwarderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class GuarantorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class HazardousItemNotificationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class HeadOfficeParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ImporterParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InformationContentProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InsuranceParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InterestedParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InventoryReportingParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class IssuerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemPriceExtension(PriceExtensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LoadingProofParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LogisticsOperatorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MainOnAccountPayment(OnAccountPaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ManufacturerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MediationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MortgageHolderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class NotaryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class NotifyParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OnAccountPayment(OnAccountPaymentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OperatingParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginalDespatchParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginatorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OwnerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Party(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PayeeParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PayerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PerformingCarrierParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PickupParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PreSelectedParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PreparationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PriceExtension(PriceExtensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReceiverParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RecipientParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ResponsibleTransportServiceProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SenderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SignatoryParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SourceIssuerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubcontractorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubscriberParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubstituteCarrierParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TaxRepresentativeParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderEvaluationParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderRecipientParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TendererParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TerminalOperatorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportAdvisorParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportServiceProviderParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportUserParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UtilityCustomerParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UtilitySupplierParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class WarrantyParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class WitnessParty(PartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AppealTermsType:
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    presentation_period: Optional[PresentationPeriod] = field(
        default=None,
        metadata={
            "name": "PresentationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    appeal_information_party: Optional[AppealInformationParty] = field(
        default=None,
        metadata={
            "name": "AppealInformationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    appeal_receiver_party: Optional[AppealReceiverParty] = field(
        default=None,
        metadata={
            "name": "AppealReceiverParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    mediation_party: Optional[MediationParty] = field(
        default=None,
        metadata={
            "name": "MediationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ContractingPartyType1:
    class Meta:
        name = "ContractingPartyType"

    buyer_profile_uri: Optional[BuyerProfileUri] = field(
        default=None,
        metadata={
            "name": "BuyerProfileURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contracting_party_type: tuple[ContractingPartyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContractingPartyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contracting_activity: tuple[ContractingActivity, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContractingActivity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class CustomerPartyType:
    customer_assigned_account_id: Optional[CustomerAssignedAccountId] = field(
        default=None,
        metadata={
            "name": "CustomerAssignedAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    supplier_assigned_account_id: Optional[SupplierAssignedAccountId] = field(
        default=None,
        metadata={
            "name": "SupplierAssignedAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    additional_account_id: tuple[AdditionalAccountId, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_contact: Optional[DeliveryContact] = field(
        default=None,
        metadata={
            "name": "DeliveryContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_contact: Optional[AccountingContact] = field(
        default=None,
        metadata={
            "name": "AccountingContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    buyer_contact: Optional[BuyerContact] = field(
        default=None,
        metadata={
            "name": "BuyerContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CustomsDeclarationType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DespatchType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    requested_despatch_date: Optional[RequestedDespatchDate] = field(
        default=None,
        metadata={
            "name": "RequestedDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    requested_despatch_time: Optional[RequestedDespatchTime] = field(
        default=None,
        metadata={
            "name": "RequestedDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_despatch_date: Optional[EstimatedDespatchDate] = field(
        default=None,
        metadata={
            "name": "EstimatedDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_despatch_time: Optional[EstimatedDespatchTime] = field(
        default=None,
        metadata={
            "name": "EstimatedDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_despatch_date: Optional[ActualDespatchDate] = field(
        default=None,
        metadata={
            "name": "ActualDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_despatch_time: Optional[ActualDespatchTime] = field(
        default=None,
        metadata={
            "name": "ActualDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    guaranteed_despatch_date: Optional[GuaranteedDespatchDate] = field(
        default=None,
        metadata={
            "name": "GuaranteedDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    guaranteed_despatch_time: Optional[GuaranteedDespatchTime] = field(
        default=None,
        metadata={
            "name": "GuaranteedDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    release_id: Optional[ReleaseId] = field(
        default=None,
        metadata={
            "name": "ReleaseID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    instructions: tuple[Instructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Instructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    despatch_address: Optional[DespatchAddress] = field(
        default=None,
        metadata={
            "name": "DespatchAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_location: Optional[DespatchLocation] = field(
        default=None,
        metadata={
            "name": "DespatchLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_party: Optional[DespatchParty] = field(
        default=None,
        metadata={
            "name": "DespatchParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    carrier_party: Optional[CarrierParty] = field(
        default=None,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    notify_party: tuple[NotifyParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NotifyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_despatch_period: Optional[EstimatedDespatchPeriod] = field(
        default=None,
        metadata={
            "name": "EstimatedDespatchPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_despatch_period: Optional[RequestedDespatchPeriod] = field(
        default=None,
        metadata={
            "name": "RequestedDespatchPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DocumentDistributionType:
    print_qualifier: Optional[PrintQualifier] = field(
        default=None,
        metadata={
            "name": "PrintQualifier",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    maximum_copies_numeric: Optional[MaximumCopiesNumeric] = field(
        default=None,
        metadata={
            "name": "MaximumCopiesNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class DocumentResponseType:
    response: Optional[Response] = field(
        default=None,
        metadata={
            "name": "Response",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    recipient_party: Optional[RecipientParty] = field(
        default=None,
        metadata={
            "name": "RecipientParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    line_response: tuple[LineResponse, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "LineResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EconomicOperatorShortListType:
    limitation_description: tuple[LimitationDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "LimitationDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expected_quantity: Optional[ExpectedQuantity] = field(
        default=None,
        metadata={
            "name": "ExpectedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pre_selected_party: tuple[PreSelectedParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PreSelectedParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EndorserPartyType:
    role_code: Optional[RoleCode] = field(
        default=None,
        metadata={
            "name": "RoleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    signatory_contact: Optional[SignatoryContact] = field(
        default=None,
        metadata={
            "name": "SignatoryContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class EvidenceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    evidence_type_code: Optional[EvidenceTypeCode] = field(
        default=None,
        metadata={
            "name": "EvidenceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    candidate_statement: tuple[CandidateStatement, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CandidateStatement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    evidence_issuing_party: Optional[EvidenceIssuingParty] = field(
        default=None,
        metadata={
            "name": "EvidenceIssuingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: Optional[DocumentReference] = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class HazardousItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    placard_notation: Optional[PlacardNotation] = field(
        default=None,
        metadata={
            "name": "PlacardNotation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    placard_endorsement: Optional[PlacardEndorsement] = field(
        default=None,
        metadata={
            "name": "PlacardEndorsement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    additional_information: tuple[AdditionalInformation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    undgcode: Optional[Undgcode] = field(
        default=None,
        metadata={
            "name": "UNDGCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    emergency_procedures_code: Optional[EmergencyProceduresCode] = field(
        default=None,
        metadata={
            "name": "EmergencyProceduresCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    medical_first_aid_guide_code: Optional[MedicalFirstAidGuideCode] = field(
        default=None,
        metadata={
            "name": "MedicalFirstAidGuideCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    technical_name: Optional[TechnicalName] = field(
        default=None,
        metadata={
            "name": "TechnicalName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    category_name: Optional[CategoryName] = field(
        default=None,
        metadata={
            "name": "CategoryName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_category_code: Optional[HazardousCategoryCode] = field(
        default=None,
        metadata={
            "name": "HazardousCategoryCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    upper_orange_hazard_placard_id: Optional[UpperOrangeHazardPlacardId] = (
        field(
            default=None,
            metadata={
                "name": "UpperOrangeHazardPlacardID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    lower_orange_hazard_placard_id: Optional[LowerOrangeHazardPlacardId] = (
        field(
            default=None,
            metadata={
                "name": "LowerOrangeHazardPlacardID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    marking_id: Optional[MarkingId] = field(
        default=None,
        metadata={
            "name": "MarkingID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazard_class_id: Optional[HazardClassId] = field(
        default=None,
        metadata={
            "name": "HazardClassID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_weight_measure: Optional[NetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_volume_measure: Optional[NetVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contact_party: Optional[ContactParty] = field(
        default=None,
        metadata={
            "name": "ContactParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    secondary_hazard: tuple[SecondaryHazard, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SecondaryHazard",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    hazardous_goods_transit: tuple[HazardousGoodsTransit, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HazardousGoodsTransit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    emergency_temperature: Optional[EmergencyTemperature] = field(
        default=None,
        metadata={
            "name": "EmergencyTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    flashpoint_temperature: Optional[FlashpointTemperature] = field(
        default=None,
        metadata={
            "name": "FlashpointTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    additional_temperature: tuple[AdditionalTemperature, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ImmobilizedSecurityType:
    immobilization_certificate_id: Optional[ImmobilizationCertificateId] = (
        field(
            default=None,
            metadata={
                "name": "ImmobilizationCertificateID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    security_id: Optional[SecurityId] = field(
        default=None,
        metadata={
            "name": "SecurityID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    face_value_amount: Optional[FaceValueAmount] = field(
        default=None,
        metadata={
            "name": "FaceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    market_value_amount: Optional[MarketValueAmount] = field(
        default=None,
        metadata={
            "name": "MarketValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    shares_number_quantity: Optional[SharesNumberQuantity] = field(
        default=None,
        metadata={
            "name": "SharesNumberQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemIdentificationType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    extended_id: Optional[ExtendedId] = field(
        default=None,
        metadata={
            "name": "ExtendedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    barcode_symbology_id: Optional[BarcodeSymbologyId] = field(
        default=None,
        metadata={
            "name": "BarcodeSymbologyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    physical_attribute: tuple[PhysicalAttribute, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PhysicalAttribute",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    measurement_dimension: tuple[MeasurementDimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class NotificationRequirementType:
    notification_type_code: Optional[NotificationTypeCode] = field(
        default=None,
        metadata={
            "name": "NotificationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    post_event_notification_duration_measure: Optional[
        PostEventNotificationDurationMeasure
    ] = field(
        default=None,
        metadata={
            "name": "PostEventNotificationDurationMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pre_event_notification_duration_measure: Optional[
        PreEventNotificationDurationMeasure
    ] = field(
        default=None,
        metadata={
            "name": "PreEventNotificationDurationMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    notify_party: tuple[NotifyParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NotifyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    notification_period: tuple[NotificationPeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NotificationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    notification_location: tuple[NotificationLocation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NotificationLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PaymentMandateType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mandate_type_code: Optional[MandateTypeCode] = field(
        default=None,
        metadata={
            "name": "MandateTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_payment_instructions_numeric: Optional[
        MaximumPaymentInstructionsNumeric
    ] = field(
        default=None,
        metadata={
            "name": "MaximumPaymentInstructionsNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_paid_amount: Optional[MaximumPaidAmount] = field(
        default=None,
        metadata={
            "name": "MaximumPaidAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    signature_id: Optional[SignatureId] = field(
        default=None,
        metadata={
            "name": "SignatureID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payer_party: Optional[PayerParty] = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payer_financial_account: Optional[PayerFinancialAccount] = field(
        default=None,
        metadata={
            "name": "PayerFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    validity_period: Optional[ValidityPeriod] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_reversal_period: Optional[PaymentReversalPeriod] = field(
        default=None,
        metadata={
            "name": "PaymentReversalPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    clause: tuple[Clause, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Clause",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PickupType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_pickup_date: Optional[ActualPickupDate] = field(
        default=None,
        metadata={
            "name": "ActualPickupDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_pickup_time: Optional[ActualPickupTime] = field(
        default=None,
        metadata={
            "name": "ActualPickupTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    earliest_pickup_date: Optional[EarliestPickupDate] = field(
        default=None,
        metadata={
            "name": "EarliestPickupDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    earliest_pickup_time: Optional[EarliestPickupTime] = field(
        default=None,
        metadata={
            "name": "EarliestPickupTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_pickup_date: Optional[LatestPickupDate] = field(
        default=None,
        metadata={
            "name": "LatestPickupDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_pickup_time: Optional[LatestPickupTime] = field(
        default=None,
        metadata={
            "name": "LatestPickupTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pickup_location: Optional[PickupLocation] = field(
        default=None,
        metadata={
            "name": "PickupLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pickup_party: Optional[PickupParty] = field(
        default=None,
        metadata={
            "name": "PickupParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PowerOfAttorneyType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: Optional[IssueDate] = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: Optional[IssueTime] = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    notary_party: Optional[NotaryParty] = field(
        default=None,
        metadata={
            "name": "NotaryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    agent_party: Optional[AgentParty] = field(
        default=None,
        metadata={
            "name": "AgentParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    witness_party: tuple[WitnessParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "WitnessParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    mandate_document_reference: tuple[MandateDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MandateDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ResultOfVerificationType:
    validator_id: Optional[ValidatorId] = field(
        default=None,
        metadata={
            "name": "ValidatorID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validation_result_code: Optional[ValidationResultCode] = field(
        default=None,
        metadata={
            "name": "ValidationResultCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validation_date: Optional[ValidationDate] = field(
        default=None,
        metadata={
            "name": "ValidationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validation_time: Optional[ValidationTime] = field(
        default=None,
        metadata={
            "name": "ValidationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validate_process: Optional[ValidateProcess] = field(
        default=None,
        metadata={
            "name": "ValidateProcess",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validate_tool: Optional[ValidateTool] = field(
        default=None,
        metadata={
            "name": "ValidateTool",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validate_tool_version: Optional[ValidateToolVersion] = field(
        default=None,
        metadata={
            "name": "ValidateToolVersion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    signatory_party: Optional[SignatoryParty] = field(
        default=None,
        metadata={
            "name": "SignatoryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ServiceProviderPartyType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    service_type_code: Optional[ServiceTypeCode] = field(
        default=None,
        metadata={
            "name": "ServiceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    service_type: tuple[ServiceType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ServiceType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    seller_contact: Optional[SellerContact] = field(
        default=None,
        metadata={
            "name": "SellerContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ShareholderPartyType:
    partecipation_percent: Optional[PartecipationPercent] = field(
        default=None,
        metadata={
            "name": "PartecipationPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class SignatureType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validation_date: Optional[ValidationDate] = field(
        default=None,
        metadata={
            "name": "ValidationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validation_time: Optional[ValidationTime] = field(
        default=None,
        metadata={
            "name": "ValidationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validator_id: Optional[ValidatorId] = field(
        default=None,
        metadata={
            "name": "ValidatorID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    canonicalization_method: Optional[CanonicalizationMethod] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    signature_method: Optional[SignatureMethod] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    signatory_party: Optional[SignatoryParty] = field(
        default=None,
        metadata={
            "name": "SignatoryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    digital_signature_attachment: Optional[DigitalSignatureAttachment] = field(
        default=None,
        metadata={
            "name": "DigitalSignatureAttachment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    original_document_reference: Optional[OriginalDocumentReference] = field(
        default=None,
        metadata={
            "name": "OriginalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class SupplierPartyType:
    customer_assigned_account_id: Optional[CustomerAssignedAccountId] = field(
        default=None,
        metadata={
            "name": "CustomerAssignedAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    additional_account_id: tuple[AdditionalAccountId, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    data_sending_capability: Optional[DataSendingCapability] = field(
        default=None,
        metadata={
            "name": "DataSendingCapability",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_contact: Optional[DespatchContact] = field(
        default=None,
        metadata={
            "name": "DespatchContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_contact: Optional[AccountingContact] = field(
        default=None,
        metadata={
            "name": "AccountingContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_contact: Optional[SellerContact] = field(
        default=None,
        metadata={
            "name": "SellerContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TradeFinancingType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    financing_instrument_code: Optional[FinancingInstrumentCode] = field(
        default=None,
        metadata={
            "name": "FinancingInstrumentCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract_document_reference: Optional[ContractDocumentReference] = field(
        default=None,
        metadata={
            "name": "ContractDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    financing_party: Optional[FinancingParty] = field(
        default=None,
        metadata={
            "name": "FinancingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    financing_financial_account: Optional[FinancingFinancialAccount] = field(
        default=None,
        metadata={
            "name": "FinancingFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    clause: tuple[Clause, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Clause",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransportMeansType:
    journey_id: Optional[JourneyId] = field(
        default=None,
        metadata={
            "name": "JourneyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_nationality_id: Optional[RegistrationNationalityId] = field(
        default=None,
        metadata={
            "name": "RegistrationNationalityID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_nationality: tuple[RegistrationNationality, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RegistrationNationality",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    direction_code: Optional[DirectionCode] = field(
        default=None,
        metadata={
            "name": "DirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_means_type_code: Optional[TransportMeansTypeCode] = field(
        default=None,
        metadata={
            "name": "TransportMeansTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trade_service_code: Optional[TradeServiceCode] = field(
        default=None,
        metadata={
            "name": "TradeServiceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    stowage: Optional[Stowage] = field(
        default=None,
        metadata={
            "name": "Stowage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    air_transport: Optional[AirTransport] = field(
        default=None,
        metadata={
            "name": "AirTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    road_transport: Optional[RoadTransport] = field(
        default=None,
        metadata={
            "name": "RoadTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    rail_transport: Optional[RailTransport] = field(
        default=None,
        metadata={
            "name": "RailTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maritime_transport: Optional[MaritimeTransport] = field(
        default=None,
        metadata={
            "name": "MaritimeTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    owner_party: Optional[OwnerParty] = field(
        default=None,
        metadata={
            "name": "OwnerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    measurement_dimension: tuple[MeasurementDimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class WinningPartyType:
    rank: Optional[Rank] = field(
        default=None,
        metadata={
            "name": "Rank",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class AccountingCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AccountingSupplierParty(SupplierPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AdditionalDocumentResponse(DocumentResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AdditionalItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AppealTerms(AppealTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ApplicableTransportMeans(TransportMeansType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BuyerCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BuyersItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CatalogueItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractingParty(ContractingPartyType1):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractorCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CustomsDeclaration(CustomsDeclarationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeliveryCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Despatch(DespatchType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DespatchSupplierParty(SupplierPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DocumentDistribution(DocumentDistributionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DocumentResponse(DocumentResponseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EconomicOperatorShortList(EconomicOperatorShortListType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EndorserParty(EndorserPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Evidence(EvidenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class HazardousItem(HazardousItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ImmobilizedSecurity(ImmobilizedSecurityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ManufacturersItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class NotificationRequirement(NotificationRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginatorCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PaymentMandate(PaymentMandateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Pickup(PickupType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PowerOfAttorney(PowerOfAttorneyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RecipientCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ResultOfVerification(ResultOfVerificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RetailerCustomerParty(CustomerPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SellerSupplierParty(SupplierPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SellersItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ServiceProviderParty(ServiceProviderPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ShareholderParty(ShareholderPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Signature(SignatureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class StandardItemIdentification(ItemIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SuggestedEvidence(EvidenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SupplierParty(SupplierPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TradeFinancing(TradeFinancingType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportMeans(TransportMeansType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class WinningParty(WinningPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CertificateType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    certificate_type_code: Optional[CertificateTypeCode] = field(
        default=None,
        metadata={
            "name": "CertificateTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    certificate_type: Optional[UblCommonBasicComponents21CertificateType] = (
        field(
            default=None,
            metadata={
                "name": "CertificateType",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
                "required": True,
            },
        )
    )
    remarks: tuple[Remarks, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    signature: tuple[Signature, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CompletedTaskType:
    annual_average_amount: Optional[AnnualAverageAmount] = field(
        default=None,
        metadata={
            "name": "AnnualAverageAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_task_amount: Optional[TotalTaskAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaskAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party_capacity_amount: Optional[PartyCapacityAmount] = field(
        default=None,
        metadata={
            "name": "PartyCapacityAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    evidence_supplied: tuple[EvidenceSupplied, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EvidenceSupplied",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    recipient_customer_party: Optional[RecipientCustomerParty] = field(
        default=None,
        metadata={
            "name": "RecipientCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EndorsementType:
    document_id: Optional[DocumentId] = field(
        default=None,
        metadata={
            "name": "DocumentID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    approval_status: Optional[ApprovalStatus] = field(
        default=None,
        metadata={
            "name": "ApprovalStatus",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    remarks: tuple[Remarks, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    endorser_party: Optional[EndorserParty] = field(
        default=None,
        metadata={
            "name": "EndorserParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    signature: tuple[Signature, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EvaluationCriterionType:
    evaluation_criterion_type_code: Optional[EvaluationCriterionTypeCode] = (
        field(
            default=None,
            metadata={
                "name": "EvaluationCriterionTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    threshold_amount: Optional[ThresholdAmount] = field(
        default=None,
        metadata={
            "name": "ThresholdAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    threshold_quantity: Optional[ThresholdQuantity] = field(
        default=None,
        metadata={
            "name": "ThresholdQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expression_code: Optional[ExpressionCode] = field(
        default=None,
        metadata={
            "name": "ExpressionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expression: tuple[Expression, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Expression",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    duration_period: Optional[DurationPeriod] = field(
        default=None,
        metadata={
            "name": "DurationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    suggested_evidence: tuple[SuggestedEvidence, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SuggestedEvidence",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PartyLegalEntityType:
    registration_name: Optional[RegistrationName] = field(
        default=None,
        metadata={
            "name": "RegistrationName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_id: Optional[CompanyId] = field(
        default=None,
        metadata={
            "name": "CompanyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_date: Optional[RegistrationDate] = field(
        default=None,
        metadata={
            "name": "RegistrationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_expiration_date: Optional[RegistrationExpirationDate] = field(
        default=None,
        metadata={
            "name": "RegistrationExpirationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_legal_form_code: Optional[CompanyLegalFormCode] = field(
        default=None,
        metadata={
            "name": "CompanyLegalFormCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_legal_form: Optional[CompanyLegalForm] = field(
        default=None,
        metadata={
            "name": "CompanyLegalForm",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sole_proprietorship_indicator: Optional[SoleProprietorshipIndicator] = (
        field(
            default=None,
            metadata={
                "name": "SoleProprietorshipIndicator",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    company_liquidation_status_code: Optional[CompanyLiquidationStatusCode] = (
        field(
            default=None,
            metadata={
                "name": "CompanyLiquidationStatusCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    corporate_stock_amount: Optional[CorporateStockAmount] = field(
        default=None,
        metadata={
            "name": "CorporateStockAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fully_paid_shares_indicator: Optional[FullyPaidSharesIndicator] = field(
        default=None,
        metadata={
            "name": "FullyPaidSharesIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_address: Optional[RegistrationAddress] = field(
        default=None,
        metadata={
            "name": "RegistrationAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    corporate_registration_scheme: Optional[CorporateRegistrationScheme] = (
        field(
            default=None,
            metadata={
                "name": "CorporateRegistrationScheme",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    head_office_party: Optional[HeadOfficeParty] = field(
        default=None,
        metadata={
            "name": "HeadOfficeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shareholder_party: tuple[ShareholderParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ShareholderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PaymentMeansType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_means_code: Optional[PaymentMeansCode] = field(
        default=None,
        metadata={
            "name": "PaymentMeansCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    payment_due_date: Optional[PaymentDueDate] = field(
        default=None,
        metadata={
            "name": "PaymentDueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_channel_code: Optional[PaymentChannelCode] = field(
        default=None,
        metadata={
            "name": "PaymentChannelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    instruction_id: Optional[InstructionId] = field(
        default=None,
        metadata={
            "name": "InstructionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    instruction_note: tuple[InstructionNote, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "InstructionNote",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_id: tuple[PaymentId, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    card_account: Optional[CardAccount] = field(
        default=None,
        metadata={
            "name": "CardAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payer_financial_account: Optional[PayerFinancialAccount] = field(
        default=None,
        metadata={
            "name": "PayerFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payee_financial_account: Optional[PayeeFinancialAccount] = field(
        default=None,
        metadata={
            "name": "PayeeFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    credit_account: Optional[CreditAccount] = field(
        default=None,
        metadata={
            "name": "CreditAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_mandate: Optional[PaymentMandate] = field(
        default=None,
        metadata={
            "name": "PaymentMandate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    trade_financing: Optional[TradeFinancing] = field(
        default=None,
        metadata={
            "name": "TradeFinancing",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TendererRequirementType:
    name: tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tenderer_requirement_type_code: Optional[TendererRequirementTypeCode] = (
        field(
            default=None,
            metadata={
                "name": "TendererRequirementTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    legal_reference: Optional[LegalReference] = field(
        default=None,
        metadata={
            "name": "LegalReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    suggested_evidence: tuple[SuggestedEvidence, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SuggestedEvidence",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TenderingProcessType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    original_contracting_system_id: Optional[OriginalContractingSystemId] = (
        field(
            default=None,
            metadata={
                "name": "OriginalContractingSystemID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    negotiation_description: tuple[NegotiationDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NegotiationDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    procedure_code: Optional[ProcedureCode] = field(
        default=None,
        metadata={
            "name": "ProcedureCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    urgency_code: Optional[UrgencyCode] = field(
        default=None,
        metadata={
            "name": "UrgencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expense_code: Optional[ExpenseCode] = field(
        default=None,
        metadata={
            "name": "ExpenseCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    part_presentation_code: Optional[PartPresentationCode] = field(
        default=None,
        metadata={
            "name": "PartPresentationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contracting_system_code: Optional[ContractingSystemCode] = field(
        default=None,
        metadata={
            "name": "ContractingSystemCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    submission_method_code: Optional[SubmissionMethodCode] = field(
        default=None,
        metadata={
            "name": "SubmissionMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    candidate_reduction_constraint_indicator: Optional[
        CandidateReductionConstraintIndicator
    ] = field(
        default=None,
        metadata={
            "name": "CandidateReductionConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    government_agreement_constraint_indicator: Optional[
        GovernmentAgreementConstraintIndicator
    ] = field(
        default=None,
        metadata={
            "name": "GovernmentAgreementConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_availability_period: Optional[DocumentAvailabilityPeriod] = field(
        default=None,
        metadata={
            "name": "DocumentAvailabilityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_submission_deadline_period: Optional[
        TenderSubmissionDeadlinePeriod
    ] = field(
        default=None,
        metadata={
            "name": "TenderSubmissionDeadlinePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    invitation_submission_period: Optional[InvitationSubmissionPeriod] = field(
        default=None,
        metadata={
            "name": "InvitationSubmissionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    participation_request_reception_period: Optional[
        ParticipationRequestReceptionPeriod
    ] = field(
        default=None,
        metadata={
            "name": "ParticipationRequestReceptionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    notice_document_reference: tuple[NoticeDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NoticeDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    additional_document_reference: tuple[AdditionalDocumentReference, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "AdditionalDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    process_justification: tuple[ProcessJustification, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ProcessJustification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    economic_operator_short_list: Optional[EconomicOperatorShortList] = field(
        default=None,
        metadata={
            "name": "EconomicOperatorShortList",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    open_tender_event: tuple[OpenTenderEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OpenTenderEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    auction_terms: Optional[AuctionTerms] = field(
        default=None,
        metadata={
            "name": "AuctionTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    framework_agreement: Optional[FrameworkAgreement] = field(
        default=None,
        metadata={
            "name": "FrameworkAgreement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class Certificate(CertificateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CompletedTask(CompletedTaskType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EmbassyEndorsement(EndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Endorsement(EndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EvaluationCriterion(EvaluationCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinancialEvaluationCriterion(EvaluationCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InsuranceEndorsement(EndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class IssuerEndorsement(EndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PartyLegalEntity(PartyLegalEntityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PaymentMeans(PaymentMeansType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SpecificTendererRequirement(TendererRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TechnicalEvaluationCriterion(EvaluationCriterionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TendererRequirement(TendererRequirementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderingProcess(TenderingProcessType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AllowanceChargeType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    charge_indicator: Optional[ChargeIndicator] = field(
        default=None,
        metadata={
            "name": "ChargeIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    allowance_charge_reason_code: Optional[AllowanceChargeReasonCode] = field(
        default=None,
        metadata={
            "name": "AllowanceChargeReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    allowance_charge_reason: tuple[AllowanceChargeReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceChargeReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    multiplier_factor_numeric: Optional[MultiplierFactorNumeric] = field(
        default=None,
        metadata={
            "name": "MultiplierFactorNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    prepaid_indicator: Optional[PrepaidIndicator] = field(
        default=None,
        metadata={
            "name": "PrepaidIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    base_amount: Optional[BaseAmount] = field(
        default=None,
        metadata={
            "name": "BaseAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    per_unit_amount: Optional[PerUnitAmount] = field(
        default=None,
        metadata={
            "name": "PerUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_category: tuple[TaxCategory, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: Optional[TaxTotal] = field(
        default=None,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_means: tuple[PaymentMeans, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemType:
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pack_quantity: Optional[PackQuantity] = field(
        default=None,
        metadata={
            "name": "PackQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pack_size_numeric: Optional[PackSizeNumeric] = field(
        default=None,
        metadata={
            "name": "PackSizeNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    catalogue_indicator: Optional[CatalogueIndicator] = field(
        default=None,
        metadata={
            "name": "CatalogueIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_risk_indicator: Optional[HazardousRiskIndicator] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    additional_information: tuple[AdditionalInformation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    keyword: tuple[Keyword, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Keyword",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    brand_name: tuple[BrandName, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BrandName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    model_name: tuple[ModelName, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ModelName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    buyers_item_identification: Optional[BuyersItemIdentification] = field(
        default=None,
        metadata={
            "name": "BuyersItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sellers_item_identification: Optional[SellersItemIdentification] = field(
        default=None,
        metadata={
            "name": "SellersItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    manufacturers_item_identification: tuple[
        ManufacturersItemIdentification, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "ManufacturersItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    standard_item_identification: Optional[StandardItemIdentification] = field(
        default=None,
        metadata={
            "name": "StandardItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    catalogue_item_identification: Optional[CatalogueItemIdentification] = (
        field(
            default=None,
            metadata={
                "name": "CatalogueItemIdentification",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    additional_item_identification: tuple[
        AdditionalItemIdentification, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    catalogue_document_reference: Optional[CatalogueDocumentReference] = field(
        default=None,
        metadata={
            "name": "CatalogueDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_specification_document_reference: tuple[
        ItemSpecificationDocumentReference, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "ItemSpecificationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    origin_country: Optional[OriginCountry] = field(
        default=None,
        metadata={
            "name": "OriginCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    commodity_classification: tuple[CommodityClassification, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transaction_conditions: tuple[TransactionConditions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransactionConditions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    hazardous_item: tuple[HazardousItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HazardousItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    classified_tax_category: tuple[ClassifiedTaxCategory, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ClassifiedTaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    additional_item_property: tuple[AdditionalItemProperty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalItemProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    manufacturer_party: tuple[ManufacturerParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ManufacturerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    information_content_provider_party: Optional[
        InformationContentProviderParty
    ] = field(
        default=None,
        metadata={
            "name": "InformationContentProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    origin_address: tuple[OriginAddress, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OriginAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_instance: tuple[ItemInstance, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ItemInstance",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    certificate: tuple[Certificate, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Certificate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    dimension: tuple[Dimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class QualifyingPartyType:
    participation_percent: Optional[ParticipationPercent] = field(
        default=None,
        metadata={
            "name": "ParticipationPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    personal_situation: tuple[PersonalSituation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PersonalSituation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    operating_years_quantity: Optional[OperatingYearsQuantity] = field(
        default=None,
        metadata={
            "name": "OperatingYearsQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    employee_quantity: Optional[EmployeeQuantity] = field(
        default=None,
        metadata={
            "name": "EmployeeQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    business_classification_evidence_id: Optional[
        BusinessClassificationEvidenceId
    ] = field(
        default=None,
        metadata={
            "name": "BusinessClassificationEvidenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    business_identity_evidence_id: Optional[BusinessIdentityEvidenceId] = (
        field(
            default=None,
            metadata={
                "name": "BusinessIdentityEvidenceID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    tenderer_role_code: Optional[TendererRoleCode] = field(
        default=None,
        metadata={
            "name": "TendererRoleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    business_classification_scheme: Optional[BusinessClassificationScheme] = (
        field(
            default=None,
            metadata={
                "name": "BusinessClassificationScheme",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    technical_capability: tuple[TechnicalCapability, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TechnicalCapability",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    financial_capability: tuple[FinancialCapability, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FinancialCapability",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    completed_task: tuple[CompletedTask, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CompletedTask",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    declaration: tuple[Declaration, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Declaration",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    economic_operator_role: Optional[EconomicOperatorRole] = field(
        default=None,
        metadata={
            "name": "EconomicOperatorRole",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TendererQualificationRequestType:
    company_legal_form_code: Optional[CompanyLegalFormCode] = field(
        default=None,
        metadata={
            "name": "CompanyLegalFormCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_legal_form: Optional[CompanyLegalForm] = field(
        default=None,
        metadata={
            "name": "CompanyLegalForm",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    personal_situation: tuple[PersonalSituation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PersonalSituation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    operating_years_quantity: Optional[OperatingYearsQuantity] = field(
        default=None,
        metadata={
            "name": "OperatingYearsQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    employee_quantity: Optional[EmployeeQuantity] = field(
        default=None,
        metadata={
            "name": "EmployeeQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_business_classification_scheme: tuple[
        RequiredBusinessClassificationScheme, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "RequiredBusinessClassificationScheme",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    technical_evaluation_criterion: tuple[
        TechnicalEvaluationCriterion, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "TechnicalEvaluationCriterion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    financial_evaluation_criterion: tuple[
        FinancialEvaluationCriterion, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "FinancialEvaluationCriterion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    specific_tenderer_requirement: tuple[SpecificTendererRequirement, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "SpecificTendererRequirement",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    economic_operator_role: tuple[EconomicOperatorRole, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EconomicOperatorRole",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class AdditionalQualifyingParty(QualifyingPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AllowanceCharge(AllowanceChargeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExtraAllowanceCharge(AllowanceChargeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FreightAllowanceCharge(AllowanceChargeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Item(ItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MainQualifyingParty(QualifyingPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class QualifyingParty(QualifyingPartyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ServiceAllowanceCharge(AllowanceChargeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SupplyItem(ItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TendererQualificationRequest(TendererQualificationRequestType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BillingReferenceLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CatalogueItemSpecificationUpdateLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    contractor_customer_party: Optional[ContractorCustomerParty] = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class DeliveryTermsType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    special_terms: tuple[SpecialTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SpecialTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    loss_risk_responsibility_code: Optional[LossRiskResponsibilityCode] = (
        field(
            default=None,
            metadata={
                "name": "LossRiskResponsibilityCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    loss_risk: tuple[LossRisk, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "LossRisk",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivery_location: Optional[DeliveryLocation] = field(
        default=None,
        metadata={
            "name": "DeliveryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: Optional[AllowanceCharge] = field(
        default=None,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DespatchLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_status_code: Optional[LineStatusCode] = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivered_quantity: Optional[DeliveredQuantity] = field(
        default=None,
        metadata={
            "name": "DeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    backorder_quantity: Optional[BackorderQuantity] = field(
        default=None,
        metadata={
            "name": "BackorderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    backorder_reason: tuple[BackorderReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BackorderReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    outstanding_quantity: Optional[OutstandingQuantity] = field(
        default=None,
        metadata={
            "name": "OutstandingQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    outstanding_reason: tuple[OutstandingReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OutstandingReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    oversupply_quantity: Optional[OversupplyQuantity] = field(
        default=None,
        metadata={
            "name": "OversupplyQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_line_reference: tuple[OrderLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    shipment: tuple["Shipment", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EventLineItemType:
    line_number_numeric: Optional[LineNumberNumeric] = field(
        default=None,
        metadata={
            "name": "LineNumberNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    participating_locations_location: Optional[
        ParticipatingLocationsLocation
    ] = field(
        default=None,
        metadata={
            "name": "ParticipatingLocationsLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    retail_planned_impact: tuple[RetailPlannedImpact, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RetailPlannedImpact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supply_item: Optional[SupplyItem] = field(
        default=None,
        metadata={
            "name": "SupplyItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class ExceptionCriteriaLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    threshold_value_comparison_code: Optional[ThresholdValueComparisonCode] = (
        field(
            default=None,
            metadata={
                "name": "ThresholdValueComparisonCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
                "required": True,
            },
        )
    )
    threshold_quantity: Optional[ThresholdQuantity] = field(
        default=None,
        metadata={
            "name": "ThresholdQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    exception_status_code: Optional[ExceptionStatusCode] = field(
        default=None,
        metadata={
            "name": "ExceptionStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    collaboration_priority_code: Optional[CollaborationPriorityCode] = field(
        default=None,
        metadata={
            "name": "CollaborationPriorityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exception_resolution_code: Optional[ExceptionResolutionCode] = field(
        default=None,
        metadata={
            "name": "ExceptionResolutionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    supply_chain_activity_type_code: Optional[SupplyChainActivityTypeCode] = (
        field(
            default=None,
            metadata={
                "name": "SupplyChainActivityTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    performance_metric_type_code: Optional[PerformanceMetricTypeCode] = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    effective_period: Optional[EffectivePeriod] = field(
        default=None,
        metadata={
            "name": "EffectivePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supply_item: tuple[SupplyItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SupplyItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )
    forecast_exception_criterion_line: Optional[
        ForecastExceptionCriterionLine
    ] = field(
        default=None,
        metadata={
            "name": "ForecastExceptionCriterionLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ExceptionNotificationLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exception_status_code: Optional[ExceptionStatusCode] = field(
        default=None,
        metadata={
            "name": "ExceptionStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    collaboration_priority_code: Optional[CollaborationPriorityCode] = field(
        default=None,
        metadata={
            "name": "CollaborationPriorityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    resolution_code: Optional[ResolutionCode] = field(
        default=None,
        metadata={
            "name": "ResolutionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    compared_value_measure: Optional[ComparedValueMeasure] = field(
        default=None,
        metadata={
            "name": "ComparedValueMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    source_value_measure: Optional[SourceValueMeasure] = field(
        default=None,
        metadata={
            "name": "SourceValueMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    variance_quantity: Optional[VarianceQuantity] = field(
        default=None,
        metadata={
            "name": "VarianceQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    supply_chain_activity_type_code: Optional[SupplyChainActivityTypeCode] = (
        field(
            default=None,
            metadata={
                "name": "SupplyChainActivityTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    performance_metric_type_code: Optional[PerformanceMetricTypeCode] = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exception_observation_period: Optional[ExceptionObservationPeriod] = field(
        default=None,
        metadata={
            "name": "ExceptionObservationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    forecast_exception: Optional[ForecastException] = field(
        default=None,
        metadata={
            "name": "ForecastException",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supply_item: Optional[SupplyItem] = field(
        default=None,
        metadata={
            "name": "SupplyItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class InstructionForReturnsLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    manufacturer_party: Optional[ManufacturerParty] = field(
        default=None,
        metadata={
            "name": "ManufacturerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class InventoryReportLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    inventory_value_amount: Optional[InventoryValueAmount] = field(
        default=None,
        metadata={
            "name": "InventoryValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    availability_date: Optional[AvailabilityDate] = field(
        default=None,
        metadata={
            "name": "AvailabilityDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    availability_status_code: Optional[AvailabilityStatusCode] = field(
        default=None,
        metadata={
            "name": "AvailabilityStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    inventory_location: Optional[InventoryLocation] = field(
        default=None,
        metadata={
            "name": "InventoryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PerformanceDataLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    performance_value_quantity: Optional[PerformanceValueQuantity] = field(
        default=None,
        metadata={
            "name": "PerformanceValueQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    performance_metric_type_code: Optional[PerformanceMetricTypeCode] = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PriceType:
    price_amount: Optional[PriceAmount] = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    base_quantity: Optional[BaseQuantity] = field(
        default=None,
        metadata={
            "name": "BaseQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    price_change_reason: tuple[PriceChangeReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PriceChangeReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    price_type_code: Optional[PriceTypeCode] = field(
        default=None,
        metadata={
            "name": "PriceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    price_type: Optional[UblCommonBasicComponents21PriceType] = field(
        default=None,
        metadata={
            "name": "PriceType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    orderable_unit_factor_rate: Optional[OrderableUnitFactorRate] = field(
        default=None,
        metadata={
            "name": "OrderableUnitFactorRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validity_period: tuple[ValidityPeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    price_list: Optional[PriceList] = field(
        default=None,
        metadata={
            "name": "PriceList",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pricing_exchange_rate: Optional[PricingExchangeRate] = field(
        default=None,
        metadata={
            "name": "PricingExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ReceiptLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_quantity: Optional[ReceivedQuantity] = field(
        default=None,
        metadata={
            "name": "ReceivedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    short_quantity: Optional[ShortQuantity] = field(
        default=None,
        metadata={
            "name": "ShortQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    shortage_action_code: Optional[ShortageActionCode] = field(
        default=None,
        metadata={
            "name": "ShortageActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    rejected_quantity: Optional[RejectedQuantity] = field(
        default=None,
        metadata={
            "name": "RejectedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reject_reason_code: Optional[RejectReasonCode] = field(
        default=None,
        metadata={
            "name": "RejectReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reject_reason: tuple[RejectReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RejectReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reject_action_code: Optional[RejectActionCode] = field(
        default=None,
        metadata={
            "name": "RejectActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity_discrepancy_code: Optional[QuantityDiscrepancyCode] = field(
        default=None,
        metadata={
            "name": "QuantityDiscrepancyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    oversupply_quantity: Optional[OversupplyQuantity] = field(
        default=None,
        metadata={
            "name": "OversupplyQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_date: Optional[ReceivedDate] = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    timing_complaint_code: Optional[TimingComplaintCode] = field(
        default=None,
        metadata={
            "name": "TimingComplaintCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    timing_complaint: Optional[TimingComplaint] = field(
        default=None,
        metadata={
            "name": "TimingComplaint",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_line_reference: Optional[OrderLineReference] = field(
        default=None,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_line_reference: tuple[DespatchLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DespatchLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: tuple[Item, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment: tuple["Shipment", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class StockAvailabilityReportLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    value_amount: Optional[ValueAmount] = field(
        default=None,
        metadata={
            "name": "ValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    availability_date: Optional[AvailabilityDate] = field(
        default=None,
        metadata={
            "name": "AvailabilityDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    availability_status_code: Optional[AvailabilityStatusCode] = field(
        default=None,
        metadata={
            "name": "AvailabilityStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class AlternativeConditionPrice(PriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BillingReferenceLine(BillingReferenceLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CatalogueItemSpecificationUpdateLine(
    CatalogueItemSpecificationUpdateLineType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeliveryTerms(DeliveryTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DespatchLine(DespatchLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EventLineItem(EventLineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExceptionCriteriaLine(ExceptionCriteriaLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExceptionNotificationLine(ExceptionNotificationLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class HandlingUnitDespatchLine(DespatchLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InstructionForReturnsLine(InstructionForReturnsLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InventoryReportLine(InventoryReportLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PerformanceDataLine(PerformanceDataLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Price(PriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReceiptLine(ReceiptLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReceivedHandlingUnitReceiptLine(ReceiptLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class StockAvailabilityReportLine(StockAvailabilityReportLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TaxExclusivePrice(PriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TaxInclusivePrice(PriceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BillingReferenceType:
    invoice_document_reference: Optional[InvoiceDocumentReference] = field(
        default=None,
        metadata={
            "name": "InvoiceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    self_billed_invoice_document_reference: Optional[
        SelfBilledInvoiceDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "SelfBilledInvoiceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    credit_note_document_reference: Optional[CreditNoteDocumentReference] = (
        field(
            default=None,
            metadata={
                "name": "CreditNoteDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    self_billed_credit_note_document_reference: Optional[
        SelfBilledCreditNoteDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "SelfBilledCreditNoteDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    debit_note_document_reference: Optional[DebitNoteDocumentReference] = (
        field(
            default=None,
            metadata={
                "name": "DebitNoteDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    reminder_document_reference: Optional[ReminderDocumentReference] = field(
        default=None,
        metadata={
            "name": "ReminderDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    additional_document_reference: Optional[AdditionalDocumentReference] = (
        field(
            default=None,
            metadata={
                "name": "AdditionalDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    billing_reference_line: tuple[BillingReferenceLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BillingReferenceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ConsignmentType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    carrier_assigned_id: Optional[CarrierAssignedId] = field(
        default=None,
        metadata={
            "name": "CarrierAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consignee_assigned_id: Optional[ConsigneeAssignedId] = field(
        default=None,
        metadata={
            "name": "ConsigneeAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consignor_assigned_id: Optional[ConsignorAssignedId] = field(
        default=None,
        metadata={
            "name": "ConsignorAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    freight_forwarder_assigned_id: Optional[FreightForwarderAssignedId] = (
        field(
            default=None,
            metadata={
                "name": "FreightForwarderAssignedID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    broker_assigned_id: Optional[BrokerAssignedId] = field(
        default=None,
        metadata={
            "name": "BrokerAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contracted_carrier_assigned_id: Optional[ContractedCarrierAssignedId] = (
        field(
            default=None,
            metadata={
                "name": "ContractedCarrierAssignedID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    performing_carrier_assigned_id: Optional[PerformingCarrierAssignedId] = (
        field(
            default=None,
            metadata={
                "name": "PerformingCarrierAssignedID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    summary_description: tuple[SummaryDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SummaryDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_invoice_amount: Optional[TotalInvoiceAmount] = field(
        default=None,
        metadata={
            "name": "TotalInvoiceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_customs_value_amount: Optional[DeclaredCustomsValueAmount] = (
        field(
            default=None,
            metadata={
                "name": "DeclaredCustomsValueAmount",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    tariff_description: tuple[TariffDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TariffDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tariff_code: Optional[TariffCode] = field(
        default=None,
        metadata={
            "name": "TariffCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    insurance_premium_amount: Optional[InsurancePremiumAmount] = field(
        default=None,
        metadata={
            "name": "InsurancePremiumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_weight_measure: Optional[GrossWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_weight_measure: Optional[NetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_net_weight_measure: Optional[NetNetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    chargeable_weight_measure: Optional[ChargeableWeightMeasure] = field(
        default=None,
        metadata={
            "name": "ChargeableWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_volume_measure: Optional[GrossVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_volume_measure: Optional[NetVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    loading_length_measure: Optional[LoadingLengthMeasure] = field(
        default=None,
        metadata={
            "name": "LoadingLengthMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    remarks: tuple[Remarks, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_risk_indicator: Optional[HazardousRiskIndicator] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    animal_food_indicator: Optional[AnimalFoodIndicator] = field(
        default=None,
        metadata={
            "name": "AnimalFoodIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    human_food_indicator: Optional[HumanFoodIndicator] = field(
        default=None,
        metadata={
            "name": "HumanFoodIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    livestock_indicator: Optional[LivestockIndicator] = field(
        default=None,
        metadata={
            "name": "LivestockIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    bulk_cargo_indicator: Optional[BulkCargoIndicator] = field(
        default=None,
        metadata={
            "name": "BulkCargoIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    containerized_indicator: Optional[ContainerizedIndicator] = field(
        default=None,
        metadata={
            "name": "ContainerizedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    general_cargo_indicator: Optional[GeneralCargoIndicator] = field(
        default=None,
        metadata={
            "name": "GeneralCargoIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    special_security_indicator: Optional[SpecialSecurityIndicator] = field(
        default=None,
        metadata={
            "name": "SpecialSecurityIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    third_party_payer_indicator: Optional[ThirdPartyPayerIndicator] = field(
        default=None,
        metadata={
            "name": "ThirdPartyPayerIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    carrier_service_instructions: tuple[CarrierServiceInstructions, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "CarrierServiceInstructions",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    customs_clearance_service_instructions: tuple[
        CustomsClearanceServiceInstructions, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "CustomsClearanceServiceInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    forwarder_service_instructions: tuple[
        ForwarderServiceInstructions, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "ForwarderServiceInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    special_service_instructions: tuple[SpecialServiceInstructions, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "SpecialServiceInstructions",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    sequence_id: Optional[SequenceId] = field(
        default=None,
        metadata={
            "name": "SequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    shipping_priority_level_code: Optional[ShippingPriorityLevelCode] = field(
        default=None,
        metadata={
            "name": "ShippingPriorityLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_code: Optional[HandlingCode] = field(
        default=None,
        metadata={
            "name": "HandlingCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_instructions: tuple[HandlingInstructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HandlingInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    information: tuple[Information, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_goods_item_quantity: Optional[TotalGoodsItemQuantity] = field(
        default=None,
        metadata={
            "name": "TotalGoodsItemQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_transport_handling_unit_quantity: Optional[
        TotalTransportHandlingUnitQuantity
    ] = field(
        default=None,
        metadata={
            "name": "TotalTransportHandlingUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    insurance_value_amount: Optional[InsuranceValueAmount] = field(
        default=None,
        metadata={
            "name": "InsuranceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_for_carriage_value_amount: Optional[
        DeclaredForCarriageValueAmount
    ] = field(
        default=None,
        metadata={
            "name": "DeclaredForCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_statistics_value_amount: Optional[
        DeclaredStatisticsValueAmount
    ] = field(
        default=None,
        metadata={
            "name": "DeclaredStatisticsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_on_board_value_amount: Optional[FreeOnBoardValueAmount] = field(
        default=None,
        metadata={
            "name": "FreeOnBoardValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    special_instructions: tuple[SpecialInstructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SpecialInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    split_consignment_indicator: Optional[SplitConsignmentIndicator] = field(
        default=None,
        metadata={
            "name": "SplitConsignmentIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivery_instructions: tuple[DeliveryInstructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consignment_quantity: Optional[ConsignmentQuantity] = field(
        default=None,
        metadata={
            "name": "ConsignmentQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consolidatable_indicator: Optional[ConsolidatableIndicator] = field(
        default=None,
        metadata={
            "name": "ConsolidatableIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    haulage_instructions: tuple[HaulageInstructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HaulageInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    loading_sequence_id: Optional[LoadingSequenceId] = field(
        default=None,
        metadata={
            "name": "LoadingSequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    child_consignment_quantity: Optional[ChildConsignmentQuantity] = field(
        default=None,
        metadata={
            "name": "ChildConsignmentQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_packages_quantity: Optional[TotalPackagesQuantity] = field(
        default=None,
        metadata={
            "name": "TotalPackagesQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consolidated_shipment: tuple["ConsolidatedShipment", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConsolidatedShipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    customs_declaration: tuple[CustomsDeclaration, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CustomsDeclaration",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_pickup_transport_event: Optional[
        "RequestedPickupTransportEvent"
    ] = field(
        default=None,
        metadata={
            "name": "RequestedPickupTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_delivery_transport_event: Optional[
        "RequestedDeliveryTransportEvent"
    ] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_pickup_transport_event: Optional["PlannedPickupTransportEvent"] = (
        field(
            default=None,
            metadata={
                "name": "PlannedPickupTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    planned_delivery_transport_event: Optional[
        "PlannedDeliveryTransportEvent"
    ] = field(
        default=None,
        metadata={
            "name": "PlannedDeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    status: tuple[Status, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    child_consignment: tuple["ChildConsignment", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ChildConsignment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consignee_party: Optional[ConsigneeParty] = field(
        default=None,
        metadata={
            "name": "ConsigneeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exporter_party: Optional[ExporterParty] = field(
        default=None,
        metadata={
            "name": "ExporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consignor_party: Optional[ConsignorParty] = field(
        default=None,
        metadata={
            "name": "ConsignorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    importer_party: Optional[ImporterParty] = field(
        default=None,
        metadata={
            "name": "ImporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    carrier_party: Optional[CarrierParty] = field(
        default=None,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    freight_forwarder_party: Optional[FreightForwarderParty] = field(
        default=None,
        metadata={
            "name": "FreightForwarderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    notify_party: Optional[NotifyParty] = field(
        default=None,
        metadata={
            "name": "NotifyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    original_despatch_party: Optional[OriginalDespatchParty] = field(
        default=None,
        metadata={
            "name": "OriginalDespatchParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    final_delivery_party: Optional[FinalDeliveryParty] = field(
        default=None,
        metadata={
            "name": "FinalDeliveryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    performing_carrier_party: Optional[PerformingCarrierParty] = field(
        default=None,
        metadata={
            "name": "PerformingCarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    substitute_carrier_party: Optional[SubstituteCarrierParty] = field(
        default=None,
        metadata={
            "name": "SubstituteCarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    logistics_operator_party: Optional[LogisticsOperatorParty] = field(
        default=None,
        metadata={
            "name": "LogisticsOperatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_advisor_party: Optional[TransportAdvisorParty] = field(
        default=None,
        metadata={
            "name": "TransportAdvisorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    hazardous_item_notification_party: Optional[
        HazardousItemNotificationParty
    ] = field(
        default=None,
        metadata={
            "name": "HazardousItemNotificationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    insurance_party: Optional[InsuranceParty] = field(
        default=None,
        metadata={
            "name": "InsuranceParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    mortgage_holder_party: Optional[MortgageHolderParty] = field(
        default=None,
        metadata={
            "name": "MortgageHolderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    bill_of_lading_holder_party: Optional[BillOfLadingHolderParty] = field(
        default=None,
        metadata={
            "name": "BillOfLadingHolderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    original_departure_country: Optional[OriginalDepartureCountry] = field(
        default=None,
        metadata={
            "name": "OriginalDepartureCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    final_destination_country: Optional[FinalDestinationCountry] = field(
        default=None,
        metadata={
            "name": "FinalDestinationCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transit_country: tuple[TransitCountry, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransitCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_contract: Optional["TransportContract"] = field(
        default=None,
        metadata={
            "name": "TransportContract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_event: tuple["TransportEvent", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    original_despatch_transportation_service: Optional[
        "OriginalDespatchTransportationService"
    ] = field(
        default=None,
        metadata={
            "name": "OriginalDespatchTransportationService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    final_delivery_transportation_service: Optional[
        "FinalDeliveryTransportationService"
    ] = field(
        default=None,
        metadata={
            "name": "FinalDeliveryTransportationService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: Optional[DeliveryTerms] = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_terms: Optional["PaymentTerms"] = field(
        default=None,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    collect_payment_terms: Optional["CollectPaymentTerms"] = field(
        default=None,
        metadata={
            "name": "CollectPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    disbursement_payment_terms: Optional["DisbursementPaymentTerms"] = field(
        default=None,
        metadata={
            "name": "DisbursementPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    prepaid_payment_terms: Optional["PrepaidPaymentTerms"] = field(
        default=None,
        metadata={
            "name": "PrepaidPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    freight_allowance_charge: tuple[FreightAllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    extra_allowance_charge: tuple[ExtraAllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ExtraAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    main_carriage_shipment_stage: tuple["MainCarriageShipmentStage", ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "MainCarriageShipmentStage",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    pre_carriage_shipment_stage: tuple["PreCarriageShipmentStage", ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "PreCarriageShipmentStage",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    on_carriage_shipment_stage: tuple["OnCarriageShipmentStage", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OnCarriageShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_handling_unit: tuple["TransportHandlingUnit", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportHandlingUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    first_arrival_port_location: Optional[FirstArrivalPortLocation] = field(
        default=None,
        metadata={
            "name": "FirstArrivalPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    last_exit_port_location: Optional[LastExitPortLocation] = field(
        default=None,
        metadata={
            "name": "LastExitPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DeliveryType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_delivery_date: Optional[ActualDeliveryDate] = field(
        default=None,
        metadata={
            "name": "ActualDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_delivery_time: Optional[ActualDeliveryTime] = field(
        default=None,
        metadata={
            "name": "ActualDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_delivery_date: Optional[LatestDeliveryDate] = field(
        default=None,
        metadata={
            "name": "LatestDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_delivery_time: Optional[LatestDeliveryTime] = field(
        default=None,
        metadata={
            "name": "LatestDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    release_id: Optional[ReleaseId] = field(
        default=None,
        metadata={
            "name": "ReleaseID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tracking_id: Optional[TrackingId] = field(
        default=None,
        metadata={
            "name": "TrackingID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivery_address: Optional[DeliveryAddress] = field(
        default=None,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_location: Optional[DeliveryLocation] = field(
        default=None,
        metadata={
            "name": "DeliveryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    alternative_delivery_location: Optional[AlternativeDeliveryLocation] = (
        field(
            default=None,
            metadata={
                "name": "AlternativeDeliveryLocation",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    requested_delivery_period: Optional[RequestedDeliveryPeriod] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    promised_delivery_period: Optional[PromisedDeliveryPeriod] = field(
        default=None,
        metadata={
            "name": "PromisedDeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_delivery_period: Optional[EstimatedDeliveryPeriod] = field(
        default=None,
        metadata={
            "name": "EstimatedDeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    carrier_party: Optional[CarrierParty] = field(
        default=None,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_party: Optional[DeliveryParty] = field(
        default=None,
        metadata={
            "name": "DeliveryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    notify_party: tuple[NotifyParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NotifyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch: Optional[Despatch] = field(
        default=None,
        metadata={
            "name": "Despatch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: tuple[DeliveryTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    minimum_delivery_unit: Optional[MinimumDeliveryUnit] = field(
        default=None,
        metadata={
            "name": "MinimumDeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maximum_delivery_unit: Optional[MaximumDeliveryUnit] = field(
        default=None,
        metadata={
            "name": "MaximumDeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment: Optional["Shipment"] = field(
        default=None,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class MiscellaneousEventType:
    miscellaneous_event_type_code: Optional[MiscellaneousEventTypeCode] = (
        field(
            default=None,
            metadata={
                "name": "MiscellaneousEventTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
                "required": True,
            },
        )
    )
    event_line_item: tuple[EventLineItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EventLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class PromotionalEventLineItemType:
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    event_line_item: Optional[EventLineItem] = field(
        default=None,
        metadata={
            "name": "EventLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class SalesItemType:
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    activity_property: tuple[ActivityProperty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ActivityProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_exclusive_price: tuple[TaxExclusivePrice, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxExclusivePrice",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_inclusive_price: tuple[TaxInclusivePrice, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxInclusivePrice",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class TelecommunicationsServiceType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    call_date: Optional[CallDate] = field(
        default=None,
        metadata={
            "name": "CallDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    call_time: Optional[CallTime] = field(
        default=None,
        metadata={
            "name": "CallTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    service_number_called: Optional[ServiceNumberCalled] = field(
        default=None,
        metadata={
            "name": "ServiceNumberCalled",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    telecommunications_service_category: Optional[
        TelecommunicationsServiceCategory
    ] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telecommunications_service_category_code: Optional[
        TelecommunicationsServiceCategoryCode
    ] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCategoryCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    movie_title: Optional[MovieTitle] = field(
        default=None,
        metadata={
            "name": "MovieTitle",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    roaming_partner_name: Optional[RoamingPartnerName] = field(
        default=None,
        metadata={
            "name": "RoamingPartnerName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pay_per_view: Optional[PayPerView] = field(
        default=None,
        metadata={
            "name": "PayPerView",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telecommunications_service_call: Optional[
        TelecommunicationsServiceCall
    ] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCall",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telecommunications_service_call_code: Optional[
        TelecommunicationsServiceCallCode
    ] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCallCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    call_base_amount: Optional[CallBaseAmount] = field(
        default=None,
        metadata={
            "name": "CallBaseAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    call_extension_amount: Optional[CallExtensionAmount] = field(
        default=None,
        metadata={
            "name": "CallExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    country: Optional[Country] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exchange_rate: tuple[ExchangeRate, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    call_duty: tuple[CallDuty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CallDuty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    time_duty: tuple[TimeDuty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TimeDuty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransportExecutionTermsType:
    transport_user_special_terms: tuple[TransportUserSpecialTerms, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "TransportUserSpecialTerms",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    transport_service_provider_special_terms: tuple[
        TransportServiceProviderSpecialTerms, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportServiceProviderSpecialTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    change_conditions: tuple[ChangeConditions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ChangeConditions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_terms: tuple[PaymentTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: tuple[DeliveryTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    bonus_payment_terms: Optional[BonusPaymentTerms] = field(
        default=None,
        metadata={
            "name": "BonusPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    commission_payment_terms: Optional[CommissionPaymentTerms] = field(
        default=None,
        metadata={
            "name": "CommissionPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    penalty_payment_terms: Optional[PenaltyPaymentTerms] = field(
        default=None,
        metadata={
            "name": "PenaltyPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    environmental_emission: tuple[EnvironmentalEmission, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EnvironmentalEmission",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    notification_requirement: tuple[NotificationRequirement, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "NotificationRequirement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    service_charge_payment_terms: Optional[ServiceChargePaymentTerms] = field(
        default=None,
        metadata={
            "name": "ServiceChargePaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class BillingReference(BillingReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ChildConsignment(ConsignmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Consignment(ConsignmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContractualDelivery(DeliveryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Delivery(DeliveryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MiscellaneousEvent(MiscellaneousEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PromotionalEventLineItem(PromotionalEventLineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReferencedConsignment(ConsignmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SalesItem(SalesItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TelecommunicationsService(TelecommunicationsServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportExecutionTerms(TransportExecutionTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ActivityDataLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    supply_chain_activity_type_code: Optional[SupplyChainActivityTypeCode] = (
        field(
            default=None,
            metadata={
                "name": "SupplyChainActivityTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
                "required": True,
            },
        )
    )
    buyer_customer_party: Optional[BuyerCustomerParty] = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    activity_period: Optional[ActivityPeriod] = field(
        default=None,
        metadata={
            "name": "ActivityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    activity_origin_location: Optional[ActivityOriginLocation] = field(
        default=None,
        metadata={
            "name": "ActivityOriginLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    activity_final_location: Optional[ActivityFinalLocation] = field(
        default=None,
        metadata={
            "name": "ActivityFinalLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sales_item: tuple[SalesItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class ConsumptionLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    parent_document_line_reference_id: Optional[
        ParentDocumentLineReferenceId
    ] = field(
        default=None,
        metadata={
            "name": "ParentDocumentLineReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoiced_quantity: Optional[InvoicedQuantity] = field(
        default=None,
        metadata={
            "name": "InvoicedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: tuple[Delivery, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    utility_item: Optional[UtilityItem] = field(
        default=None,
        metadata={
            "name": "UtilityItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    unstructured_price: Optional[UnstructuredPrice] = field(
        default=None,
        metadata={
            "name": "UnstructuredPrice",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ForecastLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    frozen_document_indicator: Optional[FrozenDocumentIndicator] = field(
        default=None,
        metadata={
            "name": "FrozenDocumentIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_period: Optional[ForecastPeriod] = field(
        default=None,
        metadata={
            "name": "ForecastPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sales_item: Optional[SalesItem] = field(
        default=None,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ForecastRevisionLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    revised_forecast_line_id: Optional[RevisedForecastLineId] = field(
        default=None,
        metadata={
            "name": "RevisedForecastLineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    source_forecast_issue_date: Optional[SourceForecastIssueDate] = field(
        default=None,
        metadata={
            "name": "SourceForecastIssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    source_forecast_issue_time: Optional[SourceForecastIssueTime] = field(
        default=None,
        metadata={
            "name": "SourceForecastIssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    adjustment_reason_code: Optional[AdjustmentReasonCode] = field(
        default=None,
        metadata={
            "name": "AdjustmentReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    forecast_period: Optional[ForecastPeriod] = field(
        default=None,
        metadata={
            "name": "ForecastPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sales_item: Optional[SalesItem] = field(
        default=None,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class GoodsItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sequence_number_id: Optional[SequenceNumberId] = field(
        default=None,
        metadata={
            "name": "SequenceNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_risk_indicator: Optional[HazardousRiskIndicator] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_customs_value_amount: Optional[DeclaredCustomsValueAmount] = (
        field(
            default=None,
            metadata={
                "name": "DeclaredCustomsValueAmount",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    declared_for_carriage_value_amount: Optional[
        DeclaredForCarriageValueAmount
    ] = field(
        default=None,
        metadata={
            "name": "DeclaredForCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_statistics_value_amount: Optional[
        DeclaredStatisticsValueAmount
    ] = field(
        default=None,
        metadata={
            "name": "DeclaredStatisticsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_on_board_value_amount: Optional[FreeOnBoardValueAmount] = field(
        default=None,
        metadata={
            "name": "FreeOnBoardValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    insurance_value_amount: Optional[InsuranceValueAmount] = field(
        default=None,
        metadata={
            "name": "InsuranceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_amount: Optional[ValueAmount] = field(
        default=None,
        metadata={
            "name": "ValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_weight_measure: Optional[GrossWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_weight_measure: Optional[NetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_net_weight_measure: Optional[NetNetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    chargeable_weight_measure: Optional[ChargeableWeightMeasure] = field(
        default=None,
        metadata={
            "name": "ChargeableWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_volume_measure: Optional[GrossVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_volume_measure: Optional[NetVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    preference_criterion_code: Optional[PreferenceCriterionCode] = field(
        default=None,
        metadata={
            "name": "PreferenceCriterionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_customs_id: Optional[RequiredCustomsId] = field(
        default=None,
        metadata={
            "name": "RequiredCustomsID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customs_status_code: Optional[CustomsStatusCode] = field(
        default=None,
        metadata={
            "name": "CustomsStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customs_tariff_quantity: Optional[CustomsTariffQuantity] = field(
        default=None,
        metadata={
            "name": "CustomsTariffQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customs_import_classified_indicator: Optional[
        CustomsImportClassifiedIndicator
    ] = field(
        default=None,
        metadata={
            "name": "CustomsImportClassifiedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    chargeable_quantity: Optional[ChargeableQuantity] = field(
        default=None,
        metadata={
            "name": "ChargeableQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    returnable_quantity: Optional[ReturnableQuantity] = field(
        default=None,
        metadata={
            "name": "ReturnableQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trace_id: Optional[TraceId] = field(
        default=None,
        metadata={
            "name": "TraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    item: tuple[Item, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    goods_item_container: tuple["GoodsItemContainer", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "GoodsItemContainer",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    freight_allowance_charge: tuple[FreightAllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    invoice_line: tuple["InvoiceLine", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "InvoiceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    temperature: tuple[Temperature, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Temperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contained_goods_item: tuple["ContainedGoodsItem", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContainedGoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    origin_address: Optional[OriginAddress] = field(
        default=None,
        metadata={
            "name": "OriginAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: Optional[Delivery] = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pickup: Optional[Pickup] = field(
        default=None,
        metadata={
            "name": "Pickup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch: Optional[Despatch] = field(
        default=None,
        metadata={
            "name": "Despatch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    measurement_dimension: tuple[MeasurementDimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    containing_package: tuple["ContainingPackage", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContainingPackage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment_document_reference: Optional[ShipmentDocumentReference] = field(
        default=None,
        metadata={
            "name": "ShipmentDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    minimum_temperature: Optional[MinimumTemperature] = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maximum_temperature: Optional[MaximumTemperature] = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemInformationRequestLineType:
    time_frequency_code: Optional[TimeFrequencyCode] = field(
        default=None,
        metadata={
            "name": "TimeFrequencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    supply_chain_activity_type_code: Optional[SupplyChainActivityTypeCode] = (
        field(
            default=None,
            metadata={
                "name": "SupplyChainActivityTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    forecast_type_code: Optional[ForecastTypeCode] = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    performance_metric_type_code: Optional[PerformanceMetricTypeCode] = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    period: tuple[Period, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )
    sales_item: tuple[SalesItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class PromotionalSpecificationType:
    specification_id: Optional[SpecificationId] = field(
        default=None,
        metadata={
            "name": "SpecificationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    promotional_event_line_item: tuple[PromotionalEventLineItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PromotionalEventLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )
    event_tactic: tuple[EventTactic, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EventTactic",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ReminderLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    balance_brought_forward_indicator: Optional[
        BalanceBroughtForwardIndicator
    ] = field(
        default=None,
        metadata={
            "name": "BalanceBroughtForwardIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    debit_line_amount: Optional[DebitLineAmount] = field(
        default=None,
        metadata={
            "name": "DebitLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    credit_line_amount: Optional[CreditLineAmount] = field(
        default=None,
        metadata={
            "name": "CreditLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    penalty_surcharge_percent: Optional[PenaltySurchargePercent] = field(
        default=None,
        metadata={
            "name": "PenaltySurchargePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Optional[Amount] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reminder_period: tuple[ReminderPeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReminderPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    billing_reference: tuple[BillingReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exchange_rate: Optional[ExchangeRate] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RemittanceAdviceLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    debit_line_amount: Optional[DebitLineAmount] = field(
        default=None,
        metadata={
            "name": "DebitLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    credit_line_amount: Optional[CreditLineAmount] = field(
        default=None,
        metadata={
            "name": "CreditLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    balance_amount: Optional[BalanceAmount] = field(
        default=None,
        metadata={
            "name": "BalanceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoicing_party_reference: Optional[InvoicingPartyReference] = field(
        default=None,
        metadata={
            "name": "InvoicingPartyReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_supplier_party: Optional[AccountingSupplierParty] = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_customer_party: Optional[AccountingCustomerParty] = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    buyer_customer_party: Optional[BuyerCustomerParty] = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_customer_party: Optional[OriginatorCustomerParty] = field(
        default=None,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payee_party: Optional[PayeeParty] = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    invoice_period: tuple[InvoicePeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    billing_reference: tuple[BillingReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exchange_rate: Optional[ExchangeRate] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class StatementLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    balance_brought_forward_indicator: Optional[
        BalanceBroughtForwardIndicator
    ] = field(
        default=None,
        metadata={
            "name": "BalanceBroughtForwardIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    debit_line_amount: Optional[DebitLineAmount] = field(
        default=None,
        metadata={
            "name": "DebitLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    credit_line_amount: Optional[CreditLineAmount] = field(
        default=None,
        metadata={
            "name": "CreditLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    balance_amount: Optional[BalanceAmount] = field(
        default=None,
        metadata={
            "name": "BalanceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_means: Optional[PaymentMeans] = field(
        default=None,
        metadata={
            "name": "PaymentMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_terms: tuple[PaymentTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    buyer_customer_party: Optional[BuyerCustomerParty] = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_customer_party: Optional[OriginatorCustomerParty] = field(
        default=None,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_customer_party: Optional[AccountingCustomerParty] = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_supplier_party: Optional[AccountingSupplierParty] = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payee_party: Optional[PayeeParty] = field(
        default=None,
        metadata={
            "name": "PayeeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    invoice_period: tuple[InvoicePeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    billing_reference: tuple[BillingReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exchange_rate: Optional[ExchangeRate] = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    collected_payment: tuple[CollectedPayment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CollectedPayment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TelecommunicationsSupplyLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    phone_number: Optional[PhoneNumber] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exchange_rate: tuple[ExchangeRate, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    telecommunications_service: tuple[TelecommunicationsService, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TelecommunicationsService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class ActivityDataLine(ActivityDataLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsumptionLine(ConsumptionLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContainedGoodsItem(GoodsItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ForecastLine(ForecastLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ForecastRevisionLine(ForecastRevisionLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class GoodsItem(GoodsItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemInformationRequestLine(ItemInformationRequestLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PromotionalSpecification(PromotionalSpecificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReferencedGoodsItem(GoodsItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReminderLine(ReminderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RemittanceAdviceLine(RemittanceAdviceLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class StatementLine(StatementLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SupplyChainActivityDataLine(ActivityDataLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TelecommunicationsSupplyLine(TelecommunicationsSupplyLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PackageType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    returnable_material_indicator: Optional[ReturnableMaterialIndicator] = (
        field(
            default=None,
            metadata={
                "name": "ReturnableMaterialIndicator",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    package_level_code: Optional[PackageLevelCode] = field(
        default=None,
        metadata={
            "name": "PackageLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    packaging_type_code: Optional[PackagingTypeCode] = field(
        default=None,
        metadata={
            "name": "PackagingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    packing_material: tuple[PackingMaterial, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PackingMaterial",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trace_id: Optional[TraceId] = field(
        default=None,
        metadata={
            "name": "TraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contained_package: tuple["ContainedPackage", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContainedPackage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    containing_transport_equipment: Optional[
        "ContainingTransportEquipment"
    ] = field(
        default=None,
        metadata={
            "name": "ContainingTransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    goods_item: tuple[GoodsItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "GoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    measurement_dimension: tuple[MeasurementDimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_unit: tuple[DeliveryUnit, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: Optional[Delivery] = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pickup: Optional[Pickup] = field(
        default=None,
        metadata={
            "name": "Pickup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch: Optional[Despatch] = field(
        default=None,
        metadata={
            "name": "Despatch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PromotionalEventType:
    promotional_event_type_code: Optional[PromotionalEventTypeCode] = field(
        default=None,
        metadata={
            "name": "PromotionalEventTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    submission_date: Optional[SubmissionDate] = field(
        default=None,
        metadata={
            "name": "SubmissionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    first_shipment_availibility_date: Optional[
        FirstShipmentAvailibilityDate
    ] = field(
        default=None,
        metadata={
            "name": "FirstShipmentAvailibilityDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_proposal_acceptance_date: Optional[LatestProposalAcceptanceDate] = (
        field(
            default=None,
            metadata={
                "name": "LatestProposalAcceptanceDate",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    promotional_specification: tuple[PromotionalSpecification, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PromotionalSpecification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class ShipmentType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    shipping_priority_level_code: Optional[ShippingPriorityLevelCode] = field(
        default=None,
        metadata={
            "name": "ShippingPriorityLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_code: Optional[HandlingCode] = field(
        default=None,
        metadata={
            "name": "HandlingCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_instructions: tuple[HandlingInstructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HandlingInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    information: tuple[Information, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_weight_measure: Optional[GrossWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_weight_measure: Optional[NetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_net_weight_measure: Optional[NetNetWeightMeasure] = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_volume_measure: Optional[GrossVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_volume_measure: Optional[NetVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_goods_item_quantity: Optional[TotalGoodsItemQuantity] = field(
        default=None,
        metadata={
            "name": "TotalGoodsItemQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_transport_handling_unit_quantity: Optional[
        TotalTransportHandlingUnitQuantity
    ] = field(
        default=None,
        metadata={
            "name": "TotalTransportHandlingUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    insurance_value_amount: Optional[InsuranceValueAmount] = field(
        default=None,
        metadata={
            "name": "InsuranceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_customs_value_amount: Optional[DeclaredCustomsValueAmount] = (
        field(
            default=None,
            metadata={
                "name": "DeclaredCustomsValueAmount",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    declared_for_carriage_value_amount: Optional[
        DeclaredForCarriageValueAmount
    ] = field(
        default=None,
        metadata={
            "name": "DeclaredForCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_statistics_value_amount: Optional[
        DeclaredStatisticsValueAmount
    ] = field(
        default=None,
        metadata={
            "name": "DeclaredStatisticsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_on_board_value_amount: Optional[FreeOnBoardValueAmount] = field(
        default=None,
        metadata={
            "name": "FreeOnBoardValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    special_instructions: tuple[SpecialInstructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SpecialInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivery_instructions: tuple[DeliveryInstructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    split_consignment_indicator: Optional[SplitConsignmentIndicator] = field(
        default=None,
        metadata={
            "name": "SplitConsignmentIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consignment_quantity: Optional[ConsignmentQuantity] = field(
        default=None,
        metadata={
            "name": "ConsignmentQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consignment: tuple[Consignment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Consignment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    goods_item: tuple[GoodsItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "GoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment_stage: tuple["ShipmentStage", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: Optional[Delivery] = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_handling_unit: tuple["TransportHandlingUnit", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportHandlingUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    return_address: Optional[ReturnAddress] = field(
        default=None,
        metadata={
            "name": "ReturnAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    origin_address: Optional[OriginAddress] = field(
        default=None,
        metadata={
            "name": "OriginAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    first_arrival_port_location: Optional[FirstArrivalPortLocation] = field(
        default=None,
        metadata={
            "name": "FirstArrivalPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    last_exit_port_location: Optional[LastExitPortLocation] = field(
        default=None,
        metadata={
            "name": "LastExitPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    export_country: Optional[ExportCountry] = field(
        default=None,
        metadata={
            "name": "ExportCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    freight_allowance_charge: tuple[FreightAllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TelecommunicationsSupplyType:
    telecommunications_supply_type: Optional[
        UblCommonBasicComponents21TelecommunicationsSupplyType
    ] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsSupplyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telecommunications_supply_type_code: Optional[
        TelecommunicationsSupplyTypeCode
    ] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsSupplyTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    privacy_code: Optional[PrivacyCode] = field(
        default=None,
        metadata={
            "name": "PrivacyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_amount: Optional[TotalAmount] = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telecommunications_supply_line: tuple[
        TelecommunicationsSupplyLine, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "TelecommunicationsSupplyLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class ActualPackage(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ConsolidatedShipment(ShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContainedPackage(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContainingPackage(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Package(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PromotionalEvent(PromotionalEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReferencedPackage(PackageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReferencedShipment(ShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReportedShipment(ShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Shipment(ShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TelecommunicationsSupply(TelecommunicationsSupplyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CertificateOfOriginApplicationType:
    reference_id: Optional[ReferenceId] = field(
        default=None,
        metadata={
            "name": "ReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    certificate_type: Optional[UblCommonBasicComponents21CertificateType] = (
        field(
            default=None,
            metadata={
                "name": "CertificateType",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
                "required": True,
            },
        )
    )
    application_status_code: Optional[ApplicationStatusCode] = field(
        default=None,
        metadata={
            "name": "ApplicationStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    original_job_id: Optional[OriginalJobId] = field(
        default=None,
        metadata={
            "name": "OriginalJobID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    previous_job_id: Optional[PreviousJobId] = field(
        default=None,
        metadata={
            "name": "PreviousJobID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    remarks: tuple[Remarks, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    shipment: Optional[Shipment] = field(
        default=None,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    endorser_party: tuple[EndorserParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EndorserParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )
    preparation_party: Optional[PreparationParty] = field(
        default=None,
        metadata={
            "name": "PreparationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    issuer_party: Optional[IssuerParty] = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    exporter_party: Optional[ExporterParty] = field(
        default=None,
        metadata={
            "name": "ExporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    importer_party: Optional[ImporterParty] = field(
        default=None,
        metadata={
            "name": "ImporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    issuing_country: Optional[IssuingCountry] = field(
        default=None,
        metadata={
            "name": "IssuingCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    document_distribution: tuple[DocumentDistribution, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentDistribution",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supporting_document_reference: tuple[SupportingDocumentReference, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "SupportingDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    signature: tuple[Signature, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ConsumptionType:
    utility_statement_type_code: Optional[UtilityStatementTypeCode] = field(
        default=None,
        metadata={
            "name": "UtilityStatementTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    main_period: Optional[MainPeriod] = field(
        default=None,
        metadata={
            "name": "MainPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    energy_water_supply: Optional[EnergyWaterSupply] = field(
        default=None,
        metadata={
            "name": "EnergyWaterSupply",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    telecommunications_supply: Optional[TelecommunicationsSupply] = field(
        default=None,
        metadata={
            "name": "TelecommunicationsSupply",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    legal_monetary_total: Optional[LegalMonetaryTotal] = field(
        default=None,
        metadata={
            "name": "LegalMonetaryTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class ItemLocationQuantityType:
    lead_time_measure: Optional[LeadTimeMeasure] = field(
        default=None,
        metadata={
            "name": "LeadTimeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_risk_indicator: Optional[HazardousRiskIndicator] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trading_restrictions: tuple[TradingRestrictions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TradingRestrictions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    applicable_territory_address: tuple[ApplicableTerritoryAddress, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "ApplicableTerritoryAddress",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_unit: tuple[DeliveryUnit, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    applicable_tax_category: tuple[ApplicableTaxCategory, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ApplicableTaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    package: Optional[Package] = field(
        default=None,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    dependent_price_reference: Optional[DependentPriceReference] = field(
        default=None,
        metadata={
            "name": "DependentPriceReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class OrderedShipmentType:
    shipment: Optional[Shipment] = field(
        default=None,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    package: tuple[Package, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransportEventType:
    identification_id: Optional[IdentificationId] = field(
        default=None,
        metadata={
            "name": "IdentificationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    occurrence_date: Optional[OccurrenceDate] = field(
        default=None,
        metadata={
            "name": "OccurrenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    occurrence_time: Optional[OccurrenceTime] = field(
        default=None,
        metadata={
            "name": "OccurrenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_event_type_code: Optional[TransportEventTypeCode] = field(
        default=None,
        metadata={
            "name": "TransportEventTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    completion_indicator: Optional[CompletionIndicator] = field(
        default=None,
        metadata={
            "name": "CompletionIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reported_shipment: Optional[ReportedShipment] = field(
        default=None,
        metadata={
            "name": "ReportedShipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    current_status: tuple[CurrentStatus, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CurrentStatus",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contact: tuple[Contact, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    period: tuple[Period, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class AcceptanceTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ActualArrivalTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ActualDepartureTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ActualPickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ActualWaypointTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AvailabilityTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CertificateOfOriginApplication(CertificateOfOriginApplicationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class Consumption(ConsumptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DeliveryTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DetentionTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DischargeTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DropoffTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EstimatedArrivalTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class EstimatedDepartureTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExaminationTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ExportationTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class HandlingTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemLocationQuantity(ItemLocationQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LoadingTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OfferedItemLocationQuantity(ItemLocationQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OptionalTakeoverTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OrderedShipment(OrderedShipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginalItemLocationQuantity(ItemLocationQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PlannedArrivalTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PlannedDeliveryTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PlannedDepartureTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PlannedPickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PlannedWaypointTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PositioningTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class QuarantineTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReceiptTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedArrivalTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedDeliveryTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedDepartureTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedPickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestedWaypointTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequiredItemLocationQuantity(ItemLocationQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class StorageTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TakeoverTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UpdatedDeliveryTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UpdatedPickupTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class WarehousingTransportEvent(TransportEventType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CatalogueLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    action_code: Optional[ActionCode] = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    life_cycle_status_code: Optional[LifeCycleStatusCode] = field(
        default=None,
        metadata={
            "name": "LifeCycleStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract_subdivision: Optional[ContractSubdivision] = field(
        default=None,
        metadata={
            "name": "ContractSubdivision",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    orderable_indicator: Optional[OrderableIndicator] = field(
        default=None,
        metadata={
            "name": "OrderableIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    orderable_unit: Optional[OrderableUnit] = field(
        default=None,
        metadata={
            "name": "OrderableUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    content_unit_quantity: Optional[ContentUnitQuantity] = field(
        default=None,
        metadata={
            "name": "ContentUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_quantity_increment_numeric: Optional[
        OrderQuantityIncrementNumeric
    ] = field(
        default=None,
        metadata={
            "name": "OrderQuantityIncrementNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_order_quantity: Optional[MinimumOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_order_quantity: Optional[MaximumOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    warranty_information: tuple[WarrantyInformation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "WarrantyInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pack_level_code: Optional[PackLevelCode] = field(
        default=None,
        metadata={
            "name": "PackLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contractor_customer_party: Optional[ContractorCustomerParty] = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_party: Optional[WarrantyParty] = field(
        default=None,
        metadata={
            "name": "WarrantyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    line_validity_period: Optional[LineValidityPeriod] = field(
        default=None,
        metadata={
            "name": "LineValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_comparison: tuple[ItemComparison, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ItemComparison",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    component_related_item: tuple[ComponentRelatedItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ComponentRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accessory_related_item: tuple[AccessoryRelatedItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AccessoryRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    required_related_item: tuple[RequiredRelatedItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RequiredRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    replacement_related_item: tuple[ReplacementRelatedItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReplacementRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    complementary_related_item: tuple[ComplementaryRelatedItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ComplementaryRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    replaced_related_item: tuple[ReplacedRelatedItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReplacedRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    required_item_location_quantity: tuple[
        RequiredItemLocationQuantity, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "RequiredItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    keyword_item_property: tuple[KeywordItemProperty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "KeywordItemProperty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    call_for_tenders_line_reference: Optional[CallForTendersLineReference] = (
        field(
            default=None,
            metadata={
                "name": "CallForTendersLineReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    call_for_tenders_document_reference: Optional[
        CallForTendersDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "CallForTendersDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CataloguePricingUpdateLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    contractor_customer_party: Optional[ContractorCustomerParty] = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: Optional[SellerSupplierParty] = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    required_item_location_quantity: tuple[
        RequiredItemLocationQuantity, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "RequiredItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CatalogueRequestLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    contract_subdivision: Optional[ContractSubdivision] = field(
        default=None,
        metadata={
            "name": "ContractSubdivision",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_validity_period: Optional[LineValidityPeriod] = field(
        default=None,
        metadata={
            "name": "LineValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    required_item_location_quantity: tuple[
        RequiredItemLocationQuantity, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "RequiredItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class ItemManagementProfileType:
    frozen_period_days_numeric: Optional[FrozenPeriodDaysNumeric] = field(
        default=None,
        metadata={
            "name": "FrozenPeriodDaysNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_inventory_quantity: Optional[MinimumInventoryQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumInventoryQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    multiple_order_quantity: Optional[MultipleOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MultipleOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_interval_days_numeric: Optional[OrderIntervalDaysNumeric] = field(
        default=None,
        metadata={
            "name": "OrderIntervalDaysNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    replenishment_owner_description: tuple[
        ReplenishmentOwnerDescription, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "ReplenishmentOwnerDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    target_service_percent: Optional[TargetServicePercent] = field(
        default=None,
        metadata={
            "name": "TargetServicePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    target_inventory_quantity: Optional[TargetInventoryQuantity] = field(
        default=None,
        metadata={
            "name": "TargetInventoryQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    effective_period: Optional[EffectivePeriod] = field(
        default=None,
        metadata={
            "name": "EffectivePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    item_location_quantity: Optional[ItemLocationQuantity] = field(
        default=None,
        metadata={
            "name": "ItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PricingReferenceType:
    original_item_location_quantity: Optional[OriginalItemLocationQuantity] = (
        field(
            default=None,
            metadata={
                "name": "OriginalItemLocationQuantity",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    alternative_condition_price: tuple[AlternativeConditionPrice, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AlternativeConditionPrice",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RequestForTenderLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_included_indicator: Optional[TaxIncludedIndicator] = field(
        default=None,
        metadata={
            "name": "TaxIncludedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_amount: Optional[MinimumAmount] = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_amount: Optional[MaximumAmount] = field(
        default=None,
        metadata={
            "name": "MaximumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_amount: Optional[EstimatedAmount] = field(
        default=None,
        metadata={
            "name": "EstimatedAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_period: tuple[DeliveryPeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    required_item_location_quantity: tuple[
        RequiredItemLocationQuantity, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "RequiredItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    sub_request_for_tender_line: tuple["SubRequestForTenderLine", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubRequestForTenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ShipmentStageType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_mode_code: Optional[TransportModeCode] = field(
        default=None,
        metadata={
            "name": "TransportModeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_means_type_code: Optional[TransportMeansTypeCode] = field(
        default=None,
        metadata={
            "name": "TransportMeansTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transit_direction_code: Optional[TransitDirectionCode] = field(
        default=None,
        metadata={
            "name": "TransitDirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pre_carriage_indicator: Optional[PreCarriageIndicator] = field(
        default=None,
        metadata={
            "name": "PreCarriageIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    on_carriage_indicator: Optional[OnCarriageIndicator] = field(
        default=None,
        metadata={
            "name": "OnCarriageIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_delivery_date: Optional[EstimatedDeliveryDate] = field(
        default=None,
        metadata={
            "name": "EstimatedDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_delivery_time: Optional[EstimatedDeliveryTime] = field(
        default=None,
        metadata={
            "name": "EstimatedDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_delivery_date: Optional[RequiredDeliveryDate] = field(
        default=None,
        metadata={
            "name": "RequiredDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_delivery_time: Optional[RequiredDeliveryTime] = field(
        default=None,
        metadata={
            "name": "RequiredDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    loading_sequence_id: Optional[LoadingSequenceId] = field(
        default=None,
        metadata={
            "name": "LoadingSequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    successive_sequence_id: Optional[SuccessiveSequenceId] = field(
        default=None,
        metadata={
            "name": "SuccessiveSequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    instructions: tuple[Instructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Instructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    demurrage_instructions: tuple[DemurrageInstructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DemurrageInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    crew_quantity: Optional[CrewQuantity] = field(
        default=None,
        metadata={
            "name": "CrewQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    passenger_quantity: Optional[PassengerQuantity] = field(
        default=None,
        metadata={
            "name": "PassengerQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transit_period: Optional[TransitPeriod] = field(
        default=None,
        metadata={
            "name": "TransitPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    carrier_party: tuple[CarrierParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_means: Optional[TransportMeans] = field(
        default=None,
        metadata={
            "name": "TransportMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    loading_port_location: Optional[LoadingPortLocation] = field(
        default=None,
        metadata={
            "name": "LoadingPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    unloading_port_location: Optional[UnloadingPortLocation] = field(
        default=None,
        metadata={
            "name": "UnloadingPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transship_port_location: Optional[TransshipPortLocation] = field(
        default=None,
        metadata={
            "name": "TransshipPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    loading_transport_event: Optional[LoadingTransportEvent] = field(
        default=None,
        metadata={
            "name": "LoadingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    examination_transport_event: Optional[ExaminationTransportEvent] = field(
        default=None,
        metadata={
            "name": "ExaminationTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    availability_transport_event: Optional[AvailabilityTransportEvent] = field(
        default=None,
        metadata={
            "name": "AvailabilityTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exportation_transport_event: Optional[ExportationTransportEvent] = field(
        default=None,
        metadata={
            "name": "ExportationTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    discharge_transport_event: Optional[DischargeTransportEvent] = field(
        default=None,
        metadata={
            "name": "DischargeTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warehousing_transport_event: Optional[WarehousingTransportEvent] = field(
        default=None,
        metadata={
            "name": "WarehousingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    takeover_transport_event: Optional[TakeoverTransportEvent] = field(
        default=None,
        metadata={
            "name": "TakeoverTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    optional_takeover_transport_event: Optional[
        OptionalTakeoverTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "OptionalTakeoverTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    dropoff_transport_event: Optional[DropoffTransportEvent] = field(
        default=None,
        metadata={
            "name": "DropoffTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    actual_pickup_transport_event: Optional[ActualPickupTransportEvent] = (
        field(
            default=None,
            metadata={
                "name": "ActualPickupTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    delivery_transport_event: Optional[DeliveryTransportEvent] = field(
        default=None,
        metadata={
            "name": "DeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    receipt_transport_event: Optional[ReceiptTransportEvent] = field(
        default=None,
        metadata={
            "name": "ReceiptTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    storage_transport_event: Optional[StorageTransportEvent] = field(
        default=None,
        metadata={
            "name": "StorageTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    acceptance_transport_event: Optional[AcceptanceTransportEvent] = field(
        default=None,
        metadata={
            "name": "AcceptanceTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    terminal_operator_party: Optional[TerminalOperatorParty] = field(
        default=None,
        metadata={
            "name": "TerminalOperatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    customs_agent_party: Optional[CustomsAgentParty] = field(
        default=None,
        metadata={
            "name": "CustomsAgentParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_transit_period: Optional[EstimatedTransitPeriod] = field(
        default=None,
        metadata={
            "name": "EstimatedTransitPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    freight_allowance_charge: tuple[FreightAllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    freight_charge_location: Optional[FreightChargeLocation] = field(
        default=None,
        metadata={
            "name": "FreightChargeLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    detention_transport_event: tuple[DetentionTransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DetentionTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_departure_transport_event: Optional[
        RequestedDepartureTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "RequestedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_arrival_transport_event: Optional[
        RequestedArrivalTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "RequestedArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_waypoint_transport_event: tuple[
        RequestedWaypointTransportEvent, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "RequestedWaypointTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_departure_transport_event: Optional[
        PlannedDepartureTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "PlannedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_arrival_transport_event: Optional[PlannedArrivalTransportEvent] = (
        field(
            default=None,
            metadata={
                "name": "PlannedArrivalTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    planned_waypoint_transport_event: tuple[
        PlannedWaypointTransportEvent, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "PlannedWaypointTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    actual_departure_transport_event: Optional[
        ActualDepartureTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    actual_waypoint_transport_event: Optional[ActualWaypointTransportEvent] = (
        field(
            default=None,
            metadata={
                "name": "ActualWaypointTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    actual_arrival_transport_event: Optional[ActualArrivalTransportEvent] = (
        field(
            default=None,
            metadata={
                "name": "ActualArrivalTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    transport_event: tuple[TransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_departure_transport_event: Optional[
        EstimatedDepartureTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "EstimatedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_arrival_transport_event: Optional[
        EstimatedArrivalTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "EstimatedArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    passenger_person: tuple[PassengerPerson, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PassengerPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    driver_person: tuple[DriverPerson, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DriverPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    reporting_person: Optional[ReportingPerson] = field(
        default=None,
        metadata={
            "name": "ReportingPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    crew_member_person: tuple[CrewMemberPerson, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CrewMemberPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    security_officer_person: Optional[SecurityOfficerPerson] = field(
        default=None,
        metadata={
            "name": "SecurityOfficerPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    master_person: Optional[MasterPerson] = field(
        default=None,
        metadata={
            "name": "MasterPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    ships_surgeon_person: Optional[ShipsSurgeonPerson] = field(
        default=None,
        metadata={
            "name": "ShipsSurgeonPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class SupplierConsumptionType:
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    utility_supplier_party: Optional[UtilitySupplierParty] = field(
        default=None,
        metadata={
            "name": "UtilitySupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    utility_customer_party: Optional[UtilityCustomerParty] = field(
        default=None,
        metadata={
            "name": "UtilityCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consumption: Optional[Consumption] = field(
        default=None,
        metadata={
            "name": "Consumption",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    contract: Optional[Contract] = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consumption_line: tuple[ConsumptionLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConsumptionLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "min_occurs": 1,
        },
    )


@dataclass(frozen=True)
class TenderLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_tax_amount: Optional[TotalTaxAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    orderable_unit: Optional[OrderableUnit] = field(
        default=None,
        metadata={
            "name": "OrderableUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    content_unit_quantity: Optional[ContentUnitQuantity] = field(
        default=None,
        metadata={
            "name": "ContentUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_quantity_increment_numeric: Optional[
        OrderQuantityIncrementNumeric
    ] = field(
        default=None,
        metadata={
            "name": "OrderQuantityIncrementNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_order_quantity: Optional[MinimumOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_order_quantity: Optional[MaximumOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    warranty_information: tuple[WarrantyInformation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "WarrantyInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pack_level_code: Optional[PackLevelCode] = field(
        default=None,
        metadata={
            "name": "PackLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    offered_item_location_quantity: tuple[OfferedItemLocationQuantity, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "OfferedItemLocationQuantity",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    replacement_related_item: tuple[ReplacementRelatedItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReplacementRelatedItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_party: Optional[WarrantyParty] = field(
        default=None,
        metadata={
            "name": "WarrantyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sub_tender_line: tuple["SubTenderLine", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubTenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    call_for_tenders_line_reference: Optional[CallForTendersLineReference] = (
        field(
            default=None,
            metadata={
                "name": "CallForTendersLineReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    call_for_tenders_document_reference: Optional[
        CallForTendersDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "CallForTendersDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransportEquipmentType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    referenced_consignment_id: tuple[ReferencedConsignmentId, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReferencedConsignmentID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_equipment_type_code: Optional[TransportEquipmentTypeCode] = (
        field(
            default=None,
            metadata={
                "name": "TransportEquipmentTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    provider_type_code: Optional[ProviderTypeCode] = field(
        default=None,
        metadata={
            "name": "ProviderTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    owner_type_code: Optional[OwnerTypeCode] = field(
        default=None,
        metadata={
            "name": "OwnerTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    size_type_code: Optional[SizeTypeCode] = field(
        default=None,
        metadata={
            "name": "SizeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    disposition_code: Optional[DispositionCode] = field(
        default=None,
        metadata={
            "name": "DispositionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fullness_indication_code: Optional[FullnessIndicationCode] = field(
        default=None,
        metadata={
            "name": "FullnessIndicationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    refrigeration_on_indicator: Optional[RefrigerationOnIndicator] = field(
        default=None,
        metadata={
            "name": "RefrigerationOnIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    information: tuple[Information, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Information",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    returnability_indicator: Optional[ReturnabilityIndicator] = field(
        default=None,
        metadata={
            "name": "ReturnabilityIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    legal_status_indicator: Optional[LegalStatusIndicator] = field(
        default=None,
        metadata={
            "name": "LegalStatusIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    air_flow_percent: Optional[AirFlowPercent] = field(
        default=None,
        metadata={
            "name": "AirFlowPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    humidity_percent: Optional[HumidityPercent] = field(
        default=None,
        metadata={
            "name": "HumidityPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    animal_food_approved_indicator: Optional[AnimalFoodApprovedIndicator] = (
        field(
            default=None,
            metadata={
                "name": "AnimalFoodApprovedIndicator",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    human_food_approved_indicator: Optional[HumanFoodApprovedIndicator] = (
        field(
            default=None,
            metadata={
                "name": "HumanFoodApprovedIndicator",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    dangerous_goods_approved_indicator: Optional[
        DangerousGoodsApprovedIndicator
    ] = field(
        default=None,
        metadata={
            "name": "DangerousGoodsApprovedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    refrigerated_indicator: Optional[RefrigeratedIndicator] = field(
        default=None,
        metadata={
            "name": "RefrigeratedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    characteristics: Optional[Characteristics] = field(
        default=None,
        metadata={
            "name": "Characteristics",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    damage_remarks: tuple[DamageRemarks, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DamageRemarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    special_transport_requirements: tuple[
        SpecialTransportRequirements, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "SpecialTransportRequirements",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_weight_measure: Optional[GrossWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_volume_measure: Optional[GrossVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tare_weight_measure: Optional[TareWeightMeasure] = field(
        default=None,
        metadata={
            "name": "TareWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tracking_device_code: Optional[TrackingDeviceCode] = field(
        default=None,
        metadata={
            "name": "TrackingDeviceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    power_indicator: Optional[PowerIndicator] = field(
        default=None,
        metadata={
            "name": "PowerIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trace_id: Optional[TraceId] = field(
        default=None,
        metadata={
            "name": "TraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    measurement_dimension: tuple[MeasurementDimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_equipment_seal: tuple[TransportEquipmentSeal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportEquipmentSeal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    minimum_temperature: Optional[MinimumTemperature] = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maximum_temperature: Optional[MaximumTemperature] = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    provider_party: Optional[ProviderParty] = field(
        default=None,
        metadata={
            "name": "ProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    loading_proof_party: Optional[LoadingProofParty] = field(
        default=None,
        metadata={
            "name": "LoadingProofParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supplier_party: Optional[SupplierParty] = field(
        default=None,
        metadata={
            "name": "SupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    owner_party: Optional[OwnerParty] = field(
        default=None,
        metadata={
            "name": "OwnerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    operating_party: Optional[OperatingParty] = field(
        default=None,
        metadata={
            "name": "OperatingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    loading_location: Optional[LoadingLocation] = field(
        default=None,
        metadata={
            "name": "LoadingLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    unloading_location: Optional[UnloadingLocation] = field(
        default=None,
        metadata={
            "name": "UnloadingLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    storage_location: Optional[StorageLocation] = field(
        default=None,
        metadata={
            "name": "StorageLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    positioning_transport_event: tuple[PositioningTransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PositioningTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    quarantine_transport_event: tuple[QuarantineTransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "QuarantineTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_transport_event: tuple[DeliveryTransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pickup_transport_event: tuple[PickupTransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PickupTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    handling_transport_event: tuple[HandlingTransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HandlingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    loading_transport_event: tuple[LoadingTransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "LoadingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_event: tuple[TransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    applicable_transport_means: Optional[ApplicableTransportMeans] = field(
        default=None,
        metadata={
            "name": "ApplicableTransportMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    haulage_trading_terms: tuple[HaulageTradingTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HaulageTradingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    hazardous_goods_transit: tuple[HazardousGoodsTransit, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HazardousGoodsTransit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    packaged_transport_handling_unit: tuple[
        "PackagedTransportHandlingUnit", ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "PackagedTransportHandlingUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    service_allowance_charge: tuple[ServiceAllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ServiceAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    freight_allowance_charge: tuple[FreightAllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FreightAllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    attached_transport_equipment: tuple["AttachedTransportEquipment", ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "AttachedTransportEquipment",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    delivery: Optional[Delivery] = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pickup: Optional[Pickup] = field(
        default=None,
        metadata={
            "name": "Pickup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch: Optional[Despatch] = field(
        default=None,
        metadata={
            "name": "Despatch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment_document_reference: tuple[ShipmentDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ShipmentDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contained_in_transport_equipment: tuple[
        "ContainedInTransportEquipment", ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "ContainedInTransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    package: tuple[Package, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    goods_item: tuple[GoodsItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "GoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransportScheduleType:
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    reference_date: Optional[ReferenceDate] = field(
        default=None,
        metadata={
            "name": "ReferenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reference_time: Optional[ReferenceTime] = field(
        default=None,
        metadata={
            "name": "ReferenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reliability_percent: Optional[ReliabilityPercent] = field(
        default=None,
        metadata={
            "name": "ReliabilityPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    remarks: tuple[Remarks, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    status_location: Optional[StatusLocation] = field(
        default=None,
        metadata={
            "name": "StatusLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    actual_arrival_transport_event: Optional[ActualArrivalTransportEvent] = (
        field(
            default=None,
            metadata={
                "name": "ActualArrivalTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    actual_departure_transport_event: Optional[
        ActualDepartureTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "ActualDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_departure_transport_event: Optional[
        EstimatedDepartureTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "EstimatedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_arrival_transport_event: Optional[
        EstimatedArrivalTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "EstimatedArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_departure_transport_event: Optional[
        PlannedDepartureTransportEvent
    ] = field(
        default=None,
        metadata={
            "name": "PlannedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_arrival_transport_event: Optional[PlannedArrivalTransportEvent] = (
        field(
            default=None,
            metadata={
                "name": "PlannedArrivalTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )


@dataclass(frozen=True)
class AttachedTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CatalogueLine(CatalogueLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CataloguePricingUpdateLine(CataloguePricingUpdateLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CatalogueRequestLine(CatalogueRequestLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContainedInTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ContainingTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ItemManagementProfile(ItemManagementProfileType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MainCarriageShipmentStage(ShipmentStageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OnCarriageShipmentStage(ShipmentStageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PreCarriageShipmentStage(ShipmentStageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PricingReference(PricingReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ReferencedTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestForTenderLine(RequestForTenderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ShipmentStage(ShipmentStageType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubRequestForTenderLine(RequestForTenderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubTenderLine(TenderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SupplierConsumption(SupplierConsumptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SupportedTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderLine(TenderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportSchedule(TransportScheduleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class UnsupportedTransportEquipment(TransportEquipmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CreditNoteLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    credited_quantity: Optional[CreditedQuantity] = field(
        default=None,
        metadata={
            "name": "CreditedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_point_date: Optional[TaxPointDate] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_of_charge_indicator: Optional[FreeOfChargeIndicator] = field(
        default=None,
        metadata={
            "name": "FreeOfChargeIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoice_period: tuple[InvoicePeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    order_line_reference: tuple[OrderLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    discrepancy_response: tuple[DiscrepancyResponse, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DiscrepancyResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_line_reference: tuple[DespatchLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DespatchLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    receipt_line_reference: tuple[ReceiptLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReceiptLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    billing_reference: tuple[BillingReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pricing_reference: Optional[PricingReference] = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_party: Optional[OriginatorParty] = field(
        default=None,
        metadata={
            "name": "OriginatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: tuple[Delivery, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_terms: tuple[PaymentTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: tuple[DeliveryTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sub_credit_note_line: tuple["SubCreditNoteLine", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubCreditNoteLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_price_extension: Optional[ItemPriceExtension] = field(
        default=None,
        metadata={
            "name": "ItemPriceExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DebitNoteLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    debited_quantity: Optional[DebitedQuantity] = field(
        default=None,
        metadata={
            "name": "DebitedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tax_point_date: Optional[TaxPointDate] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    discrepancy_response: tuple[DiscrepancyResponse, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DiscrepancyResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_line_reference: tuple[DespatchLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DespatchLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    receipt_line_reference: tuple[ReceiptLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReceiptLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    billing_reference: tuple[BillingReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pricing_reference: Optional[PricingReference] = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: tuple[Delivery, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sub_debit_note_line: tuple["SubDebitNoteLine", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubDebitNoteLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class GoodsItemContainerType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_equipment: tuple[TransportEquipment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class InvoiceLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoiced_quantity: Optional[InvoicedQuantity] = field(
        default=None,
        metadata={
            "name": "InvoicedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tax_point_date: Optional[TaxPointDate] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: Optional[PaymentPurposeCode] = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_of_charge_indicator: Optional[FreeOfChargeIndicator] = field(
        default=None,
        metadata={
            "name": "FreeOfChargeIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoice_period: tuple[InvoicePeriod, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "InvoicePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    order_line_reference: tuple[OrderLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_line_reference: tuple[DespatchLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DespatchLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    receipt_line_reference: tuple[ReceiptLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReceiptLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    billing_reference: tuple[BillingReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BillingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pricing_reference: Optional[PricingReference] = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_party: Optional[OriginatorParty] = field(
        default=None,
        metadata={
            "name": "OriginatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: tuple[Delivery, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_terms: tuple[PaymentTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    withholding_tax_total: tuple[WithholdingTaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "WithholdingTaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: Optional[DeliveryTerms] = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sub_invoice_line: tuple["SubInvoiceLine", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubInvoiceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_price_extension: Optional[ItemPriceExtension] = field(
        default=None,
        metadata={
            "name": "ItemPriceExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class LineItemType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    sales_order_id: Optional[SalesOrderId] = field(
        default=None,
        metadata={
            "name": "SalesOrderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_status_code: Optional[LineStatusCode] = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_tax_amount: Optional[TotalTaxAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: Optional[MinimumQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: Optional[MaximumQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_backorder_quantity: Optional[MinimumBackorderQuantity] = field(
        default=None,
        metadata={
            "name": "MinimumBackorderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_backorder_quantity: Optional[MaximumBackorderQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumBackorderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    inspection_method_code: Optional[InspectionMethodCode] = field(
        default=None,
        metadata={
            "name": "InspectionMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    partial_delivery_indicator: Optional[PartialDeliveryIndicator] = field(
        default=None,
        metadata={
            "name": "PartialDeliveryIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    back_order_allowed_indicator: Optional[BackOrderAllowedIndicator] = field(
        default=None,
        metadata={
            "name": "BackOrderAllowedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: Optional[AccountingCostCode] = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: Optional[AccountingCost] = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    warranty_information: tuple[WarrantyInformation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "WarrantyInformation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivery: tuple[Delivery, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: Optional[DeliveryTerms] = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_party: Optional[OriginatorParty] = field(
        default=None,
        metadata={
            "name": "OriginatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    ordered_shipment: tuple[OrderedShipment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrderedShipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pricing_reference: Optional[PricingReference] = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: tuple[AllowanceCharge, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    price: Optional[Price] = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Optional[Item] = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    sub_line_item: tuple["SubLineItem", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_party: Optional[WarrantyParty] = field(
        default=None,
        metadata={
            "name": "WarrantyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_price_extension: Optional[ItemPriceExtension] = field(
        default=None,
        metadata={
            "name": "ItemPriceExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    line_reference: tuple[LineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "LineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ProcurementProjectType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "min_occurs": 1,
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    procurement_type_code: Optional[ProcurementTypeCode] = field(
        default=None,
        metadata={
            "name": "ProcurementTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    procurement_sub_type_code: Optional[ProcurementSubTypeCode] = field(
        default=None,
        metadata={
            "name": "ProcurementSubTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quality_control_code: Optional[QualityControlCode] = field(
        default=None,
        metadata={
            "name": "QualityControlCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_fee_amount: Optional[RequiredFeeAmount] = field(
        default=None,
        metadata={
            "name": "RequiredFeeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fee_description: tuple[FeeDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FeeDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    requested_delivery_date: Optional[RequestedDeliveryDate] = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_overall_contract_quantity: Optional[
        EstimatedOverallContractQuantity
    ] = field(
        default=None,
        metadata={
            "name": "EstimatedOverallContractQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    requested_tender_total: Optional[RequestedTenderTotal] = field(
        default=None,
        metadata={
            "name": "RequestedTenderTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    main_commodity_classification: Optional[MainCommodityClassification] = (
        field(
            default=None,
            metadata={
                "name": "MainCommodityClassification",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    additional_commodity_classification: tuple[
        AdditionalCommodityClassification, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalCommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    realized_location: tuple[RealizedLocation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RealizedLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_period: Optional[PlannedPeriod] = field(
        default=None,
        metadata={
            "name": "PlannedPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_extension: Optional[ContractExtension] = field(
        default=None,
        metadata={
            "name": "ContractExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    request_for_tender_line: tuple[RequestForTenderLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RequestForTenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class SubscriberConsumptionType:
    consumption_id: Optional[ConsumptionId] = field(
        default=None,
        metadata={
            "name": "ConsumptionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    specification_type_code: Optional[SpecificationTypeCode] = field(
        default=None,
        metadata={
            "name": "SpecificationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_metered_quantity: Optional[TotalMeteredQuantity] = field(
        default=None,
        metadata={
            "name": "TotalMeteredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_party: Optional[SubscriberParty] = field(
        default=None,
        metadata={
            "name": "SubscriberParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    utility_consumption_point: Optional[UtilityConsumptionPoint] = field(
        default=None,
        metadata={
            "name": "UtilityConsumptionPoint",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    on_account_payment: tuple[OnAccountPayment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OnAccountPayment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consumption: Optional[Consumption] = field(
        default=None,
        metadata={
            "name": "Consumption",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supplier_consumption: tuple[SupplierConsumption, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SupplierConsumption",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransportHandlingUnitType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_handling_unit_type_code: Optional[
        TransportHandlingUnitTypeCode
    ] = field(
        default=None,
        metadata={
            "name": "TransportHandlingUnitTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_code: Optional[HandlingCode] = field(
        default=None,
        metadata={
            "name": "HandlingCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_instructions: tuple[HandlingInstructions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HandlingInstructions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_risk_indicator: Optional[HazardousRiskIndicator] = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_goods_item_quantity: Optional[TotalGoodsItemQuantity] = field(
        default=None,
        metadata={
            "name": "TotalGoodsItemQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_package_quantity: Optional[TotalPackageQuantity] = field(
        default=None,
        metadata={
            "name": "TotalPackageQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    damage_remarks: tuple[DamageRemarks, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DamageRemarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    shipping_marks: tuple[ShippingMarks, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ShippingMarks",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trace_id: Optional[TraceId] = field(
        default=None,
        metadata={
            "name": "TraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_unit_despatch_line: tuple[HandlingUnitDespatchLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HandlingUnitDespatchLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    actual_package: tuple[ActualPackage, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ActualPackage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    received_handling_unit_receipt_line: tuple[
        ReceivedHandlingUnitReceiptLine, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "ReceivedHandlingUnitReceiptLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_equipment: tuple[TransportEquipment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_means: tuple[TransportMeans, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    hazardous_goods_transit: tuple[HazardousGoodsTransit, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HazardousGoodsTransit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    measurement_dimension: tuple[MeasurementDimension, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    minimum_temperature: Optional[MinimumTemperature] = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maximum_temperature: Optional[MaximumTemperature] = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    goods_item: tuple[GoodsItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "GoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    floor_space_measurement_dimension: Optional[
        FloorSpaceMeasurementDimension
    ] = field(
        default=None,
        metadata={
            "name": "FloorSpaceMeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pallet_space_measurement_dimension: Optional[
        PalletSpaceMeasurementDimension
    ] = field(
        default=None,
        metadata={
            "name": "PalletSpaceMeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment_document_reference: tuple[ShipmentDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ShipmentDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    status: tuple[Status, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    customs_declaration: tuple[CustomsDeclaration, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CustomsDeclaration",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    referenced_shipment: tuple[ReferencedShipment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ReferencedShipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    package: tuple[Package, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Package",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransportationServiceType:
    transport_service_code: Optional[TransportServiceCode] = field(
        default=None,
        metadata={
            "name": "TransportServiceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tariff_class_code: Optional[TariffClassCode] = field(
        default=None,
        metadata={
            "name": "TariffClassCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    priority: Optional[Priority] = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    freight_rate_class_code: Optional[FreightRateClassCode] = field(
        default=None,
        metadata={
            "name": "FreightRateClassCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transportation_service_description: tuple[
        TransportationServiceDescription, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportationServiceDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transportation_service_details_uri: Optional[
        TransportationServiceDetailsUri
    ] = field(
        default=None,
        metadata={
            "name": "TransportationServiceDetailsURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nomination_date: Optional[NominationDate] = field(
        default=None,
        metadata={
            "name": "NominationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nomination_time: Optional[NominationTime] = field(
        default=None,
        metadata={
            "name": "NominationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Optional[Name] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_equipment: tuple[TransportEquipment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supported_transport_equipment: tuple[SupportedTransportEquipment, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "SupportedTransportEquipment",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    unsupported_transport_equipment: tuple[
        UnsupportedTransportEquipment, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "UnsupportedTransportEquipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    commodity_classification: tuple[CommodityClassification, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supported_commodity_classification: tuple[
        SupportedCommodityClassification, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "SupportedCommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    unsupported_commodity_classification: tuple[
        UnsupportedCommodityClassification, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "UnsupportedCommodityClassification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    total_capacity_dimension: Optional[TotalCapacityDimension] = field(
        default=None,
        metadata={
            "name": "TotalCapacityDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment_stage: tuple[ShipmentStage, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_event: tuple[TransportEvent, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    responsible_transport_service_provider_party: Optional[
        ResponsibleTransportServiceProviderParty
    ] = field(
        default=None,
        metadata={
            "name": "ResponsibleTransportServiceProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    environmental_emission: tuple[EnvironmentalEmission, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EnvironmentalEmission",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_duration_period: Optional[EstimatedDurationPeriod] = field(
        default=None,
        metadata={
            "name": "EstimatedDurationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    scheduled_service_frequency: tuple[ScheduledServiceFrequency, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ScheduledServiceFrequency",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class AdditionalTransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class AlternativeLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class BuyerProposedSubstituteLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class CreditNoteLine(CreditNoteLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class DebitNoteLine(DebitNoteLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class FinalDeliveryTransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class GoodsItemContainer(GoodsItemContainerType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class InvoiceLine(InvoiceLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class LineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class MainTransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OriginalDespatchTransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class PackagedTransportHandlingUnit(TransportHandlingUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ProcurementProject(ProcurementProjectType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SellerProposedSubstituteLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SellerSubstitutedLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubCreditNoteLine(CreditNoteLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubDebitNoteLine(DebitNoteLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubInvoiceLine(InvoiceLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubLineItem(LineItemType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class SubscriberConsumption(SubscriberConsumptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportHandlingUnit(TransportHandlingUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportationService(TransportationServiceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OrderLineType:
    substitution_status_code: Optional[SubstitutionStatusCode] = field(
        default=None,
        metadata={
            "name": "SubstitutionStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_item: Optional[LineItem] = field(
        default=None,
        metadata={
            "name": "LineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    seller_proposed_substitute_line_item: tuple[
        SellerProposedSubstituteLineItem, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "SellerProposedSubstituteLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_substituted_line_item: tuple[SellerSubstitutedLineItem, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "SellerSubstitutedLineItem",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    buyer_proposed_substitute_line_item: tuple[
        BuyerProposedSubstituteLineItem, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "BuyerProposedSubstituteLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    catalogue_line_reference: Optional[CatalogueLineReference] = field(
        default=None,
        metadata={
            "name": "CatalogueLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    quotation_line_reference: Optional[QuotationLineReference] = field(
        default=None,
        metadata={
            "name": "QuotationLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    order_line_reference: tuple[OrderLineReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OrderLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ProcurementProjectLotType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tendering_terms: Optional["TenderingTerms"] = field(
        default=None,
        metadata={
            "name": "TenderingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    procurement_project: Optional[ProcurementProject] = field(
        default=None,
        metadata={
            "name": "ProcurementProject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class QuotationLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: Optional[LineExtensionAmount] = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_tax_amount: Optional[TotalTaxAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    request_for_quotation_line_id: Optional[RequestForQuotationLineId] = field(
        default=None,
        metadata={
            "name": "RequestForQuotationLineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    line_item: Optional[LineItem] = field(
        default=None,
        metadata={
            "name": "LineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    seller_proposed_substitute_line_item: tuple[
        SellerProposedSubstituteLineItem, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "SellerProposedSubstituteLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    alternative_line_item: tuple[AlternativeLineItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AlternativeLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    request_line_reference: Optional[RequestLineReference] = field(
        default=None,
        metadata={
            "name": "RequestLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RequestForQuotationLineType:
    id: Optional[Id] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Optional[Uuid] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    optional_line_item_indicator: Optional[OptionalLineItemIndicator] = field(
        default=None,
        metadata={
            "name": "OptionalLineItemIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    privacy_code: Optional[PrivacyCode] = field(
        default=None,
        metadata={
            "name": "PrivacyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    security_classification_code: Optional[SecurityClassificationCode] = field(
        default=None,
        metadata={
            "name": "SecurityClassificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_reference: tuple[DocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    line_item: Optional[LineItem] = field(
        default=None,
        metadata={
            "name": "LineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )


@dataclass(frozen=True)
class TransportationSegmentType:
    sequence_numeric: Optional[SequenceNumeric] = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    transport_execution_plan_reference_id: Optional[
        TransportExecutionPlanReferenceId
    ] = field(
        default=None,
        metadata={
            "name": "TransportExecutionPlanReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transportation_service: Optional[TransportationService] = field(
        default=None,
        metadata={
            "name": "TransportationService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    transport_service_provider_party: Optional[
        TransportServiceProviderParty
    ] = field(
        default=None,
        metadata={
            "name": "TransportServiceProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    referenced_consignment: Optional[ReferencedConsignment] = field(
        default=None,
        metadata={
            "name": "ReferencedConsignment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment_stage: tuple[ShipmentStage, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class InterestedProcurementProjectLot(ProcurementProjectLotType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class OrderLine(OrderLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class ProcurementProjectLot(ProcurementProjectLotType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class QuotationLine(QuotationLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class RequestForQuotationLine(RequestForQuotationLineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TransportationSegment(TransportationSegmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class QualificationResolutionType:
    admission_code: Optional[AdmissionCode] = field(
        default=None,
        metadata={
            "name": "AdmissionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    exclusion_reason: tuple[ExclusionReason, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ExclusionReason",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    resolution: tuple[Resolution, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Resolution",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    resolution_date: Optional[ResolutionDate] = field(
        default=None,
        metadata={
            "name": "ResolutionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    resolution_time: Optional[ResolutionTime] = field(
        default=None,
        metadata={
            "name": "ResolutionTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    procurement_project_lot: Optional[ProcurementProjectLot] = field(
        default=None,
        metadata={
            "name": "ProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TenderPreparationType:
    tender_envelope_id: Optional[TenderEnvelopeId] = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tender_envelope_type_code: Optional[TenderEnvelopeTypeCode] = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    open_tender_id: Optional[OpenTenderId] = field(
        default=None,
        metadata={
            "name": "OpenTenderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    procurement_project_lot: tuple[ProcurementProjectLot, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_tender_requirement: tuple[DocumentTenderRequirement, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DocumentTenderRequirement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TenderedProjectType:
    variant_id: Optional[VariantId] = field(
        default=None,
        metadata={
            "name": "VariantID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fee_amount: Optional[FeeAmount] = field(
        default=None,
        metadata={
            "name": "FeeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fee_description: tuple[FeeDescription, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FeeDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tender_envelope_id: Optional[TenderEnvelopeId] = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tender_envelope_type_code: Optional[TenderEnvelopeTypeCode] = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    procurement_project_lot: Optional[ProcurementProjectLot] = field(
        default=None,
        metadata={
            "name": "ProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    evidence_document_reference: tuple[EvidenceDocumentReference, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EvidenceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_total: tuple[TaxTotal, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TaxTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    legal_monetary_total: Optional[LegalMonetaryTotal] = field(
        default=None,
        metadata={
            "name": "LegalMonetaryTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_line: tuple[TenderLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    awarding_criterion_response: tuple[AwardingCriterionResponse, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AwardingCriterionResponse",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TendererPartyQualificationType:
    interested_procurement_project_lot: tuple[
        InterestedProcurementProjectLot, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "InterestedProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    main_qualifying_party: Optional[MainQualifyingParty] = field(
        default=None,
        metadata={
            "name": "MainQualifyingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    additional_qualifying_party: tuple[AdditionalQualifyingParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalQualifyingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class AwardedTenderedProject(TenderedProjectType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class QualificationResolution(QualificationResolutionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderPreparation(TenderPreparationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderedProject(TenderedProjectType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TendererPartyQualification(TendererPartyQualificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderResultType:
    tender_result_code: Optional[TenderResultCode] = field(
        default=None,
        metadata={
            "name": "TenderResultCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description: tuple[Description, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    advertisement_amount: Optional[AdvertisementAmount] = field(
        default=None,
        metadata={
            "name": "AdvertisementAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    award_date: Optional[AwardDate] = field(
        default=None,
        metadata={
            "name": "AwardDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    award_time: Optional[AwardTime] = field(
        default=None,
        metadata={
            "name": "AwardTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_tender_quantity: Optional[ReceivedTenderQuantity] = field(
        default=None,
        metadata={
            "name": "ReceivedTenderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    lower_tender_amount: Optional[LowerTenderAmount] = field(
        default=None,
        metadata={
            "name": "LowerTenderAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    higher_tender_amount: Optional[HigherTenderAmount] = field(
        default=None,
        metadata={
            "name": "HigherTenderAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    start_date: Optional[StartDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_electronic_tender_quantity: Optional[
        ReceivedElectronicTenderQuantity
    ] = field(
        default=None,
        metadata={
            "name": "ReceivedElectronicTenderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_foreign_tender_quantity: Optional[
        ReceivedForeignTenderQuantity
    ] = field(
        default=None,
        metadata={
            "name": "ReceivedForeignTenderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract: Optional[Contract] = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    awarded_tendered_project: Optional[AwardedTenderedProject] = field(
        default=None,
        metadata={
            "name": "AwardedTenderedProject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_formalization_period: Optional[ContractFormalizationPeriod] = (
        field(
            default=None,
            metadata={
                "name": "ContractFormalizationPeriod",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    subcontract_terms: tuple[SubcontractTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubcontractTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    winning_party: tuple[WinningParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "WinningParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TenderingTermsType:
    awarding_method_type_code: Optional[AwardingMethodTypeCode] = field(
        default=None,
        metadata={
            "name": "AwardingMethodTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    price_evaluation_code: Optional[PriceEvaluationCode] = field(
        default=None,
        metadata={
            "name": "PriceEvaluationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_variant_quantity: Optional[MaximumVariantQuantity] = field(
        default=None,
        metadata={
            "name": "MaximumVariantQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    variant_constraint_indicator: Optional[VariantConstraintIndicator] = field(
        default=None,
        metadata={
            "name": "VariantConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accepted_variants_description: tuple[AcceptedVariantsDescription, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "AcceptedVariantsDescription",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    price_revision_formula_description: tuple[
        PriceRevisionFormulaDescription, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "PriceRevisionFormulaDescription",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    funding_program_code: Optional[FundingProgramCode] = field(
        default=None,
        metadata={
            "name": "FundingProgramCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    funding_program: tuple[FundingProgram, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FundingProgram",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_advertisement_amount: Optional[MaximumAdvertisementAmount] = field(
        default=None,
        metadata={
            "name": "MaximumAdvertisementAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    note: tuple[Note, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Note",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_frequency_code: Optional[PaymentFrequencyCode] = field(
        default=None,
        metadata={
            "name": "PaymentFrequencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    economic_operator_registry_uri: Optional[EconomicOperatorRegistryUri] = (
        field(
            default=None,
            metadata={
                "name": "EconomicOperatorRegistryURI",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    required_curricula_indicator: Optional[RequiredCurriculaIndicator] = field(
        default=None,
        metadata={
            "name": "RequiredCurriculaIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    other_conditions_indicator: Optional[OtherConditionsIndicator] = field(
        default=None,
        metadata={
            "name": "OtherConditionsIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    additional_conditions: tuple[AdditionalConditions, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AdditionalConditions",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_security_clearance_date: Optional[LatestSecurityClearanceDate] = (
        field(
            default=None,
            metadata={
                "name": "LatestSecurityClearanceDate",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    documentation_fee_amount: Optional[DocumentationFeeAmount] = field(
        default=None,
        metadata={
            "name": "DocumentationFeeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    penalty_clause: tuple[PenaltyClause, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PenaltyClause",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    required_financial_guarantee: tuple[RequiredFinancialGuarantee, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "RequiredFinancialGuarantee",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    procurement_legislation_document_reference: Optional[
        ProcurementLegislationDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "ProcurementLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    fiscal_legislation_document_reference: Optional[
        FiscalLegislationDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "FiscalLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    environmental_legislation_document_reference: Optional[
        EnvironmentalLegislationDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "EnvironmentalLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    employment_legislation_document_reference: Optional[
        EmploymentLegislationDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "EmploymentLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contractual_document_reference: tuple[
        ContractualDocumentReference, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "ContractualDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    call_for_tenders_document_reference: Optional[
        CallForTendersDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "CallForTendersDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_validity_period: Optional[WarrantyValidityPeriod] = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_terms: tuple[PaymentTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tenderer_qualification_request: tuple[
        TendererQualificationRequest, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "TendererQualificationRequest",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowed_subcontract_terms: tuple[AllowedSubcontractTerms, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AllowedSubcontractTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_preparation: tuple[TenderPreparation, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TenderPreparation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_execution_requirement: tuple[
        ContractExecutionRequirement, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "name": "ContractExecutionRequirement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    awarding_terms: Optional[AwardingTerms] = field(
        default=None,
        metadata={
            "name": "AwardingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    additional_information_party: Optional[AdditionalInformationParty] = field(
        default=None,
        metadata={
            "name": "AdditionalInformationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_provider_party: Optional[DocumentProviderParty] = field(
        default=None,
        metadata={
            "name": "DocumentProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_recipient_party: Optional[TenderRecipientParty] = field(
        default=None,
        metadata={
            "name": "TenderRecipientParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_responsible_party: Optional[ContractResponsibleParty] = field(
        default=None,
        metadata={
            "name": "ContractResponsibleParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_evaluation_party: tuple[TenderEvaluationParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TenderEvaluationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_validity_period: Optional[TenderValidityPeriod] = field(
        default=None,
        metadata={
            "name": "TenderValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_acceptance_period: Optional[ContractAcceptancePeriod] = field(
        default=None,
        metadata={
            "name": "ContractAcceptancePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    appeal_terms: Optional[AppealTerms] = field(
        default=None,
        metadata={
            "name": "AppealTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    language: tuple[Language, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    budget_account_line: tuple[BudgetAccountLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "BudgetAccountLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    replaced_notice_document_reference: Optional[
        ReplacedNoticeDocumentReference
    ] = field(
        default=None,
        metadata={
            "name": "ReplacedNoticeDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TenderResult(TenderResultType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"


@dataclass(frozen=True)
class TenderingTerms(TenderingTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
