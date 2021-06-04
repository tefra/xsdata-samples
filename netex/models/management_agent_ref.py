from dataclasses import dataclass
from netex.models.management_agent_ref_structure import ManagementAgentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ManagementAgentRef(ManagementAgentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
