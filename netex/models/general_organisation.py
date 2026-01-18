from __future__ import annotations

from dataclasses import dataclass

from .general_organisation_version_structure import (
    GeneralOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralOrganisation(GeneralOrganisationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
