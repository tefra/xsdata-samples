from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.action_type import ActionType
from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.atts_type import AttsType
from sdmx_ml.models.group_type_abstract import GroupTypeAbstract
from sdmx_ml.models.metadata_set_type import MetadataSetType
from sdmx_ml.models.obs_type import ObsType
from sdmx_ml.models.series_type import SeriesType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific"
)


@dataclass(frozen=True)
class DataSetType(AnnotableType):
    """
    <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">DataSetType
    is the abstract type which defines the base structure for any data
    structure definition specific data set.

    A derived data set type will be created that is specific to a data
    structure definition and the details of the organisation of the data
    (i.e. which dimension is the observation dimension). Data is organised
    into either a collection of series (grouped observations) or a
    collection of un-grouped observations. The derived data set type will
    restrict this choice to be either grouped or un-grouped observations.
    If this dimension is "AllDimensions" then the derived data set type
    must consist of a collection of un-grouped observations; otherwise the
    data set will contain a collection of series with the observations in
    the series disambiguated by the specified dimension at the observation
    level. This data set is capable of containing data (observed values)
    and/or documentation (data and metadata attribute values) and can be
    used for incremental updates and deletions (i.e. only the relevant
    updates or deletes are exchanged). It is assumed that each series or
    un-grouped observation will be distinct in its purpose. For example, if
    series contains both data and documentation, it assumed that each
    series will have a unique key. If the series contains only data or only
    documentation, then it is possible that another series with the same
    key might exist, but with not with the same purpose (i.e. to provide
    data or documentation) as the first series.</ns1:p> <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">This
    base type is designed such that derived types can be processed in a
    generic manner; it assures that data structure definition specific data
    will have a consistent structure. The group, series, obs, and atts
    elements are unqualified, meaning that they are not qualified with a
    namespace in an instance. This means that in the derived data set
    types, the elements will always be the same, regardless of the target
    namespace of the schemas which defines these derived types. This allows
    for consistent processing of the structure without regard to what the
    namespace might be for the data structure definition specific
    schema.</ns1:p>.

    :ivar data_provider: DataProvider contains a reference to the
        provider for the data set.
    :ivar choice:
    :ivar metadata: Allows for attachment of reference metadata against
        to the data set.
    :ivar structure_ref: The structureRef contains a reference to a
        structural specification in the header of a data or reference
        metadata message. The structural specification details which
        structure the data or reference metadata conforms to, as well as
        providing additional information such as how the data is
        structure (e.g. which dimension occurs at the observation level
        for a data set).
    :ivar set_id: The setID provides an identification of the data or
        metadata set.
    :ivar action: The action attribute indicates whether the file is
        appending, replacing, or deleting.
    :ivar reporting_begin_date: The reportingBeginDate indicates the
        inclusive start time of the data reported in the data or
        metadata set.
    :ivar reporting_end_date: The reportingEndDate indicates the
        inclusive end time of the data reported in the data or metadata
        set.
    :ivar valid_from_date: The validFromDate indicates the inclusive
        start time indicating the validity of the information in the
        data or metadata set.
    :ivar valid_to_date: The validToDate indicates the inclusive end
        time indicating the validity of the information in the data or
        metadata set.
    :ivar publication_year: The publicationYear holds the ISO 8601 four-
        digit year.
    :ivar publication_period: The publicationPeriod specifies the period
        of publication of the data or metadata in terms of whatever
        provisioning agreements might be in force (i.e., "Q1 2005" if
        that is the time of publication for a data set published on a
        quarterly basis).
    :ivar local_attributes:
    """

    data_provider: str | None = field(
        default=None,
        metadata={
            "name": "DataProvider",
            "type": "Element",
            "namespace": "",
            "pattern": r".+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+",
        },
    )
    choice: tuple[
        AttsType | GroupTypeAbstract | SeriesType | ObsType, ...
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Atts",
                    "type": AttsType,
                    "namespace": "",
                },
                {
                    "name": "Group",
                    "type": GroupTypeAbstract,
                    "namespace": "",
                },
                {
                    "name": "Series",
                    "type": SeriesType,
                    "namespace": "",
                },
                {
                    "name": "Obs",
                    "type": ObsType,
                    "namespace": "",
                },
            ),
        },
    )
    metadata: MetadataSetType | None = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "",
        },
    )
    structure_ref: str | None = field(
        default=None,
        metadata={
            "name": "structureRef",
            "type": "Attribute",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific",
            "required": True,
        },
    )
    set_id: str | None = field(
        default=None,
        metadata={
            "name": "setID",
            "type": "Attribute",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    action: ActionType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific",
        },
    )
    reporting_begin_date: XmlPeriod | XmlDate | XmlDateTime | None = (
        field(
            default=None,
            metadata={
                "name": "reportingBeginDate",
                "type": "Attribute",
                "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific",
            },
        )
    )
    reporting_end_date: XmlPeriod | XmlDate | XmlDateTime | None = (
        field(
            default=None,
            metadata={
                "name": "reportingEndDate",
                "type": "Attribute",
                "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific",
            },
        )
    )
    valid_from_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "validFromDate",
            "type": "Attribute",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific",
        },
    )
    valid_to_date: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "validToDate",
            "type": "Attribute",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific",
        },
    )
    publication_year: XmlPeriod | None = field(
        default=None,
        metadata={
            "name": "publicationYear",
            "type": "Attribute",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific",
        },
    )
    publication_period: XmlPeriod | XmlDate | XmlDateTime | str | None = field(
        default=None,
        metadata={
            "name": "publicationPeriod",
            "type": "Attribute",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific",
            "pattern": r".{5}A1.*",
        },
    )
    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )
