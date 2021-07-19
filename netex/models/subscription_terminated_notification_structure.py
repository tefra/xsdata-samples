from dataclasses import dataclass, field
from typing import List
from .extensions_1 import Extensions1
from .producer_response_structure import ProducerResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionTerminatedNotificationStructure(ProducerResponseStructure):
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SubscriberRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionFilterRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "SubscriptionRef",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Description",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Extensions",
                    "type": Extensions1,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        }
    )
