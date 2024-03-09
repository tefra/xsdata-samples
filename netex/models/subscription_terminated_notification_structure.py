from dataclasses import dataclass, field
from typing import List, Optional

from .error_description_structure import ErrorDescriptionStructure
from .extensions_1 import Extensions1
from .participant_ref_structure import ParticipantRefStructure
from .producer_response_structure import ProducerResponseStructure
from .subscription_filter_ref_structure import SubscriptionFilterRefStructure
from .subscription_qualifier_structure import SubscriptionQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionTerminatedNotificationStructure(ProducerResponseStructure):
    subscriber_ref: List[ParticipantRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_filter_ref: List[SubscriptionFilterRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionFilterRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_ref: List[SubscriptionQualifierStructure] = field(
        default_factory=list,
        metadata={
            "name": "SubscriptionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    description: Optional[ErrorDescriptionStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
