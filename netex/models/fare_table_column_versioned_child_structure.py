from dataclasses import dataclass, field
from typing import List, Optional, Type
from .alternative_texts_rel_structure import VersionedChildStructure
from .fare_table_ref import FareTableRef
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .object_refs_rel_structure import ObjectRefsRelStructure
from .standard_fare_table_ref import StandardFareTableRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareTableColumnVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "FareTableColumn_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "noticeAssignments",
                    "type": NoticeAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "representing",
                    "type": ObjectRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "columns",
                    "type": Type["FareTableColumnsRelStructure"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 6,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FareTableColumn(FareTableColumnVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class FareTableColumnsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareTableColumns_RelStructure"

    fare_table_column: List[FareTableColumn] = field(
        default_factory=list,
        metadata={
            "name": "FareTableColumn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
