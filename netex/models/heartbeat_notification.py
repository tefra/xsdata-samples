from dataclasses import dataclass

from .heartbeat_notification_structure import HeartbeatNotificationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class HeartbeatNotification(HeartbeatNotificationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
