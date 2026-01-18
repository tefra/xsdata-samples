from __future__ import annotations

from dataclasses import dataclass

from .management_agent_version_structure import ManagementAgentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ManagementAgent(ManagementAgentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
