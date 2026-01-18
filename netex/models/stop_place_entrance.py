from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .stop_place_entrance_version_structure import (
    StopPlaceEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceEntrance(StopPlaceEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
