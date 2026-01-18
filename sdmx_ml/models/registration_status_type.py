from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.registration_type import RegistrationType
from sdmx_ml.models.status_message_type_2 import StatusMessageType2

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class RegistrationStatusType:
    """
    RegistrationStatusType describes the structure of a registration
    status.

    :ivar registration: Registration, at the very least echoes the
        submitted registration. It the request was to create a new
        registration and it was successful, an id must be supplied.
    :ivar status_message: StatusMessage provides that status for the
        registration request, and if necessary, any error or warning
        information.
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
    status_message: StatusMessageType2 | None = field(
        default=None,
        metadata={
            "name": "StatusMessage",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
