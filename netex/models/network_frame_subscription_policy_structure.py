from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkFrameSubscriptionPolicyStructure:
    incremental_updates: None | bool = field(
        default=None,
        metadata={
            "name": "IncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
