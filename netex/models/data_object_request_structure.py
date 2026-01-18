from __future__ import annotations

from dataclasses import dataclass, field

from .abstract_functional_service_request_structure import (
    AbstractFunctionalServiceRequestStructure,
)
from .extensions_1 import Extensions1
from .network_frame_request_policy_structure import (
    NetworkFrameRequestPolicyStructure,
)
from .network_frame_topic import NetworkFrameTopic

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectRequestStructure(AbstractFunctionalServiceRequestStructure):
    topics: DataObjectRequestStructure.Topics = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    policy: None | NetworkFrameRequestPolicyStructure = field(
        default=None,
        metadata={
            "name": "Policy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    extensions: None | Extensions1 = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class Topics:
        network_frame_topic: NetworkFrameTopic = field(
            metadata={
                "name": "NetworkFrameTopic",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
