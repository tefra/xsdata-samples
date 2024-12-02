from dataclasses import dataclass, field

from sdmx_ml.models.codelist_base_type import CodelistBaseType
from sdmx_ml.models.codelist_extension_type import CodelistExtensionType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CodelistType(CodelistBaseType):
    """
    :ivar codelist_extension: CodelistExtension allows for the extension
        of codelists by referencing the codelists to be extended and
        providing inclusion/exclusion rules for selecting the codes to
        extend. The order of these is important as it is indicates the
        order of precedence of the extended codelists for conflict
        resolution of codes. However, the prefix property can be used to
        ensure uniqueness of inherited codes in the extending codelist,
        in case conflicting codes must be included.
    """

    codelist_extension: tuple[CodelistExtensionType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CodelistExtension",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
