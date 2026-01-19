from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .dead_run_ref import DeadRunRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .service_journey_ref import ServiceJourneyRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ExplicitJourneyRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "explicitJourneyRefs_RelStructure"

    service_journey_ref_or_vehicle_journey_ref: Sequence[
        TemplateServiceJourneyRef
        | ServiceJourneyRef
        | DeadRunRef
        | VehicleJourneyRef
    ] = field(
        default_factory=list,
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
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
