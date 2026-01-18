from __future__ import annotations

from dataclasses import dataclass

from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    AmountType as UblUnqualifiedDataTypes21AmountType,
)
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    BinaryObjectType,
    CodeType,
    IdentifierType,
    IndicatorType,
    NumericType,
    TimeType,
)
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    DateType as UblUnqualifiedDataTypes21DateType,
)
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    MeasureType as UblUnqualifiedDataTypes21MeasureType,
)
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    NameType as UblUnqualifiedDataTypes21NameType,
)
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    PercentType as UblUnqualifiedDataTypes21PercentType,
)
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    QuantityType as UblUnqualifiedDataTypes21QuantityType,
)
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    RateType as UblUnqualifiedDataTypes21RateType,
)
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    TextType as UblUnqualifiedDataTypes21TextType,
)

__NAMESPACE__ = (
    "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
)


@dataclass(frozen=True, kw_only=True)
class AcceptedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class AcceptedVariantsDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class AccountFormatCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AccountIdtype(IdentifierType):
    class Meta:
        name = "AccountIDType"


@dataclass(frozen=True, kw_only=True)
class AccountTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AccountingCostCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AccountingCostType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActivityTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActivityTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActualDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActualDeliveryTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActualDespatchDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActualDespatchTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActualPickupDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActualPickupTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ActualTemperatureReductionQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True, kw_only=True)
class AdValoremIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class AdditionalAccountIdtype(IdentifierType):
    class Meta:
        name = "AdditionalAccountIDType"


@dataclass(frozen=True, kw_only=True)
class AdditionalConditionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class AdditionalInformationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class AdditionalStreetNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class AddressFormatCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AddressTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AdjustmentReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AdmissionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AdvertisementAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class AgencyIdtype(IdentifierType):
    class Meta:
        name = "AgencyIDType"


@dataclass(frozen=True, kw_only=True)
class AgencyNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class AirFlowPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class AircraftIdtype(IdentifierType):
    class Meta:
        name = "AircraftIDType"


@dataclass(frozen=True, kw_only=True)
class AliasNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class AllowanceChargeReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AllowanceChargeReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class AllowanceTotalAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class AltitudeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class AmountRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True, kw_only=True)
class AmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class AnimalFoodApprovedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class AnimalFoodIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class AnnualAverageAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class ApplicationStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ApprovalDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ApprovalStatusType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class AttributeIdtype(IdentifierType):
    class Meta:
        name = "AttributeIDType"


@dataclass(frozen=True, kw_only=True)
class AuctionConstraintIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class AuctionUritype(IdentifierType):
    class Meta:
        name = "AuctionURIType"


@dataclass(frozen=True, kw_only=True)
class AvailabilityDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class AvailabilityStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AverageAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class AverageSubsequentContractAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class AwardDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class AwardTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AwardingCriterionDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class AwardingCriterionIdtype(IdentifierType):
    class Meta:
        name = "AwardingCriterionIDType"


@dataclass(frozen=True, kw_only=True)
class AwardingCriterionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class AwardingMethodTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class BackOrderAllowedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class BackorderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class BackorderReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class BalanceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class BalanceBroughtForwardIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class BarcodeSymbologyIdtype(IdentifierType):
    class Meta:
        name = "BarcodeSymbologyIDType"


@dataclass(frozen=True, kw_only=True)
class BaseAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class BaseQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class BaseUnitMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class BasedOnConsensusIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class BasicConsumedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class BatchQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class BestBeforeDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class BindingOnBuyerIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class BirthDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class BirthplaceNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class BlockNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class BrandNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class BrokerAssignedIdtype(IdentifierType):
    class Meta:
        name = "BrokerAssignedIDType"


@dataclass(frozen=True, kw_only=True)
class BudgetYearNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class BuildingNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class BuildingNumberType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class BulkCargoIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class BusinessClassificationEvidenceIdtype(IdentifierType):
    class Meta:
        name = "BusinessClassificationEvidenceIDType"


@dataclass(frozen=True, kw_only=True)
class BusinessIdentityEvidenceIdtype(IdentifierType):
    class Meta:
        name = "BusinessIdentityEvidenceIDType"


@dataclass(frozen=True, kw_only=True)
class BuyerEventIdtype(IdentifierType):
    class Meta:
        name = "BuyerEventIDType"


@dataclass(frozen=True, kw_only=True)
class BuyerProfileUritype(IdentifierType):
    class Meta:
        name = "BuyerProfileURIType"


@dataclass(frozen=True, kw_only=True)
class BuyerReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class Cv2Idtype(IdentifierType):
    class Meta:
        name = "CV2IDType"


@dataclass(frozen=True, kw_only=True)
class CalculationExpressionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CalculationExpressionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CalculationMethodCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CalculationRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True, kw_only=True)
class CalculationSequenceNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class CallBaseAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class CallDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class CallExtensionAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class CallTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CancellationNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CandidateReductionConstraintIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class CandidateStatementType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CanonicalizationMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CapabilityTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CardChipCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CardTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CargoTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CarrierAssignedIdtype(IdentifierType):
    class Meta:
        name = "CarrierAssignedIDType"


@dataclass(frozen=True, kw_only=True)
class CarrierServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CatalogueIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class CategoryNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class CertificateTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CertificateTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ChangeConditionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ChannelCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ChannelType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CharacterSetCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CharacteristicsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ChargeIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ChargeTotalAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class ChargeableQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ChargeableWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class ChildConsignmentQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ChipApplicationIdtype(IdentifierType):
    class Meta:
        name = "ChipApplicationIDType"


@dataclass(frozen=True, kw_only=True)
class CityNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class CitySubdivisionNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class CodeValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CollaborationPriorityCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CommentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CommodityCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CompanyIdtype(IdentifierType):
    class Meta:
        name = "CompanyIDType"


@dataclass(frozen=True, kw_only=True)
class CompanyLegalFormCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CompanyLegalFormType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CompanyLiquidationStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ComparedValueMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class ComparisonDataCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ComparisonDataSourceCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ComparisonForecastIssueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ComparisonForecastIssueTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CompletionIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConditionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConditionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConditionsDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConditionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsigneeAssignedIdtype(IdentifierType):
    class Meta:
        name = "ConsigneeAssignedIDType"


@dataclass(frozen=True, kw_only=True)
class ConsignmentQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsignorAssignedIdtype(IdentifierType):
    class Meta:
        name = "ConsignorAssignedIDType"


@dataclass(frozen=True, kw_only=True)
class ConsolidatableIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConstitutionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumerIncentiveTacticTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumerUnitQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumersEnergyLevelCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumersEnergyLevelType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumptionEnergyQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumptionIdtype(IdentifierType):
    class Meta:
        name = "ConsumptionIDType"


@dataclass(frozen=True, kw_only=True)
class ConsumptionLevelCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumptionLevelType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumptionReportIdtype(IdentifierType):
    class Meta:
        name = "ConsumptionReportIDType"


@dataclass(frozen=True, kw_only=True)
class ConsumptionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumptionTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ConsumptionWaterQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ContainerizedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ContentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ContentUnitQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ContractFolderIdtype(IdentifierType):
    class Meta:
        name = "ContractFolderIDType"


@dataclass(frozen=True, kw_only=True)
class ContractNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ContractSubdivisionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ContractTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ContractTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ContractedCarrierAssignedIdtype(IdentifierType):
    class Meta:
        name = "ContractedCarrierAssignedIDType"


@dataclass(frozen=True, kw_only=True)
class ContractingSystemCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CoordinateSystemCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CopyIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class CorporateRegistrationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CorporateStockAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class CorrectionAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class CorrectionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CorrectionTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CorrectionUnitAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class CountrySubentityCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CountrySubentityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CreditLineAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class CreditNoteTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CreditedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class CrewQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class CurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CurrentChargeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CurrentChargeTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CustomerAssignedAccountIdtype(IdentifierType):
    class Meta:
        name = "CustomerAssignedAccountIDType"


@dataclass(frozen=True, kw_only=True)
class CustomerReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class CustomizationIdtype(IdentifierType):
    class Meta:
        name = "CustomizationIDType"


@dataclass(frozen=True, kw_only=True)
class CustomsClearanceServiceInstructionsType(
    UblUnqualifiedDataTypes21TextType
):
    pass


@dataclass(frozen=True, kw_only=True)
class CustomsImportClassifiedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class CustomsStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class CustomsTariffQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class DamageRemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DangerousGoodsApprovedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class DataSendingCapabilityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DataSourceCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class DebitLineAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class DebitedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class DeclarationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DeclaredCarriageValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class DeclaredCustomsValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class DeclaredForCarriageValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class DeclaredStatisticsValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class DeliveredQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class DeliveryInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DemurrageInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DepartmentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DescriptionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DespatchAdviceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DifferenceTemperatureReductionQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True, kw_only=True)
class DirectionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DisplayTacticTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DispositionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DistrictType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DocumentCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DocumentDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DocumentHashType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DocumentIdtype(IdentifierType):
    class Meta:
        name = "DocumentIDType"


@dataclass(frozen=True, kw_only=True)
class DocumentStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DocumentStatusReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DocumentStatusReasonDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DocumentTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DocumentTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class DocumentationFeeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class DueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class DurationMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class DutyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class DutyType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class EarliestPickupDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class EarliestPickupTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class EconomicOperatorRegistryUritype(IdentifierType):
    class Meta:
        name = "EconomicOperatorRegistryURIType"


@dataclass(frozen=True, kw_only=True)
class EffectiveDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class EffectiveTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ElectronicDeviceDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ElectronicMailType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class EmbeddedDocumentBinaryObjectType(BinaryObjectType):
    pass


@dataclass(frozen=True, kw_only=True)
class EmergencyProceduresCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class EmployeeQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class EncodingCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class EndDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class EndTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class EndpointIdtype(IdentifierType):
    class Meta:
        name = "EndpointIDType"


@dataclass(frozen=True, kw_only=True)
class EnvironmentalEmissionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class EstimatedAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class EstimatedConsumedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class EstimatedDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class EstimatedDeliveryTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class EstimatedDespatchDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class EstimatedDespatchTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class EstimatedOverallContractAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class EstimatedOverallContractQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True, kw_only=True)
class EvaluationCriterionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class EvidenceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExceptionResolutionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExceptionStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExchangeMarketIdtype(IdentifierType):
    class Meta:
        name = "ExchangeMarketIDType"


@dataclass(frozen=True, kw_only=True)
class ExclusionReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExecutionRequirementCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExemptionReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExemptionReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExpectedOperatorQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExpectedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExpenseCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExpiryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExpiryTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExpressionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExpressionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ExtendedIdtype(IdentifierType):
    class Meta:
        name = "ExtendedIDType"


@dataclass(frozen=True, kw_only=True)
class ExtensionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class FaceValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class FamilyNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class FeatureTacticTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class FeeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class FeeDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class FileNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class FinancingInstrumentCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class FirstNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class FirstShipmentAvailibilityDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class FloorType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class FollowupContractIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ForecastPurposeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ForecastTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class FormatCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ForwarderServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class FreeOfChargeIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class FreeOnBoardValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class FreightForwarderAssignedIdtype(IdentifierType):
    class Meta:
        name = "FreightForwarderAssignedIDType"


@dataclass(frozen=True, kw_only=True)
class FreightRateClassCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class FrequencyType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class FrozenDocumentIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class FrozenPeriodDaysNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class FullnessIndicationCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class FullyPaidSharesIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class FundingProgramCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class FundingProgramType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class GasPressureQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class GenderCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class GeneralCargoIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class GovernmentAgreementConstraintIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class GrossTonnageMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class GrossVolumeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class GrossWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class GuaranteeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class GuaranteedDespatchDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class GuaranteedDespatchTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class HandlingCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class HandlingInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class HashAlgorithmMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class HaulageInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class HazardClassIdtype(IdentifierType):
    class Meta:
        name = "HazardClassIDType"


@dataclass(frozen=True, kw_only=True)
class HazardousCategoryCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class HazardousRegulationCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class HazardousRiskIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class HeatingTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class HeatingTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class HigherTenderAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class HolderNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class HumanFoodApprovedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class HumanFoodIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class HumidityPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class Idtype(IdentifierType):
    class Meta:
        name = "IDType"


@dataclass(frozen=True, kw_only=True)
class IdentificationCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class IdentificationIdtype(IdentifierType):
    class Meta:
        name = "IdentificationIDType"


@dataclass(frozen=True, kw_only=True)
class ImmobilizationCertificateIdtype(IdentifierType):
    class Meta:
        name = "ImmobilizationCertificateIDType"


@dataclass(frozen=True, kw_only=True)
class ImportanceCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class IndicationIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class IndustryClassificationCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class InformationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class InformationUritype(IdentifierType):
    class Meta:
        name = "InformationURIType"


@dataclass(frozen=True, kw_only=True)
class InhalationToxicityZoneCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class InhouseMailType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class InspectionMethodCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class InstallmentDueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class InstructionIdtype(IdentifierType):
    class Meta:
        name = "InstructionIDType"


@dataclass(frozen=True, kw_only=True)
class InstructionNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class InstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class InsurancePremiumAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class InsuranceValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class InventoryValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class InvoiceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class InvoicedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class InvoicingPartyReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class IssueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class IssueNumberIdtype(IdentifierType):
    class Meta:
        name = "IssueNumberIDType"


@dataclass(frozen=True, kw_only=True)
class IssueTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class IssuerIdtype(IdentifierType):
    class Meta:
        name = "IssuerIDType"


@dataclass(frozen=True, kw_only=True)
class ItemClassificationCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ItemUpdateRequestIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class JobTitleType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class JourneyIdtype(IdentifierType):
    class Meta:
        name = "JourneyIDType"


@dataclass(frozen=True, kw_only=True)
class JustificationDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class JustificationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class KeywordType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class LanguageIdtype(IdentifierType):
    class Meta:
        name = "LanguageIDType"


@dataclass(frozen=True, kw_only=True)
class LastRevisionDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class LastRevisionTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestDeliveryTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestMeterQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestMeterReadingDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestMeterReadingMethodCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestMeterReadingMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestPickupDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestPickupTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestProposalAcceptanceDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatestSecurityClearanceDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatitudeDegreesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatitudeDirectionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LatitudeMinutesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class LeadTimeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class LegalReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class LegalStatusIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class LiabilityAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class LicensePlateIdtype(IdentifierType):
    class Meta:
        name = "LicensePlateIDType"


@dataclass(frozen=True, kw_only=True)
class LifeCycleStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LimitationDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class LineCountNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class LineExtensionAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class LineIdtype(IdentifierType):
    class Meta:
        name = "LineIDType"


@dataclass(frozen=True, kw_only=True)
class LineNumberNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class LineStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LineType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ListValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class LivestockIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class LoadingLengthMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class LoadingSequenceIdtype(IdentifierType):
    class Meta:
        name = "LoadingSequenceIDType"


@dataclass(frozen=True, kw_only=True)
class LocaleCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LocationIdtype(IdentifierType):
    class Meta:
        name = "LocationIDType"


@dataclass(frozen=True, kw_only=True)
class LocationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class LocationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LoginType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class LogoReferenceIdtype(IdentifierType):
    class Meta:
        name = "LogoReferenceIDType"


@dataclass(frozen=True, kw_only=True)
class LongitudeDegreesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class LongitudeDirectionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LongitudeMinutesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class LossRiskResponsibilityCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class LossRiskType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class LotNumberIdtype(IdentifierType):
    class Meta:
        name = "LotNumberIDType"


@dataclass(frozen=True, kw_only=True)
class LowTendersDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class LowerOrangeHazardPlacardIdtype(IdentifierType):
    class Meta:
        name = "LowerOrangeHazardPlacardIDType"


@dataclass(frozen=True, kw_only=True)
class LowerTenderAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class MandateTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ManufactureDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ManufactureTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class MarkAttentionIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class MarkAttentionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MarkCareIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class MarkCareType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MarketValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class MarkingIdtype(IdentifierType):
    class Meta:
        name = "MarkingIDType"


@dataclass(frozen=True, kw_only=True)
class MathematicOperatorCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumAdvertisementAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumBackorderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumCopiesNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumNumberNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumOperatorQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumOrderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumPaidAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumPaymentInstructionsNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MaximumVariantQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class MedicalFirstAidGuideCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class MeterConstantCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class MeterConstantType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MeterNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MeterNumberType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MeterReadingCommentsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MeterReadingTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class MeterReadingTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MiddleNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class MimeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumBackorderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumImprovementBidType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumInventoryQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumNumberNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumOrderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MinimumValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MiscellaneousEventTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ModelNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class MonetaryScopeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MovieTitleType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class MultipleOrderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class MultiplierFactorNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class NameCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class NameSuffixType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class NameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class NationalityIdtype(IdentifierType):
    class Meta:
        name = "NationalityIDType"


@dataclass(frozen=True, kw_only=True)
class NatureCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class NegotiationDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class NetNetWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class NetTonnageMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class NetVolumeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class NetWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class NetworkIdtype(IdentifierType):
    class Meta:
        name = "NetworkIDType"


@dataclass(frozen=True, kw_only=True)
class NominationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class NominationTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class NormalTemperatureReductionQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True, kw_only=True)
class NoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class NotificationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class OccurrenceDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class OccurrenceTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class OnCarriageIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class OneTimeChargeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class OneTimeChargeTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class OntologyUritype(IdentifierType):
    class Meta:
        name = "OntologyURIType"


@dataclass(frozen=True, kw_only=True)
class OpenTenderIdtype(IdentifierType):
    class Meta:
        name = "OpenTenderIDType"


@dataclass(frozen=True, kw_only=True)
class OperatingYearsQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class OptionalLineItemIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class OptionsDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class OrderIntervalDaysNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class OrderQuantityIncrementNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class OrderResponseCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class OrderTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class OrderableIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class OrderableUnitFactorRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True, kw_only=True)
class OrderableUnitType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class OrganizationDepartmentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class OriginalContractingSystemIdtype(IdentifierType):
    class Meta:
        name = "OriginalContractingSystemIDType"


@dataclass(frozen=True, kw_only=True)
class OriginalJobIdtype(IdentifierType):
    class Meta:
        name = "OriginalJobIDType"


@dataclass(frozen=True, kw_only=True)
class OtherConditionsIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class OtherInstructionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class OtherNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class OutstandingQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class OutstandingReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class OversupplyQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class OwnerTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PackLevelCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PackQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class PackSizeNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class PackageLevelCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PackagingTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PackingCriteriaCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PackingMaterialType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaidAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaidDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaidTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ParentDocumentIdtype(IdentifierType):
    class Meta:
        name = "ParentDocumentIDType"


@dataclass(frozen=True, kw_only=True)
class ParentDocumentLineReferenceIdtype(IdentifierType):
    class Meta:
        name = "ParentDocumentLineReferenceIDType"


@dataclass(frozen=True, kw_only=True)
class ParentDocumentTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ParentDocumentVersionIdtype(IdentifierType):
    class Meta:
        name = "ParentDocumentVersionIDType"


@dataclass(frozen=True, kw_only=True)
class PartPresentationCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PartecipationPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class PartialDeliveryIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ParticipationPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class PartyCapacityAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class PartyTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PartyTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PassengerQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class PasswordType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PayPerViewType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PayableAlternativeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class PayableAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class PayableRoundingAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class PayerReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentAlternativeCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentChannelCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentDueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentFrequencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentIdtype(IdentifierType):
    class Meta:
        name = "PaymentIDType"


@dataclass(frozen=True, kw_only=True)
class PaymentMeansCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentMeansIdtype(IdentifierType):
    class Meta:
        name = "PaymentMeansIDType"


@dataclass(frozen=True, kw_only=True)
class PaymentNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentOrderReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentPurposeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PaymentTermsDetailsUritype(IdentifierType):
    class Meta:
        name = "PaymentTermsDetailsURIType"


@dataclass(frozen=True, kw_only=True)
class PenaltyAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class PenaltySurchargePercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class PerUnitAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class PercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class PerformanceMetricTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PerformanceValueQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class PerformingCarrierAssignedIdtype(IdentifierType):
    class Meta:
        name = "PerformingCarrierAssignedIDType"


@dataclass(frozen=True, kw_only=True)
class PersonalSituationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PhoneNumberType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PlacardEndorsementType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PlacardNotationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PlannedDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class PlotIdentificationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PositionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PostEventNotificationDurationMeasureType(
    UblUnqualifiedDataTypes21MeasureType
):
    pass


@dataclass(frozen=True, kw_only=True)
class PostalZoneType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PostboxType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PowerIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class PreCarriageIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class PreEventNotificationDurationMeasureType(
    UblUnqualifiedDataTypes21MeasureType
):
    pass


@dataclass(frozen=True, kw_only=True)
class PreferenceCriterionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PrepaidAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class PrepaidIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class PrepaidPaymentReferenceIdtype(IdentifierType):
    class Meta:
        name = "PrepaidPaymentReferenceIDType"


@dataclass(frozen=True, kw_only=True)
class PreviousCancellationReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PreviousJobIdtype(IdentifierType):
    class Meta:
        name = "PreviousJobIDType"


@dataclass(frozen=True, kw_only=True)
class PreviousMeterQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class PreviousMeterReadingDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class PreviousMeterReadingMethodCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PreviousMeterReadingMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PreviousVersionIdtype(IdentifierType):
    class Meta:
        name = "PreviousVersionIDType"


@dataclass(frozen=True, kw_only=True)
class PriceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class PriceChangeReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PriceEvaluationCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PriceRevisionFormulaDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PriceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PriceTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PricingCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PricingUpdateRequestIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class PrimaryAccountNumberIdtype(IdentifierType):
    class Meta:
        name = "PrimaryAccountNumberIDType"


@dataclass(frozen=True, kw_only=True)
class PrintQualifierType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PriorityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PrivacyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PrizeDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class PrizeIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ProcedureCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ProcessDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ProcessReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ProcessReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ProcurementSubTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ProcurementTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ProductTraceIdtype(IdentifierType):
    class Meta:
        name = "ProductTraceIDType"


@dataclass(frozen=True, kw_only=True)
class ProfileExecutionIdtype(IdentifierType):
    class Meta:
        name = "ProfileExecutionIDType"


@dataclass(frozen=True, kw_only=True)
class ProfileIdtype(IdentifierType):
    class Meta:
        name = "ProfileIDType"


@dataclass(frozen=True, kw_only=True)
class ProfileStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ProgressPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class PromotionalEventTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ProviderTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PublishAwardIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class PurposeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class PurposeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class QualityControlCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class QuantityDiscrepancyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class QuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class RadioCallSignIdtype(IdentifierType):
    class Meta:
        name = "RadioCallSignIDType"


@dataclass(frozen=True, kw_only=True)
class RailCarIdtype(IdentifierType):
    class Meta:
        name = "RailCarIDType"


@dataclass(frozen=True, kw_only=True)
class RankType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class RateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReceiptAdviceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReceivedDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReceivedElectronicTenderQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True, kw_only=True)
class ReceivedForeignTenderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReceivedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReceivedTenderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReferenceDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReferenceEventCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReferenceIdtype(IdentifierType):
    class Meta:
        name = "ReferenceIDType"


@dataclass(frozen=True, kw_only=True)
class ReferenceTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReferencedConsignmentIdtype(IdentifierType):
    class Meta:
        name = "ReferencedConsignmentIDType"


@dataclass(frozen=True, kw_only=True)
class RefrigeratedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class RefrigerationOnIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class RegionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class RegisteredDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class RegisteredTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RegistrationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class RegistrationExpirationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class RegistrationIdtype(IdentifierType):
    class Meta:
        name = "RegistrationIDType"


@dataclass(frozen=True, kw_only=True)
class RegistrationNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class RegistrationNationalityIdtype(IdentifierType):
    class Meta:
        name = "RegistrationNationalityIDType"


@dataclass(frozen=True, kw_only=True)
class RegistrationNationalityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class RegulatoryDomainType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class RejectActionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RejectReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RejectReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class RejectedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class RejectionNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReleaseIdtype(IdentifierType):
    class Meta:
        name = "ReleaseIDType"


@dataclass(frozen=True, kw_only=True)
class ReliabilityPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class RemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReminderSequenceNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReminderTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReplenishmentOwnerDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class RequestForQuotationLineIdtype(IdentifierType):
    class Meta:
        name = "RequestForQuotationLineIDType"


@dataclass(frozen=True, kw_only=True)
class RequestedDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class RequestedDespatchDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class RequestedDespatchTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RequestedInvoiceCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RequestedPublicationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class RequiredCurriculaIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class RequiredCustomsIdtype(IdentifierType):
    class Meta:
        name = "RequiredCustomsIDType"


@dataclass(frozen=True, kw_only=True)
class RequiredDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class RequiredDeliveryTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RequiredFeeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResidenceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResidenceTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResidentOccupantsNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResolutionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResolutionDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResolutionTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResolutionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResponseCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResponseDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ResponseTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RetailEventNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class RetailEventStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReturnabilityIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReturnableMaterialIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ReturnableQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class RevisedForecastLineIdtype(IdentifierType):
    class Meta:
        name = "RevisedForecastLineIDType"


@dataclass(frozen=True, kw_only=True)
class RevisionDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class RevisionStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RevisionTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RoamingPartnerNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class RoleCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class RoleDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class RoomType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class RoundingAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class SalesOrderIdtype(IdentifierType):
    class Meta:
        name = "SalesOrderIDType"


@dataclass(frozen=True, kw_only=True)
class SalesOrderLineIdtype(IdentifierType):
    class Meta:
        name = "SalesOrderLineIDType"


@dataclass(frozen=True, kw_only=True)
class SchemeUritype(IdentifierType):
    class Meta:
        name = "SchemeURIType"


@dataclass(frozen=True, kw_only=True)
class SealIssuerTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SealStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SealingPartyTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class SecurityClassificationCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SecurityIdtype(IdentifierType):
    class Meta:
        name = "SecurityIDType"


@dataclass(frozen=True, kw_only=True)
class SellerEventIdtype(IdentifierType):
    class Meta:
        name = "SellerEventIDType"


@dataclass(frozen=True, kw_only=True)
class SequenceIdtype(IdentifierType):
    class Meta:
        name = "SequenceIDType"


@dataclass(frozen=True, kw_only=True)
class SequenceNumberIdtype(IdentifierType):
    class Meta:
        name = "SequenceNumberIDType"


@dataclass(frozen=True, kw_only=True)
class SequenceNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class SerialIdtype(IdentifierType):
    class Meta:
        name = "SerialIDType"


@dataclass(frozen=True, kw_only=True)
class ServiceInformationPreferenceCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ServiceNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class ServiceNumberCalledType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ServiceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ServiceTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class SettlementDiscountAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class SettlementDiscountPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class SharesNumberQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ShippingMarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ShippingOrderIdtype(IdentifierType):
    class Meta:
        name = "ShippingOrderIDType"


@dataclass(frozen=True, kw_only=True)
class ShippingPriorityLevelCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ShipsRequirementsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ShortQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ShortageActionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SignatureIdtype(IdentifierType):
    class Meta:
        name = "SignatureIDType"


@dataclass(frozen=True, kw_only=True)
class SignatureMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class SizeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SoleProprietorshipIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class SourceCurrencyBaseRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True, kw_only=True)
class SourceCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SourceForecastIssueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class SourceForecastIssueTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SourceValueMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class SpecialInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class SpecialSecurityIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class SpecialServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class SpecialTermsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class SpecialTransportRequirementsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class SpecificationIdtype(IdentifierType):
    class Meta:
        name = "SpecificationIDType"


@dataclass(frozen=True, kw_only=True)
class SpecificationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SplitConsignmentIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class StartDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class StartTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class StatementTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class StatusAvailableIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class StatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class StatusReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class StatusReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class StreetNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class SubcontractingConditionsCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SubmissionDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class SubmissionDueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class SubmissionMethodCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SubscriberIdtype(IdentifierType):
    class Meta:
        name = "SubscriberIDType"


@dataclass(frozen=True, kw_only=True)
class SubscriberTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SubscriberTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class SubstitutionStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class SuccessiveSequenceIdtype(IdentifierType):
    class Meta:
        name = "SuccessiveSequenceIDType"


@dataclass(frozen=True, kw_only=True)
class SummaryDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class SupplierAssignedAccountIdtype(IdentifierType):
    class Meta:
        name = "SupplierAssignedAccountIDType"


@dataclass(frozen=True, kw_only=True)
class SupplyChainActivityTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TareWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class TargetCurrencyBaseRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True, kw_only=True)
class TargetCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TargetInventoryQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class TargetServicePercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class TariffClassCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TariffCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TariffDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxEnergyAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxEnergyBalanceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxEnergyOnAccountAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxEvidenceIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxExclusiveAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxExemptionReasonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxExemptionReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxIncludedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxInclusiveAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxLevelCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxPointDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TaxableAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TechnicalCommitteeDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TechnicalNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsServiceCallCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsServiceCallType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsServiceCategoryCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsServiceCategoryType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsSupplyTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsSupplyTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TelefaxType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TelephoneType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TenderEnvelopeIdtype(IdentifierType):
    class Meta:
        name = "TenderEnvelopeIDType"


@dataclass(frozen=True, kw_only=True)
class TenderEnvelopeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TenderResultCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TenderTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TendererRequirementTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TendererRoleCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TestMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TextType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ThirdPartyPayerIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class ThresholdAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class ThresholdQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ThresholdValueComparisonCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TierRangeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TierRatePercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True, kw_only=True)
class TimeAmountType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TimeDeltaDaysQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class TimeFrequencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TimezoneOffsetType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TimingComplaintCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TimingComplaintType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TitleType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ToOrderIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalBalanceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalConsumedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalCreditAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalDebitAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalDeliveredQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalGoodsItemQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalInvoiceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalMeteredQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalPackageQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalPackagesQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalPaymentAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalTaskAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalTaxAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TotalTransportHandlingUnitQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True, kw_only=True)
class TraceIdtype(IdentifierType):
    class Meta:
        name = "TraceIDType"


@dataclass(frozen=True, kw_only=True)
class TrackingDeviceCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TrackingIdtype(IdentifierType):
    class Meta:
        name = "TrackingIDType"


@dataclass(frozen=True, kw_only=True)
class TradeItemPackingLabelingTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TradeServiceCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TradingRestrictionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TrainIdtype(IdentifierType):
    class Meta:
        name = "TrainIDType"


@dataclass(frozen=True, kw_only=True)
class TransactionCurrencyTaxAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransitDirectionCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportAuthorizationCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportEmergencyCardCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportEquipmentTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportEventTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportExecutionPlanReferenceIdtype(IdentifierType):
    class Meta:
        name = "TransportExecutionPlanReferenceIDType"


@dataclass(frozen=True, kw_only=True)
class TransportExecutionStatusCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportHandlingUnitTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportMeansTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportModeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportServiceCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportServiceProviderRemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportServiceProviderSpecialTermsType(
    UblUnqualifiedDataTypes21TextType
):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportUserRemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportUserSpecialTermsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportationServiceDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class TransportationServiceDetailsUritype(IdentifierType):
    class Meta:
        name = "TransportationServiceDetailsURIType"


@dataclass(frozen=True, kw_only=True)
class TransportationStatusTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class TypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class UblversionIdtype(IdentifierType):
    class Meta:
        name = "UBLVersionIDType"


@dataclass(frozen=True, kw_only=True)
class UndgcodeType(CodeType):
    class Meta:
        name = "UNDGCodeType"


@dataclass(frozen=True, kw_only=True)
class Uritype(IdentifierType):
    class Meta:
        name = "URIType"


@dataclass(frozen=True, kw_only=True)
class Uuidtype(IdentifierType):
    class Meta:
        name = "UUIDType"


@dataclass(frozen=True, kw_only=True)
class UnknownPriceIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class UpperOrangeHazardPlacardIdtype(IdentifierType):
    class Meta:
        name = "UpperOrangeHazardPlacardIDType"


@dataclass(frozen=True, kw_only=True)
class UrgencyCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class UtilityStatementTypeCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValidateProcessType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValidateToolType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValidateToolVersionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValidationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValidationResultCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValidationTimeType(TimeType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValidatorIdtype(IdentifierType):
    class Meta:
        name = "ValidatorIDType"


@dataclass(frozen=True, kw_only=True)
class ValidityStartDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValueMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValueQualifierType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValueQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class ValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class VarianceQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True, kw_only=True)
class VariantConstraintIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True, kw_only=True)
class VariantIdtype(IdentifierType):
    class Meta:
        name = "VariantIDType"


@dataclass(frozen=True, kw_only=True)
class VersionIdtype(IdentifierType):
    class Meta:
        name = "VersionIDType"


@dataclass(frozen=True, kw_only=True)
class VesselIdtype(IdentifierType):
    class Meta:
        name = "VesselIDType"


@dataclass(frozen=True, kw_only=True)
class VesselNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True, kw_only=True)
class WarrantyInformationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class WebsiteUritype(IdentifierType):
    class Meta:
        name = "WebsiteURIType"


@dataclass(frozen=True, kw_only=True)
class WeekDayCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class WeightNumericType(NumericType):
    pass


@dataclass(frozen=True, kw_only=True)
class WeightType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class WeightingAlgorithmCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class WorkPhaseCodeType(CodeType):
    pass


@dataclass(frozen=True, kw_only=True)
class WorkPhaseType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True, kw_only=True)
class XpathType(UblUnqualifiedDataTypes21TextType):
    class Meta:
        name = "XPathType"


@dataclass(frozen=True, kw_only=True)
class AcceptedIndicator(AcceptedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AcceptedVariantsDescription(AcceptedVariantsDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AccountFormatCode(AccountFormatCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AccountId(AccountIdtype):
    class Meta:
        name = "AccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AccountTypeCode(AccountTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AccountingCost(AccountingCostType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AccountingCostCode(AccountingCostCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActionCode(ActionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActivityType(ActivityTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActivityTypeCode(ActivityTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActualDeliveryDate(ActualDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActualDeliveryTime(ActualDeliveryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActualDespatchDate(ActualDespatchDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActualDespatchTime(ActualDespatchTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActualPickupDate(ActualPickupDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActualPickupTime(ActualPickupTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ActualTemperatureReductionQuantity(
    ActualTemperatureReductionQuantityType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AdValoremIndicator(AdValoremIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AdditionalAccountId(AdditionalAccountIdtype):
    class Meta:
        name = "AdditionalAccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AdditionalConditions(AdditionalConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AdditionalInformation(AdditionalInformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AdditionalStreetName(AdditionalStreetNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AddressFormatCode(AddressFormatCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AddressTypeCode(AddressTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AdjustmentReasonCode(AdjustmentReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AdmissionCode(AdmissionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AdvertisementAmount(AdvertisementAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AgencyId(AgencyIdtype):
    class Meta:
        name = "AgencyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AgencyName(AgencyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AirFlowPercent(AirFlowPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AircraftId(AircraftIdtype):
    class Meta:
        name = "AircraftID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AliasName(AliasNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AllowanceChargeReason(AllowanceChargeReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AllowanceChargeReasonCode(AllowanceChargeReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AllowanceTotalAmount(AllowanceTotalAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AltitudeMeasure(AltitudeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Amount(AmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AmountRate(AmountRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AnimalFoodApprovedIndicator(AnimalFoodApprovedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AnimalFoodIndicator(AnimalFoodIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AnnualAverageAmount(AnnualAverageAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ApplicationStatusCode(ApplicationStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ApprovalDate(ApprovalDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ApprovalStatus(ApprovalStatusType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AttributeId(AttributeIdtype):
    class Meta:
        name = "AttributeID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AuctionConstraintIndicator(AuctionConstraintIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AuctionUri(AuctionUritype):
    class Meta:
        name = "AuctionURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AvailabilityDate(AvailabilityDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AvailabilityStatusCode(AvailabilityStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AverageAmount(AverageAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AverageSubsequentContractAmount(AverageSubsequentContractAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AwardDate(AwardDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AwardTime(AwardTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AwardingCriterionDescription(AwardingCriterionDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AwardingCriterionId(AwardingCriterionIdtype):
    class Meta:
        name = "AwardingCriterionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AwardingCriterionTypeCode(AwardingCriterionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class AwardingMethodTypeCode(AwardingMethodTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BackOrderAllowedIndicator(BackOrderAllowedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BackorderQuantity(BackorderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BackorderReason(BackorderReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BalanceAmount(BalanceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BalanceBroughtForwardIndicator(BalanceBroughtForwardIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BarcodeSymbologyId(BarcodeSymbologyIdtype):
    class Meta:
        name = "BarcodeSymbologyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BaseAmount(BaseAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BaseQuantity(BaseQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BaseUnitMeasure(BaseUnitMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BasedOnConsensusIndicator(BasedOnConsensusIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BasicConsumedQuantity(BasicConsumedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BatchQuantity(BatchQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BestBeforeDate(BestBeforeDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BindingOnBuyerIndicator(BindingOnBuyerIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BirthDate(BirthDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BirthplaceName(BirthplaceNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BlockName(BlockNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BrandName(BrandNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BrokerAssignedId(BrokerAssignedIdtype):
    class Meta:
        name = "BrokerAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BudgetYearNumeric(BudgetYearNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BuildingName(BuildingNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BuildingNumber(BuildingNumberType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BulkCargoIndicator(BulkCargoIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BusinessClassificationEvidenceId(BusinessClassificationEvidenceIdtype):
    class Meta:
        name = "BusinessClassificationEvidenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BusinessIdentityEvidenceId(BusinessIdentityEvidenceIdtype):
    class Meta:
        name = "BusinessIdentityEvidenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BuyerEventId(BuyerEventIdtype):
    class Meta:
        name = "BuyerEventID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BuyerProfileUri(BuyerProfileUritype):
    class Meta:
        name = "BuyerProfileURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class BuyerReference(BuyerReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Cv2Id(Cv2Idtype):
    class Meta:
        name = "CV2ID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CalculationExpression(CalculationExpressionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CalculationExpressionCode(CalculationExpressionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CalculationMethodCode(CalculationMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CalculationRate(CalculationRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CalculationSequenceNumeric(CalculationSequenceNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CallBaseAmount(CallBaseAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CallDate(CallDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CallExtensionAmount(CallExtensionAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CallTime(CallTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CancellationNote(CancellationNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CandidateReductionConstraintIndicator(
    CandidateReductionConstraintIndicatorType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CandidateStatement(CandidateStatementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CanonicalizationMethod(CanonicalizationMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CapabilityTypeCode(CapabilityTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CardChipCode(CardChipCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CardTypeCode(CardTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CargoTypeCode(CargoTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CarrierAssignedId(CarrierAssignedIdtype):
    class Meta:
        name = "CarrierAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CarrierServiceInstructions(CarrierServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CatalogueIndicator(CatalogueIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CategoryName(CategoryNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CertificateType(CertificateTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CertificateTypeCode(CertificateTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ChangeConditions(ChangeConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Channel(ChannelType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ChannelCode(ChannelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CharacterSetCode(CharacterSetCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Characteristics(CharacteristicsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ChargeIndicator(ChargeIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ChargeTotalAmount(ChargeTotalAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ChargeableQuantity(ChargeableQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ChargeableWeightMeasure(ChargeableWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ChildConsignmentQuantity(ChildConsignmentQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ChipApplicationId(ChipApplicationIdtype):
    class Meta:
        name = "ChipApplicationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CityName(CityNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CitySubdivisionName(CitySubdivisionNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CodeValue(CodeValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CollaborationPriorityCode(CollaborationPriorityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Comment(CommentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CommodityCode(CommodityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CompanyId(CompanyIdtype):
    class Meta:
        name = "CompanyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CompanyLegalForm(CompanyLegalFormType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CompanyLegalFormCode(CompanyLegalFormCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CompanyLiquidationStatusCode(CompanyLiquidationStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ComparedValueMeasure(ComparedValueMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ComparisonDataCode(ComparisonDataCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ComparisonDataSourceCode(ComparisonDataSourceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ComparisonForecastIssueDate(ComparisonForecastIssueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ComparisonForecastIssueTime(ComparisonForecastIssueTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CompletionIndicator(CompletionIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Condition(ConditionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConditionCode(ConditionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Conditions(ConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConditionsDescription(ConditionsDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsigneeAssignedId(ConsigneeAssignedIdtype):
    class Meta:
        name = "ConsigneeAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsignmentQuantity(ConsignmentQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsignorAssignedId(ConsignorAssignedIdtype):
    class Meta:
        name = "ConsignorAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsolidatableIndicator(ConsolidatableIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConstitutionCode(ConstitutionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumerIncentiveTacticTypeCode(ConsumerIncentiveTacticTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumerUnitQuantity(ConsumerUnitQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumersEnergyLevel(ConsumersEnergyLevelType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumersEnergyLevelCode(ConsumersEnergyLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumptionEnergyQuantity(ConsumptionEnergyQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumptionId(ConsumptionIdtype):
    class Meta:
        name = "ConsumptionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumptionLevel(ConsumptionLevelType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumptionLevelCode(ConsumptionLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumptionReportId(ConsumptionReportIdtype):
    class Meta:
        name = "ConsumptionReportID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumptionType(ConsumptionTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumptionTypeCode(ConsumptionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ConsumptionWaterQuantity(ConsumptionWaterQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ContainerizedIndicator(ContainerizedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Content(ContentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ContentUnitQuantity(ContentUnitQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ContractFolderId(ContractFolderIdtype):
    class Meta:
        name = "ContractFolderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ContractName(ContractNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ContractSubdivision(ContractSubdivisionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ContractType(ContractTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ContractTypeCode(ContractTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ContractedCarrierAssignedId(ContractedCarrierAssignedIdtype):
    class Meta:
        name = "ContractedCarrierAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ContractingSystemCode(ContractingSystemCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CoordinateSystemCode(CoordinateSystemCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CopyIndicator(CopyIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CorporateRegistrationTypeCode(CorporateRegistrationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CorporateStockAmount(CorporateStockAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CorrectionAmount(CorrectionAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CorrectionType(CorrectionTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CorrectionTypeCode(CorrectionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CorrectionUnitAmount(CorrectionUnitAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CountrySubentity(CountrySubentityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CountrySubentityCode(CountrySubentityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CreditLineAmount(CreditLineAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CreditNoteTypeCode(CreditNoteTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CreditedQuantity(CreditedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CrewQuantity(CrewQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CurrencyCode(CurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CurrentChargeType(CurrentChargeTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CurrentChargeTypeCode(CurrentChargeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CustomerAssignedAccountId(CustomerAssignedAccountIdtype):
    class Meta:
        name = "CustomerAssignedAccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CustomerReference(CustomerReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CustomizationId(CustomizationIdtype):
    class Meta:
        name = "CustomizationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CustomsClearanceServiceInstructions(
    CustomsClearanceServiceInstructionsType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CustomsImportClassifiedIndicator(CustomsImportClassifiedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CustomsStatusCode(CustomsStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class CustomsTariffQuantity(CustomsTariffQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DamageRemarks(DamageRemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DangerousGoodsApprovedIndicator(DangerousGoodsApprovedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DataSendingCapability(DataSendingCapabilityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DataSourceCode(DataSourceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Date(DateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DebitLineAmount(DebitLineAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DebitedQuantity(DebitedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DeclarationTypeCode(DeclarationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DeclaredCarriageValueAmount(DeclaredCarriageValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DeclaredCustomsValueAmount(DeclaredCustomsValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DeclaredForCarriageValueAmount(DeclaredForCarriageValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DeclaredStatisticsValueAmount(DeclaredStatisticsValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DeliveredQuantity(DeliveredQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DeliveryInstructions(DeliveryInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DemurrageInstructions(DemurrageInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Department(DepartmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Description(DescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DescriptionCode(DescriptionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DespatchAdviceTypeCode(DespatchAdviceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DifferenceTemperatureReductionQuantity(
    DifferenceTemperatureReductionQuantityType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DirectionCode(DirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DisplayTacticTypeCode(DisplayTacticTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DispositionCode(DispositionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class District(DistrictType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentCurrencyCode(DocumentCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentDescription(DocumentDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentHash(DocumentHashType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentId(DocumentIdtype):
    class Meta:
        name = "DocumentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentStatusCode(DocumentStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentStatusReasonCode(DocumentStatusReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentStatusReasonDescription(DocumentStatusReasonDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentType(DocumentTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentTypeCode(DocumentTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DocumentationFeeAmount(DocumentationFeeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DueDate(DueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DurationMeasure(DurationMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Duty(DutyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class DutyCode(DutyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EarliestPickupDate(EarliestPickupDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EarliestPickupTime(EarliestPickupTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EconomicOperatorRegistryUri(EconomicOperatorRegistryUritype):
    class Meta:
        name = "EconomicOperatorRegistryURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EffectiveDate(EffectiveDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EffectiveTime(EffectiveTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ElectronicDeviceDescription(ElectronicDeviceDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ElectronicMail(ElectronicMailType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EmbeddedDocumentBinaryObject(EmbeddedDocumentBinaryObjectType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EmergencyProceduresCode(EmergencyProceduresCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EmployeeQuantity(EmployeeQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EncodingCode(EncodingCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EndDate(EndDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EndTime(EndTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EndpointId(EndpointIdtype):
    class Meta:
        name = "EndpointID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EnvironmentalEmissionTypeCode(EnvironmentalEmissionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EstimatedAmount(EstimatedAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EstimatedConsumedQuantity(EstimatedConsumedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EstimatedDeliveryDate(EstimatedDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EstimatedDeliveryTime(EstimatedDeliveryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EstimatedDespatchDate(EstimatedDespatchDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EstimatedDespatchTime(EstimatedDespatchTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EstimatedOverallContractAmount(EstimatedOverallContractAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EstimatedOverallContractQuantity(EstimatedOverallContractQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EvaluationCriterionTypeCode(EvaluationCriterionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class EvidenceTypeCode(EvidenceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExceptionResolutionCode(ExceptionResolutionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExceptionStatusCode(ExceptionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExchangeMarketId(ExchangeMarketIdtype):
    class Meta:
        name = "ExchangeMarketID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExclusionReason(ExclusionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExecutionRequirementCode(ExecutionRequirementCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExemptionReason(ExemptionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExemptionReasonCode(ExemptionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExpectedOperatorQuantity(ExpectedOperatorQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExpectedQuantity(ExpectedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExpenseCode(ExpenseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExpiryDate(ExpiryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExpiryTime(ExpiryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Expression(ExpressionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExpressionCode(ExpressionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ExtendedId(ExtendedIdtype):
    class Meta:
        name = "ExtendedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Extension(ExtensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FaceValueAmount(FaceValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FamilyName(FamilyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FeatureTacticTypeCode(FeatureTacticTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FeeAmount(FeeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FeeDescription(FeeDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FileName(FileNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FinancingInstrumentCode(FinancingInstrumentCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FirstName(FirstNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FirstShipmentAvailibilityDate(FirstShipmentAvailibilityDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Floor(FloorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FollowupContractIndicator(FollowupContractIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ForecastPurposeCode(ForecastPurposeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ForecastTypeCode(ForecastTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FormatCode(FormatCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ForwarderServiceInstructions(ForwarderServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FreeOfChargeIndicator(FreeOfChargeIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FreeOnBoardValueAmount(FreeOnBoardValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FreightForwarderAssignedId(FreightForwarderAssignedIdtype):
    class Meta:
        name = "FreightForwarderAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FreightRateClassCode(FreightRateClassCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Frequency(FrequencyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FrozenDocumentIndicator(FrozenDocumentIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FrozenPeriodDaysNumeric(FrozenPeriodDaysNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FullnessIndicationCode(FullnessIndicationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FullyPaidSharesIndicator(FullyPaidSharesIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FundingProgram(FundingProgramType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class FundingProgramCode(FundingProgramCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GasPressureQuantity(GasPressureQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GenderCode(GenderCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GeneralCargoIndicator(GeneralCargoIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GovernmentAgreementConstraintIndicator(
    GovernmentAgreementConstraintIndicatorType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GrossTonnageMeasure(GrossTonnageMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GrossVolumeMeasure(GrossVolumeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GrossWeightMeasure(GrossWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GuaranteeTypeCode(GuaranteeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GuaranteedDespatchDate(GuaranteedDespatchDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class GuaranteedDespatchTime(GuaranteedDespatchTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HandlingCode(HandlingCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HandlingInstructions(HandlingInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HashAlgorithmMethod(HashAlgorithmMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HaulageInstructions(HaulageInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HazardClassId(HazardClassIdtype):
    class Meta:
        name = "HazardClassID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HazardousCategoryCode(HazardousCategoryCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HazardousRegulationCode(HazardousRegulationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HazardousRiskIndicator(HazardousRiskIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HeatingType(HeatingTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HeatingTypeCode(HeatingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HigherTenderAmount(HigherTenderAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HolderName(HolderNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HumanFoodApprovedIndicator(HumanFoodApprovedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HumanFoodIndicator(HumanFoodIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class HumidityPercent(HumidityPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Id(Idtype):
    class Meta:
        name = "ID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class IdentificationCode(IdentificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class IdentificationId(IdentificationIdtype):
    class Meta:
        name = "IdentificationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ImmobilizationCertificateId(ImmobilizationCertificateIdtype):
    class Meta:
        name = "ImmobilizationCertificateID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ImportanceCode(ImportanceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class IndicationIndicator(IndicationIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class IndustryClassificationCode(IndustryClassificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Information(InformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InformationUri(InformationUritype):
    class Meta:
        name = "InformationURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InhalationToxicityZoneCode(InhalationToxicityZoneCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InhouseMail(InhouseMailType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InspectionMethodCode(InspectionMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InstallmentDueDate(InstallmentDueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InstructionId(InstructionIdtype):
    class Meta:
        name = "InstructionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InstructionNote(InstructionNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Instructions(InstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InsurancePremiumAmount(InsurancePremiumAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InsuranceValueAmount(InsuranceValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InventoryValueAmount(InventoryValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InvoiceTypeCode(InvoiceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InvoicedQuantity(InvoicedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class InvoicingPartyReference(InvoicingPartyReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class IssueDate(IssueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class IssueNumberId(IssueNumberIdtype):
    class Meta:
        name = "IssueNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class IssueTime(IssueTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class IssuerId(IssuerIdtype):
    class Meta:
        name = "IssuerID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ItemClassificationCode(ItemClassificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ItemUpdateRequestIndicator(ItemUpdateRequestIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class JobTitle(JobTitleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class JourneyId(JourneyIdtype):
    class Meta:
        name = "JourneyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Justification(JustificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class JustificationDescription(JustificationDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Keyword(KeywordType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LanguageId(LanguageIdtype):
    class Meta:
        name = "LanguageID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LastRevisionDate(LastRevisionDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LastRevisionTime(LastRevisionTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestDeliveryDate(LatestDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestDeliveryTime(LatestDeliveryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestMeterQuantity(LatestMeterQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestMeterReadingDate(LatestMeterReadingDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestMeterReadingMethod(LatestMeterReadingMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestMeterReadingMethodCode(LatestMeterReadingMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestPickupDate(LatestPickupDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestPickupTime(LatestPickupTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestProposalAcceptanceDate(LatestProposalAcceptanceDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatestSecurityClearanceDate(LatestSecurityClearanceDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatitudeDegreesMeasure(LatitudeDegreesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatitudeDirectionCode(LatitudeDirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LatitudeMinutesMeasure(LatitudeMinutesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LeadTimeMeasure(LeadTimeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LegalReference(LegalReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LegalStatusIndicator(LegalStatusIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LiabilityAmount(LiabilityAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LicensePlateId(LicensePlateIdtype):
    class Meta:
        name = "LicensePlateID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LifeCycleStatusCode(LifeCycleStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LimitationDescription(LimitationDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Line(LineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LineCountNumeric(LineCountNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LineExtensionAmount(LineExtensionAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LineId(LineIdtype):
    class Meta:
        name = "LineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LineNumberNumeric(LineNumberNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LineStatusCode(LineStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ListValue(ListValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LivestockIndicator(LivestockIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LoadingLengthMeasure(LoadingLengthMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LoadingSequenceId(LoadingSequenceIdtype):
    class Meta:
        name = "LoadingSequenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LocaleCode(LocaleCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Location(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LocationId(LocationIdtype):
    class Meta:
        name = "LocationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LocationTypeCode(LocationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Login(LoginType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LogoReferenceId(LogoReferenceIdtype):
    class Meta:
        name = "LogoReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LongitudeDegreesMeasure(LongitudeDegreesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LongitudeDirectionCode(LongitudeDirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LongitudeMinutesMeasure(LongitudeMinutesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LossRisk(LossRiskType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LossRiskResponsibilityCode(LossRiskResponsibilityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LotNumberId(LotNumberIdtype):
    class Meta:
        name = "LotNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LowTendersDescription(LowTendersDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LowerOrangeHazardPlacardId(LowerOrangeHazardPlacardIdtype):
    class Meta:
        name = "LowerOrangeHazardPlacardID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class LowerTenderAmount(LowerTenderAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MandateTypeCode(MandateTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ManufactureDate(ManufactureDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ManufactureTime(ManufactureTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MarkAttention(MarkAttentionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MarkAttentionIndicator(MarkAttentionIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MarkCare(MarkCareType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MarkCareIndicator(MarkCareIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MarketValueAmount(MarketValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MarkingId(MarkingIdtype):
    class Meta:
        name = "MarkingID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MathematicOperatorCode(MathematicOperatorCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumAdvertisementAmount(MaximumAdvertisementAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumAmount(MaximumAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumBackorderQuantity(MaximumBackorderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumCopiesNumeric(MaximumCopiesNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumMeasure(MaximumMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumNumberNumeric(MaximumNumberNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumOperatorQuantity(MaximumOperatorQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumOrderQuantity(MaximumOrderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumPaidAmount(MaximumPaidAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumPaymentInstructionsNumeric(MaximumPaymentInstructionsNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumPercent(MaximumPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumQuantity(MaximumQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumValue(MaximumValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MaximumVariantQuantity(MaximumVariantQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Measure(MeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MedicalFirstAidGuideCode(MedicalFirstAidGuideCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MeterConstant(MeterConstantType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MeterConstantCode(MeterConstantCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MeterName(MeterNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MeterNumber(MeterNumberType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MeterReadingComments(MeterReadingCommentsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MeterReadingType(MeterReadingTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MeterReadingTypeCode(MeterReadingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MiddleName(MiddleNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MimeCode(MimeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumAmount(MinimumAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumBackorderQuantity(MinimumBackorderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumImprovementBid(MinimumImprovementBidType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumInventoryQuantity(MinimumInventoryQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumMeasure(MinimumMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumNumberNumeric(MinimumNumberNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumOrderQuantity(MinimumOrderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumPercent(MinimumPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumQuantity(MinimumQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MinimumValue(MinimumValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MiscellaneousEventTypeCode(MiscellaneousEventTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ModelName(ModelNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MonetaryScope(MonetaryScopeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MovieTitle(MovieTitleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MultipleOrderQuantity(MultipleOrderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class MultiplierFactorNumeric(MultiplierFactorNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Name(NameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NameCode(NameCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NameSuffix(NameSuffixType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NationalityId(NationalityIdtype):
    class Meta:
        name = "NationalityID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NatureCode(NatureCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NegotiationDescription(NegotiationDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NetNetWeightMeasure(NetNetWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NetTonnageMeasure(NetTonnageMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NetVolumeMeasure(NetVolumeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NetWeightMeasure(NetWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NetworkId(NetworkIdtype):
    class Meta:
        name = "NetworkID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NominationDate(NominationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NominationTime(NominationTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NormalTemperatureReductionQuantity(
    NormalTemperatureReductionQuantityType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Note(NoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class NotificationTypeCode(NotificationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OccurrenceDate(OccurrenceDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OccurrenceTime(OccurrenceTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OnCarriageIndicator(OnCarriageIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OneTimeChargeType(OneTimeChargeTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OneTimeChargeTypeCode(OneTimeChargeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OntologyUri(OntologyUritype):
    class Meta:
        name = "OntologyURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OpenTenderId(OpenTenderIdtype):
    class Meta:
        name = "OpenTenderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OperatingYearsQuantity(OperatingYearsQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OptionalLineItemIndicator(OptionalLineItemIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OptionsDescription(OptionsDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OrderIntervalDaysNumeric(OrderIntervalDaysNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OrderQuantityIncrementNumeric(OrderQuantityIncrementNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OrderResponseCode(OrderResponseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OrderTypeCode(OrderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OrderableIndicator(OrderableIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OrderableUnit(OrderableUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OrderableUnitFactorRate(OrderableUnitFactorRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OrganizationDepartment(OrganizationDepartmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OriginalContractingSystemId(OriginalContractingSystemIdtype):
    class Meta:
        name = "OriginalContractingSystemID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OriginalJobId(OriginalJobIdtype):
    class Meta:
        name = "OriginalJobID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OtherConditionsIndicator(OtherConditionsIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OtherInstruction(OtherInstructionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OtherName(OtherNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OutstandingQuantity(OutstandingQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OutstandingReason(OutstandingReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OversupplyQuantity(OversupplyQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class OwnerTypeCode(OwnerTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PackLevelCode(PackLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PackQuantity(PackQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PackSizeNumeric(PackSizeNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PackageLevelCode(PackageLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PackagingTypeCode(PackagingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PackingCriteriaCode(PackingCriteriaCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PackingMaterial(PackingMaterialType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaidAmount(PaidAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaidDate(PaidDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaidTime(PaidTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ParentDocumentId(ParentDocumentIdtype):
    class Meta:
        name = "ParentDocumentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ParentDocumentLineReferenceId(ParentDocumentLineReferenceIdtype):
    class Meta:
        name = "ParentDocumentLineReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ParentDocumentTypeCode(ParentDocumentTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ParentDocumentVersionId(ParentDocumentVersionIdtype):
    class Meta:
        name = "ParentDocumentVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PartPresentationCode(PartPresentationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PartecipationPercent(PartecipationPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PartialDeliveryIndicator(PartialDeliveryIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ParticipationPercent(ParticipationPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PartyCapacityAmount(PartyCapacityAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PartyType(PartyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PartyTypeCode(PartyTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PassengerQuantity(PassengerQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Password(PasswordType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PayPerView(PayPerViewType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PayableAlternativeAmount(PayableAlternativeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PayableAmount(PayableAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PayableRoundingAmount(PayableRoundingAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PayerReference(PayerReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentAlternativeCurrencyCode(PaymentAlternativeCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentChannelCode(PaymentChannelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentCurrencyCode(PaymentCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentDescription(PaymentDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentDueDate(PaymentDueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentFrequencyCode(PaymentFrequencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentId(PaymentIdtype):
    class Meta:
        name = "PaymentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentMeansCode(PaymentMeansCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentMeansId(PaymentMeansIdtype):
    class Meta:
        name = "PaymentMeansID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentNote(PaymentNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentOrderReference(PaymentOrderReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentPercent(PaymentPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentPurposeCode(PaymentPurposeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PaymentTermsDetailsUri(PaymentTermsDetailsUritype):
    class Meta:
        name = "PaymentTermsDetailsURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PenaltyAmount(PenaltyAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PenaltySurchargePercent(PenaltySurchargePercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PerUnitAmount(PerUnitAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Percent(PercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PerformanceMetricTypeCode(PerformanceMetricTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PerformanceValueQuantity(PerformanceValueQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PerformingCarrierAssignedId(PerformingCarrierAssignedIdtype):
    class Meta:
        name = "PerformingCarrierAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PersonalSituation(PersonalSituationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PhoneNumber(PhoneNumberType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PlacardEndorsement(PlacardEndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PlacardNotation(PlacardNotationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PlannedDate(PlannedDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PlotIdentification(PlotIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PositionCode(PositionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PostEventNotificationDurationMeasure(
    PostEventNotificationDurationMeasureType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PostalZone(PostalZoneType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Postbox(PostboxType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PowerIndicator(PowerIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreCarriageIndicator(PreCarriageIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreEventNotificationDurationMeasure(
    PreEventNotificationDurationMeasureType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreferenceCriterionCode(PreferenceCriterionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PrepaidAmount(PrepaidAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PrepaidIndicator(PrepaidIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PrepaidPaymentReferenceId(PrepaidPaymentReferenceIdtype):
    class Meta:
        name = "PrepaidPaymentReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreviousCancellationReasonCode(PreviousCancellationReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreviousJobId(PreviousJobIdtype):
    class Meta:
        name = "PreviousJobID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreviousMeterQuantity(PreviousMeterQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreviousMeterReadingDate(PreviousMeterReadingDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreviousMeterReadingMethod(PreviousMeterReadingMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreviousMeterReadingMethodCode(PreviousMeterReadingMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PreviousVersionId(PreviousVersionIdtype):
    class Meta:
        name = "PreviousVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PriceAmount(PriceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PriceChangeReason(PriceChangeReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PriceEvaluationCode(PriceEvaluationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PriceRevisionFormulaDescription(PriceRevisionFormulaDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PriceType(PriceTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PriceTypeCode(PriceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PricingCurrencyCode(PricingCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PricingUpdateRequestIndicator(PricingUpdateRequestIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PrimaryAccountNumberId(PrimaryAccountNumberIdtype):
    class Meta:
        name = "PrimaryAccountNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PrintQualifier(PrintQualifierType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Priority(PriorityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PrivacyCode(PrivacyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PrizeDescription(PrizeDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PrizeIndicator(PrizeIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProcedureCode(ProcedureCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProcessDescription(ProcessDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProcessReason(ProcessReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProcessReasonCode(ProcessReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProcurementSubTypeCode(ProcurementSubTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProcurementTypeCode(ProcurementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProductTraceId(ProductTraceIdtype):
    class Meta:
        name = "ProductTraceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProfileExecutionId(ProfileExecutionIdtype):
    class Meta:
        name = "ProfileExecutionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProfileId(ProfileIdtype):
    class Meta:
        name = "ProfileID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProfileStatusCode(ProfileStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProgressPercent(ProgressPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PromotionalEventTypeCode(PromotionalEventTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ProviderTypeCode(ProviderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PublishAwardIndicator(PublishAwardIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Purpose(PurposeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class PurposeCode(PurposeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class QualityControlCode(QualityControlCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Quantity(QuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class QuantityDiscrepancyCode(QuantityDiscrepancyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RadioCallSignId(RadioCallSignIdtype):
    class Meta:
        name = "RadioCallSignID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RailCarId(RailCarIdtype):
    class Meta:
        name = "RailCarID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Rank(RankType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Rate(RateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReceiptAdviceTypeCode(ReceiptAdviceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReceivedDate(ReceivedDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReceivedElectronicTenderQuantity(ReceivedElectronicTenderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReceivedForeignTenderQuantity(ReceivedForeignTenderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReceivedQuantity(ReceivedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReceivedTenderQuantity(ReceivedTenderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Reference(ReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReferenceDate(ReferenceDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReferenceEventCode(ReferenceEventCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReferenceId(ReferenceIdtype):
    class Meta:
        name = "ReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReferenceTime(ReferenceTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReferencedConsignmentId(ReferencedConsignmentIdtype):
    class Meta:
        name = "ReferencedConsignmentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RefrigeratedIndicator(RefrigeratedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RefrigerationOnIndicator(RefrigerationOnIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Region(RegionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RegisteredDate(RegisteredDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RegisteredTime(RegisteredTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RegistrationDate(RegistrationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RegistrationExpirationDate(RegistrationExpirationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RegistrationId(RegistrationIdtype):
    class Meta:
        name = "RegistrationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RegistrationName(RegistrationNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RegistrationNationality(RegistrationNationalityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RegistrationNationalityId(RegistrationNationalityIdtype):
    class Meta:
        name = "RegistrationNationalityID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RegulatoryDomain(RegulatoryDomainType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RejectActionCode(RejectActionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RejectReason(RejectReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RejectReasonCode(RejectReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RejectedQuantity(RejectedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RejectionNote(RejectionNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReleaseId(ReleaseIdtype):
    class Meta:
        name = "ReleaseID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReliabilityPercent(ReliabilityPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Remarks(RemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReminderSequenceNumeric(ReminderSequenceNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReminderTypeCode(ReminderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReplenishmentOwnerDescription(ReplenishmentOwnerDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequestForQuotationLineId(RequestForQuotationLineIdtype):
    class Meta:
        name = "RequestForQuotationLineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequestedDeliveryDate(RequestedDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequestedDespatchDate(RequestedDespatchDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequestedDespatchTime(RequestedDespatchTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequestedInvoiceCurrencyCode(RequestedInvoiceCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequestedPublicationDate(RequestedPublicationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequiredCurriculaIndicator(RequiredCurriculaIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequiredCustomsId(RequiredCustomsIdtype):
    class Meta:
        name = "RequiredCustomsID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequiredDeliveryDate(RequiredDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequiredDeliveryTime(RequiredDeliveryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RequiredFeeAmount(RequiredFeeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ResidenceType(ResidenceTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ResidenceTypeCode(ResidenceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ResidentOccupantsNumeric(ResidentOccupantsNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Resolution(ResolutionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ResolutionCode(ResolutionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ResolutionDate(ResolutionDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ResolutionTime(ResolutionTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ResponseCode(ResponseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ResponseDate(ResponseDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ResponseTime(ResponseTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RetailEventName(RetailEventNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RetailEventStatusCode(RetailEventStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReturnabilityIndicator(ReturnabilityIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReturnableMaterialIndicator(ReturnableMaterialIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ReturnableQuantity(ReturnableQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RevisedForecastLineId(RevisedForecastLineIdtype):
    class Meta:
        name = "RevisedForecastLineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RevisionDate(RevisionDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RevisionStatusCode(RevisionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RevisionTime(RevisionTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RoamingPartnerName(RoamingPartnerNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RoleCode(RoleCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RoleDescription(RoleDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Room(RoomType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class RoundingAmount(RoundingAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SalesOrderId(SalesOrderIdtype):
    class Meta:
        name = "SalesOrderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SalesOrderLineId(SalesOrderLineIdtype):
    class Meta:
        name = "SalesOrderLineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SchemeUri(SchemeUritype):
    class Meta:
        name = "SchemeURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SealIssuerTypeCode(SealIssuerTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SealStatusCode(SealStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SealingPartyType(SealingPartyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SecurityClassificationCode(SecurityClassificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SecurityId(SecurityIdtype):
    class Meta:
        name = "SecurityID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SellerEventId(SellerEventIdtype):
    class Meta:
        name = "SellerEventID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SequenceId(SequenceIdtype):
    class Meta:
        name = "SequenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SequenceNumberId(SequenceNumberIdtype):
    class Meta:
        name = "SequenceNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SequenceNumeric(SequenceNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SerialId(SerialIdtype):
    class Meta:
        name = "SerialID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ServiceInformationPreferenceCode(ServiceInformationPreferenceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ServiceName(ServiceNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ServiceNumberCalled(ServiceNumberCalledType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ServiceType(ServiceTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ServiceTypeCode(ServiceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SettlementDiscountAmount(SettlementDiscountAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SettlementDiscountPercent(SettlementDiscountPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SharesNumberQuantity(SharesNumberQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ShippingMarks(ShippingMarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ShippingOrderId(ShippingOrderIdtype):
    class Meta:
        name = "ShippingOrderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ShippingPriorityLevelCode(ShippingPriorityLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ShipsRequirements(ShipsRequirementsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ShortQuantity(ShortQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ShortageActionCode(ShortageActionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SignatureId(SignatureIdtype):
    class Meta:
        name = "SignatureID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SignatureMethod(SignatureMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SizeTypeCode(SizeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SoleProprietorshipIndicator(SoleProprietorshipIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SourceCurrencyBaseRate(SourceCurrencyBaseRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SourceCurrencyCode(SourceCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SourceForecastIssueDate(SourceForecastIssueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SourceForecastIssueTime(SourceForecastIssueTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SourceValueMeasure(SourceValueMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SpecialInstructions(SpecialInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SpecialSecurityIndicator(SpecialSecurityIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SpecialServiceInstructions(SpecialServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SpecialTerms(SpecialTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SpecialTransportRequirements(SpecialTransportRequirementsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SpecificationId(SpecificationIdtype):
    class Meta:
        name = "SpecificationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SpecificationTypeCode(SpecificationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SplitConsignmentIndicator(SplitConsignmentIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class StartDate(StartDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class StartTime(StartTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class StatementTypeCode(StatementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class StatusAvailableIndicator(StatusAvailableIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class StatusCode(StatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class StatusReason(StatusReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class StatusReasonCode(StatusReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class StreetName(StreetNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SubcontractingConditionsCode(SubcontractingConditionsCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SubmissionDate(SubmissionDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SubmissionDueDate(SubmissionDueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SubmissionMethodCode(SubmissionMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SubscriberId(SubscriberIdtype):
    class Meta:
        name = "SubscriberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SubscriberType(SubscriberTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SubscriberTypeCode(SubscriberTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SubstitutionStatusCode(SubstitutionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SuccessiveSequenceId(SuccessiveSequenceIdtype):
    class Meta:
        name = "SuccessiveSequenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SummaryDescription(SummaryDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SupplierAssignedAccountId(SupplierAssignedAccountIdtype):
    class Meta:
        name = "SupplierAssignedAccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class SupplyChainActivityTypeCode(SupplyChainActivityTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TareWeightMeasure(TareWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TargetCurrencyBaseRate(TargetCurrencyBaseRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TargetCurrencyCode(TargetCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TargetInventoryQuantity(TargetInventoryQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TargetServicePercent(TargetServicePercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TariffClassCode(TariffClassCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TariffCode(TariffCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TariffDescription(TariffDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxAmount(TaxAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxCurrencyCode(TaxCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxEnergyAmount(TaxEnergyAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxEnergyBalanceAmount(TaxEnergyBalanceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxEnergyOnAccountAmount(TaxEnergyOnAccountAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxEvidenceIndicator(TaxEvidenceIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxExclusiveAmount(TaxExclusiveAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxExemptionReason(TaxExemptionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxExemptionReasonCode(TaxExemptionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxIncludedIndicator(TaxIncludedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxInclusiveAmount(TaxInclusiveAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxLevelCode(TaxLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxPointDate(TaxPointDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxTypeCode(TaxTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TaxableAmount(TaxableAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TechnicalCommitteeDescription(TechnicalCommitteeDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TechnicalName(TechnicalNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsServiceCall(TelecommunicationsServiceCallType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsServiceCallCode(TelecommunicationsServiceCallCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsServiceCategory(TelecommunicationsServiceCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsServiceCategoryCode(
    TelecommunicationsServiceCategoryCodeType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsSupplyType(TelecommunicationsSupplyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TelecommunicationsSupplyTypeCode(TelecommunicationsSupplyTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Telefax(TelefaxType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Telephone(TelephoneType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TenderEnvelopeId(TenderEnvelopeIdtype):
    class Meta:
        name = "TenderEnvelopeID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TenderEnvelopeTypeCode(TenderEnvelopeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TenderResultCode(TenderResultCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TenderTypeCode(TenderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TendererRequirementTypeCode(TendererRequirementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TendererRoleCode(TendererRoleCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TestMethod(TestMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Text(TextType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ThirdPartyPayerIndicator(ThirdPartyPayerIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ThresholdAmount(ThresholdAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ThresholdQuantity(ThresholdQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ThresholdValueComparisonCode(ThresholdValueComparisonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TierRange(TierRangeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TierRatePercent(TierRatePercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TimeAmount(TimeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TimeDeltaDaysQuantity(TimeDeltaDaysQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TimeFrequencyCode(TimeFrequencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TimezoneOffset(TimezoneOffsetType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TimingComplaint(TimingComplaintType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TimingComplaintCode(TimingComplaintCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Title(TitleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ToOrderIndicator(ToOrderIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalAmount(TotalAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalBalanceAmount(TotalBalanceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalConsumedQuantity(TotalConsumedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalCreditAmount(TotalCreditAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalDebitAmount(TotalDebitAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalDeliveredQuantity(TotalDeliveredQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalGoodsItemQuantity(TotalGoodsItemQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalInvoiceAmount(TotalInvoiceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalMeteredQuantity(TotalMeteredQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalPackageQuantity(TotalPackageQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalPackagesQuantity(TotalPackagesQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalPaymentAmount(TotalPaymentAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalTaskAmount(TotalTaskAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalTaxAmount(TotalTaxAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TotalTransportHandlingUnitQuantity(
    TotalTransportHandlingUnitQuantityType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TraceId(TraceIdtype):
    class Meta:
        name = "TraceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TrackingDeviceCode(TrackingDeviceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TrackingId(TrackingIdtype):
    class Meta:
        name = "TrackingID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TradeItemPackingLabelingTypeCode(TradeItemPackingLabelingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TradeServiceCode(TradeServiceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TradingRestrictions(TradingRestrictionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TrainId(TrainIdtype):
    class Meta:
        name = "TrainID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransactionCurrencyTaxAmount(TransactionCurrencyTaxAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransitDirectionCode(TransitDirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportAuthorizationCode(TransportAuthorizationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportEmergencyCardCode(TransportEmergencyCardCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportEquipmentTypeCode(TransportEquipmentTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportEventTypeCode(TransportEventTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportExecutionPlanReferenceId(TransportExecutionPlanReferenceIdtype):
    class Meta:
        name = "TransportExecutionPlanReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportExecutionStatusCode(TransportExecutionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportHandlingUnitTypeCode(TransportHandlingUnitTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportMeansTypeCode(TransportMeansTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportModeCode(TransportModeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportServiceCode(TransportServiceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportServiceProviderRemarks(TransportServiceProviderRemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportServiceProviderSpecialTerms(
    TransportServiceProviderSpecialTermsType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportUserRemarks(TransportUserRemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportUserSpecialTerms(TransportUserSpecialTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportationServiceDescription(TransportationServiceDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportationServiceDetailsUri(TransportationServiceDetailsUritype):
    class Meta:
        name = "TransportationServiceDetailsURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TransportationStatusTypeCode(TransportationStatusTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class TypeCode(TypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class UblversionId(UblversionIdtype):
    class Meta:
        name = "UBLVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Undgcode(UndgcodeType):
    class Meta:
        name = "UNDGCode"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Uri(Uritype):
    class Meta:
        name = "URI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Uuid(Uuidtype):
    class Meta:
        name = "UUID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class UnknownPriceIndicator(UnknownPriceIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class UpperOrangeHazardPlacardId(UpperOrangeHazardPlacardIdtype):
    class Meta:
        name = "UpperOrangeHazardPlacardID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class UrgencyCode(UrgencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class UtilityStatementTypeCode(UtilityStatementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValidateProcess(ValidateProcessType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValidateTool(ValidateToolType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValidateToolVersion(ValidateToolVersionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValidationDate(ValidationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValidationResultCode(ValidationResultCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValidationTime(ValidationTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValidatorId(ValidatorIdtype):
    class Meta:
        name = "ValidatorID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValidityStartDate(ValidityStartDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Value(ValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValueAmount(ValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValueMeasure(ValueMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValueQualifier(ValueQualifierType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class ValueQuantity(ValueQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class VarianceQuantity(VarianceQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class VariantConstraintIndicator(VariantConstraintIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class VariantId(VariantIdtype):
    class Meta:
        name = "VariantID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class VersionId(VersionIdtype):
    class Meta:
        name = "VersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class VesselId(VesselIdtype):
    class Meta:
        name = "VesselID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class VesselName(VesselNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class WarrantyInformation(WarrantyInformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class WebsiteUri(WebsiteUritype):
    class Meta:
        name = "WebsiteURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class WeekDayCode(WeekDayCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Weight(WeightType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class WeightNumeric(WeightNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class WeightingAlgorithmCode(WeightingAlgorithmCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class WorkPhase(WorkPhaseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class WorkPhaseCode(WorkPhaseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True, kw_only=True)
class Xpath(XpathType):
    class Meta:
        name = "XPath"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
