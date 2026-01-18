from __future__ import annotations

from dataclasses import dataclass

from .residential_qualification_version_structure import (
    ResidentialQualificationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResidentialQualification(ResidentialQualificationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
