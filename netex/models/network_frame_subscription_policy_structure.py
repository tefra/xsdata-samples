from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkFrameSubscriptionPolicyStructure:
    incremental_updates: bool | None = field(
        default=None,
        metadata={
            "name": "IncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
