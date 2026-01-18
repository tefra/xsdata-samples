from __future__ import annotations

from dataclasses import dataclass

from .organisation_version_structure import OrganisationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Organisation1(OrganisationVersionStructure):
    class Meta:
        name = "Organisation"
        namespace = "http://www.netex.org.uk/netex"
