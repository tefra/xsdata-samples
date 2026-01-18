from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .abstract_capabilities_structure import AbstractCapabilitiesStructure
from .data_object_capability_request_policy_structure import (
    DataObjectCapabilityRequestPolicyStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: DataObjectServiceCapabilitiesStructure.TopicFiltering | None = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_policy: DataObjectCapabilityRequestPolicyStructure | None = (
        field(
            default=None,
            metadata={
                "name": "RequestPolicy",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    subscription_policy: DataObjectServiceCapabilitiesStructure.SubscriptionPolicy | None = field(
        default=None,
        metadata={
            "name": "SubscriptionPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    response_features: object | None = field(
        default=None,
        metadata={
            "name": "ResponseFeatures",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass
    class TopicFiltering:
        filter_by_frame: bool | None = field(
            default=None,
            metadata={
                "name": "FilterByFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )

    @dataclass
    class SubscriptionPolicy:
        has_incremental_updates: bool | None = field(
            default=None,
            metadata={
                "name": "HasIncrementalUpdates",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
