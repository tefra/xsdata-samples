from __future__ import annotations

from dataclasses import dataclass, field

from .authority_ref import AuthorityRef
from .group_of_lines_version_structure import GroupOfLinesVersionStructure
from .groups_of_lines_in_frame_rel_structure import (
    GroupsOfLinesInFrameRelStructure,
)
from .groups_of_operators_refs_rel_structure import (
    GroupsOfOperatorsRefsRelStructure,
)
from .operator_ref import OperatorRef
from .tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkVersionStructure(GroupOfLinesVersionStructure):
    class Meta:
        name = "Network_VersionStructure"

    transport_organisation_ref: None | AuthorityRef | OperatorRef = field(
        default=None,
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
            ),
        },
    )
    groups_of_operators: None | GroupsOfOperatorsRefsRelStructure = field(
        default=None,
        metadata={
            "name": "groupsOfOperators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_lines: None | GroupsOfLinesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "groupsOfLines",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_zones: None | TariffZoneRefsRelStructure = field(
        default=None,
        metadata={
            "name": "tariffZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
