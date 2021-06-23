from dataclasses import dataclass, field
from typing import Optional
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

    authority_ref: Optional[AuthorityRef] = field(
        default=None,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_organisation_ref: Optional[TransportOrganisationRef] = field(
        default=None,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_operators: Optional[GroupsOfTransportOrganisationsRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_lines: Optional[GroupsOfLinesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariff_zones: Optional[TariffZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
