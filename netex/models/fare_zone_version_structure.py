from dataclasses import dataclass, field
from typing import Optional, Union
from .authority_ref import AuthorityRef
from .fare_sections_rel_structure import FareSectionsRelStructure
from .fare_zone_ref_structure import FareZoneRefStructure
from .fare_zone_refs_rel_structure import FareZoneRefsRelStructure
from .group_of_operators_ref import GroupOfOperatorsRef
from .operator_ref import OperatorRef
from .scoping_method_enumeration import ScopingMethodEnumeration
from .tariff_zone_refs_rel_structure import TariffZoneRefsRelStructure
from .tariff_zone_version_structure import TariffZoneVersionStructure
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
    authority_ref_or_operator_ref: Optional[Union[AuthorityRef, OperatorRef]] = field(
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
