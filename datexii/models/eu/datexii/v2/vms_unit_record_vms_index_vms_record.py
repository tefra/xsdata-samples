from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.vms_record import VmsRecord

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VmsUnitRecordVmsIndexVmsRecord:
    class Meta:
        name = "_VmsUnitRecordVmsIndexVmsRecord"

    vms_record: VmsRecord = field(
        metadata={
            "name": "vmsRecord",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    vms_index: int = field(
        metadata={
            "name": "vmsIndex",
            "type": "Attribute",
            "required": True,
        }
    )
