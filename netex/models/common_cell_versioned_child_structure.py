from dataclasses import dataclass, field
from typing import Optional, Union

from .entity_in_version_structure import VersionedChildStructure
from .fare_table_column_ref_structure import FareTableColumnRefStructure
from .fare_table_ref import FareTableRef
from .fare_table_row_ref_structure import FareTableRowRefStructure
from .multilingual_string import MultilingualString
from .standard_fare_table_ref import StandardFareTableRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CommonCellVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "CommonCell_VersionedChildStructure"

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
    column_ref: FareTableColumnRefStructure | None = field(
        default=None,
        metadata={
            "name": "ColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    row_ref: FareTableRowRefStructure | None = field(
        default=None,
        metadata={
            "name": "RowRef",
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
