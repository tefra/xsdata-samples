from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from sdmx_ml.models.hierarchical_code_base_type import HierarchicalCodeBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class HierarchicalCodeType(HierarchicalCodeBaseType):
    """HierarchicalCodeType describes the structure of a hierarchical code.

    A hierarchical code provides for a reference to a code that is
    referenced within the hierarchical code list via either a complete
    reference to a code through either a URN or full set of reference
    fields. Codes are arranged in a hierarchy by this reference. Note
    that it is possible to reference a single code such that it has
    multiple parents within the hierarchy. Further, the hierarchy may or
    may not be a leveled one.

    :ivar code: Code provides a complete, explicit reference to a code
        through either its URN, or a complete reference to the codelist
        and code.
    :ivar hierarchical_code: HierarchicalCode is used to nest referenced
        codes into a value based hierarchy.
    :ivar level: Level references a formal level defined within the
        hierarchy which defines this hierarchical code. This is only
        necessary if the nesting depth of the hierarchical code does not
        correspond to the nesting depth of the level to which it belongs
        (i.e. the hieararchical code is to skip down a level).
        Otherwise, the code is assumed to exist at the level in which
        the nesting depth of the level matches the nesting depth of the
        code.
    :ivar valid_from: The validFrom attriubte indicates the point in
        time in which the hiearchical code became effective. This can be
        used to track the historicity of codes changing over time.
    :ivar valid_to: The validTo attriubte indicates the point in time in
        which the hiearchical code became no longer effective. This can
        be used to track the historicity of codes changing over time.
    """

    code: Optional[str] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.codelist\.Code=.+",
        },
    )
    hierarchical_code: tuple["HierarchicalCodeType", ...] = field(
        default_factory=tuple,
        metadata={
            "name": "HierarchicalCode",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    level: Optional[str] = field(
        default=None,
        metadata={
            "name": "Level",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    valid_from: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
        },
    )
    valid_to: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "validTo",
            "type": "Attribute",
        },
    )
