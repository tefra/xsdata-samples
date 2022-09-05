from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    Country,
    Currency,
    DeliveryDetail,
    Language,
    ListOfAttachment,
    ListOfDateCoded,
    ListOfDimension,
    ListOfPrice,
    ListOfReferenceCoded,
    Party,
    Quantity,
    Reference,
    TermsOfDelivery,
    ValidityDates,
)
from xcbl.models.goods_receipt import ListOfTransportRouting
from xcbl.models.order_request import (
    AllowanceOrChargeDescription,
    BillToParty,
    BuyerParty,
    BuyerTaxInformation,
    CardInfo,
    CatalogReference,
    ConditionsOfSale,
    CountryOfDestination,
    CountryOfOrigin,
    Fiaccount,
    FinalRecipient,
    HazardousMaterials,
    ItemAllowancesOrCharges,
    ItemContractReferences,
    ItemIdentifiers,
    LineItemAttachments,
    LineItemNum,
    LineItemType,
    ListOfAllowOrCharge,
    ListOfItemReferences,
    ListOfMessageId,
    ListOfNameValueSet,
    ListOfPackageDetail,
    ListOfPartyCoded,
    ListOfQuantityCoded,
    ListOfStructuredNote,
    MaxBackOrderQuantity,
    MonetaryValue,
    ParentItemNumber,
    PartyTaxInformation,
    PaymentInstructions,
    RemitToParty,
    SellerParty,
    SellerTaxInformation,
    ShipFromParty,
    ShipToParty,
    Tax,
    TaxAccountingCurrency,
    TaxReference,
    TotalQuantity,
    TotalValue,
)
from xcbl.models.payment_request_acknowledgment import ListOfRateOfExchangeDetail
from xcbl.models.planning_schedule import MaterialIssuerParty
from xcbl.models.request_for_quotation import (
    AccountNumber,
    BuyersCatalogNumber,
    ContractReference,
    PriceListNumber,
    PriceListVersionNumber,
    SoldToParty,
    WarehouseParty,
)


@dataclass(kw_only=True)
class AsnpartialOrder:
    class Meta:
        name = "ASNPartialOrder"

    asnpartial_order_coded: str = field(
        metadata={
            "name": "ASNPartialOrderCoded",
            "type": "Element",
            "required": True,
        }
    )
    asnpartial_order_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ASNPartialOrderCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ActualPaymentStatus:
    actual_payment_status_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActualPaymentStatusCoded",
            "type": "Element",
        }
    )
    actual_payment_status_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActualPaymentStatusCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AllowOrChargeTreatment:
    allow_or_charge_treatment_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeTreatmentCoded",
            "type": "Element",
        }
    )
    allow_or_charge_treatment_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeTreatmentCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InvoiceMedium:
    invoice_medium_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceMediumCoded",
            "type": "Element",
        }
    )
    invoice_medium_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceMediumCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InvoicePaymentStatus:
    invoice_payment_status_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoicePaymentStatusCoded",
            "type": "Element",
        }
    )
    invoice_payment_status_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoicePaymentStatusCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InvoicePurpose:
    invoice_purpose_coded: str = field(
        metadata={
            "name": "InvoicePurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    invoice_purpose_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoicePurposeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InvoiceType:
    invoice_type_coded: str = field(
        metadata={
            "name": "InvoiceTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    invoice_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceTypeCodedOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PaymentMean:
    payment_mean_coded: str = field(
        metadata={
            "name": "PaymentMeanCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_coded_mean_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentCodedMeanOther",
            "type": "Element",
        }
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
class BuyerTax:
    tax: Tax = field(
        metadata={
            "name": "Tax",
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
class ChargeTotal:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
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
class ExportLicenceNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ForeignCurrencyPayment:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FromFitransfer:
    class Meta:
        name = "FromFITransfer"

    fiaccount: Fiaccount = field(
        metadata={
            "name": "FIAccount",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class GrossValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
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
class InvoiceAllowancesOrCharges:
    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceCurrencyAmt:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
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
class InvoiceHeaderAttachments:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
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
class InvoicePaymentInstructions:
    payment_instructions: PaymentInstructions = field(
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceTaxReference:
    tax_reference: TaxReference = field(
        metadata={
            "name": "TaxReference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class InvoiceTermsOfDelivery:
    terms_of_delivery: TermsOfDelivery = field(
        metadata={
            "name": "TermsOfDelivery",
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
class ManufacturingParty:
    party: Party = field(
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class NetValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
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
        }
    )
    remit_to_party: Optional[RemitToParty] = field(
        default=None,
        metadata={
            "name": "RemitToParty",
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
class PaymentRef:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PrepaidAmount:
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
class RelatedInvoiceType:
    invoice_type: InvoiceType = field(
        metadata={
            "name": "InvoiceType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemitToTax:
    tax: Tax = field(
        metadata={
            "name": "Tax",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RemitToTaxInformation:
    party_tax_information: PartyTaxInformation = field(
        metadata={
            "name": "PartyTaxInformation",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequirementReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
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
class SummaryAllowOrCharge:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
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
class TaxSummary:
    tax: Tax = field(
        metadata={
            "name": "Tax",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxValue:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TaxValueInTaxAccountingCurrency:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ToFitransfer:
    class Meta:
        name = "ToFITransfer"

    fiaccount: Fiaccount = field(
        metadata={
            "name": "FIAccount",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalAmountMinusDiscount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalAmountPayable:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TotalDiscount:
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
        }
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
    transport_route_id: str = field(
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
    work_breakdown_structure: Optional[str] = field(
        default=None,
        metadata={
            "name": "WorkBreakdownStructure",
            "type": "Element",
        }
    )
    fixed_asset: Optional[str] = field(
        default=None,
        metadata={
            "name": "FixedAsset",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ExceptionQuantities:
    ordered: Optional[Ordered] = field(
        default=None,
        metadata={
            "name": "Ordered",
            "type": "Element",
        }
    )
    damaged: Optional[Damaged] = field(
        default=None,
        metadata={
            "name": "Damaged",
            "type": "Element",
        }
    )
    unusable: Optional[Unusable] = field(
        default=None,
        metadata={
            "name": "Unusable",
            "type": "Element",
        }
    )
    returned: Optional[Returned] = field(
        default=None,
        metadata={
            "name": "Returned",
            "type": "Element",
        }
    )
    shipped_to_date: Optional[ShippedToDate] = field(
        default=None,
        metadata={
            "name": "ShippedToDate",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Fitransfer:
    class Meta:
        name = "FITransfer"

    from_fitransfer: Optional[FromFitransfer] = field(
        default=None,
        metadata={
            "name": "FromFITransfer",
            "type": "Element",
        }
    )
    to_fitransfer: ToFitransfer = field(
        metadata={
            "name": "ToFITransfer",
            "type": "Element",
            "required": True,
        }
    )
    payment_record_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRecordOther",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InvoiceDates:
    invoice_due_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceDueDate",
            "type": "Element",
        }
    )
    expected_ship_to_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExpectedShipToDateTime",
            "type": "Element",
        }
    )
    actual_ship_to_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ActualShipToDateTime",
            "type": "Element",
        }
    )
    receipt_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReceiptDateTime",
            "type": "Element",
        }
    )
    tax_period: Optional[TaxPeriod] = field(
        default=None,
        metadata={
            "name": "TaxPeriod",
            "type": "Element",
        }
    )
    invoicing_period: Optional[InvoicingPeriod] = field(
        default=None,
        metadata={
            "name": "InvoicingPeriod",
            "type": "Element",
        }
    )
    list_of_other_invoice_dates: Optional[ListOfOtherInvoiceDates] = field(
        default=None,
        metadata={
            "name": "ListOfOtherInvoiceDates",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InvoiceParty:
    buyer_party: BuyerParty = field(
        metadata={
            "name": "BuyerParty",
            "type": "Element",
            "required": True,
        }
    )
    buyer_tax_information: Optional[BuyerTaxInformation] = field(
        default=None,
        metadata={
            "name": "BuyerTaxInformation",
            "type": "Element",
        }
    )
    buyer_tax: Optional[BuyerTax] = field(
        default=None,
        metadata={
            "name": "BuyerTax",
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
    remit_to_tax_information: Optional[RemitToTaxInformation] = field(
        default=None,
        metadata={
            "name": "RemitToTaxInformation",
            "type": "Element",
        }
    )
    remit_to_tax: Optional[RemitToTax] = field(
        default=None,
        metadata={
            "name": "RemitToTax",
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
    warehouse_party: Optional[WarehouseParty] = field(
        default=None,
        metadata={
            "name": "WarehouseParty",
            "type": "Element",
        }
    )
    sold_to_party: Optional[SoldToParty] = field(
        default=None,
        metadata={
            "name": "SoldToParty",
            "type": "Element",
        }
    )
    manufacturing_party: Optional[ManufacturingParty] = field(
        default=None,
        metadata={
            "name": "ManufacturingParty",
            "type": "Element",
        }
    )
    material_issuer_party: Optional[MaterialIssuerParty] = field(
        default=None,
        metadata={
            "name": "MaterialIssuerParty",
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
class InvoicePricingDetail:
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
        }
    )
    tax_accounting_sub_total_value: Optional[TaxAccountingSubTotalValue] = field(
        default=None,
        metadata={
            "name": "TaxAccountingSubTotalValue",
            "type": "Element",
        }
    )
    actual_payment_status: Optional[ActualPaymentStatus] = field(
        default=None,
        metadata={
            "name": "ActualPaymentStatus",
            "type": "Element",
        }
    )
    total_tax_amount: Optional[TotalTaxAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InvoiceTotals:
    net_value: NetValue = field(
        metadata={
            "name": "NetValue",
            "type": "Element",
            "required": True,
        }
    )
    gross_value: GrossValue = field(
        metadata={
            "name": "GrossValue",
            "type": "Element",
            "required": True,
        }
    )
    tax_value: Optional[TaxValue] = field(
        default=None,
        metadata={
            "name": "TaxValue",
            "type": "Element",
        }
    )
    tax_value_in_tax_accounting_currency: Optional[TaxValueInTaxAccountingCurrency] = field(
        default=None,
        metadata={
            "name": "TaxValueInTaxAccountingCurrency",
            "type": "Element",
        }
    )
    charge_total: Optional[ChargeTotal] = field(
        default=None,
        metadata={
            "name": "ChargeTotal",
            "type": "Element",
        }
    )
    total_amount_payable: Optional[TotalAmountPayable] = field(
        default=None,
        metadata={
            "name": "TotalAmountPayable",
            "type": "Element",
        }
    )
    prepaid_amount: Optional[PrepaidAmount] = field(
        default=None,
        metadata={
            "name": "PrepaidAmount",
            "type": "Element",
        }
    )
    total_discount: Optional[TotalDiscount] = field(
        default=None,
        metadata={
            "name": "TotalDiscount",
            "type": "Element",
        }
    )
    total_tax_amount: Optional[TotalTaxAmount] = field(
        default=None,
        metadata={
            "name": "TotalTaxAmount",
            "type": "Element",
        }
    )
    total_amount_minus_discount: Optional[TotalAmountMinusDiscount] = field(
        default=None,
        metadata={
            "name": "TotalAmountMinusDiscount",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfTaxSummary:
    tax_summary: List[TaxSummary] = field(
        default_factory=list,
        metadata={
            "name": "TaxSummary",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class PaymentAmount:
    invoice_currency_amt: InvoiceCurrencyAmt = field(
        metadata={
            "name": "InvoiceCurrencyAmt",
            "type": "Element",
            "required": True,
        }
    )
    foreign_currency_payment: ForeignCurrencyPayment = field(
        metadata={
            "name": "ForeignCurrencyPayment",
            "type": "Element",
            "required": True,
        }
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
    purchase_order_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchaseOrderDate",
            "type": "Element",
        }
    )
    purchase_order_line_item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PurchaseOrderLineItemNumber",
            "type": "Element",
        }
    )
    partial_order_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialOrderCoded",
            "type": "Element",
        }
    )
    partial_order_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartialOrderCodedOther",
            "type": "Element",
        }
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
    invoice_line_item_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceLineItemNumber",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class SpecificRequirement:
    requirement_type_coded: str = field(
        metadata={
            "name": "RequirementTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    requirement_type_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequirementTypeCodedOther",
            "type": "Element",
        }
    )
    requirement_reference: Optional[RequirementReference] = field(
        default=None,
        metadata={
            "name": "RequirementReference",
            "type": "Element",
        }
    )
    requirement_details: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequirementDetails",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class TotalAllowOrCharge:
    allow_or_charge_indicator_coded: str = field(
        metadata={
            "name": "AllowOrChargeIndicatorCoded",
            "type": "Element",
            "required": True,
        }
    )
    allow_or_charge_indicator_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeIndicatorCodedOther",
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
    summary_allow_or_charge: SummaryAllowOrCharge = field(
        metadata={
            "name": "SummaryAllowOrCharge",
            "type": "Element",
            "required": True,
        }
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
    tracking_call_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrackingCallURL",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class AllowOrChargeSummary:
    total_allow_or_charge: List[TotalAllowOrCharge] = field(
        default_factory=list,
        metadata={
            "name": "TotalAllowOrCharge",
            "type": "Element",
            "min_occurs": 1,
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
class ListOfCarrierReference:
    carrier_reference: List[CarrierReference] = field(
        default_factory=list,
        metadata={
            "name": "CarrierReference",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfRelatedInvoiceRef:
    related_invoice_ref: List[RelatedInvoiceRef] = field(
        default_factory=list,
        metadata={
            "name": "RelatedInvoiceRef",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfSpecificRequirement:
    specific_requirement: List[SpecificRequirement] = field(
        default_factory=list,
        metadata={
            "name": "SpecificRequirement",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class PaymentRecord:
    payment_ref: Optional[PaymentRef] = field(
        default=None,
        metadata={
            "name": "PaymentRef",
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
    fitransfer: Optional[Fitransfer] = field(
        default=None,
        metadata={
            "name": "FITransfer",
            "type": "Element",
        }
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
        }
    )
    packing_list_number: Optional[PackingListNumber] = field(
        default=None,
        metadata={
            "name": "PackingListNumber",
            "type": "Element",
        }
    )
    contract_number: Optional[ContractNumber] = field(
        default=None,
        metadata={
            "name": "ContractNumber",
            "type": "Element",
        }
    )
    bill_of_lading_number: Optional[BillOfLadingNumber] = field(
        default=None,
        metadata={
            "name": "BillOfLadingNumber",
            "type": "Element",
        }
    )
    air_waybill_number: Optional[AirWaybillNumber2] = field(
        default=None,
        metadata={
            "name": "AirWaybillNumber",
            "type": "Element",
        }
    )
    import_licence_number: Optional[ImportLicenceNumber] = field(
        default=None,
        metadata={
            "name": "ImportLicenceNumber",
            "type": "Element",
        }
    )
    export_licence_number: Optional[ExportLicenceNumber] = field(
        default=None,
        metadata={
            "name": "ExportLicenceNumber",
            "type": "Element",
        }
    )
    letter_of_credit_number: Optional[LetterOfCreditNumber] = field(
        default=None,
        metadata={
            "name": "LetterOfCreditNumber",
            "type": "Element",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Element",
        }
    )
    tracking_information: Optional[TrackingInformation] = field(
        default=None,
        metadata={
            "name": "TrackingInformation",
            "type": "Element",
        }
    )
    list_of_carrier_reference: Optional[ListOfCarrierReference] = field(
        default=None,
        metadata={
            "name": "ListOfCarrierReference",
            "type": "Element",
        }
    )
    other_asnreferences: Optional[OtherAsnreferences] = field(
        default=None,
        metadata={
            "name": "OtherASNReferences",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ActualPayment:
    payment_amount: PaymentAmount = field(
        metadata={
            "name": "PaymentAmount",
            "type": "Element",
            "required": True,
        }
    )
    payment_date: str = field(
        metadata={
            "name": "PaymentDate",
            "type": "Element",
            "required": True,
        }
    )
    payment_mean: PaymentMean = field(
        metadata={
            "name": "PaymentMean",
            "type": "Element",
            "required": True,
        }
    )
    payment_record: Optional[PaymentRecord] = field(
        default=None,
        metadata={
            "name": "PaymentRecord",
            "type": "Element",
        }
    )
    other_payment_info: List[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherPaymentInfo",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class CountryRequirement:
    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )
    list_of_specific_requirement: ListOfSpecificRequirement = field(
        metadata={
            "name": "ListOfSpecificRequirement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AsnorderNumber:
    class Meta:
        name = "ASNOrderNumber"

    buyer_order_number: str = field(
        metadata={
            "name": "BuyerOrderNumber",
            "type": "Element",
            "required": True,
        }
    )
    seller_order_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SellerOrderNumber",
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
    asnpartial_order: Optional[AsnpartialOrder] = field(
        default=None,
        metadata={
            "name": "ASNPartialOrder",
            "type": "Element",
        }
    )
    asnreferences: Optional[Asnreferences] = field(
        default=None,
        metadata={
            "name": "ASNReferences",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class ListOfActualPayment:
    actual_payment: List[ActualPayment] = field(
        default_factory=list,
        metadata={
            "name": "ActualPayment",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class ListOfCountryRequirement:
    country_requirement: List[CountryRequirement] = field(
        default_factory=list,
        metadata={
            "name": "CountryRequirement",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class InvoiceReferences:
    purchase_order_reference: Optional[PurchaseOrderReference] = field(
        default=None,
        metadata={
            "name": "PurchaseOrderReference",
            "type": "Element",
        }
    )
    contract_reference: Optional[ContractReference] = field(
        default=None,
        metadata={
            "name": "ContractReference",
            "type": "Element",
        }
    )
    account_number: Optional[AccountNumber] = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Element",
        }
    )
    proforma_invoice_number: Optional[ProformaInvoiceNumber] = field(
        default=None,
        metadata={
            "name": "ProformaInvoiceNumber",
            "type": "Element",
        }
    )
    asnnumber: Optional[Asnnumber] = field(
        default=None,
        metadata={
            "name": "ASNNumber",
            "type": "Element",
        }
    )
    asnorder_number: Optional[AsnorderNumber] = field(
        default=None,
        metadata={
            "name": "ASNOrderNumber",
            "type": "Element",
        }
    )
    supplier_order_number: Optional[SupplierOrderNumber] = field(
        default=None,
        metadata={
            "name": "SupplierOrderNumber",
            "type": "Element",
        }
    )
    price_list_number: Optional[PriceListNumber] = field(
        default=None,
        metadata={
            "name": "PriceListNumber",
            "type": "Element",
        }
    )
    price_list_version_number: Optional[PriceListVersionNumber] = field(
        default=None,
        metadata={
            "name": "PriceListVersionNumber",
            "type": "Element",
        }
    )
    buyers_catalog_number: Optional[BuyersCatalogNumber] = field(
        default=None,
        metadata={
            "name": "BuyersCatalogNumber",
            "type": "Element",
        }
    )
    bill_of_lading_number: Optional[BillOfLadingNumber] = field(
        default=None,
        metadata={
            "name": "BillOfLadingNumber",
            "type": "Element",
        }
    )
    air_way_bill_number: Optional[AirWayBillNumber1] = field(
        default=None,
        metadata={
            "name": "AirWayBillNumber",
            "type": "Element",
        }
    )
    letter_of_credit_number: Optional[LetterOfCreditNumber] = field(
        default=None,
        metadata={
            "name": "LetterOfCreditNumber",
            "type": "Element",
        }
    )
    authorization_reference: Optional[AuthorizationReference] = field(
        default=None,
        metadata={
            "name": "AuthorizationReference",
            "type": "Element",
        }
    )
    delivery_note_number: Optional[DeliveryNoteNumber] = field(
        default=None,
        metadata={
            "name": "DeliveryNoteNumber",
            "type": "Element",
        }
    )
    cost_allocation: Optional[CostAllocation] = field(
        default=None,
        metadata={
            "name": "CostAllocation",
            "type": "Element",
        }
    )
    list_of_related_invoice_ref: Optional[ListOfRelatedInvoiceRef] = field(
        default=None,
        metadata={
            "name": "ListOfRelatedInvoiceRef",
            "type": "Element",
        }
    )
    other_invoice_references: Optional[OtherInvoiceReferences] = field(
        default=None,
        metadata={
            "name": "OtherInvoiceReferences",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InvoiceSummary:
    number_of_lines: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumberOfLines",
            "type": "Element",
        }
    )
    invoice_totals: Optional[InvoiceTotals] = field(
        default=None,
        metadata={
            "name": "InvoiceTotals",
            "type": "Element",
        }
    )
    list_of_tax_summary: Optional[ListOfTaxSummary] = field(
        default=None,
        metadata={
            "name": "ListOfTaxSummary",
            "type": "Element",
        }
    )
    allow_or_charge_summary: Optional[AllowOrChargeSummary] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeSummary",
            "type": "Element",
        }
    )
    invoice_payment_status: Optional[InvoicePaymentStatus] = field(
        default=None,
        metadata={
            "name": "InvoicePaymentStatus",
            "type": "Element",
        }
    )
    list_of_actual_payment: Optional[ListOfActualPayment] = field(
        default=None,
        metadata={
            "name": "ListOfActualPayment",
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
class OtherCountryRequirments:
    list_of_country_requirement: ListOfCountryRequirement = field(
        metadata={
            "name": "ListOfCountryRequirement",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CountrySpecificRequirements:
    nota_fiscal_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "NotaFiscalType",
            "type": "Element",
        }
    )
    payment_reference_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentReferenceNumber",
            "type": "Element",
        }
    )
    other_country_requirments: Optional[OtherCountryRequirments] = field(
        default=None,
        metadata={
            "name": "OtherCountryRequirments",
            "type": "Element",
        }
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
    line_item_references: Optional[LineItemReferences] = field(
        default=None,
        metadata={
            "name": "LineItemReferences",
            "type": "Element",
        }
    )
    exception_quantities: Optional[ExceptionQuantities] = field(
        default=None,
        metadata={
            "name": "ExceptionQuantities",
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class InvoiceHeader:
    invoice_number: InvoiceNumber = field(
        metadata={
            "name": "InvoiceNumber",
            "type": "Element",
            "required": True,
        }
    )
    invoice_issue_date: str = field(
        metadata={
            "name": "InvoiceIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    tax_point_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
        }
    )
    invoice_references: List[InvoiceReferences] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceReferences",
            "type": "Element",
        }
    )
    invoice_purpose: InvoicePurpose = field(
        metadata={
            "name": "InvoicePurpose",
            "type": "Element",
            "required": True,
        }
    )
    invoice_type: InvoiceType = field(
        metadata={
            "name": "InvoiceType",
            "type": "Element",
            "required": True,
        }
    )
    invoice_currency: Optional[InvoiceCurrency] = field(
        default=None,
        metadata={
            "name": "InvoiceCurrency",
            "type": "Element",
        }
    )
    payment_currency: Optional[PaymentCurrency] = field(
        default=None,
        metadata={
            "name": "PaymentCurrency",
            "type": "Element",
        }
    )
    list_of_rate_of_exchange_detail: Optional[ListOfRateOfExchangeDetail] = field(
        default=None,
        metadata={
            "name": "ListOfRateOfExchangeDetail",
            "type": "Element",
        }
    )
    tax_accounting_currency: Optional[TaxAccountingCurrency] = field(
        default=None,
        metadata={
            "name": "TaxAccountingCurrency",
            "type": "Element",
        }
    )
    invoice_language: InvoiceLanguage = field(
        metadata={
            "name": "InvoiceLanguage",
            "type": "Element",
            "required": True,
        }
    )
    invoice_tax_reference: Optional[InvoiceTaxReference] = field(
        default=None,
        metadata={
            "name": "InvoiceTaxReference",
            "type": "Element",
        }
    )
    invoice_medium: Optional[InvoiceMedium] = field(
        default=None,
        metadata={
            "name": "InvoiceMedium",
            "type": "Element",
        }
    )
    allow_or_charge_treatment: Optional[AllowOrChargeTreatment] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeTreatment",
            "type": "Element",
        }
    )
    invoice_dates: Optional[InvoiceDates] = field(
        default=None,
        metadata={
            "name": "InvoiceDates",
            "type": "Element",
        }
    )
    invoice_party: InvoiceParty = field(
        metadata={
            "name": "InvoiceParty",
            "type": "Element",
            "required": True,
        }
    )
    list_of_transport_routing: Optional[ListOfTransportRouting] = field(
        default=None,
        metadata={
            "name": "ListOfTransportRouting",
            "type": "Element",
        }
    )
    invoice_terms_of_delivery: Optional[InvoiceTermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "InvoiceTermsOfDelivery",
            "type": "Element",
        }
    )
    invoice_payment_instructions: Optional[InvoicePaymentInstructions] = field(
        default=None,
        metadata={
            "name": "InvoicePaymentInstructions",
            "type": "Element",
        }
    )
    invoice_allowances_or_charges: Optional[InvoiceAllowancesOrCharges] = field(
        default=None,
        metadata={
            "name": "InvoiceAllowancesOrCharges",
            "type": "Element",
        }
    )
    country_specific_requirements: Optional[CountrySpecificRequirements] = field(
        default=None,
        metadata={
            "name": "CountrySpecificRequirements",
            "type": "Element",
        }
    )
    invoice_header_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "InvoiceHeaderNote",
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
    invoice_header_attachments: Optional[InvoiceHeaderAttachments] = field(
        default=None,
        metadata={
            "name": "InvoiceHeaderAttachments",
            "type": "Element",
        }
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
        }
    )
    other_invoice_parties: Optional[OtherInvoiceParties] = field(
        default=None,
        metadata={
            "name": "OtherInvoiceParties",
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
class ListOfInvoiceItemDetail:
    invoice_item_detail: List[InvoiceItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceItemDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass(kw_only=True)
class InvoiceDetail:
    list_of_invoice_item_detail: ListOfInvoiceItemDetail = field(
        metadata={
            "name": "ListOfInvoiceItemDetail",
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
class Invoice:
    invoice_header: InvoiceHeader = field(
        metadata={
            "name": "InvoiceHeader",
            "type": "Element",
            "required": True,
        }
    )
    invoice_detail: InvoiceDetail = field(
        metadata={
            "name": "InvoiceDetail",
            "type": "Element",
            "required": True,
        }
    )
    invoice_summary: Optional[InvoiceSummary] = field(
        default=None,
        metadata={
            "name": "InvoiceSummary",
            "type": "Element",
        }
    )
