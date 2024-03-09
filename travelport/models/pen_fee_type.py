from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PenFeeType:
    """
    Parameters
    ----------
    dep_required
        Deposit required. True if require. False if not required.
    dep_non_ref
        Deposit non-refundable.  True is  non-refundanbe.  False is
        refundable.
    tk_non_ref
        Ticket non-refundable. True if non-refundanbe. False if refundable.
    air_vfee
        Carrier fee. True if carrier fee is assessed should passenger for
        complete all conditions for travel at fare. False if it does not
        exist.
    cancellation
        Cancellation. True if subject to penalty. False if no penalty.
    fail_confirm_space
        Failure to confirm space. True if subject to penalty if seats are
        not confirmed. False if subject to penalty if seats are confirmed.
    itin_chg
        Subject to penalty if Itinerary is changed requiring reissue of
        ticket. True if subject to penalty. False if no penalty if reissue
        required.
    replace_tk
        Replace ticket. True if subject to penalty, if replacement of lost
        ticket / exchange order. False if no penalty, if replacement of lost
        ticket or exchange order.
    applicable
        Applicable. True if amount specified is applicable. Flase if amount
        specified is not applicable.
    applicable_to
        Applicable to penalty or deposit. True if amount specified applies
        to penalty. False if amount specified applies to deposit.
    amt
        Amount of penalty.  If XXX.XX then it is an amount.  If it is XX
        then is is a percenatge.  Eg 100.00 or 000100.
    type_value
        Type of penalty.  If it is D then dollar.  If it is P then
        percentage.
    currency
        Currency code of penalty (e.g. USD).
    """

    dep_required: None | bool = field(
        default=None,
        metadata={
            "name": "DepRequired",
            "type": "Attribute",
        },
    )
    dep_non_ref: None | bool = field(
        default=None,
        metadata={
            "name": "DepNonRef",
            "type": "Attribute",
        },
    )
    tk_non_ref: None | bool = field(
        default=None,
        metadata={
            "name": "TkNonRef",
            "type": "Attribute",
        },
    )
    air_vfee: None | bool = field(
        default=None,
        metadata={
            "name": "AirVFee",
            "type": "Attribute",
        },
    )
    cancellation: None | bool = field(
        default=None,
        metadata={
            "name": "Cancellation",
            "type": "Attribute",
        },
    )
    fail_confirm_space: None | bool = field(
        default=None,
        metadata={
            "name": "FailConfirmSpace",
            "type": "Attribute",
        },
    )
    itin_chg: None | bool = field(
        default=None,
        metadata={
            "name": "ItinChg",
            "type": "Attribute",
        },
    )
    replace_tk: None | bool = field(
        default=None,
        metadata={
            "name": "ReplaceTk",
            "type": "Attribute",
        },
    )
    applicable: None | bool = field(
        default=None,
        metadata={
            "name": "Applicable",
            "type": "Attribute",
        },
    )
    applicable_to: None | bool = field(
        default=None,
        metadata={
            "name": "ApplicableTo",
            "type": "Attribute",
        },
    )
    amt: None | Decimal = field(
        default=None,
        metadata={
            "name": "Amt",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Attribute",
        },
    )
