from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .journey_timing_versioned_child_structure import (
    JourneyTimingVersionedChildStructure,
)
from .service_journey_ref import ServiceJourneyRef
from .template_service_journey_ref import TemplateServiceJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultServiceJourneyRunTimeVersionedChildStructure(
    JourneyTimingVersionedChildStructure
):
    class Meta:
        name = "DefaultServiceJourneyRunTime_VersionedChildStructure"

    run_time: XmlDuration = field(
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    service_journey_ref: (
        None | TemplateServiceJourneyRef | ServiceJourneyRef
    ) = field(
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
