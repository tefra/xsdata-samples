from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.vms import Vms

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VmsUnitVmsIndexVms:
    class Meta:
        name = "_VmsUnitVmsIndexVms"

    vms: Vms = field(
        metadata={
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
