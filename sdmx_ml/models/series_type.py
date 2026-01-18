from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.comp_type import CompType
from sdmx_ml.models.metadata_set_type import MetadataSetType
from sdmx_ml.models.obs_type import ObsType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific"
)


@dataclass(frozen=True)
class SeriesType(AnnotableType):
    """
    <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">SeriesType
    is the abstract type which defines a structure which is used to group a
    collection of observations which have a key in common.

    The key for a series is every dimension defined in the data structure
    definition, save the dimension declared to be at the observation level
    for this data set. In addition to observations, values can be provided
    for data and metadata attributes which are associated with the
    dimensions which make up this series key (so long as the attributes do
    not specify a group attachment or also have an relationship with the
    observation dimension). It is possible for the series to contain only
    observations or only attribute values, or both.</ns1:p> <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">Data
    structure definition schemas will derive a type based on this that is
    specific to the data structure definition and the variation of the
    format being expressed in the schema. Both the dimension values which
    make up the key and the attribute values associated with the key
    dimensions will be represented with XML attributes. This is specified
    in the content model with the declaration of anyAttributes in the
    "local" namespace. The derived series type will refine this structure
    so that the attributes are explicit. The XML attributes will be given a
    name based on the attribute's identifier. These XML attributes will be
    unqualified (meaning they do not have a namespace associated with
    them). The dimension XML attributes will be required while the
    attribute XML attributes will be optional. To allow for generic
    processing, it is required that the only unqualified XML attributes in
    the derived group type be for the series dimensions and attributes
    declared in the data structure definition. If additional attributes are
    required, these should be qualified with a namespace so that a generic
    application can easily distinguish them as not being meant to represent
    a data structure definition dimension or attribute.</ns1:p>.

    :ivar comp: Comp contains the details of series level attributes
        that have complex representation and cannot be expressed as XML
        attributes.
    :ivar obs:
    :ivar metadata: Allows for attachment of reference metadata against
        to the series.
    :ivar time_period: The TIME_PERIOD attribute is an explict attribute
        for the time dimension. This is declared in the base schema
        since it has a fixed identifier and representation. The derived
        series type will either require or prohibit this attribute,
        depending on whether time is the observation dimension. If the
        time dimension specifies a more specific representation of time
        the derived type will restrict the type definition to the
        appropriate type.
    :ivar local_attributes:
    """

    comp: tuple[CompType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Comp",
            "type": "Element",
            "namespace": "",
        },
    )
    obs: tuple[ObsType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Obs",
            "type": "Element",
            "namespace": "",
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
    time_period: XmlPeriod | XmlDate | XmlDateTime | str | None = field(
        default=None,
        metadata={
            "name": "TIME_PERIOD",
            "type": "Attribute",
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
