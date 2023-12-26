from dataclasses import dataclass, field
from .all_organisations_ref_structure import AllOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllTransportOrganisationsRefStructure(AllOrganisationsRefStructure):
    ref: str = field(
        init=False,
        default="All",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
