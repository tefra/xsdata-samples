from dataclasses import dataclass, field
from typing import Optional
from .abstract_subscription_structure import AbstractSubscriptionStructure
from .data_object_request import DataObjectRequest
from .extensions_1 import Extensions1
from .network_frame_subscription_policy_structure import NetworkFrameSubscriptionPolicyStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataObjectSubscriptionStructure(AbstractSubscriptionStructure):
    data_object_request: Optional[DataObjectRequest] = field(
        default=None,
        metadata={
            "name": "DataObjectRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    subscription_policy: Optional[NetworkFrameSubscriptionPolicyStructure] = field(
        default=None,
        metadata={
            "name": "SubscriptionPolicy",
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
