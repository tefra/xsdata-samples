from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DefaultValueApplicationStrategyEnumSimple(Enum):
    """
    :cvar DEFAULT_IF_REVISION_UPDATE: If the AUTOSAR model is older than
        the Baseline of the Data Exchange Point and the older version
        did not yet support the attribute, then the AUTOSAR defined
        default value SHALL be applied before further validation or
        processing.
    :cvar DEFAULT_IF_UNDEFINED: If the AUTOSAR model does not explicitly
        specify a value, then the apply the AUTOSAR defined default
        value  before further validation or processing.
    :cvar NO_DEFAULT: do not apply the AUTOSAR defined default value
    """

    DEFAULT_IF_REVISION_UPDATE = "DEFAULT-IF-REVISION-UPDATE"
    DEFAULT_IF_UNDEFINED = "DEFAULT-IF-UNDEFINED"
    NO_DEFAULT = "NO-DEFAULT"
