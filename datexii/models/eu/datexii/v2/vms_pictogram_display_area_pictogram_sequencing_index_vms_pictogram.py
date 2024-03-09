from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.vms_pictogram import VmsPictogram

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsPictogramDisplayAreaPictogramSequencingIndexVmsPictogram:
    class Meta:
        name = "_VmsPictogramDisplayAreaPictogramSequencingIndexVmsPictogram"

    vms_pictogram: Optional[VmsPictogram] = field(
        default=None,
        metadata={
            "name": "vmsPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    pictogram_sequencing_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramSequencingIndex",
            "type": "Attribute",
            "required": True,
        },
    )
