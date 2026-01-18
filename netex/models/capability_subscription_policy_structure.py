from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitySubscriptionPolicyStructure:
    has_incremental_updates: None | bool = field(
        default=None,
        metadata={
            "name": "HasIncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    has_change_sensitivity: None | bool = field(
        default=None,
        metadata={
            "name": "HasChangeSensitivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
