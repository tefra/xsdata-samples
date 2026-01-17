from dataclasses import dataclass, field

from sdmx_ml.models.registration_status_type import RegistrationStatusType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class SubmitRegistrationsResponseType:
    """
    SubmitRegistrationsResponseType describes the structure of a
    registration response.

    For each submitted registration in the request, a registration status
    is provided. The status elements should be provided in the same order
    as the submitted registrations, although each status will echo the
    request to ensure accurate processing of the responses.

    :ivar registration_status: RegistrationStatus provided the status
        details for the submitted registration. It echoes the original
        submission and provides status information about the request.
    """

    registration_status: tuple[RegistrationStatusType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RegistrationStatus",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "min_occurs": 1,
        },
    )
