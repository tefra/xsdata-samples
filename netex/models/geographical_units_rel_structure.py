from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .geographical_unit import GeographicalUnit
from .geographical_unit_ref import GeographicalUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GeographicalUnitsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "geographicalUnits_RelStructure"

    geographical_unit_ref_or_geographical_unit: Iterable[
        GeographicalUnitRef | GeographicalUnit
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalUnitRef",
                    "type": GeographicalUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnit",
                    "type": GeographicalUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
