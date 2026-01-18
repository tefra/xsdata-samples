from dataclasses import dataclass, field
from typing import Optional

from crossref.models.gov.nih.nlm.ncbi.jats1.custom_meta_group import (
    CustomMetaGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.extended_by import ExtendedBy
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta_base_tagset import (
    ProcessingMetaBaseTagset,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta_mathml_version import (
    ProcessingMetaMathmlVersion,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta_table_model import (
    ProcessingMetaTableModel,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.processing_meta_tagset_family import (
    ProcessingMetaTagsetFamily,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.restricted_by import RestrictedBy

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class ProcessingMeta:
    """
    <div> <h3>Processing Metadata Model</h3> </div>.
    """

    class Meta:
        name = "processing-meta"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    restricted_by: list[RestrictedBy] = field(
        default_factory=list,
        metadata={
            "name": "restricted-by",
            "type": "Element",
        },
    )
    extended_by: list[ExtendedBy] = field(
        default_factory=list,
        metadata={
            "name": "extended-by",
            "type": "Element",
        },
    )
    custom_meta_group: list[CustomMetaGroup] = field(
        default_factory=list,
        metadata={
            "name": "custom-meta-group",
            "type": "Element",
        },
    )
    base_tagset: ProcessingMetaBaseTagset | None = field(
        default=None,
        metadata={
            "name": "base-tagset",
            "type": "Attribute",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    math_representation: list[str] = field(
        default_factory=list,
        metadata={
            "name": "math-representation",
            "type": "Attribute",
            "tokens": True,
        },
    )
    mathml_version: ProcessingMetaMathmlVersion | None = field(
        default=None,
        metadata={
            "name": "mathml-version",
            "type": "Attribute",
        },
    )
    table_model: ProcessingMetaTableModel | None = field(
        default=None,
        metadata={
            "name": "table-model",
            "type": "Attribute",
        },
    )
    tagset_family: ProcessingMetaTagsetFamily | None = field(
        default=None,
        metadata={
            "name": "tagset-family",
            "type": "Attribute",
        },
    )
    base: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
