from dataclasses import dataclass, field
from typing import List
from netex.models.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.models.parking_tariff_ref import ParkingTariffRef
from netex.models.tariff_ref import TariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "tariffRefs_RelStructure"

    parking_tariff_ref: List[ParkingTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    tariff_ref: List[TariffRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
