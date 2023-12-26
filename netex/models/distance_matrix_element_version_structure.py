from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union
from .cell_versioned_child_structure import PriceableObjectVersionStructure
from .distance_matrix_element_prices_rel_structure import (
    DistanceMatrixElementPricesRelStructure,
)
from .fare_point_in_pattern_ref_structure import FarePointInPatternRefStructure
from .fare_section_ref_structure import FareSectionRefStructure
from .fare_table_ref import FareTableRef
from .geographical_structure_factors_rel_structure import (
    GeographicalStructureFactorsRelStructure,
)
from .scheduled_stop_point_derived_view_structure import (
    ScheduledStopPointDerivedViewStructure,
)
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .series_constraints_rel_structure import SeriesConstraintsRelStructure
from .standard_fare_table_ref import StandardFareTableRef
from .tariff_refs_rel_structure import TariffRefsRelStructure
from .tariff_zone_ref_structure import TariffZoneRefStructure
from .zone_derived_view_structure import ZoneDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistanceMatrixElementVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "DistanceMatrixElement_VersionStructure"

    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relative_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "RelativeRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_direct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsDirect",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    inverse_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InverseAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            ScheduledStopPointRefStructure,
            ScheduledStopPointDerivedViewStructure,
            TariffZoneRefStructure,
            ZoneDerivedViewStructure,
            FareSectionRefStructure,
            FarePointInPatternRefStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StartStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartStopPointView",
                    "type": ScheduledStopPointDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StartTariffZoneView",
                    "type": ZoneDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FromFareSectionRef",
                    "type": FareSectionRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FromFarePointInPatternRef",
                    "type": FarePointInPatternRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_1: Optional[
        Union[
            ScheduledStopPointRefStructure,
            ScheduledStopPointDerivedViewStructure,
            TariffZoneRefStructure,
            ZoneDerivedViewStructure,
            FareSectionRefStructure,
            FarePointInPatternRefStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EndStopPointRef",
                    "type": ScheduledStopPointRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndStopPointView",
                    "type": ScheduledStopPointDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndTariffZoneRef",
                    "type": TariffZoneRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EndTariffZoneView",
                    "type": ZoneDerivedViewStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ToFareSectionRef",
                    "type": FareSectionRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ToFarePointInPatternRef",
                    "type": FarePointInPatternRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    series_constraints: Optional[SeriesConstraintsRelStructure] = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    structure_factors: Optional[
        GeographicalStructureFactorsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "structureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariffs: Optional[TariffRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    standard_fare_table_ref_or_fare_table_ref: Optional[
        Union[StandardFareTableRef, FareTableRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    prices: Optional[DistanceMatrixElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
