from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

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

    overtaking_width: Decimal | None = field(
        default=None,
        metadata={
            "name": "OvertakingWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overtaking_on_link_ref: LinkRefStructure | None = field(
        default=None,
        metadata={
            "name": "OvertakingOnLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    overtaking_at_point_ref: PointRefStructure | None = field(
        default=None,
        metadata={
            "name": "OvertakingAtPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overtaking_vehicle_type_ref: TransportTypeRefStructure | None = field(
        default=None,
        metadata={
            "name": "OvertakingVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    overtaken_vehicle_type_ref: TransportTypeRefStructure | None = field(
        default=None,
        metadata={
            "name": "OvertakenVehicleTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
