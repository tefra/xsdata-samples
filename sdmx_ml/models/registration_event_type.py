from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.registration_type import RegistrationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class RegistrationEventType:
    """
    This provides the details of a data or metadata registration event for
    the purposes of notification.

    :ivar registration: Registration provides the changed details of the
        data or metadata registration.
    """

    registration: RegistrationType | None = field(
        default=None,
        metadata={
            "name": "Registration",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
