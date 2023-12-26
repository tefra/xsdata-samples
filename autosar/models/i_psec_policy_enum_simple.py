from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IPsecPolicyEnumSimple(Enum):
    """
    :cvar DROP: Signifying that packets should be discarded
    :cvar IPSEC: Signifying that packets should be protected.
    :cvar PASSTHROUGH: Signifying that no IPsec processing should be
        done at all.
    :cvar REJECT: Signifying that packets should be discarded and a
        diagnostic ICMP returned.
    """

    DROP = "DROP"
    IPSEC = "IPSEC"
    PASSTHROUGH = "PASSTHROUGH"
    REJECT = "REJECT"
