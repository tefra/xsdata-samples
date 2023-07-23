from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_vehicle_search_availability_rsp import BaseVehicleSearchAvailabilityRsp
from travelport.models.marketing_information_1 import MarketingInformation1

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleSearchAvailabilityRsp(BaseVehicleSearchAvailabilityRsp):
    """
    Parameters
    ----------
    marketing_information
        Marketing text or notices by Suppliers. 1P only.
    media_links_search_id
        Unique search id to retrieve the media links using
        VehicleMediaLinksReq.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    marketing_information: None | MarketingInformation1 = field(
        default=None,
        metadata={
            "name": "MarketingInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        }
    )
    media_links_search_id: None | str = field(
        default=None,
        metadata={
            "name": "MediaLinksSearchId",
            "type": "Attribute",
        }
    )
