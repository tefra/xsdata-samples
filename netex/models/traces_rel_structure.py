from collections.abc import Iterable
from dataclasses import dataclass, field

from .trace import Trace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TracesRelStructure:
    class Meta:
        name = "traces_RelStructure"

    trace: Iterable[Trace] = field(
        default_factory=list,
        metadata={
            "name": "Trace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
