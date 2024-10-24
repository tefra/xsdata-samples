from dataclasses import dataclass, field
from typing import List, Optional, Union

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
    ListType,
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

    object_id: List[ObjectId] = field(
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
    abstract: List[Abstract] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    kwd_group: List[KwdGroup] = field(
        default_factory=list,
        metadata={
            "name": "kwd-group",
            "type": "Element",
        },
    )
    subj_group: List[SubjGroup] = field(
        default_factory=list,
        metadata={
            "name": "subj-group",
            "type": "Element",
        },
    )
    address: List[Address] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    alternatives: List[Alternatives] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer: List[Answer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    answer_set: List[AnswerSet] = field(
        default_factory=list,
        metadata={
            "name": "answer-set",
            "type": "Element",
        },
    )
    array: List[Array] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    block_alternatives: List[BlockAlternatives] = field(
        default_factory=list,
        metadata={
            "name": "block-alternatives",
            "type": "Element",
        },
    )
    boxed_text: List[BoxedText] = field(
        default_factory=list,
        metadata={
            "name": "boxed-text",
            "type": "Element",
        },
    )
    chem_struct_wrap: List[ChemStructWrap] = field(
        default_factory=list,
        metadata={
            "name": "chem-struct-wrap",
            "type": "Element",
        },
    )
    code: List[Code] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    explanation: List[Explanation] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig: List[Fig] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fig_group: List[FigGroup] = field(
        default_factory=list,
        metadata={
            "name": "fig-group",
            "type": "Element",
        },
    )
    graphic: List[Graphic] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    media: List[Media] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    preformat: List[Preformat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question: List[Question] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    question_wrap: List[QuestionWrap] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap",
            "type": "Element",
        },
    )
    question_wrap_group: List[QuestionWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "question-wrap-group",
            "type": "Element",
        },
    )
    supplementary_material: List[SupplementaryMaterial] = field(
        default_factory=list,
        metadata={
            "name": "supplementary-material",
            "type": "Element",
        },
    )
    table_wrap: List[TableWrap] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap",
            "type": "Element",
        },
    )
    table_wrap_group: List[TableWrapGroup] = field(
        default_factory=list,
        metadata={
            "name": "table-wrap-group",
            "type": "Element",
        },
    )
    disp_formula: List[DispFormula] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula",
            "type": "Element",
        },
    )
    disp_formula_group: List[DispFormulaGroup] = field(
        default_factory=list,
        metadata={
            "name": "disp-formula-group",
            "type": "Element",
        },
    )
    def_list: List[DefList] = field(
        default_factory=list,
        metadata={
            "name": "def-list",
            "type": "Element",
        },
    )
    list_value: List[ListType] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
        },
    )
    tex_math: List[TexMath] = field(
        default_factory=list,
        metadata={
            "name": "tex-math",
            "type": "Element",
        },
    )
    math: List[Math] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/1998/Math/MathML",
        },
    )
    p: List[P] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    related_article: List[RelatedArticle] = field(
        default_factory=list,
        metadata={
            "name": "related-article",
            "type": "Element",
        },
    )
    related_object: List[RelatedObject] = field(
        default_factory=list,
        metadata={
            "name": "related-object",
            "type": "Element",
        },
    )
    disp_quote: List[DispQuote] = field(
        default_factory=list,
        metadata={
            "name": "disp-quote",
            "type": "Element",
        },
    )
    speech: List[Speech] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    statement: List[Statement] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    verse_group: List[VerseGroup] = field(
        default_factory=list,
        metadata={
            "name": "verse-group",
            "type": "Element",
        },
    )
    app: List[App] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref_list: List[RefList] = field(
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
