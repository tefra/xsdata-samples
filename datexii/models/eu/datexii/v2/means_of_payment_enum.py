from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class MeansOfPaymentEnum(Enum):
    """
    Means of payment.

    :cvar PAYMENT_CARD: Payment by electronic card(s). Use
        'AcceptedPaymentCards' resp. 'UsedPaymentCard' to specify them
        more exactly.
    :cvar CASH: Cash payment.
    :cvar CASH_COINS_ONLY: Cash payment with coins only.
    :cvar DIRECT_CASH_TRANSFER: Direct cash transfer.
    :cvar ELECTRONIC_SETTLEMENT: Electronic settlement; includes on
        board units.
    :cvar RFID: RFID.
    :cvar MOBILE_APP: Payment method using an app on a smartphone.
    :cvar PAY_BY_SMS: Payment by SMS. The telephone number can be
        specified by 'paymentAdditionalDescription'.
    :cvar MOBILE_PHONE: A payment method using a mobile phone but
        without an app or SMS, for instance by calling a number.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other.
    """
    PAYMENT_CARD = "paymentCard"
    CASH = "cash"
    CASH_COINS_ONLY = "cashCoinsOnly"
    DIRECT_CASH_TRANSFER = "directCashTransfer"
    ELECTRONIC_SETTLEMENT = "electronicSettlement"
    RFID = "rfid"
    MOBILE_APP = "mobileApp"
    PAY_BY_SMS = "payBySMS"
    MOBILE_PHONE = "mobilePhone"
    UNKNOWN = "unknown"
    OTHER = "other"
