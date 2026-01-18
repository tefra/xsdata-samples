from __future__ import annotations

from dataclasses import dataclass

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceGroupAbstract(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "PriceGroup_"
        namespace = "http://www.netex.org.uk/netex"
