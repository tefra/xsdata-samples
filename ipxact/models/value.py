from dataclasses import dataclass

from ipxact.models.string_expression import StringExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class Value(StringExpression):
    """
    The value of the parameter.
    """

    class Meta:
        name = "value"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"
