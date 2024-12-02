from dataclasses import dataclass, field
from typing import Optional, Union

from crossref.models.gov.nih.nlm.ncbi.jats1.abbrev import (
    Abstract,
    Address,
    Alternatives,
    Answer,
    AnswerSet,
    Array,
    BlockAlternatives,
    BoxedText,
    ChemStructWrap,
    Code,
    DefList,
    DispFormula,
    DispFormulaGroup,
    DispQuote,
    Explanation,
    Fig,
    FigGroup,
    Graphic,
    KwdGroup,
    Label,
    List,
    Media,
    P,
    Preformat,
    Question,
    QuestionWrap,
    QuestionWrapGroup,
    RefList,
    RelatedArticle,
    RelatedObject,
    Speech,
    Statement,
    SubjGroup,
    SupplementaryMaterial,
    TableWrap,
    TableWrapGroup,
    Title,
    VerseGroup,
)
from crossref.models.gov.nih.nlm.ncbi.jats1.app import App
from crossref.models.gov.nih.nlm.ncbi.jats1.object_id import ObjectId
from crossref.models.gov.nih.nlm.ncbi.jats1.tex_math import TexMath
from crossref.models.org.w3.pkg_1998.math.math_ml.math import Math
from crossref.models.xml.lang_value import LangValue

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


@dataclass
class AppGroup:
    """
    <div> <h3>Appendix Group</h3> </div>
    """

    class Meta:
        name = "app-group"
        namespace = "http://www.ncbi.nlm.nih.gov/JATS1"

    object_id: list[ObjectId] = field(
        default_factory=list,
        metadata={
            "name": "object-id",
            "type": "Element",
        },
    )
    label: Optional[Label] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    title: Optional[Title] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    abstract: list[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: list[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: list[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    address: list[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: list[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: list[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: list[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: list[Array] = field(
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
    explanation: list[Explanation] = field(
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
    question: list[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: list[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: list[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
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
    disp_formula: list[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: list[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: list[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: list[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: list[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: list[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: list[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: list[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: list[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: list[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: list[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: list[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    app: list[App] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: list[RefList] = field(
        default_factory=list,
        metadata={
            "name": "ref-list",
            "type": "Element",
        },
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "content-type",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specific_use: Optional[str] = field(
        default=None,
        metadata={
            "name": "specific-use",
            "type": "Attribute",
        },
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
    lang: Optional[Union[str, LangValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )
