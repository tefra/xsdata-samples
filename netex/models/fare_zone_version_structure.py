from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.authority_ref import AuthorityRef
from netex.models.fare_sections_rel_structure import FareSectionsRelStructure
from netex.models.fare_zone_ref_structure import FareZoneRefStructure
from netex.models.fare_zone_refs_rel_structure import FareZoneRefsRelStructure
from netex.models.group_of_operators_ref import GroupOfOperatorsRef
from netex.models.operator_ref import OperatorRef
from netex.models.scoping_method_enumeration import ScopingMethodEnumeration
from netex.models.tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from netex.models.tariff_zone_version_structure import TariffZoneVersionStructure
from netex.models.transport_organisation_ref import TransportOrganisationRef
from netex.models.zone_topology_enumeration import ZoneTopologyEnumeration

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
    authority_ref: List[AuthorityRef] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    operator_ref: List[OperatorRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
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
    group_of_operators_ref: Optional[GroupOfOperatorsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_sections: Optional[FareSectionsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contains: Optional[TariffZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    neighbours: Optional[FareZoneRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
