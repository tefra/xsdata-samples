from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.base_header_type import BaseHeaderType
from sdmx_ml.models.generic_metadata_structure_type import (
    GenericMetadataStructureType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class GenericMetadataHeaderType(BaseHeaderType):
    """
    GenericMetadataHeaderType defines the header format for generic
    reference metadata.

    :ivar data_provider: DataProvider identifies the provider of the
        data for a data message.
    :ivar reporting_begin: ReportingBegin provides the start of the time
        period covered by the message (in the case of data).
    :ivar reporting_end: ReportingEnd provides the end of the time
        period covered by the message (in the case of data).
    :ivar embargo_date: EmbargoDate holds a time period before which the
        data included in this message is not available.
    :ivar structure:
    """

    data_provider: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    reporting_begin: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    reporting_end: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    embargo_date: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    structure: tuple[GenericMetadataStructureType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Structure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "min_occurs": 1,
        },
    )
