from __future__ import annotations

from dataclasses import dataclass, field

from .self_drive_submode_enumeration import SelfDriveSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SelfDriveSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SelfDriveSubmodeEnumeration = field(
        default=SelfDriveSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
