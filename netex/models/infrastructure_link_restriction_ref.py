from dataclasses import dataclass

from .infrastructure_link_restriction_ref_structure import (
    InfrastructureLinkRestrictionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class InfrastructureLinkRestrictionRef(
    InfrastructureLinkRestrictionRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
