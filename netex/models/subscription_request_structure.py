from dataclasses import dataclass, field
from typing import List
from .abstract_functional_service_subscription_request import AbstractFunctionalServiceSubscriptionRequest
from .abstract_subscription_request_structure import AbstractSubscriptionRequestStructure
from .data_object_subscription_request import DataObjectSubscriptionRequest

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionRequestStructure(AbstractSubscriptionRequestStructure):
    data_object_subscription_request: List[DataObjectSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    abstract_functional_service_subscription_request: List[AbstractFunctionalServiceSubscriptionRequest] = field(
        default_factory=list,
        metadata={
            "name": "AbstractFunctionalServiceSubscriptionRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        }
    )
