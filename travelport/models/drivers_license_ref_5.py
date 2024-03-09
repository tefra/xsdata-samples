from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass
class DriversLicenseRef5:
    class Meta:
        name = "DriversLicenseRef"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
