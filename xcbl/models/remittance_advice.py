from dataclasses import dataclass, field
from typing import Optional

from xcbl.models.request_for_quotation import (
    AccountNumber,
    BuyersCatalogNumber,
    ContractReference,
    FinancialInstitution,
    PaymentInstructions,
    PriceListNumber,
    PriceListVersionNumber,
)
from xcbl.models.shipping_schedule_response import (
    BuyerOrderNumber,
    ListOfMessageId,
    SellerOrderNumber,
    Sequence,
    TransportRouteId,
)
from xcbl.models.sourcing_result import (
    Attachment,
    BillToParty,
    BuyerParty,
    CatalogReference,
    ConditionsOfSale,
    CountryOfDestination,
    CountryOfOrigin,
    DeliveryDetail,
    FinalRecipient,
    HazardousMaterials,
    ItemAllowancesOrCharges,
    ItemContractReferences,
    ItemIdentifiers,
    LineItemAttachments,
    LineItemNote,
    LineItemNum,
    LineItemType,
    ListOfDateCoded,
    ListOfItemReferences,
    ListOfNameValueSet,
    ListOfPrice,
    ListOfQuantityCoded,
    ListOfReferenceCoded,
    ListOfStructuredNote,
    MaxBackOrderQuantity,
    MonetaryValue,
    NameValuePair,
    OffCatalogFlag,
    ParentItemNumber,
    Quantity,
    RateOfExchangeDetail,
    ReferenceCoded,
    RemitToParty,
    Tax,
    TotalQuantity,
    TotalValue,
)
from xcbl.models.sourcing_result_response import (
    GeneralNote,
    Purpose,
)
from xcbl.models.time_series_response import (
    ContactNumber,
    ListOfDimension,
    ListOfIdentifier,
    ListOfPartyCoded,
    Mdfbusiness,
    NameAddress,
    OrderContact,
    OtherContacts,
    Party,
    PartyId,
    ReceivingContact,
    ShippingContact,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import (
    CorrespondenceLanguage,
    Language,
    ValidityDates,
)


@dataclass(kw_only=True)
class AsnpartialOrderCoded:
    class Meta:
        name = "ASNPartialOrderCoded"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AsnpartialOrderCodedOther:
    class Meta:
        name = "ASNPartialOrderCodedOther"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ActualPaymentStatusCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ActualPaymentStatusCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ActualShipToDateTime:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AdjustmentDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AdjustmentNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AdjustmentPercent:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AdjustmentReasonCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AdjustmentReasonCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CertificateAuthority:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class EncryptedData:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ExpectedShipToDateTime:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FinancialInstitutionQaulifierCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FinancialInstitutionQaulifierCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FixedAsset:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceDueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceLineItemNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class IsCredit:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class LineItemReference:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PartialOrderCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PartialOrderCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentReasonCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentReasonCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentSettlementDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PurchaseOrderDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PurchaseOrderLineItemNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class ReceiptDateTime:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RemittaceAdviceIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RemittanceAdviceStatusCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RemittanceAdviceStatusCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SummaryNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalLineItem:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TotalPaymentDocuments:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TraceTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TraceTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TrackingCallUrl:
    class Meta:
        name = "TrackingCallURL"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TransactionHandlingCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TransactionHandlingCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Url:
    class Meta:
        name = "URL"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class WorkBreakdownStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Asnnumber:
    class Meta:
        name = "ASNNumber"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AsnpartialOrder:
    class Meta:
        name = "ASNPartialOrder"

    asnpartial_order_coded: AsnpartialOrderCoded = field(
        metadata={
            "name": "ASNPartialOrderCoded",
            "type": "Element",
            "required": True,
        }
    )
    asnpartial_order_coded_other: Optional[AsnpartialOrderCodedOther] = field(
        default=None,
        metadata={
            "name": "ASNPartialOrderCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ActualAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ActualPaymentStatus:
    actual_payment_status_coded: Optional[ActualPaymentStatusCoded] = field(
        default=None,
        metadata={
            "name": "ActualPaymentStatusCoded",
            "type": "Element",
        },
    )
    actual_payment_status_coded_other: Optional[
        ActualPaymentStatusCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "ActualPaymentStatusCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AdjustmentAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AirWayBillNumber1:
    class Meta:
        name = "AirWayBillNumber"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AirWaybillNumber2:
    class Meta:
        name = "AirWaybillNumber"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuthorizationAssignedBy:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AuthorizationNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BillOfLadingNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CarrierReferenceNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ContractNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CostAllocationNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Damaged:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DeliveryNoteNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class EncryptedField:
    sequence: Optional[Sequence] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
        },
    )
    encrypted_data: EncryptedData = field(
        metadata={
            "name": "EncryptedData",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ExpectedAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ExportLicenceNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FinancialInstitutionCoded:
    financial_institution_qaulifier_coded: FinancialInstitutionQaulifierCoded = field(
        metadata={
            "name": "FinancialInstitutionQaulifierCoded",
            "type": "Element",
            "required": True,
        }
    )
    financial_institution_qaulifier_coded_other: Optional[
        FinancialInstitutionQaulifierCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "FinancialInstitutionQaulifierCodedOther",
            "type": "Element",
        },
    )
    financial_institution: FinancialInstitution = field(
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ImportLicenceNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceCurrencyTotalValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceType:
    invoice_type_coded: InvoiceTypeCoded = field(
        metadata={
            "name": "InvoiceTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    invoice_type_coded_other: Optional[InvoiceTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "InvoiceTypeCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class InvoicingDetailAmountDue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoicingDetailAmountPaid:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoicingDetailReference:
    reference_coded: ReferenceCoded = field(
        metadata={
            "name": "ReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoicingPeriod:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LetterOfCreditNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfOtherInvoiceDates:
    list_of_date_coded: ListOfDateCoded = field(
        metadata={
            "name": "ListOfDateCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfRateOfExchangeDetail:
    rate_of_exchange_detail: list[RateOfExchangeDetail] = field(
        default_factory=list,
        metadata={
            "name": "RateOfExchangeDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfRemittanceAdviceReference:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfValues:
    name_value_pair: list[NameValuePair] = field(
        default_factory=list,
        metadata={
            "name": "NameValuePair",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Ordered:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherAsnreferences:
    class Meta:
        name = "OtherASNReferences"

    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherInvoiceParties:
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        },
    )
    remit_to_party: Optional[RemitToParty] = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        },
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class OtherInvoiceReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PackingListNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PayeeParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PayerParty:
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
        },
    )
    mdfbusiness: Optional[Mdfbusiness] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        },
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        },
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        },
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        },
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        },
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        },
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        },
    )
    certificate_authority: Optional[CertificateAuthority] = field(
        default=None,
        metadata={
            "name": "CertificateAuthority",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentCurrencyTotalValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ProformaInvoiceNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PurchaseOrderNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemittanceAdviceAttachment:
    attachment: Attachment = field(
        metadata={
            "name": "Attachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemittanceAdviceId:
    class Meta:
        name = "RemittanceAdviceID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemittanceAdvicePurpose:
    purpose: Purpose = field(
        metadata={
            "name": "Purpose",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Returned:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShipmentIdentifier:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ShippedToDate:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SupplierOrderNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SupplierParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxAccountingSubTotalValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxPeriod:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalAmountDue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalAmountPaid:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalSettlementAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalTaxAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TraceReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TrackingNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Unusable:
    quantity: Quantity = field(
        metadata={
            "name": "Quantity",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Adjustment:
    line_item_reference: Optional[LineItemReference] = field(
        default=None,
        metadata={
            "name": "LineItemReference",
            "type": "Element",
        },
    )
    adjustment_reason_coded: AdjustmentReasonCoded = field(
        metadata={
            "name": "AdjustmentReasonCoded",
            "type": "Element",
            "required": True,
        }
    )
    adjustment_reason_coded_other: Optional[AdjustmentReasonCodedOther] = (
        field(
            default=None,
            metadata={
                "name": "AdjustmentReasonCodedOther",
                "type": "Element",
            },
        )
    )
    adjustment_date: Optional[AdjustmentDate] = field(
        default=None,
        metadata={
            "name": "AdjustmentDate",
            "type": "Element",
        },
    )
    expected_amount: Optional[ExpectedAmount] = field(
        default=None,
        metadata={
            "name": "ExpectedAmount",
            "type": "Element",
        },
    )
    adjustment_amount: Optional[AdjustmentAmount] = field(
        default=None,
        metadata={
            "name": "AdjustmentAmount",
            "type": "Element",
        },
    )
    adjustment_percent: Optional[AdjustmentPercent] = field(
        default=None,
        metadata={
            "name": "AdjustmentPercent",
            "type": "Element",
        },
    )
    actual_amount: ActualAmount = field(
        metadata={
            "name": "ActualAmount",
            "type": "Element",
            "required": True,
        }
    )
    adjustment_note: Optional[AdjustmentNote] = field(
        default=None,
        metadata={
            "name": "AdjustmentNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AuthorizationReference:
    authorization_number: AuthorizationNumber = field(
        metadata={
            "name": "AuthorizationNumber",
            "type": "Element",
            "required": True,
        }
    )
    authorization_assigned_by: Optional[AuthorizationAssignedBy] = field(
        default=None,
        metadata={
            "name": "AuthorizationAssignedBy",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class CarrierReference:
    carrier_reference_number: CarrierReferenceNumber = field(
        metadata={
            "name": "CarrierReferenceNumber",
            "type": "Element",
            "required": True,
        }
    )
    transport_route_id: TransportRouteId = field(
        metadata={
            "name": "TransportRouteID",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CostAllocation:
    cost_allocation_number: CostAllocationNumber = field(
        metadata={
            "name": "CostAllocationNumber",
            "type": "Element",
            "required": True,
        }
    )
    work_breakdown_structure: Optional[WorkBreakdownStructure] = field(
        default=None,
        metadata={
            "name": "WorkBreakdownStructure",
            "type": "Element",
        },
    )
    fixed_asset: Optional[FixedAsset] = field(
        default=None,
        metadata={
            "name": "FixedAsset",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ExceptionQuantities:
    ordered: Optional[Ordered] = field(
        default=None,
        metadata={
            "name": "Ordered",
            "type": "Element",
        },
    )
    damaged: Optional[Damaged] = field(
        default=None,
        metadata={
            "name": "Damaged",
            "type": "Element",
        },
    )
    unusable: Optional[Unusable] = field(
        default=None,
        metadata={
            "name": "Unusable",
            "type": "Element",
        },
    )
    returned: Optional[Returned] = field(
        default=None,
        metadata={
            "name": "Returned",
            "type": "Element",
        },
    )
    shipped_to_date: Optional[ShippedToDate] = field(
        default=None,
        metadata={
            "name": "ShippedToDate",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class InvoiceDates:
    invoice_due_date: Optional[InvoiceDueDate] = field(
        default=None,
        metadata={
            "name": "InvoiceDueDate",
            "type": "Element",
        },
    )
    expected_ship_to_date_time: Optional[ExpectedShipToDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedShipToDateTime",
            "type": "Element",
        },
    )
    actual_ship_to_date_time: Optional[ActualShipToDateTime] = field(
        default=None,
        metadata={
            "name": "ActualShipToDateTime",
            "type": "Element",
        },
    )
    receipt_date_time: Optional[ReceiptDateTime] = field(
        default=None,
        metadata={
            "name": "ReceiptDateTime",
            "type": "Element",
        },
    )
    tax_period: Optional[TaxPeriod] = field(
        default=None,
        metadata={
            "name": "TaxPeriod",
            "type": "Element",
        },
    )
    invoicing_period: Optional[InvoicingPeriod] = field(
        default=None,
        metadata={
            "name": "InvoicingPeriod",
            "type": "Element",
        },
    )
    list_of_other_invoice_dates: Optional[ListOfOtherInvoiceDates] = field(
        default=None,
        metadata={
            "name": "ListOfOtherInvoiceDates",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class InvoicePricingDetail:
    list_of_price: ListOfPrice = field(
        metadata={
            "name": "ListOfPrice",
            "type": "Element",
            "required": True,
        }
    )
    tax: list[Tax] = field(
        default_factory=list,
        metadata={
            "name": "Tax",
            "type": "Element",
        },
    )
    item_allowances_or_charges: Optional[ItemAllowancesOrCharges] = field(
        default=None,
        metadata={
            "name": "ItemAllowancesOrCharges",
            "type": "Element",
        },
    )
    total_value: Optional[TotalValue] = field(
        default=None,
        metadata={
            "name": "TotalValue",
            "type": "Element",
        },
    )
    invoice_currency_total_value: InvoiceCurrencyTotalValue = field(
        metadata={
            "name": "InvoiceCurrencyTotalValue",
            "type": "Element",
            "required": True,
        }
    )
    payment_currency_total_value: Optional[PaymentCurrencyTotalValue] = field(
        default=None,
        metadata={
            "name": "PaymentCurrencyTotalValue",
            "type": "Element",
        },
    )
    tax_accounting_sub_total_value: Optional[TaxAccountingSubTotalValue] = (
        field(
            default=None,
            metadata={
                "name": "TaxAccountingSubTotalValue",
                "type": "Element",
            },
        )
    )
    actual_payment_status: Optional[ActualPaymentStatus] = field(
        default=None,
        metadata={
            "name": "ActualPaymentStatus",
            "type": "Element",
        },
    )
    total_tax_amount: Optional[TotalTaxAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfEncryptedField:
    encrypted_field: list[EncryptedField] = field(
        default_factory=list,
        metadata={
            "name": "EncryptedField",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfFinancialInstitutionCoded:
    financial_institution_coded: list[FinancialInstitutionCoded] = field(
        default_factory=list,
        metadata={
            "name": "FinancialInstitutionCoded",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfSummaryItems:
    list_of_values: ListOfValues = field(
        metadata={
            "name": "ListOfValues",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentParty:
    payer_party: PayerParty = field(
        metadata={
            "name": "PayerParty",
            "type": "Element",
            "required": True,
        }
    )
    payee_party: PayeeParty = field(
        metadata={
            "name": "PayeeParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_party: Optional[BuyerParty] = field(
        default=None,
        metadata={
            "name": "BuyerParty",
            "type": "Element",
        },
    )
    supplier_party: Optional[SupplierParty] = field(
        default=None,
        metadata={
            "name": "SupplierParty",
            "type": "Element",
        },
    )
    bill_to_party: Optional[BillToParty] = field(
        default=None,
        metadata={
            "name": "BillToParty",
            "type": "Element",
        },
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PurchaseOrderReference:
    purchase_order_number: PurchaseOrderNumber = field(
        metadata={
            "name": "PurchaseOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    purchase_order_date: Optional[PurchaseOrderDate] = field(
        default=None,
        metadata={
            "name": "PurchaseOrderDate",
            "type": "Element",
        },
    )
    purchase_order_line_item_number: Optional[PurchaseOrderLineItemNumber] = (
        field(
            default=None,
            metadata={
                "name": "PurchaseOrderLineItemNumber",
                "type": "Element",
            },
        )
    )
    partial_order_coded: Optional[PartialOrderCoded] = field(
        default=None,
        metadata={
            "name": "PartialOrderCoded",
            "type": "Element",
        },
    )
    partial_order_coded_other: Optional[PartialOrderCodedOther] = field(
        default=None,
        metadata={
            "name": "PartialOrderCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RelatedInvoiceType:
    invoice_type: InvoiceType = field(
        metadata={
            "name": "InvoiceType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TraceType:
    trace_type_coded: TraceTypeCoded = field(
        metadata={
            "name": "TraceTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    trace_type_coded_other: Optional[TraceTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "TraceTypeCodedOther",
            "type": "Element",
        },
    )
    trace_reference: Optional[TraceReference] = field(
        default=None,
        metadata={
            "name": "TraceReference",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TrackingInformation:
    tracking_number: TrackingNumber = field(
        metadata={
            "name": "TrackingNumber",
            "type": "Element",
            "required": True,
        }
    )
    tracking_call_url: Optional[TrackingCallUrl] = field(
        default=None,
        metadata={
            "name": "TrackingCallURL",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class EncryptedInfo:
    certificate_authority: Optional[CertificateAuthority] = field(
        default=None,
        metadata={
            "name": "CertificateAuthority",
            "type": "Element",
        },
    )
    list_of_encrypted_field: ListOfEncryptedField = field(
        metadata={
            "name": "ListOfEncryptedField",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LineItemDates:
    invoice_dates: InvoiceDates = field(
        metadata={
            "name": "InvoiceDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfAdjustments:
    adjustment: list[Adjustment] = field(
        default_factory=list,
        metadata={
            "name": "Adjustment",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfCarrierReference:
    carrier_reference: list[CarrierReference] = field(
        default_factory=list,
        metadata={
            "name": "CarrierReference",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class RelatedInvoiceRef:
    related_invoice_type: RelatedInvoiceType = field(
        metadata={
            "name": "RelatedInvoiceType",
            "type": "Element",
            "required": True,
        }
    )
    invoice_number: InvoiceNumber = field(
        metadata={
            "name": "InvoiceNumber",
            "type": "Element",
            "required": True,
        }
    )
    invoice_line_item_number: Optional[InvoiceLineItemNumber] = field(
        default=None,
        metadata={
            "name": "InvoiceLineItemNumber",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RemittanceAdviceHeader:
    remittance_advice_purpose: RemittanceAdvicePurpose = field(
        metadata={
            "name": "RemittanceAdvicePurpose",
            "type": "Element",
            "required": True,
        }
    )
    remittace_advice_issue_date: RemittaceAdviceIssueDate = field(
        metadata={
            "name": "RemittaceAdviceIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    remittance_advice_id: RemittanceAdviceId = field(
        metadata={
            "name": "RemittanceAdviceID",
            "type": "Element",
            "required": True,
        }
    )
    remittance_advice_status_coded: Optional[RemittanceAdviceStatusCoded] = (
        field(
            default=None,
            metadata={
                "name": "RemittanceAdviceStatusCoded",
                "type": "Element",
            },
        )
    )
    remittance_advice_status_coded_other: Optional[
        RemittanceAdviceStatusCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceStatusCodedOther",
            "type": "Element",
        },
    )
    payment_settlement_date: Optional[PaymentSettlementDate] = field(
        default=None,
        metadata={
            "name": "PaymentSettlementDate",
            "type": "Element",
        },
    )
    total_amount_due: Optional[TotalAmountDue] = field(
        default=None,
        metadata={
            "name": "TotalAmountDue",
            "type": "Element",
        },
    )
    total_amount_paid: TotalAmountPaid = field(
        metadata={
            "name": "TotalAmountPaid",
            "type": "Element",
            "required": True,
        }
    )
    payment_currency: PaymentCurrency = field(
        metadata={
            "name": "PaymentCurrency",
            "type": "Element",
            "required": True,
        }
    )
    list_of_rate_of_exchange_detail: Optional[ListOfRateOfExchangeDetail] = (
        field(
            default=None,
            metadata={
                "name": "ListOfRateOfExchangeDetail",
                "type": "Element",
            },
        )
    )
    list_of_price: Optional[ListOfPrice] = field(
        default=None,
        metadata={
            "name": "ListOfPrice",
            "type": "Element",
        },
    )
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )
    is_credit: Optional[IsCredit] = field(
        default=None,
        metadata={
            "name": "IsCredit",
            "type": "Element",
        },
    )
    payment_instructions: Optional[PaymentInstructions] = field(
        default=None,
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
        },
    )
    list_of_financial_institution_coded: Optional[
        ListOfFinancialInstitutionCoded
    ] = field(
        default=None,
        metadata={
            "name": "ListOfFinancialInstitutionCoded",
            "type": "Element",
        },
    )
    payment_party: PaymentParty = field(
        metadata={
            "name": "PaymentParty",
            "type": "Element",
            "required": True,
        }
    )
    payment_reason_coded: Optional[PaymentReasonCoded] = field(
        default=None,
        metadata={
            "name": "PaymentReasonCoded",
            "type": "Element",
        },
    )
    payment_reason_coded_other: Optional[PaymentReasonCodedOther] = field(
        default=None,
        metadata={
            "name": "PaymentReasonCodedOther",
            "type": "Element",
        },
    )
    transaction_handling_coded: Optional[TransactionHandlingCoded] = field(
        default=None,
        metadata={
            "name": "TransactionHandlingCoded",
            "type": "Element",
        },
    )
    transaction_handling_coded_other: Optional[
        TransactionHandlingCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "TransactionHandlingCodedOther",
            "type": "Element",
        },
    )
    trace_type: Optional[TraceType] = field(
        default=None,
        metadata={
            "name": "TraceType",
            "type": "Element",
        },
    )
    list_of_remittance_advice_reference: Optional[
        ListOfRemittanceAdviceReference
    ] = field(
        default=None,
        metadata={
            "name": "ListOfRemittanceAdviceReference",
            "type": "Element",
        },
    )
    remittance_advice_attachment: Optional[RemittanceAdviceAttachment] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceAttachment",
            "type": "Element",
        },
    )
    general_note: Optional[GeneralNote] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Asnreferences:
    class Meta:
        name = "ASNReferences"

    shipment_identifier: Optional[ShipmentIdentifier] = field(
        default=None,
        metadata={
            "name": "ShipmentIdentifier",
            "type": "Element",
        },
    )
    packing_list_number: Optional[PackingListNumber] = field(
        default=None,
        metadata={
            "name": "PackingListNumber",
            "type": "Element",
        },
    )
    contract_number: Optional[ContractNumber] = field(
        default=None,
        metadata={
            "name": "ContractNumber",
            "type": "Element",
        },
    )
    bill_of_lading_number: Optional[BillOfLadingNumber] = field(
        default=None,
        metadata={
            "name": "BillOfLadingNumber",
            "type": "Element",
        },
    )
    air_waybill_number: Optional[AirWaybillNumber2] = field(
        default=None,
        metadata={
            "name": "AirWaybillNumber",
            "type": "Element",
        },
    )
    import_licence_number: Optional[ImportLicenceNumber] = field(
        default=None,
        metadata={
            "name": "ImportLicenceNumber",
            "type": "Element",
        },
    )
    export_licence_number: Optional[ExportLicenceNumber] = field(
        default=None,
        metadata={
            "name": "ExportLicenceNumber",
            "type": "Element",
        },
    )
    letter_of_credit_number: Optional[LetterOfCreditNumber] = field(
        default=None,
        metadata={
            "name": "LetterOfCreditNumber",
            "type": "Element",
        },
    )
    url: Optional[Url] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
        },
    )
    tracking_information: Optional[TrackingInformation] = field(
        default=None,
        metadata={
            "name": "TrackingInformation",
            "type": "Element",
        },
    )
    list_of_carrier_reference: Optional[ListOfCarrierReference] = field(
        default=None,
        metadata={
            "name": "ListOfCarrierReference",
            "type": "Element",
        },
    )
    other_asnreferences: Optional[OtherAsnreferences] = field(
        default=None,
        metadata={
            "name": "OtherASNReferences",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfRelatedInvoiceRef:
    related_invoice_ref: list[RelatedInvoiceRef] = field(
        default_factory=list,
        metadata={
            "name": "RelatedInvoiceRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PaymentRequestSummary:
    total_payment_documents: Optional[TotalPaymentDocuments] = field(
        default=None,
        metadata={
            "name": "TotalPaymentDocuments",
            "type": "Element",
        },
    )
    total_line_item: Optional[TotalLineItem] = field(
        default=None,
        metadata={
            "name": "TotalLineItem",
            "type": "Element",
        },
    )
    total_settlement_amount: Optional[TotalSettlementAmount] = field(
        default=None,
        metadata={
            "name": "TotalSettlementAmount",
            "type": "Element",
        },
    )
    encrypted_info: Optional[EncryptedInfo] = field(
        default=None,
        metadata={
            "name": "EncryptedInfo",
            "type": "Element",
        },
    )
    list_of_summary_items: Optional[ListOfSummaryItems] = field(
        default=None,
        metadata={
            "name": "ListOfSummaryItems",
            "type": "Element",
        },
    )
    summary_note: Optional[SummaryNote] = field(
        default=None,
        metadata={
            "name": "SummaryNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class AsnorderNumber:
    class Meta:
        name = "ASNOrderNumber"

    buyer_order_number: BuyerOrderNumber = field(
        metadata={
            "name": "BuyerOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_number: Optional[SellerOrderNumber] = field(
        default=None,
        metadata={
            "name": "SellerOrderNumber",
            "type": "Element",
        },
    )
    list_of_message_id: Optional[ListOfMessageId] = field(
        default=None,
        metadata={
            "name": "ListOfMessageID",
            "type": "Element",
        },
    )
    asnpartial_order: Optional[AsnpartialOrder] = field(
        default=None,
        metadata={
            "name": "ASNPartialOrder",
            "type": "Element",
        },
    )
    asnreferences: Optional[Asnreferences] = field(
        default=None,
        metadata={
            "name": "ASNReferences",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RemittanceAdviceSummary:
    payment_request_summary: PaymentRequestSummary = field(
        metadata={
            "name": "PaymentRequestSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceReferences:
    purchase_order_reference: Optional[PurchaseOrderReference] = field(
        default=None,
        metadata={
            "name": "PurchaseOrderReference",
            "type": "Element",
        },
    )
    contract_reference: Optional[ContractReference] = field(
        default=None,
        metadata={
            "name": "ContractReference",
            "type": "Element",
        },
    )
    account_number: Optional[AccountNumber] = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Element",
        },
    )
    proforma_invoice_number: Optional[ProformaInvoiceNumber] = field(
        default=None,
        metadata={
            "name": "ProformaInvoiceNumber",
            "type": "Element",
        },
    )
    asnnumber: Optional[Asnnumber] = field(
        default=None,
        metadata={
            "name": "ASNNumber",
            "type": "Element",
        },
    )
    asnorder_number: Optional[AsnorderNumber] = field(
        default=None,
        metadata={
            "name": "ASNOrderNumber",
            "type": "Element",
        },
    )
    supplier_order_number: Optional[SupplierOrderNumber] = field(
        default=None,
        metadata={
            "name": "SupplierOrderNumber",
            "type": "Element",
        },
    )
    price_list_number: Optional[PriceListNumber] = field(
        default=None,
        metadata={
            "name": "PriceListNumber",
            "type": "Element",
        },
    )
    price_list_version_number: Optional[PriceListVersionNumber] = field(
        default=None,
        metadata={
            "name": "PriceListVersionNumber",
            "type": "Element",
        },
    )
    buyers_catalog_number: Optional[BuyersCatalogNumber] = field(
        default=None,
        metadata={
            "name": "BuyersCatalogNumber",
            "type": "Element",
        },
    )
    bill_of_lading_number: Optional[BillOfLadingNumber] = field(
        default=None,
        metadata={
            "name": "BillOfLadingNumber",
            "type": "Element",
        },
    )
    air_way_bill_number: Optional[AirWayBillNumber1] = field(
        default=None,
        metadata={
            "name": "AirWayBillNumber",
            "type": "Element",
        },
    )
    letter_of_credit_number: Optional[LetterOfCreditNumber] = field(
        default=None,
        metadata={
            "name": "LetterOfCreditNumber",
            "type": "Element",
        },
    )
    authorization_reference: Optional[AuthorizationReference] = field(
        default=None,
        metadata={
            "name": "AuthorizationReference",
            "type": "Element",
        },
    )
    delivery_note_number: Optional[DeliveryNoteNumber] = field(
        default=None,
        metadata={
            "name": "DeliveryNoteNumber",
            "type": "Element",
        },
    )
    cost_allocation: Optional[CostAllocation] = field(
        default=None,
        metadata={
            "name": "CostAllocation",
            "type": "Element",
        },
    )
    list_of_related_invoice_ref: Optional[ListOfRelatedInvoiceRef] = field(
        default=None,
        metadata={
            "name": "ListOfRelatedInvoiceRef",
            "type": "Element",
        },
    )
    other_invoice_references: Optional[OtherInvoiceReferences] = field(
        default=None,
        metadata={
            "name": "OtherInvoiceReferences",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class LineItemReferences:
    invoice_references: InvoiceReferences = field(
        metadata={
            "name": "InvoiceReferences",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceBaseItemDetail:
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
        },
    )
    parent_item_number: Optional[ParentItemNumber] = field(
        default=None,
        metadata={
            "name": "ParentItemNumber",
            "type": "Element",
        },
    )
    item_identifiers: Optional[ItemIdentifiers] = field(
        default=None,
        metadata={
            "name": "ItemIdentifiers",
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
    total_quantity: Optional[TotalQuantity] = field(
        default=None,
        metadata={
            "name": "TotalQuantity",
            "type": "Element",
        },
    )
    max_back_order_quantity: Optional[MaxBackOrderQuantity] = field(
        default=None,
        metadata={
            "name": "MaxBackOrderQuantity",
            "type": "Element",
        },
    )
    list_of_quantity_coded: Optional[ListOfQuantityCoded] = field(
        default=None,
        metadata={
            "name": "ListOfQuantityCoded",
            "type": "Element",
        },
    )
    off_catalog_flag: Optional[OffCatalogFlag] = field(
        default=None,
        metadata={
            "name": "OffCatalogFlag",
            "type": "Element",
        },
    )
    catalog_reference: Optional[CatalogReference] = field(
        default=None,
        metadata={
            "name": "CatalogReference",
            "type": "Element",
        },
    )
    item_contract_references: Optional[ItemContractReferences] = field(
        default=None,
        metadata={
            "name": "ItemContractReferences",
            "type": "Element",
        },
    )
    list_of_item_references: Optional[ListOfItemReferences] = field(
        default=None,
        metadata={
            "name": "ListOfItemReferences",
            "type": "Element",
        },
    )
    country_of_origin: Optional[CountryOfOrigin] = field(
        default=None,
        metadata={
            "name": "CountryOfOrigin",
            "type": "Element",
        },
    )
    country_of_destination: Optional[CountryOfDestination] = field(
        default=None,
        metadata={
            "name": "CountryOfDestination",
            "type": "Element",
        },
    )
    final_recipient: Optional[FinalRecipient] = field(
        default=None,
        metadata={
            "name": "FinalRecipient",
            "type": "Element",
        },
    )
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        },
    )
    conditions_of_sale: Optional[ConditionsOfSale] = field(
        default=None,
        metadata={
            "name": "ConditionsOfSale",
            "type": "Element",
        },
    )
    hazardous_materials: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "HazardousMaterials",
            "type": "Element",
        },
    )
    line_item_references: Optional[LineItemReferences] = field(
        default=None,
        metadata={
            "name": "LineItemReferences",
            "type": "Element",
        },
    )
    exception_quantities: Optional[ExceptionQuantities] = field(
        default=None,
        metadata={
            "name": "ExceptionQuantities",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class InvoiceItemDetail:
    invoice_base_item_detail: InvoiceBaseItemDetail = field(
        metadata={
            "name": "InvoiceBaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    invoice_pricing_detail: InvoicePricingDetail = field(
        metadata={
            "name": "InvoicePricingDetail",
            "type": "Element",
            "required": True,
        }
    )
    line_item_dates: Optional[LineItemDates] = field(
        default=None,
        metadata={
            "name": "LineItemDates",
            "type": "Element",
        },
    )
    other_invoice_parties: Optional[OtherInvoiceParties] = field(
        default=None,
        metadata={
            "name": "OtherInvoiceParties",
            "type": "Element",
        },
    )
    delivery_detail: Optional[DeliveryDetail] = field(
        default=None,
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
        },
    )
    line_item_note: Optional[LineItemNote] = field(
        default=None,
        metadata={
            "name": "LineItemNote",
            "type": "Element",
        },
    )
    list_of_structured_note: Optional[ListOfStructuredNote] = field(
        default=None,
        metadata={
            "name": "ListOfStructuredNote",
            "type": "Element",
        },
    )
    list_of_name_value_set: Optional[ListOfNameValueSet] = field(
        default=None,
        metadata={
            "name": "ListOfNameValueSet",
            "type": "Element",
        },
    )
    line_item_attachments: Optional[LineItemAttachments] = field(
        default=None,
        metadata={
            "name": "LineItemAttachments",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class InvoicingItemDetail:
    invoice_item_detail: InvoiceItemDetail = field(
        metadata={
            "name": "InvoiceItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoicingDetail:
    invoicing_detail_reference: InvoicingDetailReference = field(
        metadata={
            "name": "InvoicingDetailReference",
            "type": "Element",
            "required": True,
        }
    )
    invoicing_detail_amount_due: Optional[InvoicingDetailAmountDue] = field(
        default=None,
        metadata={
            "name": "InvoicingDetailAmountDue",
            "type": "Element",
        },
    )
    invoicing_detail_amount_paid: Optional[InvoicingDetailAmountPaid] = field(
        default=None,
        metadata={
            "name": "InvoicingDetailAmountPaid",
            "type": "Element",
        },
    )
    invoicing_item_detail: Optional[InvoicingItemDetail] = field(
        default=None,
        metadata={
            "name": "InvoicingItemDetail",
            "type": "Element",
        },
    )
    list_of_adjustments: Optional[ListOfAdjustments] = field(
        default=None,
        metadata={
            "name": "ListOfAdjustments",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfInvoicingDetail:
    invoicing_detail: list[InvoicingDetail] = field(
        default_factory=list,
        metadata={
            "name": "InvoicingDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class Subsidiary:
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
        },
    )
    mdfbusiness: Optional[Mdfbusiness] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        },
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        },
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        },
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        },
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        },
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        },
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        },
    )
    list_of_invoicing_detail: ListOfInvoicingDetail = field(
        metadata={
            "name": "ListOfInvoicingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfSubsidiary:
    subsidiary: list[Subsidiary] = field(
        default_factory=list,
        metadata={
            "name": "Subsidiary",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class RemittanceAdviceDetail:
    list_of_subsidiary: Optional[ListOfSubsidiary] = field(
        default=None,
        metadata={
            "name": "ListOfSubsidiary",
            "type": "Element",
        },
    )
    list_of_invoicing_detail: Optional[ListOfInvoicingDetail] = field(
        default=None,
        metadata={
            "name": "ListOfInvoicingDetail",
            "type": "Element",
        },
    )
    list_of_adjustments: Optional[ListOfAdjustments] = field(
        default=None,
        metadata={
            "name": "ListOfAdjustments",
            "type": "Element",
        },
    )
    remittance_advice_id: Optional[RemittanceAdviceId] = field(
        default=None,
        metadata={
            "name": "RemittanceAdviceID",
            "type": "Element",
        },
    )
    contact_number: Optional[ContactNumber] = field(
        default=None,
        metadata={
            "name": "ContactNumber",
            "type": "Element",
        },
    )
    general_note: Optional[GeneralNote] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfRemittanceAdviceDetail:
    remittance_advice_detail: list[RemittanceAdviceDetail] = field(
        default_factory=list,
        metadata={
            "name": "RemittanceAdviceDetail",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class RemittanceAdvice:
    remittance_advice_header: RemittanceAdviceHeader = field(
        metadata={
            "name": "RemittanceAdviceHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_remittance_advice_detail: ListOfRemittanceAdviceDetail = field(
        metadata={
            "name": "ListOfRemittanceAdviceDetail",
            "type": "Element",
            "required": True,
        }
    )
    remittance_advice_summary: RemittanceAdviceSummary = field(
        metadata={
            "name": "RemittanceAdviceSummary",
            "type": "Element",
            "required": True,
        }
    )
