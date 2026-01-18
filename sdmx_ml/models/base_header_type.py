from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.action_type import ActionType
from sdmx_ml.models.name import Name
from sdmx_ml.models.party_type import PartyType
from sdmx_ml.models.payload_structure_type import PayloadStructureType
from sdmx_ml.models.sender_type import SenderType
from sdmx_ml.models.text_type import TextType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class BaseHeaderType:
    """
    BaseHeaderType in an abstract base type that defines the basis for all
    message headers.

    Specific message formats will refine this.

    :ivar id: ID identifies an identification for the message, assigned
        by the sender.
    :ivar test: Test indicates whether the message is for test purposes
        or not.
    :ivar prepared: Prepared is the date the message was prepared.
    :ivar sender: Sender is information about the party that is
        transmitting the message.
    :ivar receiver: Receiver is information about the party that is the
        intended recipient of the message.
    :ivar name: Name provides a name for the transmission. Multiple
        instances allow for parallel language values.
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
    :ivar source: Source provides human-readable information about the
        source of the data.
    """

    id: str | None = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    test: bool = field(
        default=False,
        metadata={
            "name": "Test",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
        },
    )
    prepared: XmlDateTime | XmlDate | None = field(
        default=None,
        metadata={
            "name": "Prepared",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
        },
    )
    sender: SenderType | None = field(
        default=None,
        metadata={
            "name": "Sender",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
        },
    )
    receiver: tuple[PartyType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Receiver",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    name: tuple[Name, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common",
        },
    )
    structure: tuple[PayloadStructureType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Structure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    data_provider: str | None = field(
        default=None,
        metadata={
            "name": "DataProvider",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "pattern": r".+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+",
        },
    )
    metadata_provider: str | None = field(
        default=None,
        metadata={
            "name": "MetadataProvider",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "pattern": r".+\.base\.MetadataProvider=.+:METADATA_PROVIDERS\(.+\).+",
        },
    )
    data_set_action: ActionType | None = field(
        default=None,
        metadata={
            "name": "DataSetAction",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    data_set_id: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DataSetID",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    extracted: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "Extracted",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    reporting_begin: XmlPeriod | XmlDate | XmlDateTime | str | None = (
        field(
            default=None,
            metadata={
                "name": "ReportingBegin",
                "type": "Element",
                "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                "pattern": r".{5}A1.*",
            },
        )
    )
    reporting_end: XmlPeriod | XmlDate | XmlDateTime | str | None = (
        field(
            default=None,
            metadata={
                "name": "ReportingEnd",
                "type": "Element",
                "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
                "pattern": r".{5}A1.*",
            },
        )
    )
    embargo_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "EmbargoDate",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    source: tuple[TextType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
