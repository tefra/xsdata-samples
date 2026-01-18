from __future__ import annotations

from dataclasses import dataclass

from .other_organisation_version_structure import (
    OtherOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ManagementAgentVersionStructure(OtherOrganisationVersionStructure):
    class Meta:
        name = "ManagementAgent_VersionStructure"
