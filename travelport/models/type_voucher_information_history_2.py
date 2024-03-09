from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_voucher_type_5 import TypeVoucherType5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeVoucherInformationHistory2:
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
        name = "typeVoucherInformationHistory"

    voucher_type: None | TypeVoucherType5 = field(
        default=None,
        metadata={
            "name": "VoucherType",
            "type": "Attribute",
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
