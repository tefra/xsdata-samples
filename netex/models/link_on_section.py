from dataclasses import dataclass
from netex.models.link_on_section_versioned_child_structure import LinkOnSectionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LinkOnSection(LinkOnSectionVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
