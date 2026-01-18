from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.annotable_type import AnnotableType
from sdmx_ml.models.member_selection_type import MemberSelectionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class RegionType(AnnotableType):
    """
    RegionType is an abstract type which defines a generic constraint
    region.

    This type can be refined to define regions for data or metadata sets. A
    region is defined by a collection of key values - each of which a
    collection of values for a component which disambiguates data (i.e.
    dimensions of a dataset). For each region, a collection of attribute
    values can be provided. Taken together, the key values and attributes
    serve to identify or describe a subset of a data or metadata set.
    Finally, the region can flagged as being included or excluded, although
    this flag only makes sense when the region is used in a particular
    context.

    :ivar key_value: KeyValue contains a reference to a component which
        disambiguates the data (i.e. a dimension) and provides a
        collection of values for the component. The collection of values
        can be flagged as being inclusive or exclusive to the region
        being defined. Any key component that is not included is assumed
        to be wild carded, which is to say that the cube includes all
        possible values for the un-referenced key components. Further,
        this assumption applies to the values of the components as well.
        The values for any given component can only be sub-setted in the
        region by explicit inclusion or exclusion. For example, a
        dimension X which has the possible values of 1, 2, 3 is assumed
        to have all of these values if a key value is not defined. If a
        key value is defined with an inclusion attribute of true and the
        values of 1 and 2, the only the values of 1 and 2 for dimension
        X are included in the definition of the region. If the key value
        is defined with an inclusion attribute of false and the value of
        1, then the values of 2 and 3 for dimension X are included in
        the definition of the region. Note that any given key component
        must only be referenced once in the region.
    :ivar component: Component contains a reference to a component (data
        attribute, metadata attribute, or measure) and provides a
        collection of values for the referenced component. This serves
        to state that for the key which defines the region, the
        components that are specified here have or do not have
        (depending on the include attribute of the value set) the values
        provided. It is possible to provide a component reference
        without specifying values, for the purpose of stating the
        component is absent (include = false) or present with an
        unbounded set of values. As opposed to key components, which are
        assumed to be wild carded if absent, no assumptions are made
        about the absence of a component. Only components which are
        explicitly stated to be present or absent from the region will
        be know. All unstated components for the set cannot be assumed
        to absent or present.
    :ivar include: The include attribute indicates that the region is to
        be included or excluded within the context in which it is
        defined. For example, if the regions is defined as part of a
        content constraint, the exclude flag would mean the data
        identified by the region is not present.
    :ivar valid_from:
    :ivar valid_to:
    """

    key_value: tuple[MemberSelectionType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "KeyValue",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    component: tuple[MemberSelectionType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Component",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    include: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    valid_from: XmlPeriod | XmlDate | XmlDateTime | str | None = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
    valid_to: XmlPeriod | XmlDate | XmlDateTime | str | None = field(
        default=None,
        metadata={
            "name": "validTo",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
