from dataclasses import dataclass, field

from .type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllCountriesRefStructure(TypeOfValueRefStructure):
    ref: str = field(
        init=False,
        default="All",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
