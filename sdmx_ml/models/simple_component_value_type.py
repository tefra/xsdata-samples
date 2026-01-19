from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.exclude_root_type import ExcludeRootType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class SimpleComponentValueType:
    """
    SimpleValueType contains a simple value for a component, and if that
    value is from a code list, the ability to indicate that child codes in
    a simple hierarchy are part of the value set of the component for the
    region.

    :ivar value:
    :ivar cascade_values: The cascadeValues attribute, if true,
        indicates that if the value is taken from a code all child codes
        in a simple hierarchy are understood be included in the region.
    :ivar lang: The xml:lang attribute specifies a language code for the
        value. This is used when the component value support multi-
        lingual values.
    :ivar valid_from:
    :ivar valid_to:
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    cascade_values: bool | ExcludeRootType = field(
        default=False,
        metadata={
            "name": "cascadeValues",
            "type": "Attribute",
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    valid_from: None | XmlPeriod | XmlDate | XmlDateTime | str = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
    valid_to: None | XmlPeriod | XmlDate | XmlDateTime | str = field(
        default=None,
        metadata={
            "name": "validTo",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )
