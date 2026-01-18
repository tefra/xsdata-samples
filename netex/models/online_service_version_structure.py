from dataclasses import dataclass, field

from .mobility_service_refs_rel_structure import (
    MobilityServiceRefsRelStructure,
)
from .mobility_service_version_structure import MobilityServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnlineServiceVersionStructure(MobilityServiceVersionStructure):
    class Meta:
        name = "OnlineService_VersionStructure"

    log_in_required: bool | None = field(
        default=None,
        metadata={
            "name": "LogInRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    proposing_services: MobilityServiceRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "proposingServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
