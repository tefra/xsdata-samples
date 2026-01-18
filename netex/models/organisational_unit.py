from __future__ import annotations

from dataclasses import dataclass

from .organisational_unit_version_structure import (
    OrganisationalUnitVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationalUnit(OrganisationalUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
