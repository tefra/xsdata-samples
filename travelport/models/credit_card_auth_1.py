from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class CreditCardAuth1:
    """The result of a Credit Auth Request.

    Will contain all the authorization info and result codes.

    Parameters
    ----------
    key
    payment_ref
    trans_id
        The transaction id from the credit processing system
    number
    amount
        The amount that was authorized.
    auth_code
        The authorization code to confirm card acceptance
    auth_result_code
        The result code of the authorization command.
    avsresult_code
        The address verification result code (if AVS was requested)
    message
        The message explains the result of the authorization command.
    provider_reservation_info_ref
    form_of_payment_ref
    """
    class Meta:
        name = "CreditCardAuth"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    payment_ref: None | str = field(
        default=None,
        metadata={
            "name": "PaymentRef",
            "type": "Attribute",
        }
    )
    trans_id: None | str = field(
        default=None,
        metadata={
            "name": "TransId",
            "type": "Attribute",
        }
    )
    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 13,
            "max_length": 128,
        }
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    auth_code: None | str = field(
        default=None,
        metadata={
            "name": "AuthCode",
            "type": "Attribute",
        }
    )
    auth_result_code: None | str = field(
        default=None,
        metadata={
            "name": "AuthResultCode",
            "type": "Attribute",
            "required": True,
        }
    )
    avsresult_code: None | str = field(
        default=None,
        metadata={
            "name": "AVSResultCode",
            "type": "Attribute",
        }
    )
    message: None | str = field(
        default=None,
        metadata={
            "name": "Message",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    form_of_payment_ref: None | str = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Attribute",
        }
    )
