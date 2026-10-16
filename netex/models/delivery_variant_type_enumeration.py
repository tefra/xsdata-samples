from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DeliveryVariantTypeEnumeration(StrEnum):
    ANY = "any"
    PRINTED = "printed"
    TEXT_TO_SPEECH = "textToSpeech"
    RECORDED_ANNOUNCEMENT = "recordedAnnouncement"
    WEB = "web"
    MOBILE = "mobile"
    OTHER = "other"
