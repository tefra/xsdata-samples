from dataclasses import dataclass, field
from typing import Any, List, Optional, Union

from .entity_in_version_structure import VersionedChildStructure
from .fare_table_ref import FareTableRef
from .multilingual_string import MultilingualString
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .object_refs_rel_structure import ObjectRefsRelStructure
from .standard_fare_table_ref import StandardFareTableRef
from .strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareTableRowsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareTableRows_RelStructure"

    fare_table_row: List["FareTableRow"] = field(
        default_factory=list,
        metadata={
            "name": "FareTableRow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )


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
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_table_ref: Optional[Union[StandardFareTableRef, FareTableRef]] = (
        field(
            default=None,
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
                ),
            },
        )
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    representing: Optional[ObjectRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rows: Optional[FareTableRowsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FareTableRow(FareTableRowVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
