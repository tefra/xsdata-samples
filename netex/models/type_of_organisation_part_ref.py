from dataclasses import dataclass
from .type_of_organisation_part_ref_structure import (
    TypeOfOrganisationPartRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfOrganisationPartRef(TypeOfOrganisationPartRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
