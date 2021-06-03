from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EthernetSwitchVlanIngressTagEnumSimple(Enum):
    """
    :cvar DROP_UNTAGGED: Drop if untagged.
    :cvar FORWARD_AS_IS: Forward with the same VLAN as received. Also
        untagged frames will be forwarded as untagged.
    """
    DROP_UNTAGGED = "DROP-UNTAGGED"
    FORWARD_AS_IS = "FORWARD-AS-IS"
