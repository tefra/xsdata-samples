from dataclasses import dataclass, field
from typing import Optional

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTariffZonesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfTariffZones_VersionStructure"

    members: Optional[TariffZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
