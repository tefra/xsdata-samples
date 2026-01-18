from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FamilyFacilityEnumeration(Enum):
    NONE = "none"
    SERVICES_FOR_CHILDREN = "servicesForChildren"
    SERVICES_FOR_ARMY_FAMILIES = "servicesForArmyFamilies"
    NURSERY_SERVICE = "nurseryService"
