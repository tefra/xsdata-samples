from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.email_notification_recipients_2 import EmailNotificationRecipients2

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class EmailNotification2:
    """Send Email Notification to the emails specified in Booking Traveler.

    Supported Provider : 1G/1V

    Parameters
    ----------
    email_ref
        Reference to Booking Traveler Email.
    recipients
        Indicates the recipients of the mail addresses for which the user
        requires the system to send the itinerary.List of Possible Values:
        All = Send Email to All addresses Default = Send Email to Primary
        Booking Traveler Specific = Send Email to specific address Referred
        in EmailRef.
    """
    class Meta:
        name = "EmailNotification"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    email_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "EmailRef",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    recipients: None | EmailNotificationRecipients2 = field(
        default=None,
        metadata={
            "name": "Recipients",
            "type": "Attribute",
            "required": True,
        }
    )
