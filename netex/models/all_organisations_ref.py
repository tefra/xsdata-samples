from __future__ import annotations

from dataclasses import dataclass

from .all_organisations_ref_structure import AllOrganisationsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllOrganisationsRef(AllOrganisationsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
