# -*- coding: utf-8 -*-
#
# python-srt2ass: https://github.com/ewwink/python-srt2ass
# by: ewwink
# modified by:  一堂宁宁
# modified by: Lenshyuu227

import sys
import os
import re
import codecs


def fileopen(input_file):
    # use correct codec to encode the input file
    encodings = ["utf-32", "utf-16", "utf-8", "cp1252", "gb2312", "gbk", "big5"]
    tmp = ''
    for enc in encodings:
        try:
            with codecs.open(input_file, mode="r", encoding=enc) as fd:
                # return an instance of StreamReaderWriter
                tmp = fd.read()
                break
        except:
            # print enc + ' failed'
            continue
    return [tmp, enc]


def srt2ass(input_file,sub_style):
    if '.ass' in input_file:
        return input_file

    if not os.path.isfile(input_file):
        print(input_file + ' not exist')
        return

    src = fileopen(input_file)
    tmp = src[0]
    # encoding = src[1] # Will not encode so do not need to pass codec para
    src = ''
    utf8bom = ''

    if u'\ufeff' in tmp:
        tmp = tmp.replace(u'\ufeff', '')
        utf8bom = u'\ufeff'
    
    tmp = tmp.replace("\r", "")
    lines = [x.strip() for x in tmp.split("\n") if x.strip()]
    subLines = ''
    tmpLines = ''
    lineCount = 0
    output_file = '.'.join(input_file.split('.')[:-1])
    output_file += '.ass'

    for ln in range(len(lines)):
        line = lines[ln]
        if line.isdigit() and re.match('-?\d\d:\d\d:\d\d', lines[(ln+1)]):
            if tmpLines:
                subLines += tmpLines + "\n"
            tmpLines = ''
            lineCount = 0
            continue
        else:
            if re.match('-?\d\d:\d\d:\d\d', line):
                line = line.replace('-0', '0')
                if sub_style =='default':
                    tmpLines += 'Dialogue: 0,' + line + ',default,,0,0,0,,'
                elif sub_style =='227CN':
                    tmpLines += 'Dialogue: 0,' + line + ',Default_1080卫星,,0,0,0,,'
            else:
                if lineCount < 2:
                    tmpLines += line
                else:
                    tmpLines += "\n" + line
            lineCount += 1
        ln += 1


    subLines += tmpLines + "\n"

    subLines = re.sub(r'\d(\d:\d{2}:\d{2}),(\d{2})\d', '\\1.\\2', subLines)
    subLines = re.sub(r'\s+-->\s+', ',', subLines)
    # replace style
    # subLines = re.sub(r'<([ubi])>', "{\\\\\g<1>1}", subLines)
    # subLines = re.sub(r'</([ubi])>', "{\\\\\g<1>0}", subLines)
    # subLines = re.sub(r'<font\s+color="?#(\w{2})(\w{2})(\w{2})"?>', "{\\\\c&H\\3\\2\\1&}", subLines)
    # subLines = re.sub(r'</font>', "", subLines)

    if sub_style == 'default':
        head_str = head_str_default
    elif sub_style == '227CN':
        head_str = head_str_227

    output_str = utf8bom + head_str + '\n' + subLines
    # encode again for head string
    output_str = output_str.encode('utf8')

    with open(output_file, 'wb') as output:
        output.write(output_str)

    output_file = output_file.replace('\\', '\\\\')
    output_file = output_file.replace('/', '//')
    return output_file


# if len(sys.argv) > 1:
#     for name in sys.argv[1:]:
#         srt2ass(name,sub_style=)


head_str_default = '''[Script Info]
; This is an Advanced Sub Station Alpha v4+ script.
; The script is generated by N46Whisper_227
Title:
ScriptType: v4.00+
Collisions: Normal
PlayDepth: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: default,Meiryo,90,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00050506,-1,0,0,0,100,100,5,0,1,3.5,0,2,135,135,10,1
[Events]
Format: Layer, Start, End, Style, Actor, MarginL, MarginR, MarginV, Effect, Text'''



head_str_227 = '''[Script Info]
; This is an Advanced Sub Station Alpha v4+ script.
; The script is generated by N46Whisper
Title:
ScriptType: v4.00+
Collisions: Normal
PlayDepth: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default_1080卫星,Noto Sans CJK SC Bold,85,&H00FFFFFF,&H000019FF,&H00C6910E,&H00000000,-1,0,0,0,100,100,0,0,1,3,2,2,11,11,20,1
Style: 节目组的※,Noto Sans CJK SC Bold,89,&H00494949,&H000000FF,&H00F3F3F9,&H00000000,0,0,0,0,100,100,0,0,1,3,2,1,0,0,100,1
Style: 吐槽（左）,Noto Sans CJK SC Bold,55,&H00FFFFFF,&H000019FF,&H00030304,&H00000000,-1,0,0,0,100,100,0,0,1,1,2,7,100,773,310,1
Style: 看板（蓝色-白底）,Resource Han Rounded CN Medium,110,&H00C0742E,&H000019FF,&H00FFFFFF,&H00000000,-1,0,0,0,86.6667,100,0,0,1,4,0,2,5,5,10,1
Style: 看板（淡蓝-白底）,Benmo Zhuhei,110,&H00EF9E06,&H000019FF,&H00FFFFFF,&H00000000,-1,0,0,0,86.6667,100,0,0,1,4,0,2,5,5,10,1
Style: 看板（橙底-白边）,Benmo Zhuhei,110,&H00069AF7,&H000019FF,&H00FFFFFF,&H00000000,-1,0,0,0,86.6667,100,0,0,1,4,0,2,5,5,10,1
Style: 标题,Benmo Zhuhei,70,&H00FFFFFF,&H000019FF,&H00FFFFFF,&H00986007,-1,0,0,0,100,100,0,0,1,4,2,1,120,120,190,1
Style: 节目组的※,Noto Sans CJK SC Bold,89,&H00494949,&H000000FF,&H00F3F3F9,&H00000000,0,0,0,0,100,100,0,0,1,3,2,1,0,0,100,1
Style: 注释,Noto Sans CJK SC Bold,52,&H00FFFFFF,&H000000FF,&H00868072,&H00868072,0,0,0,0,100,100,0,0,1,3,1,9,60,60,32,1
Style: 227logo,Noto Sans CJK SC Bold,62,&H00D58D00,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,2,16,16,16,1
Style: STAFF,Noto Sans CJK SC Bold,75,&H00FFFFFF,&H00FFFF00,&H00C6910E,&H00000000,-1,0,0,0,100,100,0,0,1,3,2,7,30,0,30,1

[Events]
Format: Layer, Start, End, Style, Actor, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,0:23:59.98,227logo,,0,0,0,,{\p1\alpha99\an9\1vc(&HD58D00&,&HD2AA03&,&HD58D00&,&HD2AA03&)\fscx110\fscy110\pos(1798,22)}m 244 46 b 244 46 244 46 244 46 b 252 24 288 16 290 47 b 291 69 263 81 247 94 b 262 93 288 98 293 85 b 296 86 288 92 288 100 b 314 81 326 73 333 58 b 337 47 331 41 329 39 b 324 34 319 35 313 36 b 307 37 303 43 299 47 b 299 43 304 38 306 35 b 308 33 310 30 314 29 b 317 28 321 27 324 27 b 335 25 342 35 344 41 b 347 48 343 58 342 58 b 339 64 334 69 329 74 b 325 77 321 81 317 84 b 312 87 307 91 302 94 b 313 94 323 95 332 92 b 336 89 340 86 343 83 b 346 80 348 76 351 73 b 359 64 378 41 420 49 b 419 51 419 51 418 52 b 390 45 371 56 357 69 b 357 71 357 72 359 72 b 372 72 385 72 399 72 b 382 94 369 115 358 137 b 352 143 348 137 349 133 b 362 114 376 97 388 80 b 378 80 370 80 360 80 b 347 78 325 109 351 152 b 351 153 350 153 350 154 b 342 143 333 128 337 103 b 337 101 334 99 232 101 b 247 88 272 75 277 59 b 282 51 278 33 259 36 b 252 36 247 43 245 46 b 245 46 244 46 244 46  {\p0\fs41\fnNoto Sans CJK SC bold\b1}中文应援团
Dialogue: 0,0:00:00.00,0:00:07.58,STAFF,,0,0,0,,{\an7\fad(300,300)}本字幕仅作学习交流之用 禁止二次上传及用于营业目的的传播\N翻译：XX XX XX XX \N时轴：XX XX XX XX\N校对&压制：XX\N更多请关注@227中文应援站'''

