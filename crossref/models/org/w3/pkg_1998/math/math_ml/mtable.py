from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union
from crossref.models.org.w3.pkg_1998.math.math_ml.columnalignstyle import Columnalignstyle
from crossref.models.org.w3.pkg_1998.math.math_ml.common_pres_att_value import CommonPresAttValue
from crossref.models.org.w3.pkg_1998.math.math_ml.linestyle import Linestyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mlabeledtr import Mlabeledtr
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_attributes_displaystyle import MtableAttributesDisplaystyle
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_attributes_equalcolumns import MtableAttributesEqualcolumns
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_attributes_equalrows import MtableAttributesEqualrows
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_attributes_side import MtableAttributesSide
from crossref.models.org.w3.pkg_1998.math.math_ml.mtable_attributes_value import MtableAttributesValue
from crossref.models.org.w3.pkg_1998.math.math_ml.mtr import Mtr
from crossref.models.org.w3.pkg_1998.math.math_ml.verticalalign import Verticalalign

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass
class Mtable:
    class Meta:
        name = "mtable"
        namespace = "http://www.w3.org/1998/Math/MathML"

    mtr: List[Mtr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mlabeledtr: List[Mlabeledtr] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    xref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    class_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Attribute",
            "tokens": True,
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    mathcolor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    mathbackground: Optional[Union[str, CommonPresAttValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((#[0-9a-fA-F]{3}([0-9a-fA-F]{3})?)|[aA][qQ][uU][aA]|[bB][lL][aA][cC][kK]|[bB][lL][uU][eE]|[fF][uU][cC][hH][sS][iI][aA]|[gG][rR][aA][yY]|[gG][rR][eE][eE][nN]|[lL][iI][mM][eE]|[mM][aA][rR][oO][oO][nN]|[nN][aA][vV][yY]|[oO][lL][iI][vV][eE]|[pP][uU][rR][pP][lL][eE]|[rR][eE][dD]|[sS][iI][lL][vV][eE][rR]|[tT][eE][aA][lL]|[wW][hH][iI][tT][eE]|[yY][eE][lL][lL][oO][wW])\s*",
        }
    )
    align: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*(top|bottom|center|baseline|axis)(\s+-?[0-9]+)?\s*",
        }
    )
    rowalign: List[Verticalalign] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    columnalign: List[Columnalignstyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    groupalign: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(\s*\{\s*(left|center|right|decimalpoint)(\s+(left|center|right|decimalpoint))*\})*\s*",
        }
    )
    alignmentscope: List[MtableAttributesValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    columnwidth: List[MtableAttributesValue] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    width: Optional[Union[str, MtableAttributesValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
    rowspacing: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        }
    )
    columnspacing: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
            "tokens": True,
        }
    )
    rowlines: List[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    columnlines: List[Linestyle] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        }
    )
    frame: Optional[Linestyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    framespacing: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "length": 2,
            "tokens": True,
        }
    )
    equalrows: Optional[MtableAttributesEqualrows] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    equalcolumns: Optional[MtableAttributesEqualcolumns] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    displaystyle: Optional[MtableAttributesDisplaystyle] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    side: Optional[MtableAttributesSide] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    minlabelspacing: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\s*((-?[0-9]*([0-9]\.?|\.[0-9])[0-9]*(e[mx]|in|cm|mm|p[xtc]|%)?)|(negative)?((very){0,2}thi(n|ck)|medium)mathspace)\s*",
        }
    )
