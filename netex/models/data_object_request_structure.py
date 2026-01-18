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


@dataclass
class DataObjectRequestStructure(AbstractFunctionalServiceRequestStructure):
    topics: DataObjectRequestStructure.Topics | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    policy: NetworkFrameRequestPolicyStructure | None = field(
        default=None,
        metadata={
            "name": "Policy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    extensions: Extensions1 | None = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass
    class Topics:
        network_frame_topic: NetworkFrameTopic | None = field(
            default=None,
            metadata={
                "name": "NetworkFrameTopic",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            },
        )
