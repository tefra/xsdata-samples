from __future__ import annotations

from dataclasses import dataclass, field

from .version_of_object_ref_structure import VersionOfObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllOrganisationsRefStructure(VersionOfObjectRefStructure):
    ref: str = field(
        init=False,
        default="All",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
