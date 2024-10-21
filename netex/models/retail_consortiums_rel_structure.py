from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .retail_consortium import RetailConsortium
from .retail_consortium_ref import RetailConsortiumRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RetailConsortiumsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "retailConsortiums_RelStructure"

    retail_consortium_ref_or_retail_consortium: Iterable[
        Union[RetailConsortiumRef, RetailConsortium]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailConsortium",
                    "type": RetailConsortium,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
