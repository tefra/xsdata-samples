from dataclasses import dataclass

from .abstract_notification_structure import AbstractNotificationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class DataReadyRequestStructure(AbstractNotificationStructure):
    pass
