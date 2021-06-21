from dataclasses import dataclass, field
from typing import List, Optional
from .authority_ref import AuthorityRef
from .fare_sections_rel_structure import FareSectionsRelStructure
from .fare_zone_ref_structure import FareZoneRefStructure
from .fare_zone_refs_rel_structure import FareZoneRefsRelStructure
from .group_of_operators_ref import GroupOfOperatorsRef
from .operator_ref import OperatorRef
from .scoping_method_enumeration import ScopingMethodEnumeration
from .tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from .tariff_zone_version_structure import TariffZoneVersionStructure
from .transport_organisation_ref import TransportOrganisationRef
from .zone_topology_enumeration import ZoneTopologyEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareZoneVersionStructure(TariffZoneVersionStructure):
    class Meta:
        name = "FareZone_VersionStructure"

    parent_fare_zone_ref: Optional[FareZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentFareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    zone_topology: Optional[ZoneTopologyEnumeration] = field(
        default=None,
        metadata={
            "name": "ZoneTopology",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    scoping_method: Optional[ScopingMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "ScopingMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
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
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareSections",
                    "type": FareSectionsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "contains",
                    "type": TariffZoneRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "neighbours",
                    "type": FareZoneRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 4,
        }
    )
