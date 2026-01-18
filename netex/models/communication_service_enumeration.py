from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CommunicationServiceEnumeration(Enum):
    FREE_WIFI = "freeWifi"
    PUBLIC_WIFI = "publicWifi"
    PHONE = "phone"
    INTERNET = "internet"
    MOBILE_COVERAGE = "mobileCoverage"
    VIDEO_ENTERTAINMENT = "videoEntertainment"
    AUDIO_ENTERTAINMENT = "audioEntertainment"
    POSTBOX = "postbox"
    POST_OFFICE = "postOffice"
    BUSINESS_SERVICES = "businessServices"
