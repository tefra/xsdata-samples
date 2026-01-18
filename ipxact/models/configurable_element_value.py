from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.complex_base_expression import ComplexBaseExpression

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ConfigurableElementValue(ComplexBaseExpression):
    """
    Describes the content of a configurable element.

    The required referenceId attribute refers to the ID attribute of the
    configurable element.

    :ivar reference_id: Refers to the ID attribute of the configurable
        element.
    :ivar id:
    """

    class Meta:
        name = "configurableElementValue"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    reference_id: str | None = field(
        default=None,
        metadata={
            "name": "referenceId",
            "type": "Attribute",
            "required": True,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
