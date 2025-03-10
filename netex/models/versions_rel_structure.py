from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .version import Version
from .version_ref import VersionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VersionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "versions_RelStructure"

    version_ref_or_version: Iterable[Union[VersionRef, Version]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VersionRef",
                    "type": VersionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Version",
                    "type": Version,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
