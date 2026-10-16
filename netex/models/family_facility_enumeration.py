from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class FamilyFacilityEnumeration(StrEnum):
    NONE = "none"
    SERVICES_FOR_CHILDREN = "servicesForChildren"
    SERVICES_FOR_ARMY_FAMILIES = "servicesForArmyFamilies"
    NURSERY_SERVICE = "nurseryService"
