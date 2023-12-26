from dataclasses import dataclass, field
from typing import Optional
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Routing_VersionStructure"

    is_restricted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsRestricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    return_route_identical: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnRouteIdentical",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    forwards_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ForwardsOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cross_border: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CrossBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
