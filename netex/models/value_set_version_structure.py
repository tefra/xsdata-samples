from dataclasses import dataclass, field
from typing import Optional
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .types_of_value_structure import TypesOfValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ValueSetVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "ValueSet_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    values: Optional[TypesOfValueStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_of_values: Optional[str] = field(
        default=None,
        metadata={
            "name": "classOfValues",
            "type": "Attribute",
        }
    )
