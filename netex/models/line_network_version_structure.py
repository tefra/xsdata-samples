from dataclasses import dataclass, field
from typing import Optional, Union
from .entity_in_version_structure import DataManagedObjectStructure
from .flexible_line_ref import FlexibleLineRef
from .group_of_lines_ref import GroupOfLinesRef
from .line_ref import LineRef
from .line_sections_rel_structure import LineSectionsRelStructure
from .multilingual_string import MultilingualString
from .network_ref import NetworkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LineNetworkVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "LineNetwork_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_lines_ref: Optional[Union[NetworkRef, GroupOfLinesRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    line_ref: Optional[Union[FlexibleLineRef, LineRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    sections: Optional[LineSectionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
