from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_vehicle_search_availability_req import (
    BaseVehicleSearchAvailabilityReq,
)

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class VehicleSearchAvailabilityReq(BaseVehicleSearchAvailabilityReq):
    """
    Parameters
    ----------
    return_media_links
        Set indicator to true to retrieve the media links. Default False
    return_all_rates
        Default, false.  If true, all available rates are returned if
        applicable for the specified provider.
    return_approximate_total
        Applies only if ReturnAllRates is set to true.  If false, base rates
        are returned. If true, approximate total rates are returned as
        supported by the car vendor.  Default is false.
    return_extra_rate_info
        Applies only if ReturnAllRates is set to true. If false, basic rate
        details are returned. If true, additional rate information is
        returned.  Default is false.
    policy_reference
        This attribute will be used to pass in a value on the request which
        would be used to link to a ‘Policy Group’ in a policy engine
        external to UAPI.
    return_inclusion_details
        Set indicator to true to retrieve the Rate Inclusion Details.
        Default False
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    return_media_links: bool = field(
        default=False,
        metadata={
            "name": "ReturnMediaLinks",
            "type": "Attribute",
        },
    )
    return_all_rates: bool = field(
        default=False,
        metadata={
            "name": "ReturnAllRates",
            "type": "Attribute",
        },
    )
    return_approximate_total: bool = field(
        default=False,
        metadata={
            "name": "ReturnApproximateTotal",
            "type": "Attribute",
        },
    )
    return_extra_rate_info: bool = field(
        default=False,
        metadata={
            "name": "ReturnExtraRateInfo",
            "type": "Attribute",
        },
    )
    policy_reference: None | str = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 20,
        },
    )
    return_inclusion_details: bool = field(
        default=False,
        metadata={
            "name": "ReturnInclusionDetails",
            "type": "Attribute",
        },
    )
