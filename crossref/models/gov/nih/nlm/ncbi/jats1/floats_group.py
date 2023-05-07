from dataclasses import dataclass, field
from typing import List, Optional
from crossref.models.gov.nih.nlm.ncbi.jats1.annotation import (
    Alternatives,
    BlockAlternatives,
    BoxedText,
    ChemStructWrap,
    Code,
    Fig,
    FigGroup,
    Graphic,
    Media,
    Preformat,
    SupplementaryMaterial,
    TableWrap,
    TableWrapGroup,
)

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class FloatsGroup:
    """<div>

    <h3>Floats Group</h3> </div>
    """
    class Meta:
        name = "floats-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alternatives: List[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        }
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        }
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        }
    )
    code: List[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        }
    )
    graphic: List[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        }
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        }
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
