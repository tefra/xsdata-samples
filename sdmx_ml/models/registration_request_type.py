from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.action_type import ActionType
from sdmx_ml.models.registration_type import RegistrationType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry"


@dataclass(frozen=True, kw_only=True)
class RegistrationRequestType:
    """
    RegistrationRequestType describes the structure of a single
    registration request.

    It contains the details of a registation and an action field to
    indicate the action to be taken on the contained registration.

    :ivar registration: Registration contains the details of the
        data/metadata set registration to be added, updated, or deleted.
    :ivar action: The action attribute indicates whether this is an
        addition, a modification, or a deletion of a registration.
    """

    registration: RegistrationType = field(
        metadata={
            "name": "Registration",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry",
            "required": True,
        }
    )
    action: ActionType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
