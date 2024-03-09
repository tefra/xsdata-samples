from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class Penalty1:
    """
    Exchange penalty information.
    """

    class Meta:
        name = "Penalty"
        namespace = "http://www.travelport.com/schema/common_v52_0"

    cancel_refund: None | bool = field(
        default=None,
        metadata={
            "name": "CancelRefund",
            "type": "Attribute",
        },
    )
    non_refundable: None | bool = field(
        default=None,
        metadata={
            "name": "NonRefundable",
            "type": "Attribute",
        },
    )
    non_exchangeable: None | bool = field(
        default=None,
        metadata={
            "name": "NonExchangeable",
            "type": "Attribute",
        },
    )
    cancelation_penalty: None | bool = field(
        default=None,
        metadata={
            "name": "CancelationPenalty",
            "type": "Attribute",
        },
    )
    reissue_penalty: None | bool = field(
        default=None,
        metadata={
            "name": "ReissuePenalty",
            "type": "Attribute",
        },
    )
    non_reissue_penalty: None | bool = field(
        default=None,
        metadata={
            "name": "NonReissuePenalty",
            "type": "Attribute",
        },
    )
    ticket_refund_penalty: None | bool = field(
        default=None,
        metadata={
            "name": "TicketRefundPenalty",
            "type": "Attribute",
        },
    )
    charge_applicable: None | bool = field(
        default=None,
        metadata={
            "name": "ChargeApplicable",
            "type": "Attribute",
        },
    )
    charge_portion: None | bool = field(
        default=None,
        metadata={
            "name": "ChargePortion",
            "type": "Attribute",
        },
    )
    penalty_amount: None | str = field(
        default=None,
        metadata={
            "name": "PenaltyAmount",
            "type": "Attribute",
        },
    )
