from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_voucher_type_2 import TypeVoucherType2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class TypeVoucherInformation2:
    """
    Information pertaining to the payment of a Vehicle Rental.

    Parameters
    ----------
    voucher_type
        Specifies if the Voucher is for Full Credit or a Group/Day or a
        Monetary Amount.
    amount
        Amount associated with the Voucher.
    confirmation_number
        Confirmation from the vendor for the voucher
    account_name
        Associated account name for the voucher
    """

    class Meta:
        name = "typeVoucherInformation"

    voucher_type: None | TypeVoucherType2 = field(
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
