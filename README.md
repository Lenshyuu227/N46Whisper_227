# N46Whisper

Language : English | [简体中文](./README_CN.md) 

N46Whisper is a Google Colab notebook application that developed for streamlined video subtitle file generation to improve productivity of Nogizaka46 (and Sakamichi groups) subbers.

The notebook is based on [Whisper](https://github.com/openai/whisper), a general-prupose speech recognition model.

The output file will be in Advanced SubStation Alpha(ass) format with built-in style of selected sub group so it can be directly imported into [Aegisub](https://github.com/Aegisub/Aegisub) for subsequent editing.

## What's New：
2023.3.15:
* Add functions to split multiple words/sententces in one line.
* Update documents and other minor fixes.

2023.3.12:
* Add chatGPT translation and bilingual subtitle file generation features.
* Update documents and other minor fixes.

2023.01.26：
* Update scripts to reflect recent changes in Whisper.

2022.12.31：
* Allow user to select files directly from mounted google drive.
* Other minor fixes.

2023.2.15（@Lenshyuu227）：
* Add large-v2 option.
* Add '227CN' Styles.
* Modify links.
* If you have any thoughts, requests or questions that directly related to this Fork, please feel free to post issues here or [Contact Me](mailto:kakiharuka@lenshyuu.com)

2023.2.17 (@Lenshyuu227)：
* Add srt2ass_test.ipynb (for srt2ass test in local environment).
* Add testData folder (test data for srt2ass).
* Modify srt2ass.py to split lines with spaces. Those splited lines all use the same time stamp, with 'adjust_required' label to remind users to adjust the time stamps while editing the subtitle file to avoid overlapping.

## How to use
* [Click here](https://colab.research.google.com/github/Lenshyuu227/N46Whisper_227/blob/main/N46Whisper.ipynb) to open the notebook in Google Colab.
* Upload file and follow the instruction to run the notebook.
* The ass file will be automatically downloaded once done.

## AI translation
The notebook now allow users to translate transcribed subtitle text line by line using AT translation tools.

Currently, it supports `chatGPT` and the default target language is `zh-CN`.

The translated text will be append in the same line after the original text and sepearted by `/N`, such that a new bilingual subtitle file is generated.

For instance: 

![QQ截图20230312155700](https://user-images.githubusercontent.com/49441654/224525469-18a43cbc-33b9-4b2f-b7ca-7ae0c1865b17.png)

An example of bilingual subtitle:

![QQ截图20230312160015](https://user-images.githubusercontent.com/49441654/224525526-51e2123c-6e1c-427c-8d67-9ccd4a7e6630.png)

To use the AI translation, users must use their own OpenAI API Key. To obtain a free Key, go to https://platform.openai.com/account/api-keys

Please note there will be limitaions on usage for free keys, choose a paid plan to speed up at your own cost.

## Split lines
Users can choose to split text in a single line by space.The child lines will have same time stamp with the parent line, respectively.

For instance, for a line contains multiple long sentences:
>Dialogue: 0,0:01:00.52,0:01:17.52,default,,0,0,0,,Birthday Liveについて話そうかなと思います よろしくお願いします

After split:
>Dialogue: 0,0:01:00.52,0:01:17.52,default,,0,0,0,,Birthday Liveについて話そうかなと思います(adjust_required)

>Dialogue: 0,0:01:00.52,0:01:17.52,default,,0,0,0,,ろしくお願いします(adjust_required)

## Support
The application can substantially reduce the labor and time cost of sub groups or individual subbers. However, despite the impressive performance, the Whisper model and the application itself are not come without limitations. Please read the orgininal documents and Discussions to learn more about the usage of Whisper and the common issues.

However, if you have any throughts, requests or questions that directly related to making subtitiles for Sakamichi group girls, please feel free to post here or [contact me](mailto:admin@ikedateresa.cc)

## License
The code is released under the MIT license. See [License](./LICENSE.md) for details.

