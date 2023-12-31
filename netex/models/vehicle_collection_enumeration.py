from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class VehicleCollectionEnumeration(Enum):
    ON_SITE = "onSite"
    OFF_SITE_SHUTTLE = "offSiteShuttle"
    OFF_SITE = "offSite"
    MEET_AND_GREET = "meetAndGreet"
    FLOATING = "floating"
    OTHER = "other"
