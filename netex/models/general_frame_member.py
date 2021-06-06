from dataclasses import dataclass
from .general_frame_member_structure import GeneralFrameMemberStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeneralFrameMember(GeneralFrameMemberStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
