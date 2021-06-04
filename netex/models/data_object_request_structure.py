from dataclasses import dataclass, field
from typing import Optional
from netex.models.abstract_functional_service_request_structure import AbstractFunctionalServiceRequestStructure
from netex.models.extensions_1 import Extensions1
from netex.models.network_frame_request_policy_structure import NetworkFrameRequestPolicyStructure
from netex.models.network_frame_topic import NetworkFrameTopic

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectRequestStructure(AbstractFunctionalServiceRequestStructure):
    topics: Optional["DataObjectRequestStructure.Topics"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    policy: Optional[NetworkFrameRequestPolicyStructure] = field(
        default=None,
        metadata={
            "name": "Policy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )

    @dataclass
    class Topics:
        network_frame_topic: Optional[NetworkFrameTopic] = field(
            default=None,
            metadata={
                "name": "NetworkFrameTopic",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "required": True,
            }
        )
