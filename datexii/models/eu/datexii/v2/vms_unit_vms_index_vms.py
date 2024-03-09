from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.vms import Vms

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsUnitVmsIndexVms:
    class Meta:
        name = "_VmsUnitVmsIndexVms"

    vms: Optional[Vms] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    vms_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "vmsIndex",
            "type": "Attribute",
            "required": True,
        },
    )
