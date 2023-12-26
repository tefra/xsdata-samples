from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EthGlobalTimeMessageFormatEnumSimple(Enum):
    """
    :cvar IEEE802_1_AS: Message format according to IEEE 802.1AS
        standard.
    :cvar IEEE802_1_AS_AUTOSAR: Message format according to IEEE 802.1AS
        standard with AUTOSAR extensions.
    """

    IEEE802_1_AS = "IEEE802-1AS"
    IEEE802_1_AS_AUTOSAR = "IEEE802-1AS-AUTOSAR"
