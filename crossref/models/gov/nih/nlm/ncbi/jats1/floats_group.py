from __future__ import annotations

from dataclasses import dataclass, field

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
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


@dataclass(kw_only=True)
class FloatsGroup:
    """
    <div> <h3>Floats Group</h3> </div>.
    """

    class Meta:
        name = "floats-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: list[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: list[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: list[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: list[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: list[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: list[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: list[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: list[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: list[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    supplementary_material: list[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: list[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: list[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    base: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
