from travelport.models.air import (
    Advtype,
    Apisrequirements,
    ApisrequirementsList,
    AccountRelatedRules,
    ActionDetails,
    AdditionalInfo,
    AddlBookingCodeInformation,
    Adjustment,
    Affiliations,
    AirAvailInfo,
    AirBaseReq,
    AirExchangeBundle,
    AirExchangeBundleList,
    AirExchangeBundleTotal,
    AirExchangeEligibilityReq,
    AirExchangeEligibilityRsp,
    AirExchangeModifiers,
    AirExchangeMulitQuoteList,
    AirExchangeMultiQuoteOption,
    AirExchangeMultiQuoteReq,
    AirExchangeMultiQuoteRsp,
    AirExchangeQuoteReq,
    AirExchangeQuoteRsp,
    AirExchangeReq,
    AirExchangeRsp,
    AirExchangeTicketBundle,
    AirExchangeTicketingReq,
    AirExchangeTicketingRsp,
    AirFareDiscount,
    AirFareDisplayModifiers,
    AirFareDisplayReq,
    AirFareDisplayRsp,
    AirFareDisplayRuleKey,
    AirFareRuleCategory,
    AirFareRulesModifier,
    AirFareRulesReq,
    AirFareRulesRsp,
    AirItinerary,
    AirItineraryDetails,
    AirItinerarySolution,
    AirItinerarySolutionRef,
    AirLegModifiers,
    AirLegModifiersOrderBy,
    AirMerchandisingDetailsReq,
    AirMerchandisingDetailsRsp,
    AirMerchandisingOfferAvailabilityReq,
    AirMerchandisingOfferAvailabilityRsp,
    AirPrePayReq,
    AirPrePayRsp,
    AirPricePoint,
    AirPricePointList,
    AirPriceReq,
    AirPriceResult,
    AirPriceRsp,
    AirPricingAdjustment,
    AirPricingCommand,
    AirPricingInfo,
    AirPricingInfoList,
    AirPricingInfoRef,
    AirPricingModifiers,
    AirPricingPayment,
    AirPricingSolution,
    AirPricingSolutionItinerary,
    AirPricingTicketingModifiers,
    AirRefundBundle,
    AirRefundBundleRefundType,
    AirRefundInfo,
    AirRefundModifiers,
    AirRefundQuoteReq,
    AirRefundQuoteRsp,
    AirRefundReq,
    AirRefundRsp,
    AirRepriceReq,
    AirRepriceRsp,
    AirReservation,
    AirReservationLocatorCode,
    AirRetrieveDocumentReq,
    AirRetrieveDocumentRsp,
    AirScheduleChangedInfo,
    AirSearchAsynchModifiers,
    AirSearchModifiers,
    AirSearchModifiersOrderBy,
    AirSearchReq,
    AirSearchRsp,
    AirSegment,
    AirSegmentData,
    AirSegmentDetails,
    AirSegmentError,
    AirSegmentList,
    AirSegmentPricingModifiers,
    AirSegmentRef,
    AirSegmentSellFailureInfo,
    AirSegmentTicketingModifiers,
    AirSolution,
    AirSolutionChangedInfo,
    AirSolutionChangedInfoReasonCode,
    AirTicketingModifiers,
    AirTicketingReq,
    AirTicketingRsp,
    AirUpsellSearchReq,
    AirUpsellSearchRsp,
    AirVoidDocumentReq,
    AirVoidDocumentRsp,
    Alliance,
    AlternateLocationDistance,
    AlternateLocationDistanceList,
    AlternateLocationDistanceRef,
    AlternateRoute,
    AlternateRouteList,
    ApplicableSegment,
    AssociatedRemark,
    AsyncProviderSpecificResponse,
    AuditData,
    AutoPricingInfo,
    AutoSeatAssignment,
    AvailabilityErrorInfo,
    AvailabilitySearchReq,
    AvailabilitySearchRsp,
    AvailableDiscount,
    AvailableSsr,
    BackOfficeHandOff,
    BagDetails,
    BaggageAllowance,
    BaggageAllowanceInfo,
    BaggageAllowances,
    BaggageRestriction,
    BaseAirExchangeMultiQuoteReq,
    BaseAirExchangeQuoteReq,
    BaseAirPriceReq,
    BaseAirPriceRsp,
    BaseAirSearchReq,
    BaseAvailabilitySearchRsp,
    BaseBaggageAllowanceInfo,
    BaseLowFareSearchReq,
    BillingDetailItem,
    BookingCode,
    BookingCodeInfo,
    BookingInfo,
    BookingRules,
    BookingRulesFareReference,
    Brand,
    BrandId,
    BrandInfo,
    BrandList,
    BrandModifiers,
    BrandingInfo,
    BundledService,
    BundledServices,
    Chgtype,
    Co2Emission,
    Co2Emissions,
    CarrierCode,
    CarrierList,
    CarryOnAllowanceInfo,
    CategoryDetailsType,
    Characteristic as AirCharacteristic,
    ChargesRules,
    CodeshareInfo,
    CompanyName,
    ConjunctedTicketInfo,
    Connection,
    ContractCode,
    Coupon,
    CreditSummary,
    CustomerReceiptInfo,
    CustomerSearch,
    DefaultBrandDetail,
    DestinationPurposeCode,
    DetailedBillingInformation,
    Dimension,
    DirectionInfoDirection,
    Document,
    DocumentInfo,
    DocumentModifiers,
    DocumentOptions,
    DocumentRequired,
    DocumentSelect,
    Emd,
    Emdcommission,
    Emdcoupon,
    Emdendorsement,
    Emdinfo,
    EmdissuanceReq,
    EmdissuanceRsp,
    EmdpricingInfo,
    EmdretrieveReq,
    EmdretrieveRsp,
    Emdsummary,
    EmdsummaryInfo,
    EmdtravelerInfo,
    EmdAvailabilityChargeIndicator,
    EmdRefundReissueIndicator,
    Etr,
    ElectronicMiscDocument,
    Embargo,
    EmbargoInfo,
    EmbargoList,
    Enumeration,
    ExchangeAirSegment,
    ExchangeEligibilityInfo,
    ExchangePenaltyInfo,
    ExchangedTicketInfo,
    ExcludeTicketing,
    ExemptObfee,
    ExemptTaxes,
    ExpertSolution,
    ExpertSolutionList,
    Facility,
    FareBasis,
    FareCalc,
    FareDetails,
    FareDetailsRef,
    FareDisplay,
    FareDisplayRule,
    FareGuaranteeInfo,
    FareInfo,
    FareInfoList,
    FareInfoMessage,
    FareInfoRef,
    FareMileageInformation,
    FareNote,
    FareNoteList,
    FareNoteRef,
    FarePricing,
    FareRemark,
    FareRemarkList,
    FareRemarkRef,
    FareRestriction,
    FareRestrictionDate,
    FareRestrictionDateEndDateIndicator,
    FareRestrictionDaysOfWeek,
    FareRestrictionSaleDate,
    FareRestrictionSeasonal,
    FareRoutingInformation,
    FareRule,
    FareRuleCategory,
    FareRuleCategoryTypes,
    FareRuleFailureInfo,
    FareRuleKey,
    FareRuleLong,
    FareRuleLongRef,
    FareRuleLookup,
    FareRuleNameValue,
    FareRuleShort,
    FareRuleShortRef,
    FareRulesFilter,
    FareRulesFilterCategory,
    FareStatus,
    FareStatusFailureInfo,
    FareSurcharge,
    FareTicketDesignator,
    FareType,
    FaxDetails,
    FaxDetailsInformation,
    FeeApplication,
    FeeInfo,
    FlexExploreModifiers,
    FlexExploreModifiersType,
    FlightDetails,
    FlightDetailsList,
    FlightDetailsRef,
    FlightDetailsReq,
    FlightDetailsRsp,
    FlightInfo,
    FlightInfoCriteria,
    FlightInfoDetail,
    FlightInformationReq,
    FlightInformationRsp,
    FlightOption,
    FlightOptionsList,
    FlightTimeDetail,
    FlightTimeTableCriteria,
    FlightTimeTableReq,
    FlightTimeTableRsp,
    FlightType,
    GeneralTimeTable,
    GroupedOption,
    GroupedOptionInfo,
    HostReservation,
    HostTokenList as AirHostTokenList,
    ImageLocation,
    InFlightServices,
    IncludeAddlBookingCodeInfo,
    InvoluntaryChange,
    IssuanceModifiers,
    Itinerary,
    Journey,
    JourneyData,
    LandCharges,
    LanguageOption,
    Leg,
    LegDetail,
    LegPrice,
    LegRef,
    LowFareSearchAsynchReq,
    LowFareSearchAsynchRsp,
    LowFareSearchReq,
    LowFareSearchRsp,
    LoyaltyCardDetails,
    Maxtype,
    Mintype,
    ManualFareAdjustment,
    MaxLayoverDurationType,
    Meals,
    MerchandisingAvailabilityDetails,
    MerchandisingDetails,
    MerchandisingPricingModifiers,
    MultiGdssearchIndicator,
    Othtype,
    OfferAvailabilityModifiers,
    Option,
    OptionalService,
    OptionalServiceModifier,
    OptionalServiceModifiers,
    OptionalServiceRef,
    OptionalServices,
    OptionalServicesInfo,
    OriginalItineraryDetails,
    OverrideCode,
    Pcc,
    PassengerDetails,
    PassengerDetailsRef,
    PassengerReceiptOverride,
    PassengerSeatPrice,
    PassengerTicketNumber,
    PassengerType,
    PaymentRef as AirPaymentRef,
    PenFeeType,
    Penalty as AirPenalty,
    PenaltyFareInformation,
    PenaltyInformation,
    PermittedCabins,
    PermittedCarriers,
    PersonName,
    PersonNameSearch,
    PocketItineraryRemark,
    PolicyCodesList,
    PrePayAccount,
    PrePayCustomer,
    PrePayId,
    PrePayPriceInfo,
    PrePayProfileInfo,
    PreferredBookingCodes,
    PreferredCabins,
    PreferredCarriers,
    PriceChangeType,
    PriceRange,
    PricingDetails,
    PrintBlankFormItinerary,
    ProhibitedCabins,
    ProhibitedCarriers,
    PromoCode,
    RailCoachDetails,
    RefundFailureInfo,
    RelatedTraveler,
    RepricingModifiers,
    RepricingModifiersFlightType,
    Restriction as AirRestriction,
    RetrieveLowFareSearchReq,
    RetrieveLowFareSearchRsp,
    Route,
    RouteList,
    RoutingRules,
    Row,
    Rows,
    RuleAdvancedPurchase,
    RuleCharges,
    RuleLengthOfStay,
    Rules,
    ScheduleSearchReq,
    ScheduleSearchRsp,
    SearchAirLeg,
    SearchSpecificAirSegment,
    SearchTraveler,
    SeatInformation,
    SeatMapReq,
    SeatMapRsp,
    SegmentIndex,
    SegmentModifiers,
    SegmentSelect,
    SelectionModifiers,
    ServiceAssociations,
    ServiceGroup,
    ServiceSubGroup,
    SolutionGroup,
    SpecificSeatAssignment,
    SpecificTimeTable,
    SplitTicketingSearch,
    SponsoredFltInfo,
    StructuredFareRulesType,
    SvcSegment,
    Tcr,
    TcrexchangeBundle,
    Tcrinfo,
    TcrrefundBundle,
    TcrrefundBundleRefundType,
    Tax,
    TaxInfo,
    TermConditions,
    Text,
    TextInfo,
    Ticket,
    TicketAgency,
    TicketDesignator,
    TicketEndorsement,
    TicketFailureInfo,
    TicketInfo,
    TicketValidity,
    TicketingModifiers,
    TicketingModifiersRef,
    Title,
    TourCode,
    TravelArranger,
    Url,
    Urlinfo,
    UpsellBrand,
    ValueDetails,
    Variance,
    VoidDocumentInfo,
    VoidFailureInfo,
    VoidResultInfo,
    WaiverCode,
    YieldType,
    TypeAtpcoglobalIndicator,
    TypeAirReservationWithFop,
    TypeAlliance,
    TypeAnchorFlightData,
    TypeApplicableSegment,
    TypeAssessIndicator,
    TypeBackOffice,
    TypeBaseAirReservation,
    TypeBaseAirSegment,
    TypeBillingDetailsDataType,
    TypeBillingDetailsName,
    TypeBooking,
    TypeBulkTicketModifierType,
    TypeCarrierCode,
    TypeConnectionIndicator,
    TypeCouponStatus,
    TypeDaysOfOperation,
    TypeDefaultBrandDetail,
    TypeDestinationCode,
    TypeDisplayCategory,
    TypeDiversity,
    TypeEticketability,
    TypeFacility,
    TypeFailureInfo,
    TypeFareBreak,
    TypeFareDirectionality,
    TypeFareDiscount,
    TypeFareGuarantee,
    TypeFarePenalty,
    TypeFarePenaltyPenaltyApplies,
    TypeFareRestrictionType,
    TypeFareRuleCategoryCode,
    TypeFareRuleType,
    TypeFareSearchOption,
    TypeFareStatusCode,
    TypeFareTripType,
    TypeFaresIndicator,
    TypeIgnoreStopOver,
    TypeInventoryRequest,
    TypeItinerary,
    TypeItineraryOption,
    TypeMealService,
    TypeMileOrRouteBasedFare,
    TypeNativeSearchModifier,
    TypeNonAirReservationRef as AirTypeNonAirReservationRef,
    TypePosition,
    TypePricingMethod,
    TypePrivateFare,
    TypePurposeCode,
    TypeReportingType,
    TypeRestrictionLengthOfStay,
    TypeRowLocation,
    TypeSeatAvailability,
    TypeSegmentRef as AirTypeSegmentRef,
    TypeStayUnit,
    TypeTcrstatus,
    TypeTaxInfoWithPaymentRef,
    TypeTextElement,
    TypeTicketFailureInfo,
    TypeTicketModifierAccountingType,
    TypeTicketModifierAmountType,
    TypeTicketModifierPercentType,
    TypeTicketModifierValueType,
    TypeTicketingModifiersRef,
    TypeTripType,
    TypeUnitOfMeasure,
    TypeUnitWeight,
    TypeVarianceIndicator,
    TypeVarianceType,
    TypeWeight,
)
from travelport.models.common import (
    Apiprovider,
    Arcpayment,
    AccountCode,
    AccountInformation,
    AccountingRemark,
    ActionStatus,
    ActionStatusType,
    AddSvc,
    AddressRestriction,
    AgencyContactInfo,
    AgencyInfo,
    AgencyInformation,
    AgencyPayment,
    AgencySellInfo,
    AgentAction,
    AgentActionActionType,
    AgentIdoverride,
    AgentVoucher,
    AirExchangeInfo,
    AirSearchParameters,
    AirSeatAssignment,
    Airport,
    AppliedProfile,
    Auxdata,
    Bsppayment,
    BaseAsyncProviderSpecificResponse,
    BaseCoreReq,
    BaseCoreSearchReq,
    BaseCreateReservationReq,
    BaseCreateWithFormOfPaymentReq,
    BaseReq,
    BaseReservation,
    BaseRsp,
    BaseSearchReq,
    BaseSearchRsp,
    BillingPointOfSaleInfo,
    BookingDates,
    BookingSource,
    BookingSourceType,
    BookingTraveler,
    BookingTravelerInfo,
    BookingTravelerInformation,
    BookingTravelerName,
    BookingTravelerRef,
    CabinClass,
    CardRestriction,
    Carrier,
    Certificate,
    Characteristic as CommonCharacteristic,
    Check,
    City,
    CityOrAirport,
    Commission,
    CommissionRemark,
    ConnectionPoint,
    ConsolidatorRemark,
    ContinuityCheckOverride,
    CoordinateLocation,
    CorporateDiscountId,
    Credentials,
    CreditCard,
    CreditCardAuth,
    CustomProfileInformation,
    CustomerId,
    CustomizedNameData,
    DebitCard,
    DeliveryInfo,
    DirectPayment,
    DiscountCard,
    DiscountCardRef,
    Distance,
    DistanceUnits,
    DriversLicense,
    DriversLicenseRef,
    Email,
    EmailNotification,
    EmailNotificationRecipients,
    Endorsement,
    EnettVan,
    ErrorInfo,
    ExchangedCoupon,
    FileFinishingInfo,
    FormOfPayment,
    FormOfPaymentRef,
    FormattedTextTextType,
    FormattedTextTextTypeTextFormat,
    GeneralRemark,
    Group,
    Guarantee,
    GuaranteeType,
    HostToken,
    HostTokenList as CommonHostTokenList,
    IncludedInBase,
    IndustryStandardSsr,
    InvoiceData,
    InvoiceRemark,
    KeyMapping,
    Keyword,
    LinkedUniversalRecord,
    Location,
    LocationAddress,
    LocatorCode,
    LoyaltyCard,
    LoyaltyCardRef,
    LoyaltyProgram,
    Mco,
    McoexchangeInfo,
    McofeeInfo,
    McofeeInfoFeeAppliesToInd,
    Mcoinformation,
    McopriceData,
    Mcoremark,
    Mcotext,
    MarketingInformation,
    MealRequest,
    MediaItem,
    MetaData,
    MiscFormOfPayment,
    ModificationType,
    Name,
    NameOverride,
    NameRemark,
    NextResultReference,
    Osi,
    OperatedBy,
    OptionalServiceApplicabilityType,
    OptionalServiceApplicationLimitType,
    OptionalServicesTypeCodeGroupType,
    OtherGuaranteeInfo,
    OtherGuaranteeInfoType,
    OverridePcc,
    OwnershipChange,
    PassengerInfo,
    PassiveInfo,
    Payment,
    PaymentAdvice,
    PaymentRef as CommonPaymentRef,
    PaymentRestriction,
    PaymentType,
    Penalty as CommonPenalty,
    PermittedProviders,
    PersonalGeography,
    PhoneNumber,
    PhoneNumberType,
    PointOfCommencement,
    PointOfSale,
    PolicyInformation,
    Postscript,
    PriceMatchError,
    Provider,
    ProviderArnksegment,
    ProviderReservationDetail,
    ProviderReservationInfoRef,
    PseudoCityCode,
    QueuePlace,
    QueueSelector,
    RailLocation,
    RailSeatAssignment,
    ReferencePoint,
    RefundRemark,
    Remark,
    RequestKeyMappings,
    RequiredField,
    RequiredFieldName,
    Requisition,
    RequisitionCategory,
    RequisitionType,
    ReservationName,
    ResponseMessage,
    ResponseMessageType,
    Restriction as CommonRestriction,
    ReviewBooking,
    RoleInfo,
    Ssr,
    Ssrinfo,
    SearchEvent,
    SearchPassenger,
    SearchTicketing,
    SearchTicketingReservationStatus,
    SearchTicketingTicketStatus,
    SeatAssignment,
    SeatAttribute,
    SeatAttributes,
    Segment,
    SegmentRemark,
    SellMessage,
    ServiceData,
    ServiceFeeInfo,
    ServiceFeeTaxInfo,
    ServiceInfo,
    ServiceRuleType,
    ShopInformation,
    SimpleName,
    SpecialEquipment,
    State,
    StockControl,
    SupplierLocator,
    TaxDetail,
    TerminalSessionInfo,
    ThirdPartyInformation,
    TicketNumber,
    TransactionType,
    TravelComplianceData,
    TravelInfo,
    TravelSegment,
    TravelerInformation,
    TravelerType,
    UrticketStatus,
    UnassociatedRemark,
    UnitedNations,
    VendorLocation,
    Xmlremark,
    AttrDocumentDocumentType,
    AttrFlexShoppingTier,
    TypeAdjustmentTarget,
    TypeAdjustmentType,
    TypeAgencyHierarchyLongReference,
    TypeAgencyHierarchyReference,
    TypeAgencyPayment,
    TypeAgencyProfileLevel,
    TypeAgentInfo,
    TypeAssociatedRemark,
    TypeAssociatedRemarkWithSegmentRef,
    TypeBookingTransactionsAllowed,
    TypeCommissionLevel,
    TypeCommissionModifier,
    TypeCommissionType,
    TypeCreditCardType,
    TypeDateRange,
    TypeDirection,
    TypeDistance,
    TypeDoorCount,
    TypeElement,
    TypeElementStatus,
    TypeErrorInfo,
    TypeEventType,
    TypeFarePull,
    TypeFeeInfo,
    TypeFlexibleTimeSpec,
    TypeFormOfPaymentPnrreference,
    TypeFormOfRefund,
    TypeFuel,
    TypeFulfillmentIdtype,
    TypeFulfillmentType,
    TypeGeneralReference,
    TypeGuaranteeInformation,
    TypeGuaranteeInformationAgencyType,
    TypeGuaranteeInformationType,
    TypeImageSize,
    TypeInvoiceRecordCategory,
    TypeItineraryCode,
    TypeItineraryType,
    TypeKeyBasedReference,
    TypeKeyword,
    TypeLicenseCode,
    TypeLocation,
    TypeLoggingLevel,
    TypeMcofeeType,
    TypeMcostatus,
    TypeMcotype,
    TypeNonAirReservationRef as CommonTypeNonAirReservationRef,
    TypeOtakeyword,
    TypeOtasubKey,
    TypeOtherImageSize,
    TypePassengerType,
    TypePaymentCard,
    TypePolicy,
    TypePolicyCodesList,
    TypePriceClassOfService,
    TypePricingType,
    TypeProduct,
    TypeProfileApplicability,
    TypeProfileEntityStatus,
    TypeProfileEntityStatusWithDelete,
    TypeProfileLevel,
    TypeProfileLevelWithCredential,
    TypeProfileLevelWithSystem,
    TypeProfileRef,
    TypeProfileType,
    TypeProviderReservationDetail,
    TypeProviderReservationSpecificInfo,
    TypeProviderToken,
    TypePurchaseWindow,
    TypeQueueModifyAction,
    TypeRateCategory,
    TypeRateDescription,
    TypeRateGuarantee,
    TypeRateTimePeriod,
    TypeRecordStatus,
    TypeRemark,
    TypeRemarkWithTravelerRef,
    TypeReqSeat,
    TypeReserveRequirement,
    TypeResidency,
    TypeResponseImageSize,
    TypeResultMessage,
    TypeResultMessageType,
    TypeSearchLocation,
    TypeSearchTimeSpec,
    TypeSegmentRef as CommonTypeSegmentRef,
    TypeSource,
    TypeSpecificTime,
    TypeStatus,
    TypeStructuredAddress,
    TypeSubKey,
    TypeTax,
    TypeTaxInfo,
    TypeTicketStatus,
    TypeTimeRange,
    TypeTimeSpec,
    TypeTransactionsAllowed,
    TypeTrinary,
    TypeVehicleCategory,
    TypeVehicleClass,
    TypeVehicleLocation,
    TypeVehicleTransmission,
    TypeVendorLocation,
    TypeVoucherInformation,
    TypeVoucherType,
)
from travelport.models.rail import (
    Characteristic as RailCharacteristic,
    Coach,
    FareValidity,
    FulFillmentType,
    JourneyRemark,
    OperatingCompany,
    RailAutoSeatAssignment,
    RailAvailInfo,
    RailBookingInfo,
    RailExchangeInfo,
    RailExchangeSolution,
    RailFare,
    RailFareComponent,
    RailFareId,
    RailFareIdlist,
    RailFareIdref,
    RailFareList,
    RailFareNote,
    RailFareNoteList,
    RailFareNoteRef,
    RailFareRef,
    RailInfo,
    RailJourney,
    RailJourneyList,
    RailJourneyRef,
    RailLegModifiers,
    RailPricingInfo,
    RailPricingModifiers,
    RailPricingSolution,
    RailRefundInfo,
    RailReservation,
    RailSearchModifiers,
    RailSegment,
    RailSegmentInfo,
    RailSegmentList,
    RailSegmentRef,
    RailSolutionChangedInfo,
    RailSolutionChangedInfoReasonCode,
    RailSpecificSeatAssignment,
    RailSupplier,
    RailTicketInfo,
    SearchRailLeg,
    TicketAdvisory,
    TypeCoachClassType,
    TypeJourneyDirection,
    TypeRailDirection,
    TypeRailPricingSolution,
    TypeRailSegmentInfo,
    TypeRailTicketStatus,
    TypeResponseType,
    TypeTransportMode,
)
from travelport.models.services import (
    AirAvailabilitySearchPortTypeService,
    AirAvailabilitySearchPortTypeServiceInput,
    AirAvailabilitySearchPortTypeServiceOutput,
    AirExchangeEligibilityPortTypeService,
    AirExchangeEligibilityPortTypeServiceInput,
    AirExchangeEligibilityPortTypeServiceOutput,
    AirExchangeMultiQuotePortTypeService,
    AirExchangeMultiQuotePortTypeServiceInput,
    AirExchangeMultiQuotePortTypeServiceOutput,
    AirExchangeProcessPortTypeService,
    AirExchangeProcessPortTypeServiceInput,
    AirExchangeProcessPortTypeServiceOutput,
    AirExchangeQuotePortTypeService,
    AirExchangeQuotePortTypeServiceInput,
    AirExchangeQuotePortTypeServiceOutput,
    AirExchangeTicketingPortTypeService,
    AirExchangeTicketingPortTypeServiceInput,
    AirExchangeTicketingPortTypeServiceOutput,
    AirFareDisplayPortTypeService,
    AirFareDisplayPortTypeServiceInput,
    AirFareDisplayPortTypeServiceOutput,
    AirFareRulesPortTypeService,
    AirFareRulesPortTypeServiceInput,
    AirFareRulesPortTypeServiceOutput,
    AirLowFareSearchAsynchPortTypeService,
    AirLowFareSearchAsynchPortTypeServiceInput,
    AirLowFareSearchAsynchPortTypeServiceOutput,
    AirLowFareSearchPortTypeService,
    AirLowFareSearchPortTypeServiceInput,
    AirLowFareSearchPortTypeServiceOutput,
    AirMerchandisingDetailsPortTypeService,
    AirMerchandisingDetailsPortTypeServiceInput,
    AirMerchandisingDetailsPortTypeServiceOutput,
    AirMerchandisingOfferAvailabilityPortTypeService,
    AirMerchandisingOfferAvailabilityPortTypeServiceInput,
    AirMerchandisingOfferAvailabilityPortTypeServiceOutput,
    AirPrePayPortTypeService,
    AirPrePayPortTypeServiceInput,
    AirPrePayPortTypeServiceOutput,
    AirPricePortTypeService,
    AirPricePortTypeServiceInput,
    AirPricePortTypeServiceOutput,
    AirRefundQuotePortTypeService,
    AirRefundQuotePortTypeServiceInput,
    AirRefundQuotePortTypeServiceOutput,
    AirRefundTicketPortTypeService,
    AirRefundTicketPortTypeServiceInput,
    AirRefundTicketPortTypeServiceOutput,
    AirRepriceSearchPortTypeService,
    AirRepriceSearchPortTypeServiceInput,
    AirRepriceSearchPortTypeServiceOutput,
    AirRetrieveDocumentPortTypeService,
    AirRetrieveDocumentPortTypeServiceInput,
    AirRetrieveDocumentPortTypeServiceOutput,
    AirRetrieveLowFareSearchPortTypeService,
    AirRetrieveLowFareSearchPortTypeServiceInput,
    AirRetrieveLowFareSearchPortTypeServiceOutput,
    AirScheduleSearchPortTypeService,
    AirScheduleSearchPortTypeServiceInput,
    AirScheduleSearchPortTypeServiceOutput,
    AirTicketingPortTypeService,
    AirTicketingPortTypeServiceInput,
    AirTicketingPortTypeServiceOutput,
    AirUpsellSearchPortTypeService,
    AirUpsellSearchPortTypeServiceInput,
    AirUpsellSearchPortTypeServiceOutput,
    AirVoidDocumentPortTypeService,
    AirVoidDocumentPortTypeServiceInput,
    AirVoidDocumentPortTypeServiceOutput,
    EmdissuancePortTypeService,
    EmdissuancePortTypeServiceInput,
    EmdissuancePortTypeServiceOutput,
    EmdretrievePortTypeService,
    EmdretrievePortTypeServiceInput,
    EmdretrievePortTypeServiceOutput,
    FlightDetailsPortTypeService,
    FlightDetailsPortTypeServiceInput,
    FlightDetailsPortTypeServiceOutput,
    FlightInfoPortTypeService,
    FlightInfoPortTypeServiceInput,
    FlightInfoPortTypeServiceOutput,
    FlightTimeTablePortTypeService,
    FlightTimeTablePortTypeServiceInput,
    FlightTimeTablePortTypeServiceOutput,
    SeatMapPortTypeService,
    SeatMapPortTypeServiceInput,
    SeatMapPortTypeServiceOutput,
)
from travelport.models.session import SessionContext
