from dataclasses import dataclass
from .allowed_resource_usage_exceeded_error_structure import (
    AllowedResourceUsageExceededErrorStructure,
)

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class AllowedResourceUsageExceededError(
    AllowedResourceUsageExceededErrorStructure
):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
