from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .authority import Authority
from .containment_aggregation_structure import ContainmentAggregationStructure
from .operator import Operator

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TransportOperatorsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transportOperatorsInFrame_RelStructure"

    authority_or_operator: Iterable[Authority | Operator] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Authority",
                    "type": Authority,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Operator",
                    "type": Operator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
