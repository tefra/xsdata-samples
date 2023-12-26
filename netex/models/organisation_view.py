from dataclasses import dataclass
from .organisation_derived_view_structure import (
    OrganisationDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationView(OrganisationDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
