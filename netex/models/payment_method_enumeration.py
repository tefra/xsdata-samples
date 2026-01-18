from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class PaymentMethodEnumeration(Enum):
    CASH = "cash"
    CASH_EXACT_CHANGE_ONLY = "cashExactChangeOnly"
    CASH_AND_CARD = "cashAndCard"
    COIN = "coin"
    BANKNOTE = "banknote"
    CHEQUE = "cheque"
    TRAVELLERS_CHEQUE = "travellersCheque"
    POSTAL_ORDER = "postalOrder"
    COMPANY_CHEQUE = "companyCheque"
    CREDIT_CARD = "creditCard"
    DEBIT_CARD = "debitCard"
    CARDS_ONLY = "cardsOnly"
    TRAVEL_CARD = "travelCard"
    CONTACTLESS_PAYMENT_CARD = "contactlessPaymentCard"
    CONTACTLESS_TRAVEL_CARD = "contactlessTravelCard"
    DIRECT_DEBIT = "directDebit"
    BANK_TRANSFER = "bankTransfer"
    EPAY_DEVICE = "epayDevice"
    EPAY_ACCOUNT = "epayAccount"
    SMS = "sms"
    MOBILE_PHONE = "mobilePhone"
    MOBILE_APP = "mobileApp"
    VOUCHER = "voucher"
    TOKEN = "token"
    WARRANT = "warrant"
    MILEAGE_POINTS = "mileagePoints"
    OTHER = "other"
