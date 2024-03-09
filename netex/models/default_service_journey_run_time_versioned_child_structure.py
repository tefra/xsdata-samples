from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from .journey_timing_versioned_child_structure import (
    JourneyTimingVersionedChildStructure,
)
from .service_journey_ref import ServiceJourneyRef
from .template_service_journey_ref import TemplateServiceJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultServiceJourneyRunTimeVersionedChildStructure(
    JourneyTimingVersionedChildStructure
):
    class Meta:
        name = "DefaultServiceJourneyRunTime_VersionedChildStructure"

    run_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    service_journey_ref: Optional[
        Union[TemplateServiceJourneyRef, ServiceJourneyRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
