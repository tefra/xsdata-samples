from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FieldAccessPolicyDefinitionRef:
    """
    Indicates the accessibility of the data in the field.
    """

    class Meta:
        name = "fieldAccessPolicyDefinitionRef"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

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
