from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.type_base_air_reservation import TypeBaseAirReservation

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class TypeAirReservationWithFop(TypeBaseAirReservation):
    """
    Air Reservation With Form Of Payment.
    """

    class Meta:
        name = "typeAirReservationWithFOP"

    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
