from collections.abc import Iterable
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .type_of_concession import TypeOfConcession
from .type_of_concession_ref import TypeOfConcessionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfConcessionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "typeOfConcessions_RelStructure"

    type_of_concession_ref_or_type_of_concession: Iterable[
        TypeOfConcessionRef | TypeOfConcession
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfConcessionRef",
                    "type": TypeOfConcessionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfConcession",
                    "type": TypeOfConcession,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
