from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ExecutionOrderConstraintTypeEnumSimple(Enum):
    """
    :cvar HIERARCHICAL_EOC: Specifies that the Execution Order
        Constraint specifies a hierarchical execution order constraint.
    :cvar ORDINARY_EOC: Specifies that the Execution Order Constraint
        specifies an ordinary execution order constraint.
    :cvar REPETITIVE_EOC: Specifies that the Execution Order Constraint
        specifies a repetitive execution order constraint.
    """
    HIERARCHICAL_EOC = "HIERARCHICAL-EOC"
    ORDINARY_EOC = "ORDINARY-EOC"
    REPETITIVE_EOC = "REPETITIVE-EOC"
