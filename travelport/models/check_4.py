from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class Check4:
    """
    Check Form of Payment.

    Parameters
    ----------
    micrnumber
        Magnetic Ink Character Reader Number of check.
    routing_number
        The bank routing number of the check.
    account_number
        The account number of the check
    check_number
        The sequential check number of the check.
    """

    class Meta:
        name = "Check"
        namespace = "http://www.travelport.com/schema/common_v33_0"

    micrnumber: None | str = field(
        default=None,
        metadata={
            "name": "MICRNumber",
            "type": "Attribute",
            "max_length": 29,
        },
    )
    routing_number: None | str = field(
        default=None,
        metadata={
            "name": "RoutingNumber",
            "type": "Attribute",
        },
    )
    account_number: None | str = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Attribute",
        },
    )
    check_number: None | str = field(
        default=None,
        metadata={
            "name": "CheckNumber",
            "type": "Attribute",
        },
    )
