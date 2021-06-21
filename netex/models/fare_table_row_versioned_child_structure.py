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
class FareTableRowVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "FareTableRow_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
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
                    "name": "rows",
                    "type": Type["FareTableRowsRelStructure"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 2,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class FareTableRow(FareTableRowVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class FareTableRowsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareTableRows_RelStructure"

    fare_table_row: List[FareTableRow] = field(
        default_factory=list,
        metadata={
            "name": "FareTableRow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
