# Description of performance

I used a test file called original.test.txt, which has 200 Japanese sentences, to test maxmatch.py. Below is the code used:
```
cat original.test.txt | python maxmatch.py dictionary.txt > output.test.txt
```
To evaluate the performance of maxmatch.py, I used evaluate.py. Below is the code used:
```
python3 evaluate.py output.test.txt tokenised.test.txt
```

Below is the output of evaluation, including the number of sentences processed and the average Word Error Rate (WER):

Number of sentences: 200\
Average WER: 29.41%

Below is an example of the evaluation results:

WER: 32.65%\
REF: 紀元 前 4 9  年 1 月 1 日 、 マ ル コ   ・ アン ト ニ オ     は 、 総督 が 自分 自身 を 平和 の 友 で ある と 宣言 し た 、 カ エ サ ル    から の 宣言 書 を 読 み 上げ   た 。\
HYP: 紀元 前   49 年 1 月 1 日 、     マルコ ・        アントニオ は 、 総督 が 自分 自身 を 平和 の 友 で ある と 宣言 し た 、       カエサル から の 宣言 書 を     読み上げ た 。\
EVA:      D S              D D S     D  D D S                                             D D D S                D D S

