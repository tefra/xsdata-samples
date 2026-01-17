from dataclasses import dataclass

from ipxact.models.real_expression import RealExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Phase(RealExpression):
    """
    This is an non-negative floating point number that is used to sequence
    when a generator is run.

    The generators are run in order starting with zero. There may be
    multiple generators with the same phase number. In this case, the order
    should not matter with respect to other generators at the same phase.
    If no phase number is given the generator will be considered in the
    "last" phase and these generators will be run in the order in which
    they are encountered while processing generator elements.
    """

    class Meta:
        name = "phase"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
