from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClosedTimeRangeStructure:
    start_time: XmlTime = field(
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_time: XmlTime = field(
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
