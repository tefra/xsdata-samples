from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .participant_ref_structure import ParticipantRefStructure
from .subscription_qualifier_structure import SubscriptionQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AbstractSubscriptionStructure:
    subscriber_ref: ParticipantRefStructure | None = field(
        default=None,
        metadata={
            "name": "SubscriberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    subscription_identifier: SubscriptionQualifierStructure | None = field(
        default=None,
        metadata={
            "name": "SubscriptionIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    initial_termination_time: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "InitialTerminationTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
