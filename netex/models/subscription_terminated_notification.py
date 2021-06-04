from dataclasses import dataclass
from netex.models.subscription_terminated_notification_structure import SubscriptionTerminatedNotificationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionTerminatedNotification(SubscriptionTerminatedNotificationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
