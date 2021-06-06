from dataclasses import dataclass, field
from typing import List
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .tariff_zone_ref_1 import TariffZoneRef1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "tariffZoneRefs_RelStructure"

    tariff_zone_ref: List[TariffZoneRef1] = field(
        default_factory=list,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
