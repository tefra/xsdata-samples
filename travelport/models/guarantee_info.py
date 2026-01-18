from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.deposit_amount import DepositAmount
from travelport.models.guarantee_info_guarantee_type import (
    GuaranteeInfoGuaranteeType,
)
from travelport.models.guarantee_payment_type import GuaranteePaymentType

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass(kw_only=True)
class GuaranteeInfo:
    """
    Parameters
    ----------
    deposit_amount
        Amount required for deposit/prepayment
    deposit_nights
        Number of Nights required for deposit/prepayment
    deposit_percent
        Percentage of stay required for deposit/prepayment
    guarantee_payment_type
        Accepted payment types
    absolute_deadline
        Latest date/time when deposit/payment/guarantee is required.
    credentials_required
        Identification required at booking/checkin. Not supported by 1P.
    hold_time
        Expiration time for room reservation held without deposit/guarantee.
    guarantee_type
        Deposit, Guarantee, or Prepayment required to hold/book the room.
        Applicable only for HotelSupershopper, Hotel Details and Hotel
        rules.
    offset_time_unit
        The units of time, e.g: days, hours, etc that apply to the deadline.
        Enumerated values are “Year”, “Month”, “Day”, and “Hour”.
    offset_unit_multiplier
        The number of units of DeadlineTimeUnit.
    offset_drop_time
        An enumerated type indicating when the deadline drop time goes into
        effect. Enumerated values are “AfterBooking” and “BeforeArrival”.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    deposit_amount: None | DepositAmount = field(
        default=None,
        metadata={
            "name": "DepositAmount",
            "type": "Element",
        },
    )
    deposit_nights: None | int = field(
        default=None,
        metadata={
            "name": "DepositNights",
            "type": "Element",
        },
    )
    deposit_percent: None | int = field(
        default=None,
        metadata={
            "name": "DepositPercent",
            "type": "Element",
        },
    )
    guarantee_payment_type: list[GuaranteePaymentType] = field(
        default_factory=list,
        metadata={
            "name": "GuaranteePaymentType",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    absolute_deadline: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "AbsoluteDeadline",
            "type": "Attribute",
        },
    )
    credentials_required: None | bool = field(
        default=None,
        metadata={
            "name": "CredentialsRequired",
            "type": "Attribute",
        },
    )
    hold_time: None | str = field(
        default=None,
        metadata={
            "name": "HoldTime",
            "type": "Attribute",
        },
    )
    guarantee_type: None | GuaranteeInfoGuaranteeType = field(
        default=None,
        metadata={
            "name": "GuaranteeType",
            "type": "Attribute",
        },
    )
    offset_time_unit: None | str = field(
        default=None,
        metadata={
            "name": "OffsetTimeUnit",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        },
    )
    offset_unit_multiplier: None | int = field(
        default=None,
        metadata={
            "name": "OffsetUnitMultiplier",
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 999,
        },
    )
    offset_drop_time: None | str = field(
        default=None,
        metadata={
            "name": "OffsetDropTime",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        },
    )
