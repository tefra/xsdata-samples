from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ValidityStatusEnum(Enum):
    """
    Values of validity status that can be assigned to a described event, action
    or item.

    :cvar ACTIVE: The described event, action or item is currently
        active regardless of the definition of the validity time
        specification.
    :cvar SUSPENDED: The described event, action or item is currently
        suspended, that is inactive, regardless of the definition of the
        validity time specification.
    :cvar DEFINED_BY_VALIDITY_TIME_SPEC: The validity status of the
        described event, action or item is in accordance with the
        definition of the validity time specification.
    """
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DEFINED_BY_VALIDITY_TIME_SPEC = "definedByValidityTimeSpec"
