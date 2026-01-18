from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .capability_not_supported_error import CapabilityNotSupportedError
from .data_object_delivery import DataObjectDelivery
from .error_description_structure import ErrorDescriptionStructure
from .other_error import OtherError

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class ServiceDeliveryBodyStructure:
    status: None | bool = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: None | ServiceDeliveryBodyStructure.ErrorCondition = (
        field(
            default=None,
            metadata={
                "name": "ErrorCondition",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
    )
    more_data: None | bool = field(
        default=None,
        metadata={
            "name": "MoreData",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    data_object_delivery: Iterable[DataObjectDelivery] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectDelivery",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    srs_name: None | str = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )

    @dataclass
    class ErrorCondition:
        capability_not_supported_error_or_other_error: (
            None | CapabilityNotSupportedError | OtherError
        ) = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "CapabilityNotSupportedError",
                        "type": CapabilityNotSupportedError,
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
        description: None | ErrorDescriptionStructure = field(
            default=None,
            metadata={
                "name": "Description",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
