from __future__ import annotations

from dataclasses import dataclass, field

from .compound_train_ref import CompoundTrainRef
from .infrastructure_link_restriction_version_structure import (
    InfrastructureLinkRestrictionVersionStructure,
)
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RestrictedManoeuvreVersionStructure(
    InfrastructureLinkRestrictionVersionStructure
):
    class Meta:
        name = "RestrictedManoeuvre_VersionStructure"

    transport_type_ref_or_vehicle_type_ref: (
        SimpleVehicleTypeRef
        | CompoundTrainRef
        | TrainRef
        | VehicleTypeRef
        | TransportTypeRef
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
