from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class AdditionalBindingTimeEnumSimple(Enum):
    """
    :cvar BLUEPRINT_DERIVATION_TIME: The point in time when an object is
        created from a blueprint.
    :cvar POST_BUILD: After the executable has been built.
    """
    BLUEPRINT_DERIVATION_TIME = "BLUEPRINT-DERIVATION-TIME"
    POST_BUILD = "POST-BUILD"
