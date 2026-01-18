from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import VersionedChildStructure
from .fare_table_column_ref_structure import FareTableColumnRefStructure
from .fare_table_ref import FareTableRef
from .fare_table_row_ref_structure import FareTableRowRefStructure
from .multilingual_string import MultilingualString
from .standard_fare_table_ref import StandardFareTableRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommonCellVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "CommonCell_VersionedChildStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_table_ref: None | StandardFareTableRef | FareTableRef = field(
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
    column_ref: None | FareTableColumnRefStructure = field(
        default=None,
        metadata={
            "name": "ColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    row_ref: None | FareTableRowRefStructure = field(
        default=None,
        metadata={
            "name": "RowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
