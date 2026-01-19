from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .group_of_distance_matrix_elements_ref import (
    GroupOfDistanceMatrixElementsRef,
)
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .parking_tariff_ref import ParkingTariffRef
from .tariff_ref import TariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsedInRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "usedInRefs_RelStructure"

    choice: Sequence[
        ParkingTariffRef
        | TariffRef
        | GroupOfDistanceMatrixElementsRef
        | GroupOfSalesOfferPackagesRef
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
                {
                    "name": "GroupOfDistanceMatrixElementsRef",
                    "type": GroupOfDistanceMatrixElementsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSalesOfferPackagesRef",
                    "type": GroupOfSalesOfferPackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
