from __future__ import annotations

from dataclasses import dataclass, field

from .codespaces_rel_structure import CodespacesRelStructure
from .entity_in_version_structure import (
    DataManagedObjectStructure,
    ValidityConditionsRelStructure,
)
from .layer_refs_rel_structure import LayerRefsRelStructure
from .multilingual_string import MultilingualString
from .traces_rel_structure import TracesRelStructure
from .type_of_frame_ref import TypeOfFrameRef
from .version_frame_defaults_structure import VersionFrameDefaultsStructure
from .version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from .version_ref_structure import VersionRefStructure
from .versions_rel_structure import VersionsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionFrameVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VersionFrame_VersionStructure"

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
    type_of_frame_ref: None | TypeOfFrameRef = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    baseline_version_frame_ref: None | VersionRefStructure = field(
        default=None,
        metadata={
            "name": "BaselineVersionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    codespaces: None | CodespacesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    frame_defaults: None | VersionFrameDefaultsStructure = field(
        default=None,
        metadata={
            "name": "FrameDefaults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    versions: None | VersionsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prerequisites: None | VersionFrameRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    traces: None | TracesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    content_validity_conditions: None | ValidityConditionsRelStructure = field(
        default=None,
        metadata={
            "name": "contentValidityConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    layers: None | LayerRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
