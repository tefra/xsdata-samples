from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AccessibilityEnum(Enum):
    """
    Special forms of accessibility, easements and marking for handicapped people.

    :cvar BARRIER_FREE_ACCESSIBLE: Accessible without any steps or other
        barriers. This is not as strong as handicappedAccessible.
    :cvar HANDICAPPED_ACCESSIBLE: Accessible for handicapped people.
        Wheelchair accessible is a special form of it.
    :cvar WHEEL_CHAIR_ACCESSIBLE: Accessible by people in a wheelchair.
    :cvar HANDICAPPED_EASEMENTS: There are special easements for
        handicapped people, like handrails or handicapped-friendly
        furniture.
    :cvar ORIENTATION_SYSTEM_FOR_BLIND_PEOPLE: There is some orientation
        system, which helps blind or visually impaired people. Examples
        might be some acoustic system or tactile paving.
    :cvar HANDICAPPED_MARKED: There is a visible mark for the privilege
        of handicapped or disabled people (e.g. a wheelchair symbol).
    :cvar NONE: No form of special accessibility, i.e. usually not
        convenient for handicapped people, e.g. because of steps or
        barriers.
    :cvar UNKNOWN: It is unknown, whether there is a special form of
        accessibility.
    :cvar OTHER: Other.
    """

    BARRIER_FREE_ACCESSIBLE = "barrierFreeAccessible"
    HANDICAPPED_ACCESSIBLE = "handicappedAccessible"
    WHEEL_CHAIR_ACCESSIBLE = "wheelChairAccessible"
    HANDICAPPED_EASEMENTS = "handicappedEasements"
    ORIENTATION_SYSTEM_FOR_BLIND_PEOPLE = "orientationSystemForBlindPeople"
    HANDICAPPED_MARKED = "handicappedMarked"
    NONE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"
