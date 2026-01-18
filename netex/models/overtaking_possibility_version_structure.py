from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .link_ref_structure import LinkRefStructure
from .network_restriction_version_structure import (
    NetworkRestrictionVersionStructure,
)
from .point_ref_structure import PointRefStructure
from .transport_type_ref_structure import TransportTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OvertakingPossibilityVersionStructure(
    NetworkRestrictionVersionStructure
):
    class Meta:
        name = "OvertakingPossibility_VersionStructure"

    overtaking_width: None | Decimal = field(
        default=None,
        metadata={
            "name": "OvertakingWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overtaking_on_link_ref: None | LinkRefStructure = field(
        default=None,
        metadata={
            "name": "OvertakingOnLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    overtaking_at_point_ref: None | PointRefStructure = field(
        default=None,
        metadata={
            "name": "OvertakingAtPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overtaking_vehicle_type_ref: None | TransportTypeRefStructure = field(
        default=None,
        metadata={
            "name": "OvertakingVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overtaken_vehicle_type_ref: None | TransportTypeRefStructure = field(
        default=None,
        metadata={
            "name": "OvertakenVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
