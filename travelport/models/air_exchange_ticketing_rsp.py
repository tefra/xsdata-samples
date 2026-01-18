from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_solution_changed_info import AirSolutionChangedInfo
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.detailed_billing_information import (
    DetailedBillingInformation,
)
from travelport.models.etr import Etr
from travelport.models.ticket_failure_info import TicketFailureInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class AirExchangeTicketingRsp(BaseRsp1):
    """
    Response to reissue a ticket.

    Parameters
    ----------
    air_solution_changed_info
    etr
        Provider 1G, 1V, 1P.
    ticket_failure_info
        Provider 1G, 1V, 1P.
    detailed_billing_information
        Providers 1G, 1V, 1P.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_solution_changed_info: None | AirSolutionChangedInfo = field(
        default=None,
        metadata={
            "name": "AirSolutionChangedInfo",
            "type": "Element",
        },
    )
    etr: None | Etr = field(
        default=None,
        metadata={
            "name": "ETR",
            "type": "Element",
        },
    )
    ticket_failure_info: None | TicketFailureInfo = field(
        default=None,
        metadata={
            "name": "TicketFailureInfo",
            "type": "Element",
        },
    )
    detailed_billing_information: None | DetailedBillingInformation = field(
        default=None,
        metadata={
            "name": "DetailedBillingInformation",
            "type": "Element",
        },
    )
