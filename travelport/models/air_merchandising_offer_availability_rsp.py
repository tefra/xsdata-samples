from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.air_solution import AirSolution
from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.embargo_list import EmbargoList
from travelport.models.optional_services import OptionalServices
from travelport.models.remark_1 import Remark1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirMerchandisingOfferAvailabilityRsp(BaseRsp1):
    """
    Contains the merchandising offerings for the given passenger and itinerary.

    Parameters
    ----------
    air_solution
        Provider: 1G,1V,1P,ACH.
    remark
        Provider: 1G,1V,1P,ACH.
    optional_services
    embargo_list
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    air_solution: None | AirSolution = field(
        default=None,
        metadata={
            "name": "AirSolution",
            "type": "Element",
            "required": True,
        }
    )
    remark: None | Remark1 = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    optional_services: None | OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
        }
    )
    embargo_list: None | EmbargoList = field(
        default=None,
        metadata={
            "name": "EmbargoList",
            "type": "Element",
        }
    )
