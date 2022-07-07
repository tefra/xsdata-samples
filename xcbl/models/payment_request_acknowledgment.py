from dataclasses import dataclass, field
from typing import List, Optional
from xcbl.models.auction_create import (
    CorrespondenceLanguage,
    Language,
    ListOfIdentifier,
    ListOfValues,
    NameAddress,
    NameValuePair,
    OrderContact,
    OtherContacts,
    Party,
    PartyId,
    RateOfExchangeDetail,
    ReceivingContact,
    Reference,
    ShippingContact,
)
from xcbl.models.order_request import (
    AccountDetail,
    BillToParty,
    BuyerParty,
    FinancialInstitution,
    ListOfPartyCoded,
    MonetaryValue,
)


@dataclass
class EncryptedField:
    sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
        }
    )
    encrypted_data: Optional[str] = field(
        default=None,
        metadata={
            "name": "EncryptedData",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class CreditAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class DebitAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class FiaccountData:
    class Meta:
        name = "FIAccountData"

    account_detail: Optional[AccountDetail] = field(
        default=None,
        metadata={
            "name": "AccountDetail",
            "type": "Element",
        }
    )
    financial_institution: Optional[FinancialInstitution] = field(
        default=None,
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )
    sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sequence",
            "type": "Element",
        }
    )
    finote: Optional[str] = field(
        default=None,
        metadata={
            "name": "FINote",
            "type": "Element",
        }
    )


@dataclass
class FiaccountDetail:
    class Meta:
        name = "FIAccountDetail"

    account_detail: Optional[AccountDetail] = field(
        default=None,
        metadata={
            "name": "AccountDetail",
            "type": "Element",
            "required": True,
        }
    )
    financial_institution: Optional[FinancialInstitution] = field(
        default=None,
        metadata={
            "name": "FinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfEncryptedField:
    encrypted_field: List[EncryptedField] = field(
        default_factory=list,
        metadata={
            "name": "EncryptedField",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfRateOfExchangeDetail:
    rate_of_exchange_detail: List[RateOfExchangeDetail] = field(
        default_factory=list,
        metadata={
            "name": "RateOfExchangeDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class ListOfSummaryItems:
    list_of_values: Optional[ListOfValues] = field(
        default=None,
        metadata={
            "name": "ListOfValues",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class OffendingPaymentElement:
    name_value_pair: Optional[NameValuePair] = field(
        default=None,
        metadata={
            "name": "NameValuePair",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PayeeParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PayerParty:
    party_id: Optional[PartyId] = field(
        default=None,
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
        }
    )
    mdfbusiness: Optional[str] = field(
        default=None,
        metadata={
            "name": "MDFBusiness",
            "type": "Element",
        }
    )
    name_address: Optional[NameAddress] = field(
        default=None,
        metadata={
            "name": "NameAddress",
            "type": "Element",
        }
    )
    order_contact: Optional[OrderContact] = field(
        default=None,
        metadata={
            "name": "OrderContact",
            "type": "Element",
        }
    )
    receiving_contact: Optional[ReceivingContact] = field(
        default=None,
        metadata={
            "name": "ReceivingContact",
            "type": "Element",
        }
    )
    shipping_contact: Optional[ShippingContact] = field(
        default=None,
        metadata={
            "name": "ShippingContact",
            "type": "Element",
        }
    )
    other_contacts: Optional[OtherContacts] = field(
        default=None,
        metadata={
            "name": "OtherContacts",
            "type": "Element",
        }
    )
    correspondence_language: Optional[CorrespondenceLanguage] = field(
        default=None,
        metadata={
            "name": "CorrespondenceLanguage",
            "type": "Element",
        }
    )
    certificate_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertificateAuthority",
            "type": "Element",
        }
    )


@dataclass
class PaymentDocumentId:
    class Meta:
        name = "PaymentDocumentID"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentRequestIdreference:
    class Meta:
        name = "PaymentRequestIDReference"

    reference: Optional[Reference] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SettlementAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class SupplierParty:
    party: Optional[Party] = field(
        default=None,
        metadata={
            "name": "Party",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class TotalSettlementAmount:
    monetary_value: Optional[MonetaryValue] = field(
        default=None,
        metadata={
            "name": "MonetaryValue",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class EncryptedInfo:
    certificate_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertificateAuthority",
            "type": "Element",
        }
    )
    list_of_encrypted_field: Optional[ListOfEncryptedField] = field(
        default=None,
        metadata={
            "name": "ListOfEncryptedField",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfFiaccount:
    class Meta:
        name = "ListOfFIAccount"

    fiaccount_data: List[FiaccountData] = field(
        default_factory=list,
        metadata={
            "name": "FIAccountData",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class OriginatingFinancialInstitution:
    fiaccount_detail: Optional[FiaccountDetail] = field(
        default=None,
        metadata={
            "name": "FIAccountDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentException:
    payment_exception_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentExceptionCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_exception_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentExceptionCodedOther",
            "type": "Element",
        }
    )
    payment_exception_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentExceptionNote",
            "type": "Element",
        }
    )
    offending_payment_element: Optional[OffendingPaymentElement] = field(
        default=None,
        metadata={
            "name": "OffendingPaymentElement",
            "type": "Element",
        }
    )


@dataclass
class PaymentParty:
    payer_party: Optional[PayerParty] = field(
        default=None,
        metadata={
            "name": "PayerParty",
            "type": "Element",
            "required": True,
        }
    )
    payee_party: Optional[PayeeParty] = field(
        default=None,
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
        }
    )
    supplier_party: Optional[SupplierParty] = field(
        default=None,
        metadata={
            "name": "SupplierParty",
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
    list_of_party_coded: Optional[ListOfPartyCoded] = field(
        default=None,
        metadata={
            "name": "ListOfPartyCoded",
            "type": "Element",
        }
    )


@dataclass
class PaymentRequestAcknHeader:
    payment_request_ackn_coded: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRequestAcknCoded",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_ackn_coded_other: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRequestAcknCodedOther",
            "type": "Element",
        }
    )
    payment_request_ackn_issue_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRequestAcknIssueDate",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_ackn_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRequestAcknID",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_idreference: Optional[PaymentRequestIdreference] = field(
        default=None,
        metadata={
            "name": "PaymentRequestIDReference",
            "type": "Element",
        }
    )
    certificate_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "CertificateAuthority",
            "type": "Element",
        }
    )
    successful_recept_indicator: Optional[str] = field(
        default=None,
        metadata={
            "name": "SuccessfulReceptIndicator",
            "type": "Element",
            "required": True,
        }
    )
    general_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeneralNote",
            "type": "Element",
        }
    )
    language: Optional[Language] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ReceivingFinancialInstitution:
    fiaccount_detail: Optional[FiaccountDetail] = field(
        default=None,
        metadata={
            "name": "FIAccountDetail",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfFinancialInstitutions:
    list_of_fiaccount: Optional[ListOfFiaccount] = field(
        default=None,
        metadata={
            "name": "ListOfFIAccount",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class ListOfPaymentException:
    payment_exception: List[PaymentException] = field(
        default_factory=list,
        metadata={
            "name": "PaymentException",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PaymentRequestSummary:
    total_payment_documents: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPaymentDocuments",
            "type": "Element",
        }
    )
    total_line_item: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalLineItem",
            "type": "Element",
        }
    )
    total_settlement_amount: Optional[TotalSettlementAmount] = field(
        default=None,
        metadata={
            "name": "TotalSettlementAmount",
            "type": "Element",
        }
    )
    encrypted_info: Optional[EncryptedInfo] = field(
        default=None,
        metadata={
            "name": "EncryptedInfo",
            "type": "Element",
        }
    )
    list_of_summary_items: Optional[ListOfSummaryItems] = field(
        default=None,
        metadata={
            "name": "ListOfSummaryItems",
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


@dataclass
class FinancialInstitutionDetail:
    originating_financial_institution: Optional[OriginatingFinancialInstitution] = field(
        default=None,
        metadata={
            "name": "OriginatingFinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )
    receiving_financial_institution: Optional[ReceivingFinancialInstitution] = field(
        default=None,
        metadata={
            "name": "ReceivingFinancialInstitution",
            "type": "Element",
            "required": True,
        }
    )
    list_of_financial_institutions: Optional[ListOfFinancialInstitutions] = field(
        default=None,
        metadata={
            "name": "ListOfFinancialInstitutions",
            "type": "Element",
        }
    )


@dataclass
class PaymentRequestAcknSummary:
    payment_request_summary: Optional[PaymentRequestSummary] = field(
        default=None,
        metadata={
            "name": "PaymentRequestSummary",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class PaymentRequestAcknDetail:
    confirmation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConfirmationID",
            "type": "Element",
            "required": True,
        }
    )
    payment_document_id: Optional[PaymentDocumentId] = field(
        default=None,
        metadata={
            "name": "PaymentDocumentID",
            "type": "Element",
            "required": True,
        }
    )
    payment_sequence_no: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentSequenceNo",
            "type": "Element",
        }
    )
    settlement_amount: Optional[SettlementAmount] = field(
        default=None,
        metadata={
            "name": "SettlementAmount",
            "type": "Element",
        }
    )
    debit_amount: Optional[DebitAmount] = field(
        default=None,
        metadata={
            "name": "DebitAmount",
            "type": "Element",
        }
    )
    credit_amount: Optional[CreditAmount] = field(
        default=None,
        metadata={
            "name": "CreditAmount",
            "type": "Element",
        }
    )
    payment_party: Optional[PaymentParty] = field(
        default=None,
        metadata={
            "name": "PaymentParty",
            "type": "Element",
        }
    )
    financial_institution_detail: Optional[FinancialInstitutionDetail] = field(
        default=None,
        metadata={
            "name": "FinancialInstitutionDetail",
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
    excpetion_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExcpetionNote",
            "type": "Element",
        }
    )
    payment_request_note: Optional[str] = field(
        default=None,
        metadata={
            "name": "PaymentRequestNote",
            "type": "Element",
        }
    )
    list_of_payment_exception: Optional[ListOfPaymentException] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentException",
            "type": "Element",
        }
    )
    encrypted_info: Optional[EncryptedInfo] = field(
        default=None,
        metadata={
            "name": "EncryptedInfo",
            "type": "Element",
        }
    )


@dataclass
class ListOfPaymentRequestAcknDetail:
    payment_request_ackn_detail: List[PaymentRequestAcknDetail] = field(
        default_factory=list,
        metadata={
            "name": "PaymentRequestAcknDetail",
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class PaymentRequestAcknowledgment:
    payment_request_ackn_header: Optional[PaymentRequestAcknHeader] = field(
        default=None,
        metadata={
            "name": "PaymentRequestAcknHeader",
            "type": "Element",
            "required": True,
        }
    )
    list_of_payment_request_ackn_detail: Optional[ListOfPaymentRequestAcknDetail] = field(
        default=None,
        metadata={
            "name": "ListOfPaymentRequestAcknDetail",
            "type": "Element",
            "required": True,
        }
    )
    payment_request_ackn_summary: Optional[PaymentRequestAcknSummary] = field(
        default=None,
        metadata={
            "name": "PaymentRequestAcknSummary",
            "type": "Element",
            "required": True,
        }
    )
