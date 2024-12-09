from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class AccessPropertiesType:
    """
    :ivar access_entry_type_ref: Reference to a user defined
        accessEntryType. Assumed to be DEFAULT if not present.
    :ivar id:
    """

    class Meta:
        name = "accessPropertiesType"

    access_entry_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "accessEntryTypeRef",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
