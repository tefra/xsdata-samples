from dataclasses import dataclass
from netex.models.group_ticket_version_structure import GroupTicketVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupTicket(GroupTicketVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
