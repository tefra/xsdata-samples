from dataclasses import dataclass, field

from sdmx_ml.models.registration_request_type import RegistrationRequestType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubmitRegistrationsRequestType:
    """
    SubmitRegistrationsRequestType defines the payload of a request message used to
    submit addtions, updates, or deletions of data/metadata set registrations.

    :ivar registration_request: RegistrationRequest provides the details
        of a requested registration and the action to take on it. A
        reference to a provision agreement that exists in the registry
        must be provide along with a simple and/or queryable data
        source. The id should only be provided when updating or deleting
        a registration.
    """

    registration_request: tuple[RegistrationRequestType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RegistrationRequest",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "min_occurs": 1,
        },
    )
