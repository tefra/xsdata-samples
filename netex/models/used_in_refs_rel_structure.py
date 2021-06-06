from dataclasses import dataclass, field
from typing import List
from .group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .parking_tariff_ref import ParkingTariffRef
from .tariff_ref import TariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UsedInRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "usedInRefs_RelStructure"

    parking_tariff_ref: List[ParkingTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_ref: List[TariffRef] = field(
        default_factory=list,
        metadata={
            "name": "TariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distance_matrix_elements_ref: List[GroupOfDistanceMatrixElementsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_sales_offer_packages_ref: List[GroupOfSalesOfferPackagesRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
