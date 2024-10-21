from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .fare_contract import FareContract
from .fare_contract_ref import FareContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "fareContracts_RelStructure"

    fare_contract_ref_or_fare_contract: Iterable[
        Union[FareContractRef, FareContract]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareContractRef",
                    "type": FareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContract",
                    "type": FareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
