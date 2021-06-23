from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from .journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure
from .service_journey_ref import ServiceJourneyRef
from .template_service_journey_ref import TemplateServiceJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DefaultServiceJourneyRunTimeVersionedChildStructure(JourneyTimingVersionedChildStructure):
    class Meta:
        name = "DefaultServiceJourneyRunTime_VersionedChildStructure"

    run_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    template_service_journey_ref: Optional[TemplateServiceJourneyRef] = field(
        default=None,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_journey_ref: Optional[ServiceJourneyRef] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
