from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .parking_ref import ParkingRef
from .point_of_interest_ref import PointOfInterestRef
from .service_site_ref import ServiceSiteRef
from .site_ref import SiteRef
from .stop_place_ref import StopPlaceRef
from .taxi_rank_ref import TaxiRankRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "siteRefs_RelStructure"

    stop_place_ref_or_site_ref: Iterable[
        TaxiRankRef
        | StopPlaceRef
        | ParkingRef
        | PointOfInterestRef
        | ServiceSiteRef
        | SiteRef
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
