from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceAttentionEnumeration(Enum):
    NONE_VALUE = "none"
    DOORBELL = "doorbell"
    HELP_POINT = "helpPoint"
    INTERCOM = "intercom"
    OTHER = "other"
