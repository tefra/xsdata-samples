from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.order_response import (
    NumberOfLines,
    TaxAccountingCurrency,
)
from xcbl.models.quote import TaxReference
from xcbl.models.remittance_advice import (
    InvoiceDates,
    InvoiceItemDetail,
    InvoiceNumber,
    InvoiceReferences,
    InvoiceType,
    ListOfRateOfExchangeDetail,
    PaymentCurrency,
    SummaryNote,
    TotalTaxAmount,
)
from xcbl.models.request_for_quotation import (
    CardInfo,
    Fiaccount,
    PaymentInstructions,
    PaymentMeanCoded,
)
from xcbl.models.shipping_schedule import ListOfPackageDetail
from xcbl.models.shipping_schedule_response import (
    ListOfTransportRouting,
    MaterialIssuerParty,
)
from xcbl.models.sourcing_result import (
    AllowanceOrChargeDescription,
    BillToParty,
    BuyerParty,
    BuyerTaxInformation,
    ListOfAllowOrCharge,
    ListOfAttachment,
    ListOfNameValueSet,
    ListOfStructuredNote,
    MonetaryValue,
    PartyTaxInformation,
    RemitToParty,
    SellerParty,
    SellerTaxInformation,
    ShipFromParty,
    ShipToParty,
    SoldToParty,
    Tax,
    TermsOfDelivery,
    WarehouseParty,
)
from xcbl.models.time_series_response import (
    ListOfPartyCoded,
    Party,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import (
    Country,
    Language,
)


@dataclass(kw_only=True)
class AllowOrChargeIndicatorCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AllowOrChargeIndicatorCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AllowOrChargeTreatmentCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AllowOrChargeTreatmentCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceHeaderNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceMediumCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoiceMediumCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoicePaymentStatusCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoicePaymentStatusCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoicePurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class InvoicePurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NotaFiscalType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class OtherPaymentInfo:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentCodedMeanOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentRecordOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentReferenceNumber:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequirementDetails:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequirementTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequirementTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class TaxPointDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AllowOrChargeTreatment:
    allow_or_charge_treatment_coded: Optional[
        AllowOrChargeTreatmentCoded
    ] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeTreatmentCoded",
            "type": "Element",
        },
    )
    allow_or_charge_treatment_coded_other: Optional[
        AllowOrChargeTreatmentCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeTreatmentCodedOther",
            "type": "Element",
        },
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
class ChargeTotal:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
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
class InvoiceMedium:
    invoice_medium_coded: Optional[InvoiceMediumCoded] = field(
        default=None,
        metadata={
            "name": "InvoiceMediumCoded",
            "type": "Element",
        },
    )
    invoice_medium_coded_other: Optional[InvoiceMediumCodedOther] = field(
        default=None,
        metadata={
            "name": "InvoiceMediumCodedOther",
            "type": "Element",
        },
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
class InvoicePaymentStatus:
    invoice_payment_status_coded: Optional[InvoicePaymentStatusCoded] = field(
        default=None,
        metadata={
            "name": "InvoicePaymentStatusCoded",
            "type": "Element",
        },
    )
    invoice_payment_status_coded_other: Optional[
        InvoicePaymentStatusCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "InvoicePaymentStatusCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class InvoicePurpose:
    invoice_purpose_coded: InvoicePurposeCoded = field(
        metadata={
            "name": "InvoicePurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    invoice_purpose_coded_other: Optional[InvoicePurposeCodedOther] = field(
        default=None,
        metadata={
            "name": "InvoicePurposeCodedOther",
            "type": "Element",
        },
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
class ListOfInvoiceItemDetail:
    invoice_item_detail: List[InvoiceItemDetail] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceItemDetail",
            "type": "Element",
            "min_occurs": 1,
        },
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
class PaymentMean:
    payment_mean_coded: PaymentMeanCoded = field(
        metadata={
            "name": "PaymentMeanCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_coded_mean_other: Optional[PaymentCodedMeanOther] = field(
        default=None,
        metadata={
            "name": "PaymentCodedMeanOther",
            "type": "Element",
        },
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
class SummaryAllowOrCharge:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
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
class Fitransfer:
    class Meta:
        name = "FITransfer"

    from_fitransfer: Optional[FromFitransfer] = field(
        default=None,
        metadata={
            "name": "FromFITransfer",
            "type": "Element",
        },
    )
    to_fitransfer: ToFitransfer = field(
        metadata={
            "name": "ToFITransfer",
            "type": "Element",
            "required": True,
        }
    )
    payment_record_other: Optional[PaymentRecordOther] = field(
        default=None,
        metadata={
            "name": "PaymentRecordOther",
            "type": "Element",
        },
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
        },
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
        },
    )
    buyer_tax: Optional[BuyerTax] = field(
        default=None,
        metadata={
            "name": "BuyerTax",
            "type": "Element",
        },
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
        },
    )
    ship_to_party: Optional[ShipToParty] = field(
        default=None,
        metadata={
            "name": "ShipToParty",
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
    remit_to_party: Optional[RemitToParty] = field(
        default=None,
        metadata={
            "name": "RemitToParty",
            "type": "Element",
        },
    )
    remit_to_tax_information: Optional[RemitToTaxInformation] = field(
        default=None,
        metadata={
            "name": "RemitToTaxInformation",
            "type": "Element",
        },
    )
    remit_to_tax: Optional[RemitToTax] = field(
        default=None,
        metadata={
            "name": "RemitToTax",
            "type": "Element",
        },
    )
    ship_from_party: Optional[ShipFromParty] = field(
        default=None,
        metadata={
            "name": "ShipFromParty",
            "type": "Element",
        },
    )
    warehouse_party: Optional[WarehouseParty] = field(
        default=None,
        metadata={
            "name": "WarehouseParty",
            "type": "Element",
        },
    )
    sold_to_party: Optional[SoldToParty] = field(
        default=None,
        metadata={
            "name": "SoldToParty",
            "type": "Element",
        },
    )
    manufacturing_party: Optional[ManufacturingParty] = field(
        default=None,
        metadata={
            "name": "ManufacturingParty",
            "type": "Element",
        },
    )
    material_issuer_party: Optional[MaterialIssuerParty] = field(
        default=None,
        metadata={
            "name": "MaterialIssuerParty",
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
        },
    )
    tax_value_in_tax_accounting_currency: Optional[
        TaxValueInTaxAccountingCurrency
    ] = field(
        default=None,
        metadata={
            "name": "TaxValueInTaxAccountingCurrency",
            "type": "Element",
        },
    )
    charge_total: Optional[ChargeTotal] = field(
        default=None,
        metadata={
            "name": "ChargeTotal",
            "type": "Element",
        },
    )
    total_amount_payable: Optional[TotalAmountPayable] = field(
        default=None,
        metadata={
            "name": "TotalAmountPayable",
            "type": "Element",
        },
    )
    prepaid_amount: Optional[PrepaidAmount] = field(
        default=None,
        metadata={
            "name": "PrepaidAmount",
            "type": "Element",
        },
    )
    total_discount: Optional[TotalDiscount] = field(
        default=None,
        metadata={
            "name": "TotalDiscount",
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
    total_amount_minus_discount: Optional[TotalAmountMinusDiscount] = field(
        default=None,
        metadata={
            "name": "TotalAmountMinusDiscount",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ListOfTaxSummary:
    tax_summary: List[TaxSummary] = field(
        default_factory=list,
        metadata={
            "name": "TaxSummary",
            "type": "Element",
            "min_occurs": 1,
        },
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
class SpecificRequirement:
    requirement_type_coded: RequirementTypeCoded = field(
        metadata={
            "name": "RequirementTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    requirement_type_coded_other: Optional[RequirementTypeCodedOther] = field(
        default=None,
        metadata={
            "name": "RequirementTypeCodedOther",
            "type": "Element",
        },
    )
    requirement_reference: Optional[RequirementReference] = field(
        default=None,
        metadata={
            "name": "RequirementReference",
            "type": "Element",
        },
    )
    requirement_details: Optional[RequirementDetails] = field(
        default=None,
        metadata={
            "name": "RequirementDetails",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class TotalAllowOrCharge:
    allow_or_charge_indicator_coded: AllowOrChargeIndicatorCoded = field(
        metadata={
            "name": "AllowOrChargeIndicatorCoded",
            "type": "Element",
            "required": True,
        }
    )
    allow_or_charge_indicator_coded_other: Optional[
        AllowOrChargeIndicatorCodedOther
    ] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeIndicatorCodedOther",
            "type": "Element",
        },
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
class AllowOrChargeSummary:
    total_allow_or_charge: List[TotalAllowOrCharge] = field(
        default_factory=list,
        metadata={
            "name": "TotalAllowOrCharge",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfSpecificRequirement:
    specific_requirement: List[SpecificRequirement] = field(
        default_factory=list,
        metadata={
            "name": "SpecificRequirement",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PaymentRecord:
    payment_ref: Optional[PaymentRef] = field(
        default=None,
        metadata={
            "name": "PaymentRef",
            "type": "Element",
        },
    )
    card_info: Optional[CardInfo] = field(
        default=None,
        metadata={
            "name": "CardInfo",
            "type": "Element",
        },
    )
    fitransfer: Optional[Fitransfer] = field(
        default=None,
        metadata={
            "name": "FITransfer",
            "type": "Element",
        },
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
    payment_date: PaymentDate = field(
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
        },
    )
    other_payment_info: List[OtherPaymentInfo] = field(
        default_factory=list,
        metadata={
            "name": "OtherPaymentInfo",
            "type": "Element",
        },
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
class ListOfActualPayment:
    actual_payment: List[ActualPayment] = field(
        default_factory=list,
        metadata={
            "name": "ActualPayment",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListOfCountryRequirement:
    country_requirement: List[CountryRequirement] = field(
        default_factory=list,
        metadata={
            "name": "CountryRequirement",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class InvoiceSummary:
    number_of_lines: Optional[NumberOfLines] = field(
        default=None,
        metadata={
            "name": "NumberOfLines",
            "type": "Element",
        },
    )
    invoice_totals: Optional[InvoiceTotals] = field(
        default=None,
        metadata={
            "name": "InvoiceTotals",
            "type": "Element",
        },
    )
    list_of_tax_summary: Optional[ListOfTaxSummary] = field(
        default=None,
        metadata={
            "name": "ListOfTaxSummary",
            "type": "Element",
        },
    )
    allow_or_charge_summary: Optional[AllowOrChargeSummary] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeSummary",
            "type": "Element",
        },
    )
    invoice_payment_status: Optional[InvoicePaymentStatus] = field(
        default=None,
        metadata={
            "name": "InvoicePaymentStatus",
            "type": "Element",
        },
    )
    list_of_actual_payment: Optional[ListOfActualPayment] = field(
        default=None,
        metadata={
            "name": "ListOfActualPayment",
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
    nota_fiscal_type: Optional[NotaFiscalType] = field(
        default=None,
        metadata={
            "name": "NotaFiscalType",
            "type": "Element",
        },
    )
    payment_reference_number: Optional[PaymentReferenceNumber] = field(
        default=None,
        metadata={
            "name": "PaymentReferenceNumber",
            "type": "Element",
        },
    )
    other_country_requirments: Optional[OtherCountryRequirments] = field(
        default=None,
        metadata={
            "name": "OtherCountryRequirments",
            "type": "Element",
        },
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
    invoice_issue_date: InvoiceIssueDate = field(
        metadata={
            "name": "InvoiceIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    tax_point_date: Optional[TaxPointDate] = field(
        default=None,
        metadata={
            "name": "TaxPointDate",
            "type": "Element",
        },
    )
    invoice_references: List[InvoiceReferences] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceReferences",
            "type": "Element",
        },
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
        },
    )
    payment_currency: Optional[PaymentCurrency] = field(
        default=None,
        metadata={
            "name": "PaymentCurrency",
            "type": "Element",
        },
    )
    list_of_rate_of_exchange_detail: Optional[
        ListOfRateOfExchangeDetail
    ] = field(
        default=None,
        metadata={
            "name": "ListOfRateOfExchangeDetail",
            "type": "Element",
        },
    )
    tax_accounting_currency: Optional[TaxAccountingCurrency] = field(
        default=None,
        metadata={
            "name": "TaxAccountingCurrency",
            "type": "Element",
        },
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
        },
    )
    invoice_medium: Optional[InvoiceMedium] = field(
        default=None,
        metadata={
            "name": "InvoiceMedium",
            "type": "Element",
        },
    )
    allow_or_charge_treatment: Optional[AllowOrChargeTreatment] = field(
        default=None,
        metadata={
            "name": "AllowOrChargeTreatment",
            "type": "Element",
        },
    )
    invoice_dates: Optional[InvoiceDates] = field(
        default=None,
        metadata={
            "name": "InvoiceDates",
            "type": "Element",
        },
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
        },
    )
    invoice_terms_of_delivery: Optional[InvoiceTermsOfDelivery] = field(
        default=None,
        metadata={
            "name": "InvoiceTermsOfDelivery",
            "type": "Element",
        },
    )
    invoice_payment_instructions: Optional[InvoicePaymentInstructions] = field(
        default=None,
        metadata={
            "name": "InvoicePaymentInstructions",
            "type": "Element",
        },
    )
    invoice_allowances_or_charges: Optional[
        InvoiceAllowancesOrCharges
    ] = field(
        default=None,
        metadata={
            "name": "InvoiceAllowancesOrCharges",
            "type": "Element",
        },
    )
    country_specific_requirements: Optional[
        CountrySpecificRequirements
    ] = field(
        default=None,
        metadata={
            "name": "CountrySpecificRequirements",
            "type": "Element",
        },
    )
    invoice_header_note: Optional[InvoiceHeaderNote] = field(
        default=None,
        metadata={
            "name": "InvoiceHeaderNote",
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
    invoice_header_attachments: Optional[InvoiceHeaderAttachments] = field(
        default=None,
        metadata={
            "name": "InvoiceHeaderAttachments",
            "type": "Element",
        },
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
        },
    )
