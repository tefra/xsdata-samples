from dataclasses import dataclass
from netex.models.group_ticket_ref_structure import GroupTicketRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupTicketRef(GroupTicketRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
