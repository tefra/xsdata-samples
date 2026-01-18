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


@dataclass(frozen=True)
class AcceptedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class AcceptedVariantsDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class AccountFormatCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AccountIdtype(IdentifierType):
    class Meta:
        name = "AccountIDType"


@dataclass(frozen=True)
class AccountTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AccountingCostCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AccountingCostType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ActionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ActivityTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ActivityTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ActualDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ActualDeliveryTimeType(TimeType):
    pass


@dataclass(frozen=True)
class ActualDespatchDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ActualDespatchTimeType(TimeType):
    pass


@dataclass(frozen=True)
class ActualPickupDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ActualPickupTimeType(TimeType):
    pass


@dataclass(frozen=True)
class ActualTemperatureReductionQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True)
class AdValoremIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class AdditionalAccountIdtype(IdentifierType):
    class Meta:
        name = "AdditionalAccountIDType"


@dataclass(frozen=True)
class AdditionalConditionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class AdditionalInformationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class AdditionalStreetNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class AddressFormatCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AddressTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AdjustmentReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AdmissionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AdvertisementAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class AgencyIdtype(IdentifierType):
    class Meta:
        name = "AgencyIDType"


@dataclass(frozen=True)
class AgencyNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class AirFlowPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class AircraftIdtype(IdentifierType):
    class Meta:
        name = "AircraftIDType"


@dataclass(frozen=True)
class AliasNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class AllowanceChargeReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AllowanceChargeReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class AllowanceTotalAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class AltitudeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class AmountRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True)
class AmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class AnimalFoodApprovedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class AnimalFoodIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class AnnualAverageAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class ApplicationStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ApprovalDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ApprovalStatusType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class AttributeIdtype(IdentifierType):
    class Meta:
        name = "AttributeIDType"


@dataclass(frozen=True)
class AuctionConstraintIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class AuctionUritype(IdentifierType):
    class Meta:
        name = "AuctionURIType"


@dataclass(frozen=True)
class AvailabilityDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class AvailabilityStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AverageAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class AverageSubsequentContractAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class AwardDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class AwardTimeType(TimeType):
    pass


@dataclass(frozen=True)
class AwardingCriterionDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class AwardingCriterionIdtype(IdentifierType):
    class Meta:
        name = "AwardingCriterionIDType"


@dataclass(frozen=True)
class AwardingCriterionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class AwardingMethodTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class BackOrderAllowedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class BackorderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class BackorderReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class BalanceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class BalanceBroughtForwardIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class BarcodeSymbologyIdtype(IdentifierType):
    class Meta:
        name = "BarcodeSymbologyIDType"


@dataclass(frozen=True)
class BaseAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class BaseQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class BaseUnitMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class BasedOnConsensusIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class BasicConsumedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class BatchQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class BestBeforeDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class BindingOnBuyerIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class BirthDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class BirthplaceNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class BlockNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class BrandNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class BrokerAssignedIdtype(IdentifierType):
    class Meta:
        name = "BrokerAssignedIDType"


@dataclass(frozen=True)
class BudgetYearNumericType(NumericType):
    pass


@dataclass(frozen=True)
class BuildingNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class BuildingNumberType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class BulkCargoIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class BusinessClassificationEvidenceIdtype(IdentifierType):
    class Meta:
        name = "BusinessClassificationEvidenceIDType"


@dataclass(frozen=True)
class BusinessIdentityEvidenceIdtype(IdentifierType):
    class Meta:
        name = "BusinessIdentityEvidenceIDType"


@dataclass(frozen=True)
class BuyerEventIdtype(IdentifierType):
    class Meta:
        name = "BuyerEventIDType"


@dataclass(frozen=True)
class BuyerProfileUritype(IdentifierType):
    class Meta:
        name = "BuyerProfileURIType"


@dataclass(frozen=True)
class BuyerReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class Cv2Idtype(IdentifierType):
    class Meta:
        name = "CV2IDType"


@dataclass(frozen=True)
class CalculationExpressionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CalculationExpressionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CalculationMethodCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CalculationRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True)
class CalculationSequenceNumericType(NumericType):
    pass


@dataclass(frozen=True)
class CallBaseAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class CallDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class CallExtensionAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class CallTimeType(TimeType):
    pass


@dataclass(frozen=True)
class CancellationNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CandidateReductionConstraintIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class CandidateStatementType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CanonicalizationMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CapabilityTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CardChipCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CardTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CargoTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CarrierAssignedIdtype(IdentifierType):
    class Meta:
        name = "CarrierAssignedIDType"


@dataclass(frozen=True)
class CarrierServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CatalogueIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class CategoryNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class CertificateTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CertificateTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ChangeConditionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ChannelCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ChannelType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CharacterSetCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CharacteristicsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ChargeIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ChargeTotalAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class ChargeableQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ChargeableWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class ChildConsignmentQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ChipApplicationIdtype(IdentifierType):
    class Meta:
        name = "ChipApplicationIDType"


@dataclass(frozen=True)
class CityNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class CitySubdivisionNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class CodeValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CollaborationPriorityCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CommentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CommodityCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CompanyIdtype(IdentifierType):
    class Meta:
        name = "CompanyIDType"


@dataclass(frozen=True)
class CompanyLegalFormCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CompanyLegalFormType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CompanyLiquidationStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ComparedValueMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class ComparisonDataCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ComparisonDataSourceCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ComparisonForecastIssueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ComparisonForecastIssueTimeType(TimeType):
    pass


@dataclass(frozen=True)
class CompletionIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ConditionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ConditionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ConditionsDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ConditionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ConsigneeAssignedIdtype(IdentifierType):
    class Meta:
        name = "ConsigneeAssignedIDType"


@dataclass(frozen=True)
class ConsignmentQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ConsignorAssignedIdtype(IdentifierType):
    class Meta:
        name = "ConsignorAssignedIDType"


@dataclass(frozen=True)
class ConsolidatableIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ConstitutionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ConsumerIncentiveTacticTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ConsumerUnitQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ConsumersEnergyLevelCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ConsumersEnergyLevelType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ConsumptionEnergyQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ConsumptionIdtype(IdentifierType):
    class Meta:
        name = "ConsumptionIDType"


@dataclass(frozen=True)
class ConsumptionLevelCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ConsumptionLevelType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ConsumptionReportIdtype(IdentifierType):
    class Meta:
        name = "ConsumptionReportIDType"


@dataclass(frozen=True)
class ConsumptionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ConsumptionTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ConsumptionWaterQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ContainerizedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ContentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ContentUnitQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ContractFolderIdtype(IdentifierType):
    class Meta:
        name = "ContractFolderIDType"


@dataclass(frozen=True)
class ContractNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ContractSubdivisionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ContractTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ContractTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ContractedCarrierAssignedIdtype(IdentifierType):
    class Meta:
        name = "ContractedCarrierAssignedIDType"


@dataclass(frozen=True)
class ContractingSystemCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CoordinateSystemCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CopyIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class CorporateRegistrationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CorporateStockAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class CorrectionAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class CorrectionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CorrectionTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CorrectionUnitAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class CountrySubentityCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CountrySubentityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CreditLineAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class CreditNoteTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CreditedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class CrewQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class CurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CurrentChargeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CurrentChargeTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CustomerAssignedAccountIdtype(IdentifierType):
    class Meta:
        name = "CustomerAssignedAccountIDType"


@dataclass(frozen=True)
class CustomerReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class CustomizationIdtype(IdentifierType):
    class Meta:
        name = "CustomizationIDType"


@dataclass(frozen=True)
class CustomsClearanceServiceInstructionsType(
    UblUnqualifiedDataTypes21TextType
):
    pass


@dataclass(frozen=True)
class CustomsImportClassifiedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class CustomsStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class CustomsTariffQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class DamageRemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DangerousGoodsApprovedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class DataSendingCapabilityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DataSourceCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class DebitLineAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class DebitedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class DeclarationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DeclaredCarriageValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class DeclaredCustomsValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class DeclaredForCarriageValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class DeclaredStatisticsValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class DeliveredQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class DeliveryInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DemurrageInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DepartmentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DescriptionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DespatchAdviceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DifferenceTemperatureReductionQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True)
class DirectionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DisplayTacticTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DispositionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DistrictType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DocumentCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DocumentDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DocumentHashType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DocumentIdtype(IdentifierType):
    class Meta:
        name = "DocumentIDType"


@dataclass(frozen=True)
class DocumentStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DocumentStatusReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DocumentStatusReasonDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DocumentTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DocumentTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class DocumentationFeeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class DueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class DurationMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class DutyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class DutyType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class EarliestPickupDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class EarliestPickupTimeType(TimeType):
    pass


@dataclass(frozen=True)
class EconomicOperatorRegistryUritype(IdentifierType):
    class Meta:
        name = "EconomicOperatorRegistryURIType"


@dataclass(frozen=True)
class EffectiveDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class EffectiveTimeType(TimeType):
    pass


@dataclass(frozen=True)
class ElectronicDeviceDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ElectronicMailType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class EmbeddedDocumentBinaryObjectType(BinaryObjectType):
    pass


@dataclass(frozen=True)
class EmergencyProceduresCodeType(CodeType):
    pass


@dataclass(frozen=True)
class EmployeeQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class EncodingCodeType(CodeType):
    pass


@dataclass(frozen=True)
class EndDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class EndTimeType(TimeType):
    pass


@dataclass(frozen=True)
class EndpointIdtype(IdentifierType):
    class Meta:
        name = "EndpointIDType"


@dataclass(frozen=True)
class EnvironmentalEmissionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class EstimatedAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class EstimatedConsumedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class EstimatedDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class EstimatedDeliveryTimeType(TimeType):
    pass


@dataclass(frozen=True)
class EstimatedDespatchDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class EstimatedDespatchTimeType(TimeType):
    pass


@dataclass(frozen=True)
class EstimatedOverallContractAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class EstimatedOverallContractQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True)
class EvaluationCriterionTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class EvidenceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ExceptionResolutionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ExceptionStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ExchangeMarketIdtype(IdentifierType):
    class Meta:
        name = "ExchangeMarketIDType"


@dataclass(frozen=True)
class ExclusionReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ExecutionRequirementCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ExemptionReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ExemptionReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ExpectedOperatorQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ExpectedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ExpenseCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ExpiryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ExpiryTimeType(TimeType):
    pass


@dataclass(frozen=True)
class ExpressionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ExpressionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ExtendedIdtype(IdentifierType):
    class Meta:
        name = "ExtendedIDType"


@dataclass(frozen=True)
class ExtensionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class FaceValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class FamilyNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class FeatureTacticTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class FeeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class FeeDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class FileNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class FinancingInstrumentCodeType(CodeType):
    pass


@dataclass(frozen=True)
class FirstNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class FirstShipmentAvailibilityDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class FloorType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class FollowupContractIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ForecastPurposeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ForecastTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class FormatCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ForwarderServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class FreeOfChargeIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class FreeOnBoardValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class FreightForwarderAssignedIdtype(IdentifierType):
    class Meta:
        name = "FreightForwarderAssignedIDType"


@dataclass(frozen=True)
class FreightRateClassCodeType(CodeType):
    pass


@dataclass(frozen=True)
class FrequencyType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class FrozenDocumentIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class FrozenPeriodDaysNumericType(NumericType):
    pass


@dataclass(frozen=True)
class FullnessIndicationCodeType(CodeType):
    pass


@dataclass(frozen=True)
class FullyPaidSharesIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class FundingProgramCodeType(CodeType):
    pass


@dataclass(frozen=True)
class FundingProgramType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class GasPressureQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class GenderCodeType(CodeType):
    pass


@dataclass(frozen=True)
class GeneralCargoIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class GovernmentAgreementConstraintIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class GrossTonnageMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class GrossVolumeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class GrossWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class GuaranteeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class GuaranteedDespatchDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class GuaranteedDespatchTimeType(TimeType):
    pass


@dataclass(frozen=True)
class HandlingCodeType(CodeType):
    pass


@dataclass(frozen=True)
class HandlingInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class HashAlgorithmMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class HaulageInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class HazardClassIdtype(IdentifierType):
    class Meta:
        name = "HazardClassIDType"


@dataclass(frozen=True)
class HazardousCategoryCodeType(CodeType):
    pass


@dataclass(frozen=True)
class HazardousRegulationCodeType(CodeType):
    pass


@dataclass(frozen=True)
class HazardousRiskIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class HeatingTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class HeatingTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class HigherTenderAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class HolderNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class HumanFoodApprovedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class HumanFoodIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class HumidityPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class Idtype(IdentifierType):
    class Meta:
        name = "IDType"


@dataclass(frozen=True)
class IdentificationCodeType(CodeType):
    pass


@dataclass(frozen=True)
class IdentificationIdtype(IdentifierType):
    class Meta:
        name = "IdentificationIDType"


@dataclass(frozen=True)
class ImmobilizationCertificateIdtype(IdentifierType):
    class Meta:
        name = "ImmobilizationCertificateIDType"


@dataclass(frozen=True)
class ImportanceCodeType(CodeType):
    pass


@dataclass(frozen=True)
class IndicationIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class IndustryClassificationCodeType(CodeType):
    pass


@dataclass(frozen=True)
class InformationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class InformationUritype(IdentifierType):
    class Meta:
        name = "InformationURIType"


@dataclass(frozen=True)
class InhalationToxicityZoneCodeType(CodeType):
    pass


@dataclass(frozen=True)
class InhouseMailType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class InspectionMethodCodeType(CodeType):
    pass


@dataclass(frozen=True)
class InstallmentDueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class InstructionIdtype(IdentifierType):
    class Meta:
        name = "InstructionIDType"


@dataclass(frozen=True)
class InstructionNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class InstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class InsurancePremiumAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class InsuranceValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class InventoryValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class InvoiceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class InvoicedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class InvoicingPartyReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class IssueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class IssueNumberIdtype(IdentifierType):
    class Meta:
        name = "IssueNumberIDType"


@dataclass(frozen=True)
class IssueTimeType(TimeType):
    pass


@dataclass(frozen=True)
class IssuerIdtype(IdentifierType):
    class Meta:
        name = "IssuerIDType"


@dataclass(frozen=True)
class ItemClassificationCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ItemUpdateRequestIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class JobTitleType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class JourneyIdtype(IdentifierType):
    class Meta:
        name = "JourneyIDType"


@dataclass(frozen=True)
class JustificationDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class JustificationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class KeywordType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class LanguageIdtype(IdentifierType):
    class Meta:
        name = "LanguageIDType"


@dataclass(frozen=True)
class LastRevisionDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class LastRevisionTimeType(TimeType):
    pass


@dataclass(frozen=True)
class LatestDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class LatestDeliveryTimeType(TimeType):
    pass


@dataclass(frozen=True)
class LatestMeterQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class LatestMeterReadingDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class LatestMeterReadingMethodCodeType(CodeType):
    pass


@dataclass(frozen=True)
class LatestMeterReadingMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class LatestPickupDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class LatestPickupTimeType(TimeType):
    pass


@dataclass(frozen=True)
class LatestProposalAcceptanceDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class LatestSecurityClearanceDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class LatitudeDegreesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class LatitudeDirectionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class LatitudeMinutesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class LeadTimeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class LegalReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class LegalStatusIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class LiabilityAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class LicensePlateIdtype(IdentifierType):
    class Meta:
        name = "LicensePlateIDType"


@dataclass(frozen=True)
class LifeCycleStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class LimitationDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class LineCountNumericType(NumericType):
    pass


@dataclass(frozen=True)
class LineExtensionAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class LineIdtype(IdentifierType):
    class Meta:
        name = "LineIDType"


@dataclass(frozen=True)
class LineNumberNumericType(NumericType):
    pass


@dataclass(frozen=True)
class LineStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class LineType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ListValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class LivestockIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class LoadingLengthMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class LoadingSequenceIdtype(IdentifierType):
    class Meta:
        name = "LoadingSequenceIDType"


@dataclass(frozen=True)
class LocaleCodeType(CodeType):
    pass


@dataclass(frozen=True)
class LocationIdtype(IdentifierType):
    class Meta:
        name = "LocationIDType"


@dataclass(frozen=True)
class LocationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class LocationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class LoginType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class LogoReferenceIdtype(IdentifierType):
    class Meta:
        name = "LogoReferenceIDType"


@dataclass(frozen=True)
class LongitudeDegreesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class LongitudeDirectionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class LongitudeMinutesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class LossRiskResponsibilityCodeType(CodeType):
    pass


@dataclass(frozen=True)
class LossRiskType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class LotNumberIdtype(IdentifierType):
    class Meta:
        name = "LotNumberIDType"


@dataclass(frozen=True)
class LowTendersDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class LowerOrangeHazardPlacardIdtype(IdentifierType):
    class Meta:
        name = "LowerOrangeHazardPlacardIDType"


@dataclass(frozen=True)
class LowerTenderAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class MandateTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ManufactureDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ManufactureTimeType(TimeType):
    pass


@dataclass(frozen=True)
class MarkAttentionIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class MarkAttentionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MarkCareIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class MarkCareType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MarketValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class MarkingIdtype(IdentifierType):
    class Meta:
        name = "MarkingIDType"


@dataclass(frozen=True)
class MathematicOperatorCodeType(CodeType):
    pass


@dataclass(frozen=True)
class MaximumAdvertisementAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class MaximumAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class MaximumBackorderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MaximumCopiesNumericType(NumericType):
    pass


@dataclass(frozen=True)
class MaximumMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class MaximumNumberNumericType(NumericType):
    pass


@dataclass(frozen=True)
class MaximumOperatorQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MaximumOrderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MaximumPaidAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class MaximumPaymentInstructionsNumericType(NumericType):
    pass


@dataclass(frozen=True)
class MaximumPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class MaximumQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MaximumValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MaximumVariantQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class MedicalFirstAidGuideCodeType(CodeType):
    pass


@dataclass(frozen=True)
class MeterConstantCodeType(CodeType):
    pass


@dataclass(frozen=True)
class MeterConstantType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MeterNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MeterNumberType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MeterReadingCommentsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MeterReadingTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class MeterReadingTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MiddleNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class MimeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class MinimumAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class MinimumBackorderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MinimumImprovementBidType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MinimumInventoryQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MinimumMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class MinimumNumberNumericType(NumericType):
    pass


@dataclass(frozen=True)
class MinimumOrderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MinimumPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class MinimumQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MinimumValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MiscellaneousEventTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ModelNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class MonetaryScopeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MovieTitleType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class MultipleOrderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class MultiplierFactorNumericType(NumericType):
    pass


@dataclass(frozen=True)
class NameCodeType(CodeType):
    pass


@dataclass(frozen=True)
class NameSuffixType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class NameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class NationalityIdtype(IdentifierType):
    class Meta:
        name = "NationalityIDType"


@dataclass(frozen=True)
class NatureCodeType(CodeType):
    pass


@dataclass(frozen=True)
class NegotiationDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class NetNetWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class NetTonnageMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class NetVolumeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class NetWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class NetworkIdtype(IdentifierType):
    class Meta:
        name = "NetworkIDType"


@dataclass(frozen=True)
class NominationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class NominationTimeType(TimeType):
    pass


@dataclass(frozen=True)
class NormalTemperatureReductionQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True)
class NoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class NotificationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class OccurrenceDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class OccurrenceTimeType(TimeType):
    pass


@dataclass(frozen=True)
class OnCarriageIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class OneTimeChargeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class OneTimeChargeTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class OntologyUritype(IdentifierType):
    class Meta:
        name = "OntologyURIType"


@dataclass(frozen=True)
class OpenTenderIdtype(IdentifierType):
    class Meta:
        name = "OpenTenderIDType"


@dataclass(frozen=True)
class OperatingYearsQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class OptionalLineItemIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class OptionsDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class OrderIntervalDaysNumericType(NumericType):
    pass


@dataclass(frozen=True)
class OrderQuantityIncrementNumericType(NumericType):
    pass


@dataclass(frozen=True)
class OrderResponseCodeType(CodeType):
    pass


@dataclass(frozen=True)
class OrderTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class OrderableIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class OrderableUnitFactorRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True)
class OrderableUnitType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class OrganizationDepartmentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class OriginalContractingSystemIdtype(IdentifierType):
    class Meta:
        name = "OriginalContractingSystemIDType"


@dataclass(frozen=True)
class OriginalJobIdtype(IdentifierType):
    class Meta:
        name = "OriginalJobIDType"


@dataclass(frozen=True)
class OtherConditionsIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class OtherInstructionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class OtherNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class OutstandingQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class OutstandingReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class OversupplyQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class OwnerTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PackLevelCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PackQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class PackSizeNumericType(NumericType):
    pass


@dataclass(frozen=True)
class PackageLevelCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PackagingTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PackingCriteriaCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PackingMaterialType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PaidAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class PaidDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class PaidTimeType(TimeType):
    pass


@dataclass(frozen=True)
class ParentDocumentIdtype(IdentifierType):
    class Meta:
        name = "ParentDocumentIDType"


@dataclass(frozen=True)
class ParentDocumentLineReferenceIdtype(IdentifierType):
    class Meta:
        name = "ParentDocumentLineReferenceIDType"


@dataclass(frozen=True)
class ParentDocumentTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ParentDocumentVersionIdtype(IdentifierType):
    class Meta:
        name = "ParentDocumentVersionIDType"


@dataclass(frozen=True)
class PartPresentationCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PartecipationPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class PartialDeliveryIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ParticipationPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class PartyCapacityAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class PartyTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PartyTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PassengerQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class PasswordType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PayPerViewType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PayableAlternativeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class PayableAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class PayableRoundingAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class PayerReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PaymentAlternativeCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PaymentChannelCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PaymentCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PaymentDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PaymentDueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class PaymentFrequencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PaymentIdtype(IdentifierType):
    class Meta:
        name = "PaymentIDType"


@dataclass(frozen=True)
class PaymentMeansCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PaymentMeansIdtype(IdentifierType):
    class Meta:
        name = "PaymentMeansIDType"


@dataclass(frozen=True)
class PaymentNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PaymentOrderReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PaymentPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class PaymentPurposeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PaymentTermsDetailsUritype(IdentifierType):
    class Meta:
        name = "PaymentTermsDetailsURIType"


@dataclass(frozen=True)
class PenaltyAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class PenaltySurchargePercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class PerUnitAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class PercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class PerformanceMetricTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PerformanceValueQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class PerformingCarrierAssignedIdtype(IdentifierType):
    class Meta:
        name = "PerformingCarrierAssignedIDType"


@dataclass(frozen=True)
class PersonalSituationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PhoneNumberType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PlacardEndorsementType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PlacardNotationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PlannedDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class PlotIdentificationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PositionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PostEventNotificationDurationMeasureType(
    UblUnqualifiedDataTypes21MeasureType
):
    pass


@dataclass(frozen=True)
class PostalZoneType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PostboxType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PowerIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class PreCarriageIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class PreEventNotificationDurationMeasureType(
    UblUnqualifiedDataTypes21MeasureType
):
    pass


@dataclass(frozen=True)
class PreferenceCriterionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PrepaidAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class PrepaidIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class PrepaidPaymentReferenceIdtype(IdentifierType):
    class Meta:
        name = "PrepaidPaymentReferenceIDType"


@dataclass(frozen=True)
class PreviousCancellationReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PreviousJobIdtype(IdentifierType):
    class Meta:
        name = "PreviousJobIDType"


@dataclass(frozen=True)
class PreviousMeterQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class PreviousMeterReadingDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class PreviousMeterReadingMethodCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PreviousMeterReadingMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PreviousVersionIdtype(IdentifierType):
    class Meta:
        name = "PreviousVersionIDType"


@dataclass(frozen=True)
class PriceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class PriceChangeReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PriceEvaluationCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PriceRevisionFormulaDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PriceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PriceTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PricingCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PricingUpdateRequestIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class PrimaryAccountNumberIdtype(IdentifierType):
    class Meta:
        name = "PrimaryAccountNumberIDType"


@dataclass(frozen=True)
class PrintQualifierType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PriorityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PrivacyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PrizeDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class PrizeIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ProcedureCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ProcessDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ProcessReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ProcessReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ProcurementSubTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ProcurementTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ProductTraceIdtype(IdentifierType):
    class Meta:
        name = "ProductTraceIDType"


@dataclass(frozen=True)
class ProfileExecutionIdtype(IdentifierType):
    class Meta:
        name = "ProfileExecutionIDType"


@dataclass(frozen=True)
class ProfileIdtype(IdentifierType):
    class Meta:
        name = "ProfileIDType"


@dataclass(frozen=True)
class ProfileStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ProgressPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class PromotionalEventTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ProviderTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PublishAwardIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class PurposeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class PurposeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class QualityControlCodeType(CodeType):
    pass


@dataclass(frozen=True)
class QuantityDiscrepancyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class QuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class RadioCallSignIdtype(IdentifierType):
    class Meta:
        name = "RadioCallSignIDType"


@dataclass(frozen=True)
class RailCarIdtype(IdentifierType):
    class Meta:
        name = "RailCarIDType"


@dataclass(frozen=True)
class RankType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class RateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True)
class ReceiptAdviceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ReceivedDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ReceivedElectronicTenderQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True)
class ReceivedForeignTenderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ReceivedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ReceivedTenderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ReferenceDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ReferenceEventCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ReferenceIdtype(IdentifierType):
    class Meta:
        name = "ReferenceIDType"


@dataclass(frozen=True)
class ReferenceTimeType(TimeType):
    pass


@dataclass(frozen=True)
class ReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ReferencedConsignmentIdtype(IdentifierType):
    class Meta:
        name = "ReferencedConsignmentIDType"


@dataclass(frozen=True)
class RefrigeratedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class RefrigerationOnIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class RegionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class RegisteredDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class RegisteredTimeType(TimeType):
    pass


@dataclass(frozen=True)
class RegistrationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class RegistrationExpirationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class RegistrationIdtype(IdentifierType):
    class Meta:
        name = "RegistrationIDType"


@dataclass(frozen=True)
class RegistrationNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class RegistrationNationalityIdtype(IdentifierType):
    class Meta:
        name = "RegistrationNationalityIDType"


@dataclass(frozen=True)
class RegistrationNationalityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class RegulatoryDomainType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class RejectActionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class RejectReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class RejectReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class RejectedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class RejectionNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ReleaseIdtype(IdentifierType):
    class Meta:
        name = "ReleaseIDType"


@dataclass(frozen=True)
class ReliabilityPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class RemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ReminderSequenceNumericType(NumericType):
    pass


@dataclass(frozen=True)
class ReminderTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ReplenishmentOwnerDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class RequestForQuotationLineIdtype(IdentifierType):
    class Meta:
        name = "RequestForQuotationLineIDType"


@dataclass(frozen=True)
class RequestedDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class RequestedDespatchDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class RequestedDespatchTimeType(TimeType):
    pass


@dataclass(frozen=True)
class RequestedInvoiceCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class RequestedPublicationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class RequiredCurriculaIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class RequiredCustomsIdtype(IdentifierType):
    class Meta:
        name = "RequiredCustomsIDType"


@dataclass(frozen=True)
class RequiredDeliveryDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class RequiredDeliveryTimeType(TimeType):
    pass


@dataclass(frozen=True)
class RequiredFeeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class ResidenceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ResidenceTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ResidentOccupantsNumericType(NumericType):
    pass


@dataclass(frozen=True)
class ResolutionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ResolutionDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ResolutionTimeType(TimeType):
    pass


@dataclass(frozen=True)
class ResolutionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ResponseCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ResponseDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ResponseTimeType(TimeType):
    pass


@dataclass(frozen=True)
class RetailEventNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class RetailEventStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ReturnabilityIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ReturnableMaterialIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ReturnableQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class RevisedForecastLineIdtype(IdentifierType):
    class Meta:
        name = "RevisedForecastLineIDType"


@dataclass(frozen=True)
class RevisionDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class RevisionStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class RevisionTimeType(TimeType):
    pass


@dataclass(frozen=True)
class RoamingPartnerNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class RoleCodeType(CodeType):
    pass


@dataclass(frozen=True)
class RoleDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class RoomType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class RoundingAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class SalesOrderIdtype(IdentifierType):
    class Meta:
        name = "SalesOrderIDType"


@dataclass(frozen=True)
class SalesOrderLineIdtype(IdentifierType):
    class Meta:
        name = "SalesOrderLineIDType"


@dataclass(frozen=True)
class SchemeUritype(IdentifierType):
    class Meta:
        name = "SchemeURIType"


@dataclass(frozen=True)
class SealIssuerTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SealStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SealingPartyTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class SecurityClassificationCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SecurityIdtype(IdentifierType):
    class Meta:
        name = "SecurityIDType"


@dataclass(frozen=True)
class SellerEventIdtype(IdentifierType):
    class Meta:
        name = "SellerEventIDType"


@dataclass(frozen=True)
class SequenceIdtype(IdentifierType):
    class Meta:
        name = "SequenceIDType"


@dataclass(frozen=True)
class SequenceNumberIdtype(IdentifierType):
    class Meta:
        name = "SequenceNumberIDType"


@dataclass(frozen=True)
class SequenceNumericType(NumericType):
    pass


@dataclass(frozen=True)
class SerialIdtype(IdentifierType):
    class Meta:
        name = "SerialIDType"


@dataclass(frozen=True)
class ServiceInformationPreferenceCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ServiceNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class ServiceNumberCalledType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ServiceTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ServiceTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class SettlementDiscountAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class SettlementDiscountPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class SharesNumberQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ShippingMarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ShippingOrderIdtype(IdentifierType):
    class Meta:
        name = "ShippingOrderIDType"


@dataclass(frozen=True)
class ShippingPriorityLevelCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ShipsRequirementsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ShortQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ShortageActionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SignatureIdtype(IdentifierType):
    class Meta:
        name = "SignatureIDType"


@dataclass(frozen=True)
class SignatureMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class SizeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SoleProprietorshipIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class SourceCurrencyBaseRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True)
class SourceCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SourceForecastIssueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class SourceForecastIssueTimeType(TimeType):
    pass


@dataclass(frozen=True)
class SourceValueMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class SpecialInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class SpecialSecurityIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class SpecialServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class SpecialTermsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class SpecialTransportRequirementsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class SpecificationIdtype(IdentifierType):
    class Meta:
        name = "SpecificationIDType"


@dataclass(frozen=True)
class SpecificationTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SplitConsignmentIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class StartDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class StartTimeType(TimeType):
    pass


@dataclass(frozen=True)
class StatementTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class StatusAvailableIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class StatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class StatusReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class StatusReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class StreetNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class SubcontractingConditionsCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SubmissionDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class SubmissionDueDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class SubmissionMethodCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SubscriberIdtype(IdentifierType):
    class Meta:
        name = "SubscriberIDType"


@dataclass(frozen=True)
class SubscriberTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SubscriberTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class SubstitutionStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class SuccessiveSequenceIdtype(IdentifierType):
    class Meta:
        name = "SuccessiveSequenceIDType"


@dataclass(frozen=True)
class SummaryDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class SupplierAssignedAccountIdtype(IdentifierType):
    class Meta:
        name = "SupplierAssignedAccountIDType"


@dataclass(frozen=True)
class SupplyChainActivityTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TareWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class TargetCurrencyBaseRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass(frozen=True)
class TargetCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TargetInventoryQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class TargetServicePercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class TariffClassCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TariffCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TariffDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TaxAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TaxCurrencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TaxEnergyAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TaxEnergyBalanceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TaxEnergyOnAccountAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TaxEvidenceIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class TaxExclusiveAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TaxExemptionReasonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TaxExemptionReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TaxIncludedIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class TaxInclusiveAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TaxLevelCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TaxPointDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class TaxTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TaxableAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TechnicalCommitteeDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TechnicalNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class TelecommunicationsServiceCallCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TelecommunicationsServiceCallType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TelecommunicationsServiceCategoryCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TelecommunicationsServiceCategoryType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TelecommunicationsSupplyTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TelecommunicationsSupplyTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TelefaxType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TelephoneType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TenderEnvelopeIdtype(IdentifierType):
    class Meta:
        name = "TenderEnvelopeIDType"


@dataclass(frozen=True)
class TenderEnvelopeTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TenderResultCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TenderTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TendererRequirementTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TendererRoleCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TestMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TextType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ThirdPartyPayerIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class ThresholdAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class ThresholdQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ThresholdValueComparisonCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TierRangeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TierRatePercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass(frozen=True)
class TimeAmountType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TimeDeltaDaysQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class TimeFrequencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TimezoneOffsetType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TimingComplaintCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TimingComplaintType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TitleType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ToOrderIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class TotalAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TotalBalanceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TotalConsumedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class TotalCreditAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TotalDebitAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TotalDeliveredQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class TotalGoodsItemQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class TotalInvoiceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TotalMeteredQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class TotalPackageQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class TotalPackagesQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class TotalPaymentAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TotalTaskAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TotalTaxAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TotalTransportHandlingUnitQuantityType(
    UblUnqualifiedDataTypes21QuantityType
):
    pass


@dataclass(frozen=True)
class TraceIdtype(IdentifierType):
    class Meta:
        name = "TraceIDType"


@dataclass(frozen=True)
class TrackingDeviceCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TrackingIdtype(IdentifierType):
    class Meta:
        name = "TrackingIDType"


@dataclass(frozen=True)
class TradeItemPackingLabelingTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TradeServiceCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TradingRestrictionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TrainIdtype(IdentifierType):
    class Meta:
        name = "TrainIDType"


@dataclass(frozen=True)
class TransactionCurrencyTaxAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class TransitDirectionCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportAuthorizationCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportEmergencyCardCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportEquipmentTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportEventTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportExecutionPlanReferenceIdtype(IdentifierType):
    class Meta:
        name = "TransportExecutionPlanReferenceIDType"


@dataclass(frozen=True)
class TransportExecutionStatusCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportHandlingUnitTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportMeansTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportModeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportServiceCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TransportServiceProviderRemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TransportServiceProviderSpecialTermsType(
    UblUnqualifiedDataTypes21TextType
):
    pass


@dataclass(frozen=True)
class TransportUserRemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TransportUserSpecialTermsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TransportationServiceDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class TransportationServiceDetailsUritype(IdentifierType):
    class Meta:
        name = "TransportationServiceDetailsURIType"


@dataclass(frozen=True)
class TransportationStatusTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class TypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class UblversionIdtype(IdentifierType):
    class Meta:
        name = "UBLVersionIDType"


@dataclass(frozen=True)
class UndgcodeType(CodeType):
    class Meta:
        name = "UNDGCodeType"


@dataclass(frozen=True)
class Uritype(IdentifierType):
    class Meta:
        name = "URIType"


@dataclass(frozen=True)
class Uuidtype(IdentifierType):
    class Meta:
        name = "UUIDType"


@dataclass(frozen=True)
class UnknownPriceIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class UpperOrangeHazardPlacardIdtype(IdentifierType):
    class Meta:
        name = "UpperOrangeHazardPlacardIDType"


@dataclass(frozen=True)
class UrgencyCodeType(CodeType):
    pass


@dataclass(frozen=True)
class UtilityStatementTypeCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ValidateProcessType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ValidateToolType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ValidateToolVersionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ValidationDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ValidationResultCodeType(CodeType):
    pass


@dataclass(frozen=True)
class ValidationTimeType(TimeType):
    pass


@dataclass(frozen=True)
class ValidatorIdtype(IdentifierType):
    class Meta:
        name = "ValidatorIDType"


@dataclass(frozen=True)
class ValidityStartDateType(UblUnqualifiedDataTypes21DateType):
    pass


@dataclass(frozen=True)
class ValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass(frozen=True)
class ValueMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass(frozen=True)
class ValueQualifierType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class ValueQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class ValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class VarianceQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass(frozen=True)
class VariantConstraintIndicatorType(IndicatorType):
    pass


@dataclass(frozen=True)
class VariantIdtype(IdentifierType):
    class Meta:
        name = "VariantIDType"


@dataclass(frozen=True)
class VersionIdtype(IdentifierType):
    class Meta:
        name = "VersionIDType"


@dataclass(frozen=True)
class VesselIdtype(IdentifierType):
    class Meta:
        name = "VesselIDType"


@dataclass(frozen=True)
class VesselNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass(frozen=True)
class WarrantyInformationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class WebsiteUritype(IdentifierType):
    class Meta:
        name = "WebsiteURIType"


@dataclass(frozen=True)
class WeekDayCodeType(CodeType):
    pass


@dataclass(frozen=True)
class WeightNumericType(NumericType):
    pass


@dataclass(frozen=True)
class WeightType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class WeightingAlgorithmCodeType(CodeType):
    pass


@dataclass(frozen=True)
class WorkPhaseCodeType(CodeType):
    pass


@dataclass(frozen=True)
class WorkPhaseType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass(frozen=True)
class XpathType(UblUnqualifiedDataTypes21TextType):
    class Meta:
        name = "XPathType"


@dataclass(frozen=True)
class AcceptedIndicator(AcceptedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AcceptedVariantsDescription(AcceptedVariantsDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AccountFormatCode(AccountFormatCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AccountId(AccountIdtype):
    class Meta:
        name = "AccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AccountTypeCode(AccountTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AccountingCost(AccountingCostType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AccountingCostCode(AccountingCostCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActionCode(ActionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActivityType(ActivityTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActivityTypeCode(ActivityTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActualDeliveryDate(ActualDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActualDeliveryTime(ActualDeliveryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActualDespatchDate(ActualDespatchDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActualDespatchTime(ActualDespatchTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActualPickupDate(ActualPickupDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActualPickupTime(ActualPickupTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ActualTemperatureReductionQuantity(
    ActualTemperatureReductionQuantityType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AdValoremIndicator(AdValoremIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AdditionalAccountId(AdditionalAccountIdtype):
    class Meta:
        name = "AdditionalAccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AdditionalConditions(AdditionalConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AdditionalInformation(AdditionalInformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AdditionalStreetName(AdditionalStreetNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AddressFormatCode(AddressFormatCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AddressTypeCode(AddressTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AdjustmentReasonCode(AdjustmentReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AdmissionCode(AdmissionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AdvertisementAmount(AdvertisementAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AgencyId(AgencyIdtype):
    class Meta:
        name = "AgencyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AgencyName(AgencyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AirFlowPercent(AirFlowPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AircraftId(AircraftIdtype):
    class Meta:
        name = "AircraftID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AliasName(AliasNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AllowanceChargeReason(AllowanceChargeReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AllowanceChargeReasonCode(AllowanceChargeReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AllowanceTotalAmount(AllowanceTotalAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AltitudeMeasure(AltitudeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Amount(AmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AmountRate(AmountRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AnimalFoodApprovedIndicator(AnimalFoodApprovedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AnimalFoodIndicator(AnimalFoodIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AnnualAverageAmount(AnnualAverageAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ApplicationStatusCode(ApplicationStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ApprovalDate(ApprovalDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ApprovalStatus(ApprovalStatusType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AttributeId(AttributeIdtype):
    class Meta:
        name = "AttributeID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AuctionConstraintIndicator(AuctionConstraintIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AuctionUri(AuctionUritype):
    class Meta:
        name = "AuctionURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AvailabilityDate(AvailabilityDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AvailabilityStatusCode(AvailabilityStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AverageAmount(AverageAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AverageSubsequentContractAmount(AverageSubsequentContractAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AwardDate(AwardDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AwardTime(AwardTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AwardingCriterionDescription(AwardingCriterionDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AwardingCriterionId(AwardingCriterionIdtype):
    class Meta:
        name = "AwardingCriterionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AwardingCriterionTypeCode(AwardingCriterionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class AwardingMethodTypeCode(AwardingMethodTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BackOrderAllowedIndicator(BackOrderAllowedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BackorderQuantity(BackorderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BackorderReason(BackorderReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BalanceAmount(BalanceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BalanceBroughtForwardIndicator(BalanceBroughtForwardIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BarcodeSymbologyId(BarcodeSymbologyIdtype):
    class Meta:
        name = "BarcodeSymbologyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BaseAmount(BaseAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BaseQuantity(BaseQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BaseUnitMeasure(BaseUnitMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BasedOnConsensusIndicator(BasedOnConsensusIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BasicConsumedQuantity(BasicConsumedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BatchQuantity(BatchQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BestBeforeDate(BestBeforeDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BindingOnBuyerIndicator(BindingOnBuyerIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BirthDate(BirthDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BirthplaceName(BirthplaceNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BlockName(BlockNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BrandName(BrandNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BrokerAssignedId(BrokerAssignedIdtype):
    class Meta:
        name = "BrokerAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BudgetYearNumeric(BudgetYearNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BuildingName(BuildingNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BuildingNumber(BuildingNumberType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BulkCargoIndicator(BulkCargoIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BusinessClassificationEvidenceId(BusinessClassificationEvidenceIdtype):
    class Meta:
        name = "BusinessClassificationEvidenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BusinessIdentityEvidenceId(BusinessIdentityEvidenceIdtype):
    class Meta:
        name = "BusinessIdentityEvidenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BuyerEventId(BuyerEventIdtype):
    class Meta:
        name = "BuyerEventID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BuyerProfileUri(BuyerProfileUritype):
    class Meta:
        name = "BuyerProfileURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class BuyerReference(BuyerReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Cv2Id(Cv2Idtype):
    class Meta:
        name = "CV2ID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CalculationExpression(CalculationExpressionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CalculationExpressionCode(CalculationExpressionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CalculationMethodCode(CalculationMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CalculationRate(CalculationRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CalculationSequenceNumeric(CalculationSequenceNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CallBaseAmount(CallBaseAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CallDate(CallDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CallExtensionAmount(CallExtensionAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CallTime(CallTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CancellationNote(CancellationNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CandidateReductionConstraintIndicator(
    CandidateReductionConstraintIndicatorType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CandidateStatement(CandidateStatementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CanonicalizationMethod(CanonicalizationMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CapabilityTypeCode(CapabilityTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CardChipCode(CardChipCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CardTypeCode(CardTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CargoTypeCode(CargoTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CarrierAssignedId(CarrierAssignedIdtype):
    class Meta:
        name = "CarrierAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CarrierServiceInstructions(CarrierServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CatalogueIndicator(CatalogueIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CategoryName(CategoryNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CertificateType(CertificateTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CertificateTypeCode(CertificateTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ChangeConditions(ChangeConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Channel(ChannelType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ChannelCode(ChannelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CharacterSetCode(CharacterSetCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Characteristics(CharacteristicsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ChargeIndicator(ChargeIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ChargeTotalAmount(ChargeTotalAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ChargeableQuantity(ChargeableQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ChargeableWeightMeasure(ChargeableWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ChildConsignmentQuantity(ChildConsignmentQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ChipApplicationId(ChipApplicationIdtype):
    class Meta:
        name = "ChipApplicationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CityName(CityNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CitySubdivisionName(CitySubdivisionNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CodeValue(CodeValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CollaborationPriorityCode(CollaborationPriorityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Comment(CommentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CommodityCode(CommodityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CompanyId(CompanyIdtype):
    class Meta:
        name = "CompanyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CompanyLegalForm(CompanyLegalFormType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CompanyLegalFormCode(CompanyLegalFormCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CompanyLiquidationStatusCode(CompanyLiquidationStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ComparedValueMeasure(ComparedValueMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ComparisonDataCode(ComparisonDataCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ComparisonDataSourceCode(ComparisonDataSourceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ComparisonForecastIssueDate(ComparisonForecastIssueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ComparisonForecastIssueTime(ComparisonForecastIssueTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CompletionIndicator(CompletionIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Condition(ConditionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConditionCode(ConditionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Conditions(ConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConditionsDescription(ConditionsDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsigneeAssignedId(ConsigneeAssignedIdtype):
    class Meta:
        name = "ConsigneeAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsignmentQuantity(ConsignmentQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsignorAssignedId(ConsignorAssignedIdtype):
    class Meta:
        name = "ConsignorAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsolidatableIndicator(ConsolidatableIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConstitutionCode(ConstitutionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumerIncentiveTacticTypeCode(ConsumerIncentiveTacticTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumerUnitQuantity(ConsumerUnitQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumersEnergyLevel(ConsumersEnergyLevelType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumersEnergyLevelCode(ConsumersEnergyLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumptionEnergyQuantity(ConsumptionEnergyQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumptionId(ConsumptionIdtype):
    class Meta:
        name = "ConsumptionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumptionLevel(ConsumptionLevelType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumptionLevelCode(ConsumptionLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumptionReportId(ConsumptionReportIdtype):
    class Meta:
        name = "ConsumptionReportID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumptionType(ConsumptionTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumptionTypeCode(ConsumptionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ConsumptionWaterQuantity(ConsumptionWaterQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ContainerizedIndicator(ContainerizedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Content(ContentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ContentUnitQuantity(ContentUnitQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ContractFolderId(ContractFolderIdtype):
    class Meta:
        name = "ContractFolderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ContractName(ContractNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ContractSubdivision(ContractSubdivisionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ContractType(ContractTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ContractTypeCode(ContractTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ContractedCarrierAssignedId(ContractedCarrierAssignedIdtype):
    class Meta:
        name = "ContractedCarrierAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ContractingSystemCode(ContractingSystemCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CoordinateSystemCode(CoordinateSystemCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CopyIndicator(CopyIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CorporateRegistrationTypeCode(CorporateRegistrationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CorporateStockAmount(CorporateStockAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CorrectionAmount(CorrectionAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CorrectionType(CorrectionTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CorrectionTypeCode(CorrectionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CorrectionUnitAmount(CorrectionUnitAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CountrySubentity(CountrySubentityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CountrySubentityCode(CountrySubentityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CreditLineAmount(CreditLineAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CreditNoteTypeCode(CreditNoteTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CreditedQuantity(CreditedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CrewQuantity(CrewQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CurrencyCode(CurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CurrentChargeType(CurrentChargeTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CurrentChargeTypeCode(CurrentChargeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CustomerAssignedAccountId(CustomerAssignedAccountIdtype):
    class Meta:
        name = "CustomerAssignedAccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CustomerReference(CustomerReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CustomizationId(CustomizationIdtype):
    class Meta:
        name = "CustomizationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CustomsClearanceServiceInstructions(
    CustomsClearanceServiceInstructionsType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CustomsImportClassifiedIndicator(CustomsImportClassifiedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CustomsStatusCode(CustomsStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class CustomsTariffQuantity(CustomsTariffQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DamageRemarks(DamageRemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DangerousGoodsApprovedIndicator(DangerousGoodsApprovedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DataSendingCapability(DataSendingCapabilityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DataSourceCode(DataSourceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Date(DateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DebitLineAmount(DebitLineAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DebitedQuantity(DebitedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DeclarationTypeCode(DeclarationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DeclaredCarriageValueAmount(DeclaredCarriageValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DeclaredCustomsValueAmount(DeclaredCustomsValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DeclaredForCarriageValueAmount(DeclaredForCarriageValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DeclaredStatisticsValueAmount(DeclaredStatisticsValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DeliveredQuantity(DeliveredQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DeliveryInstructions(DeliveryInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DemurrageInstructions(DemurrageInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Department(DepartmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Description(DescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DescriptionCode(DescriptionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DespatchAdviceTypeCode(DespatchAdviceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DifferenceTemperatureReductionQuantity(
    DifferenceTemperatureReductionQuantityType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DirectionCode(DirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DisplayTacticTypeCode(DisplayTacticTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DispositionCode(DispositionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class District(DistrictType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentCurrencyCode(DocumentCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentDescription(DocumentDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentHash(DocumentHashType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentId(DocumentIdtype):
    class Meta:
        name = "DocumentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentStatusCode(DocumentStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentStatusReasonCode(DocumentStatusReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentStatusReasonDescription(DocumentStatusReasonDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentType(DocumentTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentTypeCode(DocumentTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DocumentationFeeAmount(DocumentationFeeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DueDate(DueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DurationMeasure(DurationMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Duty(DutyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class DutyCode(DutyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EarliestPickupDate(EarliestPickupDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EarliestPickupTime(EarliestPickupTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EconomicOperatorRegistryUri(EconomicOperatorRegistryUritype):
    class Meta:
        name = "EconomicOperatorRegistryURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EffectiveDate(EffectiveDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EffectiveTime(EffectiveTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ElectronicDeviceDescription(ElectronicDeviceDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ElectronicMail(ElectronicMailType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EmbeddedDocumentBinaryObject(EmbeddedDocumentBinaryObjectType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EmergencyProceduresCode(EmergencyProceduresCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EmployeeQuantity(EmployeeQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EncodingCode(EncodingCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EndDate(EndDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EndTime(EndTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EndpointId(EndpointIdtype):
    class Meta:
        name = "EndpointID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EnvironmentalEmissionTypeCode(EnvironmentalEmissionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EstimatedAmount(EstimatedAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EstimatedConsumedQuantity(EstimatedConsumedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EstimatedDeliveryDate(EstimatedDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EstimatedDeliveryTime(EstimatedDeliveryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EstimatedDespatchDate(EstimatedDespatchDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EstimatedDespatchTime(EstimatedDespatchTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EstimatedOverallContractAmount(EstimatedOverallContractAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EstimatedOverallContractQuantity(EstimatedOverallContractQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EvaluationCriterionTypeCode(EvaluationCriterionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class EvidenceTypeCode(EvidenceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExceptionResolutionCode(ExceptionResolutionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExceptionStatusCode(ExceptionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExchangeMarketId(ExchangeMarketIdtype):
    class Meta:
        name = "ExchangeMarketID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExclusionReason(ExclusionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExecutionRequirementCode(ExecutionRequirementCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExemptionReason(ExemptionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExemptionReasonCode(ExemptionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExpectedOperatorQuantity(ExpectedOperatorQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExpectedQuantity(ExpectedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExpenseCode(ExpenseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExpiryDate(ExpiryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExpiryTime(ExpiryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Expression(ExpressionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExpressionCode(ExpressionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ExtendedId(ExtendedIdtype):
    class Meta:
        name = "ExtendedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Extension(ExtensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FaceValueAmount(FaceValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FamilyName(FamilyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FeatureTacticTypeCode(FeatureTacticTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FeeAmount(FeeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FeeDescription(FeeDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FileName(FileNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FinancingInstrumentCode(FinancingInstrumentCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FirstName(FirstNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FirstShipmentAvailibilityDate(FirstShipmentAvailibilityDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Floor(FloorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FollowupContractIndicator(FollowupContractIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ForecastPurposeCode(ForecastPurposeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ForecastTypeCode(ForecastTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FormatCode(FormatCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ForwarderServiceInstructions(ForwarderServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FreeOfChargeIndicator(FreeOfChargeIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FreeOnBoardValueAmount(FreeOnBoardValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FreightForwarderAssignedId(FreightForwarderAssignedIdtype):
    class Meta:
        name = "FreightForwarderAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FreightRateClassCode(FreightRateClassCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Frequency(FrequencyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FrozenDocumentIndicator(FrozenDocumentIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FrozenPeriodDaysNumeric(FrozenPeriodDaysNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FullnessIndicationCode(FullnessIndicationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FullyPaidSharesIndicator(FullyPaidSharesIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FundingProgram(FundingProgramType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class FundingProgramCode(FundingProgramCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GasPressureQuantity(GasPressureQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GenderCode(GenderCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GeneralCargoIndicator(GeneralCargoIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GovernmentAgreementConstraintIndicator(
    GovernmentAgreementConstraintIndicatorType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GrossTonnageMeasure(GrossTonnageMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GrossVolumeMeasure(GrossVolumeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GrossWeightMeasure(GrossWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GuaranteeTypeCode(GuaranteeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GuaranteedDespatchDate(GuaranteedDespatchDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class GuaranteedDespatchTime(GuaranteedDespatchTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HandlingCode(HandlingCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HandlingInstructions(HandlingInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HashAlgorithmMethod(HashAlgorithmMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HaulageInstructions(HaulageInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HazardClassId(HazardClassIdtype):
    class Meta:
        name = "HazardClassID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HazardousCategoryCode(HazardousCategoryCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HazardousRegulationCode(HazardousRegulationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HazardousRiskIndicator(HazardousRiskIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HeatingType(HeatingTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HeatingTypeCode(HeatingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HigherTenderAmount(HigherTenderAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HolderName(HolderNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HumanFoodApprovedIndicator(HumanFoodApprovedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HumanFoodIndicator(HumanFoodIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class HumidityPercent(HumidityPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Id(Idtype):
    class Meta:
        name = "ID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class IdentificationCode(IdentificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class IdentificationId(IdentificationIdtype):
    class Meta:
        name = "IdentificationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ImmobilizationCertificateId(ImmobilizationCertificateIdtype):
    class Meta:
        name = "ImmobilizationCertificateID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ImportanceCode(ImportanceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class IndicationIndicator(IndicationIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class IndustryClassificationCode(IndustryClassificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Information(InformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InformationUri(InformationUritype):
    class Meta:
        name = "InformationURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InhalationToxicityZoneCode(InhalationToxicityZoneCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InhouseMail(InhouseMailType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InspectionMethodCode(InspectionMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InstallmentDueDate(InstallmentDueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InstructionId(InstructionIdtype):
    class Meta:
        name = "InstructionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InstructionNote(InstructionNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Instructions(InstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InsurancePremiumAmount(InsurancePremiumAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InsuranceValueAmount(InsuranceValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InventoryValueAmount(InventoryValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InvoiceTypeCode(InvoiceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InvoicedQuantity(InvoicedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class InvoicingPartyReference(InvoicingPartyReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class IssueDate(IssueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class IssueNumberId(IssueNumberIdtype):
    class Meta:
        name = "IssueNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class IssueTime(IssueTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class IssuerId(IssuerIdtype):
    class Meta:
        name = "IssuerID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ItemClassificationCode(ItemClassificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ItemUpdateRequestIndicator(ItemUpdateRequestIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class JobTitle(JobTitleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class JourneyId(JourneyIdtype):
    class Meta:
        name = "JourneyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Justification(JustificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class JustificationDescription(JustificationDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Keyword(KeywordType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LanguageId(LanguageIdtype):
    class Meta:
        name = "LanguageID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LastRevisionDate(LastRevisionDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LastRevisionTime(LastRevisionTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestDeliveryDate(LatestDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestDeliveryTime(LatestDeliveryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestMeterQuantity(LatestMeterQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestMeterReadingDate(LatestMeterReadingDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestMeterReadingMethod(LatestMeterReadingMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestMeterReadingMethodCode(LatestMeterReadingMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestPickupDate(LatestPickupDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestPickupTime(LatestPickupTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestProposalAcceptanceDate(LatestProposalAcceptanceDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatestSecurityClearanceDate(LatestSecurityClearanceDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatitudeDegreesMeasure(LatitudeDegreesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatitudeDirectionCode(LatitudeDirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LatitudeMinutesMeasure(LatitudeMinutesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LeadTimeMeasure(LeadTimeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LegalReference(LegalReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LegalStatusIndicator(LegalStatusIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LiabilityAmount(LiabilityAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LicensePlateId(LicensePlateIdtype):
    class Meta:
        name = "LicensePlateID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LifeCycleStatusCode(LifeCycleStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LimitationDescription(LimitationDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Line(LineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LineCountNumeric(LineCountNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LineExtensionAmount(LineExtensionAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LineId(LineIdtype):
    class Meta:
        name = "LineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LineNumberNumeric(LineNumberNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LineStatusCode(LineStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ListValue(ListValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LivestockIndicator(LivestockIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LoadingLengthMeasure(LoadingLengthMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LoadingSequenceId(LoadingSequenceIdtype):
    class Meta:
        name = "LoadingSequenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LocaleCode(LocaleCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Location(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LocationId(LocationIdtype):
    class Meta:
        name = "LocationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LocationTypeCode(LocationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Login(LoginType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LogoReferenceId(LogoReferenceIdtype):
    class Meta:
        name = "LogoReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LongitudeDegreesMeasure(LongitudeDegreesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LongitudeDirectionCode(LongitudeDirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LongitudeMinutesMeasure(LongitudeMinutesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LossRisk(LossRiskType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LossRiskResponsibilityCode(LossRiskResponsibilityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LotNumberId(LotNumberIdtype):
    class Meta:
        name = "LotNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LowTendersDescription(LowTendersDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LowerOrangeHazardPlacardId(LowerOrangeHazardPlacardIdtype):
    class Meta:
        name = "LowerOrangeHazardPlacardID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class LowerTenderAmount(LowerTenderAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MandateTypeCode(MandateTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ManufactureDate(ManufactureDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ManufactureTime(ManufactureTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MarkAttention(MarkAttentionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MarkAttentionIndicator(MarkAttentionIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MarkCare(MarkCareType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MarkCareIndicator(MarkCareIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MarketValueAmount(MarketValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MarkingId(MarkingIdtype):
    class Meta:
        name = "MarkingID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MathematicOperatorCode(MathematicOperatorCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumAdvertisementAmount(MaximumAdvertisementAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumAmount(MaximumAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumBackorderQuantity(MaximumBackorderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumCopiesNumeric(MaximumCopiesNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumMeasure(MaximumMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumNumberNumeric(MaximumNumberNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumOperatorQuantity(MaximumOperatorQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumOrderQuantity(MaximumOrderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumPaidAmount(MaximumPaidAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumPaymentInstructionsNumeric(MaximumPaymentInstructionsNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumPercent(MaximumPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumQuantity(MaximumQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumValue(MaximumValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MaximumVariantQuantity(MaximumVariantQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Measure(MeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MedicalFirstAidGuideCode(MedicalFirstAidGuideCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MeterConstant(MeterConstantType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MeterConstantCode(MeterConstantCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MeterName(MeterNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MeterNumber(MeterNumberType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MeterReadingComments(MeterReadingCommentsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MeterReadingType(MeterReadingTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MeterReadingTypeCode(MeterReadingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MiddleName(MiddleNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MimeCode(MimeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumAmount(MinimumAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumBackorderQuantity(MinimumBackorderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumImprovementBid(MinimumImprovementBidType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumInventoryQuantity(MinimumInventoryQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumMeasure(MinimumMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumNumberNumeric(MinimumNumberNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumOrderQuantity(MinimumOrderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumPercent(MinimumPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumQuantity(MinimumQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MinimumValue(MinimumValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MiscellaneousEventTypeCode(MiscellaneousEventTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ModelName(ModelNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MonetaryScope(MonetaryScopeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MovieTitle(MovieTitleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MultipleOrderQuantity(MultipleOrderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class MultiplierFactorNumeric(MultiplierFactorNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Name(NameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NameCode(NameCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NameSuffix(NameSuffixType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NationalityId(NationalityIdtype):
    class Meta:
        name = "NationalityID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NatureCode(NatureCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NegotiationDescription(NegotiationDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NetNetWeightMeasure(NetNetWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NetTonnageMeasure(NetTonnageMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NetVolumeMeasure(NetVolumeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NetWeightMeasure(NetWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NetworkId(NetworkIdtype):
    class Meta:
        name = "NetworkID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NominationDate(NominationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NominationTime(NominationTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NormalTemperatureReductionQuantity(
    NormalTemperatureReductionQuantityType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Note(NoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class NotificationTypeCode(NotificationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OccurrenceDate(OccurrenceDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OccurrenceTime(OccurrenceTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OnCarriageIndicator(OnCarriageIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OneTimeChargeType(OneTimeChargeTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OneTimeChargeTypeCode(OneTimeChargeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OntologyUri(OntologyUritype):
    class Meta:
        name = "OntologyURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OpenTenderId(OpenTenderIdtype):
    class Meta:
        name = "OpenTenderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OperatingYearsQuantity(OperatingYearsQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OptionalLineItemIndicator(OptionalLineItemIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OptionsDescription(OptionsDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OrderIntervalDaysNumeric(OrderIntervalDaysNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OrderQuantityIncrementNumeric(OrderQuantityIncrementNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OrderResponseCode(OrderResponseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OrderTypeCode(OrderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OrderableIndicator(OrderableIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OrderableUnit(OrderableUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OrderableUnitFactorRate(OrderableUnitFactorRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OrganizationDepartment(OrganizationDepartmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OriginalContractingSystemId(OriginalContractingSystemIdtype):
    class Meta:
        name = "OriginalContractingSystemID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OriginalJobId(OriginalJobIdtype):
    class Meta:
        name = "OriginalJobID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OtherConditionsIndicator(OtherConditionsIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OtherInstruction(OtherInstructionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OtherName(OtherNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OutstandingQuantity(OutstandingQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OutstandingReason(OutstandingReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OversupplyQuantity(OversupplyQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class OwnerTypeCode(OwnerTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PackLevelCode(PackLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PackQuantity(PackQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PackSizeNumeric(PackSizeNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PackageLevelCode(PackageLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PackagingTypeCode(PackagingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PackingCriteriaCode(PackingCriteriaCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PackingMaterial(PackingMaterialType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaidAmount(PaidAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaidDate(PaidDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaidTime(PaidTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ParentDocumentId(ParentDocumentIdtype):
    class Meta:
        name = "ParentDocumentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ParentDocumentLineReferenceId(ParentDocumentLineReferenceIdtype):
    class Meta:
        name = "ParentDocumentLineReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ParentDocumentTypeCode(ParentDocumentTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ParentDocumentVersionId(ParentDocumentVersionIdtype):
    class Meta:
        name = "ParentDocumentVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PartPresentationCode(PartPresentationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PartecipationPercent(PartecipationPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PartialDeliveryIndicator(PartialDeliveryIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ParticipationPercent(ParticipationPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PartyCapacityAmount(PartyCapacityAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PartyType(PartyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PartyTypeCode(PartyTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PassengerQuantity(PassengerQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Password(PasswordType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PayPerView(PayPerViewType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PayableAlternativeAmount(PayableAlternativeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PayableAmount(PayableAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PayableRoundingAmount(PayableRoundingAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PayerReference(PayerReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentAlternativeCurrencyCode(PaymentAlternativeCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentChannelCode(PaymentChannelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentCurrencyCode(PaymentCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentDescription(PaymentDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentDueDate(PaymentDueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentFrequencyCode(PaymentFrequencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentId(PaymentIdtype):
    class Meta:
        name = "PaymentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentMeansCode(PaymentMeansCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentMeansId(PaymentMeansIdtype):
    class Meta:
        name = "PaymentMeansID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentNote(PaymentNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentOrderReference(PaymentOrderReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentPercent(PaymentPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentPurposeCode(PaymentPurposeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PaymentTermsDetailsUri(PaymentTermsDetailsUritype):
    class Meta:
        name = "PaymentTermsDetailsURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PenaltyAmount(PenaltyAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PenaltySurchargePercent(PenaltySurchargePercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PerUnitAmount(PerUnitAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Percent(PercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PerformanceMetricTypeCode(PerformanceMetricTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PerformanceValueQuantity(PerformanceValueQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PerformingCarrierAssignedId(PerformingCarrierAssignedIdtype):
    class Meta:
        name = "PerformingCarrierAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PersonalSituation(PersonalSituationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PhoneNumber(PhoneNumberType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PlacardEndorsement(PlacardEndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PlacardNotation(PlacardNotationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PlannedDate(PlannedDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PlotIdentification(PlotIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PositionCode(PositionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PostEventNotificationDurationMeasure(
    PostEventNotificationDurationMeasureType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PostalZone(PostalZoneType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Postbox(PostboxType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PowerIndicator(PowerIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreCarriageIndicator(PreCarriageIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreEventNotificationDurationMeasure(
    PreEventNotificationDurationMeasureType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreferenceCriterionCode(PreferenceCriterionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PrepaidAmount(PrepaidAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PrepaidIndicator(PrepaidIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PrepaidPaymentReferenceId(PrepaidPaymentReferenceIdtype):
    class Meta:
        name = "PrepaidPaymentReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreviousCancellationReasonCode(PreviousCancellationReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreviousJobId(PreviousJobIdtype):
    class Meta:
        name = "PreviousJobID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreviousMeterQuantity(PreviousMeterQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreviousMeterReadingDate(PreviousMeterReadingDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreviousMeterReadingMethod(PreviousMeterReadingMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreviousMeterReadingMethodCode(PreviousMeterReadingMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PreviousVersionId(PreviousVersionIdtype):
    class Meta:
        name = "PreviousVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PriceAmount(PriceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PriceChangeReason(PriceChangeReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PriceEvaluationCode(PriceEvaluationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PriceRevisionFormulaDescription(PriceRevisionFormulaDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PriceType(PriceTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PriceTypeCode(PriceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PricingCurrencyCode(PricingCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PricingUpdateRequestIndicator(PricingUpdateRequestIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PrimaryAccountNumberId(PrimaryAccountNumberIdtype):
    class Meta:
        name = "PrimaryAccountNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PrintQualifier(PrintQualifierType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Priority(PriorityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PrivacyCode(PrivacyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PrizeDescription(PrizeDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PrizeIndicator(PrizeIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProcedureCode(ProcedureCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProcessDescription(ProcessDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProcessReason(ProcessReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProcessReasonCode(ProcessReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProcurementSubTypeCode(ProcurementSubTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProcurementTypeCode(ProcurementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProductTraceId(ProductTraceIdtype):
    class Meta:
        name = "ProductTraceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProfileExecutionId(ProfileExecutionIdtype):
    class Meta:
        name = "ProfileExecutionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProfileId(ProfileIdtype):
    class Meta:
        name = "ProfileID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProfileStatusCode(ProfileStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProgressPercent(ProgressPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PromotionalEventTypeCode(PromotionalEventTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ProviderTypeCode(ProviderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PublishAwardIndicator(PublishAwardIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Purpose(PurposeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class PurposeCode(PurposeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class QualityControlCode(QualityControlCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Quantity(QuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class QuantityDiscrepancyCode(QuantityDiscrepancyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RadioCallSignId(RadioCallSignIdtype):
    class Meta:
        name = "RadioCallSignID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RailCarId(RailCarIdtype):
    class Meta:
        name = "RailCarID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Rank(RankType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Rate(RateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReceiptAdviceTypeCode(ReceiptAdviceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReceivedDate(ReceivedDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReceivedElectronicTenderQuantity(ReceivedElectronicTenderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReceivedForeignTenderQuantity(ReceivedForeignTenderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReceivedQuantity(ReceivedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReceivedTenderQuantity(ReceivedTenderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Reference(ReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReferenceDate(ReferenceDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReferenceEventCode(ReferenceEventCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReferenceId(ReferenceIdtype):
    class Meta:
        name = "ReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReferenceTime(ReferenceTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReferencedConsignmentId(ReferencedConsignmentIdtype):
    class Meta:
        name = "ReferencedConsignmentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RefrigeratedIndicator(RefrigeratedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RefrigerationOnIndicator(RefrigerationOnIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Region(RegionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RegisteredDate(RegisteredDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RegisteredTime(RegisteredTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RegistrationDate(RegistrationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RegistrationExpirationDate(RegistrationExpirationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RegistrationId(RegistrationIdtype):
    class Meta:
        name = "RegistrationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RegistrationName(RegistrationNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RegistrationNationality(RegistrationNationalityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RegistrationNationalityId(RegistrationNationalityIdtype):
    class Meta:
        name = "RegistrationNationalityID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RegulatoryDomain(RegulatoryDomainType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RejectActionCode(RejectActionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RejectReason(RejectReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RejectReasonCode(RejectReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RejectedQuantity(RejectedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RejectionNote(RejectionNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReleaseId(ReleaseIdtype):
    class Meta:
        name = "ReleaseID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReliabilityPercent(ReliabilityPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Remarks(RemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReminderSequenceNumeric(ReminderSequenceNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReminderTypeCode(ReminderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReplenishmentOwnerDescription(ReplenishmentOwnerDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequestForQuotationLineId(RequestForQuotationLineIdtype):
    class Meta:
        name = "RequestForQuotationLineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequestedDeliveryDate(RequestedDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequestedDespatchDate(RequestedDespatchDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequestedDespatchTime(RequestedDespatchTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequestedInvoiceCurrencyCode(RequestedInvoiceCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequestedPublicationDate(RequestedPublicationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequiredCurriculaIndicator(RequiredCurriculaIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequiredCustomsId(RequiredCustomsIdtype):
    class Meta:
        name = "RequiredCustomsID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequiredDeliveryDate(RequiredDeliveryDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequiredDeliveryTime(RequiredDeliveryTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RequiredFeeAmount(RequiredFeeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ResidenceType(ResidenceTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ResidenceTypeCode(ResidenceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ResidentOccupantsNumeric(ResidentOccupantsNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Resolution(ResolutionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ResolutionCode(ResolutionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ResolutionDate(ResolutionDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ResolutionTime(ResolutionTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ResponseCode(ResponseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ResponseDate(ResponseDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ResponseTime(ResponseTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RetailEventName(RetailEventNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RetailEventStatusCode(RetailEventStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReturnabilityIndicator(ReturnabilityIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReturnableMaterialIndicator(ReturnableMaterialIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ReturnableQuantity(ReturnableQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RevisedForecastLineId(RevisedForecastLineIdtype):
    class Meta:
        name = "RevisedForecastLineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RevisionDate(RevisionDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RevisionStatusCode(RevisionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RevisionTime(RevisionTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RoamingPartnerName(RoamingPartnerNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RoleCode(RoleCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RoleDescription(RoleDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Room(RoomType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class RoundingAmount(RoundingAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SalesOrderId(SalesOrderIdtype):
    class Meta:
        name = "SalesOrderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SalesOrderLineId(SalesOrderLineIdtype):
    class Meta:
        name = "SalesOrderLineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SchemeUri(SchemeUritype):
    class Meta:
        name = "SchemeURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SealIssuerTypeCode(SealIssuerTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SealStatusCode(SealStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SealingPartyType(SealingPartyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SecurityClassificationCode(SecurityClassificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SecurityId(SecurityIdtype):
    class Meta:
        name = "SecurityID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SellerEventId(SellerEventIdtype):
    class Meta:
        name = "SellerEventID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SequenceId(SequenceIdtype):
    class Meta:
        name = "SequenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SequenceNumberId(SequenceNumberIdtype):
    class Meta:
        name = "SequenceNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SequenceNumeric(SequenceNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SerialId(SerialIdtype):
    class Meta:
        name = "SerialID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ServiceInformationPreferenceCode(ServiceInformationPreferenceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ServiceName(ServiceNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ServiceNumberCalled(ServiceNumberCalledType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ServiceType(ServiceTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ServiceTypeCode(ServiceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SettlementDiscountAmount(SettlementDiscountAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SettlementDiscountPercent(SettlementDiscountPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SharesNumberQuantity(SharesNumberQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ShippingMarks(ShippingMarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ShippingOrderId(ShippingOrderIdtype):
    class Meta:
        name = "ShippingOrderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ShippingPriorityLevelCode(ShippingPriorityLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ShipsRequirements(ShipsRequirementsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ShortQuantity(ShortQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ShortageActionCode(ShortageActionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SignatureId(SignatureIdtype):
    class Meta:
        name = "SignatureID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SignatureMethod(SignatureMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SizeTypeCode(SizeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SoleProprietorshipIndicator(SoleProprietorshipIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SourceCurrencyBaseRate(SourceCurrencyBaseRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SourceCurrencyCode(SourceCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SourceForecastIssueDate(SourceForecastIssueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SourceForecastIssueTime(SourceForecastIssueTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SourceValueMeasure(SourceValueMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SpecialInstructions(SpecialInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SpecialSecurityIndicator(SpecialSecurityIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SpecialServiceInstructions(SpecialServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SpecialTerms(SpecialTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SpecialTransportRequirements(SpecialTransportRequirementsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SpecificationId(SpecificationIdtype):
    class Meta:
        name = "SpecificationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SpecificationTypeCode(SpecificationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SplitConsignmentIndicator(SplitConsignmentIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class StartDate(StartDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class StartTime(StartTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class StatementTypeCode(StatementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class StatusAvailableIndicator(StatusAvailableIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class StatusCode(StatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class StatusReason(StatusReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class StatusReasonCode(StatusReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class StreetName(StreetNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SubcontractingConditionsCode(SubcontractingConditionsCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SubmissionDate(SubmissionDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SubmissionDueDate(SubmissionDueDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SubmissionMethodCode(SubmissionMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SubscriberId(SubscriberIdtype):
    class Meta:
        name = "SubscriberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SubscriberType(SubscriberTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SubscriberTypeCode(SubscriberTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SubstitutionStatusCode(SubstitutionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SuccessiveSequenceId(SuccessiveSequenceIdtype):
    class Meta:
        name = "SuccessiveSequenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SummaryDescription(SummaryDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SupplierAssignedAccountId(SupplierAssignedAccountIdtype):
    class Meta:
        name = "SupplierAssignedAccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class SupplyChainActivityTypeCode(SupplyChainActivityTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TareWeightMeasure(TareWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TargetCurrencyBaseRate(TargetCurrencyBaseRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TargetCurrencyCode(TargetCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TargetInventoryQuantity(TargetInventoryQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TargetServicePercent(TargetServicePercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TariffClassCode(TariffClassCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TariffCode(TariffCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TariffDescription(TariffDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxAmount(TaxAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxCurrencyCode(TaxCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxEnergyAmount(TaxEnergyAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxEnergyBalanceAmount(TaxEnergyBalanceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxEnergyOnAccountAmount(TaxEnergyOnAccountAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxEvidenceIndicator(TaxEvidenceIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxExclusiveAmount(TaxExclusiveAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxExemptionReason(TaxExemptionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxExemptionReasonCode(TaxExemptionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxIncludedIndicator(TaxIncludedIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxInclusiveAmount(TaxInclusiveAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxLevelCode(TaxLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxPointDate(TaxPointDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxTypeCode(TaxTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TaxableAmount(TaxableAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TechnicalCommitteeDescription(TechnicalCommitteeDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TechnicalName(TechnicalNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TelecommunicationsServiceCall(TelecommunicationsServiceCallType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TelecommunicationsServiceCallCode(TelecommunicationsServiceCallCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TelecommunicationsServiceCategory(TelecommunicationsServiceCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TelecommunicationsServiceCategoryCode(
    TelecommunicationsServiceCategoryCodeType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TelecommunicationsSupplyType(TelecommunicationsSupplyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TelecommunicationsSupplyTypeCode(TelecommunicationsSupplyTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Telefax(TelefaxType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Telephone(TelephoneType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TenderEnvelopeId(TenderEnvelopeIdtype):
    class Meta:
        name = "TenderEnvelopeID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TenderEnvelopeTypeCode(TenderEnvelopeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TenderResultCode(TenderResultCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TenderTypeCode(TenderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TendererRequirementTypeCode(TendererRequirementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TendererRoleCode(TendererRoleCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TestMethod(TestMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Text(TextType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ThirdPartyPayerIndicator(ThirdPartyPayerIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ThresholdAmount(ThresholdAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ThresholdQuantity(ThresholdQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ThresholdValueComparisonCode(ThresholdValueComparisonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TierRange(TierRangeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TierRatePercent(TierRatePercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TimeAmount(TimeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TimeDeltaDaysQuantity(TimeDeltaDaysQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TimeFrequencyCode(TimeFrequencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TimezoneOffset(TimezoneOffsetType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TimingComplaint(TimingComplaintType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TimingComplaintCode(TimingComplaintCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Title(TitleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ToOrderIndicator(ToOrderIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalAmount(TotalAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalBalanceAmount(TotalBalanceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalConsumedQuantity(TotalConsumedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalCreditAmount(TotalCreditAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalDebitAmount(TotalDebitAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalDeliveredQuantity(TotalDeliveredQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalGoodsItemQuantity(TotalGoodsItemQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalInvoiceAmount(TotalInvoiceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalMeteredQuantity(TotalMeteredQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalPackageQuantity(TotalPackageQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalPackagesQuantity(TotalPackagesQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalPaymentAmount(TotalPaymentAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalTaskAmount(TotalTaskAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalTaxAmount(TotalTaxAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TotalTransportHandlingUnitQuantity(
    TotalTransportHandlingUnitQuantityType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TraceId(TraceIdtype):
    class Meta:
        name = "TraceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TrackingDeviceCode(TrackingDeviceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TrackingId(TrackingIdtype):
    class Meta:
        name = "TrackingID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TradeItemPackingLabelingTypeCode(TradeItemPackingLabelingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TradeServiceCode(TradeServiceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TradingRestrictions(TradingRestrictionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TrainId(TrainIdtype):
    class Meta:
        name = "TrainID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransactionCurrencyTaxAmount(TransactionCurrencyTaxAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransitDirectionCode(TransitDirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportAuthorizationCode(TransportAuthorizationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportEmergencyCardCode(TransportEmergencyCardCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportEquipmentTypeCode(TransportEquipmentTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportEventTypeCode(TransportEventTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportExecutionPlanReferenceId(TransportExecutionPlanReferenceIdtype):
    class Meta:
        name = "TransportExecutionPlanReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportExecutionStatusCode(TransportExecutionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportHandlingUnitTypeCode(TransportHandlingUnitTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportMeansTypeCode(TransportMeansTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportModeCode(TransportModeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportServiceCode(TransportServiceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportServiceProviderRemarks(TransportServiceProviderRemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportServiceProviderSpecialTerms(
    TransportServiceProviderSpecialTermsType
):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportUserRemarks(TransportUserRemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportUserSpecialTerms(TransportUserSpecialTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportationServiceDescription(TransportationServiceDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportationServiceDetailsUri(TransportationServiceDetailsUritype):
    class Meta:
        name = "TransportationServiceDetailsURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TransportationStatusTypeCode(TransportationStatusTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class TypeCode(TypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class UblversionId(UblversionIdtype):
    class Meta:
        name = "UBLVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Undgcode(UndgcodeType):
    class Meta:
        name = "UNDGCode"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Uri(Uritype):
    class Meta:
        name = "URI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Uuid(Uuidtype):
    class Meta:
        name = "UUID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class UnknownPriceIndicator(UnknownPriceIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class UpperOrangeHazardPlacardId(UpperOrangeHazardPlacardIdtype):
    class Meta:
        name = "UpperOrangeHazardPlacardID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class UrgencyCode(UrgencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class UtilityStatementTypeCode(UtilityStatementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValidateProcess(ValidateProcessType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValidateTool(ValidateToolType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValidateToolVersion(ValidateToolVersionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValidationDate(ValidationDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValidationResultCode(ValidationResultCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValidationTime(ValidationTimeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValidatorId(ValidatorIdtype):
    class Meta:
        name = "ValidatorID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValidityStartDate(ValidityStartDateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Value(ValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValueAmount(ValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValueMeasure(ValueMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValueQualifier(ValueQualifierType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class ValueQuantity(ValueQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class VarianceQuantity(VarianceQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class VariantConstraintIndicator(VariantConstraintIndicatorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class VariantId(VariantIdtype):
    class Meta:
        name = "VariantID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class VersionId(VersionIdtype):
    class Meta:
        name = "VersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class VesselId(VesselIdtype):
    class Meta:
        name = "VesselID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class VesselName(VesselNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class WarrantyInformation(WarrantyInformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class WebsiteUri(WebsiteUritype):
    class Meta:
        name = "WebsiteURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class WeekDayCode(WeekDayCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Weight(WeightType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class WeightNumeric(WeightNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class WeightingAlgorithmCode(WeightingAlgorithmCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class WorkPhase(WorkPhaseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class WorkPhaseCode(WorkPhaseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass(frozen=True)
class Xpath(XpathType):
    class Meta:
        name = "XPath"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
