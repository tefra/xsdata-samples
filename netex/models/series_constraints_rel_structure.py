from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .series_constraint import SeriesConstraint
from .series_constraint_ref import SeriesConstraintRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SeriesConstraintsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "SeriesConstraints_RelStructure"

    series_constraint_ref_or_series_constraint: List[Union[SeriesConstraintRef, SeriesConstraint]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SeriesConstraintRef",
                    "type": SeriesConstraintRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraint",
                    "type": SeriesConstraint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
