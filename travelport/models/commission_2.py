from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_trinary import TypeTrinary

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class Commission2:
    """
    Parameters
    ----------
    indicator
        Indicates if the Rate Plan is commissionable.True: Rate is
        commissionable.False: Rate is not commissionable.Unknown: Commission
        indicator is not returned by the hotel supplier (chain or property).
    percent
        The percentage applied to the commissionable amount to determine the
        payable commission amount.
    commission_amount
        The commission amount in the aggregator’s or supplier’s currency.
    approx_commission_amount
        The approximate commission amount in the agency’s provisioned or
        requested currency.
    commission_on_surcharges
        Commission on surcharges in the aggregator’s or supplier’s currency.
    approx_commission_on_surcharges
        The approximate commission on surcharges in the agency’s provisioned
        or requested currency.
    """

    class Meta:
        name = "Commission"
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    indicator: None | TypeTrinary = field(
        default=None,
        metadata={
            "name": "Indicator",
            "type": "Attribute",
        },
    )
    percent: None | str = field(
        default=None,
        metadata={
            "name": "Percent",
            "type": "Attribute",
        },
    )
    commission_amount: None | str = field(
        default=None,
        metadata={
            "name": "CommissionAmount",
            "type": "Attribute",
        },
    )
    approx_commission_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproxCommissionAmount",
            "type": "Attribute",
        },
    )
    commission_on_surcharges: None | str = field(
        default=None,
        metadata={
            "name": "CommissionOnSurcharges",
            "type": "Attribute",
        },
    )
    approx_commission_on_surcharges: None | str = field(
        default=None,
        metadata={
            "name": "ApproxCommissionOnSurcharges",
            "type": "Attribute",
        },
    )
