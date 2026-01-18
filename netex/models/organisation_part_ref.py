from __future__ import annotations

from dataclasses import dataclass

from .organisation_part_ref_structure import OrganisationPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationPartRef(OrganisationPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
