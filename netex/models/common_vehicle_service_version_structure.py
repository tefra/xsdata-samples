from dataclasses import dataclass, field
from typing import Optional

from .mobility_service_version_structure import MobilityServiceVersionStructure
from .online_service_refs_rel_structure import OnlineServiceRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonVehicleServiceVersionStructure(MobilityServiceVersionStructure):
    class Meta:
        name = "CommonVehicleService_VersionStructure"

    booking_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BookingRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    registration_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RegistrationRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    proposed_by_services: Optional[OnlineServiceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "proposedByServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
