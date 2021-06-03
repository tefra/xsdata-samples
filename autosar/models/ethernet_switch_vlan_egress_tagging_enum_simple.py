from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EthernetSwitchVlanEgressTaggingEnumSimple(Enum):
    """
    :cvar NOT_SENT: will not be sent
    :cvar SENT_TAGGED: sent with its VLAN tag
    :cvar SENT_UNTAGGED: sent without a VLAN tag
    """
    NOT_SENT = "NOT-SENT"
    SENT_TAGGED = "SENT-TAGGED"
    SENT_UNTAGGED = "SENT-UNTAGGED"
