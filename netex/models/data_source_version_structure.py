from dataclasses import dataclass, field
from typing import Optional
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DataSourceVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "DataSource_VersionStructure"

    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
