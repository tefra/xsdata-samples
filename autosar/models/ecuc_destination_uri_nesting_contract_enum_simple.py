from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EcucDestinationUriNestingContractEnumSimple(Enum):
    """
    :cvar LEAF_OF_TARGET_CONTAINER: EcucDestinationUriPolicy describes
        elements (subContainers, Parameters, References) that are
        directly owned by the target container.
    :cvar TARGET_CONTAINER: EcucDestinationUriPolicy describes the
        target container of EcucUriReferenceDef.
    :cvar VERTEX_OF_TARGET_CONTAINER: EcucDestinationUriPolicy describes
        elements (subContainers, Parameters, References) of the target
        container which can be defined in arbitrary nested subContainer
        structure.
    """
    LEAF_OF_TARGET_CONTAINER = "LEAF-OF-TARGET-CONTAINER"
    TARGET_CONTAINER = "TARGET-CONTAINER"
    VERTEX_OF_TARGET_CONTAINER = "VERTEX-OF-TARGET-CONTAINER"
