from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class EntranceAttentionEnumeration(StrEnum):
    NONE = "none"
    DOORBELL = "doorbell"
    HELP_POINT = "helpPoint"
    INTERCOM = "intercom"
    OTHER = "other"
