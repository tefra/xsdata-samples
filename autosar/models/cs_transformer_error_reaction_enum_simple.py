from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CsTransformerErrorReactionEnumSimple(Enum):
    """
    :cvar APPLICATION_ONLY: The application is responsible for any error
        reaction. No autonomous error reaction of RTE and transformer.
    :cvar AUTONOMOUS: RTE and Transformer coordinate an autonomous error
        reaction on their own.
    """
    APPLICATION_ONLY = "APPLICATION-ONLY"
    AUTONOMOUS = "AUTONOMOUS"
