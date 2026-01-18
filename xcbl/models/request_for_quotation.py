from dataclasses import dataclass, field

from xcbl.models.shipping_schedule import ListOfPackageDetail
from xcbl.models.shipping_schedule_response import (
    OrderType,
    TotalNumberOfLineItems,
    TransportRouting,
)
from xcbl.models.sourcing_create import (
    DecisionDate,
    DeliveryDate,
)
from xcbl.models.sourcing_result import (
    BaseItemDetail,
    Contract,
    DeliveryDetail,
    ListOfAllowOrCharge,
    ListOfAttachment,
    ListOfReferenceCoded,
    MonetaryValue,
    OrderParty,
    PricingDetail,
    Tax,
    TermsOfDelivery,
)
from xcbl.models.trading_partner_organization_information import Currency
from xcbl.models.trading_partner_response import Reference
from xcbl.models.trading_partner_user_information import (
    Country,
    Language,
    Region,
    ValidityDates,
)


@dataclass(kw_only=True)
class AccountControlKey:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AccountId:
    class Meta:
        name = "AccountID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AccountName1:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AccountName2:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AccountTypeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AccountTypeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AdviseBefore:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CancelIfNotDelivered:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CardAuthCode:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CardExpirationDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CardHolderName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CardNum:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CardRefNum:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CardType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class CardTypeOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DeliveryDateEarliest:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DeliveryDateLatest:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DiscountDateTimeRefCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DiscountDateTimeRefCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DiscountDayOfMonth:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DiscountDaysDue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DiscountDueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class DiscountPercent:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FibranchCity:
    class Meta:
        name = "FIBranchCity"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FibranchHouseNumber:
    class Meta:
        name = "FIBranchHouseNumber"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FibranchId:
    class Meta:
        name = "FIBranchID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FibranchName:
    class Meta:
        name = "FIBranchName"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FibranchPostalCode:
    class Meta:
        name = "FIBranchPostalCode"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FibranchStreet:
    class Meta:
        name = "FIBranchStreet"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FibranchStreetSupplement1:
    class Meta:
        name = "FIBranchStreetSupplement1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FibranchStreetSupplement2:
    class Meta:
        name = "FIBranchStreetSupplement2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FinancialInstitutionId:
    class Meta:
        name = "FinancialInstitutionID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class FinancialInstitutionName:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class Iban:
    class Meta:
        name = "IBAN"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NetDateTimeRefCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NetDateTimeRefCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NetDaysDue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class NetDueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentMeanCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentMeanCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentSystemCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentSystemCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentTermCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentTermCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentTermValue:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class PaymentTermsNote:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequestQuoteGeneralNotes:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequestQuoteIssueDate:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequestQuotePurposeCoded:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class RequestQuotePurposeCodedOther:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class SecondaryAccountId:
    class Meta:
        name = "SecondaryAccountID"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass(kw_only=True)
class AccountNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AccountReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class BuyersCatalogNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CardInfo:
    card_num: CardNum = field(
        metadata={
            "name": "CardNum",
            "type": "Element",
            "required": True,
        }
    )
    card_auth_code: CardAuthCode | None = field(
        default=None,
        metadata={
            "name": "CardAuthCode",
            "type": "Element",
        },
    )
    card_ref_num: CardRefNum | None = field(
        default=None,
        metadata={
            "name": "CardRefNum",
            "type": "Element",
        },
    )
    card_expiration_date: CardExpirationDate | None = field(
        default=None,
        metadata={
            "name": "CardExpirationDate",
            "type": "Element",
        },
    )
    card_type: CardType | None = field(
        default=None,
        metadata={
            "name": "CardType",
            "type": "Element",
        },
    )
    card_type_other: CardTypeOther | None = field(
        default=None,
        metadata={
            "name": "CardTypeOther",
            "type": "Element",
        },
    )
    card_holder_name: CardHolderName | None = field(
        default=None,
        metadata={
            "name": "CardHolderName",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ContractReference:
    contract: Contract = field(
        metadata={
            "name": "Contract",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class DiscountAmount:
    monetary_value: MonetaryValue = field(
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FibranchCountry:
    class Meta:
        name = "FIBranchCountry"

    country: Country = field(
        metadata={
            "name": "Country",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FibranchRegion:
    class Meta:
        name = "FIBranchRegion"

    region: Region = field(
        metadata={
            "name": "Region",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ListOfRequestQuotePackageDetail:
    list_of_package_detail: ListOfPackageDetail = field(
        metadata={
            "name": "ListOfPackageDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OtherRequestQuoteReferences:
    list_of_reference_coded: ListOfReferenceCoded = field(
        metadata={
            "name": "ListOfReferenceCoded",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentMeanReference:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceListNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PriceListVersionNumber:
    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteAllowanceOrCharge:
    list_of_allow_or_charge: ListOfAllowOrCharge = field(
        metadata={
            "name": "ListOfAllowOrCharge",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteCurrency:
    currency: Currency = field(
        metadata={
            "name": "Currency",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteDeliveryDetail:
    delivery_detail: DeliveryDetail = field(
        metadata={
            "name": "DeliveryDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteId:
    class Meta:
        name = "RequestQuoteID"

    reference: Reference = field(
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteItemDetail:
    base_item_detail: BaseItemDetail = field(
        metadata={
            "name": "BaseItemDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteItemListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteLanguage:
    language: Language = field(
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteListOfAttachment:
    list_of_attachment: ListOfAttachment = field(
        metadata={
            "name": "ListOfAttachment",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteParty:
    order_party: OrderParty = field(
        metadata={
            "name": "OrderParty",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuotePricingDetail:
    pricing_detail: PricingDetail = field(
        metadata={
            "name": "PricingDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuotePurpose:
    request_quote_purpose_coded: RequestQuotePurposeCoded = field(
        metadata={
            "name": "RequestQuotePurposeCoded",
            "type": "Element",
            "required": True,
        }
    )
    request_quote_purpose_coded_other: RequestQuotePurposeCodedOther | None = (
        field(
            default=None,
            metadata={
                "name": "RequestQuotePurposeCodedOther",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class RequestQuoteSummary:
    total_number_of_line_items: TotalNumberOfLineItems | None = field(
        default=None,
        metadata={
            "name": "TotalNumberOfLineItems",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RequestQuoteTax:
    tax: Tax = field(
        metadata={
            "name": "Tax",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteTermsOfDelivery:
    terms_of_delivery: TermsOfDelivery = field(
        metadata={
            "name": "TermsOfDelivery",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteTransport:
    transport_routing: TransportRouting = field(
        metadata={
            "name": "TransportRouting",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteValidityDate:
    validity_dates: ValidityDates = field(
        metadata={
            "name": "ValidityDates",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ResultingOrderType:
    order_type: OrderType = field(
        metadata={
            "name": "OrderType",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AccountDetail:
    account_id: AccountId = field(
        metadata={
            "name": "AccountID",
            "type": "Element",
            "required": True,
        }
    )
    secondary_account_id: SecondaryAccountId | None = field(
        default=None,
        metadata={
            "name": "SecondaryAccountID",
            "type": "Element",
        },
    )
    iban: Iban | None = field(
        default=None,
        metadata={
            "name": "IBAN",
            "type": "Element",
        },
    )
    account_control_key: AccountControlKey | None = field(
        default=None,
        metadata={
            "name": "AccountControlKey",
            "type": "Element",
        },
    )
    account_type_coded: AccountTypeCoded = field(
        metadata={
            "name": "AccountTypeCoded",
            "type": "Element",
            "required": True,
        }
    )
    account_type_coded_other: AccountTypeCodedOther | None = field(
        default=None,
        metadata={
            "name": "AccountTypeCodedOther",
            "type": "Element",
        },
    )
    account_name1: AccountName1 = field(
        metadata={
            "name": "AccountName1",
            "type": "Element",
            "required": True,
        }
    )
    account_name2: AccountName2 | None = field(
        default=None,
        metadata={
            "name": "AccountName2",
            "type": "Element",
        },
    )
    currency: Currency | None = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
        },
    )
    account_references: AccountReferences | None = field(
        default=None,
        metadata={
            "name": "AccountReferences",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Discounts:
    discount_percent: DiscountPercent | None = field(
        default=None,
        metadata={
            "name": "DiscountPercent",
            "type": "Element",
        },
    )
    discount_amount: DiscountAmount | None = field(
        default=None,
        metadata={
            "name": "DiscountAmount",
            "type": "Element",
        },
    )
    discount_days_due: DiscountDaysDue | None = field(
        default=None,
        metadata={
            "name": "DiscountDaysDue",
            "type": "Element",
        },
    )
    discount_due_date: DiscountDueDate | None = field(
        default=None,
        metadata={
            "name": "DiscountDueDate",
            "type": "Element",
        },
    )
    discount_day_of_month: DiscountDayOfMonth | None = field(
        default=None,
        metadata={
            "name": "DiscountDayOfMonth",
            "type": "Element",
        },
    )
    discount_date_time_ref_coded: DiscountDateTimeRefCoded | None = field(
        default=None,
        metadata={
            "name": "DiscountDateTimeRefCoded",
            "type": "Element",
        },
    )
    discount_date_time_ref_coded_other: (
        DiscountDateTimeRefCodedOther | None
    ) = field(
        default=None,
        metadata={
            "name": "DiscountDateTimeRefCodedOther",
            "type": "Element",
        },
    )
    net_days_due: NetDaysDue | None = field(
        default=None,
        metadata={
            "name": "NetDaysDue",
            "type": "Element",
        },
    )
    net_due_date: NetDueDate | None = field(
        default=None,
        metadata={
            "name": "NetDueDate",
            "type": "Element",
        },
    )
    net_date_time_ref_coded: NetDateTimeRefCoded | None = field(
        default=None,
        metadata={
            "name": "NetDateTimeRefCoded",
            "type": "Element",
        },
    )
    net_date_time_ref_coded_other: NetDateTimeRefCodedOther | None = field(
        default=None,
        metadata={
            "name": "NetDateTimeRefCodedOther",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class FinancialInstitution:
    financial_institution_id: FinancialInstitutionId = field(
        metadata={
            "name": "FinancialInstitutionID",
            "type": "Element",
            "required": True,
        }
    )
    financial_institution_name: FinancialInstitutionName = field(
        metadata={
            "name": "FinancialInstitutionName",
            "type": "Element",
            "required": True,
        }
    )
    fibranch_id: FibranchId | None = field(
        default=None,
        metadata={
            "name": "FIBranchID",
            "type": "Element",
        },
    )
    fibranch_name: FibranchName | None = field(
        default=None,
        metadata={
            "name": "FIBranchName",
            "type": "Element",
        },
    )
    fibranch_street: FibranchStreet | None = field(
        default=None,
        metadata={
            "name": "FIBranchStreet",
            "type": "Element",
        },
    )
    fibranch_house_number: FibranchHouseNumber | None = field(
        default=None,
        metadata={
            "name": "FIBranchHouseNumber",
            "type": "Element",
        },
    )
    fibranch_street_supplement1: FibranchStreetSupplement1 | None = field(
        default=None,
        metadata={
            "name": "FIBranchStreetSupplement1",
            "type": "Element",
        },
    )
    fibranch_street_supplement2: FibranchStreetSupplement2 | None = field(
        default=None,
        metadata={
            "name": "FIBranchStreetSupplement2",
            "type": "Element",
        },
    )
    fibranch_postal_code: FibranchPostalCode | None = field(
        default=None,
        metadata={
            "name": "FIBranchPostalCode",
            "type": "Element",
        },
    )
    fibranch_city: FibranchCity | None = field(
        default=None,
        metadata={
            "name": "FIBranchCity",
            "type": "Element",
        },
    )
    fibranch_region: FibranchRegion | None = field(
        default=None,
        metadata={
            "name": "FIBranchRegion",
            "type": "Element",
        },
    )
    fibranch_country: FibranchCountry | None = field(
        default=None,
        metadata={
            "name": "FIBranchCountry",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RequestQuoteDate:
    request_quote_validity_date: RequestQuoteValidityDate = field(
        metadata={
            "name": "RequestQuoteValidityDate",
            "type": "Element",
            "required": True,
        }
    )
    decision_date: DecisionDate | None = field(
        default=None,
        metadata={
            "name": "DecisionDate",
            "type": "Element",
        },
    )
    delivery_date: DeliveryDate | None = field(
        default=None,
        metadata={
            "name": "DeliveryDate",
            "type": "Element",
        },
    )
    delivery_date_earliest: DeliveryDateEarliest | None = field(
        default=None,
        metadata={
            "name": "DeliveryDateEarliest",
            "type": "Element",
        },
    )
    delivery_date_latest: DeliveryDateLatest | None = field(
        default=None,
        metadata={
            "name": "DeliveryDateLatest",
            "type": "Element",
        },
    )
    advise_before: AdviseBefore | None = field(
        default=None,
        metadata={
            "name": "AdviseBefore",
            "type": "Element",
        },
    )
    cancel_if_not_delivered: CancelIfNotDelivered | None = field(
        default=None,
        metadata={
            "name": "CancelIfNotDelivered",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RequestQuoteDetails:
    request_quote_item_detail: RequestQuoteItemDetail = field(
        metadata={
            "name": "RequestQuoteItemDetail",
            "type": "Element",
            "required": True,
        }
    )
    request_quote_pricing_detail: RequestQuotePricingDetail | None = field(
        default=None,
        metadata={
            "name": "RequestQuotePricingDetail",
            "type": "Element",
        },
    )
    request_quote_delivery_detail: RequestQuoteDeliveryDetail | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteDeliveryDetail",
            "type": "Element",
        },
    )
    request_quote_item_list_of_attachment: (
        RequestQuoteItemListOfAttachment | None
    ) = field(
        default=None,
        metadata={
            "name": "RequestQuoteItemListOfAttachment",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class RequestQuoteReference:
    contract_reference: ContractReference | None = field(
        default=None,
        metadata={
            "name": "ContractReference",
            "type": "Element",
        },
    )
    account_number: AccountNumber | None = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Element",
        },
    )
    price_list_number: PriceListNumber | None = field(
        default=None,
        metadata={
            "name": "PriceListNumber",
            "type": "Element",
        },
    )
    price_list_version_number: PriceListVersionNumber | None = field(
        default=None,
        metadata={
            "name": "PriceListVersionNumber",
            "type": "Element",
        },
    )
    buyers_catalog_number: BuyersCatalogNumber | None = field(
        default=None,
        metadata={
            "name": "BuyersCatalogNumber",
            "type": "Element",
        },
    )
    other_request_quote_references: OtherRequestQuoteReferences | None = field(
        default=None,
        metadata={
            "name": "OtherRequestQuoteReferences",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Fiaccount:
    class Meta:
        name = "FIAccount"

    account_detail: AccountDetail | None = field(
        default=None,
        metadata={
            "name": "AccountDetail",
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
class ListOfRequestQuoteDetails:
    request_quote_details: list[RequestQuoteDetails] = field(
        default_factory=list,
        metadata={
            "name": "RequestQuoteDetails",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class PaymentTermDetails:
    discounts: Discounts = field(
        metadata={
            "name": "Discounts",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class OriginatingFiaccount:
    class Meta:
        name = "OriginatingFIAccount"

    fiaccount: Fiaccount = field(
        metadata={
            "name": "FIAccount",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentTerm:
    payment_term_coded: PaymentTermCoded = field(
        metadata={
            "name": "PaymentTermCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_term_coded_other: PaymentTermCodedOther | None = field(
        default=None,
        metadata={
            "name": "PaymentTermCodedOther",
            "type": "Element",
        },
    )
    payment_term_value: PaymentTermValue | None = field(
        default=None,
        metadata={
            "name": "PaymentTermValue",
            "type": "Element",
        },
    )
    payment_term_details: PaymentTermDetails | None = field(
        default=None,
        metadata={
            "name": "PaymentTermDetails",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class ReceivingFiaccount:
    class Meta:
        name = "ReceivingFIAccount"

    fiaccount: Fiaccount = field(
        metadata={
            "name": "FIAccount",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PaymentMethod:
    payment_mean_coded: PaymentMeanCoded = field(
        metadata={
            "name": "PaymentMeanCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_mean_coded_other: PaymentMeanCodedOther | None = field(
        default=None,
        metadata={
            "name": "PaymentMeanCodedOther",
            "type": "Element",
        },
    )
    payment_mean_reference: PaymentMeanReference | None = field(
        default=None,
        metadata={
            "name": "PaymentMeanReference",
            "type": "Element",
        },
    )
    payment_system_coded: PaymentSystemCoded | None = field(
        default=None,
        metadata={
            "name": "PaymentSystemCoded",
            "type": "Element",
        },
    )
    payment_system_coded_other: PaymentSystemCodedOther | None = field(
        default=None,
        metadata={
            "name": "PaymentSystemCodedOther",
            "type": "Element",
        },
    )
    originating_fiaccount: OriginatingFiaccount | None = field(
        default=None,
        metadata={
            "name": "OriginatingFIAccount",
            "type": "Element",
        },
    )
    receiving_fiaccount: ReceivingFiaccount | None = field(
        default=None,
        metadata={
            "name": "ReceivingFIAccount",
            "type": "Element",
        },
    )
    card_info: CardInfo | None = field(
        default=None,
        metadata={
            "name": "CardInfo",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentTerms:
    payment_term: list[PaymentTerm] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerm",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    discounts: list[Discounts] = field(
        default_factory=list,
        metadata={
            "name": "Discounts",
            "type": "Element",
        },
    )
    payment_terms_note: PaymentTermsNote | None = field(
        default=None,
        metadata={
            "name": "PaymentTermsNote",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class PaymentInstructions:
    payment_terms: list[PaymentTerms] = field(
        default_factory=list,
        metadata={
            "name": "PaymentTerms",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    payment_method: list[PaymentMethod] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class RequestQuoteTermsOfPayment:
    payment_instructions: PaymentInstructions = field(
        metadata={
            "name": "PaymentInstructions",
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RequestQuoteHeader:
    request_quote_issue_date: RequestQuoteIssueDate = field(
        metadata={
            "name": "RequestQuoteIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    request_quote_id: RequestQuoteId = field(
        metadata={
            "name": "RequestQuoteID",
            "type": "Element",
            "required": True,
        }
    )
    request_quote_reference: RequestQuoteReference | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteReference",
            "type": "Element",
        },
    )
    request_quote_purpose: RequestQuotePurpose | None = field(
        default=None,
        metadata={
            "name": "RequestQuotePurpose",
            "type": "Element",
        },
    )
    request_quote_date: RequestQuoteDate | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteDate",
            "type": "Element",
        },
    )
    request_quote_party: RequestQuoteParty = field(
        metadata={
            "name": "RequestQuoteParty",
            "type": "Element",
            "required": True,
        }
    )
    resulting_order_type: ResultingOrderType | None = field(
        default=None,
        metadata={
            "name": "ResultingOrderType",
            "type": "Element",
        },
    )
    request_quote_currency: RequestQuoteCurrency | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteCurrency",
            "type": "Element",
        },
    )
    request_quote_allowance_or_charge: RequestQuoteAllowanceOrCharge | None = (
        field(
            default=None,
            metadata={
                "name": "RequestQuoteAllowanceOrCharge",
                "type": "Element",
            },
        )
    )
    request_quote_terms_of_payment: RequestQuoteTermsOfPayment | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteTermsOfPayment",
            "type": "Element",
        },
    )
    request_quote_terms_of_delivery: RequestQuoteTermsOfDelivery | None = (
        field(
            default=None,
            metadata={
                "name": "RequestQuoteTermsOfDelivery",
                "type": "Element",
            },
        )
    )
    request_quote_tax: RequestQuoteTax | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteTax",
            "type": "Element",
        },
    )
    request_quote_transport: RequestQuoteTransport | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteTransport",
            "type": "Element",
        },
    )
    request_quote_language: RequestQuoteLanguage | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteLanguage",
            "type": "Element",
        },
    )
    request_quote_general_notes: RequestQuoteGeneralNotes | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteGeneralNotes",
            "type": "Element",
        },
    )
    request_quote_list_of_attachment: RequestQuoteListOfAttachment | None = (
        field(
            default=None,
            metadata={
                "name": "RequestQuoteListOfAttachment",
                "type": "Element",
            },
        )
    )


@dataclass(kw_only=True)
class RequestForQuotation:
    request_quote_header: RequestQuoteHeader = field(
        metadata={
            "name": "RequestQuoteHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_request_quote_details: ListOfRequestQuoteDetails | None = field(
        default=None,
        metadata={
            "name": "ListOfRequestQuoteDetails",
            "type": "Element",
        },
    )
    list_of_request_quote_package_detail: (
        ListOfRequestQuotePackageDetail | None
    ) = field(
        default=None,
        metadata={
            "name": "ListOfRequestQuotePackageDetail",
            "type": "Element",
        },
    )
    request_quote_summary: RequestQuoteSummary | None = field(
        default=None,
        metadata={
            "name": "RequestQuoteSummary",
            "type": "Element",
        },
    )
