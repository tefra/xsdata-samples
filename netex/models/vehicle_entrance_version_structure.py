from dataclasses import dataclass, field
from typing import Optional

from .site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEntranceVersionStructure(SiteEntranceVersionStructure):
    class Meta:
        name = "VehicleEntrance_VersionStructure"

    public: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Public",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
