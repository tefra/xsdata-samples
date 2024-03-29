from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_voucher_type_1 import TypeVoucherType1

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class TypeVoucherInformation1:
    """
    Information pertaining to the payment of a Vehicle Rental.

    Parameters
    ----------
    voucher_type
        Specifies if the Voucher is for Full Credit or a Group/Day or a
        Monetary Amount or RegularVoucher.
    amount
        Amount associated with the Voucher.
    confirmation_number
        Confirmation from the vendor for the voucher
    account_name
        Associated account name for the voucher
    number
        To advise car associates of the voucher number and store in the car
        segment. It is required when VoucherType selected as
        "RegularVoucher" for 1P only.
    """

    class Meta:
        name = "typeVoucherInformation"

    voucher_type: None | TypeVoucherType1 = field(
        default=None,
        metadata={
            "name": "VoucherType",
            "type": "Attribute",
            "required": True,
        },
    )
    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Attribute",
        },
    )
    confirmation_number: None | str = field(
        default=None,
        metadata={
            "name": "ConfirmationNumber",
            "type": "Attribute",
        },
    )
    account_name: None | str = field(
        default=None,
        metadata={
            "name": "AccountName",
            "type": "Attribute",
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
