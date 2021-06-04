from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LanguageUseEnumeration(Enum):
    NORMALLY_USED = "normallyUsed"
    UNDERSTOOD = "understood"
    NATIVE = "native"
    SPOKEN = "spoken"
    WRITTEN = "written"
    READ = "read"
    OTHER = "other"
    ALL_USES = "allUses"
