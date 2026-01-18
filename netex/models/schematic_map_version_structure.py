from __future__ import annotations

from dataclasses import dataclass, field

from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .schematic_map_members_rel_structure import (
    SchematicMapMembersRelStructure,
)
from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SchematicMapVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "SchematicMap_VersionStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    image_uri: None | str = field(
        default=None,
        metadata={
            "name": "ImageUri",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    depicted_object_ref: None | VersionOfObjectRefStructure = field(
        default=None,
        metadata={
            "name": "DepictedObjectRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: None | SchematicMapMembersRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
