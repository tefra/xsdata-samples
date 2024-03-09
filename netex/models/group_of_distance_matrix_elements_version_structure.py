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

    use_to_exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseToExclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    structure_factors: Optional[
        GeographicalStructureFactorsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "structureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[DistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[DistanceMatrixElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
