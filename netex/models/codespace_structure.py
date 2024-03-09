from dataclasses import dataclass, field
from typing import Optional

from .entity_structure import EntityStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CodespaceStructure(EntityStructure):
    xmlns: Optional[str] = field(
        default=None,
        metadata={
            "name": "Xmlns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    xmlns_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "XmlnsUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    data_source_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "dataSourceRef",
            "type": "Attribute",
        },
    )
