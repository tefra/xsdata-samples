from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.comp_type import CompType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific"
)


@dataclass(frozen=True, kw_only=True)
class AttsType(AnnotableType):
    """
    <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">AttsType
    is the abstract type which defines a structure which is used to group a
    collection of data or metadata attributes which have a key in common.

    The key for a attribute collection is a subset of the dimension defined
    in the data structure definition. This is also used for data set level
    attributes (i.e. those with an attribute relationship of none). In this
    case, the subset of dimensions is empty.</ns1:p> <ns1:p
    xmlns:ns1="http://www.sdmx.org/resources/sdmxml/schemas/v3_0/data/structurespecific">Data
    structure definition schemas will derive a type based on this that is
    specific to the data structure definition. The dimension values which
    make up the key will be represented with local (non-namespace
    qualified) XML attributes. The metadata attribute values associated
    with the key dimensions will be expressed as XML local (non-namespace
    qualified) attributes if they are simple values (e.g. enumerated,
    dates, numbers) and are not repeatable. Metadata attributes that are
    repeatable, or do not have simple values (e.g. text) will be expressed
    using the Comp element. This dimensions and simple attributes are
    specified in the content model with the declaration of anyAttributes in
    the "local" namespace. The derived series type will refine this
    structure so that the attributes are explicit. The XML attributes will
    be given a name based on the attribute's identifier. These XML
    attributes will be unqualified (meaning they do not have a namespace
    associated with them). The dimension XML attributes will be required
    while the attribute XML attributes will be optional. To allow for
    generic processing, it is required that the only unqualified XML
    attributes in the derived group type be for the series dimensions and
    attributes declared in the data structure definition. If additional
    attributes are required, these should be qualified with a namespace so
    that a generic application can easily distinguish them as not being
    meant to represent a data structure definition dimension or
    attribute.</ns1:p>.

    :ivar comp: Comp contains the details of the data or metadata
        attributes that have complex representation and cannot be
        expressed as XML attributes.
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
    time_period: None | XmlPeriod | XmlDate | XmlDateTime | str = field(
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
