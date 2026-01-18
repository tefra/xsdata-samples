from __future__ import annotations

from dataclasses import dataclass

from .transport_organisation_version_structure import (
    TransportOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatorVersionStructure(TransportOrganisationVersionStructure):
    class Meta:
        name = "Operator_VersionStructure"
