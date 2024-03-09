from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class MiscFormOfPayment1:
    """
    Miscellaneous Form of Payments.

    Parameters
    ----------
    credit_card_type
        The 2 letter credit/ debit card type or code which may not have been
        issued using the standard bank card types  - i.e. an airline issued
        card
    credit_card_number
    exp_date
        The Expiration date of this card in YYYY-MM format.
    text
        Any free form text which may be associated with the Miscellaneous
        Form of Payment. This text may be provider or GDS specific
    category
        Indicates what Category the Miscellaneous Form Of Payment is being
        used for payment - The category may vary by GDS. Allowable values
        are "Text" "Credit" "CreditCard" "FreeFormCreditCard" "Invoice"
        "NonRefundable" "MultipleReceivables" "Exchange" "Cash"
    acceptance_override
        Override airline restriction on the credit card.
    """

    class Meta:
        name = "MiscFormOfPayment"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    credit_card_type: None | str = field(
        default=None,
        metadata={
            "name": "CreditCardType",
            "type": "Attribute",
            "length": 2,
        },
    )
    credit_card_number: None | str = field(
        default=None,
        metadata={
            "name": "CreditCardNumber",
            "type": "Attribute",
            "min_length": 13,
            "max_length": 128,
        },
    )
    exp_date: None | XmlPeriod = field(
        default=None,
        metadata={
            "name": "ExpDate",
            "type": "Attribute",
        },
    )
    text: None | str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        },
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        },
    )
    acceptance_override: None | bool = field(
        default=None,
        metadata={
            "name": "AcceptanceOverride",
            "type": "Attribute",
        },
    )
