from dataclasses import dataclass
from netex.models.group_of_link_sequences_version_structure import GroupOfLinkSequencesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfLinkSequences(GroupOfLinkSequencesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
