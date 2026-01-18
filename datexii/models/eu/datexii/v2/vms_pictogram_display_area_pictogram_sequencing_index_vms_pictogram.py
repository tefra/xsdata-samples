from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.vms_pictogram import VmsPictogram

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VmsPictogramDisplayAreaPictogramSequencingIndexVmsPictogram:
    class Meta:
        name = "_VmsPictogramDisplayAreaPictogramSequencingIndexVmsPictogram"

    vms_pictogram: VmsPictogram = field(
        metadata={
            "name": "vmsPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    pictogram_sequencing_index: int = field(
        metadata={
            "name": "pictogramSequencingIndex",
            "type": "Attribute",
            "required": True,
        }
    )
