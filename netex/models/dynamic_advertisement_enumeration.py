from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DynamicAdvertisementEnumeration(Enum):
    ALWAYS = "always"
    NEVER = "never"
    ONLY_IF_ORDERED = "onlyIfOrdered"
    ONLY_IF_SIGNED_ON = "onlyIfSignedOn"
