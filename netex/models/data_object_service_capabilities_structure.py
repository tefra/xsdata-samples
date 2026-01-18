from __future__ import annotations

from dataclasses import dataclass, field

from .abstract_capabilities_structure import AbstractCapabilitiesStructure
from .data_object_capability_request_policy_structure import (
    DataObjectCapabilityRequestPolicyStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: (
        None | DataObjectServiceCapabilitiesStructure.TopicFiltering
    ) = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    request_policy: None | DataObjectCapabilityRequestPolicyStructure = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    subscription_policy: (
        None | DataObjectServiceCapabilitiesStructure.SubscriptionPolicy
    ) = field(
        default=None,
        metadata={
            "name": "SubscriptionPolicy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    response_features: None | object = field(
        default=None,
        metadata={
            "name": "ResponseFeatures",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )

    @dataclass(kw_only=True)
    class TopicFiltering:
        filter_by_frame: None | bool = field(
            default=None,
            metadata={
                "name": "FilterByFrame",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )

    @dataclass(kw_only=True)
    class SubscriptionPolicy:
        has_incremental_updates: None | bool = field(
            default=None,
            metadata={
                "name": "HasIncrementalUpdates",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
