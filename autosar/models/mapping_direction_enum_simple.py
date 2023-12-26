from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class MappingDirectionEnumSimple(Enum):
    """
    :cvar BIDIRECTIONAL: The TextTableMapping is applicable in both
        directions.
    :cvar FIRST_TO_SECOND: The TextTableMapping is applicable in the
        direction from firstDataPrototype / firstOperationArgument
        referring into the PortInterface of the PPortPrototype to
        secondDataPrototype / secondOperationArgument referring into the
        PortInterface of the RPortPrototype.
    :cvar SECOND_TO_FIRST: The TextTableMapping is applicable in the
        direction from secondDataPrototype / secondOperationArgument
        referring into the PortInterface of the PPortPrototype to
        firstDataPrototype / firstOperationArgument referring into the
        PortInterface of the RPortPrototype.
    """

    BIDIRECTIONAL = "BIDIRECTIONAL"
    FIRST_TO_SECOND = "FIRST-TO-SECOND"
    SECOND_TO_FIRST = "SECOND-TO-FIRST"
