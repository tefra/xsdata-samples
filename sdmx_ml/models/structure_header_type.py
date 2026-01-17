from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.base_header_type import BaseHeaderType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class StructureHeaderType(BaseHeaderType):
    """
    StructureHeaderType defines the structure for structural metadata
    messages.

    :ivar structure: Structure provides a reference to the structure
        (either explicitly or through a structure usage reference) that
        describes the format of data or reference metadata. In addition
        to the structure, it is required to also supply the namespace of
        the structure specific schema that defines the format of the
        data/metadata. For cross sectional data, additional information
        is also required to state which dimension is being used at the
        observation level. This information will allow the structure
        specific schema to be generated. For generic format messages,
        this is used to simply reference the underlying structure. It is
        not mandatory in these cases and the generic data/metadata sets
        will require this reference explicitly.
    :ivar data_provider: DataProvider identifies the provider of the
        data for a data message.
    :ivar metadata_provider: MetadataProvider identifies the provider of
        the metadata for a metadata message.
    :ivar data_set_action: DataSetAction code provides a code for
        determining whether the enclosed message is an Update or Delete
        message (not to be used with the UtilityData message).
    :ivar data_set_id: DataSetID provides an identifier for a contained
        data set.
    :ivar extracted: Extracted is a time-stamp from the system rendering
        the data.
    :ivar reporting_begin: ReportingBegin provides the start of the time
        period covered by the message (in the case of data).
    :ivar reporting_end: ReportingEnd provides the end of the time
        period covered by the message (in the case of data).
    :ivar embargo_date: EmbargoDate holds a time period before which the
        data included in this message is not available.
    """

    structure: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    data_provider: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    metadata_provider: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    data_set_action: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    data_set_id: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    extracted: Any = field(
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
