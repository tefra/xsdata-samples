from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from travelport.models.type_trinary import TypeTrinary

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class CancelInfo:
    """Returns cancellation information for certain hotel returned in response.

    This information is available through GDS transactions

    Parameters
    ----------
    cancellation_policy
        Return cancellation policy text by the aggregator.
    text
        The informational text provided by the supplier to cancel the
        booking, if @Method="INFO". For all other values of @Method, Text is
        not returned.
    non_refundable_stay_indicator
        True if Deposit or Payment is non-refundable
    cancel_deadline
        Last date/time the reservation can be canceled without penalty.
    tax_inclusive
        Indicates whether or not the Penalty amount includes taxes.
    fee_inclusive
        Indicates whether or not the Penalty amount includes fees.
    cancel_penalty_amount
        This will contain the cancellation penalty amount.
    number_of_nights
        This will contain the number of nights that will be assessed as the
        cancelation penalty.
    cancel_penalty_percent
        This will contain the cancellation penalty expressed as a
        percentage.
    cancel_penalty_percent_applies_to
        This will contain the cost qualifier that explains what the
        percentage is applied to in order to calculate the cancel penalty.
    method
        Cancellation method, either "API", "URL", "INFO", or "NONE".
    supported
        If true, the booking can be canceled. If false, the booking cannot
        be canceled.
    url
        The URL provided by the supplier to cancel the booking, if
        @Method="URL". For all other values of @Method, @URL is not
        returned.
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

    cancellation_policy: None | str = field(
        default=None,
        metadata={
            "name": "CancellationPolicy",
            "type": "Element",
        },
    )
    text: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Text",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    non_refundable_stay_indicator: None | TypeTrinary = field(
        default=None,
        metadata={
            "name": "NonRefundableStayIndicator",
            "type": "Attribute",
        },
    )
    cancel_deadline: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CancelDeadline",
            "type": "Attribute",
        },
    )
    tax_inclusive: None | bool = field(
        default=None,
        metadata={
            "name": "TaxInclusive",
            "type": "Attribute",
        },
    )
    fee_inclusive: None | bool = field(
        default=None,
        metadata={
            "name": "FeeInclusive",
            "type": "Attribute",
        },
    )
    cancel_penalty_amount: None | str = field(
        default=None,
        metadata={
            "name": "CancelPenaltyAmount",
            "type": "Attribute",
        },
    )
    number_of_nights: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfNights",
            "type": "Attribute",
        },
    )
    cancel_penalty_percent: None | float = field(
        default=None,
        metadata={
            "name": "CancelPenaltyPercent",
            "type": "Attribute",
        },
    )
    cancel_penalty_percent_applies_to: None | str = field(
        default=None,
        metadata={
            "name": "CancelPenaltyPercentAppliesTo",
            "type": "Attribute",
        },
    )
    method: None | str = field(
        default=None,
        metadata={
            "name": "Method",
            "type": "Attribute",
        },
    )
    supported: None | bool = field(
        default=None,
        metadata={
            "name": "Supported",
            "type": "Attribute",
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "name": "URL",
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
