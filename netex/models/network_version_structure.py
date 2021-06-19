from dataclasses import dataclass, field
from typing import List
from .authority_ref import AuthorityRef
from .group_of_lines_version_structure import GroupOfLinesVersionStructure
from .groups_of_lines_in_frame_rel_structure import GroupsOfLinesInFrameRelStructure
from .groups_of_transport_organisations_refs_rel_structure import GroupsOfTransportOrganisationsRefsRelStructure
from .operator_ref import OperatorRef
from .tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from .transport_organisation_ref import TransportOrganisationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkVersionStructure(GroupOfLinesVersionStructure):
    class Meta:
        name = "Network_VersionStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportOrganisationRef",
                    "type": TransportOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfOperators",
                    "type": GroupsOfTransportOrganisationsRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfLines",
                    "type": GroupsOfLinesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "tariffZones",
                    "type": TariffZoneRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 8,
        }
    )
