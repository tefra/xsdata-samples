from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class CapabilitySubscriptionPolicyStructure:
    has_incremental_updates: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasIncrementalUpdates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    has_change_sensitivity: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasChangeSensitivity",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
