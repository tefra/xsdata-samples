from dataclasses import dataclass
from netex.models.unknown_subscriber_error_structure import UnknownSubscriberErrorStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class UnknownSubscriberError(UnknownSubscriberErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
