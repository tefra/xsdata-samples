from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.enumerated_value_type import EnumeratedValueType

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class EnumeratedValues:
    """
    Enumerates specific values that can be assigned to the bit field.

    :ivar enumeration_definition_ref: References an enumeration to be
        found in a local or external library.  The four attributes
        define the VLNV of the referenced element.
    :ivar enumerated_value: Enumerates specific values that can be
        assigned to the bit field. The name of this enumerated value.
        This may be used as a token in generating code.
    """

    class Meta:
        name = "enumeratedValues"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    enumeration_definition_ref: Optional[
        "EnumeratedValues.EnumerationDefinitionRef"
    ] = field(
        default=None,
        metadata={
            "name": "enumerationDefinitionRef",
            "type": "Element",
        },
    )
    enumerated_value: list[EnumeratedValueType] = field(
        default_factory=list,
        metadata={
            "name": "enumeratedValue",
            "type": "Element",
        },
    )

    @dataclass
    class EnumerationDefinitionRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_definitions: Optional[str] = field(
            default=None,
            metadata={
                "name": "typeDefinitions",
                "type": "Attribute",
                "required": True,
            },
        )
