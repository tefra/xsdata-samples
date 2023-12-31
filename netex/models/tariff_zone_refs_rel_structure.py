from dataclasses import dataclass, field
from typing import List, Union
from .fare_zone_ref import FareZoneRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .tariff_zone_ref import TariffZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffZoneRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "tariffZoneRefs_RelStructure"

    tariff_zone_ref: List[Union[FareZoneRef, TariffZoneRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareZoneRef",
                    "type": FareZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffZoneRef",
                    "type": TariffZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
