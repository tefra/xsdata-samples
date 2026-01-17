from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.comp_type import CompType
from sdmx_ml.models.metadata_set_type import MetadataSetType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific"
)


@dataclass(frozen=True)
class ObsType(AnnotableType):
    """
    <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">ObsType
    is the abstract type which defines the structure of a grouped or
    un-grouped observation.

    The observation must be provided a key, which is either a value for the
    dimension which is declared to be at the observation level if the
    observation is grouped, or a full set of values for all dimensions in
    the data structure definition if the observation is un-grouped. This
    key should disambiguate the observation within the context in which it
    is defined (e.g. there should not be another observation with the same
    dimension value in a series). The observation can contain an observed
    value and/or attribute values.</ns1:p> <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">Data
    structure definition schemas will derive a type or types based on this
    that is specific to the data structure definition and the variation of
    the format being expressed in the schema. The dimension value(s) which
    make up the key and the data and metadata attribute values associated
    with the key dimension(s) or the primary measure will be represented
    with XML attributes. This is specified in the content model with the
    declaration of anyAttributes in the "local" namespace. The derived
    observation type will refine this structure so that the attributes are
    explicit. The XML attributes will be given a name based on the
    attribute's identifier. These XML attributes will be unqualified
    (meaning they do not have a namespace associated with them). The
    dimension XML attribute(s) will be required while the attribute XML
    attributes will be optional. To allow for generic processing, it is
    required that the only unqualified XML attributes in the derived
    observation type be for the observation dimension(s) and attributes
    declared in the data structure definition. If additional attributes are
    required, these should be qualified with a namespace so that a generic
    application can easily distinguish them as not being meant to represent
    a data structure definition dimension or attribute.</ns1:p>.

    :ivar comp: Comp contains the details of observation measures or
        attributes that have complex representation and cannot be
        expressed as XML attributes.
    :ivar metadata: Allows for attachment of reference metadata against
        to the observation.
    :ivar type_value: The type attribute is used when the derived format
        requires that explicit measure be used. In this case, the
        derived type based on the measure will fix this value to be the
        identification of the measure concept. This will not be
        required, but since it is fixed it will be available in the post
        validation information set which will allow for generic
        processing of the data. If explicit measures are not used, then
        the derived type will prohibit the use of this attribute.
    :ivar time_period: The TIME_PERIOD attribute is an explicit
        attribute for the time dimension. This is declared in the base
        schema since it has a fixed identifier and representation. The
        derived series type will either require or prohibit this
        attribute, depending on whether time is the observation
        dimension. If the time dimension specifies a more specific
        representation of time the derived type will restrict the type
        definition to the appropriate type.
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
    metadata: Optional[MetadataSetType] = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    time_period: Optional[Union[XmlPeriod, XmlDate, XmlDateTime, str]] = field(
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
