from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .medium_application_instance import MediumApplicationInstance

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumApplicationInstanceRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "mediumApplicationInstance_RelStructure"

    medium_application_instance: Iterable[MediumApplicationInstance] = field(
        default_factory=list,
        metadata={
            "name": "MediumApplicationInstance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
