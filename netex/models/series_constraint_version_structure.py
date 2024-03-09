from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from .connection_ref_structure import ConnectionRefStructure
from .fare_basis_enumeration import FareBasisEnumeration
from .fare_points_in_pattern_rel_structure import (
    FarePointsInPatternRelStructure,
)
from .journey_pattern_refs_rel_structure import JourneyPatternRefsRelStructure
from .multilingual_string import MultilingualString
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .private_code import PrivateCode
from .routing_type_enumeration import RoutingTypeEnumeration
from .series_constraint_prices_rel_structure import (
    SeriesConstraintPricesRelStructure,
)
from .series_constraint_refs_rel_structure import (
    SeriesConstraintRefsRelStructure,
)
from .series_type_enumeration import SeriesTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "SeriesConstraint_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    itinerary: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Itinerary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    symbol_marking_usual_route: Optional[str] = field(
        default=None,
        metadata={
            "name": "SymbolMarkingUsualRoute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    series_type: Optional[SeriesTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "SeriesType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    routing_type: Optional[RoutingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RoutingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_basis: Optional[FareBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "FareBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    first_class_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstClassDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    second_class_distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SecondClassDistance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    discrete: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Discrete",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_connection_ref: Optional[ConnectionRefStructure] = field(
        default=None,
        metadata={
            "name": "FromConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_connection_ref: Optional[ConnectionRefStructure] = field(
        default=None,
        metadata={
            "name": "ToConnectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_points_in_pattern: List[FarePointsInPatternRelStructure] = field(
        default_factory=list,
        metadata={
            "name": "farePointsInPattern",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_patterns: List[JourneyPatternRefsRelStructure] = field(
        default_factory=list,
        metadata={
            "name": "journeyPatterns",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: List[SeriesConstraintPricesRelStructure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    replaces: List[SeriesConstraintRefsRelStructure] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
