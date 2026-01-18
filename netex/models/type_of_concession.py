from __future__ import annotations

from dataclasses import dataclass

from .type_of_concession_version_structure import (
    TypeOfConcessionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfConcession(TypeOfConcessionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
