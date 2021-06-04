from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.models.cell_versioned_child_structure import PriceableObjectVersionStructure
from netex.models.distance_matrix_element_prices_rel_structure import DistanceMatrixElementPricesRelStructure
from netex.models.fare_point_in_pattern_ref_structure import FarePointInPatternRefStructure
from netex.models.fare_section_ref_structure import FareSectionRefStructure
from netex.models.fare_table_ref import FareTableRef
from netex.models.geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from netex.models.scheduled_stop_point_derived_view_structure import ScheduledStopPointDerivedViewStructure
from netex.models.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.models.series_constraints_rel_structure import SeriesConstraintsRelStructure
from netex.models.standard_fare_table_ref import StandardFareTableRef
from netex.models.tariff_refs_rel_structure import TariffRefsRelStructure
from netex.models.tariff_zone_ref_structure import TariffZoneRefStructure
from netex.models.zone_derived_view_structure import ZoneDerivedViewStructure

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
        }
    )
    relative_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "RelativeRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_direct: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsDirect",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    inverse_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InverseAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_stop_point_view: Optional[ScheduledStopPointDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "StartStopPointView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_tariff_zone_ref: Optional[TariffZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "StartTariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_tariff_zone_view: Optional[ZoneDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "StartTariffZoneView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_fare_section_ref: Optional[FareSectionRefStructure] = field(
        default=None,
        metadata={
            "name": "FromFareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_fare_point_in_pattern_ref: Optional[FarePointInPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "FromFarePointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_stop_point_view: Optional[ScheduledStopPointDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "EndStopPointView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_tariff_zone_ref: Optional[TariffZoneRefStructure] = field(
        default=None,
        metadata={
            "name": "EndTariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_tariff_zone_view: Optional[ZoneDerivedViewStructure] = field(
        default=None,
        metadata={
            "name": "EndTariffZoneView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_fare_section_ref: Optional[FareSectionRefStructure] = field(
        default=None,
        metadata={
            "name": "ToFareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_fare_point_in_pattern_ref: Optional[FarePointInPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "ToFarePointInPatternRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraints: Optional[SeriesConstraintsRelStructure] = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    structure_factors: Optional[GeographicalStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "structureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariffs: Optional[TariffRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_fare_table_ref: List[StandardFareTableRef] = field(
        default_factory=list,
        metadata={
            "name": "StandardFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
        }
    )
    fare_table_ref: Optional[FareTableRef] = field(
        default=None,
        metadata={
            "name": "FareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[DistanceMatrixElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
