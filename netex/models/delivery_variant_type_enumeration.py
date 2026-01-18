from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DeliveryVariantTypeEnumeration(Enum):
    ANY = "any"
    PRINTED = "printed"
    TEXT_TO_SPEECH = "textToSpeech"
    RECORDED_ANNOUNCEMENT = "recordedAnnouncement"
    WEB = "web"
    MOBILE = "mobile"
    OTHER = "other"
