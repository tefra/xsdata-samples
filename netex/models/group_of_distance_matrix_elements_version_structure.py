from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .distance_matrix_element_prices_rel_structure import (
    DistanceMatrixElementPricesRelStructure,
)
from .distance_matrix_elements_rel_structure import (
    DistanceMatrixElementsRelStructure,
)
from .geographical_structure_factors_rel_structure import (
    GeographicalStructureFactorsRelStructure,
)
from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .priceable_object_version_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfDistanceMatrixElementsVersionStructure(
    GroupOfEntitiesVersionStructure
):
    class Meta:
        name = "GroupOfDistanceMatrixElements_VersionStructure"

    use_to_exclude: bool | None = field(
        default=None,
        metadata={
            "name": "UseToExclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_groups: PriceGroupsRelStructure | None = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_tables: FareTablesRelStructure | None = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Decimal | None = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    structure_factors: GeographicalStructureFactorsRelStructure | None = (
        field(
            default=None,
            metadata={
                "name": "structureFactors",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    notice_assignments: NoticeAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: DistanceMatrixElementsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: DistanceMatrixElementPricesRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
