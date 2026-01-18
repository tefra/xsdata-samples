from __future__ import annotations

from dataclasses import dataclass

from .serviced_organisation_version_structure import (
    ServicedOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServicedOrganisation(ServicedOrganisationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
