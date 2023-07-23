from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "http://www.travelport.com/schema/gdsQueue_v52_0"


@dataclass
class QueueElement:
    """
    Parameters
    ----------
    provider_code
    provider_locator_code
    departure_date
    queue_date
        Denotes the GDS formatted Date a PNR is placed in queue.
    queue_time
        Time a PNR placed in queue.
    name
        Name as in queue
    universal_record_locator_code
        Present if there is an associated UR
    created_by_agent_code
        Agent who created UR - Present if there is an associated UR
    modified_by_agent_code
        Agent who modified UR - Present if there is an associated UR with
        modifications
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/gdsQueue_v52_0"

    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        }
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        }
    )
    departure_date: None | str = field(
        default=None,
        metadata={
            "name": "DepartureDate",
            "type": "Attribute",
        }
    )
    queue_date: None | str = field(
        default=None,
        metadata={
            "name": "QueueDate",
            "type": "Attribute",
        }
    )
    queue_time: None | XmlTime = field(
        default=None,
        metadata={
            "name": "QueueTime",
            "type": "Attribute",
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    created_by_agent_code: None | str = field(
        default=None,
        metadata={
            "name": "CreatedByAgentCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        }
    )
    modified_by_agent_code: None | str = field(
        default=None,
        metadata={
            "name": "ModifiedByAgentCode",
            "type": "Attribute",
            "pattern": r"[a-zA-Z0-9\-_\.@ ]{1,128}",
        }
    )
