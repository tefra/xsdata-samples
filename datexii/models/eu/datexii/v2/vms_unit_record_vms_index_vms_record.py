from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.vms_record import VmsRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsUnitRecordVmsIndexVmsRecord:
    class Meta:
        name = "_VmsUnitRecordVmsIndexVmsRecord"

    vms_record: VmsRecord | None = field(
        default=None,
        metadata={
            "name": "vmsRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vms_index: int | None = field(
        default=None,
        metadata={
            "name": "vmsIndex",
            "type": "Attribute",
            "required": True,
        },
    )
