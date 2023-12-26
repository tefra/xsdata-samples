from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.payment_address_2 import PaymentAddress2
from travelport.models.payment_phone_2 import PaymentPhone2
from travelport.models.type_date_options_2 import TypeDateOptions2
from travelport.models.type_key_element_2 import TypeKeyElement2
from travelport.models.type_payment_type_2 import TypePaymentType2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypePaymentDetailsHistory2(TypeKeyElement2):
    """
    History Element for Payment Details.

    Parameters
    ----------
    payment_phone
        Payment Phone
    payment_address
        Payment Address
    start_date
        Payment start date
    expiration_date
        Payment expiration date
    type_value
        Type of Payment
    issued_to_name
        Name of the issuee
    extended_payment
        Extended Payment Indicator
    payment_supplier
        The supplier code of the payment. (VI, CA, AX, etc)
    account_number
        Payment account number. (ie. Credit card number, etc)
    description
        Description of the Payment
    priority_order
        Priority order associated with this PaymentDetails.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "typePaymentDetailsHistory"

    payment_phone: None | PaymentPhone2 = field(
        default=None,
        metadata={
            "name": "PaymentPhone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    payment_address: None | PaymentAddress2 = field(
        default=None,
        metadata={
            "name": "PaymentAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    start_date: None | TypeDateOptions2 = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    expiration_date: None | TypeDateOptions2 = field(
        default=None,
        metadata={
            "name": "ExpirationDate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    type_value: None | TypePaymentType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    issued_to_name: None | str = field(
        default=None,
        metadata={
            "name": "IssuedToName",
            "type": "Attribute",
        },
    )
    extended_payment: None | bool = field(
        default=None,
        metadata={
            "name": "ExtendedPayment",
            "type": "Attribute",
        },
    )
    payment_supplier: None | str = field(
        default=None,
        metadata={
            "name": "PaymentSupplier",
            "type": "Attribute",
            "max_length": 6,
        },
    )
    account_number: None | str = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        },
    )
