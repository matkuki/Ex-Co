
# -*- coding: utf-8 -*-

"""
    Ex.Co. LICENSE :
        This file is part of Ex.Co..

        Ex.Co. is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        Ex.Co. is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with Ex.Co..  If not, see <http://www.gnu.org/licenses/>.


    PYTHON LICENSE :
        "Python" and the Python logos are trademarks or registered trademarks of the Python Software Foundation,
        used by Ex.Co. with permission from the Foundation


    Cython LICENSE:
        Cython is freely available under the open source Apache License


    PyQt4 LICENSE :
        PyQt4 is licensed under the GNU General Public License version 3
    PyQt Alternative Logo LICENSE:
        The PyQt Alternative Logo is licensed under Creative Commons CC0 1.0 Universal Public Domain Dedication


    Qt Logo LICENSE:
        The Qt logo is copyright of Digia Plc and/or its subsidiaries.
        Digia, Qt and their respective logos are trademarks of Digia Corporation in Finland and/or other countries worldwide.


    Tango Icons LICENSE:
        The Tango base icon theme is released to the Public Domain.
        The Tango base icon theme is made possible by the Tango Desktop Project.
    
    My Tango Style Icons LICENSE:
        The Tango icons I created are released under the GNU General Public License version 3.
    
    
    Eric6 LICENSE:
        Eric6 IDE is licensed under the GNU General Public License version 3


    Nuitka LICENSE:
        Nuitka is a Python compiler compatible with Ex.Co..
        Nuitka is freely available under the open source Apache License.
"""

##  FILE DESCRIPTION:
##      'Midnight Commander' theme made for Seba

import PyQt4.QtGui


Form = "#295a88"
Cursor = PyQt4.QtGui.QColor(0xffeeeeec)


class FoldMargin:
    ForeGround = PyQt4.QtGui.QColor(0xff4096bf)
    BackGround = PyQt4.QtGui.QColor(0xff3476a3)


class LineMargin:
    ForeGround = PyQt4.QtGui.QColor(0xffeeeeec)
    BackGround = PyQt4.QtGui.QColor(0xff3465a4)


class Indication:
    Font = "#e6e6e6"
    ActiveBackGround = "#112435"
    ActiveBorder = "#e6e6e6"
    PassiveBackGround = "#295a88"
    PassiveBorder = "#33aaff"


class TextDifferColors:
    Indicator_Unique_1_Color = PyQt4.QtGui.QColor(0x72, 0x9f, 0xcf, 80)
    Indicator_Unique_2_Color = PyQt4.QtGui.QColor(0xad, 0x7f, 0xa8, 80)
    Indicator_Similar_Color = PyQt4.QtGui.QColor(0x8a, 0xe2, 0x34, 80)

    
class Font:
    Default = PyQt4.QtGui.QColor(0xffeeeeec)
    
    class Repl:
        """
        THE MESSAGE COLORS ARE: 0xBBGGRR (BB-blue,GG-green,RR-red)
        """
        Error = 0x0000ff
        Warning = 0xe4761f
        Success = 0x007f00
        Diff_Unique_1 = 0xcf9f72
        Diff_Unique_2 = 0xa87fad
        Diff_Similar = 0x069a4e
    
    class Ada:
        Default = ('Courier', 0xffeeeeec, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        Procedure = ('Courier', 0xff5abcd8, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Type = ('Courier', 0xffa3c2da, 10, None)
        Package = ('Courier', 0xfff5b0cb, 10, None)
    
    class Nim:
        Default = ('Courier', 0xffeeeeec, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        BasicKeyword = ('Courier', 0xffa3c2da, 10, True)
        TopKeyword = ('Courier', 0xffabb5c0, 10, True)
        String = ('Courier', 0xffc4bbb8, 10, None)
        LongString = ('Courier', 0xfff5b0cb, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xff7f7f7f, 10, None)
        Unsafe = ('Courier', 0xffc00000, 10, True)
        Type = ('Courier', 0xffe8e800, 10, True)
        DocumentationComment = ('Courier', 0xffc75146, 10, None)
        Definition = ('Courier', 0xff74ccf4, 10, None)
        Class = ('Courier', 0xff5abcd8, 10, None)
        KeywordOperator = ('Courier', 0xffd891ff, 10, None)
        CharLiteral = ('Courier', 0xff00c8ff, 10, None)
        CaseOf = ('Courier', 0xffd5abff, 10, None)
        UserKeyword = ('Courier', 0xffff8040, 10, None)
        MultilineComment = ('Courier', 0xffad2e24, 10, None)
        MultilineDocumentation = ('Courier', 0xffea8c55, 10, None)
        Pragma = ('Courier', 0xffc07f40, 10, None)
    
    class RouterOS:
        Default = ('Courier', 0xffeeeeec, 10, True)
        Operator = ('Courier', 0xffB4B80A, 10, True)
        Comment = ('Courier', 0xff38B86B, 10, True)
        Keyword1 = ('Courier', 0xff32CD32, 10, True)
        Keyword2 = ('Courier', 0xffB9005C, 10, True)
        Keyword3 = ('Courier', 0xff74ccf4, 10, True)
    
    class Oberon:
        Default = ('Courier', 0xffeeeeec, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        Procedure = ('Courier', 0xff5abcd8, 10, None)
        Module = ('Courier', 0xfff5b0cb, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Type = ('Courier', 0xffa3c2da, 10, None)
    
    
    class AVS:
        BlockComment = ('Courier', 0xff6cab9d, 10, None)
        ClipProperty = ('Courier', 0xffa3c2da, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        Filter = ('Courier', 0xffa3c2da, 10, None)
        Function = ('Courier', 0xff74ccf4, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet6 = ('Courier', 0xffd5abff, 10, None)
        LineComment = ('Courier', 0xff6cab9d, 10, None)
        NestedBlockComment = ('Courier', 0xff6cab9d, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        Plugin = ('Courier', 0xff0080c0, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        TripleString = ('Courier', 0xffc4bbb8, 10, None)
    
    class Bash:
        Backticks = ('Courier', 0xff8ae234, 10, True)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc48e7b, 10, None)
        Error = ('Courier', 0xffaa0000, 10, True)
        HereDocumentDelimiter = ('Courier', 0xffeeeeec, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        ParameterExpansion = ('Courier', 0xffeeeeec, 10, None)
        Scalar = ('Courier', 0xfffce94f, 10, True)
        SingleQuotedHereDocument = ('Courier', 0xffc4bbb8, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
    
    class Batch:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        ExternalCommand = ('Courier', 0xffa3c2da, 10, None)
        HideCommandChar = ('Courier', 0xff7f7f00, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        Label = ('Courier', 0xffc4bbb8, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        Variable = ('Courier', 0xff800080, 10, None)
    
    class CMake:
        BlockForeach = ('Courier', 0xffa3c2da, 10, None)
        BlockIf = ('Courier', 0xffa3c2da, 10, None)
        BlockMacro = ('Courier', 0xffa3c2da, 10, None)
        BlockWhile = ('Courier', 0xffa3c2da, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        Function = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet3 = ('Courier', 0xffeeeeec, 10, None)
        Label = ('Courier', 0xffcc3300, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        StringLeftQuote = ('Courier', 0xffc4bbb8, 10, None)
        StringRightQuote = ('Courier', 0xffc4bbb8, 10, None)
        StringVariable = ('Courier', 0xffcc3300, 10, None)
        Variable = ('Courier', 0xffedff86, 10, None)
    
    class CPP:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffeeeeec, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffeeeeec, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffeeeeec, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffeeeeec, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet2 = ('Courier', 0xffeeeeec, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xffeeeeec, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class CSS:
        AtRule = ('Courier', 0xff7f7f00, 10, None)
        Attribute = ('Courier', 0xffedff86, 10, None)
        CSS1Property = ('Courier', 0xff0040e0, 10, None)
        CSS2Property = ('Courier', 0xff00a0e0, 10, None)
        CSS3Property = ('Courier', 0xffeeeeec, 10, None)
        ClassSelector = ('Courier', 0xffeeeeec, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffff0080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ExtendedCSSProperty = ('Courier', 0xffeeeeec, 10, None)
        ExtendedPseudoClass = ('Courier', 0xffeeeeec, 10, None)
        ExtendedPseudoElement = ('Courier', 0xffeeeeec, 10, None)
        IDSelector = ('Courier', 0xff74ccf4, 10, None)
        Important = ('Courier', 0xffff8000, 10, None)
        MediaRule = ('Courier', 0xff7f7f00, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PseudoClass = ('Courier', 0xffedff86, 10, None)
        PseudoElement = ('Courier', 0xffeeeeec, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Tag = ('Courier', 0xffa3c2da, 10, None)
        UnknownProperty = ('Courier', 0xffff0000, 10, None)
        UnknownPseudoClass = ('Courier', 0xffff0000, 10, None)
        Value = ('Courier', 0xffc4bbb8, 10, None)
        Variable = ('Courier', 0xffeeeeec, 10, None)
    
    class CSharp:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffeeeeec, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffeeeeec, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffeeeeec, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffeeeeec, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet2 = ('Courier', 0xffeeeeec, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xffeeeeec, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class CoffeeScript:
        BlockRegex = ('Courier', 0xff3f7f3f, 10, None)
        BlockRegexComment = ('Courier', 0xff6cab9d, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentBlock = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffeeeeec, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet2 = ('Courier', 0xffeeeeec, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        UUID = ('Courier', 0xffeeeeec, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class D:
        BackquoteString = ('Courier', 0xffeeeeec, 10, None)
        Character = ('Courier', 0xffc4bbb8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        CommentNested = ('Courier', 0xffa0c0a0, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordDoc = ('Courier', 0xffa3c2da, 10, None)
        KeywordSecondary = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet5 = ('Courier', 0xffeeeeec, 10, None)
        KeywordSet6 = ('Courier', 0xffeeeeec, 10, None)
        KeywordSet7 = ('Courier', 0xffeeeeec, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        RawString = ('Courier', 0xffeeeeec, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        Typedefs = ('Courier', 0xffa3c2da, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
    
    class Diff:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        Header = ('Courier', 0xfff5b0cb, 10, None)
        LineAdded = ('Courier', 0xffa3c2da, 10, None)
        LineChanged = ('Courier', 0xff7f7f7f, 10, None)
        LineRemoved = ('Courier', 0xff74ccf4, 10, None)
        Position = ('Courier', 0xffc4bbb8, 10, None)
    
    class Fortran:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Continuation = ('Courier', 0xffeeeeec, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DottedOperator = ('Courier', 0xffeeeeec, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ExtendedFunction = ('Courier', 0xffb04080, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        IntrinsicFunction = ('Courier', 0xffb00040, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        Label = ('Courier', 0xffe0c0e0, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
    
    class Fortran77:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Continuation = ('Courier', 0xffeeeeec, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DottedOperator = ('Courier', 0xffeeeeec, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ExtendedFunction = ('Courier', 0xffb04080, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        IntrinsicFunction = ('Courier', 0xffb00040, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        Label = ('Courier', 0xffe0c0e0, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
    
    class HTML:
        ASPAtStart = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptComment = ('Courier', 0xff6cab9d, 10, None)
        ASPJavaScriptCommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        ASPJavaScriptCommentLine = ('Courier', 0xff6cab9d, 10, None)
        ASPJavaScriptDefault = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPJavaScriptKeyword = ('Courier', 0xffa3c2da, 10, None)
        ASPJavaScriptNumber = ('Courier', 0xff74ccf4, 10, None)
        ASPJavaScriptRegex = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPJavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        ASPJavaScriptSymbol = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptUnclosedString = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptWord = ('Courier', 0xffeeeeec, 10, None)
        ASPPythonClassName = ('Courier', 0xff5abcd8, 10, None)
        ASPPythonComment = ('Courier', 0xff6cab9d, 10, None)
        ASPPythonDefault = ('Courier', 0xff808080, 10, None)
        ASPPythonDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPPythonFunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        ASPPythonIdentifier = ('Courier', 0xffeeeeec, 10, None)
        ASPPythonKeyword = ('Courier', 0xffa3c2da, 10, None)
        ASPPythonNumber = ('Courier', 0xff74ccf4, 10, None)
        ASPPythonOperator = ('Courier', 0xffeeeeec, 10, None)
        ASPPythonSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPPythonStart = ('Courier', 0xff808080, 10, None)
        ASPPythonTripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        ASPPythonTripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        ASPStart = ('Courier', 0xffeeeeec, 10, None)
        ASPVBScriptComment = ('Courier', 0xff008000, 10, None)
        ASPVBScriptDefault = ('Courier', 0xffeeeeec, 10, None)
        ASPVBScriptIdentifier = ('Courier', 0xff1f76e4, 10, None)
        ASPVBScriptKeyword = ('Courier', 0xff1f76e4, 10, None)
        ASPVBScriptNumber = ('Courier', 0xff008080, 10, None)
        ASPVBScriptStart = ('Courier', 0xffeeeeec, 10, None)
        ASPVBScriptString = ('Courier', 0xff800080, 10, None)
        ASPVBScriptUnclosedString = ('Courier', 0xff1f76e4, 10, None)
        ASPXCComment = ('Courier', 0xffeeeeec, 10, None)
        Attribute = ('Courier', 0xff008080, 10, None)
        CDATA = ('Courier', 0xffeeeeec, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        Entity = ('Courier', 0xff800080, 10, None)
        HTMLComment = ('Courier', 0xff808000, 10, None)
        HTMLDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        HTMLNumber = ('Courier', 0xff74ccf4, 10, None)
        HTMLSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        HTMLValue = ('Courier', 0xffff00ff, 10, None)
        JavaScriptComment = ('Courier', 0xff6cab9d, 10, None)
        JavaScriptCommentDoc = ('Courier', 0xff3f703f, 10, None)
        JavaScriptCommentLine = ('Courier', 0xff6cab9d, 10, None)
        JavaScriptDefault = ('Courier', 0xffeeeeec, 10, None)
        JavaScriptDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        JavaScriptKeyword = ('Courier', 0xffa3c2da, 10, None)
        JavaScriptNumber = ('Courier', 0xff74ccf4, 10, None)
        JavaScriptRegex = ('Courier', 0xffeeeeec, 10, None)
        JavaScriptSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        JavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        JavaScriptSymbol = ('Courier', 0xffeeeeec, 10, None)
        JavaScriptUnclosedString = ('Courier', 0xffeeeeec, 10, None)
        JavaScriptWord = ('Courier', 0xffeeeeec, 10, None)
        OtherInTag = ('Courier', 0xff800080, 10, None)
        PHPComment = ('Courier', 0xff999999, 10, None)
        PHPCommentLine = ('Courier', 0xff666666, 10, None)
        PHPDefault = ('Courier', 0xffc7dbf5, 10, None)
        PHPDoubleQuotedString = ('Courier', 0xff6cab9d, 10, None)
        PHPDoubleQuotedVariable = ('Courier', 0xffa3c2da, 10, None)
        PHPKeyword = ('Courier', 0xffc4bbb8, 10, None)
        PHPNumber = ('Courier', 0xffcc9900, 10, None)
        PHPOperator = ('Courier', 0xffeeeeec, 10, None)
        PHPSingleQuotedString = ('Courier', 0xff009f00, 10, None)
        PHPStart = ('Courier', 0xff5abcd8, 10, None)
        PHPVariable = ('Courier', 0xffa3c2da, 10, None)
        PythonClassName = ('Courier', 0xff5abcd8, 10, None)
        PythonComment = ('Courier', 0xff6cab9d, 10, None)
        PythonDefault = ('Courier', 0xff808080, 10, None)
        PythonDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        PythonFunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        PythonIdentifier = ('Courier', 0xffeeeeec, 10, None)
        PythonKeyword = ('Courier', 0xffa3c2da, 10, None)
        PythonNumber = ('Courier', 0xff74ccf4, 10, None)
        PythonOperator = ('Courier', 0xffeeeeec, 10, None)
        PythonSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        PythonStart = ('Courier', 0xff808080, 10, None)
        PythonTripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        PythonTripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        SGMLBlockDefault = ('Courier', 0xfffff5b2, 10, None)
        SGMLCommand = ('Courier', 0xff1f76e4, 10, None)
        SGMLComment = ('Courier', 0xff808000, 10, None)
        SGMLDefault = ('Courier', 0xff1f76e4, 10, None)
        SGMLDoubleQuotedString = ('Courier', 0xffedff86, 10, None)
        SGMLEntity = ('Courier', 0xff333333, 10, None)
        SGMLError = ('Courier', 0xffedff86, 10, None)
        SGMLParameter = ('Courier', 0xff006600, 10, None)
        SGMLParameterComment = ('Courier', 0xffeeeeec, 10, None)
        SGMLSingleQuotedString = ('Courier', 0xff993300, 10, None)
        SGMLSpecial = ('Courier', 0xff3366ff, 10, None)
        Script = ('Courier', 0xff1f76e4, 10, None)
        Tag = ('Courier', 0xff1f76e4, 10, None)
        UnknownAttribute = ('Courier', 0xffff0000, 10, None)
        UnknownTag = ('Courier', 0xffff0000, 10, None)
        VBScriptComment = ('Courier', 0xff008000, 10, None)
        VBScriptDefault = ('Courier', 0xffeeeeec, 10, None)
        VBScriptIdentifier = ('Courier', 0xff1f76e4, 10, None)
        VBScriptKeyword = ('Courier', 0xff1f76e4, 10, None)
        VBScriptNumber = ('Courier', 0xff008080, 10, None)
        VBScriptStart = ('Courier', 0xffeeeeec, 10, None)
        VBScriptString = ('Courier', 0xff800080, 10, None)
        VBScriptUnclosedString = ('Courier', 0xff1f76e4, 10, None)
        XMLEnd = ('Courier', 0xff5abcd8, 10, None)
        XMLStart = ('Courier', 0xff5abcd8, 10, None)
        XMLTagEnd = ('Courier', 0xff1f76e4, 10, None)
    
    class IDL:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffeeeeec, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffeeeeec, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffeeeeec, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffeeeeec, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet2 = ('Courier', 0xffeeeeec, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xff804080, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class Java:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffeeeeec, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffeeeeec, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffeeeeec, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffeeeeec, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet2 = ('Courier', 0xffeeeeec, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xffeeeeec, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class JavaScript:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff3f703f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        GlobalClass = ('Courier', 0xffeeeeec, 10, None)
        HashQuotedString = ('Courier', 0xff6cab9d, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        InactiveComment = ('Courier', 0xff90b090, 10, None)
        InactiveCommentDoc = ('Courier', 0xffd0d0d0, 10, None)
        InactiveCommentDocKeyword = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentDocKeywordError = ('Courier', 0xffc0c0c0, 10, None)
        InactiveCommentLine = ('Courier', 0xff90b090, 10, None)
        InactiveCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDefault = ('Courier', 0xffc0c0c0, 10, None)
        InactiveDoubleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveGlobalClass = ('Courier', 0xffb0b0b0, 10, None)
        InactiveHashQuotedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveIdentifier = ('Courier', 0xffb0b0b0, 10, None)
        InactiveKeyword = ('Courier', 0xff9090b0, 10, None)
        InactiveKeywordSet2 = ('Courier', 0xffc0c0c0, 10, None)
        InactiveNumber = ('Courier', 0xff90b090, 10, None)
        InactiveOperator = ('Courier', 0xffb0b0b0, 10, None)
        InactivePreProcessor = ('Courier', 0xffb0b090, 10, None)
        InactivePreProcessorComment = ('Courier', 0xffeeeeec, 10, None)
        InactivePreProcessorCommentLineDoc = ('Courier', 0xffc0c0c0, 10, None)
        InactiveRawString = ('Courier', 0xffeeeeec, 10, None)
        InactiveRegex = ('Courier', 0xff7faf7f, 10, None)
        InactiveSingleQuotedString = ('Courier', 0xffb090b0, 10, None)
        InactiveTripleQuotedVerbatimString = ('Courier', 0xffeeeeec, 10, None)
        InactiveUUID = ('Courier', 0xffc0c0c0, 10, None)
        InactiveUnclosedString = ('Courier', 0xffeeeeec, 10, None)
        InactiveVerbatimString = ('Courier', 0xff90b090, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet2 = ('Courier', 0xffeeeeec, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorComment = ('Courier', 0xff659900, 10, None)
        PreProcessorCommentLineDoc = ('Courier', 0xff3f703f, 10, None)
        RawString = ('Courier', 0xffc4bbb8, 10, None)
        Regex = ('Courier', 0xff3f7f3f, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        TripleQuotedVerbatimString = ('Courier', 0xff6cab9d, 10, None)
        UUID = ('Courier', 0xffeeeeec, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
        VerbatimString = ('Courier', 0xff6cab9d, 10, None)
    
    class Lua:
        BasicFunctions = ('Courier', 0xffa3c2da, 10, None)
        Character = ('Courier', 0xffc4bbb8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CoroutinesIOSystemFacilities = ('Courier', 0xffa3c2da, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet5 = ('Courier', 0xffeeeeec, 10, None)
        KeywordSet6 = ('Courier', 0xffeeeeec, 10, None)
        KeywordSet7 = ('Courier', 0xffeeeeec, 10, None)
        KeywordSet8 = ('Courier', 0xffeeeeec, 10, None)
        Label = ('Courier', 0xff7f7f00, 10, None)
        LineComment = ('Courier', 0xff6cab9d, 10, None)
        LiteralString = ('Courier', 0xffc4bbb8, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        StringTableMathsFunctions = ('Courier', 0xffa3c2da, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
    
    class Makefile:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        Error = ('Courier', 0xffffff00, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        Target = ('Courier', 0xffa00000, 10, None)
        Variable = ('Courier', 0xff1f76e4, 10, None)
    
    class Matlab:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
    
    class Octave:
        Command = ('Courier', 0xff7f7f00, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
    
    class PO:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        Flags = ('Courier', 0xffeeeeec, 10, None)
        Fuzzy = ('Courier', 0xffeeeeec, 10, None)
        MessageContext = ('Courier', 0xffeeeeec, 10, None)
        MessageContextText = ('Courier', 0xffeeeeec, 10, None)
        MessageContextTextEOL = ('Courier', 0xffeeeeec, 10, None)
        MessageId = ('Courier', 0xffeeeeec, 10, None)
        MessageIdText = ('Courier', 0xffeeeeec, 10, None)
        MessageIdTextEOL = ('Courier', 0xffeeeeec, 10, None)
        MessageString = ('Courier', 0xffeeeeec, 10, None)
        MessageStringText = ('Courier', 0xffeeeeec, 10, None)
        MessageStringTextEOL = ('Courier', 0xffeeeeec, 10, None)
        ProgrammerComment = ('Courier', 0xffeeeeec, 10, None)
        Reference = ('Courier', 0xffeeeeec, 10, None)
    
    class POV:
        BadDirective = ('Courier', 0xff804020, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xffff0080, 10, None)
        Directive = ('Courier', 0xff7f7f00, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        KeywordSet6 = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet7 = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet8 = ('Courier', 0xffa3c2da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        ObjectsCSGAppearance = ('Courier', 0xffa3c2da, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PredefinedFunctions = ('Courier', 0xffa3c2da, 10, None)
        PredefinedIdentifiers = ('Courier', 0xffa3c2da, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        TypesModifiersItems = ('Courier', 0xffa3c2da, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
    
    class Pascal:
        Asm = ('Courier', 0xff804080, 10, None)
        Character = ('Courier', 0xffc4bbb8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentParenthesis = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        HexNumber = ('Courier', 0xff74ccf4, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PreProcessor = ('Courier', 0xff7f7f00, 10, None)
        PreProcessorParenthesis = ('Courier', 0xff7f7f00, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
    
    class Perl:
        Array = ('Courier', 0xffeeeeec, 10, None)
        BacktickHereDocument = ('Courier', 0xffc4bbb8, 10, None)
        BacktickHereDocumentVar = ('Courier', 0xffd00000, 10, None)
        Backticks = ('Courier', 0xffffff00, 10, None)
        BackticksVar = ('Courier', 0xffd00000, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        DataSection = ('Courier', 0xff600000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedHereDocument = ('Courier', 0xffc4bbb8, 10, None)
        DoubleQuotedHereDocumentVar = ('Courier', 0xffd00000, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        DoubleQuotedStringVar = ('Courier', 0xffd00000, 10, None)
        Error = ('Courier', 0xffffff00, 10, None)
        FormatBody = ('Courier', 0xffc000c0, 10, None)
        FormatIdentifier = ('Courier', 0xffc000c0, 10, None)
        Hash = ('Courier', 0xffeeeeec, 10, None)
        HereDocumentDelimiter = ('Courier', 0xffeeeeec, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        POD = ('Courier', 0xff004000, 10, None)
        PODVerbatim = ('Courier', 0xff004000, 10, None)
        QuotedStringQ = ('Courier', 0xffc4bbb8, 10, None)
        QuotedStringQQ = ('Courier', 0xffc4bbb8, 10, None)
        QuotedStringQQVar = ('Courier', 0xffd00000, 10, None)
        QuotedStringQR = ('Courier', 0xffeeeeec, 10, None)
        QuotedStringQRVar = ('Courier', 0xffd00000, 10, None)
        QuotedStringQW = ('Courier', 0xffeeeeec, 10, None)
        QuotedStringQX = ('Courier', 0xffffff00, 10, None)
        QuotedStringQXVar = ('Courier', 0xffd00000, 10, None)
        Regex = ('Courier', 0xffeeeeec, 10, None)
        RegexVar = ('Courier', 0xffd00000, 10, None)
        Scalar = ('Courier', 0xffeeeeec, 10, None)
        SingleQuotedHereDocument = ('Courier', 0xffc4bbb8, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        SubroutinePrototype = ('Courier', 0xffeeeeec, 10, None)
        Substitution = ('Courier', 0xffeeeeec, 10, None)
        SubstitutionVar = ('Courier', 0xffd00000, 10, None)
        SymbolTable = ('Courier', 0xffeeeeec, 10, None)
        Translation = ('Courier', 0xffeeeeec, 10, None)
    
    class PostScript:
        ArrayParenthesis = ('Courier', 0xffa3c2da, 10, None)
        BadStringCharacter = ('Courier', 0xffffff00, 10, None)
        Base85String = ('Courier', 0xffc4bbb8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        DSCComment = ('Courier', 0xff3f703f, 10, None)
        DSCCommentValue = ('Courier', 0xff3060a0, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        DictionaryParenthesis = ('Courier', 0xff3060a0, 10, None)
        HexString = ('Courier', 0xff3f7f3f, 10, None)
        ImmediateEvalLiteral = ('Courier', 0xff7f7f00, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        Literal = ('Courier', 0xff7f7f00, 10, None)
        Name = ('Courier', 0xffeeeeec, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        ProcedureParenthesis = ('Courier', 0xffeeeeec, 10, None)
        Text = ('Courier', 0xffc4bbb8, 10, None)
    
    class Properties:
        Assignment = ('Courier', 0xffb06000, 10, None)
        Comment = ('Courier', 0xff74ccf4, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        DefaultValue = ('Courier', 0xff7f7f00, 10, None)
        Key = ('Courier', 0xffeeeeec, 10, None)
        Section = ('Courier', 0xffc4bbb8, 10, None)
    
    class Python:
        ClassName = ('Courier', 0xff5abcd8, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentBlock = ('Courier', 0xff7f7f7f, 10, None)
        Decorator = ('Courier', 0xff805000, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        FunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        HighlightedIdentifier = ('Courier', 0xff407090, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Inconsistent = ('Courier', 0xff6cab9d, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        NoWarning = ('Courier', 0xff808080, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Spaces = ('Courier', 0xffc4bbb8, 10, None)
        Tabs = ('Courier', 0xffc4bbb8, 10, None)
        TabsAfterSpaces = ('Courier', 0xff74ccf4, 10, None)
        TripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        TripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
    
    class Ruby:
        Backticks = ('Courier', 0xffffff00, 10, None)
        ClassName = ('Courier', 0xff5abcd8, 10, None)
        ClassVariable = ('Courier', 0xff8000b0, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        DataSection = ('Courier', 0xff600000, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DemotedKeyword = ('Courier', 0xffa3c2da, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Error = ('Courier', 0xffeeeeec, 10, None)
        FunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        Global = ('Courier', 0xff800080, 10, None)
        HereDocument = ('Courier', 0xffc4bbb8, 10, None)
        HereDocumentDelimiter = ('Courier', 0xffeeeeec, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        InstanceVariable = ('Courier', 0xffb00080, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        ModuleName = ('Courier', 0xffa000a0, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        POD = ('Courier', 0xff004000, 10, None)
        PercentStringQ = ('Courier', 0xffc4bbb8, 10, None)
        PercentStringq = ('Courier', 0xffc4bbb8, 10, None)
        PercentStringr = ('Courier', 0xffeeeeec, 10, None)
        PercentStringw = ('Courier', 0xffeeeeec, 10, None)
        PercentStringx = ('Courier', 0xffffff00, 10, None)
        Regex = ('Courier', 0xffeeeeec, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Stderr = ('Courier', 0xffeeeeec, 10, None)
        Stdin = ('Courier', 0xffeeeeec, 10, None)
        Stdout = ('Courier', 0xffeeeeec, 10, None)
        Symbol = ('Courier', 0xffc0a030, 10, None)
    
    class SQL:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        CommentDocKeyword = ('Courier', 0xff3060a0, 10, None)
        CommentDocKeywordError = ('Courier', 0xff804020, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        CommentLineHash = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        DoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet5 = ('Courier', 0xff4b0082, 10, None)
        KeywordSet6 = ('Courier', 0xffb00040, 10, None)
        KeywordSet7 = ('Courier', 0xff8b0000, 10, None)
        KeywordSet8 = ('Courier', 0xff800080, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        PlusComment = ('Courier', 0xff6cab9d, 10, None)
        PlusKeyword = ('Courier', 0xff7f7f00, 10, None)
        PlusPrompt = ('Courier', 0xff6cab9d, 10, None)
        QuotedIdentifier = ('Courier', 0xffeeeeec, 10, None)
        SingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
    
    class Spice:
        Command = ('Courier', 0xffa3c2da, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Delimiter = ('Courier', 0xffeeeeec, 10, None)
        Function = ('Courier', 0xffa3c2da, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Parameter = ('Courier', 0xff0040e0, 10, None)
        Value = ('Courier', 0xffc4bbb8, 10, None)
    
    class TCL:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentBlock = ('Courier', 0xffeeeeec, 10, None)
        CommentBox = ('Courier', 0xff6cab9d, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        ExpandKeyword = ('Courier', 0xffa3c2da, 10, None)
        ITCLKeyword = ('Courier', 0xffa3c2da, 10, None)
        Identifier = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet6 = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet7 = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet8 = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet9 = ('Courier', 0xffa3c2da, 10, None)
        Modifier = ('Courier', 0xffc4bbb8, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        QuotedKeyword = ('Courier', 0xffc4bbb8, 10, None)
        QuotedString = ('Courier', 0xffc4bbb8, 10, None)
        Substitution = ('Courier', 0xff7f7f00, 10, None)
        SubstitutionBrace = ('Courier', 0xff7f7f00, 10, None)
        TCLKeyword = ('Courier', 0xffa3c2da, 10, None)
        TkCommand = ('Courier', 0xffa3c2da, 10, None)
        TkKeyword = ('Courier', 0xffa3c2da, 10, None)
    
    class TeX:
        Command = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff3f3f3f, 10, None)
        Group = ('Courier', 0xfff5b0cb, 10, None)
        Special = ('Courier', 0xff74ccf4, 10, None)
        Symbol = ('Courier', 0xff7f7f00, 10, None)
        Text = ('Courier', 0xffeeeeec, 10, None)
    
    class VHDL:
        Attribute = ('Courier', 0xff804020, 10, None)
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentLine = ('Courier', 0xff3f7f3f, 10, None)
        Default = ('Courier', 0xff800080, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet7 = ('Courier', 0xff804020, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        StandardFunction = ('Courier', 0xff808020, 10, None)
        StandardOperator = ('Courier', 0xff74ccf4, 10, None)
        StandardPackage = ('Courier', 0xff208020, 10, None)
        StandardType = ('Courier', 0xff208080, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
    
    class Verilog:
        Comment = ('Courier', 0xff6cab9d, 10, None)
        CommentBang = ('Courier', 0xff3f7f3f, 10, None)
        CommentLine = ('Courier', 0xff6cab9d, 10, None)
        Default = ('Courier', 0xff808080, 10, None)
        Identifier = ('Courier', 0xffeeeeec, 10, None)
        Keyword = ('Courier', 0xffa3c2da, 10, None)
        KeywordSet2 = ('Courier', 0xff74ccf4, 10, None)
        Number = ('Courier', 0xff74ccf4, 10, None)
        Operator = ('Courier', 0xff007070, 10, None)
        Preprocessor = ('Courier', 0xff7f7f00, 10, None)
        String = ('Courier', 0xffc4bbb8, 10, None)
        SystemTask = ('Courier', 0xff804020, 10, None)
        UnclosedString = ('Courier', 0xffeeeeec, 10, None)
        UserKeywordSet = ('Courier', 0xff2a00ff, 10, None)
    
    class XML:
        ASPAtStart = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptComment = ('Courier', 0xff6cab9d, 10, None)
        ASPJavaScriptCommentDoc = ('Courier', 0xff7f7f7f, 10, None)
        ASPJavaScriptCommentLine = ('Courier', 0xff6cab9d, 10, None)
        ASPJavaScriptDefault = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPJavaScriptKeyword = ('Courier', 0xffa3c2da, 10, None)
        ASPJavaScriptNumber = ('Courier', 0xff74ccf4, 10, None)
        ASPJavaScriptRegex = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPJavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        ASPJavaScriptSymbol = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptUnclosedString = ('Courier', 0xffeeeeec, 10, None)
        ASPJavaScriptWord = ('Courier', 0xffeeeeec, 10, None)
        ASPPythonClassName = ('Courier', 0xff5abcd8, 10, None)
        ASPPythonComment = ('Courier', 0xff6cab9d, 10, None)
        ASPPythonDefault = ('Courier', 0xff808080, 10, None)
        ASPPythonDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPPythonFunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        ASPPythonIdentifier = ('Courier', 0xffeeeeec, 10, None)
        ASPPythonKeyword = ('Courier', 0xffa3c2da, 10, None)
        ASPPythonNumber = ('Courier', 0xff74ccf4, 10, None)
        ASPPythonOperator = ('Courier', 0xffeeeeec, 10, None)
        ASPPythonSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        ASPPythonStart = ('Courier', 0xff808080, 10, None)
        ASPPythonTripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        ASPPythonTripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        ASPStart = ('Courier', 0xffeeeeec, 10, None)
        ASPVBScriptComment = ('Courier', 0xff008000, 10, None)
        ASPVBScriptDefault = ('Courier', 0xffeeeeec, 10, None)
        ASPVBScriptIdentifier = ('Courier', 0xff1f76e4, 10, None)
        ASPVBScriptKeyword = ('Courier', 0xff1f76e4, 10, None)
        ASPVBScriptNumber = ('Courier', 0xff008080, 10, None)
        ASPVBScriptStart = ('Courier', 0xffeeeeec, 10, None)
        ASPVBScriptString = ('Courier', 0xff800080, 10, None)
        ASPVBScriptUnclosedString = ('Courier', 0xff1f76e4, 10, None)
        ASPXCComment = ('Courier', 0xffeeeeec, 10, None)
        Attribute = ('Courier', 0xff008080, 10, None)
        CDATA = ('Courier', 0xffedff86, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        Entity = ('Courier', 0xff800080, 10, None)
        HTMLComment = ('Courier', 0xff808000, 10, None)
        HTMLDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        HTMLNumber = ('Courier', 0xff74ccf4, 10, None)
        HTMLSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        HTMLValue = ('Courier', 0xff608060, 10, None)
        JavaScriptComment = ('Courier', 0xff6cab9d, 10, None)
        JavaScriptCommentDoc = ('Courier', 0xff3f703f, 10, None)
        JavaScriptCommentLine = ('Courier', 0xff6cab9d, 10, None)
        JavaScriptDefault = ('Courier', 0xffeeeeec, 10, None)
        JavaScriptDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        JavaScriptKeyword = ('Courier', 0xffa3c2da, 10, None)
        JavaScriptNumber = ('Courier', 0xff74ccf4, 10, None)
        JavaScriptRegex = ('Courier', 0xffeeeeec, 10, None)
        JavaScriptSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        JavaScriptStart = ('Courier', 0xff7f7f00, 10, None)
        JavaScriptSymbol = ('Courier', 0xffeeeeec, 10, None)
        JavaScriptUnclosedString = ('Courier', 0xffeeeeec, 10, None)
        JavaScriptWord = ('Courier', 0xffeeeeec, 10, None)
        OtherInTag = ('Courier', 0xff800080, 10, None)
        PHPComment = ('Courier', 0xff999999, 10, None)
        PHPCommentLine = ('Courier', 0xff666666, 10, None)
        PHPDefault = ('Courier', 0xffc7dbf5, 10, None)
        PHPDoubleQuotedString = ('Courier', 0xff6cab9d, 10, None)
        PHPDoubleQuotedVariable = ('Courier', 0xffa3c2da, 10, None)
        PHPKeyword = ('Courier', 0xffc4bbb8, 10, None)
        PHPNumber = ('Courier', 0xffcc9900, 10, None)
        PHPOperator = ('Courier', 0xffeeeeec, 10, None)
        PHPSingleQuotedString = ('Courier', 0xff009f00, 10, None)
        PHPStart = ('Courier', 0xffedff86, 10, None)
        PHPVariable = ('Courier', 0xffa3c2da, 10, None)
        PythonClassName = ('Courier', 0xff5abcd8, 10, None)
        PythonComment = ('Courier', 0xff6cab9d, 10, None)
        PythonDefault = ('Courier', 0xff808080, 10, None)
        PythonDoubleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        PythonFunctionMethodName = ('Courier', 0xff74ccf4, 10, None)
        PythonIdentifier = ('Courier', 0xffeeeeec, 10, None)
        PythonKeyword = ('Courier', 0xffa3c2da, 10, None)
        PythonNumber = ('Courier', 0xff74ccf4, 10, None)
        PythonOperator = ('Courier', 0xffeeeeec, 10, None)
        PythonSingleQuotedString = ('Courier', 0xffc4bbb8, 10, None)
        PythonStart = ('Courier', 0xff808080, 10, None)
        PythonTripleDoubleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        PythonTripleSingleQuotedString = ('Courier', 0xfff5b0cb, 10, None)
        SGMLBlockDefault = ('Courier', 0xfffff5b2, 10, None)
        SGMLCommand = ('Courier', 0xff1f76e4, 10, None)
        SGMLComment = ('Courier', 0xff808000, 10, None)
        SGMLDefault = ('Courier', 0xff1f76e4, 10, None)
        SGMLDoubleQuotedString = ('Courier', 0xffedff86, 10, None)
        SGMLEntity = ('Courier', 0xff333333, 10, None)
        SGMLError = ('Courier', 0xffedff86, 10, None)
        SGMLParameter = ('Courier', 0xff006600, 10, None)
        SGMLParameterComment = ('Courier', 0xffeeeeec, 10, None)
        SGMLSingleQuotedString = ('Courier', 0xff993300, 10, None)
        SGMLSpecial = ('Courier', 0xff3366ff, 10, None)
        Script = ('Courier', 0xff1f76e4, 10, None)
        Tag = ('Courier', 0xff1f76e4, 10, None)
        UnknownAttribute = ('Courier', 0xff008080, 10, None)
        UnknownTag = ('Courier', 0xff1f76e4, 10, None)
        VBScriptComment = ('Courier', 0xff008000, 10, None)
        VBScriptDefault = ('Courier', 0xffeeeeec, 10, None)
        VBScriptIdentifier = ('Courier', 0xff1f76e4, 10, None)
        VBScriptKeyword = ('Courier', 0xff1f76e4, 10, None)
        VBScriptNumber = ('Courier', 0xff008080, 10, None)
        VBScriptStart = ('Courier', 0xffeeeeec, 10, None)
        VBScriptString = ('Courier', 0xff800080, 10, None)
        VBScriptUnclosedString = ('Courier', 0xff1f76e4, 10, None)
        XMLEnd = ('Courier', 0xff800080, 10, None)
        XMLStart = ('Courier', 0xff800080, 10, None)
        XMLTagEnd = ('Courier', 0xff1f76e4, 10, None)
    
    class YAML:
        Comment = ('Courier', 0xff008800, 10, None)
        Default = ('Courier', 0xffeeeeec, 10, None)
        DocumentDelimiter = ('Courier', 0xff112435, 10, None)
        Identifier = ('Courier', 0xfff3c969, 10, None)
        Keyword = ('Courier', 0xff880088, 10, None)
        Number = ('Courier', 0xff880000, 10, None)
        Operator = ('Courier', 0xffeeeeec, 10, None)
        Reference = ('Courier', 0xff008888, 10, None)
        SyntaxErrorMarker = ('Courier', 0xff112435, 10, None)
        TextBlockMarker = ('Courier', 0xff333366, 10, None)


class Paper:
    Default = PyQt4.QtGui.QColor(0xff3465a4)
    
    class Ada:
        Default = 0xff3465a4
        Comment = 0xff3465a4
        Keyword = 0xff3465a4
        String = 0xff3465a4
        Procedure = 0xff3465a4
        Number = 0xff3465a4
        Type = 0xff3465a4
        Package = 0xff3465a4
    
    class Nim:
        Default = 0xff3465a4
        Comment = 0xff3465a4
        BasicKeyword = 0xff3465a4
        TopKeyword = 0xff3465a4
        String = 0xff3465a4
        LongString = 0xff3465a4
        Number = 0xff3465a4
        Operator = 0xff3465a4
        Unsafe = 0xff3465a4
        Type = 0xff3465a4
        DocumentationComment = 0xff3465a4
        Definition = 0xff3465a4
        Class = 0xff3465a4
        KeywordOperator = 0xff3465a4
        CharLiteral = 0xff3465a4
        CaseOf = 0xff3465a4
        UserKeyword = 0xff3465a4
        MultilineComment = 0xff3465a4
        MultilineDocumentation = 0xff3465a4
        Pragma = 0xff3465a4
    
    class RouterOS:
        Default = 0xff3465a4
        Operator = 0xff3465a4
        Comment = 0xff3465a4
        Keyword1 = 0xff3465a4
        Keyword2 = 0xff3465a4
        Keyword3 = 0xff3465a4
    
    class Oberon:
        Default = 0xff3465a4
        Comment = 0xff3465a4
        Keyword = 0xff3465a4
        String = 0xff3465a4
        Procedure = 0xff3465a4
        Module = 0xff3465a4
        Number = 0xff3465a4
        Type = 0xff3465a4
    
    
    # Generated
    class AVS:
        Function = 0xff3465a4
        KeywordSet6 = 0xff3465a4
        TripleString = 0xff3465a4
        LineComment = 0xff3465a4
        Plugin = 0xff3465a4
        String = 0xff3465a4
        ClipProperty = 0xff3465a4
        Default = 0xff3465a4
        Operator = 0xff3465a4
        Number = 0xff3465a4
        Filter = 0xff3465a4
        Identifier = 0xff3465a4
        NestedBlockComment = 0xff3465a4
        Keyword = 0xff3465a4
        BlockComment = 0xff3465a4
    
    class Bash:
        Error = 0xffff0000
        Backticks = 0xffa08080
        SingleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        HereDocumentDelimiter = 0xffddd0dd
        Comment = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        Default = 0xff3465a4
        Operator = 0xff3465a4
        ParameterExpansion = 0xffffffe0
        Number = 0xff3465a4
        Identifier = 0xff3465a4
        Keyword = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
    
    class Batch:
        Label = 0xff606060
        Default = 0xff3465a4
        Keyword = 0xff3465a4
        ExternalCommand = 0xff3465a4
        Variable = 0xff3465a4
        Comment = 0xff3465a4
        HideCommandChar = 0xff3465a4
        Operator = 0xff3465a4
    
    class CMake:
        Function = 0xff3465a4
        BlockForeach = 0xff3465a4
        BlockWhile = 0xff3465a4
        StringLeftQuote = 0xffeeeeee
        Label = 0xff3465a4
        Comment = 0xff3465a4
        BlockMacro = 0xff3465a4
        StringRightQuote = 0xffeeeeee
        Default = 0xff3465a4
        Number = 0xff3465a4
        BlockIf = 0xff3465a4
        Variable = 0xff3465a4
        KeywordSet3 = 0xff3465a4
        String = 0xffeeeeee
        StringVariable = 0xffeeeeee
    
    class CPP:
        CommentDocKeywordError = 0xff3465a4
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff3465a4
        UUID = 0xff3465a4
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
        InactiveOperator = 0xff3465a4
        InactivePreProcessor = 0xff3465a4
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff3465a4
        InactiveRawString = 0xff3465a4
        PreProcessor = 0xff3465a4
        KeywordSet2 = 0xff3465a4
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xff3465a4
        InactiveNumber = 0xff3465a4
        InactivePreProcessorCommentLineDoc = 0xff3465a4
        Number = 0xff3465a4
        InactiveUUID = 0xff3465a4
        CommentDoc = 0xff3465a4
        InactiveCommentDoc = 0xff3465a4
        GlobalClass = 0xff3465a4
        InactiveSingleQuotedString = 0xff3465a4
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff3465a4
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xff3465a4
        InactiveIdentifier = 0xff3465a4
        CommentLineDoc = 0xff3465a4
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xff3465a4
        InactiveCommentDocKeyword = 0xff3465a4
        Keyword = 0xff3465a4
        InactiveCommentLineDoc = 0xff3465a4
        InactiveDefault = 0xff3465a4
        InactiveCommentDocKeywordError = 0xff3465a4
        InactiveTripleQuotedVerbatimString = 0xff3465a4
        CommentDocKeyword = 0xff3465a4
        InactiveDoubleQuotedString = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        PreProcessorComment = 0xff3465a4
        InactiveComment = 0xff3465a4
        RawString = 0xfffff3ff
        Default = 0xff3465a4
        PreProcessorCommentLineDoc = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        InactiveKeyword = 0xff3465a4
    
    class CSS:
        Important = 0xff3465a4
        CSS3Property = 0xff3465a4
        Attribute = 0xff3465a4
        Comment = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        MediaRule = 0xff3465a4
        AtRule = 0xff3465a4
        UnknownPseudoClass = 0xff3465a4
        PseudoClass = 0xff3465a4
        Tag = 0xff3465a4
        CSS2Property = 0xff3465a4
        CSS1Property = 0xff3465a4
        IDSelector = 0xff3465a4
        ExtendedCSSProperty = 0xff3465a4
        Variable = 0xff3465a4
        ExtendedPseudoClass = 0xff3465a4
        ClassSelector = 0xff3465a4
        Default = 0xff3465a4
        PseudoElement = 0xff3465a4
        UnknownProperty = 0xff3465a4
        Value = 0xff3465a4
        ExtendedPseudoElement = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
    
    class CSharp:
        CommentDocKeywordError = 0xff3465a4
        InactiveRegex = 0xff3465a4
        InactivePreProcessorComment = 0xff3465a4
        UUID = 0xff3465a4
        InactiveVerbatimString = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
        InactiveOperator = 0xff3465a4
        InactivePreProcessor = 0xff3465a4
        UnclosedString = 0xff3465a4
        Identifier = 0xff3465a4
        InactiveRawString = 0xff3465a4
        PreProcessor = 0xff3465a4
        KeywordSet2 = 0xff3465a4
        InactiveUnclosedString = 0xff3465a4
        InactiveCommentLine = 0xff3465a4
        InactiveNumber = 0xff3465a4
        InactivePreProcessorCommentLineDoc = 0xff3465a4
        Number = 0xff3465a4
        InactiveUUID = 0xff3465a4
        CommentDoc = 0xff3465a4
        InactiveCommentDoc = 0xff3465a4
        GlobalClass = 0xff3465a4
        InactiveSingleQuotedString = 0xff3465a4
        HashQuotedString = 0xff3465a4
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff3465a4
        Regex = 0xff3465a4
        InactiveGlobalClass = 0xff3465a4
        InactiveIdentifier = 0xff3465a4
        CommentLineDoc = 0xff3465a4
        TripleQuotedVerbatimString = 0xff3465a4
        InactiveKeywordSet2 = 0xff3465a4
        InactiveCommentDocKeyword = 0xff3465a4
        Keyword = 0xff3465a4
        InactiveCommentLineDoc = 0xff3465a4
        InactiveDefault = 0xff3465a4
        InactiveCommentDocKeywordError = 0xff3465a4
        InactiveTripleQuotedVerbatimString = 0xff3465a4
        CommentDocKeyword = 0xff3465a4
        InactiveDoubleQuotedString = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        PreProcessorComment = 0xff3465a4
        InactiveComment = 0xff3465a4
        RawString = 0xff3465a4
        Default = 0xff3465a4
        PreProcessorCommentLineDoc = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        InactiveKeyword = 0xff3465a4
    
    class CoffeeScript:
        UUID = 0xff3465a4
        CommentDocKeywordError = 0xff3465a4
        GlobalClass = 0xff3465a4
        VerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
        Number = 0xff3465a4
        Identifier = 0xff3465a4
        Keyword = 0xff3465a4
        UnclosedString = 0xffe0c0e0
        Regex = 0xffe0f0e0
        CommentDocKeyword = 0xff3465a4
        BlockRegex = 0xff3465a4
        CommentLineDoc = 0xff3465a4
        PreProcessor = 0xff3465a4
        CommentLine = 0xff3465a4
        CommentBlock = 0xff3465a4
        Comment = 0xff3465a4
        KeywordSet2 = 0xff3465a4
        BlockRegexComment = 0xff3465a4
        Default = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        CommentDoc = 0xff3465a4
    
    class D:
        BackquoteString = 0xff3465a4
        CommentDocKeywordError = 0xff3465a4
        Operator = 0xff3465a4
        CommentNested = 0xff3465a4
        KeywordDoc = 0xff3465a4
        KeywordSet7 = 0xff3465a4
        Keyword = 0xff3465a4
        KeywordSecondary = 0xff3465a4
        Identifier = 0xff3465a4
        KeywordSet5 = 0xff3465a4
        CommentDocKeyword = 0xff3465a4
        KeywordSet6 = 0xff3465a4
        CommentLineDoc = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        Typedefs = 0xff3465a4
        Character = 0xff3465a4
        RawString = 0xff3465a4
        Default = 0xff3465a4
        Number = 0xff3465a4
        UnclosedString = 0xffe0c0e0
        String = 0xff3465a4
        CommentDoc = 0xff3465a4
    
    class Diff:
        Header = 0xff3465a4
        LineChanged = 0xff3465a4
        Default = 0xff3465a4
        LineRemoved = 0xff3465a4
        Command = 0xff3465a4
        Position = 0xff3465a4
        LineAdded = 0xff3465a4
        Comment = 0xff3465a4
    
    class Fortran:
        Label = 0xff3465a4
        Identifier = 0xff3465a4
        DottedOperator = 0xff3465a4
        PreProcessor = 0xff3465a4
        Comment = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        Default = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        ExtendedFunction = 0xff3465a4
        UnclosedString = 0xffe0c0e0
        Number = 0xff3465a4
        Continuation = 0xfff0e080
        IntrinsicFunction = 0xff3465a4
        Keyword = 0xff3465a4
        Operator = 0xff3465a4
    
    class Fortran77:
        Label = 0xff3465a4
        Identifier = 0xff3465a4
        DottedOperator = 0xff3465a4
        PreProcessor = 0xff3465a4
        Comment = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        Default = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        ExtendedFunction = 0xff3465a4
        UnclosedString = 0xffe0c0e0
        Number = 0xff3465a4
        Continuation = 0xfff0e080
        IntrinsicFunction = 0xff3465a4
        Keyword = 0xff3465a4
        Operator = 0xff3465a4
    
    class HTML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity = 0xff3465a4
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart = 0xff3465a4
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart = 0xff3465a4
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart = 0xff3465a4
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xff3465a4
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart = 0xff3465a4
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xff3465a4
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xff3465a4
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd = 0xff3465a4
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute = 0xff3465a4
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script = 0xff3465a4
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart = 0xff3465a4
        ASPPythonIdentifier = 0xffcfefcf
        ASPVBScriptKeyword = 0xffcfcfef
        ASPPythonTripleDoubleQuotedString = 0xffcfefcf
        ASPPythonKeyword = 0xffcfefcf
        ASPJavaScriptNumber = 0xffdfdf7f
        PHPStart = 0xffffefbf
        PythonTripleSingleQuotedString = 0xffefffef
        PHPNumber = 0xfffff8f8
        ASPPythonDefault = 0xffcfefcf
        SGMLSpecial = 0xffefefff
        OtherInTag = 0xff3465a4
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag = 0xff3465a4
        XMLEnd = 0xff3465a4
        CDATA = 0xffffdf00
        HTMLNumber = 0xff3465a4
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart = 0xff3465a4
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute = 0xff3465a4
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString = 0xff3465a4
        ASPXCComment = 0xff3465a4
        VBScriptStart = 0xff3465a4
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xff3465a4
        UnknownTag = 0xff3465a4
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class IDL:
        CommentDocKeywordError = 0xff3465a4
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff3465a4
        UUID = 0xff3465a4
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
        InactiveOperator = 0xff3465a4
        InactivePreProcessor = 0xff3465a4
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff3465a4
        InactiveRawString = 0xff3465a4
        PreProcessor = 0xff3465a4
        KeywordSet2 = 0xff3465a4
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xff3465a4
        InactiveNumber = 0xff3465a4
        InactivePreProcessorCommentLineDoc = 0xff3465a4
        Number = 0xff3465a4
        InactiveUUID = 0xff3465a4
        CommentDoc = 0xff3465a4
        InactiveCommentDoc = 0xff3465a4
        GlobalClass = 0xff3465a4
        InactiveSingleQuotedString = 0xff3465a4
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff3465a4
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xff3465a4
        InactiveIdentifier = 0xff3465a4
        CommentLineDoc = 0xff3465a4
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xff3465a4
        InactiveCommentDocKeyword = 0xff3465a4
        Keyword = 0xff3465a4
        InactiveCommentLineDoc = 0xff3465a4
        InactiveDefault = 0xff3465a4
        InactiveCommentDocKeywordError = 0xff3465a4
        InactiveTripleQuotedVerbatimString = 0xff3465a4
        CommentDocKeyword = 0xff3465a4
        InactiveDoubleQuotedString = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        PreProcessorComment = 0xff3465a4
        InactiveComment = 0xff3465a4
        RawString = 0xfffff3ff
        Default = 0xff3465a4
        PreProcessorCommentLineDoc = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        InactiveKeyword = 0xff3465a4
    
    class Java:
        CommentDocKeywordError = 0xff3465a4
        InactiveRegex = 0xffe0f0e0
        InactivePreProcessorComment = 0xff3465a4
        UUID = 0xff3465a4
        InactiveVerbatimString = 0xffe0ffe0
        SingleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
        InactiveOperator = 0xff3465a4
        InactivePreProcessor = 0xff3465a4
        UnclosedString = 0xffe0c0e0
        Identifier = 0xff3465a4
        InactiveRawString = 0xff3465a4
        PreProcessor = 0xff3465a4
        KeywordSet2 = 0xff3465a4
        InactiveUnclosedString = 0xffe0c0e0
        InactiveCommentLine = 0xff3465a4
        InactiveNumber = 0xff3465a4
        InactivePreProcessorCommentLineDoc = 0xff3465a4
        Number = 0xff3465a4
        InactiveUUID = 0xff3465a4
        CommentDoc = 0xff3465a4
        InactiveCommentDoc = 0xff3465a4
        GlobalClass = 0xff3465a4
        InactiveSingleQuotedString = 0xff3465a4
        HashQuotedString = 0xffe7ffd7
        VerbatimString = 0xffe0ffe0
        InactiveHashQuotedString = 0xff3465a4
        Regex = 0xffe0f0e0
        InactiveGlobalClass = 0xff3465a4
        InactiveIdentifier = 0xff3465a4
        CommentLineDoc = 0xff3465a4
        TripleQuotedVerbatimString = 0xffe0ffe0
        InactiveKeywordSet2 = 0xff3465a4
        InactiveCommentDocKeyword = 0xff3465a4
        Keyword = 0xff3465a4
        InactiveCommentLineDoc = 0xff3465a4
        InactiveDefault = 0xff3465a4
        InactiveCommentDocKeywordError = 0xff3465a4
        InactiveTripleQuotedVerbatimString = 0xff3465a4
        CommentDocKeyword = 0xff3465a4
        InactiveDoubleQuotedString = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        PreProcessorComment = 0xff3465a4
        InactiveComment = 0xff3465a4
        RawString = 0xfffff3ff
        Default = 0xff3465a4
        PreProcessorCommentLineDoc = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        InactiveKeyword = 0xff3465a4
    
    class JavaScript:
        CommentDocKeywordError = 0xff3465a4
        InactiveRegex = 0xff3465a4
        InactivePreProcessorComment = 0xff3465a4
        UUID = 0xff3465a4
        InactiveVerbatimString = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
        InactiveOperator = 0xff3465a4
        InactivePreProcessor = 0xff3465a4
        UnclosedString = 0xff3465a4
        Identifier = 0xff3465a4
        InactiveRawString = 0xff3465a4
        PreProcessor = 0xff3465a4
        KeywordSet2 = 0xff3465a4
        InactiveUnclosedString = 0xff3465a4
        InactiveCommentLine = 0xff3465a4
        InactiveNumber = 0xff3465a4
        InactivePreProcessorCommentLineDoc = 0xff3465a4
        Number = 0xff3465a4
        InactiveUUID = 0xff3465a4
        CommentDoc = 0xff3465a4
        InactiveCommentDoc = 0xff3465a4
        GlobalClass = 0xff3465a4
        InactiveSingleQuotedString = 0xff3465a4
        HashQuotedString = 0xff3465a4
        VerbatimString = 0xff3465a4
        InactiveHashQuotedString = 0xff3465a4
        Regex = 0xffe0f0ff
        InactiveGlobalClass = 0xff3465a4
        InactiveIdentifier = 0xff3465a4
        CommentLineDoc = 0xff3465a4
        TripleQuotedVerbatimString = 0xff3465a4
        InactiveKeywordSet2 = 0xff3465a4
        InactiveCommentDocKeyword = 0xff3465a4
        Keyword = 0xff3465a4
        InactiveCommentLineDoc = 0xff3465a4
        InactiveDefault = 0xff3465a4
        InactiveCommentDocKeywordError = 0xff3465a4
        InactiveTripleQuotedVerbatimString = 0xff3465a4
        CommentDocKeyword = 0xff3465a4
        InactiveDoubleQuotedString = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        PreProcessorComment = 0xff3465a4
        InactiveComment = 0xff3465a4
        RawString = 0xff3465a4
        Default = 0xff3465a4
        PreProcessorCommentLineDoc = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        InactiveKeyword = 0xff3465a4
    
    class Lua:
        Label = 0xff3465a4
        Identifier = 0xff3465a4
        StringTableMathsFunctions = 0xffd0d0ff
        CoroutinesIOSystemFacilities = 0xffffd0d0
        KeywordSet5 = 0xff3465a4
        KeywordSet6 = 0xff3465a4
        Preprocessor = 0xff3465a4
        LineComment = 0xff3465a4
        Comment = 0xffd0f0f0
        String = 0xff3465a4
        Character = 0xff3465a4
        Default = 0xff3465a4
        Operator = 0xff3465a4
        LiteralString = 0xffe0ffff
        Number = 0xff3465a4
        KeywordSet8 = 0xff3465a4
        KeywordSet7 = 0xff3465a4
        BasicFunctions = 0xffd0ffd0
        Keyword = 0xff3465a4
        UnclosedString = 0xffe0c0e0
    
    class Makefile:
        Default = 0xff3465a4
        Operator = 0xff3465a4
        Target = 0xff3465a4
        Preprocessor = 0xff3465a4
        Variable = 0xff3465a4
        Comment = 0xff3465a4
        Error = 0xffff0000
    
    class Matlab:
        SingleQuotedString = 0xff3465a4
        Default = 0xff3465a4
        Keyword = 0xff3465a4
        Number = 0xff3465a4
        Command = 0xff3465a4
        Identifier = 0xff3465a4
        Comment = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
    
    class Octave:
        SingleQuotedString = 0xff3465a4
        Default = 0xff3465a4
        Keyword = 0xff3465a4
        Number = 0xff3465a4
        Command = 0xff3465a4
        Identifier = 0xff3465a4
        Comment = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
    
    class PO:
        ProgrammerComment = 0xff3465a4
        Flags = 0xff3465a4
        MessageContextText = 0xff3465a4
        MessageStringTextEOL = 0xff3465a4
        MessageId = 0xff3465a4
        MessageIdText = 0xff3465a4
        Reference = 0xff3465a4
        Comment = 0xff3465a4
        MessageStringText = 0xff3465a4
        MessageContext = 0xff3465a4
        Fuzzy = 0xff3465a4
        Default = 0xff3465a4
        MessageString = 0xff3465a4
        MessageContextTextEOL = 0xff3465a4
        MessageIdTextEOL = 0xff3465a4
    
    class POV:
        KeywordSet7 = 0xffd0d0d0
        KeywordSet6 = 0xffd0ffd0
        PredefinedFunctions = 0xffd0d0ff
        CommentLine = 0xff3465a4
        PredefinedIdentifiers = 0xff3465a4
        Comment = 0xff3465a4
        Directive = 0xff3465a4
        String = 0xff3465a4
        BadDirective = 0xff3465a4
        TypesModifiersItems = 0xffffffd0
        Default = 0xff3465a4
        Operator = 0xff3465a4
        Number = 0xff3465a4
        KeywordSet8 = 0xffe0e0e0
        Identifier = 0xff3465a4
        ObjectsCSGAppearance = 0xffffd0d0
        UnclosedString = 0xffe0c0e0
    
    class Pascal:
        PreProcessorParenthesis = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        PreProcessor = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        CommentParenthesis = 0xff3465a4
        Asm = 0xff3465a4
        Character = 0xff3465a4
        Default = 0xff3465a4
        Operator = 0xff3465a4
        UnclosedString = 0xffe0c0e0
        Number = 0xff3465a4
        Identifier = 0xff3465a4
        Keyword = 0xff3465a4
        HexNumber = 0xff3465a4
    
    class Perl:
        Translation = 0xfff0e080
        BacktickHereDocument = 0xffddd0dd
        Array = 0xffffffe0
        QuotedStringQXVar = 0xffa08080
        PODVerbatim = 0xffc0ffc0
        DoubleQuotedStringVar = 0xff3465a4
        Regex = 0xffa0ffa0
        HereDocumentDelimiter = 0xffddd0dd
        SubroutinePrototype = 0xff3465a4
        BacktickHereDocumentVar = 0xffddd0dd
        QuotedStringQR = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        QuotedStringQRVar = 0xff3465a4
        SubstitutionVar = 0xff3465a4
        Operator = 0xff3465a4
        DoubleQuotedHereDocumentVar = 0xffddd0dd
        Identifier = 0xff3465a4
        QuotedStringQX = 0xff3465a4
        BackticksVar = 0xffa08080
        Keyword = 0xff3465a4
        QuotedStringQ = 0xff3465a4
        QuotedStringQQVar = 0xff3465a4
        QuotedStringQQ = 0xff3465a4
        POD = 0xffe0ffe0
        FormatIdentifier = 0xff3465a4
        RegexVar = 0xff3465a4
        Backticks = 0xffa08080
        DoubleQuotedHereDocument = 0xffddd0dd
        Scalar = 0xffffe0e0
        FormatBody = 0xfffff0ff
        Comment = 0xff3465a4
        QuotedStringQW = 0xff3465a4
        SymbolTable = 0xffe0e0e0
        Default = 0xff3465a4
        Error = 0xffff0000
        SingleQuotedHereDocument = 0xffddd0dd
        Number = 0xff3465a4
        Hash = 0xffffe0ff
        Substitution = 0xfff0e080
        DataSection = 0xfffff0d8
        DoubleQuotedString = 0xff3465a4
    
    class PostScript:
        DictionaryParenthesis = 0xff3465a4
        HexString = 0xff3465a4
        DSCCommentValue = 0xff3465a4
        ProcedureParenthesis = 0xff3465a4
        Comment = 0xff3465a4
        ImmediateEvalLiteral = 0xff3465a4
        Name = 0xff3465a4
        DSCComment = 0xff3465a4
        Default = 0xff3465a4
        Base85String = 0xff3465a4
        Number = 0xff3465a4
        ArrayParenthesis = 0xff3465a4
        Literal = 0xff3465a4
        BadStringCharacter = 0xffff0000
        Text = 0xff3465a4
        Keyword = 0xff3465a4
    
    class Properties:
        DefaultValue = 0xff3465a4
        Default = 0xff3465a4
        Section = 0xffe0f0f0
        Assignment = 0xff3465a4
        Key = 0xff3465a4
        Comment = 0xff3465a4
    
    class Python:
        TripleDoubleQuotedString = 0xff3465a4
        FunctionMethodName = 0xff3465a4
        TabsAfterSpaces = 0xff3465a4
        Tabs = 0xff3465a4
        Decorator = 0xff3465a4
        NoWarning = 0xff3465a4
        UnclosedString = 0xffe0c0e0
        Spaces = 0xff3465a4
        CommentBlock = 0xff3465a4
        Comment = 0xff3465a4
        TripleSingleQuotedString = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        Inconsistent = 0xff3465a4
        Default = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        Operator = 0xff3465a4
        Number = 0xff3465a4
        Identifier = 0xff3465a4
        ClassName = 0xff3465a4
        Keyword = 0xff3465a4
        HighlightedIdentifier = 0xff3465a4
    
    class Ruby:
        Symbol = 0xff3465a4
        Stderr = 0xffff8080
        Global = 0xff3465a4
        FunctionMethodName = 0xff3465a4
        Stdin = 0xffff8080
        HereDocumentDelimiter = 0xffddd0dd
        PercentStringr = 0xffa0ffa0
        PercentStringQ = 0xff3465a4
        ModuleName = 0xff3465a4
        HereDocument = 0xffddd0dd
        SingleQuotedString = 0xff3465a4
        PercentStringq = 0xff3465a4
        Regex = 0xffa0ffa0
        Operator = 0xff3465a4
        PercentStringw = 0xffffffe0
        PercentStringx = 0xffa08080
        POD = 0xffc0ffc0
        Keyword = 0xff3465a4
        Stdout = 0xffff8080
        ClassVariable = 0xff3465a4
        Identifier = 0xff3465a4
        DemotedKeyword = 0xff3465a4
        Backticks = 0xffa08080
        InstanceVariable = 0xff3465a4
        Comment = 0xff3465a4
        Default = 0xff3465a4
        Error = 0xffff0000
        Number = 0xff3465a4
        DataSection = 0xfffff0d8
        ClassName = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
    
    class SQL:
        PlusComment = 0xff3465a4
        KeywordSet7 = 0xff3465a4
        PlusPrompt = 0xffe0ffe0
        CommentDocKeywordError = 0xff3465a4
        CommentDocKeyword = 0xff3465a4
        KeywordSet6 = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        Operator = 0xff3465a4
        QuotedIdentifier = 0xff3465a4
        SingleQuotedString = 0xff3465a4
        PlusKeyword = 0xff3465a4
        Default = 0xff3465a4
        DoubleQuotedString = 0xff3465a4
        CommentLineHash = 0xff3465a4
        KeywordSet5 = 0xff3465a4
        Number = 0xff3465a4
        KeywordSet8 = 0xff3465a4
        Identifier = 0xff3465a4
        Keyword = 0xff3465a4
        CommentDoc = 0xff3465a4
    
    class Spice:
        Function = 0xff3465a4
        Delimiter = 0xff3465a4
        Value = 0xff3465a4
        Default = 0xff3465a4
        Number = 0xff3465a4
        Parameter = 0xff3465a4
        Command = 0xff3465a4
        Identifier = 0xff3465a4
        Comment = 0xff3465a4
    
    class TCL:
        SubstitutionBrace = 0xff3465a4
        CommentBox = 0xfff0fff0
        ITCLKeyword = 0xfffff0f0
        TkKeyword = 0xffe0fff0
        Operator = 0xff3465a4
        QuotedString = 0xfffff0f0
        ExpandKeyword = 0xffffff80
        KeywordSet7 = 0xff3465a4
        TCLKeyword = 0xff3465a4
        TkCommand = 0xffffd0d0
        Identifier = 0xff3465a4
        KeywordSet6 = 0xff3465a4
        CommentLine = 0xff3465a4
        CommentBlock = 0xfff0fff0
        Comment = 0xfff0ffe0
        Default = 0xff3465a4
        KeywordSet9 = 0xff3465a4
        Modifier = 0xff3465a4
        Number = 0xff3465a4
        KeywordSet8 = 0xff3465a4
        Substitution = 0xffeffff0
        QuotedKeyword = 0xfffff0f0
    
    class TeX:
        Symbol = 0xff3465a4
        Default = 0xff3465a4
        Command = 0xff3465a4
        Group = 0xff3465a4
        Text = 0xff3465a4
        Special = 0xff3465a4
    
    class VHDL:
        StandardOperator = 0xff3465a4
        Attribute = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        String = 0xff3465a4
        Default = 0xff3465a4
        Operator = 0xff3465a4
        StandardPackage = 0xff3465a4
        Number = 0xff3465a4
        Identifier = 0xff3465a4
        KeywordSet7 = 0xff3465a4
        StandardFunction = 0xff3465a4
        StandardType = 0xff3465a4
        Keyword = 0xff3465a4
        UnclosedString = 0xffe0c0e0
    
    class Verilog:
        CommentBang = 0xffe0f0ff
        UserKeywordSet = 0xff3465a4
        Preprocessor = 0xff3465a4
        CommentLine = 0xff3465a4
        Comment = 0xff3465a4
        KeywordSet2 = 0xff3465a4
        Default = 0xff3465a4
        Operator = 0xff3465a4
        Number = 0xff3465a4
        Identifier = 0xff3465a4
        SystemTask = 0xff3465a4
        String = 0xff3465a4
        Keyword = 0xff3465a4
        UnclosedString = 0xffe0c0e0
    
    class XML:
        HTMLValue = 0xffffefff
        PythonDefault = 0xffefffef
        Entity = 0xff3465a4
        SGMLParameter = 0xffefefff
        SGMLDefault = 0xffefefff
        PHPVariable = 0xfffff8f8
        SGMLCommand = 0xffefefff
        PythonClassName = 0xffefffef
        VBScriptUnclosedString = 0xff7f7fff
        ASPJavaScriptDefault = 0xffdfdf7f
        ASPVBScriptStart = 0xff3465a4
        VBScriptDefault = 0xffefefff
        PythonNumber = 0xffefffef
        PythonOperator = 0xffefffef
        ASPJavaScriptSingleQuotedString = 0xffdfdf7f
        PHPDefault = 0xfffff8f8
        XMLStart = 0xff3465a4
        PythonFunctionMethodName = 0xffefffef
        ASPJavaScriptStart = 0xff3465a4
        JavaScriptWord = 0xfff0f0ff
        PHPSingleQuotedString = 0xfffff8f8
        PythonTripleDoubleQuotedString = 0xffefffef
        JavaScriptComment = 0xfff0f0ff
        Default = 0xff3465a4
        SGMLSingleQuotedString = 0xffefefff
        VBScriptComment = 0xffefefff
        ASPVBScriptNumber = 0xffcfcfef
        ASPJavaScriptCommentDoc = 0xffdfdf7f
        PythonIdentifier = 0xffefffef
        VBScriptKeyword = 0xffefefff
        JavaScriptDefault = 0xfff0f0ff
        PythonStart = 0xff3465a4
        ASPPythonComment = 0xffcfefcf
        ASPJavaScriptWord = 0xffdfdf7f
        SGMLParameterComment = 0xff3465a4
        JavaScriptSingleQuotedString = 0xfff0f0ff
        PythonSingleQuotedString = 0xffefffef
        HTMLSingleQuotedString = 0xff3465a4
        ASPVBScriptString = 0xffcfcfef
        SGMLBlockDefault = 0xffcccce0
        PythonKeyword = 0xffefffef
        XMLTagEnd = 0xff3465a4
        ASPVBScriptComment = 0xffcfcfef
        ASPPythonSingleQuotedString = 0xffcfefcf
        PHPDoubleQuotedVariable = 0xfffff8f8
        ASPJavaScriptComment = 0xffdfdf7f
        JavaScriptUnclosedString = 0xffbfbbb0
        JavaScriptDoubleQuotedString = 0xfff0f0ff
        UnknownAttribute = 0xff3465a4
        ASPPythonOperator = 0xffcfefcf
        ASPJavaScriptSymbol = 0xffdfdf7f
        ASPPythonFunctionMethodName = 0xffcfefcf
        SGMLDoubleQuotedString = 0xffefefff
        PHPOperator = 0xfffff8f8
        JavaScriptNumber = 0xfff0f0ff
        PythonDoubleQuotedString = 0xffefffef
        ASPAtStart = 0xffffff00
        Script = 0xff3465a4
        PHPCommentLine = 0xfffff8f8
        SGMLComment = 0xffefefff
        JavaScriptStart = 0xff3465a4
        ASPPythonIdentifier = 0xffcfefcf
        ASPVBScriptKeyword = 0xffcfcfef
        ASPPythonTripleDoubleQuotedString = 0xffcfefcf
        ASPPythonKeyword = 0xffcfefcf
        ASPJavaScriptNumber = 0xffdfdf7f
        PHPStart = 0xffffefbf
        PythonTripleSingleQuotedString = 0xffefffef
        PHPNumber = 0xfffff8f8
        ASPPythonDefault = 0xffcfefcf
        SGMLSpecial = 0xffefefff
        OtherInTag = 0xff3465a4
        JavaScriptCommentDoc = 0xfff0f0ff
        Tag = 0xff3465a4
        XMLEnd = 0xff3465a4
        CDATA = 0xfffff0f0
        HTMLNumber = 0xff3465a4
        SGMLError = 0xffff6666
        PHPKeyword = 0xfffff8f8
        ASPVBScriptUnclosedString = 0xff7f7fff
        ASPPythonNumber = 0xffcfefcf
        VBScriptString = 0xffefefff
        ASPPythonClassName = 0xffcfefcf
        ASPPythonStart = 0xff3465a4
        JavaScriptRegex = 0xffffbbb0
        ASPJavaScriptUnclosedString = 0xffbfbbb0
        ASPJavaScriptCommentLine = 0xffdfdf7f
        SGMLEntity = 0xffefefff
        ASPJavaScriptDoubleQuotedString = 0xffdfdf7f
        ASPStart = 0xffffdf00
        Attribute = 0xff3465a4
        ASPJavaScriptKeyword = 0xffdfdf7f
        ASPVBScriptDefault = 0xffcfcfef
        ASPVBScriptIdentifier = 0xffcfcfef
        ASPJavaScriptRegex = 0xffffbbb0
        VBScriptNumber = 0xffefefff
        HTMLDoubleQuotedString = 0xff3465a4
        ASPXCComment = 0xff3465a4
        VBScriptStart = 0xff3465a4
        PHPDoubleQuotedString = 0xfffff8f8
        PHPComment = 0xfffff8f8
        ASPPythonTripleSingleQuotedString = 0xffcfefcf
        ASPPythonDoubleQuotedString = 0xffcfefcf
        JavaScriptKeyword = 0xfff0f0ff
        JavaScriptSymbol = 0xfff0f0ff
        VBScriptIdentifier = 0xffefefff
        HTMLComment = 0xff3465a4
        UnknownTag = 0xff3465a4
        JavaScriptCommentLine = 0xfff0f0ff
        PythonComment = 0xffefffef
    
    class YAML:
        TextBlockMarker = 0xff3465a4
        DocumentDelimiter = 0xfff3c969
        Operator = 0xff3465a4
        Number = 0xff3465a4
        Default = 0xff3465a4
        Identifier = 0xff3465a4
        Reference = 0xff3465a4
        Comment = 0xff3465a4
        Keyword = 0xff3465a4
        SyntaxErrorMarker = 0xffff0000
    




