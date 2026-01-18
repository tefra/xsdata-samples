from __future__ import annotations

from dataclasses import dataclass

from .organisation_ref_structure import OrganisationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnlineServiceOperatorRefStructure(OrganisationRefStructure):
    pass
