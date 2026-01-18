from __future__ import annotations

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
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    value: Value | None = field(
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
    line: Line | None = field(
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
    aircraft_id: AircraftId | None = field(
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
    auction_constraint_indicator: AuctionConstraintIndicator | None = field(
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
    auction_uri: AuctionUri | None = field(
        default=None,
        metadata={
            "name": "AuctionURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class AwardingCriterionResponseType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    awarding_criterion_id: AwardingCriterionId | None = field(
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
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subordinate_awarding_criterion_response: tuple[
        SubordinateAwardingCriterionResponse, ...
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    awarding_criterion_type_code: AwardingCriterionTypeCode | None = field(
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
    weight_numeric: WeightNumeric | None = field(
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
    calculation_expression_code: CalculationExpressionCode | None = field(
        default=None,
        metadata={
            "name": "CalculationExpressionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: MinimumQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: MaximumQuantity | None = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_amount: MinimumAmount | None = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_amount: MaximumAmount | None = field(
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
        SubordinateAwardingCriterion, ...
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
    primary_account_number_id: PrimaryAccountNumberId | None = field(
        default=None,
        metadata={
            "name": "PrimaryAccountNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    network_id: NetworkId | None = field(
        default=None,
        metadata={
            "name": "NetworkID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    card_type_code: CardTypeCode | None = field(
        default=None,
        metadata={
            "name": "CardTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validity_start_date: ValidityStartDate | None = field(
        default=None,
        metadata={
            "name": "ValidityStartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expiry_date: ExpiryDate | None = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issuer_id: IssuerId | None = field(
        default=None,
        metadata={
            "name": "IssuerID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_number_id: IssueNumberId | None = field(
        default=None,
        metadata={
            "name": "IssueNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    cv2_id: Cv2Id | None = field(
        default=None,
        metadata={
            "name": "CV2ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    card_chip_code: CardChipCode | None = field(
        default=None,
        metadata={
            "name": "CardChipCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    chip_application_id: ChipApplicationId | None = field(
        default=None,
        metadata={
            "name": "ChipApplicationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    holder_name: HolderName | None = field(
        default=None,
        metadata={
            "name": "HolderName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class CatalogueReferenceType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: IssueDate | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: IssueTime | None = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    revision_date: RevisionDate | None = field(
        default=None,
        metadata={
            "name": "RevisionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    revision_time: RevisionTime | None = field(
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
    version_id: VersionId | None = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    previous_version_id: PreviousVersionId | None = field(
        default=None,
        metadata={
            "name": "PreviousVersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ClassificationCategoryType:
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    code_value: CodeValue | None = field(
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
        CategorizesClassificationCategory, ...
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
    id: Id | None = field(
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
    nature_code: NatureCode | None = field(
        default=None,
        metadata={
            "name": "NatureCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    cargo_type_code: CargoTypeCode | None = field(
        default=None,
        metadata={
            "name": "CargoTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    commodity_code: CommodityCode | None = field(
        default=None,
        metadata={
            "name": "CommodityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    item_classification_code: ItemClassificationCode | None = field(
        default=None,
        metadata={
            "name": "ItemClassificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class CommunicationType:
    channel_code: ChannelCode | None = field(
        default=None,
        metadata={
            "name": "ChannelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    channel: Channel | None = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value: Value | None = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ConditionType:
    attribute_id: AttributeId | None = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    measure: Measure | None = field(
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
    minimum_measure: MinimumMeasure | None = field(
        default=None,
        metadata={
            "name": "MinimumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_measure: MaximumMeasure | None = field(
        default=None,
        metadata={
            "name": "MaximumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ConsumptionAverageType:
    average_amount: AverageAmount | None = field(
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
    correction_type: CorrectionType | None = field(
        default=None,
        metadata={
            "name": "CorrectionType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    correction_type_code: CorrectionTypeCode | None = field(
        default=None,
        metadata={
            "name": "CorrectionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_number: MeterNumber | None = field(
        default=None,
        metadata={
            "name": "MeterNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gas_pressure_quantity: GasPressureQuantity | None = field(
        default=None,
        metadata={
            "name": "GasPressureQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_temperature_reduction_quantity: ActualTemperatureReductionQuantity | None = field(
        default=None,
        metadata={
            "name": "ActualTemperatureReductionQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    normal_temperature_reduction_quantity: NormalTemperatureReductionQuantity | None = field(
        default=None,
        metadata={
            "name": "NormalTemperatureReductionQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    difference_temperature_reduction_quantity: DifferenceTemperatureReductionQuantity | None = field(
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
    correction_unit_amount: CorrectionUnitAmount | None = field(
        default=None,
        metadata={
            "name": "CorrectionUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_energy_quantity: ConsumptionEnergyQuantity | None = field(
        default=None,
        metadata={
            "name": "ConsumptionEnergyQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_water_quantity: ConsumptionWaterQuantity | None = field(
        default=None,
        metadata={
            "name": "ConsumptionWaterQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    correction_amount: CorrectionAmount | None = field(
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
    execution_requirement_code: ExecutionRequirementCode | None = field(
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
    activity_type_code: ActivityTypeCode | None = field(
        default=None,
        metadata={
            "name": "ActivityTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    activity_type: ActivityType | None = field(
        default=None,
        metadata={
            "name": "ActivityType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ContractingPartyTypeType:
    party_type_code: PartyTypeCode | None = field(
        default=None,
        metadata={
            "name": "PartyTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party_type: UblCommonBasicComponents21PartyType | None = field(
        default=None,
        metadata={
            "name": "PartyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class CountryType:
    identification_code: IdentificationCode | None = field(
        default=None,
        metadata={
            "name": "IdentificationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class CreditAccountType:
    account_id: AccountId | None = field(
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
    batch_quantity: BatchQuantity | None = field(
        default=None,
        metadata={
            "name": "BatchQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    consumer_unit_quantity: ConsumerUnitQuantity | None = field(
        default=None,
        metadata={
            "name": "ConsumerUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_risk_indicator: HazardousRiskIndicator | None = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class DimensionType:
    attribute_id: AttributeId | None = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    measure: Measure | None = field(
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
    minimum_measure: MinimumMeasure | None = field(
        default=None,
        metadata={
            "name": "MinimumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_measure: MaximumMeasure | None = field(
        default=None,
        metadata={
            "name": "MaximumMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class EconomicOperatorRoleType:
    role_code: RoleCode | None = field(
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
    comment: Comment | None = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_date: IssueDate | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: IssueTime | None = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class EventTacticEnumerationType:
    consumer_incentive_tactic_type_code: ConsumerIncentiveTacticTypeCode | None = field(
        default=None,
        metadata={
            "name": "ConsumerIncentiveTacticTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    display_tactic_type_code: DisplayTacticTypeCode | None = field(
        default=None,
        metadata={
            "name": "DisplayTacticTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    feature_tactic_type_code: FeatureTacticTypeCode | None = field(
        default=None,
        metadata={
            "name": "FeatureTacticTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trade_item_packing_labeling_type_code: TradeItemPackingLabelingTypeCode | None = field(
        default=None,
        metadata={
            "name": "TradeItemPackingLabelingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class EvidenceSuppliedType:
    id: Id | None = field(
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
    uri: Uri | None = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_hash: DocumentHash | None = field(
        default=None,
        metadata={
            "name": "DocumentHash",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hash_algorithm_method: HashAlgorithmMethod | None = field(
        default=None,
        metadata={
            "name": "HashAlgorithmMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expiry_date: ExpiryDate | None = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expiry_time: ExpiryTime | None = field(
        default=None,
        metadata={
            "name": "ExpiryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mime_code: MimeCode | None = field(
        default=None,
        metadata={
            "name": "MimeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    format_code: FormatCode | None = field(
        default=None,
        metadata={
            "name": "FormatCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    encoding_code: EncodingCode | None = field(
        default=None,
        metadata={
            "name": "EncodingCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    character_set_code: CharacterSetCode | None = field(
        default=None,
        metadata={
            "name": "CharacterSetCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    file_name: FileName | None = field(
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
    forecast_purpose_code: ForecastPurposeCode | None = field(
        default=None,
        metadata={
            "name": "ForecastPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_type_code: ForecastTypeCode | None = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    comparison_data_source_code: ComparisonDataSourceCode | None = field(
        default=None,
        metadata={
            "name": "ComparisonDataSourceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    data_source_code: DataSourceCode | None = field(
        default=None,
        metadata={
            "name": "DataSourceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    time_delta_days_quantity: TimeDeltaDaysQuantity | None = field(
        default=None,
        metadata={
            "name": "TimeDeltaDaysQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ForecastExceptionType:
    forecast_purpose_code: ForecastPurposeCode | None = field(
        default=None,
        metadata={
            "name": "ForecastPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_type_code: ForecastTypeCode | None = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_date: IssueDate | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issue_time: IssueTime | None = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    data_source_code: DataSourceCode | None = field(
        default=None,
        metadata={
            "name": "DataSourceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    comparison_data_code: ComparisonDataCode | None = field(
        default=None,
        metadata={
            "name": "ComparisonDataCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    comparison_forecast_issue_time: ComparisonForecastIssueTime | None = (
        field(
            default=None,
            metadata={
                "name": "ComparisonForecastIssueTime",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    comparison_forecast_issue_date: ComparisonForecastIssueDate | None = (
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
    price_amount: PriceAmount | None = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemPropertyGroupType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    importance_code: ImportanceCode | None = field(
        default=None,
        metadata={
            "name": "ImportanceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemPropertyRangeType:
    minimum_value: MinimumValue | None = field(
        default=None,
        metadata={
            "name": "MinimumValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_value: MaximumValue | None = field(
        default=None,
        metadata={
            "name": "MaximumValue",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class LanguageType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    locale_code: LocaleCode | None = field(
        default=None,
        metadata={
            "name": "LocaleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class LocationCoordinateType:
    coordinate_system_code: CoordinateSystemCode | None = field(
        default=None,
        metadata={
            "name": "CoordinateSystemCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latitude_degrees_measure: LatitudeDegreesMeasure | None = field(
        default=None,
        metadata={
            "name": "LatitudeDegreesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latitude_minutes_measure: LatitudeMinutesMeasure | None = field(
        default=None,
        metadata={
            "name": "LatitudeMinutesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latitude_direction_code: LatitudeDirectionCode | None = field(
        default=None,
        metadata={
            "name": "LatitudeDirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    longitude_degrees_measure: LongitudeDegreesMeasure | None = field(
        default=None,
        metadata={
            "name": "LongitudeDegreesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    longitude_minutes_measure: LongitudeMinutesMeasure | None = field(
        default=None,
        metadata={
            "name": "LongitudeMinutesMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    longitude_direction_code: LongitudeDirectionCode | None = field(
        default=None,
        metadata={
            "name": "LongitudeDirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    altitude_measure: AltitudeMeasure | None = field(
        default=None,
        metadata={
            "name": "AltitudeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class MeterPropertyType:
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name_code: NameCode | None = field(
        default=None,
        metadata={
            "name": "NameCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value: Value | None = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_quantity: ValueQuantity | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_reading_type: UblCommonBasicComponents21MeterReadingType | None = field(
        default=None,
        metadata={
            "name": "MeterReadingType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_reading_type_code: MeterReadingTypeCode | None = field(
        default=None,
        metadata={
            "name": "MeterReadingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    previous_meter_reading_date: PreviousMeterReadingDate | None = field(
        default=None,
        metadata={
            "name": "PreviousMeterReadingDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    previous_meter_quantity: PreviousMeterQuantity | None = field(
        default=None,
        metadata={
            "name": "PreviousMeterQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    latest_meter_reading_date: LatestMeterReadingDate | None = field(
        default=None,
        metadata={
            "name": "LatestMeterReadingDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    latest_meter_quantity: LatestMeterQuantity | None = field(
        default=None,
        metadata={
            "name": "LatestMeterQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    previous_meter_reading_method: PreviousMeterReadingMethod | None = (
        field(
            default=None,
            metadata={
                "name": "PreviousMeterReadingMethod",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    previous_meter_reading_method_code: PreviousMeterReadingMethodCode | None = field(
        default=None,
        metadata={
            "name": "PreviousMeterReadingMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_meter_reading_method: LatestMeterReadingMethod | None = field(
        default=None,
        metadata={
            "name": "LatestMeterReadingMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_meter_reading_method_code: LatestMeterReadingMethodCode | None = field(
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
    delivered_quantity: DeliveredQuantity | None = field(
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
    line_extension_amount: LineExtensionAmount | None = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_exclusive_amount: TaxExclusiveAmount | None = field(
        default=None,
        metadata={
            "name": "TaxExclusiveAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_inclusive_amount: TaxInclusiveAmount | None = field(
        default=None,
        metadata={
            "name": "TaxInclusiveAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    allowance_total_amount: AllowanceTotalAmount | None = field(
        default=None,
        metadata={
            "name": "AllowanceTotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    charge_total_amount: ChargeTotalAmount | None = field(
        default=None,
        metadata={
            "name": "ChargeTotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    prepaid_amount: PrepaidAmount | None = field(
        default=None,
        metadata={
            "name": "PrepaidAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payable_rounding_amount: PayableRoundingAmount | None = field(
        default=None,
        metadata={
            "name": "PayableRoundingAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payable_amount: PayableAmount | None = field(
        default=None,
        metadata={
            "name": "PayableAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    payable_alternative_amount: PayableAlternativeAmount | None = field(
        default=None,
        metadata={
            "name": "PayableAlternativeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class PartyIdentificationType:
    id: Id | None = field(
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
    name: Name | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    paid_amount: PaidAmount | None = field(
        default=None,
        metadata={
            "name": "PaidAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_date: ReceivedDate | None = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    paid_date: PaidDate | None = field(
        default=None,
        metadata={
            "name": "PaidDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    paid_time: PaidTime | None = field(
        default=None,
        metadata={
            "name": "PaidTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    instruction_id: InstructionId | None = field(
        default=None,
        metadata={
            "name": "InstructionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class PeriodType:
    start_date: StartDate | None = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    start_time: StartTime | None = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    end_date: EndDate | None = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    end_time: EndTime | None = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    duration_measure: DurationMeasure | None = field(
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
    attribute_id: AttributeId | None = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    position_code: PositionCode | None = field(
        default=None,
        metadata={
            "name": "PositionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    description_code: DescriptionCode | None = field(
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
    previous_cancellation_reason_code: PreviousCancellationReasonCode | None = field(
        default=None,
        metadata={
            "name": "PreviousCancellationReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    process_reason_code: ProcessReasonCode | None = field(
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
    train_id: TrainId | None = field(
        default=None,
        metadata={
            "name": "TrainID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    rail_car_id: RailCarId | None = field(
        default=None,
        metadata={
            "name": "RailCarID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class RegulationType:
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    legal_reference: LegalReference | None = field(
        default=None,
        metadata={
            "name": "LegalReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    ontology_uri: OntologyUri | None = field(
        default=None,
        metadata={
            "name": "OntologyURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class RelatedItemType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
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
    license_plate_id: LicensePlateId | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    placard_notation: PlacardNotation | None = field(
        default=None,
        metadata={
            "name": "PlacardNotation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    placard_endorsement: PlacardEndorsement | None = field(
        default=None,
        metadata={
            "name": "PlacardEndorsement",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    emergency_procedures_code: EmergencyProceduresCode | None = field(
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
    week_day_code: WeekDayCode | None = field(
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
    rate: Rate | None = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    unknown_price_indicator: UnknownPriceIndicator | None = field(
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
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subcontracting_conditions_code: SubcontractingConditionsCode | None = (
        field(
            default=None,
            metadata={
                "name": "SubcontractingConditionsCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    maximum_percent: MaximumPercent | None = field(
        default=None,
        metadata={
            "name": "MaximumPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_percent: MinimumPercent | None = field(
        default=None,
        metadata={
            "name": "MinimumPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class TemperatureType:
    attribute_id: AttributeId | None = field(
        default=None,
        metadata={
            "name": "AttributeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    measure: Measure | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    seal_issuer_type_code: SealIssuerTypeCode | None = field(
        default=None,
        metadata={
            "name": "SealIssuerTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    condition: UblCommonBasicComponents21Condition | None = field(
        default=None,
        metadata={
            "name": "Condition",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    seal_status_code: SealStatusCode | None = field(
        default=None,
        metadata={
            "name": "SealStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sealing_party_type: SealingPartyType | None = field(
        default=None,
        metadata={
            "name": "SealingPartyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class UnstructuredPriceType:
    price_amount: PriceAmount | None = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    time_amount: TimeAmount | None = field(
        default=None,
        metadata={
            "name": "TimeAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )


@dataclass(frozen=True)
class WebSiteAccessType:
    uri: Uri | None = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    password: Password | None = field(
        default=None,
        metadata={
            "name": "Password",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    login: Login | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    address_type_code: AddressTypeCode | None = field(
        default=None,
        metadata={
            "name": "AddressTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    address_format_code: AddressFormatCode | None = field(
        default=None,
        metadata={
            "name": "AddressFormatCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    postbox: Postbox | None = field(
        default=None,
        metadata={
            "name": "Postbox",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    floor: Floor | None = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    room: Room | None = field(
        default=None,
        metadata={
            "name": "Room",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    street_name: StreetName | None = field(
        default=None,
        metadata={
            "name": "StreetName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    additional_street_name: AdditionalStreetName | None = field(
        default=None,
        metadata={
            "name": "AdditionalStreetName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    block_name: BlockName | None = field(
        default=None,
        metadata={
            "name": "BlockName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    building_name: BuildingName | None = field(
        default=None,
        metadata={
            "name": "BuildingName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    building_number: BuildingNumber | None = field(
        default=None,
        metadata={
            "name": "BuildingNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    inhouse_mail: InhouseMail | None = field(
        default=None,
        metadata={
            "name": "InhouseMail",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    department: Department | None = field(
        default=None,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mark_attention: MarkAttention | None = field(
        default=None,
        metadata={
            "name": "MarkAttention",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mark_care: MarkCare | None = field(
        default=None,
        metadata={
            "name": "MarkCare",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    plot_identification: PlotIdentification | None = field(
        default=None,
        metadata={
            "name": "PlotIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    city_subdivision_name: CitySubdivisionName | None = field(
        default=None,
        metadata={
            "name": "CitySubdivisionName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    city_name: CityName | None = field(
        default=None,
        metadata={
            "name": "CityName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    postal_zone: PostalZone | None = field(
        default=None,
        metadata={
            "name": "PostalZone",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    country_subentity: CountrySubentity | None = field(
        default=None,
        metadata={
            "name": "CountrySubentity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    country_subentity_code: CountrySubentityCode | None = field(
        default=None,
        metadata={
            "name": "CountrySubentityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    region: Region | None = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    district: District | None = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    timezone_offset: TimezoneOffset | None = field(
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
    country: Country | None = field(
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
    embedded_document_binary_object: EmbeddedDocumentBinaryObject | None = (
        field(
            default=None,
            metadata={
                "name": "EmbeddedDocumentBinaryObject",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    external_reference: ExternalReference | None = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CapabilityType:
    capability_type_code: CapabilityTypeCode | None = field(
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
    value_amount: ValueAmount | None = field(
        default=None,
        metadata={
            "name": "ValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_quantity: ValueQuantity | None = field(
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
    validity_period: ValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ClassificationSchemeType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    last_revision_date: LastRevisionDate | None = field(
        default=None,
        metadata={
            "name": "LastRevisionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    last_revision_time: LastRevisionTime | None = field(
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
    name: Name | None = field(
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
    agency_id: AgencyId | None = field(
        default=None,
        metadata={
            "name": "AgencyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    agency_name: AgencyName | None = field(
        default=None,
        metadata={
            "name": "AgencyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    version_id: VersionId | None = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uri: Uri | None = field(
        default=None,
        metadata={
            "name": "URI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    scheme_uri: SchemeUri | None = field(
        default=None,
        metadata={
            "name": "SchemeURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    language_id: LanguageId | None = field(
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
    meter_number: MeterNumber | None = field(
        default=None,
        metadata={
            "name": "MeterNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_level_code: ConsumptionLevelCode | None = field(
        default=None,
        metadata={
            "name": "ConsumptionLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_level: ConsumptionLevel | None = field(
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
    period: Period | None = field(
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
    consumption_report_id: ConsumptionReportId | None = field(
        default=None,
        metadata={
            "name": "ConsumptionReportID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    consumption_type: UblCommonBasicComponents21ConsumptionType | None = (
        field(
            default=None,
            metadata={
                "name": "ConsumptionType",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    consumption_type_code: ConsumptionTypeCode | None = field(
        default=None,
        metadata={
            "name": "ConsumptionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_consumed_quantity: TotalConsumedQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    period: Period | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telephone: Telephone | None = field(
        default=None,
        metadata={
            "name": "Telephone",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telefax: Telefax | None = field(
        default=None,
        metadata={
            "name": "Telefax",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    electronic_mail: ElectronicMail | None = field(
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
    declaration_type_code: DeclarationTypeCode | None = field(
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
    comment: Comment | None = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    event_tactic_enumeration: EventTacticEnumeration | None = field(
        default=None,
        metadata={
            "name": "EventTacticEnumeration",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    period: Period | None = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class FinancialGuaranteeType:
    guarantee_type_code: GuaranteeTypeCode | None = field(
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
    liability_amount: LiabilityAmount | None = field(
        default=None,
        metadata={
            "name": "LiabilityAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount_rate: AmountRate | None = field(
        default=None,
        metadata={
            "name": "AmountRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    constitution_period: ConstitutionPeriod | None = field(
        default=None,
        metadata={
            "name": "ConstitutionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class HazardousGoodsTransitType:
    transport_emergency_card_code: TransportEmergencyCardCode | None = (
        field(
            default=None,
            metadata={
                "name": "TransportEmergencyCardCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    packing_criteria_code: PackingCriteriaCode | None = field(
        default=None,
        metadata={
            "name": "PackingCriteriaCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_regulation_code: HazardousRegulationCode | None = field(
        default=None,
        metadata={
            "name": "HazardousRegulationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    inhalation_toxicity_zone_code: InhalationToxicityZoneCode | None = (
        field(
            default=None,
            metadata={
                "name": "InhalationToxicityZoneCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    transport_authorization_code: TransportAuthorizationCode | None = field(
        default=None,
        metadata={
            "name": "TransportAuthorizationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_temperature: MaximumTemperature | None = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    minimum_temperature: MinimumTemperature | None = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemPropertyType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    name_code: NameCode | None = field(
        default=None,
        metadata={
            "name": "NameCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    test_method: TestMethod | None = field(
        default=None,
        metadata={
            "name": "TestMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value: Value | None = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_quantity: ValueQuantity | None = field(
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
    importance_code: ImportanceCode | None = field(
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
    usability_period: UsabilityPeriod | None = field(
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
    range_dimension: RangeDimension | None = field(
        default=None,
        metadata={
            "name": "RangeDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_property_range: ItemPropertyRange | None = field(
        default=None,
        metadata={
            "name": "ItemPropertyRange",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class MeterType:
    meter_number: MeterNumber | None = field(
        default=None,
        metadata={
            "name": "MeterNumber",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_name: MeterName | None = field(
        default=None,
        metadata={
            "name": "MeterName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_constant: MeterConstant | None = field(
        default=None,
        metadata={
            "name": "MeterConstant",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    meter_constant_code: MeterConstantCode | None = field(
        default=None,
        metadata={
            "name": "MeterConstantCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_delivered_quantity: TotalDeliveredQuantity | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    status_code: StatusCode | None = field(
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
    previous_price_list: PreviousPriceList | None = field(
        default=None,
        metadata={
            "name": "PreviousPriceList",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RenewalType:
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    period: Period | None = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RetailPlannedImpactType:
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_purpose_code: ForecastPurposeCode | None = field(
        default=None,
        metadata={
            "name": "ForecastPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_type_code: ForecastTypeCode | None = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    period: Period | None = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class StatusType:
    condition_code: ConditionCode | None = field(
        default=None,
        metadata={
            "name": "ConditionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reference_date: ReferenceDate | None = field(
        default=None,
        metadata={
            "name": "ReferenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reference_time: ReferenceTime | None = field(
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
    status_reason_code: StatusReasonCode | None = field(
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
    sequence_id: SequenceId | None = field(
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
    indication_indicator: IndicationIndicator | None = field(
        default=None,
        metadata={
            "name": "IndicationIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    percent: Percent | None = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reliability_percent: ReliabilityPercent | None = field(
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
    location_id: LocationId | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    budget_year_numeric: BudgetYearNumeric | None = field(
        default=None,
        metadata={
            "name": "BudgetYearNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_classification_scheme: RequiredClassificationScheme | None = (
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
    id: Id | None = field(
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
    subscriber_id: SubscriberId | None = field(
        default=None,
        metadata={
            "name": "SubscriberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_type: SubscriberType | None = field(
        default=None,
        metadata={
            "name": "SubscriberType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_type_code: SubscriberTypeCode | None = field(
        default=None,
        metadata={
            "name": "SubscriberTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_delivered_quantity: TotalDeliveredQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalDeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    address: Address | None = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    web_site_access: WebSiteAccess | None = field(
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
    minimum_number_numeric: MinimumNumberNumeric | None = field(
        default=None,
        metadata={
            "name": "MinimumNumberNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_number_numeric: MaximumNumberNumeric | None = field(
        default=None,
        metadata={
            "name": "MaximumNumberNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    option_validity_period: OptionValidityPeriod | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    corporate_registration_type_code: CorporateRegistrationTypeCode | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    copy_indicator: CopyIndicator | None = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: IssueDate | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: IssueTime | None = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_type_code: DocumentTypeCode | None = field(
        default=None,
        metadata={
            "name": "DocumentTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_type: DocumentType | None = field(
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
    language_id: LanguageId | None = field(
        default=None,
        metadata={
            "name": "LanguageID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    locale_code: LocaleCode | None = field(
        default=None,
        metadata={
            "name": "LocaleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    version_id: VersionId | None = field(
        default=None,
        metadata={
            "name": "VersionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_status_code: DocumentStatusCode | None = field(
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
    attachment: Attachment | None = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    validity_period: ValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    issuer_party: IssuerParty | None = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    result_of_verification: ResultOfVerification | None = field(
        default=None,
        metadata={
            "name": "ResultOfVerification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class FinancialInstitutionType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    address: Address | None = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class LocationType:
    id: Id | None = field(
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
    country_subentity: CountrySubentity | None = field(
        default=None,
        metadata={
            "name": "CountrySubentity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    country_subentity_code: CountrySubentityCode | None = field(
        default=None,
        metadata={
            "name": "CountrySubentityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    location_type_code: LocationTypeCode | None = field(
        default=None,
        metadata={
            "name": "LocationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    information_uri: InformationUri | None = field(
        default=None,
        metadata={
            "name": "InformationURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
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
    address: Address | None = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    subsidiary_location: tuple[SubsidiaryLocation, ...] = field(
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
    lot_number_id: LotNumberId | None = field(
        default=None,
        metadata={
            "name": "LotNumberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expiry_date: ExpiryDate | None = field(
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
    reference_id: ReferenceId | None = field(
        default=None,
        metadata={
            "name": "ReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    response_code: ResponseCode | None = field(
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
    effective_date: EffectiveDate | None = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    effective_time: EffectiveTime | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_type_code: TaxTypeCode | None = field(
        default=None,
        metadata={
            "name": "TaxTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    currency_code: CurrencyCode | None = field(
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
    reference: Reference | None = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    applicable_address: ApplicableAddress | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    financial_institution: FinancialInstitution | None = field(
        default=None,
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    address: Address | None = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class BudgetAccountLineType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_amount: TotalAmount | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    consumption_type: UblCommonBasicComponents21ConsumptionType | None = (
        field(
            default=None,
            metadata={
                "name": "ConsumptionType",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    consumption_type_code: ConsumptionTypeCode | None = field(
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
    total_consumed_quantity: TotalConsumedQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    basic_consumed_quantity: BasicConsumedQuantity | None = field(
        default=None,
        metadata={
            "name": "BasicConsumedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    resident_occupants_numeric: ResidentOccupantsNumeric | None = field(
        default=None,
        metadata={
            "name": "ResidentOccupantsNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumers_energy_level_code: ConsumersEnergyLevelCode | None = field(
        default=None,
        metadata={
            "name": "ConsumersEnergyLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumers_energy_level: ConsumersEnergyLevel | None = field(
        default=None,
        metadata={
            "name": "ConsumersEnergyLevel",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    residence_type: ResidenceType | None = field(
        default=None,
        metadata={
            "name": "ResidenceType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    residence_type_code: ResidenceTypeCode | None = field(
        default=None,
        metadata={
            "name": "ResidenceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    heating_type: HeatingType | None = field(
        default=None,
        metadata={
            "name": "HeatingType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    heating_type_code: HeatingTypeCode | None = field(
        default=None,
        metadata={
            "name": "HeatingTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    period: Period | None = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    guidance_document_reference: GuidanceDocumentReference | None = field(
        default=None,
        metadata={
            "name": "GuidanceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: DocumentReference | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: IssueDate | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: IssueTime | None = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nomination_date: NominationDate | None = field(
        default=None,
        metadata={
            "name": "NominationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nomination_time: NominationTime | None = field(
        default=None,
        metadata={
            "name": "NominationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract_type_code: ContractTypeCode | None = field(
        default=None,
        metadata={
            "name": "ContractTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract_type: UblCommonBasicComponents21ContractType | None = field(
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
    version_id: VersionId | None = field(
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
    validity_period: ValidityPeriod | None = field(
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
    nomination_period: NominationPeriod | None = field(
        default=None,
        metadata={
            "name": "NominationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contractual_delivery: ContractualDelivery | None = field(
        default=None,
        metadata={
            "name": "ContractualDelivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EmissionCalculationMethodType:
    calculation_method_code: CalculationMethodCode | None = field(
        default=None,
        metadata={
            "name": "CalculationMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fullness_indication_code: FullnessIndicationCode | None = field(
        default=None,
        metadata={
            "name": "FullnessIndicationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    measurement_from_location: MeasurementFromLocation | None = field(
        default=None,
        metadata={
            "name": "MeasurementFromLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    measurement_to_location: MeasurementToLocation | None = field(
        default=None,
        metadata={
            "name": "MeasurementToLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EnergyTaxReportType:
    tax_energy_amount: TaxEnergyAmount | None = field(
        default=None,
        metadata={
            "name": "TaxEnergyAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_energy_on_account_amount: TaxEnergyOnAccountAmount | None = field(
        default=None,
        metadata={
            "name": "TaxEnergyOnAccountAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_energy_balance_amount: TaxEnergyBalanceAmount | None = field(
        default=None,
        metadata={
            "name": "TaxEnergyBalanceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_scheme: TaxScheme | None = field(
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
    identification_id: IdentificationId | None = field(
        default=None,
        metadata={
            "name": "IdentificationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    occurrence_date: OccurrenceDate | None = field(
        default=None,
        metadata={
            "name": "OccurrenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    occurrence_time: OccurrenceTime | None = field(
        default=None,
        metadata={
            "name": "OccurrenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    type_code: TypeCode | None = field(
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
    completion_indicator: CompletionIndicator | None = field(
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
    occurence_location: OccurenceLocation | None = field(
        default=None,
        metadata={
            "name": "OccurenceLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemInstanceType:
    product_trace_id: ProductTraceId | None = field(
        default=None,
        metadata={
            "name": "ProductTraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    manufacture_date: ManufactureDate | None = field(
        default=None,
        metadata={
            "name": "ManufactureDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    manufacture_time: ManufactureTime | None = field(
        default=None,
        metadata={
            "name": "ManufactureTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    best_before_date: BestBeforeDate | None = field(
        default=None,
        metadata={
            "name": "BestBeforeDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_id: RegistrationId | None = field(
        default=None,
        metadata={
            "name": "RegistrationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    serial_id: SerialId | None = field(
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
    lot_identification: LotIdentification | None = field(
        default=None,
        metadata={
            "name": "LotIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class LineReferenceType:
    line_id: LineId | None = field(
        default=None,
        metadata={
            "name": "LineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_status_code: LineStatusCode | None = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_reference: DocumentReference | None = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class MaritimeTransportType:
    vessel_id: VesselId | None = field(
        default=None,
        metadata={
            "name": "VesselID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    vessel_name: VesselName | None = field(
        default=None,
        metadata={
            "name": "VesselName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    radio_call_sign_id: RadioCallSignId | None = field(
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
    gross_tonnage_measure: GrossTonnageMeasure | None = field(
        default=None,
        metadata={
            "name": "GrossTonnageMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_tonnage_measure: NetTonnageMeasure | None = field(
        default=None,
        metadata={
            "name": "NetTonnageMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registry_certificate_document_reference: RegistryCertificateDocumentReference | None = field(
        default=None,
        metadata={
            "name": "RegistryCertificateDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    registry_port_location: RegistryPortLocation | None = field(
        default=None,
        metadata={
            "name": "RegistryPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class OrderReferenceType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    sales_order_id: SalesOrderId | None = field(
        default=None,
        metadata={
            "name": "SalesOrderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    copy_indicator: CopyIndicator | None = field(
        default=None,
        metadata={
            "name": "CopyIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: IssueDate | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: IssueTime | None = field(
        default=None,
        metadata={
            "name": "IssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customer_reference: CustomerReference | None = field(
        default=None,
        metadata={
            "name": "CustomerReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_type_code: OrderTypeCode | None = field(
        default=None,
        metadata={
            "name": "OrderTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_reference: DocumentReference | None = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PartyTaxSchemeType:
    registration_name: RegistrationName | None = field(
        default=None,
        metadata={
            "name": "RegistrationName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_id: CompanyId | None = field(
        default=None,
        metadata={
            "name": "CompanyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_level_code: TaxLevelCode | None = field(
        default=None,
        metadata={
            "name": "TaxLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exemption_reason_code: ExemptionReasonCode | None = field(
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
    registration_address: RegistrationAddress | None = field(
        default=None,
        metadata={
            "name": "RegistrationAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tax_scheme: TaxScheme | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    percent: Percent | None = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    base_unit_measure: BaseUnitMeasure | None = field(
        default=None,
        metadata={
            "name": "BaseUnitMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    per_unit_amount: PerUnitAmount | None = field(
        default=None,
        metadata={
            "name": "PerUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_exemption_reason_code: TaxExemptionReasonCode | None = field(
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
    tier_range: TierRange | None = field(
        default=None,
        metadata={
            "name": "TierRange",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tier_rate_percent: TierRatePercent | None = field(
        default=None,
        metadata={
            "name": "TierRatePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_scheme: TaxScheme | None = field(
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
    name: Name | None = field(
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
    template_document_reference: TemplateDocumentReference | None = field(
        default=None,
        metadata={
            "name": "TemplateDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransactionConditionsType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    action_code: ActionCode | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    work_phase_code: WorkPhaseCode | None = field(
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
    progress_percent: ProgressPercent | None = field(
        default=None,
        metadata={
            "name": "ProgressPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    start_date: StartDate | None = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    end_date: EndDate | None = field(
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
    percent: Percent | None = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    location_address: LocationAddress | None = field(
        default=None,
        metadata={
            "name": "LocationAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    dependent_line_reference: DependentLineReference | None = field(
        default=None,
        metadata={
            "name": "DependentLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DutyType:
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    duty: UblCommonBasicComponents21Duty | None = field(
        default=None,
        metadata={
            "name": "Duty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    duty_code: DutyCode | None = field(
        default=None,
        metadata={
            "name": "DutyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_category: TaxCategory | None = field(
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
    environmental_emission_type_code: EnvironmentalEmissionTypeCode | None = field(
        default=None,
        metadata={
            "name": "EnvironmentalEmissionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    value_measure: ValueMeasure | None = field(
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
    source_currency_code: SourceCurrencyCode | None = field(
        default=None,
        metadata={
            "name": "SourceCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    source_currency_base_rate: SourceCurrencyBaseRate | None = field(
        default=None,
        metadata={
            "name": "SourceCurrencyBaseRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    target_currency_code: TargetCurrencyCode | None = field(
        default=None,
        metadata={
            "name": "TargetCurrencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    target_currency_base_rate: TargetCurrencyBaseRate | None = field(
        default=None,
        metadata={
            "name": "TargetCurrencyBaseRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exchange_market_id: ExchangeMarketId | None = field(
        default=None,
        metadata={
            "name": "ExchangeMarketID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    calculation_rate: CalculationRate | None = field(
        default=None,
        metadata={
            "name": "CalculationRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mathematic_operator_code: MathematicOperatorCode | None = field(
        default=None,
        metadata={
            "name": "MathematicOperatorCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    date: Date | None = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    foreign_exchange_contract: ForeignExchangeContract | None = field(
        default=None,
        metadata={
            "name": "ForeignExchangeContract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class FinancialAccountType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    alias_name: AliasName | None = field(
        default=None,
        metadata={
            "name": "AliasName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    account_type_code: AccountTypeCode | None = field(
        default=None,
        metadata={
            "name": "AccountTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    account_format_code: AccountFormatCode | None = field(
        default=None,
        metadata={
            "name": "AccountFormatCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    currency_code: CurrencyCode | None = field(
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
    financial_institution_branch: FinancialInstitutionBranch | None = field(
        default=None,
        metadata={
            "name": "FinancialInstitutionBranch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    country: Country | None = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class FrameworkAgreementType:
    expected_operator_quantity: ExpectedOperatorQuantity | None = field(
        default=None,
        metadata={
            "name": "ExpectedOperatorQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_operator_quantity: MaximumOperatorQuantity | None = field(
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
    duration_period: DurationPeriod | None = field(
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
    line_reference: LineReference | None = field(
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
    line_id: LineId | None = field(
        default=None,
        metadata={
            "name": "LineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    sales_order_line_id: SalesOrderLineId | None = field(
        default=None,
        metadata={
            "name": "SalesOrderLineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_status_code: LineStatusCode | None = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_reference: OrderReference | None = field(
        default=None,
        metadata={
            "name": "OrderReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ProjectReferenceType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: IssueDate | None = field(
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
    estimated_overall_contract_amount: EstimatedOverallContractAmount | None = field(
        default=None,
        metadata={
            "name": "EstimatedOverallContractAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_amount: TotalAmount | None = field(
        default=None,
        metadata={
            "name": "TotalAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_included_indicator: TaxIncludedIndicator | None = field(
        default=None,
        metadata={
            "name": "TaxIncludedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_amount: MinimumAmount | None = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_amount: MaximumAmount | None = field(
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
    average_subsequent_contract_amount: AverageSubsequentContractAmount | None = field(
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
    taxable_amount: TaxableAmount | None = field(
        default=None,
        metadata={
            "name": "TaxableAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_amount: TaxAmount | None = field(
        default=None,
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    calculation_sequence_numeric: CalculationSequenceNumeric | None = field(
        default=None,
        metadata={
            "name": "CalculationSequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transaction_currency_tax_amount: TransactionCurrencyTaxAmount | None = (
        field(
            default=None,
            metadata={
                "name": "TransactionCurrencyTaxAmount",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    percent: Percent | None = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    base_unit_measure: BaseUnitMeasure | None = field(
        default=None,
        metadata={
            "name": "BaseUnitMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    per_unit_amount: PerUnitAmount | None = field(
        default=None,
        metadata={
            "name": "PerUnitAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tier_range: TierRange | None = field(
        default=None,
        metadata={
            "name": "TierRange",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tier_rate_percent: TierRatePercent | None = field(
        default=None,
        metadata={
            "name": "TierRatePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_category: TaxCategory | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    subscriber_id: SubscriberId | None = field(
        default=None,
        metadata={
            "name": "SubscriberID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_type: SubscriberType | None = field(
        default=None,
        metadata={
            "name": "SubscriberType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_type_code: SubscriberTypeCode | None = field(
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
    pack_quantity: PackQuantity | None = field(
        default=None,
        metadata={
            "name": "PackQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pack_size_numeric: PackSizeNumeric | None = field(
        default=None,
        metadata={
            "name": "PackSizeNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consumption_type: UblCommonBasicComponents21ConsumptionType | None = (
        field(
            default=None,
            metadata={
                "name": "ConsumptionType",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    consumption_type_code: ConsumptionTypeCode | None = field(
        default=None,
        metadata={
            "name": "ConsumptionTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    current_charge_type: CurrentChargeType | None = field(
        default=None,
        metadata={
            "name": "CurrentChargeType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    current_charge_type_code: CurrentChargeTypeCode | None = field(
        default=None,
        metadata={
            "name": "CurrentChargeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    one_time_charge_type: OneTimeChargeType | None = field(
        default=None,
        metadata={
            "name": "OneTimeChargeType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    one_time_charge_type_code: OneTimeChargeTypeCode | None = field(
        default=None,
        metadata={
            "name": "OneTimeChargeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_category: TaxCategory | None = field(
        default=None,
        metadata={
            "name": "TaxCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract: Contract | None = field(
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
    id: Id | None = field(
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
    prepaid_payment_reference_id: PrepaidPaymentReferenceId | None = field(
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
    reference_event_code: ReferenceEventCode | None = field(
        default=None,
        metadata={
            "name": "ReferenceEventCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    settlement_discount_percent: SettlementDiscountPercent | None = field(
        default=None,
        metadata={
            "name": "SettlementDiscountPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    penalty_surcharge_percent: PenaltySurchargePercent | None = field(
        default=None,
        metadata={
            "name": "PenaltySurchargePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_percent: PaymentPercent | None = field(
        default=None,
        metadata={
            "name": "PaymentPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    settlement_discount_amount: SettlementDiscountAmount | None = field(
        default=None,
        metadata={
            "name": "SettlementDiscountAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    penalty_amount: PenaltyAmount | None = field(
        default=None,
        metadata={
            "name": "PenaltyAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_terms_details_uri: PaymentTermsDetailsUri | None = field(
        default=None,
        metadata={
            "name": "PaymentTermsDetailsURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_due_date: PaymentDueDate | None = field(
        default=None,
        metadata={
            "name": "PaymentDueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    installment_due_date: InstallmentDueDate | None = field(
        default=None,
        metadata={
            "name": "InstallmentDueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoicing_party_reference: InvoicingPartyReference | None = field(
        default=None,
        metadata={
            "name": "InvoicingPartyReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    settlement_period: SettlementPeriod | None = field(
        default=None,
        metadata={
            "name": "SettlementPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    penalty_period: PenaltyPeriod | None = field(
        default=None,
        metadata={
            "name": "PenaltyPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exchange_rate: ExchangeRate | None = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    validity_period: ValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PersonType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    first_name: FirstName | None = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    family_name: FamilyName | None = field(
        default=None,
        metadata={
            "name": "FamilyName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    title: Title | None = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    middle_name: MiddleName | None = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    other_name: OtherName | None = field(
        default=None,
        metadata={
            "name": "OtherName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name_suffix: NameSuffix | None = field(
        default=None,
        metadata={
            "name": "NameSuffix",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    job_title: JobTitle | None = field(
        default=None,
        metadata={
            "name": "JobTitle",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nationality_id: NationalityId | None = field(
        default=None,
        metadata={
            "name": "NationalityID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gender_code: GenderCode | None = field(
        default=None,
        metadata={
            "name": "GenderCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    birth_date: BirthDate | None = field(
        default=None,
        metadata={
            "name": "BirthDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    birthplace_name: BirthplaceName | None = field(
        default=None,
        metadata={
            "name": "BirthplaceName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    organization_department: OrganizationDepartment | None = field(
        default=None,
        metadata={
            "name": "OrganizationDepartment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contact: Contact | None = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    financial_account: FinancialAccount | None = field(
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
    residence_address: ResidenceAddress | None = field(
        default=None,
        metadata={
            "name": "ResidenceAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TaxTotalType:
    tax_amount: TaxAmount | None = field(
        default=None,
        metadata={
            "name": "TaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    rounding_amount: RoundingAmount | None = field(
        default=None,
        metadata={
            "name": "RoundingAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_evidence_indicator: TaxEvidenceIndicator | None = field(
        default=None,
        metadata={
            "name": "TaxEvidenceIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_included_indicator: TaxIncludedIndicator | None = field(
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
    weighting_algorithm_code: WeightingAlgorithmCode | None = field(
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
    prize_indicator: PrizeIndicator | None = field(
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
    followup_contract_indicator: FollowupContractIndicator | None = field(
        default=None,
        metadata={
            "name": "FollowupContractIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    binding_on_buyer_indicator: BindingOnBuyerIndicator | None = field(
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
    estimated_consumed_quantity: EstimatedConsumedQuantity | None = field(
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
    mark_care_indicator: MarkCareIndicator | None = field(
        default=None,
        metadata={
            "name": "MarkCareIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mark_attention_indicator: MarkAttentionIndicator | None = field(
        default=None,
        metadata={
            "name": "MarkAttentionIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    website_uri: WebsiteUri | None = field(
        default=None,
        metadata={
            "name": "WebsiteURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    logo_reference_id: LogoReferenceId | None = field(
        default=None,
        metadata={
            "name": "LogoReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    endpoint_id: EndpointId | None = field(
        default=None,
        metadata={
            "name": "EndpointID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    industry_classification_code: IndustryClassificationCode | None = field(
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
    language: Language | None = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    postal_address: PostalAddress | None = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    physical_location: PhysicalLocation | None = field(
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
    party_legal_entity: tuple[PartyLegalEntity, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PartyLegalEntity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contact: Contact | None = field(
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
    agent_party: AgentParty | None = field(
        default=None,
        metadata={
            "name": "AgentParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    service_provider_party: tuple[ServiceProviderParty, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ServiceProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    power_of_attorney: tuple[PowerOfAttorney, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "PowerOfAttorney",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    financial_account: FinancialAccount | None = field(
        default=None,
        metadata={
            "name": "FinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PriceExtensionType:
    amount: Amount | None = field(
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
    presentation_period: PresentationPeriod | None = field(
        default=None,
        metadata={
            "name": "PresentationPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    appeal_information_party: AppealInformationParty | None = field(
        default=None,
        metadata={
            "name": "AppealInformationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    appeal_receiver_party: AppealReceiverParty | None = field(
        default=None,
        metadata={
            "name": "AppealReceiverParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    mediation_party: MediationParty | None = field(
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

    buyer_profile_uri: BuyerProfileUri | None = field(
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
    party: Party | None = field(
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
    customer_assigned_account_id: CustomerAssignedAccountId | None = field(
        default=None,
        metadata={
            "name": "CustomerAssignedAccountID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    supplier_assigned_account_id: SupplierAssignedAccountId | None = field(
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
    party: Party | None = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_contact: DeliveryContact | None = field(
        default=None,
        metadata={
            "name": "DeliveryContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_contact: AccountingContact | None = field(
        default=None,
        metadata={
            "name": "AccountingContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    buyer_contact: BuyerContact | None = field(
        default=None,
        metadata={
            "name": "BuyerContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CustomsDeclarationType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    issuer_party: IssuerParty | None = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DespatchType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    requested_despatch_date: RequestedDespatchDate | None = field(
        default=None,
        metadata={
            "name": "RequestedDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    requested_despatch_time: RequestedDespatchTime | None = field(
        default=None,
        metadata={
            "name": "RequestedDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_despatch_date: EstimatedDespatchDate | None = field(
        default=None,
        metadata={
            "name": "EstimatedDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_despatch_time: EstimatedDespatchTime | None = field(
        default=None,
        metadata={
            "name": "EstimatedDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_despatch_date: ActualDespatchDate | None = field(
        default=None,
        metadata={
            "name": "ActualDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_despatch_time: ActualDespatchTime | None = field(
        default=None,
        metadata={
            "name": "ActualDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    guaranteed_despatch_date: GuaranteedDespatchDate | None = field(
        default=None,
        metadata={
            "name": "GuaranteedDespatchDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    guaranteed_despatch_time: GuaranteedDespatchTime | None = field(
        default=None,
        metadata={
            "name": "GuaranteedDespatchTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    release_id: ReleaseId | None = field(
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
    despatch_address: DespatchAddress | None = field(
        default=None,
        metadata={
            "name": "DespatchAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_location: DespatchLocation | None = field(
        default=None,
        metadata={
            "name": "DespatchLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_party: DespatchParty | None = field(
        default=None,
        metadata={
            "name": "DespatchParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    carrier_party: CarrierParty | None = field(
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
    contact: Contact | None = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_despatch_period: EstimatedDespatchPeriod | None = field(
        default=None,
        metadata={
            "name": "EstimatedDespatchPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_despatch_period: RequestedDespatchPeriod | None = field(
        default=None,
        metadata={
            "name": "RequestedDespatchPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DocumentDistributionType:
    print_qualifier: PrintQualifier | None = field(
        default=None,
        metadata={
            "name": "PrintQualifier",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    maximum_copies_numeric: MaximumCopiesNumeric | None = field(
        default=None,
        metadata={
            "name": "MaximumCopiesNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    party: Party | None = field(
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
    response: Response | None = field(
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
    issuer_party: IssuerParty | None = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    recipient_party: RecipientParty | None = field(
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
    expected_quantity: ExpectedQuantity | None = field(
        default=None,
        metadata={
            "name": "ExpectedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: MaximumQuantity | None = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: MinimumQuantity | None = field(
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
    role_code: RoleCode | None = field(
        default=None,
        metadata={
            "name": "RoleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    sequence_numeric: SequenceNumeric | None = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    party: Party | None = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    signatory_contact: SignatoryContact | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    evidence_type_code: EvidenceTypeCode | None = field(
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
    evidence_issuing_party: EvidenceIssuingParty | None = field(
        default=None,
        metadata={
            "name": "EvidenceIssuingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_reference: DocumentReference | None = field(
        default=None,
        metadata={
            "name": "DocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    language: Language | None = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class HazardousItemType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    placard_notation: PlacardNotation | None = field(
        default=None,
        metadata={
            "name": "PlacardNotation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    placard_endorsement: PlacardEndorsement | None = field(
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
    undgcode: Undgcode | None = field(
        default=None,
        metadata={
            "name": "UNDGCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    emergency_procedures_code: EmergencyProceduresCode | None = field(
        default=None,
        metadata={
            "name": "EmergencyProceduresCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    medical_first_aid_guide_code: MedicalFirstAidGuideCode | None = field(
        default=None,
        metadata={
            "name": "MedicalFirstAidGuideCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    technical_name: TechnicalName | None = field(
        default=None,
        metadata={
            "name": "TechnicalName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    category_name: CategoryName | None = field(
        default=None,
        metadata={
            "name": "CategoryName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_category_code: HazardousCategoryCode | None = field(
        default=None,
        metadata={
            "name": "HazardousCategoryCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    upper_orange_hazard_placard_id: UpperOrangeHazardPlacardId | None = (
        field(
            default=None,
            metadata={
                "name": "UpperOrangeHazardPlacardID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    lower_orange_hazard_placard_id: LowerOrangeHazardPlacardId | None = (
        field(
            default=None,
            metadata={
                "name": "LowerOrangeHazardPlacardID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    marking_id: MarkingId | None = field(
        default=None,
        metadata={
            "name": "MarkingID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazard_class_id: HazardClassId | None = field(
        default=None,
        metadata={
            "name": "HazardClassID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_weight_measure: NetWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_volume_measure: NetVolumeMeasure | None = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contact_party: ContactParty | None = field(
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
    emergency_temperature: EmergencyTemperature | None = field(
        default=None,
        metadata={
            "name": "EmergencyTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    flashpoint_temperature: FlashpointTemperature | None = field(
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
    immobilization_certificate_id: ImmobilizationCertificateId | None = (
        field(
            default=None,
            metadata={
                "name": "ImmobilizationCertificateID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    security_id: SecurityId | None = field(
        default=None,
        metadata={
            "name": "SecurityID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: IssueDate | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    face_value_amount: FaceValueAmount | None = field(
        default=None,
        metadata={
            "name": "FaceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    market_value_amount: MarketValueAmount | None = field(
        default=None,
        metadata={
            "name": "MarketValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    shares_number_quantity: SharesNumberQuantity | None = field(
        default=None,
        metadata={
            "name": "SharesNumberQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issuer_party: IssuerParty | None = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemIdentificationType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    extended_id: ExtendedId | None = field(
        default=None,
        metadata={
            "name": "ExtendedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    barcode_symbology_id: BarcodeSymbologyId | None = field(
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
    issuer_party: IssuerParty | None = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class NotificationRequirementType:
    notification_type_code: NotificationTypeCode | None = field(
        default=None,
        metadata={
            "name": "NotificationTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    post_event_notification_duration_measure: PostEventNotificationDurationMeasure | None = field(
        default=None,
        metadata={
            "name": "PostEventNotificationDurationMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pre_event_notification_duration_measure: PreEventNotificationDurationMeasure | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    mandate_type_code: MandateTypeCode | None = field(
        default=None,
        metadata={
            "name": "MandateTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_payment_instructions_numeric: MaximumPaymentInstructionsNumeric | None = field(
        default=None,
        metadata={
            "name": "MaximumPaymentInstructionsNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_paid_amount: MaximumPaidAmount | None = field(
        default=None,
        metadata={
            "name": "MaximumPaidAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    signature_id: SignatureId | None = field(
        default=None,
        metadata={
            "name": "SignatureID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payer_party: PayerParty | None = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payer_financial_account: PayerFinancialAccount | None = field(
        default=None,
        metadata={
            "name": "PayerFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    validity_period: ValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_reversal_period: PaymentReversalPeriod | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_pickup_date: ActualPickupDate | None = field(
        default=None,
        metadata={
            "name": "ActualPickupDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_pickup_time: ActualPickupTime | None = field(
        default=None,
        metadata={
            "name": "ActualPickupTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    earliest_pickup_date: EarliestPickupDate | None = field(
        default=None,
        metadata={
            "name": "EarliestPickupDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    earliest_pickup_time: EarliestPickupTime | None = field(
        default=None,
        metadata={
            "name": "EarliestPickupTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_pickup_date: LatestPickupDate | None = field(
        default=None,
        metadata={
            "name": "LatestPickupDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_pickup_time: LatestPickupTime | None = field(
        default=None,
        metadata={
            "name": "LatestPickupTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pickup_location: PickupLocation | None = field(
        default=None,
        metadata={
            "name": "PickupLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pickup_party: PickupParty | None = field(
        default=None,
        metadata={
            "name": "PickupParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PowerOfAttorneyType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_date: IssueDate | None = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    issue_time: IssueTime | None = field(
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
    notary_party: NotaryParty | None = field(
        default=None,
        metadata={
            "name": "NotaryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    agent_party: AgentParty | None = field(
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
    validator_id: ValidatorId | None = field(
        default=None,
        metadata={
            "name": "ValidatorID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validation_result_code: ValidationResultCode | None = field(
        default=None,
        metadata={
            "name": "ValidationResultCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validation_date: ValidationDate | None = field(
        default=None,
        metadata={
            "name": "ValidationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validation_time: ValidationTime | None = field(
        default=None,
        metadata={
            "name": "ValidationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validate_process: ValidateProcess | None = field(
        default=None,
        metadata={
            "name": "ValidateProcess",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validate_tool: ValidateTool | None = field(
        default=None,
        metadata={
            "name": "ValidateTool",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validate_tool_version: ValidateToolVersion | None = field(
        default=None,
        metadata={
            "name": "ValidateToolVersion",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    signatory_party: SignatoryParty | None = field(
        default=None,
        metadata={
            "name": "SignatoryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ServiceProviderPartyType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    service_type_code: ServiceTypeCode | None = field(
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
    party: Party | None = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    seller_contact: SellerContact | None = field(
        default=None,
        metadata={
            "name": "SellerContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ShareholderPartyType:
    partecipation_percent: PartecipationPercent | None = field(
        default=None,
        metadata={
            "name": "PartecipationPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party: Party | None = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class SignatureType:
    id: Id | None = field(
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
    validation_date: ValidationDate | None = field(
        default=None,
        metadata={
            "name": "ValidationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validation_time: ValidationTime | None = field(
        default=None,
        metadata={
            "name": "ValidationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    validator_id: ValidatorId | None = field(
        default=None,
        metadata={
            "name": "ValidatorID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    canonicalization_method: CanonicalizationMethod | None = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    signature_method: SignatureMethod | None = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    signatory_party: SignatoryParty | None = field(
        default=None,
        metadata={
            "name": "SignatoryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    digital_signature_attachment: DigitalSignatureAttachment | None = field(
        default=None,
        metadata={
            "name": "DigitalSignatureAttachment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    original_document_reference: OriginalDocumentReference | None = field(
        default=None,
        metadata={
            "name": "OriginalDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class SupplierPartyType:
    customer_assigned_account_id: CustomerAssignedAccountId | None = field(
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
    data_sending_capability: DataSendingCapability | None = field(
        default=None,
        metadata={
            "name": "DataSendingCapability",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party: Party | None = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch_contact: DespatchContact | None = field(
        default=None,
        metadata={
            "name": "DespatchContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_contact: AccountingContact | None = field(
        default=None,
        metadata={
            "name": "AccountingContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_contact: SellerContact | None = field(
        default=None,
        metadata={
            "name": "SellerContact",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TradeFinancingType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    financing_instrument_code: FinancingInstrumentCode | None = field(
        default=None,
        metadata={
            "name": "FinancingInstrumentCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract_document_reference: ContractDocumentReference | None = field(
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
    financing_party: FinancingParty | None = field(
        default=None,
        metadata={
            "name": "FinancingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    financing_financial_account: FinancingFinancialAccount | None = field(
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
    journey_id: JourneyId | None = field(
        default=None,
        metadata={
            "name": "JourneyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_nationality_id: RegistrationNationalityId | None = field(
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
    direction_code: DirectionCode | None = field(
        default=None,
        metadata={
            "name": "DirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_means_type_code: TransportMeansTypeCode | None = field(
        default=None,
        metadata={
            "name": "TransportMeansTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trade_service_code: TradeServiceCode | None = field(
        default=None,
        metadata={
            "name": "TradeServiceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    stowage: Stowage | None = field(
        default=None,
        metadata={
            "name": "Stowage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    air_transport: AirTransport | None = field(
        default=None,
        metadata={
            "name": "AirTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    road_transport: RoadTransport | None = field(
        default=None,
        metadata={
            "name": "RoadTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    rail_transport: RailTransport | None = field(
        default=None,
        metadata={
            "name": "RailTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maritime_transport: MaritimeTransport | None = field(
        default=None,
        metadata={
            "name": "MaritimeTransport",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    owner_party: OwnerParty | None = field(
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
    rank: Rank | None = field(
        default=None,
        metadata={
            "name": "Rank",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party: Party | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    certificate_type_code: CertificateTypeCode | None = field(
        default=None,
        metadata={
            "name": "CertificateTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    certificate_type: UblCommonBasicComponents21CertificateType | None = (
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
    issuer_party: IssuerParty | None = field(
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
    annual_average_amount: AnnualAverageAmount | None = field(
        default=None,
        metadata={
            "name": "AnnualAverageAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_task_amount: TotalTaskAmount | None = field(
        default=None,
        metadata={
            "name": "TotalTaskAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    party_capacity_amount: PartyCapacityAmount | None = field(
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
    period: Period | None = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    recipient_customer_party: RecipientCustomerParty | None = field(
        default=None,
        metadata={
            "name": "RecipientCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EndorsementType:
    document_id: DocumentId | None = field(
        default=None,
        metadata={
            "name": "DocumentID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    approval_status: ApprovalStatus | None = field(
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
    endorser_party: EndorserParty | None = field(
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
    evaluation_criterion_type_code: EvaluationCriterionTypeCode | None = (
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
    threshold_amount: ThresholdAmount | None = field(
        default=None,
        metadata={
            "name": "ThresholdAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    threshold_quantity: ThresholdQuantity | None = field(
        default=None,
        metadata={
            "name": "ThresholdQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expression_code: ExpressionCode | None = field(
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
    duration_period: DurationPeriod | None = field(
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
    registration_name: RegistrationName | None = field(
        default=None,
        metadata={
            "name": "RegistrationName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_id: CompanyId | None = field(
        default=None,
        metadata={
            "name": "CompanyID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_date: RegistrationDate | None = field(
        default=None,
        metadata={
            "name": "RegistrationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_expiration_date: RegistrationExpirationDate | None = field(
        default=None,
        metadata={
            "name": "RegistrationExpirationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_legal_form_code: CompanyLegalFormCode | None = field(
        default=None,
        metadata={
            "name": "CompanyLegalFormCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_legal_form: CompanyLegalForm | None = field(
        default=None,
        metadata={
            "name": "CompanyLegalForm",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sole_proprietorship_indicator: SoleProprietorshipIndicator | None = (
        field(
            default=None,
            metadata={
                "name": "SoleProprietorshipIndicator",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    company_liquidation_status_code: CompanyLiquidationStatusCode | None = (
        field(
            default=None,
            metadata={
                "name": "CompanyLiquidationStatusCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    corporate_stock_amount: CorporateStockAmount | None = field(
        default=None,
        metadata={
            "name": "CorporateStockAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fully_paid_shares_indicator: FullyPaidSharesIndicator | None = field(
        default=None,
        metadata={
            "name": "FullyPaidSharesIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    registration_address: RegistrationAddress | None = field(
        default=None,
        metadata={
            "name": "RegistrationAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    corporate_registration_scheme: CorporateRegistrationScheme | None = (
        field(
            default=None,
            metadata={
                "name": "CorporateRegistrationScheme",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    head_office_party: HeadOfficeParty | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_means_code: PaymentMeansCode | None = field(
        default=None,
        metadata={
            "name": "PaymentMeansCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    payment_due_date: PaymentDueDate | None = field(
        default=None,
        metadata={
            "name": "PaymentDueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_channel_code: PaymentChannelCode | None = field(
        default=None,
        metadata={
            "name": "PaymentChannelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    instruction_id: InstructionId | None = field(
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
    card_account: CardAccount | None = field(
        default=None,
        metadata={
            "name": "CardAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payer_financial_account: PayerFinancialAccount | None = field(
        default=None,
        metadata={
            "name": "PayerFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payee_financial_account: PayeeFinancialAccount | None = field(
        default=None,
        metadata={
            "name": "PayeeFinancialAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    credit_account: CreditAccount | None = field(
        default=None,
        metadata={
            "name": "CreditAccount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_mandate: PaymentMandate | None = field(
        default=None,
        metadata={
            "name": "PaymentMandate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    trade_financing: TradeFinancing | None = field(
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
    tenderer_requirement_type_code: TendererRequirementTypeCode | None = (
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
    legal_reference: LegalReference | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    original_contracting_system_id: OriginalContractingSystemId | None = (
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
    procedure_code: ProcedureCode | None = field(
        default=None,
        metadata={
            "name": "ProcedureCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    urgency_code: UrgencyCode | None = field(
        default=None,
        metadata={
            "name": "UrgencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    expense_code: ExpenseCode | None = field(
        default=None,
        metadata={
            "name": "ExpenseCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    part_presentation_code: PartPresentationCode | None = field(
        default=None,
        metadata={
            "name": "PartPresentationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contracting_system_code: ContractingSystemCode | None = field(
        default=None,
        metadata={
            "name": "ContractingSystemCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    submission_method_code: SubmissionMethodCode | None = field(
        default=None,
        metadata={
            "name": "SubmissionMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    candidate_reduction_constraint_indicator: CandidateReductionConstraintIndicator | None = field(
        default=None,
        metadata={
            "name": "CandidateReductionConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    government_agreement_constraint_indicator: GovernmentAgreementConstraintIndicator | None = field(
        default=None,
        metadata={
            "name": "GovernmentAgreementConstraintIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    document_availability_period: DocumentAvailabilityPeriod | None = field(
        default=None,
        metadata={
            "name": "DocumentAvailabilityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_submission_deadline_period: TenderSubmissionDeadlinePeriod | None = field(
        default=None,
        metadata={
            "name": "TenderSubmissionDeadlinePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    invitation_submission_period: InvitationSubmissionPeriod | None = field(
        default=None,
        metadata={
            "name": "InvitationSubmissionPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    participation_request_reception_period: ParticipationRequestReceptionPeriod | None = field(
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
    economic_operator_short_list: EconomicOperatorShortList | None = field(
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
    auction_terms: AuctionTerms | None = field(
        default=None,
        metadata={
            "name": "AuctionTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    framework_agreement: FrameworkAgreement | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    charge_indicator: ChargeIndicator | None = field(
        default=None,
        metadata={
            "name": "ChargeIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    allowance_charge_reason_code: AllowanceChargeReasonCode | None = field(
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
    multiplier_factor_numeric: MultiplierFactorNumeric | None = field(
        default=None,
        metadata={
            "name": "MultiplierFactorNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    prepaid_indicator: PrepaidIndicator | None = field(
        default=None,
        metadata={
            "name": "PrepaidIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sequence_numeric: SequenceNumeric | None = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    base_amount: BaseAmount | None = field(
        default=None,
        metadata={
            "name": "BaseAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: AccountingCostCode | None = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: AccountingCost | None = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    per_unit_amount: PerUnitAmount | None = field(
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
    tax_total: TaxTotal | None = field(
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
    pack_quantity: PackQuantity | None = field(
        default=None,
        metadata={
            "name": "PackQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pack_size_numeric: PackSizeNumeric | None = field(
        default=None,
        metadata={
            "name": "PackSizeNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    catalogue_indicator: CatalogueIndicator | None = field(
        default=None,
        metadata={
            "name": "CatalogueIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_risk_indicator: HazardousRiskIndicator | None = field(
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
    buyers_item_identification: BuyersItemIdentification | None = field(
        default=None,
        metadata={
            "name": "BuyersItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sellers_item_identification: SellersItemIdentification | None = field(
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
    standard_item_identification: StandardItemIdentification | None = field(
        default=None,
        metadata={
            "name": "StandardItemIdentification",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    catalogue_item_identification: CatalogueItemIdentification | None = (
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
    catalogue_document_reference: CatalogueDocumentReference | None = field(
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
    origin_country: OriginCountry | None = field(
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
    information_content_provider_party: InformationContentProviderParty | None = field(
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
    participation_percent: ParticipationPercent | None = field(
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
    operating_years_quantity: OperatingYearsQuantity | None = field(
        default=None,
        metadata={
            "name": "OperatingYearsQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    employee_quantity: EmployeeQuantity | None = field(
        default=None,
        metadata={
            "name": "EmployeeQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    business_classification_evidence_id: BusinessClassificationEvidenceId | None = field(
        default=None,
        metadata={
            "name": "BusinessClassificationEvidenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    business_identity_evidence_id: BusinessIdentityEvidenceId | None = (
        field(
            default=None,
            metadata={
                "name": "BusinessIdentityEvidenceID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    tenderer_role_code: TendererRoleCode | None = field(
        default=None,
        metadata={
            "name": "TendererRoleCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    business_classification_scheme: BusinessClassificationScheme | None = (
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
    party: Party | None = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    economic_operator_role: EconomicOperatorRole | None = field(
        default=None,
        metadata={
            "name": "EconomicOperatorRole",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TendererQualificationRequestType:
    company_legal_form_code: CompanyLegalFormCode | None = field(
        default=None,
        metadata={
            "name": "CompanyLegalFormCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    company_legal_form: CompanyLegalForm | None = field(
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
    operating_years_quantity: OperatingYearsQuantity | None = field(
        default=None,
        metadata={
            "name": "OperatingYearsQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    employee_quantity: EmployeeQuantity | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    amount: Amount | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    contractor_customer_party: ContractorCustomerParty | None = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: SellerSupplierParty | None = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Item | None = field(
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
    id: Id | None = field(
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
    loss_risk_responsibility_code: LossRiskResponsibilityCode | None = (
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
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivery_location: DeliveryLocation | None = field(
        default=None,
        metadata={
            "name": "DeliveryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    allowance_charge: AllowanceCharge | None = field(
        default=None,
        metadata={
            "name": "AllowanceCharge",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DespatchLineType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Uuid | None = field(
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
    line_status_code: LineStatusCode | None = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivered_quantity: DeliveredQuantity | None = field(
        default=None,
        metadata={
            "name": "DeliveredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    backorder_quantity: BackorderQuantity | None = field(
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
    outstanding_quantity: OutstandingQuantity | None = field(
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
    oversupply_quantity: OversupplyQuantity | None = field(
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
    item: Item | None = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    shipment: tuple[Shipment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class EventLineItemType:
    line_number_numeric: LineNumberNumeric | None = field(
        default=None,
        metadata={
            "name": "LineNumberNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    participating_locations_location: ParticipatingLocationsLocation | None = field(
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
    supply_item: SupplyItem | None = field(
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
    id: Id | None = field(
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
    threshold_value_comparison_code: ThresholdValueComparisonCode | None = (
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
    threshold_quantity: ThresholdQuantity | None = field(
        default=None,
        metadata={
            "name": "ThresholdQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    exception_status_code: ExceptionStatusCode | None = field(
        default=None,
        metadata={
            "name": "ExceptionStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    collaboration_priority_code: CollaborationPriorityCode | None = field(
        default=None,
        metadata={
            "name": "CollaborationPriorityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exception_resolution_code: ExceptionResolutionCode | None = field(
        default=None,
        metadata={
            "name": "ExceptionResolutionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    supply_chain_activity_type_code: SupplyChainActivityTypeCode | None = (
        field(
            default=None,
            metadata={
                "name": "SupplyChainActivityTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    performance_metric_type_code: PerformanceMetricTypeCode | None = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    effective_period: EffectivePeriod | None = field(
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
    forecast_exception_criterion_line: ForecastExceptionCriterionLine | None = field(
        default=None,
        metadata={
            "name": "ForecastExceptionCriterionLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ExceptionNotificationLineType:
    id: Id | None = field(
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
    exception_status_code: ExceptionStatusCode | None = field(
        default=None,
        metadata={
            "name": "ExceptionStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    collaboration_priority_code: CollaborationPriorityCode | None = field(
        default=None,
        metadata={
            "name": "CollaborationPriorityCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    resolution_code: ResolutionCode | None = field(
        default=None,
        metadata={
            "name": "ResolutionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    compared_value_measure: ComparedValueMeasure | None = field(
        default=None,
        metadata={
            "name": "ComparedValueMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    source_value_measure: SourceValueMeasure | None = field(
        default=None,
        metadata={
            "name": "SourceValueMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    variance_quantity: VarianceQuantity | None = field(
        default=None,
        metadata={
            "name": "VarianceQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    supply_chain_activity_type_code: SupplyChainActivityTypeCode | None = (
        field(
            default=None,
            metadata={
                "name": "SupplyChainActivityTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    performance_metric_type_code: PerformanceMetricTypeCode | None = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    exception_observation_period: ExceptionObservationPeriod | None = field(
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
    forecast_exception: ForecastException | None = field(
        default=None,
        metadata={
            "name": "ForecastException",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supply_item: SupplyItem | None = field(
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
    id: Id | None = field(
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
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    manufacturer_party: ManufacturerParty | None = field(
        default=None,
        metadata={
            "name": "ManufacturerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Item | None = field(
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
    id: Id | None = field(
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
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    inventory_value_amount: InventoryValueAmount | None = field(
        default=None,
        metadata={
            "name": "InventoryValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    availability_date: AvailabilityDate | None = field(
        default=None,
        metadata={
            "name": "AvailabilityDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    availability_status_code: AvailabilityStatusCode | None = field(
        default=None,
        metadata={
            "name": "AvailabilityStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    item: Item | None = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    inventory_location: InventoryLocation | None = field(
        default=None,
        metadata={
            "name": "InventoryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PerformanceDataLineType:
    id: Id | None = field(
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
    performance_value_quantity: PerformanceValueQuantity | None = field(
        default=None,
        metadata={
            "name": "PerformanceValueQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    performance_metric_type_code: PerformanceMetricTypeCode | None = field(
        default=None,
        metadata={
            "name": "PerformanceMetricTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    period: Period | None = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Item | None = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PriceType:
    price_amount: PriceAmount | None = field(
        default=None,
        metadata={
            "name": "PriceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    base_quantity: BaseQuantity | None = field(
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
    price_type_code: PriceTypeCode | None = field(
        default=None,
        metadata={
            "name": "PriceTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    price_type: UblCommonBasicComponents21PriceType | None = field(
        default=None,
        metadata={
            "name": "PriceType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    orderable_unit_factor_rate: OrderableUnitFactorRate | None = field(
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
    price_list: PriceList | None = field(
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
    pricing_exchange_rate: PricingExchangeRate | None = field(
        default=None,
        metadata={
            "name": "PricingExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ReceiptLineType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Uuid | None = field(
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
    received_quantity: ReceivedQuantity | None = field(
        default=None,
        metadata={
            "name": "ReceivedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    short_quantity: ShortQuantity | None = field(
        default=None,
        metadata={
            "name": "ShortQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    shortage_action_code: ShortageActionCode | None = field(
        default=None,
        metadata={
            "name": "ShortageActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    rejected_quantity: RejectedQuantity | None = field(
        default=None,
        metadata={
            "name": "RejectedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reject_reason_code: RejectReasonCode | None = field(
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
    reject_action_code: RejectActionCode | None = field(
        default=None,
        metadata={
            "name": "RejectActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity_discrepancy_code: QuantityDiscrepancyCode | None = field(
        default=None,
        metadata={
            "name": "QuantityDiscrepancyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    oversupply_quantity: OversupplyQuantity | None = field(
        default=None,
        metadata={
            "name": "OversupplyQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_date: ReceivedDate | None = field(
        default=None,
        metadata={
            "name": "ReceivedDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    timing_complaint_code: TimingComplaintCode | None = field(
        default=None,
        metadata={
            "name": "TimingComplaintCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    timing_complaint: TimingComplaint | None = field(
        default=None,
        metadata={
            "name": "TimingComplaint",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_line_reference: OrderLineReference | None = field(
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
    shipment: tuple[Shipment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class StockAvailabilityReportLineType:
    id: Id | None = field(
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
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    value_amount: ValueAmount | None = field(
        default=None,
        metadata={
            "name": "ValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    availability_date: AvailabilityDate | None = field(
        default=None,
        metadata={
            "name": "AvailabilityDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    availability_status_code: AvailabilityStatusCode | None = field(
        default=None,
        metadata={
            "name": "AvailabilityStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    item: Item | None = field(
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
    invoice_document_reference: InvoiceDocumentReference | None = field(
        default=None,
        metadata={
            "name": "InvoiceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    self_billed_invoice_document_reference: SelfBilledInvoiceDocumentReference | None = field(
        default=None,
        metadata={
            "name": "SelfBilledInvoiceDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    credit_note_document_reference: CreditNoteDocumentReference | None = (
        field(
            default=None,
            metadata={
                "name": "CreditNoteDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    self_billed_credit_note_document_reference: SelfBilledCreditNoteDocumentReference | None = field(
        default=None,
        metadata={
            "name": "SelfBilledCreditNoteDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    debit_note_document_reference: DebitNoteDocumentReference | None = (
        field(
            default=None,
            metadata={
                "name": "DebitNoteDocumentReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    reminder_document_reference: ReminderDocumentReference | None = field(
        default=None,
        metadata={
            "name": "ReminderDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    additional_document_reference: AdditionalDocumentReference | None = (
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    carrier_assigned_id: CarrierAssignedId | None = field(
        default=None,
        metadata={
            "name": "CarrierAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consignee_assigned_id: ConsigneeAssignedId | None = field(
        default=None,
        metadata={
            "name": "ConsigneeAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consignor_assigned_id: ConsignorAssignedId | None = field(
        default=None,
        metadata={
            "name": "ConsignorAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    freight_forwarder_assigned_id: FreightForwarderAssignedId | None = (
        field(
            default=None,
            metadata={
                "name": "FreightForwarderAssignedID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    broker_assigned_id: BrokerAssignedId | None = field(
        default=None,
        metadata={
            "name": "BrokerAssignedID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contracted_carrier_assigned_id: ContractedCarrierAssignedId | None = (
        field(
            default=None,
            metadata={
                "name": "ContractedCarrierAssignedID",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    performing_carrier_assigned_id: PerformingCarrierAssignedId | None = (
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
    total_invoice_amount: TotalInvoiceAmount | None = field(
        default=None,
        metadata={
            "name": "TotalInvoiceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_customs_value_amount: DeclaredCustomsValueAmount | None = (
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
    tariff_code: TariffCode | None = field(
        default=None,
        metadata={
            "name": "TariffCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    insurance_premium_amount: InsurancePremiumAmount | None = field(
        default=None,
        metadata={
            "name": "InsurancePremiumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_weight_measure: GrossWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_weight_measure: NetWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_net_weight_measure: NetNetWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    chargeable_weight_measure: ChargeableWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "ChargeableWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_volume_measure: GrossVolumeMeasure | None = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_volume_measure: NetVolumeMeasure | None = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    loading_length_measure: LoadingLengthMeasure | None = field(
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
    hazardous_risk_indicator: HazardousRiskIndicator | None = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    animal_food_indicator: AnimalFoodIndicator | None = field(
        default=None,
        metadata={
            "name": "AnimalFoodIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    human_food_indicator: HumanFoodIndicator | None = field(
        default=None,
        metadata={
            "name": "HumanFoodIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    livestock_indicator: LivestockIndicator | None = field(
        default=None,
        metadata={
            "name": "LivestockIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    bulk_cargo_indicator: BulkCargoIndicator | None = field(
        default=None,
        metadata={
            "name": "BulkCargoIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    containerized_indicator: ContainerizedIndicator | None = field(
        default=None,
        metadata={
            "name": "ContainerizedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    general_cargo_indicator: GeneralCargoIndicator | None = field(
        default=None,
        metadata={
            "name": "GeneralCargoIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    special_security_indicator: SpecialSecurityIndicator | None = field(
        default=None,
        metadata={
            "name": "SpecialSecurityIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    third_party_payer_indicator: ThirdPartyPayerIndicator | None = field(
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
    sequence_id: SequenceId | None = field(
        default=None,
        metadata={
            "name": "SequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    shipping_priority_level_code: ShippingPriorityLevelCode | None = field(
        default=None,
        metadata={
            "name": "ShippingPriorityLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_code: HandlingCode | None = field(
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
    total_goods_item_quantity: TotalGoodsItemQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalGoodsItemQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_transport_handling_unit_quantity: TotalTransportHandlingUnitQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalTransportHandlingUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    insurance_value_amount: InsuranceValueAmount | None = field(
        default=None,
        metadata={
            "name": "InsuranceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_for_carriage_value_amount: DeclaredForCarriageValueAmount | None = field(
        default=None,
        metadata={
            "name": "DeclaredForCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_statistics_value_amount: DeclaredStatisticsValueAmount | None = field(
        default=None,
        metadata={
            "name": "DeclaredStatisticsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_on_board_value_amount: FreeOnBoardValueAmount | None = field(
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
    split_consignment_indicator: SplitConsignmentIndicator | None = field(
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
    consignment_quantity: ConsignmentQuantity | None = field(
        default=None,
        metadata={
            "name": "ConsignmentQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consolidatable_indicator: ConsolidatableIndicator | None = field(
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
    loading_sequence_id: LoadingSequenceId | None = field(
        default=None,
        metadata={
            "name": "LoadingSequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    child_consignment_quantity: ChildConsignmentQuantity | None = field(
        default=None,
        metadata={
            "name": "ChildConsignmentQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_packages_quantity: TotalPackagesQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalPackagesQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consolidated_shipment: tuple[ConsolidatedShipment, ...] = field(
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
    requested_pickup_transport_event: RequestedPickupTransportEvent | None = field(
        default=None,
        metadata={
            "name": "RequestedPickupTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_delivery_transport_event: RequestedDeliveryTransportEvent | None = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_pickup_transport_event: PlannedPickupTransportEvent | None = (
        field(
            default=None,
            metadata={
                "name": "PlannedPickupTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    planned_delivery_transport_event: PlannedDeliveryTransportEvent | None = field(
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
    child_consignment: tuple[ChildConsignment, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ChildConsignment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consignee_party: ConsigneeParty | None = field(
        default=None,
        metadata={
            "name": "ConsigneeParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exporter_party: ExporterParty | None = field(
        default=None,
        metadata={
            "name": "ExporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consignor_party: ConsignorParty | None = field(
        default=None,
        metadata={
            "name": "ConsignorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    importer_party: ImporterParty | None = field(
        default=None,
        metadata={
            "name": "ImporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    carrier_party: CarrierParty | None = field(
        default=None,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    freight_forwarder_party: FreightForwarderParty | None = field(
        default=None,
        metadata={
            "name": "FreightForwarderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    notify_party: NotifyParty | None = field(
        default=None,
        metadata={
            "name": "NotifyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    original_despatch_party: OriginalDespatchParty | None = field(
        default=None,
        metadata={
            "name": "OriginalDespatchParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    final_delivery_party: FinalDeliveryParty | None = field(
        default=None,
        metadata={
            "name": "FinalDeliveryParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    performing_carrier_party: PerformingCarrierParty | None = field(
        default=None,
        metadata={
            "name": "PerformingCarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    substitute_carrier_party: SubstituteCarrierParty | None = field(
        default=None,
        metadata={
            "name": "SubstituteCarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    logistics_operator_party: LogisticsOperatorParty | None = field(
        default=None,
        metadata={
            "name": "LogisticsOperatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_advisor_party: TransportAdvisorParty | None = field(
        default=None,
        metadata={
            "name": "TransportAdvisorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    hazardous_item_notification_party: HazardousItemNotificationParty | None = field(
        default=None,
        metadata={
            "name": "HazardousItemNotificationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    insurance_party: InsuranceParty | None = field(
        default=None,
        metadata={
            "name": "InsuranceParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    mortgage_holder_party: MortgageHolderParty | None = field(
        default=None,
        metadata={
            "name": "MortgageHolderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    bill_of_lading_holder_party: BillOfLadingHolderParty | None = field(
        default=None,
        metadata={
            "name": "BillOfLadingHolderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    original_departure_country: OriginalDepartureCountry | None = field(
        default=None,
        metadata={
            "name": "OriginalDepartureCountry",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    final_destination_country: FinalDestinationCountry | None = field(
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
    transport_contract: TransportContract | None = field(
        default=None,
        metadata={
            "name": "TransportContract",
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
    original_despatch_transportation_service: OriginalDespatchTransportationService | None = field(
        default=None,
        metadata={
            "name": "OriginalDespatchTransportationService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    final_delivery_transportation_service: FinalDeliveryTransportationService | None = field(
        default=None,
        metadata={
            "name": "FinalDeliveryTransportationService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: DeliveryTerms | None = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payment_terms: PaymentTerms | None = field(
        default=None,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    collect_payment_terms: CollectPaymentTerms | None = field(
        default=None,
        metadata={
            "name": "CollectPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    disbursement_payment_terms: DisbursementPaymentTerms | None = field(
        default=None,
        metadata={
            "name": "DisbursementPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    prepaid_payment_terms: PrepaidPaymentTerms | None = field(
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
    main_carriage_shipment_stage: tuple[MainCarriageShipmentStage, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "MainCarriageShipmentStage",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    pre_carriage_shipment_stage: tuple[PreCarriageShipmentStage, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "PreCarriageShipmentStage",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    on_carriage_shipment_stage: tuple[OnCarriageShipmentStage, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "OnCarriageShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_handling_unit: tuple[TransportHandlingUnit, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportHandlingUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    first_arrival_port_location: FirstArrivalPortLocation | None = field(
        default=None,
        metadata={
            "name": "FirstArrivalPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    last_exit_port_location: LastExitPortLocation | None = field(
        default=None,
        metadata={
            "name": "LastExitPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DeliveryType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: MinimumQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: MaximumQuantity | None = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_delivery_date: ActualDeliveryDate | None = field(
        default=None,
        metadata={
            "name": "ActualDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    actual_delivery_time: ActualDeliveryTime | None = field(
        default=None,
        metadata={
            "name": "ActualDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_delivery_date: LatestDeliveryDate | None = field(
        default=None,
        metadata={
            "name": "LatestDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_delivery_time: LatestDeliveryTime | None = field(
        default=None,
        metadata={
            "name": "LatestDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    release_id: ReleaseId | None = field(
        default=None,
        metadata={
            "name": "ReleaseID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tracking_id: TrackingId | None = field(
        default=None,
        metadata={
            "name": "TrackingID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    delivery_address: DeliveryAddress | None = field(
        default=None,
        metadata={
            "name": "DeliveryAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_location: DeliveryLocation | None = field(
        default=None,
        metadata={
            "name": "DeliveryLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    alternative_delivery_location: AlternativeDeliveryLocation | None = (
        field(
            default=None,
            metadata={
                "name": "AlternativeDeliveryLocation",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    requested_delivery_period: RequestedDeliveryPeriod | None = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    promised_delivery_period: PromisedDeliveryPeriod | None = field(
        default=None,
        metadata={
            "name": "PromisedDeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_delivery_period: EstimatedDeliveryPeriod | None = field(
        default=None,
        metadata={
            "name": "EstimatedDeliveryPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    carrier_party: CarrierParty | None = field(
        default=None,
        metadata={
            "name": "CarrierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_party: DeliveryParty | None = field(
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
    despatch: Despatch | None = field(
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
    minimum_delivery_unit: MinimumDeliveryUnit | None = field(
        default=None,
        metadata={
            "name": "MinimumDeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maximum_delivery_unit: MaximumDeliveryUnit | None = field(
        default=None,
        metadata={
            "name": "MaximumDeliveryUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment: Shipment | None = field(
        default=None,
        metadata={
            "name": "Shipment",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class MiscellaneousEventType:
    miscellaneous_event_type_code: MiscellaneousEventTypeCode | None = (
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
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    event_line_item: EventLineItem | None = field(
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
    quantity: Quantity | None = field(
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
    item: Item | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    call_date: CallDate | None = field(
        default=None,
        metadata={
            "name": "CallDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    call_time: CallTime | None = field(
        default=None,
        metadata={
            "name": "CallTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    service_number_called: ServiceNumberCalled | None = field(
        default=None,
        metadata={
            "name": "ServiceNumberCalled",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    telecommunications_service_category: TelecommunicationsServiceCategory | None = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCategory",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telecommunications_service_category_code: TelecommunicationsServiceCategoryCode | None = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCategoryCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    movie_title: MovieTitle | None = field(
        default=None,
        metadata={
            "name": "MovieTitle",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    roaming_partner_name: RoamingPartnerName | None = field(
        default=None,
        metadata={
            "name": "RoamingPartnerName",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pay_per_view: PayPerView | None = field(
        default=None,
        metadata={
            "name": "PayPerView",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telecommunications_service_call: TelecommunicationsServiceCall | None = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCall",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telecommunications_service_call_code: TelecommunicationsServiceCallCode | None = field(
        default=None,
        metadata={
            "name": "TelecommunicationsServiceCallCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    call_base_amount: CallBaseAmount | None = field(
        default=None,
        metadata={
            "name": "CallBaseAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    call_extension_amount: CallExtensionAmount | None = field(
        default=None,
        metadata={
            "name": "CallExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    price: Price | None = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    country: Country | None = field(
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
    bonus_payment_terms: BonusPaymentTerms | None = field(
        default=None,
        metadata={
            "name": "BonusPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    commission_payment_terms: CommissionPaymentTerms | None = field(
        default=None,
        metadata={
            "name": "CommissionPaymentTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    penalty_payment_terms: PenaltyPaymentTerms | None = field(
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
    service_charge_payment_terms: ServiceChargePaymentTerms | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    supply_chain_activity_type_code: SupplyChainActivityTypeCode | None = (
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
    buyer_customer_party: BuyerCustomerParty | None = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: SellerSupplierParty | None = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    activity_period: ActivityPeriod | None = field(
        default=None,
        metadata={
            "name": "ActivityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    activity_origin_location: ActivityOriginLocation | None = field(
        default=None,
        metadata={
            "name": "ActivityOriginLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    activity_final_location: ActivityFinalLocation | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    parent_document_line_reference_id: ParentDocumentLineReferenceId | None = field(
        default=None,
        metadata={
            "name": "ParentDocumentLineReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoiced_quantity: InvoicedQuantity | None = field(
        default=None,
        metadata={
            "name": "InvoicedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    line_extension_amount: LineExtensionAmount | None = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    period: Period | None = field(
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
    utility_item: UtilityItem | None = field(
        default=None,
        metadata={
            "name": "UtilityItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    price: Price | None = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    unstructured_price: UnstructuredPrice | None = field(
        default=None,
        metadata={
            "name": "UnstructuredPrice",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ForecastLineType:
    id: Id | None = field(
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
    frozen_document_indicator: FrozenDocumentIndicator | None = field(
        default=None,
        metadata={
            "name": "FrozenDocumentIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    forecast_type_code: ForecastTypeCode | None = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    forecast_period: ForecastPeriod | None = field(
        default=None,
        metadata={
            "name": "ForecastPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sales_item: SalesItem | None = field(
        default=None,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ForecastRevisionLineType:
    id: Id | None = field(
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
    revised_forecast_line_id: RevisedForecastLineId | None = field(
        default=None,
        metadata={
            "name": "RevisedForecastLineID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    source_forecast_issue_date: SourceForecastIssueDate | None = field(
        default=None,
        metadata={
            "name": "SourceForecastIssueDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    source_forecast_issue_time: SourceForecastIssueTime | None = field(
        default=None,
        metadata={
            "name": "SourceForecastIssueTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    adjustment_reason_code: AdjustmentReasonCode | None = field(
        default=None,
        metadata={
            "name": "AdjustmentReasonCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    forecast_period: ForecastPeriod | None = field(
        default=None,
        metadata={
            "name": "ForecastPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sales_item: SalesItem | None = field(
        default=None,
        metadata={
            "name": "SalesItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class GoodsItemType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sequence_number_id: SequenceNumberId | None = field(
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
    hazardous_risk_indicator: HazardousRiskIndicator | None = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_customs_value_amount: DeclaredCustomsValueAmount | None = (
        field(
            default=None,
            metadata={
                "name": "DeclaredCustomsValueAmount",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    declared_for_carriage_value_amount: DeclaredForCarriageValueAmount | None = field(
        default=None,
        metadata={
            "name": "DeclaredForCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_statistics_value_amount: DeclaredStatisticsValueAmount | None = field(
        default=None,
        metadata={
            "name": "DeclaredStatisticsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_on_board_value_amount: FreeOnBoardValueAmount | None = field(
        default=None,
        metadata={
            "name": "FreeOnBoardValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    insurance_value_amount: InsuranceValueAmount | None = field(
        default=None,
        metadata={
            "name": "InsuranceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    value_amount: ValueAmount | None = field(
        default=None,
        metadata={
            "name": "ValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_weight_measure: GrossWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_weight_measure: NetWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_net_weight_measure: NetNetWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    chargeable_weight_measure: ChargeableWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "ChargeableWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_volume_measure: GrossVolumeMeasure | None = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_volume_measure: NetVolumeMeasure | None = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    preference_criterion_code: PreferenceCriterionCode | None = field(
        default=None,
        metadata={
            "name": "PreferenceCriterionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_customs_id: RequiredCustomsId | None = field(
        default=None,
        metadata={
            "name": "RequiredCustomsID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customs_status_code: CustomsStatusCode | None = field(
        default=None,
        metadata={
            "name": "CustomsStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customs_tariff_quantity: CustomsTariffQuantity | None = field(
        default=None,
        metadata={
            "name": "CustomsTariffQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    customs_import_classified_indicator: CustomsImportClassifiedIndicator | None = field(
        default=None,
        metadata={
            "name": "CustomsImportClassifiedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    chargeable_quantity: ChargeableQuantity | None = field(
        default=None,
        metadata={
            "name": "ChargeableQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    returnable_quantity: ReturnableQuantity | None = field(
        default=None,
        metadata={
            "name": "ReturnableQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trace_id: TraceId | None = field(
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
    goods_item_container: tuple[GoodsItemContainer, ...] = field(
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
    invoice_line: tuple[InvoiceLine, ...] = field(
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
    contained_goods_item: tuple[ContainedGoodsItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContainedGoodsItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    origin_address: OriginAddress | None = field(
        default=None,
        metadata={
            "name": "OriginAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: Delivery | None = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pickup: Pickup | None = field(
        default=None,
        metadata={
            "name": "Pickup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch: Despatch | None = field(
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
    containing_package: tuple[ContainingPackage, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContainingPackage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    shipment_document_reference: ShipmentDocumentReference | None = field(
        default=None,
        metadata={
            "name": "ShipmentDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    minimum_temperature: MinimumTemperature | None = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maximum_temperature: MaximumTemperature | None = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ItemInformationRequestLineType:
    time_frequency_code: TimeFrequencyCode | None = field(
        default=None,
        metadata={
            "name": "TimeFrequencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    supply_chain_activity_type_code: SupplyChainActivityTypeCode | None = (
        field(
            default=None,
            metadata={
                "name": "SupplyChainActivityTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    forecast_type_code: ForecastTypeCode | None = field(
        default=None,
        metadata={
            "name": "ForecastTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    performance_metric_type_code: PerformanceMetricTypeCode | None = field(
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
    specification_id: SpecificationId | None = field(
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
    id: Id | None = field(
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
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    balance_brought_forward_indicator: BalanceBroughtForwardIndicator | None = field(
        default=None,
        metadata={
            "name": "BalanceBroughtForwardIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    debit_line_amount: DebitLineAmount | None = field(
        default=None,
        metadata={
            "name": "DebitLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    credit_line_amount: CreditLineAmount | None = field(
        default=None,
        metadata={
            "name": "CreditLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: AccountingCostCode | None = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: AccountingCost | None = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    penalty_surcharge_percent: PenaltySurchargePercent | None = field(
        default=None,
        metadata={
            "name": "PenaltySurchargePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    amount: Amount | None = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: PaymentPurposeCode | None = field(
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
    exchange_rate: ExchangeRate | None = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RemittanceAdviceLineType:
    id: Id | None = field(
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
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    debit_line_amount: DebitLineAmount | None = field(
        default=None,
        metadata={
            "name": "DebitLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    credit_line_amount: CreditLineAmount | None = field(
        default=None,
        metadata={
            "name": "CreditLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    balance_amount: BalanceAmount | None = field(
        default=None,
        metadata={
            "name": "BalanceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: PaymentPurposeCode | None = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    invoicing_party_reference: InvoicingPartyReference | None = field(
        default=None,
        metadata={
            "name": "InvoicingPartyReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_supplier_party: AccountingSupplierParty | None = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_customer_party: AccountingCustomerParty | None = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    buyer_customer_party: BuyerCustomerParty | None = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: SellerSupplierParty | None = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_customer_party: OriginatorCustomerParty | None = field(
        default=None,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payee_party: PayeeParty | None = field(
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
    exchange_rate: ExchangeRate | None = field(
        default=None,
        metadata={
            "name": "ExchangeRate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class StatementLineType:
    id: Id | None = field(
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
    uuid: Uuid | None = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    balance_brought_forward_indicator: BalanceBroughtForwardIndicator | None = field(
        default=None,
        metadata={
            "name": "BalanceBroughtForwardIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    debit_line_amount: DebitLineAmount | None = field(
        default=None,
        metadata={
            "name": "DebitLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    credit_line_amount: CreditLineAmount | None = field(
        default=None,
        metadata={
            "name": "CreditLineAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    balance_amount: BalanceAmount | None = field(
        default=None,
        metadata={
            "name": "BalanceAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: PaymentPurposeCode | None = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_means: PaymentMeans | None = field(
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
    buyer_customer_party: BuyerCustomerParty | None = field(
        default=None,
        metadata={
            "name": "BuyerCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: SellerSupplierParty | None = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_customer_party: OriginatorCustomerParty | None = field(
        default=None,
        metadata={
            "name": "OriginatorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_customer_party: AccountingCustomerParty | None = field(
        default=None,
        metadata={
            "name": "AccountingCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    accounting_supplier_party: AccountingSupplierParty | None = field(
        default=None,
        metadata={
            "name": "AccountingSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    payee_party: PayeeParty | None = field(
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
    exchange_rate: ExchangeRate | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    phone_number: PhoneNumber | None = field(
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
    line_extension_amount: LineExtensionAmount | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    returnable_material_indicator: ReturnableMaterialIndicator | None = (
        field(
            default=None,
            metadata={
                "name": "ReturnableMaterialIndicator",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    package_level_code: PackageLevelCode | None = field(
        default=None,
        metadata={
            "name": "PackageLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    packaging_type_code: PackagingTypeCode | None = field(
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
    trace_id: TraceId | None = field(
        default=None,
        metadata={
            "name": "TraceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contained_package: tuple[ContainedPackage, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ContainedPackage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    containing_transport_equipment: ContainingTransportEquipment | None = field(
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
    delivery: Delivery | None = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pickup: Pickup | None = field(
        default=None,
        metadata={
            "name": "Pickup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch: Despatch | None = field(
        default=None,
        metadata={
            "name": "Despatch",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PromotionalEventType:
    promotional_event_type_code: PromotionalEventTypeCode | None = field(
        default=None,
        metadata={
            "name": "PromotionalEventTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    submission_date: SubmissionDate | None = field(
        default=None,
        metadata={
            "name": "SubmissionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    first_shipment_availibility_date: FirstShipmentAvailibilityDate | None = field(
        default=None,
        metadata={
            "name": "FirstShipmentAvailibilityDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    latest_proposal_acceptance_date: LatestProposalAcceptanceDate | None = (
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    shipping_priority_level_code: ShippingPriorityLevelCode | None = field(
        default=None,
        metadata={
            "name": "ShippingPriorityLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_code: HandlingCode | None = field(
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
    gross_weight_measure: GrossWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_weight_measure: NetWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "NetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_net_weight_measure: NetNetWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "NetNetWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_volume_measure: GrossVolumeMeasure | None = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    net_volume_measure: NetVolumeMeasure | None = field(
        default=None,
        metadata={
            "name": "NetVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_goods_item_quantity: TotalGoodsItemQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalGoodsItemQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_transport_handling_unit_quantity: TotalTransportHandlingUnitQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalTransportHandlingUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    insurance_value_amount: InsuranceValueAmount | None = field(
        default=None,
        metadata={
            "name": "InsuranceValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_customs_value_amount: DeclaredCustomsValueAmount | None = (
        field(
            default=None,
            metadata={
                "name": "DeclaredCustomsValueAmount",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    declared_for_carriage_value_amount: DeclaredForCarriageValueAmount | None = field(
        default=None,
        metadata={
            "name": "DeclaredForCarriageValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    declared_statistics_value_amount: DeclaredStatisticsValueAmount | None = field(
        default=None,
        metadata={
            "name": "DeclaredStatisticsValueAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_on_board_value_amount: FreeOnBoardValueAmount | None = field(
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
    split_consignment_indicator: SplitConsignmentIndicator | None = field(
        default=None,
        metadata={
            "name": "SplitConsignmentIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    consignment_quantity: ConsignmentQuantity | None = field(
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
    shipment_stage: tuple[ShipmentStage, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ShipmentStage",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery: Delivery | None = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transport_handling_unit: tuple[TransportHandlingUnit, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "TransportHandlingUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    return_address: ReturnAddress | None = field(
        default=None,
        metadata={
            "name": "ReturnAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    origin_address: OriginAddress | None = field(
        default=None,
        metadata={
            "name": "OriginAddress",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    first_arrival_port_location: FirstArrivalPortLocation | None = field(
        default=None,
        metadata={
            "name": "FirstArrivalPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    last_exit_port_location: LastExitPortLocation | None = field(
        default=None,
        metadata={
            "name": "LastExitPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    export_country: ExportCountry | None = field(
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
    telecommunications_supply_type: UblCommonBasicComponents21TelecommunicationsSupplyType | None = field(
        default=None,
        metadata={
            "name": "TelecommunicationsSupplyType",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    telecommunications_supply_type_code: TelecommunicationsSupplyTypeCode | None = field(
        default=None,
        metadata={
            "name": "TelecommunicationsSupplyTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    privacy_code: PrivacyCode | None = field(
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
    total_amount: TotalAmount | None = field(
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
    reference_id: ReferenceId | None = field(
        default=None,
        metadata={
            "name": "ReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    certificate_type: UblCommonBasicComponents21CertificateType | None = (
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
    application_status_code: ApplicationStatusCode | None = field(
        default=None,
        metadata={
            "name": "ApplicationStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    original_job_id: OriginalJobId | None = field(
        default=None,
        metadata={
            "name": "OriginalJobID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    previous_job_id: PreviousJobId | None = field(
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
    shipment: Shipment | None = field(
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
    preparation_party: PreparationParty | None = field(
        default=None,
        metadata={
            "name": "PreparationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    issuer_party: IssuerParty | None = field(
        default=None,
        metadata={
            "name": "IssuerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    exporter_party: ExporterParty | None = field(
        default=None,
        metadata={
            "name": "ExporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    importer_party: ImporterParty | None = field(
        default=None,
        metadata={
            "name": "ImporterParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    issuing_country: IssuingCountry | None = field(
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
    utility_statement_type_code: UtilityStatementTypeCode | None = field(
        default=None,
        metadata={
            "name": "UtilityStatementTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    main_period: MainPeriod | None = field(
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
    energy_water_supply: EnergyWaterSupply | None = field(
        default=None,
        metadata={
            "name": "EnergyWaterSupply",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    telecommunications_supply: TelecommunicationsSupply | None = field(
        default=None,
        metadata={
            "name": "TelecommunicationsSupply",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    legal_monetary_total: LegalMonetaryTotal | None = field(
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
    lead_time_measure: LeadTimeMeasure | None = field(
        default=None,
        metadata={
            "name": "LeadTimeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: MinimumQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: MaximumQuantity | None = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    hazardous_risk_indicator: HazardousRiskIndicator | None = field(
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
    price: Price | None = field(
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
    package: Package | None = field(
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
    dependent_price_reference: DependentPriceReference | None = field(
        default=None,
        metadata={
            "name": "DependentPriceReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class OrderedShipmentType:
    shipment: Shipment | None = field(
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
    identification_id: IdentificationId | None = field(
        default=None,
        metadata={
            "name": "IdentificationID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    occurrence_date: OccurrenceDate | None = field(
        default=None,
        metadata={
            "name": "OccurrenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    occurrence_time: OccurrenceTime | None = field(
        default=None,
        metadata={
            "name": "OccurrenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_event_type_code: TransportEventTypeCode | None = field(
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
    completion_indicator: CompletionIndicator | None = field(
        default=None,
        metadata={
            "name": "CompletionIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reported_shipment: ReportedShipment | None = field(
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
    location: Location | None = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    signature: Signature | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    action_code: ActionCode | None = field(
        default=None,
        metadata={
            "name": "ActionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    life_cycle_status_code: LifeCycleStatusCode | None = field(
        default=None,
        metadata={
            "name": "LifeCycleStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract_subdivision: ContractSubdivision | None = field(
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
    orderable_indicator: OrderableIndicator | None = field(
        default=None,
        metadata={
            "name": "OrderableIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    orderable_unit: OrderableUnit | None = field(
        default=None,
        metadata={
            "name": "OrderableUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    content_unit_quantity: ContentUnitQuantity | None = field(
        default=None,
        metadata={
            "name": "ContentUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_quantity_increment_numeric: OrderQuantityIncrementNumeric | None = field(
        default=None,
        metadata={
            "name": "OrderQuantityIncrementNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_order_quantity: MinimumOrderQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_order_quantity: MaximumOrderQuantity | None = field(
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
    pack_level_code: PackLevelCode | None = field(
        default=None,
        metadata={
            "name": "PackLevelCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contractor_customer_party: ContractorCustomerParty | None = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: SellerSupplierParty | None = field(
        default=None,
        metadata={
            "name": "SellerSupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_party: WarrantyParty | None = field(
        default=None,
        metadata={
            "name": "WarrantyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_validity_period: WarrantyValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    line_validity_period: LineValidityPeriod | None = field(
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
    item: Item | None = field(
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
    call_for_tenders_line_reference: CallForTendersLineReference | None = (
        field(
            default=None,
            metadata={
                "name": "CallForTendersLineReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    call_for_tenders_document_reference: CallForTendersDocumentReference | None = field(
        default=None,
        metadata={
            "name": "CallForTendersDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class CataloguePricingUpdateLineType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    contractor_customer_party: ContractorCustomerParty | None = field(
        default=None,
        metadata={
            "name": "ContractorCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    seller_supplier_party: SellerSupplierParty | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    contract_subdivision: ContractSubdivision | None = field(
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
    line_validity_period: LineValidityPeriod | None = field(
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
    item: Item | None = field(
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
    frozen_period_days_numeric: FrozenPeriodDaysNumeric | None = field(
        default=None,
        metadata={
            "name": "FrozenPeriodDaysNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_inventory_quantity: MinimumInventoryQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumInventoryQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    multiple_order_quantity: MultipleOrderQuantity | None = field(
        default=None,
        metadata={
            "name": "MultipleOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_interval_days_numeric: OrderIntervalDaysNumeric | None = field(
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
    target_service_percent: TargetServicePercent | None = field(
        default=None,
        metadata={
            "name": "TargetServicePercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    target_inventory_quantity: TargetInventoryQuantity | None = field(
        default=None,
        metadata={
            "name": "TargetInventoryQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    effective_period: EffectivePeriod | None = field(
        default=None,
        metadata={
            "name": "EffectivePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    item: Item | None = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    item_location_quantity: ItemLocationQuantity | None = field(
        default=None,
        metadata={
            "name": "ItemLocationQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class PricingReferenceType:
    original_item_location_quantity: OriginalItemLocationQuantity | None = (
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Uuid | None = field(
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
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: MinimumQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: MaximumQuantity | None = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_included_indicator: TaxIncludedIndicator | None = field(
        default=None,
        metadata={
            "name": "TaxIncludedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_amount: MinimumAmount | None = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_amount: MaximumAmount | None = field(
        default=None,
        metadata={
            "name": "MaximumAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_amount: EstimatedAmount | None = field(
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
    warranty_validity_period: WarrantyValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Item | None = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    sub_request_for_tender_line: tuple[SubRequestForTenderLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubRequestForTenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class ShipmentStageType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_mode_code: TransportModeCode | None = field(
        default=None,
        metadata={
            "name": "TransportModeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_means_type_code: TransportMeansTypeCode | None = field(
        default=None,
        metadata={
            "name": "TransportMeansTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transit_direction_code: TransitDirectionCode | None = field(
        default=None,
        metadata={
            "name": "TransitDirectionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    pre_carriage_indicator: PreCarriageIndicator | None = field(
        default=None,
        metadata={
            "name": "PreCarriageIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    on_carriage_indicator: OnCarriageIndicator | None = field(
        default=None,
        metadata={
            "name": "OnCarriageIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_delivery_date: EstimatedDeliveryDate | None = field(
        default=None,
        metadata={
            "name": "EstimatedDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_delivery_time: EstimatedDeliveryTime | None = field(
        default=None,
        metadata={
            "name": "EstimatedDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_delivery_date: RequiredDeliveryDate | None = field(
        default=None,
        metadata={
            "name": "RequiredDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_delivery_time: RequiredDeliveryTime | None = field(
        default=None,
        metadata={
            "name": "RequiredDeliveryTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    loading_sequence_id: LoadingSequenceId | None = field(
        default=None,
        metadata={
            "name": "LoadingSequenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    successive_sequence_id: SuccessiveSequenceId | None = field(
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
    crew_quantity: CrewQuantity | None = field(
        default=None,
        metadata={
            "name": "CrewQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    passenger_quantity: PassengerQuantity | None = field(
        default=None,
        metadata={
            "name": "PassengerQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transit_period: TransitPeriod | None = field(
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
    transport_means: TransportMeans | None = field(
        default=None,
        metadata={
            "name": "TransportMeans",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    loading_port_location: LoadingPortLocation | None = field(
        default=None,
        metadata={
            "name": "LoadingPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    unloading_port_location: UnloadingPortLocation | None = field(
        default=None,
        metadata={
            "name": "UnloadingPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    transship_port_location: TransshipPortLocation | None = field(
        default=None,
        metadata={
            "name": "TransshipPortLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    loading_transport_event: LoadingTransportEvent | None = field(
        default=None,
        metadata={
            "name": "LoadingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    examination_transport_event: ExaminationTransportEvent | None = field(
        default=None,
        metadata={
            "name": "ExaminationTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    availability_transport_event: AvailabilityTransportEvent | None = field(
        default=None,
        metadata={
            "name": "AvailabilityTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    exportation_transport_event: ExportationTransportEvent | None = field(
        default=None,
        metadata={
            "name": "ExportationTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    discharge_transport_event: DischargeTransportEvent | None = field(
        default=None,
        metadata={
            "name": "DischargeTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warehousing_transport_event: WarehousingTransportEvent | None = field(
        default=None,
        metadata={
            "name": "WarehousingTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    takeover_transport_event: TakeoverTransportEvent | None = field(
        default=None,
        metadata={
            "name": "TakeoverTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    optional_takeover_transport_event: OptionalTakeoverTransportEvent | None = field(
        default=None,
        metadata={
            "name": "OptionalTakeoverTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    dropoff_transport_event: DropoffTransportEvent | None = field(
        default=None,
        metadata={
            "name": "DropoffTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    actual_pickup_transport_event: ActualPickupTransportEvent | None = (
        field(
            default=None,
            metadata={
                "name": "ActualPickupTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    delivery_transport_event: DeliveryTransportEvent | None = field(
        default=None,
        metadata={
            "name": "DeliveryTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    receipt_transport_event: ReceiptTransportEvent | None = field(
        default=None,
        metadata={
            "name": "ReceiptTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    storage_transport_event: StorageTransportEvent | None = field(
        default=None,
        metadata={
            "name": "StorageTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    acceptance_transport_event: AcceptanceTransportEvent | None = field(
        default=None,
        metadata={
            "name": "AcceptanceTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    terminal_operator_party: TerminalOperatorParty | None = field(
        default=None,
        metadata={
            "name": "TerminalOperatorParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    customs_agent_party: CustomsAgentParty | None = field(
        default=None,
        metadata={
            "name": "CustomsAgentParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_transit_period: EstimatedTransitPeriod | None = field(
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
    freight_charge_location: FreightChargeLocation | None = field(
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
    requested_departure_transport_event: RequestedDepartureTransportEvent | None = field(
        default=None,
        metadata={
            "name": "RequestedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    requested_arrival_transport_event: RequestedArrivalTransportEvent | None = field(
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
    planned_departure_transport_event: PlannedDepartureTransportEvent | None = field(
        default=None,
        metadata={
            "name": "PlannedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_arrival_transport_event: PlannedArrivalTransportEvent | None = (
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
    actual_departure_transport_event: ActualDepartureTransportEvent | None = field(
        default=None,
        metadata={
            "name": "ActualDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    actual_waypoint_transport_event: ActualWaypointTransportEvent | None = (
        field(
            default=None,
            metadata={
                "name": "ActualWaypointTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    actual_arrival_transport_event: ActualArrivalTransportEvent | None = (
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
    estimated_departure_transport_event: EstimatedDepartureTransportEvent | None = field(
        default=None,
        metadata={
            "name": "EstimatedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_arrival_transport_event: EstimatedArrivalTransportEvent | None = field(
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
    reporting_person: ReportingPerson | None = field(
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
    security_officer_person: SecurityOfficerPerson | None = field(
        default=None,
        metadata={
            "name": "SecurityOfficerPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    master_person: MasterPerson | None = field(
        default=None,
        metadata={
            "name": "MasterPerson",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    ships_surgeon_person: ShipsSurgeonPerson | None = field(
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
    utility_supplier_party: UtilitySupplierParty | None = field(
        default=None,
        metadata={
            "name": "UtilitySupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    utility_customer_party: UtilityCustomerParty | None = field(
        default=None,
        metadata={
            "name": "UtilityCustomerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    consumption: Consumption | None = field(
        default=None,
        metadata={
            "name": "Consumption",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    contract: Contract | None = field(
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
    id: Id | None = field(
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
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: LineExtensionAmount | None = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_tax_amount: TotalTaxAmount | None = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    orderable_unit: OrderableUnit | None = field(
        default=None,
        metadata={
            "name": "OrderableUnit",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    content_unit_quantity: ContentUnitQuantity | None = field(
        default=None,
        metadata={
            "name": "ContentUnitQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    order_quantity_increment_numeric: OrderQuantityIncrementNumeric | None = field(
        default=None,
        metadata={
            "name": "OrderQuantityIncrementNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_order_quantity: MinimumOrderQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumOrderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_order_quantity: MaximumOrderQuantity | None = field(
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
    pack_level_code: PackLevelCode | None = field(
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
    item: Item | None = field(
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
    warranty_party: WarrantyParty | None = field(
        default=None,
        metadata={
            "name": "WarrantyParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_validity_period: WarrantyValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sub_tender_line: tuple[SubTenderLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubTenderLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    call_for_tenders_line_reference: CallForTendersLineReference | None = (
        field(
            default=None,
            metadata={
                "name": "CallForTendersLineReference",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    call_for_tenders_document_reference: CallForTendersDocumentReference | None = field(
        default=None,
        metadata={
            "name": "CallForTendersDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TransportEquipmentType:
    id: Id | None = field(
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
    transport_equipment_type_code: TransportEquipmentTypeCode | None = (
        field(
            default=None,
            metadata={
                "name": "TransportEquipmentTypeCode",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    provider_type_code: ProviderTypeCode | None = field(
        default=None,
        metadata={
            "name": "ProviderTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    owner_type_code: OwnerTypeCode | None = field(
        default=None,
        metadata={
            "name": "OwnerTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    size_type_code: SizeTypeCode | None = field(
        default=None,
        metadata={
            "name": "SizeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    disposition_code: DispositionCode | None = field(
        default=None,
        metadata={
            "name": "DispositionCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fullness_indication_code: FullnessIndicationCode | None = field(
        default=None,
        metadata={
            "name": "FullnessIndicationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    refrigeration_on_indicator: RefrigerationOnIndicator | None = field(
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
    returnability_indicator: ReturnabilityIndicator | None = field(
        default=None,
        metadata={
            "name": "ReturnabilityIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    legal_status_indicator: LegalStatusIndicator | None = field(
        default=None,
        metadata={
            "name": "LegalStatusIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    air_flow_percent: AirFlowPercent | None = field(
        default=None,
        metadata={
            "name": "AirFlowPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    humidity_percent: HumidityPercent | None = field(
        default=None,
        metadata={
            "name": "HumidityPercent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    animal_food_approved_indicator: AnimalFoodApprovedIndicator | None = (
        field(
            default=None,
            metadata={
                "name": "AnimalFoodApprovedIndicator",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    human_food_approved_indicator: HumanFoodApprovedIndicator | None = (
        field(
            default=None,
            metadata={
                "name": "HumanFoodApprovedIndicator",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    dangerous_goods_approved_indicator: DangerousGoodsApprovedIndicator | None = field(
        default=None,
        metadata={
            "name": "DangerousGoodsApprovedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    refrigerated_indicator: RefrigeratedIndicator | None = field(
        default=None,
        metadata={
            "name": "RefrigeratedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    characteristics: Characteristics | None = field(
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
    gross_weight_measure: GrossWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "GrossWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    gross_volume_measure: GrossVolumeMeasure | None = field(
        default=None,
        metadata={
            "name": "GrossVolumeMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tare_weight_measure: TareWeightMeasure | None = field(
        default=None,
        metadata={
            "name": "TareWeightMeasure",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tracking_device_code: TrackingDeviceCode | None = field(
        default=None,
        metadata={
            "name": "TrackingDeviceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    power_indicator: PowerIndicator | None = field(
        default=None,
        metadata={
            "name": "PowerIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    trace_id: TraceId | None = field(
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
    minimum_temperature: MinimumTemperature | None = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maximum_temperature: MaximumTemperature | None = field(
        default=None,
        metadata={
            "name": "MaximumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    provider_party: ProviderParty | None = field(
        default=None,
        metadata={
            "name": "ProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    loading_proof_party: LoadingProofParty | None = field(
        default=None,
        metadata={
            "name": "LoadingProofParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    supplier_party: SupplierParty | None = field(
        default=None,
        metadata={
            "name": "SupplierParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    owner_party: OwnerParty | None = field(
        default=None,
        metadata={
            "name": "OwnerParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    operating_party: OperatingParty | None = field(
        default=None,
        metadata={
            "name": "OperatingParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    loading_location: LoadingLocation | None = field(
        default=None,
        metadata={
            "name": "LoadingLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    unloading_location: UnloadingLocation | None = field(
        default=None,
        metadata={
            "name": "UnloadingLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    storage_location: StorageLocation | None = field(
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
    applicable_transport_means: ApplicableTransportMeans | None = field(
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
        PackagedTransportHandlingUnit, ...
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
    attached_transport_equipment: tuple[AttachedTransportEquipment, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "name": "AttachedTransportEquipment",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    delivery: Delivery | None = field(
        default=None,
        metadata={
            "name": "Delivery",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pickup: Pickup | None = field(
        default=None,
        metadata={
            "name": "Pickup",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    despatch: Despatch | None = field(
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
        ContainedInTransportEquipment, ...
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
    sequence_numeric: SequenceNumeric | None = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    reference_date: ReferenceDate | None = field(
        default=None,
        metadata={
            "name": "ReferenceDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reference_time: ReferenceTime | None = field(
        default=None,
        metadata={
            "name": "ReferenceTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    reliability_percent: ReliabilityPercent | None = field(
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
    status_location: StatusLocation | None = field(
        default=None,
        metadata={
            "name": "StatusLocation",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    actual_arrival_transport_event: ActualArrivalTransportEvent | None = (
        field(
            default=None,
            metadata={
                "name": "ActualArrivalTransportEvent",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            },
        )
    )
    actual_departure_transport_event: ActualDepartureTransportEvent | None = field(
        default=None,
        metadata={
            "name": "ActualDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_departure_transport_event: EstimatedDepartureTransportEvent | None = field(
        default=None,
        metadata={
            "name": "EstimatedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    estimated_arrival_transport_event: EstimatedArrivalTransportEvent | None = field(
        default=None,
        metadata={
            "name": "EstimatedArrivalTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_departure_transport_event: PlannedDepartureTransportEvent | None = field(
        default=None,
        metadata={
            "name": "PlannedDepartureTransportEvent",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    planned_arrival_transport_event: PlannedArrivalTransportEvent | None = (
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Uuid | None = field(
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
    credited_quantity: CreditedQuantity | None = field(
        default=None,
        metadata={
            "name": "CreditedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: LineExtensionAmount | None = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tax_point_date: TaxPointDate | None = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: AccountingCostCode | None = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: AccountingCost | None = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: PaymentPurposeCode | None = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_of_charge_indicator: FreeOfChargeIndicator | None = field(
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
    pricing_reference: PricingReference | None = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_party: OriginatorParty | None = field(
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
    item: Item | None = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    price: Price | None = field(
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
    sub_credit_note_line: tuple[SubCreditNoteLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubCreditNoteLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_price_extension: ItemPriceExtension | None = field(
        default=None,
        metadata={
            "name": "ItemPriceExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class DebitNoteLineType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Uuid | None = field(
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
    debited_quantity: DebitedQuantity | None = field(
        default=None,
        metadata={
            "name": "DebitedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: LineExtensionAmount | None = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tax_point_date: TaxPointDate | None = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: AccountingCostCode | None = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: AccountingCost | None = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: PaymentPurposeCode | None = field(
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
    pricing_reference: PricingReference | None = field(
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
    item: Item | None = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    price: Price | None = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sub_debit_note_line: tuple[SubDebitNoteLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubDebitNoteLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class GoodsItemContainerType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    quantity: Quantity | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    uuid: Uuid | None = field(
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
    invoiced_quantity: InvoicedQuantity | None = field(
        default=None,
        metadata={
            "name": "InvoicedQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: LineExtensionAmount | None = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tax_point_date: TaxPointDate | None = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: AccountingCostCode | None = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: AccountingCost | None = field(
        default=None,
        metadata={
            "name": "AccountingCost",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    payment_purpose_code: PaymentPurposeCode | None = field(
        default=None,
        metadata={
            "name": "PaymentPurposeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    free_of_charge_indicator: FreeOfChargeIndicator | None = field(
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
    pricing_reference: PricingReference | None = field(
        default=None,
        metadata={
            "name": "PricingReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_party: OriginatorParty | None = field(
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
    item: Item | None = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    price: Price | None = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    delivery_terms: DeliveryTerms | None = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    sub_invoice_line: tuple[SubInvoiceLine, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubInvoiceLine",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item_price_extension: ItemPriceExtension | None = field(
        default=None,
        metadata={
            "name": "ItemPriceExtension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class LineItemType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    sales_order_id: SalesOrderId | None = field(
        default=None,
        metadata={
            "name": "SalesOrderID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Uuid | None = field(
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
    line_status_code: LineStatusCode | None = field(
        default=None,
        metadata={
            "name": "LineStatusCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: LineExtensionAmount | None = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_tax_amount: TotalTaxAmount | None = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_quantity: MinimumQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_quantity: MaximumQuantity | None = field(
        default=None,
        metadata={
            "name": "MaximumQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    minimum_backorder_quantity: MinimumBackorderQuantity | None = field(
        default=None,
        metadata={
            "name": "MinimumBackorderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_backorder_quantity: MaximumBackorderQuantity | None = field(
        default=None,
        metadata={
            "name": "MaximumBackorderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    inspection_method_code: InspectionMethodCode | None = field(
        default=None,
        metadata={
            "name": "InspectionMethodCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    partial_delivery_indicator: PartialDeliveryIndicator | None = field(
        default=None,
        metadata={
            "name": "PartialDeliveryIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    back_order_allowed_indicator: BackOrderAllowedIndicator | None = field(
        default=None,
        metadata={
            "name": "BackOrderAllowedIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost_code: AccountingCostCode | None = field(
        default=None,
        metadata={
            "name": "AccountingCostCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    accounting_cost: AccountingCost | None = field(
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
    delivery_terms: DeliveryTerms | None = field(
        default=None,
        metadata={
            "name": "DeliveryTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    originator_party: OriginatorParty | None = field(
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
    pricing_reference: PricingReference | None = field(
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
    price: Price | None = field(
        default=None,
        metadata={
            "name": "Price",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    item: Item | None = field(
        default=None,
        metadata={
            "name": "Item",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    sub_line_item: tuple[SubLineItem, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "SubLineItem",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_validity_period: WarrantyValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "WarrantyValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_party: WarrantyParty | None = field(
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
    item_price_extension: ItemPriceExtension | None = field(
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
    id: Id | None = field(
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
    procurement_type_code: ProcurementTypeCode | None = field(
        default=None,
        metadata={
            "name": "ProcurementTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    procurement_sub_type_code: ProcurementSubTypeCode | None = field(
        default=None,
        metadata={
            "name": "ProcurementSubTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    quality_control_code: QualityControlCode | None = field(
        default=None,
        metadata={
            "name": "QualityControlCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    required_fee_amount: RequiredFeeAmount | None = field(
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
    requested_delivery_date: RequestedDeliveryDate | None = field(
        default=None,
        metadata={
            "name": "RequestedDeliveryDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    estimated_overall_contract_quantity: EstimatedOverallContractQuantity | None = field(
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
    requested_tender_total: RequestedTenderTotal | None = field(
        default=None,
        metadata={
            "name": "RequestedTenderTotal",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    main_commodity_classification: MainCommodityClassification | None = (
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
    planned_period: PlannedPeriod | None = field(
        default=None,
        metadata={
            "name": "PlannedPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_extension: ContractExtension | None = field(
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
    consumption_id: ConsumptionId | None = field(
        default=None,
        metadata={
            "name": "ConsumptionID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    specification_type_code: SpecificationTypeCode | None = field(
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
    total_metered_quantity: TotalMeteredQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalMeteredQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    subscriber_party: SubscriberParty | None = field(
        default=None,
        metadata={
            "name": "SubscriberParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    utility_consumption_point: UtilityConsumptionPoint | None = field(
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
    consumption: Consumption | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transport_handling_unit_type_code: TransportHandlingUnitTypeCode | None = field(
        default=None,
        metadata={
            "name": "TransportHandlingUnitTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    handling_code: HandlingCode | None = field(
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
    hazardous_risk_indicator: HazardousRiskIndicator | None = field(
        default=None,
        metadata={
            "name": "HazardousRiskIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_goods_item_quantity: TotalGoodsItemQuantity | None = field(
        default=None,
        metadata={
            "name": "TotalGoodsItemQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_package_quantity: TotalPackageQuantity | None = field(
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
    trace_id: TraceId | None = field(
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
    minimum_temperature: MinimumTemperature | None = field(
        default=None,
        metadata={
            "name": "MinimumTemperature",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    maximum_temperature: MaximumTemperature | None = field(
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
    floor_space_measurement_dimension: FloorSpaceMeasurementDimension | None = field(
        default=None,
        metadata={
            "name": "FloorSpaceMeasurementDimension",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    pallet_space_measurement_dimension: PalletSpaceMeasurementDimension | None = field(
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
    transport_service_code: TransportServiceCode | None = field(
        default=None,
        metadata={
            "name": "TransportServiceCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tariff_class_code: TariffClassCode | None = field(
        default=None,
        metadata={
            "name": "TariffClassCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    priority: Priority | None = field(
        default=None,
        metadata={
            "name": "Priority",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    freight_rate_class_code: FreightRateClassCode | None = field(
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
    transportation_service_details_uri: TransportationServiceDetailsUri | None = field(
        default=None,
        metadata={
            "name": "TransportationServiceDetailsURI",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nomination_date: NominationDate | None = field(
        default=None,
        metadata={
            "name": "NominationDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    nomination_time: NominationTime | None = field(
        default=None,
        metadata={
            "name": "NominationTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    name: Name | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    sequence_numeric: SequenceNumeric | None = field(
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
    total_capacity_dimension: TotalCapacityDimension | None = field(
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
    responsible_transport_service_provider_party: ResponsibleTransportServiceProviderParty | None = field(
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
    estimated_duration_period: EstimatedDurationPeriod | None = field(
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
    substitution_status_code: SubstitutionStatusCode | None = field(
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
    line_item: LineItem | None = field(
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
    catalogue_line_reference: CatalogueLineReference | None = field(
        default=None,
        metadata={
            "name": "CatalogueLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    quotation_line_reference: QuotationLineReference | None = field(
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
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tendering_terms: TenderingTerms | None = field(
        default=None,
        metadata={
            "name": "TenderingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    procurement_project: ProcurementProject | None = field(
        default=None,
        metadata={
            "name": "ProcurementProject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class QuotationLineType:
    id: Id | None = field(
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
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    line_extension_amount: LineExtensionAmount | None = field(
        default=None,
        metadata={
            "name": "LineExtensionAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    total_tax_amount: TotalTaxAmount | None = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    request_for_quotation_line_id: RequestForQuotationLineId | None = field(
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
    line_item: LineItem | None = field(
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
    request_line_reference: RequestLineReference | None = field(
        default=None,
        metadata={
            "name": "RequestLineReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class RequestForQuotationLineType:
    id: Id | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    uuid: Uuid | None = field(
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
    optional_line_item_indicator: OptionalLineItemIndicator | None = field(
        default=None,
        metadata={
            "name": "OptionalLineItemIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    privacy_code: PrivacyCode | None = field(
        default=None,
        metadata={
            "name": "PrivacyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    security_classification_code: SecurityClassificationCode | None = field(
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
    line_item: LineItem | None = field(
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
    sequence_numeric: SequenceNumeric | None = field(
        default=None,
        metadata={
            "name": "SequenceNumeric",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    transport_execution_plan_reference_id: TransportExecutionPlanReferenceId | None = field(
        default=None,
        metadata={
            "name": "TransportExecutionPlanReferenceID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    transportation_service: TransportationService | None = field(
        default=None,
        metadata={
            "name": "TransportationService",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    transport_service_provider_party: TransportServiceProviderParty | None = field(
        default=None,
        metadata={
            "name": "TransportServiceProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
            "required": True,
        },
    )
    referenced_consignment: ReferencedConsignment | None = field(
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
    admission_code: AdmissionCode | None = field(
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
    resolution_date: ResolutionDate | None = field(
        default=None,
        metadata={
            "name": "ResolutionDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    resolution_time: ResolutionTime | None = field(
        default=None,
        metadata={
            "name": "ResolutionTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    procurement_project_lot: ProcurementProjectLot | None = field(
        default=None,
        metadata={
            "name": "ProcurementProjectLot",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )


@dataclass(frozen=True)
class TenderPreparationType:
    tender_envelope_id: TenderEnvelopeId | None = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    tender_envelope_type_code: TenderEnvelopeTypeCode | None = field(
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
    open_tender_id: OpenTenderId | None = field(
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
    variant_id: VariantId | None = field(
        default=None,
        metadata={
            "name": "VariantID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    fee_amount: FeeAmount | None = field(
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
    tender_envelope_id: TenderEnvelopeId | None = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeID",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    tender_envelope_type_code: TenderEnvelopeTypeCode | None = field(
        default=None,
        metadata={
            "name": "TenderEnvelopeTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    procurement_project_lot: ProcurementProjectLot | None = field(
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
    legal_monetary_total: LegalMonetaryTotal | None = field(
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
    main_qualifying_party: MainQualifyingParty | None = field(
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
    tender_result_code: TenderResultCode | None = field(
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
    advertisement_amount: AdvertisementAmount | None = field(
        default=None,
        metadata={
            "name": "AdvertisementAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    award_date: AwardDate | None = field(
        default=None,
        metadata={
            "name": "AwardDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            "required": True,
        },
    )
    award_time: AwardTime | None = field(
        default=None,
        metadata={
            "name": "AwardTime",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_tender_quantity: ReceivedTenderQuantity | None = field(
        default=None,
        metadata={
            "name": "ReceivedTenderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    lower_tender_amount: LowerTenderAmount | None = field(
        default=None,
        metadata={
            "name": "LowerTenderAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    higher_tender_amount: HigherTenderAmount | None = field(
        default=None,
        metadata={
            "name": "HigherTenderAmount",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    start_date: StartDate | None = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_electronic_tender_quantity: ReceivedElectronicTenderQuantity | None = field(
        default=None,
        metadata={
            "name": "ReceivedElectronicTenderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    received_foreign_tender_quantity: ReceivedForeignTenderQuantity | None = field(
        default=None,
        metadata={
            "name": "ReceivedForeignTenderQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    contract: Contract | None = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    awarded_tendered_project: AwardedTenderedProject | None = field(
        default=None,
        metadata={
            "name": "AwardedTenderedProject",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_formalization_period: ContractFormalizationPeriod | None = (
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
    awarding_method_type_code: AwardingMethodTypeCode | None = field(
        default=None,
        metadata={
            "name": "AwardingMethodTypeCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    price_evaluation_code: PriceEvaluationCode | None = field(
        default=None,
        metadata={
            "name": "PriceEvaluationCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    maximum_variant_quantity: MaximumVariantQuantity | None = field(
        default=None,
        metadata={
            "name": "MaximumVariantQuantity",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    variant_constraint_indicator: VariantConstraintIndicator | None = field(
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
    funding_program_code: FundingProgramCode | None = field(
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
    maximum_advertisement_amount: MaximumAdvertisementAmount | None = field(
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
    payment_frequency_code: PaymentFrequencyCode | None = field(
        default=None,
        metadata={
            "name": "PaymentFrequencyCode",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    economic_operator_registry_uri: EconomicOperatorRegistryUri | None = (
        field(
            default=None,
            metadata={
                "name": "EconomicOperatorRegistryURI",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    required_curricula_indicator: RequiredCurriculaIndicator | None = field(
        default=None,
        metadata={
            "name": "RequiredCurriculaIndicator",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
        },
    )
    other_conditions_indicator: OtherConditionsIndicator | None = field(
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
    latest_security_clearance_date: LatestSecurityClearanceDate | None = (
        field(
            default=None,
            metadata={
                "name": "LatestSecurityClearanceDate",
                "type": "Element",
                "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2",
            },
        )
    )
    documentation_fee_amount: DocumentationFeeAmount | None = field(
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
    procurement_legislation_document_reference: ProcurementLegislationDocumentReference | None = field(
        default=None,
        metadata={
            "name": "ProcurementLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    fiscal_legislation_document_reference: FiscalLegislationDocumentReference | None = field(
        default=None,
        metadata={
            "name": "FiscalLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    environmental_legislation_document_reference: EnvironmentalLegislationDocumentReference | None = field(
        default=None,
        metadata={
            "name": "EnvironmentalLegislationDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    employment_legislation_document_reference: EmploymentLegislationDocumentReference | None = field(
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
    call_for_tenders_document_reference: CallForTendersDocumentReference | None = field(
        default=None,
        metadata={
            "name": "CallForTendersDocumentReference",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    warranty_validity_period: WarrantyValidityPeriod | None = field(
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
    awarding_terms: AwardingTerms | None = field(
        default=None,
        metadata={
            "name": "AwardingTerms",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    additional_information_party: AdditionalInformationParty | None = field(
        default=None,
        metadata={
            "name": "AdditionalInformationParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    document_provider_party: DocumentProviderParty | None = field(
        default=None,
        metadata={
            "name": "DocumentProviderParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    tender_recipient_party: TenderRecipientParty | None = field(
        default=None,
        metadata={
            "name": "TenderRecipientParty",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_responsible_party: ContractResponsibleParty | None = field(
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
    tender_validity_period: TenderValidityPeriod | None = field(
        default=None,
        metadata={
            "name": "TenderValidityPeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    contract_acceptance_period: ContractAcceptancePeriod | None = field(
        default=None,
        metadata={
            "name": "ContractAcceptancePeriod",
            "type": "Element",
            "namespace": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        },
    )
    appeal_terms: AppealTerms | None = field(
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
    replaced_notice_document_reference: ReplacedNoticeDocumentReference | None = field(
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
