from __future__ import annotations

from dataclasses import dataclass, field

from .group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from .object_refs_rel_structure import ObjectRefsRelStructure
from .version_frame_refs_rel_structure import VersionFrameRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LayerVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "Layer_VersionStructure"

    location_system: None | str = field(
        default=None,
        metadata={
            "name": "LocationSystem",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    version_frames: None | VersionFrameRefsRelStructure = field(
        default=None,
        metadata={
            "name": "versionFrames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: None | ObjectRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
