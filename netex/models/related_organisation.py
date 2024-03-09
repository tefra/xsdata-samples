from dataclasses import dataclass

from .related_organisation_version_structure import (
    RelatedOrganisationVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RelatedOrganisation(RelatedOrganisationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
