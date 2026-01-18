from __future__ import annotations

from dataclasses import dataclass

from .other_organisation_version_structure import (
    OtherOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ManagementAgentVersionStructure(OtherOrganisationVersionStructure):
    class Meta:
        name = "ManagementAgent_VersionStructure"
