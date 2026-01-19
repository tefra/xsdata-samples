from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.region_type import RegionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class MetadataTargetRegionType(RegionType):
    """
    MetadataTargetRegionType defines the structure of a metadata target
    region.

    A metadata target region must define the report structure and the
    metadata target from that structure on which the region is based. This
    type is based on the abstract RegionType and simply refines the key and
    attribute values to conform with what is applicable for target objects
    and metadata attributes, respectively. See the documentation of the
    base type for more details on how a region is defined.

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
    :ivar annotations:
    """

    key_value: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    annotations: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
