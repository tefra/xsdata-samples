from __future__ import annotations

from dataclasses import dataclass

from .organisational_unit_ref_structure import OrganisationalUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationalUnitRef(OrganisationalUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
