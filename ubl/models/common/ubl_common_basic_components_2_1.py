from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime
from ubl.models.common.ubl_unqualified_data_types_2_1 import (
    AmountType as UblUnqualifiedDataTypes21AmountType,
    BinaryObjectType,
    CodeType,
    IdentifierType,
    MeasureType as UblUnqualifiedDataTypes21MeasureType,
    NameType as UblUnqualifiedDataTypes21NameType,
    NumericType,
    PercentType as UblUnqualifiedDataTypes21PercentType,
    QuantityType as UblUnqualifiedDataTypes21QuantityType,
    RateType as UblUnqualifiedDataTypes21RateType,
    TextType as UblUnqualifiedDataTypes21TextType,
)

__NAMESPACE__ = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AcceptedIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ActualDeliveryDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ActualDeliveryTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ActualDespatchDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ActualDespatchTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ActualPickupDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ActualPickupTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AdValoremIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AnimalFoodApprovedIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AnimalFoodIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ApprovalDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AuctionConstraintIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AvailabilityDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AwardDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AwardTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class BackOrderAllowedIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class BalanceBroughtForwardIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class BasedOnConsensusIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class BestBeforeDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class BindingOnBuyerIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class BirthDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class BulkCargoIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CallDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CallTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CandidateReductionConstraintIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CatalogueIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ChargeIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ComparisonForecastIssueDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ComparisonForecastIssueTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CompletionIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ConsolidatableIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ContainerizedIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CopyIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class CustomsImportClassifiedIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class DangerousGoodsApprovedIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Date:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class DueDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EarliestPickupDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EarliestPickupTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EffectiveDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EffectiveTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EndDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EndTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EstimatedDeliveryDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EstimatedDeliveryTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EstimatedDespatchDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class EstimatedDespatchTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ExpiryDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ExpiryTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class FirstShipmentAvailibilityDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class FollowupContractIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class FreeOfChargeIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class FrozenDocumentIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class FullyPaidSharesIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class GeneralCargoIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class GovernmentAgreementConstraintIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class GuaranteedDespatchDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class GuaranteedDespatchTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class HazardousRiskIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class HumanFoodApprovedIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class HumanFoodIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class IndicationIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class InstallmentDueDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class IssueDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class IssueTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ItemUpdateRequestIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LastRevisionDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LastRevisionTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LatestDeliveryDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LatestDeliveryTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LatestMeterReadingDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LatestPickupDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LatestPickupTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LatestProposalAcceptanceDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LatestSecurityClearanceDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LegalStatusIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class LivestockIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ManufactureDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ManufactureTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class MarkAttentionIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class MarkCareIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class NominationDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class NominationTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OccurrenceDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OccurrenceTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OnCarriageIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OptionalLineItemIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OrderableIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class OtherConditionsIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PaidDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PaidTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PartialDeliveryIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PaymentDueDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PlannedDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PowerIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PreCarriageIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PrepaidIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PreviousMeterReadingDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PricingUpdateRequestIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PrizeIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class PublishAwardIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ReceivedDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ReferenceDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ReferenceTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RefrigeratedIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RefrigerationOnIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RegisteredDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RegisteredTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RegistrationDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RegistrationExpirationDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RequestedDeliveryDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RequestedDespatchDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RequestedDespatchTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RequestedPublicationDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RequiredCurriculaIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RequiredDeliveryDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RequiredDeliveryTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ResolutionDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ResolutionTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ResponseDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ResponseTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ReturnabilityIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ReturnableMaterialIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RevisionDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RevisionTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SoleProprietorshipIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SourceForecastIssueDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SourceForecastIssueTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SpecialSecurityIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SplitConsignmentIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class StartDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class StartTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class StatusAvailableIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SubmissionDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class SubmissionDueDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class TaxEvidenceIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class TaxIncludedIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class TaxPointDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ThirdPartyPayerIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ToOrderIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class UnknownPriceIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ValidationDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ValidationTime:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlTime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ValidityStartDate:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class VariantConstraintIndicator:
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class AcceptedVariantsDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class AccountFormatCodeType(CodeType):
    pass


@dataclass
class AccountIdtype(IdentifierType):
    class Meta:
        name = "AccountIDType"


@dataclass
class AccountTypeCodeType(CodeType):
    pass


@dataclass
class AccountingCostCodeType(CodeType):
    pass


@dataclass
class AccountingCostType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ActionCodeType(CodeType):
    pass


@dataclass
class ActivityTypeCodeType(CodeType):
    pass


@dataclass
class ActivityTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ActualTemperatureReductionQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class AdditionalAccountIdtype(IdentifierType):
    class Meta:
        name = "AdditionalAccountIDType"


@dataclass
class AdditionalConditionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class AdditionalInformationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class AdditionalStreetNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class AddressFormatCodeType(CodeType):
    pass


@dataclass
class AddressTypeCodeType(CodeType):
    pass


@dataclass
class AdjustmentReasonCodeType(CodeType):
    pass


@dataclass
class AdmissionCodeType(CodeType):
    pass


@dataclass
class AdvertisementAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class AgencyIdtype(IdentifierType):
    class Meta:
        name = "AgencyIDType"


@dataclass
class AgencyNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class AirFlowPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class AircraftIdtype(IdentifierType):
    class Meta:
        name = "AircraftIDType"


@dataclass
class AliasNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class AllowanceChargeReasonCodeType(CodeType):
    pass


@dataclass
class AllowanceChargeReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class AllowanceTotalAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class AltitudeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class AmountRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass
class AmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class AnnualAverageAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class ApplicationStatusCodeType(CodeType):
    pass


@dataclass
class ApprovalStatusType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class AttributeIdtype(IdentifierType):
    class Meta:
        name = "AttributeIDType"


@dataclass
class AuctionUritype(IdentifierType):
    class Meta:
        name = "AuctionURIType"


@dataclass
class AvailabilityStatusCodeType(CodeType):
    pass


@dataclass
class AverageAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class AverageSubsequentContractAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class AwardingCriterionDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class AwardingCriterionIdtype(IdentifierType):
    class Meta:
        name = "AwardingCriterionIDType"


@dataclass
class AwardingCriterionTypeCodeType(CodeType):
    pass


@dataclass
class AwardingMethodTypeCodeType(CodeType):
    pass


@dataclass
class BackorderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class BackorderReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class BalanceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class BarcodeSymbologyIdtype(IdentifierType):
    class Meta:
        name = "BarcodeSymbologyIDType"


@dataclass
class BaseAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class BaseQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class BaseUnitMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class BasicConsumedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class BatchQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class BirthplaceNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class BlockNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class BrandNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class BrokerAssignedIdtype(IdentifierType):
    class Meta:
        name = "BrokerAssignedIDType"


@dataclass
class BudgetYearNumericType(NumericType):
    pass


@dataclass
class BuildingNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class BuildingNumberType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class BusinessClassificationEvidenceIdtype(IdentifierType):
    class Meta:
        name = "BusinessClassificationEvidenceIDType"


@dataclass
class BusinessIdentityEvidenceIdtype(IdentifierType):
    class Meta:
        name = "BusinessIdentityEvidenceIDType"


@dataclass
class BuyerEventIdtype(IdentifierType):
    class Meta:
        name = "BuyerEventIDType"


@dataclass
class BuyerProfileUritype(IdentifierType):
    class Meta:
        name = "BuyerProfileURIType"


@dataclass
class BuyerReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class Cv2Idtype(IdentifierType):
    class Meta:
        name = "CV2IDType"


@dataclass
class CalculationExpressionCodeType(CodeType):
    pass


@dataclass
class CalculationExpressionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CalculationMethodCodeType(CodeType):
    pass


@dataclass
class CalculationRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass
class CalculationSequenceNumericType(NumericType):
    pass


@dataclass
class CallBaseAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class CallExtensionAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class CancellationNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CandidateStatementType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CanonicalizationMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CapabilityTypeCodeType(CodeType):
    pass


@dataclass
class CardChipCodeType(CodeType):
    pass


@dataclass
class CardTypeCodeType(CodeType):
    pass


@dataclass
class CargoTypeCodeType(CodeType):
    pass


@dataclass
class CarrierAssignedIdtype(IdentifierType):
    class Meta:
        name = "CarrierAssignedIDType"


@dataclass
class CarrierServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CategoryNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class CertificateTypeCodeType(CodeType):
    pass


@dataclass
class CertificateTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ChangeConditionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ChannelCodeType(CodeType):
    pass


@dataclass
class ChannelType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CharacterSetCodeType(CodeType):
    pass


@dataclass
class CharacteristicsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ChargeTotalAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class ChargeableQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ChargeableWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class ChildConsignmentQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ChipApplicationIdtype(IdentifierType):
    class Meta:
        name = "ChipApplicationIDType"


@dataclass
class CityNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class CitySubdivisionNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class CodeValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CollaborationPriorityCodeType(CodeType):
    pass


@dataclass
class CommentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CommodityCodeType(CodeType):
    pass


@dataclass
class CompanyIdtype(IdentifierType):
    class Meta:
        name = "CompanyIDType"


@dataclass
class CompanyLegalFormCodeType(CodeType):
    pass


@dataclass
class CompanyLegalFormType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CompanyLiquidationStatusCodeType(CodeType):
    pass


@dataclass
class ComparedValueMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class ComparisonDataCodeType(CodeType):
    pass


@dataclass
class ComparisonDataSourceCodeType(CodeType):
    pass


@dataclass
class ConditionCodeType(CodeType):
    pass


@dataclass
class ConditionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ConditionsDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ConditionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ConsigneeAssignedIdtype(IdentifierType):
    class Meta:
        name = "ConsigneeAssignedIDType"


@dataclass
class ConsignmentQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ConsignorAssignedIdtype(IdentifierType):
    class Meta:
        name = "ConsignorAssignedIDType"


@dataclass
class ConstitutionCodeType(CodeType):
    pass


@dataclass
class ConsumerIncentiveTacticTypeCodeType(CodeType):
    pass


@dataclass
class ConsumerUnitQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ConsumersEnergyLevelCodeType(CodeType):
    pass


@dataclass
class ConsumersEnergyLevelType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ConsumptionEnergyQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ConsumptionIdtype(IdentifierType):
    class Meta:
        name = "ConsumptionIDType"


@dataclass
class ConsumptionLevelCodeType(CodeType):
    pass


@dataclass
class ConsumptionLevelType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ConsumptionReportIdtype(IdentifierType):
    class Meta:
        name = "ConsumptionReportIDType"


@dataclass
class ConsumptionTypeCodeType(CodeType):
    pass


@dataclass
class ConsumptionTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ConsumptionWaterQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ContentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ContentUnitQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ContractFolderIdtype(IdentifierType):
    class Meta:
        name = "ContractFolderIDType"


@dataclass
class ContractNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ContractSubdivisionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ContractTypeCodeType(CodeType):
    pass


@dataclass
class ContractTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ContractedCarrierAssignedIdtype(IdentifierType):
    class Meta:
        name = "ContractedCarrierAssignedIDType"


@dataclass
class ContractingSystemCodeType(CodeType):
    pass


@dataclass
class CoordinateSystemCodeType(CodeType):
    pass


@dataclass
class CorporateRegistrationTypeCodeType(CodeType):
    pass


@dataclass
class CorporateStockAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class CorrectionAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class CorrectionTypeCodeType(CodeType):
    pass


@dataclass
class CorrectionTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CorrectionUnitAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class CountrySubentityCodeType(CodeType):
    pass


@dataclass
class CountrySubentityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CreditLineAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class CreditNoteTypeCodeType(CodeType):
    pass


@dataclass
class CreditedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class CrewQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class CurrencyCodeType(CodeType):
    pass


@dataclass
class CurrentChargeTypeCodeType(CodeType):
    pass


@dataclass
class CurrentChargeTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CustomerAssignedAccountIdtype(IdentifierType):
    class Meta:
        name = "CustomerAssignedAccountIDType"


@dataclass
class CustomerReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CustomizationIdtype(IdentifierType):
    class Meta:
        name = "CustomizationIDType"


@dataclass
class CustomsClearanceServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class CustomsStatusCodeType(CodeType):
    pass


@dataclass
class CustomsTariffQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class DamageRemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DataSendingCapabilityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DataSourceCodeType(CodeType):
    pass


@dataclass
class DebitLineAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class DebitedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class DeclarationTypeCodeType(CodeType):
    pass


@dataclass
class DeclaredCarriageValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class DeclaredCustomsValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class DeclaredForCarriageValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class DeclaredStatisticsValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class DeliveredQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class DeliveryInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DemurrageInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DepartmentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DescriptionCodeType(CodeType):
    pass


@dataclass
class DescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DespatchAdviceTypeCodeType(CodeType):
    pass


@dataclass
class DifferenceTemperatureReductionQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class DirectionCodeType(CodeType):
    pass


@dataclass
class DisplayTacticTypeCodeType(CodeType):
    pass


@dataclass
class DispositionCodeType(CodeType):
    pass


@dataclass
class DistrictType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DocumentCurrencyCodeType(CodeType):
    pass


@dataclass
class DocumentDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DocumentHashType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DocumentIdtype(IdentifierType):
    class Meta:
        name = "DocumentIDType"


@dataclass
class DocumentStatusCodeType(CodeType):
    pass


@dataclass
class DocumentStatusReasonCodeType(CodeType):
    pass


@dataclass
class DocumentStatusReasonDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DocumentTypeCodeType(CodeType):
    pass


@dataclass
class DocumentTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class DocumentationFeeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class DurationMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class DutyCodeType(CodeType):
    pass


@dataclass
class DutyType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class EconomicOperatorRegistryUritype(IdentifierType):
    class Meta:
        name = "EconomicOperatorRegistryURIType"


@dataclass
class ElectronicDeviceDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ElectronicMailType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class EmbeddedDocumentBinaryObjectType(BinaryObjectType):
    pass


@dataclass
class EmergencyProceduresCodeType(CodeType):
    pass


@dataclass
class EmployeeQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class EncodingCodeType(CodeType):
    pass


@dataclass
class EndpointIdtype(IdentifierType):
    class Meta:
        name = "EndpointIDType"


@dataclass
class EnvironmentalEmissionTypeCodeType(CodeType):
    pass


@dataclass
class EstimatedAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class EstimatedConsumedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class EstimatedOverallContractAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class EstimatedOverallContractQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class EvaluationCriterionTypeCodeType(CodeType):
    pass


@dataclass
class EvidenceTypeCodeType(CodeType):
    pass


@dataclass
class ExceptionResolutionCodeType(CodeType):
    pass


@dataclass
class ExceptionStatusCodeType(CodeType):
    pass


@dataclass
class ExchangeMarketIdtype(IdentifierType):
    class Meta:
        name = "ExchangeMarketIDType"


@dataclass
class ExclusionReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ExecutionRequirementCodeType(CodeType):
    pass


@dataclass
class ExemptionReasonCodeType(CodeType):
    pass


@dataclass
class ExemptionReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ExpectedOperatorQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ExpectedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ExpenseCodeType(CodeType):
    pass


@dataclass
class ExpressionCodeType(CodeType):
    pass


@dataclass
class ExpressionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ExtendedIdtype(IdentifierType):
    class Meta:
        name = "ExtendedIDType"


@dataclass
class ExtensionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class FaceValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class FamilyNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class FeatureTacticTypeCodeType(CodeType):
    pass


@dataclass
class FeeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class FeeDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class FileNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class FinancingInstrumentCodeType(CodeType):
    pass


@dataclass
class FirstNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class FloorType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ForecastPurposeCodeType(CodeType):
    pass


@dataclass
class ForecastTypeCodeType(CodeType):
    pass


@dataclass
class FormatCodeType(CodeType):
    pass


@dataclass
class ForwarderServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class FreeOnBoardValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class FreightForwarderAssignedIdtype(IdentifierType):
    class Meta:
        name = "FreightForwarderAssignedIDType"


@dataclass
class FreightRateClassCodeType(CodeType):
    pass


@dataclass
class FrequencyType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class FrozenPeriodDaysNumericType(NumericType):
    pass


@dataclass
class FullnessIndicationCodeType(CodeType):
    pass


@dataclass
class FundingProgramCodeType(CodeType):
    pass


@dataclass
class FundingProgramType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class GasPressureQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class GenderCodeType(CodeType):
    pass


@dataclass
class GrossTonnageMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class GrossVolumeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class GrossWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class GuaranteeTypeCodeType(CodeType):
    pass


@dataclass
class HandlingCodeType(CodeType):
    pass


@dataclass
class HandlingInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class HashAlgorithmMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class HaulageInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class HazardClassIdtype(IdentifierType):
    class Meta:
        name = "HazardClassIDType"


@dataclass
class HazardousCategoryCodeType(CodeType):
    pass


@dataclass
class HazardousRegulationCodeType(CodeType):
    pass


@dataclass
class HeatingTypeCodeType(CodeType):
    pass


@dataclass
class HeatingTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class HigherTenderAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class HolderNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class HumidityPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class Idtype(IdentifierType):
    class Meta:
        name = "IDType"


@dataclass
class IdentificationCodeType(CodeType):
    pass


@dataclass
class IdentificationIdtype(IdentifierType):
    class Meta:
        name = "IdentificationIDType"


@dataclass
class ImmobilizationCertificateIdtype(IdentifierType):
    class Meta:
        name = "ImmobilizationCertificateIDType"


@dataclass
class ImportanceCodeType(CodeType):
    pass


@dataclass
class IndustryClassificationCodeType(CodeType):
    pass


@dataclass
class InformationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class InformationUritype(IdentifierType):
    class Meta:
        name = "InformationURIType"


@dataclass
class InhalationToxicityZoneCodeType(CodeType):
    pass


@dataclass
class InhouseMailType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class InspectionMethodCodeType(CodeType):
    pass


@dataclass
class InstructionIdtype(IdentifierType):
    class Meta:
        name = "InstructionIDType"


@dataclass
class InstructionNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class InstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class InsurancePremiumAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class InsuranceValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class InventoryValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class InvoiceTypeCodeType(CodeType):
    pass


@dataclass
class InvoicedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class InvoicingPartyReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class IssueNumberIdtype(IdentifierType):
    class Meta:
        name = "IssueNumberIDType"


@dataclass
class IssuerIdtype(IdentifierType):
    class Meta:
        name = "IssuerIDType"


@dataclass
class ItemClassificationCodeType(CodeType):
    pass


@dataclass
class JobTitleType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class JourneyIdtype(IdentifierType):
    class Meta:
        name = "JourneyIDType"


@dataclass
class JustificationDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class JustificationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class KeywordType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class LanguageIdtype(IdentifierType):
    class Meta:
        name = "LanguageIDType"


@dataclass
class LatestMeterQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class LatestMeterReadingMethodCodeType(CodeType):
    pass


@dataclass
class LatestMeterReadingMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class LatitudeDegreesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class LatitudeDirectionCodeType(CodeType):
    pass


@dataclass
class LatitudeMinutesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class LeadTimeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class LegalReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class LiabilityAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class LicensePlateIdtype(IdentifierType):
    class Meta:
        name = "LicensePlateIDType"


@dataclass
class LifeCycleStatusCodeType(CodeType):
    pass


@dataclass
class LimitationDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class LineCountNumericType(NumericType):
    pass


@dataclass
class LineExtensionAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class LineIdtype(IdentifierType):
    class Meta:
        name = "LineIDType"


@dataclass
class LineNumberNumericType(NumericType):
    pass


@dataclass
class LineStatusCodeType(CodeType):
    pass


@dataclass
class LineType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ListValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class LoadingLengthMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class LoadingSequenceIdtype(IdentifierType):
    class Meta:
        name = "LoadingSequenceIDType"


@dataclass
class LocaleCodeType(CodeType):
    pass


@dataclass
class LocationIdtype(IdentifierType):
    class Meta:
        name = "LocationIDType"


@dataclass
class LocationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class LocationTypeCodeType(CodeType):
    pass


@dataclass
class LoginType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class LogoReferenceIdtype(IdentifierType):
    class Meta:
        name = "LogoReferenceIDType"


@dataclass
class LongitudeDegreesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class LongitudeDirectionCodeType(CodeType):
    pass


@dataclass
class LongitudeMinutesMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class LossRiskResponsibilityCodeType(CodeType):
    pass


@dataclass
class LossRiskType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class LotNumberIdtype(IdentifierType):
    class Meta:
        name = "LotNumberIDType"


@dataclass
class LowTendersDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class LowerOrangeHazardPlacardIdtype(IdentifierType):
    class Meta:
        name = "LowerOrangeHazardPlacardIDType"


@dataclass
class LowerTenderAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class MandateTypeCodeType(CodeType):
    pass


@dataclass
class MarkAttentionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MarkCareType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MarketValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class MarkingIdtype(IdentifierType):
    class Meta:
        name = "MarkingIDType"


@dataclass
class MathematicOperatorCodeType(CodeType):
    pass


@dataclass
class MaximumAdvertisementAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class MaximumAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class MaximumBackorderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MaximumCopiesNumericType(NumericType):
    pass


@dataclass
class MaximumMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class MaximumNumberNumericType(NumericType):
    pass


@dataclass
class MaximumOperatorQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MaximumOrderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MaximumPaidAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class MaximumPaymentInstructionsNumericType(NumericType):
    pass


@dataclass
class MaximumPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class MaximumQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MaximumValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MaximumVariantQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class MedicalFirstAidGuideCodeType(CodeType):
    pass


@dataclass
class MeterConstantCodeType(CodeType):
    pass


@dataclass
class MeterConstantType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MeterNameType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MeterNumberType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MeterReadingCommentsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MeterReadingTypeCodeType(CodeType):
    pass


@dataclass
class MeterReadingTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MiddleNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class MimeCodeType(CodeType):
    pass


@dataclass
class MinimumAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class MinimumBackorderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MinimumImprovementBidType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MinimumInventoryQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MinimumMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class MinimumNumberNumericType(NumericType):
    pass


@dataclass
class MinimumOrderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MinimumPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class MinimumQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MinimumValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MiscellaneousEventTypeCodeType(CodeType):
    pass


@dataclass
class ModelNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class MonetaryScopeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MovieTitleType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class MultipleOrderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class MultiplierFactorNumericType(NumericType):
    pass


@dataclass
class NameCodeType(CodeType):
    pass


@dataclass
class NameSuffixType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class NameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class NationalityIdtype(IdentifierType):
    class Meta:
        name = "NationalityIDType"


@dataclass
class NatureCodeType(CodeType):
    pass


@dataclass
class NegotiationDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class NetNetWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class NetTonnageMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class NetVolumeMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class NetWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class NetworkIdtype(IdentifierType):
    class Meta:
        name = "NetworkIDType"


@dataclass
class NormalTemperatureReductionQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class NoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class NotificationTypeCodeType(CodeType):
    pass


@dataclass
class OneTimeChargeTypeCodeType(CodeType):
    pass


@dataclass
class OneTimeChargeTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class OntologyUritype(IdentifierType):
    class Meta:
        name = "OntologyURIType"


@dataclass
class OpenTenderIdtype(IdentifierType):
    class Meta:
        name = "OpenTenderIDType"


@dataclass
class OperatingYearsQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class OptionsDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class OrderIntervalDaysNumericType(NumericType):
    pass


@dataclass
class OrderQuantityIncrementNumericType(NumericType):
    pass


@dataclass
class OrderResponseCodeType(CodeType):
    pass


@dataclass
class OrderTypeCodeType(CodeType):
    pass


@dataclass
class OrderableUnitFactorRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass
class OrderableUnitType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class OrganizationDepartmentType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class OriginalContractingSystemIdtype(IdentifierType):
    class Meta:
        name = "OriginalContractingSystemIDType"


@dataclass
class OriginalJobIdtype(IdentifierType):
    class Meta:
        name = "OriginalJobIDType"


@dataclass
class OtherInstructionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class OtherNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class OutstandingQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class OutstandingReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class OversupplyQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class OwnerTypeCodeType(CodeType):
    pass


@dataclass
class PackLevelCodeType(CodeType):
    pass


@dataclass
class PackQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class PackSizeNumericType(NumericType):
    pass


@dataclass
class PackageLevelCodeType(CodeType):
    pass


@dataclass
class PackagingTypeCodeType(CodeType):
    pass


@dataclass
class PackingCriteriaCodeType(CodeType):
    pass


@dataclass
class PackingMaterialType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PaidAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class ParentDocumentIdtype(IdentifierType):
    class Meta:
        name = "ParentDocumentIDType"


@dataclass
class ParentDocumentLineReferenceIdtype(IdentifierType):
    class Meta:
        name = "ParentDocumentLineReferenceIDType"


@dataclass
class ParentDocumentTypeCodeType(CodeType):
    pass


@dataclass
class ParentDocumentVersionIdtype(IdentifierType):
    class Meta:
        name = "ParentDocumentVersionIDType"


@dataclass
class PartPresentationCodeType(CodeType):
    pass


@dataclass
class PartecipationPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class ParticipationPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class PartyCapacityAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class PartyTypeCodeType(CodeType):
    pass


@dataclass
class PartyTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PassengerQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class PasswordType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PayPerViewType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PayableAlternativeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class PayableAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class PayableRoundingAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class PayerReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PaymentAlternativeCurrencyCodeType(CodeType):
    pass


@dataclass
class PaymentChannelCodeType(CodeType):
    pass


@dataclass
class PaymentCurrencyCodeType(CodeType):
    pass


@dataclass
class PaymentDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PaymentFrequencyCodeType(CodeType):
    pass


@dataclass
class PaymentIdtype(IdentifierType):
    class Meta:
        name = "PaymentIDType"


@dataclass
class PaymentMeansCodeType(CodeType):
    pass


@dataclass
class PaymentMeansIdtype(IdentifierType):
    class Meta:
        name = "PaymentMeansIDType"


@dataclass
class PaymentNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PaymentOrderReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PaymentPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class PaymentPurposeCodeType(CodeType):
    pass


@dataclass
class PaymentTermsDetailsUritype(IdentifierType):
    class Meta:
        name = "PaymentTermsDetailsURIType"


@dataclass
class PenaltyAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class PenaltySurchargePercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class PerUnitAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class PercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class PerformanceMetricTypeCodeType(CodeType):
    pass


@dataclass
class PerformanceValueQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class PerformingCarrierAssignedIdtype(IdentifierType):
    class Meta:
        name = "PerformingCarrierAssignedIDType"


@dataclass
class PersonalSituationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PhoneNumberType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PlacardEndorsementType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PlacardNotationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PlotIdentificationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PositionCodeType(CodeType):
    pass


@dataclass
class PostEventNotificationDurationMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class PostalZoneType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PostboxType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PreEventNotificationDurationMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class PreferenceCriterionCodeType(CodeType):
    pass


@dataclass
class PrepaidAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class PrepaidPaymentReferenceIdtype(IdentifierType):
    class Meta:
        name = "PrepaidPaymentReferenceIDType"


@dataclass
class PreviousCancellationReasonCodeType(CodeType):
    pass


@dataclass
class PreviousJobIdtype(IdentifierType):
    class Meta:
        name = "PreviousJobIDType"


@dataclass
class PreviousMeterQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class PreviousMeterReadingMethodCodeType(CodeType):
    pass


@dataclass
class PreviousMeterReadingMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PreviousVersionIdtype(IdentifierType):
    class Meta:
        name = "PreviousVersionIDType"


@dataclass
class PriceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class PriceChangeReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PriceEvaluationCodeType(CodeType):
    pass


@dataclass
class PriceRevisionFormulaDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PriceTypeCodeType(CodeType):
    pass


@dataclass
class PriceTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PricingCurrencyCodeType(CodeType):
    pass


@dataclass
class PrimaryAccountNumberIdtype(IdentifierType):
    class Meta:
        name = "PrimaryAccountNumberIDType"


@dataclass
class PrintQualifierType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PriorityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class PrivacyCodeType(CodeType):
    pass


@dataclass
class PrizeDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ProcedureCodeType(CodeType):
    pass


@dataclass
class ProcessDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ProcessReasonCodeType(CodeType):
    pass


@dataclass
class ProcessReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ProcurementSubTypeCodeType(CodeType):
    pass


@dataclass
class ProcurementTypeCodeType(CodeType):
    pass


@dataclass
class ProductTraceIdtype(IdentifierType):
    class Meta:
        name = "ProductTraceIDType"


@dataclass
class ProfileExecutionIdtype(IdentifierType):
    class Meta:
        name = "ProfileExecutionIDType"


@dataclass
class ProfileIdtype(IdentifierType):
    class Meta:
        name = "ProfileIDType"


@dataclass
class ProfileStatusCodeType(CodeType):
    pass


@dataclass
class ProgressPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class PromotionalEventTypeCodeType(CodeType):
    pass


@dataclass
class ProviderTypeCodeType(CodeType):
    pass


@dataclass
class PurposeCodeType(CodeType):
    pass


@dataclass
class PurposeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class QualityControlCodeType(CodeType):
    pass


@dataclass
class QuantityDiscrepancyCodeType(CodeType):
    pass


@dataclass
class QuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class RadioCallSignIdtype(IdentifierType):
    class Meta:
        name = "RadioCallSignIDType"


@dataclass
class RailCarIdtype(IdentifierType):
    class Meta:
        name = "RailCarIDType"


@dataclass
class RankType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class RateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass
class ReceiptAdviceTypeCodeType(CodeType):
    pass


@dataclass
class ReceivedElectronicTenderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ReceivedForeignTenderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ReceivedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ReceivedTenderQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ReferenceEventCodeType(CodeType):
    pass


@dataclass
class ReferenceIdtype(IdentifierType):
    class Meta:
        name = "ReferenceIDType"


@dataclass
class ReferenceType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ReferencedConsignmentIdtype(IdentifierType):
    class Meta:
        name = "ReferencedConsignmentIDType"


@dataclass
class RegionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class RegistrationIdtype(IdentifierType):
    class Meta:
        name = "RegistrationIDType"


@dataclass
class RegistrationNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class RegistrationNationalityIdtype(IdentifierType):
    class Meta:
        name = "RegistrationNationalityIDType"


@dataclass
class RegistrationNationalityType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class RegulatoryDomainType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class RejectActionCodeType(CodeType):
    pass


@dataclass
class RejectReasonCodeType(CodeType):
    pass


@dataclass
class RejectReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class RejectedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class RejectionNoteType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ReleaseIdtype(IdentifierType):
    class Meta:
        name = "ReleaseIDType"


@dataclass
class ReliabilityPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class RemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ReminderSequenceNumericType(NumericType):
    pass


@dataclass
class ReminderTypeCodeType(CodeType):
    pass


@dataclass
class ReplenishmentOwnerDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class RequestForQuotationLineIdtype(IdentifierType):
    class Meta:
        name = "RequestForQuotationLineIDType"


@dataclass
class RequestedInvoiceCurrencyCodeType(CodeType):
    pass


@dataclass
class RequiredCustomsIdtype(IdentifierType):
    class Meta:
        name = "RequiredCustomsIDType"


@dataclass
class RequiredFeeAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class ResidenceTypeCodeType(CodeType):
    pass


@dataclass
class ResidenceTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ResidentOccupantsNumericType(NumericType):
    pass


@dataclass
class ResolutionCodeType(CodeType):
    pass


@dataclass
class ResolutionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ResponseCodeType(CodeType):
    pass


@dataclass
class RetailEventNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class RetailEventStatusCodeType(CodeType):
    pass


@dataclass
class ReturnableQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class RevisedForecastLineIdtype(IdentifierType):
    class Meta:
        name = "RevisedForecastLineIDType"


@dataclass
class RevisionStatusCodeType(CodeType):
    pass


@dataclass
class RoamingPartnerNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class RoleCodeType(CodeType):
    pass


@dataclass
class RoleDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class RoomType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class RoundingAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class SalesOrderIdtype(IdentifierType):
    class Meta:
        name = "SalesOrderIDType"


@dataclass
class SalesOrderLineIdtype(IdentifierType):
    class Meta:
        name = "SalesOrderLineIDType"


@dataclass
class SchemeUritype(IdentifierType):
    class Meta:
        name = "SchemeURIType"


@dataclass
class SealIssuerTypeCodeType(CodeType):
    pass


@dataclass
class SealStatusCodeType(CodeType):
    pass


@dataclass
class SealingPartyTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class SecurityClassificationCodeType(CodeType):
    pass


@dataclass
class SecurityIdtype(IdentifierType):
    class Meta:
        name = "SecurityIDType"


@dataclass
class SellerEventIdtype(IdentifierType):
    class Meta:
        name = "SellerEventIDType"


@dataclass
class SequenceIdtype(IdentifierType):
    class Meta:
        name = "SequenceIDType"


@dataclass
class SequenceNumberIdtype(IdentifierType):
    class Meta:
        name = "SequenceNumberIDType"


@dataclass
class SequenceNumericType(NumericType):
    pass


@dataclass
class SerialIdtype(IdentifierType):
    class Meta:
        name = "SerialIDType"


@dataclass
class ServiceInformationPreferenceCodeType(CodeType):
    pass


@dataclass
class ServiceNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class ServiceNumberCalledType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ServiceTypeCodeType(CodeType):
    pass


@dataclass
class ServiceTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class SettlementDiscountAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class SettlementDiscountPercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class SharesNumberQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ShippingMarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ShippingOrderIdtype(IdentifierType):
    class Meta:
        name = "ShippingOrderIDType"


@dataclass
class ShippingPriorityLevelCodeType(CodeType):
    pass


@dataclass
class ShipsRequirementsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ShortQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ShortageActionCodeType(CodeType):
    pass


@dataclass
class SignatureIdtype(IdentifierType):
    class Meta:
        name = "SignatureIDType"


@dataclass
class SignatureMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class SizeTypeCodeType(CodeType):
    pass


@dataclass
class SourceCurrencyBaseRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass
class SourceCurrencyCodeType(CodeType):
    pass


@dataclass
class SourceValueMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class SpecialInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class SpecialServiceInstructionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class SpecialTermsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class SpecialTransportRequirementsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class SpecificationIdtype(IdentifierType):
    class Meta:
        name = "SpecificationIDType"


@dataclass
class SpecificationTypeCodeType(CodeType):
    pass


@dataclass
class StatementTypeCodeType(CodeType):
    pass


@dataclass
class StatusCodeType(CodeType):
    pass


@dataclass
class StatusReasonCodeType(CodeType):
    pass


@dataclass
class StatusReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class StreetNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class SubcontractingConditionsCodeType(CodeType):
    pass


@dataclass
class SubmissionMethodCodeType(CodeType):
    pass


@dataclass
class SubscriberIdtype(IdentifierType):
    class Meta:
        name = "SubscriberIDType"


@dataclass
class SubscriberTypeCodeType(CodeType):
    pass


@dataclass
class SubscriberTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class SubstitutionStatusCodeType(CodeType):
    pass


@dataclass
class SuccessiveSequenceIdtype(IdentifierType):
    class Meta:
        name = "SuccessiveSequenceIDType"


@dataclass
class SummaryDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class SupplierAssignedAccountIdtype(IdentifierType):
    class Meta:
        name = "SupplierAssignedAccountIDType"


@dataclass
class SupplyChainActivityTypeCodeType(CodeType):
    pass


@dataclass
class TareWeightMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class TargetCurrencyBaseRateType(UblUnqualifiedDataTypes21RateType):
    pass


@dataclass
class TargetCurrencyCodeType(CodeType):
    pass


@dataclass
class TargetInventoryQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class TargetServicePercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class TariffClassCodeType(CodeType):
    pass


@dataclass
class TariffCodeType(CodeType):
    pass


@dataclass
class TariffDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TaxAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TaxCurrencyCodeType(CodeType):
    pass


@dataclass
class TaxEnergyAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TaxEnergyBalanceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TaxEnergyOnAccountAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TaxExclusiveAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TaxExemptionReasonCodeType(CodeType):
    pass


@dataclass
class TaxExemptionReasonType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TaxInclusiveAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TaxLevelCodeType(CodeType):
    pass


@dataclass
class TaxTypeCodeType(CodeType):
    pass


@dataclass
class TaxableAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TechnicalCommitteeDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TechnicalNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class TelecommunicationsServiceCallCodeType(CodeType):
    pass


@dataclass
class TelecommunicationsServiceCallType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TelecommunicationsServiceCategoryCodeType(CodeType):
    pass


@dataclass
class TelecommunicationsServiceCategoryType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TelecommunicationsSupplyTypeCodeType(CodeType):
    pass


@dataclass
class TelecommunicationsSupplyTypeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TelefaxType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TelephoneType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TenderEnvelopeIdtype(IdentifierType):
    class Meta:
        name = "TenderEnvelopeIDType"


@dataclass
class TenderEnvelopeTypeCodeType(CodeType):
    pass


@dataclass
class TenderResultCodeType(CodeType):
    pass


@dataclass
class TenderTypeCodeType(CodeType):
    pass


@dataclass
class TendererRequirementTypeCodeType(CodeType):
    pass


@dataclass
class TendererRoleCodeType(CodeType):
    pass


@dataclass
class TestMethodType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TextType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ThresholdAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class ThresholdQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ThresholdValueComparisonCodeType(CodeType):
    pass


@dataclass
class TierRangeType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TierRatePercentType(UblUnqualifiedDataTypes21PercentType):
    pass


@dataclass
class TimeAmountType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TimeDeltaDaysQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class TimeFrequencyCodeType(CodeType):
    pass


@dataclass
class TimezoneOffsetType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TimingComplaintCodeType(CodeType):
    pass


@dataclass
class TimingComplaintType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TitleType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TotalAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TotalBalanceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TotalConsumedQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class TotalCreditAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TotalDebitAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TotalDeliveredQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class TotalGoodsItemQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class TotalInvoiceAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TotalMeteredQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class TotalPackageQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class TotalPackagesQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class TotalPaymentAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TotalTaskAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TotalTaxAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TotalTransportHandlingUnitQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class TraceIdtype(IdentifierType):
    class Meta:
        name = "TraceIDType"


@dataclass
class TrackingDeviceCodeType(CodeType):
    pass


@dataclass
class TrackingIdtype(IdentifierType):
    class Meta:
        name = "TrackingIDType"


@dataclass
class TradeItemPackingLabelingTypeCodeType(CodeType):
    pass


@dataclass
class TradeServiceCodeType(CodeType):
    pass


@dataclass
class TradingRestrictionsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TrainIdtype(IdentifierType):
    class Meta:
        name = "TrainIDType"


@dataclass
class TransactionCurrencyTaxAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class TransitDirectionCodeType(CodeType):
    pass


@dataclass
class TransportAuthorizationCodeType(CodeType):
    pass


@dataclass
class TransportEmergencyCardCodeType(CodeType):
    pass


@dataclass
class TransportEquipmentTypeCodeType(CodeType):
    pass


@dataclass
class TransportEventTypeCodeType(CodeType):
    pass


@dataclass
class TransportExecutionPlanReferenceIdtype(IdentifierType):
    class Meta:
        name = "TransportExecutionPlanReferenceIDType"


@dataclass
class TransportExecutionStatusCodeType(CodeType):
    pass


@dataclass
class TransportHandlingUnitTypeCodeType(CodeType):
    pass


@dataclass
class TransportMeansTypeCodeType(CodeType):
    pass


@dataclass
class TransportModeCodeType(CodeType):
    pass


@dataclass
class TransportServiceCodeType(CodeType):
    pass


@dataclass
class TransportServiceProviderRemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TransportServiceProviderSpecialTermsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TransportUserRemarksType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TransportUserSpecialTermsType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TransportationServiceDescriptionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class TransportationServiceDetailsUritype(IdentifierType):
    class Meta:
        name = "TransportationServiceDetailsURIType"


@dataclass
class TransportationStatusTypeCodeType(CodeType):
    pass


@dataclass
class TypeCodeType(CodeType):
    pass


@dataclass
class UblversionIdtype(IdentifierType):
    class Meta:
        name = "UBLVersionIDType"


@dataclass
class UndgcodeType(CodeType):
    class Meta:
        name = "UNDGCodeType"


@dataclass
class Uritype(IdentifierType):
    class Meta:
        name = "URIType"


@dataclass
class Uuidtype(IdentifierType):
    class Meta:
        name = "UUIDType"


@dataclass
class UpperOrangeHazardPlacardIdtype(IdentifierType):
    class Meta:
        name = "UpperOrangeHazardPlacardIDType"


@dataclass
class UrgencyCodeType(CodeType):
    pass


@dataclass
class UtilityStatementTypeCodeType(CodeType):
    pass


@dataclass
class ValidateProcessType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ValidateToolType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ValidateToolVersionType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ValidationResultCodeType(CodeType):
    pass


@dataclass
class ValidatorIdtype(IdentifierType):
    class Meta:
        name = "ValidatorIDType"


@dataclass
class ValueAmountType(UblUnqualifiedDataTypes21AmountType):
    pass


@dataclass
class ValueMeasureType(UblUnqualifiedDataTypes21MeasureType):
    pass


@dataclass
class ValueQualifierType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class ValueQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class ValueType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class VarianceQuantityType(UblUnqualifiedDataTypes21QuantityType):
    pass


@dataclass
class VariantIdtype(IdentifierType):
    class Meta:
        name = "VariantIDType"


@dataclass
class VersionIdtype(IdentifierType):
    class Meta:
        name = "VersionIDType"


@dataclass
class VesselIdtype(IdentifierType):
    class Meta:
        name = "VesselIDType"


@dataclass
class VesselNameType(UblUnqualifiedDataTypes21NameType):
    pass


@dataclass
class WarrantyInformationType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class WebsiteUritype(IdentifierType):
    class Meta:
        name = "WebsiteURIType"


@dataclass
class WeekDayCodeType(CodeType):
    pass


@dataclass
class WeightNumericType(NumericType):
    pass


@dataclass
class WeightType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class WeightingAlgorithmCodeType(CodeType):
    pass


@dataclass
class WorkPhaseCodeType(CodeType):
    pass


@dataclass
class WorkPhaseType(UblUnqualifiedDataTypes21TextType):
    pass


@dataclass
class XpathType(UblUnqualifiedDataTypes21TextType):
    class Meta:
        name = "XPathType"


@dataclass
class AcceptedVariantsDescription(AcceptedVariantsDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AccountFormatCode(AccountFormatCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AccountId(AccountIdtype):
    class Meta:
        name = "AccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AccountTypeCode(AccountTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AccountingCost(AccountingCostType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AccountingCostCode(AccountingCostCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ActionCode(ActionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ActivityType(ActivityTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ActivityTypeCode(ActivityTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ActualTemperatureReductionQuantity(ActualTemperatureReductionQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AdditionalAccountId(AdditionalAccountIdtype):
    class Meta:
        name = "AdditionalAccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AdditionalConditions(AdditionalConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AdditionalInformation(AdditionalInformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AdditionalStreetName(AdditionalStreetNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AddressFormatCode(AddressFormatCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AddressTypeCode(AddressTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AdjustmentReasonCode(AdjustmentReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AdmissionCode(AdmissionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AdvertisementAmount(AdvertisementAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AgencyId(AgencyIdtype):
    class Meta:
        name = "AgencyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AgencyName(AgencyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AirFlowPercent(AirFlowPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AircraftId(AircraftIdtype):
    class Meta:
        name = "AircraftID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AliasName(AliasNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AllowanceChargeReason(AllowanceChargeReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AllowanceChargeReasonCode(AllowanceChargeReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AllowanceTotalAmount(AllowanceTotalAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AltitudeMeasure(AltitudeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Amount(AmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AmountRate(AmountRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AnnualAverageAmount(AnnualAverageAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ApplicationStatusCode(ApplicationStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ApprovalStatus(ApprovalStatusType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AttributeId(AttributeIdtype):
    class Meta:
        name = "AttributeID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AuctionUri(AuctionUritype):
    class Meta:
        name = "AuctionURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AvailabilityStatusCode(AvailabilityStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AverageAmount(AverageAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AverageSubsequentContractAmount(AverageSubsequentContractAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AwardingCriterionDescription(AwardingCriterionDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AwardingCriterionId(AwardingCriterionIdtype):
    class Meta:
        name = "AwardingCriterionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AwardingCriterionTypeCode(AwardingCriterionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class AwardingMethodTypeCode(AwardingMethodTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BackorderQuantity(BackorderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BackorderReason(BackorderReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BalanceAmount(BalanceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BarcodeSymbologyId(BarcodeSymbologyIdtype):
    class Meta:
        name = "BarcodeSymbologyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BaseAmount(BaseAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BaseQuantity(BaseQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BaseUnitMeasure(BaseUnitMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BasicConsumedQuantity(BasicConsumedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BatchQuantity(BatchQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BirthplaceName(BirthplaceNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BlockName(BlockNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BrandName(BrandNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BrokerAssignedId(BrokerAssignedIdtype):
    class Meta:
        name = "BrokerAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BudgetYearNumeric(BudgetYearNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BuildingName(BuildingNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BuildingNumber(BuildingNumberType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BusinessClassificationEvidenceId(BusinessClassificationEvidenceIdtype):
    class Meta:
        name = "BusinessClassificationEvidenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BusinessIdentityEvidenceId(BusinessIdentityEvidenceIdtype):
    class Meta:
        name = "BusinessIdentityEvidenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BuyerEventId(BuyerEventIdtype):
    class Meta:
        name = "BuyerEventID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BuyerProfileUri(BuyerProfileUritype):
    class Meta:
        name = "BuyerProfileURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class BuyerReference(BuyerReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Cv2Id(Cv2Idtype):
    class Meta:
        name = "CV2ID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CalculationExpression(CalculationExpressionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CalculationExpressionCode(CalculationExpressionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CalculationMethodCode(CalculationMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CalculationRate(CalculationRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CalculationSequenceNumeric(CalculationSequenceNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CallBaseAmount(CallBaseAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CallExtensionAmount(CallExtensionAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CancellationNote(CancellationNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CandidateStatement(CandidateStatementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CanonicalizationMethod(CanonicalizationMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CapabilityTypeCode(CapabilityTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CardChipCode(CardChipCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CardTypeCode(CardTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CargoTypeCode(CargoTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CarrierAssignedId(CarrierAssignedIdtype):
    class Meta:
        name = "CarrierAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CarrierServiceInstructions(CarrierServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CategoryName(CategoryNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CertificateType(CertificateTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CertificateTypeCode(CertificateTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ChangeConditions(ChangeConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Channel(ChannelType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ChannelCode(ChannelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CharacterSetCode(CharacterSetCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Characteristics(CharacteristicsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ChargeTotalAmount(ChargeTotalAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ChargeableQuantity(ChargeableQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ChargeableWeightMeasure(ChargeableWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ChildConsignmentQuantity(ChildConsignmentQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ChipApplicationId(ChipApplicationIdtype):
    class Meta:
        name = "ChipApplicationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CityName(CityNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CitySubdivisionName(CitySubdivisionNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CodeValue(CodeValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CollaborationPriorityCode(CollaborationPriorityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Comment(CommentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CommodityCode(CommodityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CompanyId(CompanyIdtype):
    class Meta:
        name = "CompanyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CompanyLegalForm(CompanyLegalFormType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CompanyLegalFormCode(CompanyLegalFormCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CompanyLiquidationStatusCode(CompanyLiquidationStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ComparedValueMeasure(ComparedValueMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ComparisonDataCode(ComparisonDataCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ComparisonDataSourceCode(ComparisonDataSourceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Condition(ConditionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConditionCode(ConditionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Conditions(ConditionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConditionsDescription(ConditionsDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsigneeAssignedId(ConsigneeAssignedIdtype):
    class Meta:
        name = "ConsigneeAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsignmentQuantity(ConsignmentQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsignorAssignedId(ConsignorAssignedIdtype):
    class Meta:
        name = "ConsignorAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConstitutionCode(ConstitutionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumerIncentiveTacticTypeCode(ConsumerIncentiveTacticTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumerUnitQuantity(ConsumerUnitQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumersEnergyLevel(ConsumersEnergyLevelType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumersEnergyLevelCode(ConsumersEnergyLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumptionEnergyQuantity(ConsumptionEnergyQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumptionId(ConsumptionIdtype):
    class Meta:
        name = "ConsumptionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumptionLevel(ConsumptionLevelType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumptionLevelCode(ConsumptionLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumptionReportId(ConsumptionReportIdtype):
    class Meta:
        name = "ConsumptionReportID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumptionType(ConsumptionTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumptionTypeCode(ConsumptionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ConsumptionWaterQuantity(ConsumptionWaterQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Content(ContentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ContentUnitQuantity(ContentUnitQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ContractFolderId(ContractFolderIdtype):
    class Meta:
        name = "ContractFolderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ContractName(ContractNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ContractSubdivision(ContractSubdivisionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ContractType(ContractTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ContractTypeCode(ContractTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ContractedCarrierAssignedId(ContractedCarrierAssignedIdtype):
    class Meta:
        name = "ContractedCarrierAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ContractingSystemCode(ContractingSystemCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CoordinateSystemCode(CoordinateSystemCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CorporateRegistrationTypeCode(CorporateRegistrationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CorporateStockAmount(CorporateStockAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CorrectionAmount(CorrectionAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CorrectionType(CorrectionTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CorrectionTypeCode(CorrectionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CorrectionUnitAmount(CorrectionUnitAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CountrySubentity(CountrySubentityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CountrySubentityCode(CountrySubentityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CreditLineAmount(CreditLineAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CreditNoteTypeCode(CreditNoteTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CreditedQuantity(CreditedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CrewQuantity(CrewQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CurrencyCode(CurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CurrentChargeType(CurrentChargeTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CurrentChargeTypeCode(CurrentChargeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CustomerAssignedAccountId(CustomerAssignedAccountIdtype):
    class Meta:
        name = "CustomerAssignedAccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CustomerReference(CustomerReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CustomizationId(CustomizationIdtype):
    class Meta:
        name = "CustomizationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CustomsClearanceServiceInstructions(CustomsClearanceServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CustomsStatusCode(CustomsStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class CustomsTariffQuantity(CustomsTariffQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DamageRemarks(DamageRemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DataSendingCapability(DataSendingCapabilityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DataSourceCode(DataSourceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DebitLineAmount(DebitLineAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DebitedQuantity(DebitedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DeclarationTypeCode(DeclarationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DeclaredCarriageValueAmount(DeclaredCarriageValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DeclaredCustomsValueAmount(DeclaredCustomsValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DeclaredForCarriageValueAmount(DeclaredForCarriageValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DeclaredStatisticsValueAmount(DeclaredStatisticsValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DeliveredQuantity(DeliveredQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DeliveryInstructions(DeliveryInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DemurrageInstructions(DemurrageInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Department(DepartmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Description(DescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DescriptionCode(DescriptionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DespatchAdviceTypeCode(DespatchAdviceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DifferenceTemperatureReductionQuantity(DifferenceTemperatureReductionQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DirectionCode(DirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DisplayTacticTypeCode(DisplayTacticTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DispositionCode(DispositionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class District(DistrictType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentCurrencyCode(DocumentCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentDescription(DocumentDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentHash(DocumentHashType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentId(DocumentIdtype):
    class Meta:
        name = "DocumentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentStatusCode(DocumentStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentStatusReasonCode(DocumentStatusReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentStatusReasonDescription(DocumentStatusReasonDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentType(DocumentTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentTypeCode(DocumentTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DocumentationFeeAmount(DocumentationFeeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DurationMeasure(DurationMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Duty(DutyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class DutyCode(DutyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EconomicOperatorRegistryUri(EconomicOperatorRegistryUritype):
    class Meta:
        name = "EconomicOperatorRegistryURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ElectronicDeviceDescription(ElectronicDeviceDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ElectronicMail(ElectronicMailType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EmbeddedDocumentBinaryObject(EmbeddedDocumentBinaryObjectType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EmergencyProceduresCode(EmergencyProceduresCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EmployeeQuantity(EmployeeQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EncodingCode(EncodingCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EndpointId(EndpointIdtype):
    class Meta:
        name = "EndpointID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EnvironmentalEmissionTypeCode(EnvironmentalEmissionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EstimatedAmount(EstimatedAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EstimatedConsumedQuantity(EstimatedConsumedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EstimatedOverallContractAmount(EstimatedOverallContractAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EstimatedOverallContractQuantity(EstimatedOverallContractQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EvaluationCriterionTypeCode(EvaluationCriterionTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class EvidenceTypeCode(EvidenceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExceptionResolutionCode(ExceptionResolutionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExceptionStatusCode(ExceptionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExchangeMarketId(ExchangeMarketIdtype):
    class Meta:
        name = "ExchangeMarketID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExclusionReason(ExclusionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExecutionRequirementCode(ExecutionRequirementCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExemptionReason(ExemptionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExemptionReasonCode(ExemptionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExpectedOperatorQuantity(ExpectedOperatorQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExpectedQuantity(ExpectedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExpenseCode(ExpenseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Expression(ExpressionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExpressionCode(ExpressionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ExtendedId(ExtendedIdtype):
    class Meta:
        name = "ExtendedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Extension(ExtensionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FaceValueAmount(FaceValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FamilyName(FamilyNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FeatureTacticTypeCode(FeatureTacticTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FeeAmount(FeeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FeeDescription(FeeDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FileName(FileNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FinancingInstrumentCode(FinancingInstrumentCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FirstName(FirstNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Floor(FloorType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ForecastPurposeCode(ForecastPurposeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ForecastTypeCode(ForecastTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FormatCode(FormatCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ForwarderServiceInstructions(ForwarderServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FreeOnBoardValueAmount(FreeOnBoardValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FreightForwarderAssignedId(FreightForwarderAssignedIdtype):
    class Meta:
        name = "FreightForwarderAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FreightRateClassCode(FreightRateClassCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Frequency(FrequencyType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FrozenPeriodDaysNumeric(FrozenPeriodDaysNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FullnessIndicationCode(FullnessIndicationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FundingProgram(FundingProgramType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class FundingProgramCode(FundingProgramCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class GasPressureQuantity(GasPressureQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class GenderCode(GenderCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class GrossTonnageMeasure(GrossTonnageMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class GrossVolumeMeasure(GrossVolumeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class GrossWeightMeasure(GrossWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class GuaranteeTypeCode(GuaranteeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HandlingCode(HandlingCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HandlingInstructions(HandlingInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HashAlgorithmMethod(HashAlgorithmMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HaulageInstructions(HaulageInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HazardClassId(HazardClassIdtype):
    class Meta:
        name = "HazardClassID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HazardousCategoryCode(HazardousCategoryCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HazardousRegulationCode(HazardousRegulationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HeatingType(HeatingTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HeatingTypeCode(HeatingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HigherTenderAmount(HigherTenderAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HolderName(HolderNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class HumidityPercent(HumidityPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Id(Idtype):
    class Meta:
        name = "ID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class IdentificationCode(IdentificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class IdentificationId(IdentificationIdtype):
    class Meta:
        name = "IdentificationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ImmobilizationCertificateId(ImmobilizationCertificateIdtype):
    class Meta:
        name = "ImmobilizationCertificateID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ImportanceCode(ImportanceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class IndustryClassificationCode(IndustryClassificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Information(InformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InformationUri(InformationUritype):
    class Meta:
        name = "InformationURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InhalationToxicityZoneCode(InhalationToxicityZoneCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InhouseMail(InhouseMailType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InspectionMethodCode(InspectionMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InstructionId(InstructionIdtype):
    class Meta:
        name = "InstructionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InstructionNote(InstructionNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Instructions(InstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InsurancePremiumAmount(InsurancePremiumAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InsuranceValueAmount(InsuranceValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InventoryValueAmount(InventoryValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InvoiceTypeCode(InvoiceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InvoicedQuantity(InvoicedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class InvoicingPartyReference(InvoicingPartyReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class IssueNumberId(IssueNumberIdtype):
    class Meta:
        name = "IssueNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class IssuerId(IssuerIdtype):
    class Meta:
        name = "IssuerID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ItemClassificationCode(ItemClassificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class JobTitle(JobTitleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class JourneyId(JourneyIdtype):
    class Meta:
        name = "JourneyID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Justification(JustificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class JustificationDescription(JustificationDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Keyword(KeywordType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LanguageId(LanguageIdtype):
    class Meta:
        name = "LanguageID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LatestMeterQuantity(LatestMeterQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LatestMeterReadingMethod(LatestMeterReadingMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LatestMeterReadingMethodCode(LatestMeterReadingMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LatitudeDegreesMeasure(LatitudeDegreesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LatitudeDirectionCode(LatitudeDirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LatitudeMinutesMeasure(LatitudeMinutesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LeadTimeMeasure(LeadTimeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LegalReference(LegalReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LiabilityAmount(LiabilityAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LicensePlateId(LicensePlateIdtype):
    class Meta:
        name = "LicensePlateID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LifeCycleStatusCode(LifeCycleStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LimitationDescription(LimitationDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Line(LineType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LineCountNumeric(LineCountNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LineExtensionAmount(LineExtensionAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LineId(LineIdtype):
    class Meta:
        name = "LineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LineNumberNumeric(LineNumberNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LineStatusCode(LineStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ListValue(ListValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LoadingLengthMeasure(LoadingLengthMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LoadingSequenceId(LoadingSequenceIdtype):
    class Meta:
        name = "LoadingSequenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LocaleCode(LocaleCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Location(LocationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LocationId(LocationIdtype):
    class Meta:
        name = "LocationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LocationTypeCode(LocationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Login(LoginType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LogoReferenceId(LogoReferenceIdtype):
    class Meta:
        name = "LogoReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LongitudeDegreesMeasure(LongitudeDegreesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LongitudeDirectionCode(LongitudeDirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LongitudeMinutesMeasure(LongitudeMinutesMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LossRisk(LossRiskType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LossRiskResponsibilityCode(LossRiskResponsibilityCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LotNumberId(LotNumberIdtype):
    class Meta:
        name = "LotNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LowTendersDescription(LowTendersDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LowerOrangeHazardPlacardId(LowerOrangeHazardPlacardIdtype):
    class Meta:
        name = "LowerOrangeHazardPlacardID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class LowerTenderAmount(LowerTenderAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MandateTypeCode(MandateTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MarkAttention(MarkAttentionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MarkCare(MarkCareType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MarketValueAmount(MarketValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MarkingId(MarkingIdtype):
    class Meta:
        name = "MarkingID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MathematicOperatorCode(MathematicOperatorCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumAdvertisementAmount(MaximumAdvertisementAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumAmount(MaximumAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumBackorderQuantity(MaximumBackorderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumCopiesNumeric(MaximumCopiesNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumMeasure(MaximumMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumNumberNumeric(MaximumNumberNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumOperatorQuantity(MaximumOperatorQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumOrderQuantity(MaximumOrderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumPaidAmount(MaximumPaidAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumPaymentInstructionsNumeric(MaximumPaymentInstructionsNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumPercent(MaximumPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumQuantity(MaximumQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumValue(MaximumValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MaximumVariantQuantity(MaximumVariantQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Measure(MeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MedicalFirstAidGuideCode(MedicalFirstAidGuideCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MeterConstant(MeterConstantType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MeterConstantCode(MeterConstantCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MeterName(MeterNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MeterNumber(MeterNumberType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MeterReadingComments(MeterReadingCommentsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MeterReadingType(MeterReadingTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MeterReadingTypeCode(MeterReadingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MiddleName(MiddleNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MimeCode(MimeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumAmount(MinimumAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumBackorderQuantity(MinimumBackorderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumImprovementBid(MinimumImprovementBidType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumInventoryQuantity(MinimumInventoryQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumMeasure(MinimumMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumNumberNumeric(MinimumNumberNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumOrderQuantity(MinimumOrderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumPercent(MinimumPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumQuantity(MinimumQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MinimumValue(MinimumValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MiscellaneousEventTypeCode(MiscellaneousEventTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ModelName(ModelNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MonetaryScope(MonetaryScopeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MovieTitle(MovieTitleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MultipleOrderQuantity(MultipleOrderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class MultiplierFactorNumeric(MultiplierFactorNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Name(NameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NameCode(NameCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NameSuffix(NameSuffixType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NationalityId(NationalityIdtype):
    class Meta:
        name = "NationalityID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NatureCode(NatureCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NegotiationDescription(NegotiationDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NetNetWeightMeasure(NetNetWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NetTonnageMeasure(NetTonnageMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NetVolumeMeasure(NetVolumeMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NetWeightMeasure(NetWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NetworkId(NetworkIdtype):
    class Meta:
        name = "NetworkID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NormalTemperatureReductionQuantity(NormalTemperatureReductionQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Note(NoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class NotificationTypeCode(NotificationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OneTimeChargeType(OneTimeChargeTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OneTimeChargeTypeCode(OneTimeChargeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OntologyUri(OntologyUritype):
    class Meta:
        name = "OntologyURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OpenTenderId(OpenTenderIdtype):
    class Meta:
        name = "OpenTenderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OperatingYearsQuantity(OperatingYearsQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OptionsDescription(OptionsDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OrderIntervalDaysNumeric(OrderIntervalDaysNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OrderQuantityIncrementNumeric(OrderQuantityIncrementNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OrderResponseCode(OrderResponseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OrderTypeCode(OrderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OrderableUnit(OrderableUnitType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OrderableUnitFactorRate(OrderableUnitFactorRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OrganizationDepartment(OrganizationDepartmentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OriginalContractingSystemId(OriginalContractingSystemIdtype):
    class Meta:
        name = "OriginalContractingSystemID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OriginalJobId(OriginalJobIdtype):
    class Meta:
        name = "OriginalJobID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OtherInstruction(OtherInstructionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OtherName(OtherNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OutstandingQuantity(OutstandingQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OutstandingReason(OutstandingReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OversupplyQuantity(OversupplyQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class OwnerTypeCode(OwnerTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PackLevelCode(PackLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PackQuantity(PackQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PackSizeNumeric(PackSizeNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PackageLevelCode(PackageLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PackagingTypeCode(PackagingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PackingCriteriaCode(PackingCriteriaCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PackingMaterial(PackingMaterialType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaidAmount(PaidAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ParentDocumentId(ParentDocumentIdtype):
    class Meta:
        name = "ParentDocumentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ParentDocumentLineReferenceId(ParentDocumentLineReferenceIdtype):
    class Meta:
        name = "ParentDocumentLineReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ParentDocumentTypeCode(ParentDocumentTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ParentDocumentVersionId(ParentDocumentVersionIdtype):
    class Meta:
        name = "ParentDocumentVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PartPresentationCode(PartPresentationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PartecipationPercent(PartecipationPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ParticipationPercent(ParticipationPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PartyCapacityAmount(PartyCapacityAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PartyType(PartyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PartyTypeCode(PartyTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PassengerQuantity(PassengerQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Password(PasswordType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PayPerView(PayPerViewType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PayableAlternativeAmount(PayableAlternativeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PayableAmount(PayableAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PayableRoundingAmount(PayableRoundingAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PayerReference(PayerReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentAlternativeCurrencyCode(PaymentAlternativeCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentChannelCode(PaymentChannelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentCurrencyCode(PaymentCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentDescription(PaymentDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentFrequencyCode(PaymentFrequencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentId(PaymentIdtype):
    class Meta:
        name = "PaymentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentMeansCode(PaymentMeansCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentMeansId(PaymentMeansIdtype):
    class Meta:
        name = "PaymentMeansID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentNote(PaymentNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentOrderReference(PaymentOrderReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentPercent(PaymentPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentPurposeCode(PaymentPurposeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PaymentTermsDetailsUri(PaymentTermsDetailsUritype):
    class Meta:
        name = "PaymentTermsDetailsURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PenaltyAmount(PenaltyAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PenaltySurchargePercent(PenaltySurchargePercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PerUnitAmount(PerUnitAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Percent(PercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PerformanceMetricTypeCode(PerformanceMetricTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PerformanceValueQuantity(PerformanceValueQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PerformingCarrierAssignedId(PerformingCarrierAssignedIdtype):
    class Meta:
        name = "PerformingCarrierAssignedID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PersonalSituation(PersonalSituationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PhoneNumber(PhoneNumberType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PlacardEndorsement(PlacardEndorsementType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PlacardNotation(PlacardNotationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PlotIdentification(PlotIdentificationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PositionCode(PositionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PostEventNotificationDurationMeasure(PostEventNotificationDurationMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PostalZone(PostalZoneType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Postbox(PostboxType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PreEventNotificationDurationMeasure(PreEventNotificationDurationMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PreferenceCriterionCode(PreferenceCriterionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PrepaidAmount(PrepaidAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PrepaidPaymentReferenceId(PrepaidPaymentReferenceIdtype):
    class Meta:
        name = "PrepaidPaymentReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PreviousCancellationReasonCode(PreviousCancellationReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PreviousJobId(PreviousJobIdtype):
    class Meta:
        name = "PreviousJobID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PreviousMeterQuantity(PreviousMeterQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PreviousMeterReadingMethod(PreviousMeterReadingMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PreviousMeterReadingMethodCode(PreviousMeterReadingMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PreviousVersionId(PreviousVersionIdtype):
    class Meta:
        name = "PreviousVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PriceAmount(PriceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PriceChangeReason(PriceChangeReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PriceEvaluationCode(PriceEvaluationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PriceRevisionFormulaDescription(PriceRevisionFormulaDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PriceType(PriceTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PriceTypeCode(PriceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PricingCurrencyCode(PricingCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PrimaryAccountNumberId(PrimaryAccountNumberIdtype):
    class Meta:
        name = "PrimaryAccountNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PrintQualifier(PrintQualifierType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Priority(PriorityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PrivacyCode(PrivacyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PrizeDescription(PrizeDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProcedureCode(ProcedureCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProcessDescription(ProcessDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProcessReason(ProcessReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProcessReasonCode(ProcessReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProcurementSubTypeCode(ProcurementSubTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProcurementTypeCode(ProcurementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProductTraceId(ProductTraceIdtype):
    class Meta:
        name = "ProductTraceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProfileExecutionId(ProfileExecutionIdtype):
    class Meta:
        name = "ProfileExecutionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProfileId(ProfileIdtype):
    class Meta:
        name = "ProfileID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProfileStatusCode(ProfileStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProgressPercent(ProgressPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PromotionalEventTypeCode(PromotionalEventTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ProviderTypeCode(ProviderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Purpose(PurposeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class PurposeCode(PurposeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class QualityControlCode(QualityControlCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Quantity(QuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class QuantityDiscrepancyCode(QuantityDiscrepancyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RadioCallSignId(RadioCallSignIdtype):
    class Meta:
        name = "RadioCallSignID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RailCarId(RailCarIdtype):
    class Meta:
        name = "RailCarID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Rank(RankType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Rate(RateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReceiptAdviceTypeCode(ReceiptAdviceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReceivedElectronicTenderQuantity(ReceivedElectronicTenderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReceivedForeignTenderQuantity(ReceivedForeignTenderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReceivedQuantity(ReceivedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReceivedTenderQuantity(ReceivedTenderQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Reference(ReferenceType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReferenceEventCode(ReferenceEventCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReferenceId(ReferenceIdtype):
    class Meta:
        name = "ReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReferencedConsignmentId(ReferencedConsignmentIdtype):
    class Meta:
        name = "ReferencedConsignmentID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Region(RegionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RegistrationId(RegistrationIdtype):
    class Meta:
        name = "RegistrationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RegistrationName(RegistrationNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RegistrationNationality(RegistrationNationalityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RegistrationNationalityId(RegistrationNationalityIdtype):
    class Meta:
        name = "RegistrationNationalityID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RegulatoryDomain(RegulatoryDomainType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RejectActionCode(RejectActionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RejectReason(RejectReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RejectReasonCode(RejectReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RejectedQuantity(RejectedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RejectionNote(RejectionNoteType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReleaseId(ReleaseIdtype):
    class Meta:
        name = "ReleaseID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReliabilityPercent(ReliabilityPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Remarks(RemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReminderSequenceNumeric(ReminderSequenceNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReminderTypeCode(ReminderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReplenishmentOwnerDescription(ReplenishmentOwnerDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RequestForQuotationLineId(RequestForQuotationLineIdtype):
    class Meta:
        name = "RequestForQuotationLineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RequestedInvoiceCurrencyCode(RequestedInvoiceCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RequiredCustomsId(RequiredCustomsIdtype):
    class Meta:
        name = "RequiredCustomsID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RequiredFeeAmount(RequiredFeeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ResidenceType(ResidenceTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ResidenceTypeCode(ResidenceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ResidentOccupantsNumeric(ResidentOccupantsNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Resolution(ResolutionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ResolutionCode(ResolutionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ResponseCode(ResponseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RetailEventName(RetailEventNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RetailEventStatusCode(RetailEventStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ReturnableQuantity(ReturnableQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RevisedForecastLineId(RevisedForecastLineIdtype):
    class Meta:
        name = "RevisedForecastLineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RevisionStatusCode(RevisionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RoamingPartnerName(RoamingPartnerNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RoleCode(RoleCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RoleDescription(RoleDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Room(RoomType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class RoundingAmount(RoundingAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SalesOrderId(SalesOrderIdtype):
    class Meta:
        name = "SalesOrderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SalesOrderLineId(SalesOrderLineIdtype):
    class Meta:
        name = "SalesOrderLineID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SchemeUri(SchemeUritype):
    class Meta:
        name = "SchemeURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SealIssuerTypeCode(SealIssuerTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SealStatusCode(SealStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SealingPartyType(SealingPartyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SecurityClassificationCode(SecurityClassificationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SecurityId(SecurityIdtype):
    class Meta:
        name = "SecurityID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SellerEventId(SellerEventIdtype):
    class Meta:
        name = "SellerEventID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SequenceId(SequenceIdtype):
    class Meta:
        name = "SequenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SequenceNumberId(SequenceNumberIdtype):
    class Meta:
        name = "SequenceNumberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SequenceNumeric(SequenceNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SerialId(SerialIdtype):
    class Meta:
        name = "SerialID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ServiceInformationPreferenceCode(ServiceInformationPreferenceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ServiceName(ServiceNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ServiceNumberCalled(ServiceNumberCalledType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ServiceType(ServiceTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ServiceTypeCode(ServiceTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SettlementDiscountAmount(SettlementDiscountAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SettlementDiscountPercent(SettlementDiscountPercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SharesNumberQuantity(SharesNumberQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ShippingMarks(ShippingMarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ShippingOrderId(ShippingOrderIdtype):
    class Meta:
        name = "ShippingOrderID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ShippingPriorityLevelCode(ShippingPriorityLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ShipsRequirements(ShipsRequirementsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ShortQuantity(ShortQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ShortageActionCode(ShortageActionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SignatureId(SignatureIdtype):
    class Meta:
        name = "SignatureID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SignatureMethod(SignatureMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SizeTypeCode(SizeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SourceCurrencyBaseRate(SourceCurrencyBaseRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SourceCurrencyCode(SourceCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SourceValueMeasure(SourceValueMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SpecialInstructions(SpecialInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SpecialServiceInstructions(SpecialServiceInstructionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SpecialTerms(SpecialTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SpecialTransportRequirements(SpecialTransportRequirementsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SpecificationId(SpecificationIdtype):
    class Meta:
        name = "SpecificationID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SpecificationTypeCode(SpecificationTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class StatementTypeCode(StatementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class StatusCode(StatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class StatusReason(StatusReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class StatusReasonCode(StatusReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class StreetName(StreetNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SubcontractingConditionsCode(SubcontractingConditionsCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SubmissionMethodCode(SubmissionMethodCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SubscriberId(SubscriberIdtype):
    class Meta:
        name = "SubscriberID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SubscriberType(SubscriberTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SubscriberTypeCode(SubscriberTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SubstitutionStatusCode(SubstitutionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SuccessiveSequenceId(SuccessiveSequenceIdtype):
    class Meta:
        name = "SuccessiveSequenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SummaryDescription(SummaryDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SupplierAssignedAccountId(SupplierAssignedAccountIdtype):
    class Meta:
        name = "SupplierAssignedAccountID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class SupplyChainActivityTypeCode(SupplyChainActivityTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TareWeightMeasure(TareWeightMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TargetCurrencyBaseRate(TargetCurrencyBaseRateType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TargetCurrencyCode(TargetCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TargetInventoryQuantity(TargetInventoryQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TargetServicePercent(TargetServicePercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TariffClassCode(TariffClassCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TariffCode(TariffCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TariffDescription(TariffDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxAmount(TaxAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxCurrencyCode(TaxCurrencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxEnergyAmount(TaxEnergyAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxEnergyBalanceAmount(TaxEnergyBalanceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxEnergyOnAccountAmount(TaxEnergyOnAccountAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxExclusiveAmount(TaxExclusiveAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxExemptionReason(TaxExemptionReasonType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxExemptionReasonCode(TaxExemptionReasonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxInclusiveAmount(TaxInclusiveAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxLevelCode(TaxLevelCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxTypeCode(TaxTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TaxableAmount(TaxableAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TechnicalCommitteeDescription(TechnicalCommitteeDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TechnicalName(TechnicalNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TelecommunicationsServiceCall(TelecommunicationsServiceCallType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TelecommunicationsServiceCallCode(TelecommunicationsServiceCallCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TelecommunicationsServiceCategory(TelecommunicationsServiceCategoryType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TelecommunicationsServiceCategoryCode(TelecommunicationsServiceCategoryCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TelecommunicationsSupplyType(TelecommunicationsSupplyTypeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TelecommunicationsSupplyTypeCode(TelecommunicationsSupplyTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Telefax(TelefaxType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Telephone(TelephoneType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TenderEnvelopeId(TenderEnvelopeIdtype):
    class Meta:
        name = "TenderEnvelopeID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TenderEnvelopeTypeCode(TenderEnvelopeTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TenderResultCode(TenderResultCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TenderTypeCode(TenderTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TendererRequirementTypeCode(TendererRequirementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TendererRoleCode(TendererRoleCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TestMethod(TestMethodType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Text(TextType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ThresholdAmount(ThresholdAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ThresholdQuantity(ThresholdQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ThresholdValueComparisonCode(ThresholdValueComparisonCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TierRange(TierRangeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TierRatePercent(TierRatePercentType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TimeAmount(TimeAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TimeDeltaDaysQuantity(TimeDeltaDaysQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TimeFrequencyCode(TimeFrequencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TimezoneOffset(TimezoneOffsetType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TimingComplaint(TimingComplaintType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TimingComplaintCode(TimingComplaintCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Title(TitleType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalAmount(TotalAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalBalanceAmount(TotalBalanceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalConsumedQuantity(TotalConsumedQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalCreditAmount(TotalCreditAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalDebitAmount(TotalDebitAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalDeliveredQuantity(TotalDeliveredQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalGoodsItemQuantity(TotalGoodsItemQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalInvoiceAmount(TotalInvoiceAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalMeteredQuantity(TotalMeteredQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalPackageQuantity(TotalPackageQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalPackagesQuantity(TotalPackagesQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalPaymentAmount(TotalPaymentAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalTaskAmount(TotalTaskAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalTaxAmount(TotalTaxAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TotalTransportHandlingUnitQuantity(TotalTransportHandlingUnitQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TraceId(TraceIdtype):
    class Meta:
        name = "TraceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TrackingDeviceCode(TrackingDeviceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TrackingId(TrackingIdtype):
    class Meta:
        name = "TrackingID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TradeItemPackingLabelingTypeCode(TradeItemPackingLabelingTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TradeServiceCode(TradeServiceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TradingRestrictions(TradingRestrictionsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TrainId(TrainIdtype):
    class Meta:
        name = "TrainID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransactionCurrencyTaxAmount(TransactionCurrencyTaxAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransitDirectionCode(TransitDirectionCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportAuthorizationCode(TransportAuthorizationCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportEmergencyCardCode(TransportEmergencyCardCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportEquipmentTypeCode(TransportEquipmentTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportEventTypeCode(TransportEventTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportExecutionPlanReferenceId(TransportExecutionPlanReferenceIdtype):
    class Meta:
        name = "TransportExecutionPlanReferenceID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportExecutionStatusCode(TransportExecutionStatusCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportHandlingUnitTypeCode(TransportHandlingUnitTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportMeansTypeCode(TransportMeansTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportModeCode(TransportModeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportServiceCode(TransportServiceCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportServiceProviderRemarks(TransportServiceProviderRemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportServiceProviderSpecialTerms(TransportServiceProviderSpecialTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportUserRemarks(TransportUserRemarksType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportUserSpecialTerms(TransportUserSpecialTermsType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportationServiceDescription(TransportationServiceDescriptionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportationServiceDetailsUri(TransportationServiceDetailsUritype):
    class Meta:
        name = "TransportationServiceDetailsURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TransportationStatusTypeCode(TransportationStatusTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class TypeCode(TypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class UblversionId(UblversionIdtype):
    class Meta:
        name = "UBLVersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Undgcode(UndgcodeType):
    class Meta:
        name = "UNDGCode"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Uri(Uritype):
    class Meta:
        name = "URI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Uuid(Uuidtype):
    class Meta:
        name = "UUID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class UpperOrangeHazardPlacardId(UpperOrangeHazardPlacardIdtype):
    class Meta:
        name = "UpperOrangeHazardPlacardID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class UrgencyCode(UrgencyCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class UtilityStatementTypeCode(UtilityStatementTypeCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ValidateProcess(ValidateProcessType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ValidateTool(ValidateToolType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ValidateToolVersion(ValidateToolVersionType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ValidationResultCode(ValidationResultCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ValidatorId(ValidatorIdtype):
    class Meta:
        name = "ValidatorID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Value(ValueType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ValueAmount(ValueAmountType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ValueMeasure(ValueMeasureType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ValueQualifier(ValueQualifierType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class ValueQuantity(ValueQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class VarianceQuantity(VarianceQuantityType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class VariantId(VariantIdtype):
    class Meta:
        name = "VariantID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class VersionId(VersionIdtype):
    class Meta:
        name = "VersionID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class VesselId(VesselIdtype):
    class Meta:
        name = "VesselID"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class VesselName(VesselNameType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class WarrantyInformation(WarrantyInformationType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class WebsiteUri(WebsiteUritype):
    class Meta:
        name = "WebsiteURI"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class WeekDayCode(WeekDayCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Weight(WeightType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class WeightNumeric(WeightNumericType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class WeightingAlgorithmCode(WeightingAlgorithmCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class WorkPhase(WorkPhaseType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class WorkPhaseCode(WorkPhaseCodeType):
    class Meta:
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


@dataclass
class Xpath(XpathType):
    class Meta:
        name = "XPath"
        namespace = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
