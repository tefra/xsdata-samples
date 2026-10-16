from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleCollectionEnumeration(StrEnum):
    ON_SITE = "onSite"
    OFF_SITE_SHUTTLE = "offSiteShuttle"
    OFF_SITE = "offSite"
    MEET_AND_GREET = "meetAndGreet"
    FLOATING = "floating"
    OTHER = "other"
