from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlPeriod
from travelport.models.phone_number_3 import PhoneNumber3
from travelport.models.type_structured_address_3 import TypeStructuredAddress3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class TypePaymentCard3:
    """
    Container for all credit and debit card information.

    Parameters
    ----------
    phone_number
    billing_address
        The address to where the billing statements for this card are sent.
        Used for address verification purposes.
    type_value
        The 2 letter credit/ debit card type.
    number
    exp_date
        The Expiration date of this card in YYYY-MM format.
    name
        The name as it appears on the card.
    cvv
        Card Verification Code
    approval_code
        This code is required for an authorization process from the Credit
        Card company directly,required for some of the CCH carriers.This
        attribute is also used for EMD retrieve and issuance transactions.
    """
    class Meta:
        name = "typePaymentCard"

    phone_number: None | PhoneNumber3 = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        }
    )
    billing_address: None | TypeStructuredAddress3 = field(
        default=None,
        metadata={
            "name": "BillingAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v32_0",
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 2,
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
    exp_date: None | XmlPeriod = field(
        default=None,
        metadata={
            "name": "ExpDate",
            "type": "Attribute",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "max_length": 128,
        }
    )
    cvv: None | str = field(
        default=None,
        metadata={
            "name": "CVV",
            "type": "Attribute",
            "max_length": 4,
        }
    )
    approval_code: None | str = field(
        default=None,
        metadata={
            "name": "ApprovalCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
