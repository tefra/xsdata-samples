from dataclasses import dataclass, field
from typing import Optional
from netex.models.alternative_texts_rel_structure import (
    DataManagedObjectStructure,
    ValidityConditionsRelStructure,
)
from netex.models.codespaces_rel_structure import CodespacesRelStructure
from netex.models.layer_refs_rel_structure import LayerRefsRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.traces_rel_structure import TracesRelStructure
from netex.models.type_of_frame_ref import TypeOfFrameRef
from netex.models.version_frame_defaults_structure import VersionFrameDefaultsStructure
from netex.models.version_frame_refs_rel_structure import VersionFrameRefsRelStructure
from netex.models.version_ref_structure import VersionRefStructure
from netex.models.versions_rel_structure import VersionsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionFrameVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VersionFrame_VersionStructure"

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
    type_of_frame_ref: Optional[TypeOfFrameRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    baseline_version_frame_ref: Optional[VersionRefStructure] = field(
        default=None,
        metadata={
            "name": "BaselineVersionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    codespaces: Optional[CodespacesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frame_defaults: Optional[VersionFrameDefaultsStructure] = field(
        default=None,
        metadata={
            "name": "FrameDefaults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    versions: Optional[VersionsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prerequisites: Optional[VersionFrameRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    traces: Optional[TracesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    content_validity_conditions: Optional[ValidityConditionsRelStructure] = field(
        default=None,
        metadata={
            "name": "contentValidityConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    layers: Optional[LayerRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
