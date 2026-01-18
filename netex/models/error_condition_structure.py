from dataclasses import dataclass, field

from .access_not_allowed_error import AccessNotAllowedError
from .allowed_resource_usage_exceeded_error import (
    AllowedResourceUsageExceededError,
)
from .beyond_data_horizon import BeyondDataHorizon
from .capability_not_supported_error import CapabilityNotSupportedError
from .invalid_data_references_error import InvalidDataReferencesError
from .natural_language_string_structure import NaturalLanguageStringStructure
from .no_info_for_topic_error import NoInfoForTopicError
from .other_error import OtherError
from .parameters_ignored_error import ParametersIgnoredError
from .service_not_available_error import ServiceNotAvailableError
from .unknown_extensions_error import UnknownExtensionsError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ErrorConditionStructure:
    choice: (
        ServiceNotAvailableError
        | CapabilityNotSupportedError
        | AccessNotAllowedError
        | InvalidDataReferencesError
        | BeyondDataHorizon
        | NoInfoForTopicError
        | ParametersIgnoredError
        | UnknownExtensionsError
        | AllowedResourceUsageExceededError
        | OtherError
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceNotAvailableError",
                    "type": ServiceNotAvailableError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "CapabilityNotSupportedError",
                    "type": CapabilityNotSupportedError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AccessNotAllowedError",
                    "type": AccessNotAllowedError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "InvalidDataReferencesError",
                    "type": InvalidDataReferencesError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "BeyondDataHorizon",
                    "type": BeyondDataHorizon,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "NoInfoForTopicError",
                    "type": NoInfoForTopicError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ParametersIgnoredError",
                    "type": ParametersIgnoredError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "UnknownExtensionsError",
                    "type": UnknownExtensionsError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AllowedResourceUsageExceededError",
                    "type": AllowedResourceUsageExceededError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "OtherError",
                    "type": OtherError,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    description: NaturalLanguageStringStructure | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
