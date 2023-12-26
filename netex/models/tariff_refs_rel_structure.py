from dataclasses import dataclass, field
from typing import List, Union
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .parking_tariff_ref import ParkingTariffRef
from .tariff_ref import TariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "tariffRefs_RelStructure"

    parking_tariff_ref_or_tariff_ref: List[
        Union[ParkingTariffRef, TariffRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffRef",
                    "type": TariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
