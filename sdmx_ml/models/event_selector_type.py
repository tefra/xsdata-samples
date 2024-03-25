from dataclasses import dataclass, field
from typing import Tuple, Union

from sdmx_ml.models.data_registration_events_type import (
    DataRegistrationEventsType,
)
from sdmx_ml.models.metadata_registration_events_type import (
    MetadataRegistrationEventsType,
)
from sdmx_ml.models.structural_repository_events_type import (
    StructuralRepositoryEventsType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class EventSelectorType:
    """EventSelectorType describes the details of the events for a subscription.

    It allows subscribers to specify registry and repository events for
    which they wish to receive notifications.
    """

    structural_repository_events_or_data_registration_events_or_metadata_registration_events: Tuple[
        Union[
            StructuralRepositoryEventsType,
            DataRegistrationEventsType,
            MetadataRegistrationEventsType,
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StructuralRepositoryEvents",
                    "type": StructuralRepositoryEventsType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                    "max_occurs": 3,
                },
                {
                    "name": "DataRegistrationEvents",
                    "type": DataRegistrationEventsType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                    "max_occurs": 3,
                },
                {
                    "name": "MetadataRegistrationEvents",
                    "type": MetadataRegistrationEventsType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                    "max_occurs": 3,
                },
            ),
            "max_occurs": 3,
        },
    )
