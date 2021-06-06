from dataclasses import dataclass, field
from typing import Optional
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfConcessionVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "TypeOfConcession_VersionStructure"

    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
