from __future__ import annotations

from dataclasses import dataclass

from .organisation_ref_structure import OrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationRefAbstract(OrganisationRefStructure):
    class Meta:
        name = "OrganisationRef_"
        namespace = "http://www.netex.org.uk/netex"
