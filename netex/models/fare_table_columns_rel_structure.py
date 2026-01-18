from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Any, Optional, Union

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
class FareTableColumnsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "fareTableColumns_RelStructure"

    fare_table_column: Iterable[FareTableColumn] = field(
        default_factory=list,
        metadata={
            "name": "FareTableColumn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )


@dataclass
class FareTableColumnVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "FareTableColumn_VersionedChildStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_table_ref: StandardFareTableRef | FareTableRef | None = (
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
    notice_assignments: NoticeAssignmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    representing: ObjectRefsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    columns: FareTableColumnsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FareTableColumn(FareTableColumnVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
