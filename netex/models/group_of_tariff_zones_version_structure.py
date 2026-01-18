from __future__ import annotations

from dataclasses import dataclass, field

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfTariffZonesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfTariffZones_VersionStructure"

    members: None | TariffZoneRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
