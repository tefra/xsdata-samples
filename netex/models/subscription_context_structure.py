from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionContextStructure:
    heartbeat_interval: XmlDuration | None = field(
        default=None,
        metadata={
            "name": "HeartbeatInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
