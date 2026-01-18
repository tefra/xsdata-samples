from dataclasses import dataclass, field
from typing import Optional

from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RoutingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Routing_VersionStructure"

    is_restricted: bool | None = field(
        default=None,
        metadata={
            "name": "IsRestricted",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    return_route_identical: bool | None = field(
        default=None,
        metadata={
            "name": "ReturnRouteIdentical",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    forwards_only: bool | None = field(
        default=None,
        metadata={
            "name": "ForwardsOnly",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    cross_border: bool | None = field(
        default=None,
        metadata={
            "name": "CrossBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
