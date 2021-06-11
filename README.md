# FastEnglishLearn
- 还有1天就要考试了，但是你的英语单词都还没背😂
- 幸好，你预估了一下，自己浏览一个单词只需要6sec就能感到面熟🤔
- 而你，一共有6k个单词要背😓
- 幸运的是，抓紧时间，你只需要36000s=600min=10h就行了😏
- 你决定花一天刷完所有单词，在考前报个佛脚😵
- 或许只要高频词就够了

它使用了我之前写的https://github.com/what-is-me/WordListEnquiry里的moudle来查询单词，运行源代码的只需要`pip`下载一下就好了，或者直接运行`set.bat`

## 下面是最开始生成的各个文件的介绍
### .\config.json:
- 顾名思义，就是软件运行的各项设置，你可以自行修改
```c++
{
    "filename": "list.txt", //打开的单词列表
    "log": ".log", //储存浏览日志
    "choice": 1, //当"online":1时，查询单词的选项
    "color": 1, //是否打开颜色（有的终端会出现乱码，改为0就好）
    "speed": 1, //每个单词停顿的时间，单位(sec)，但是因为读单词，实际会大于2
    "online": 0, //为1则表示只有单词，将联网查询并把解释写到一个新文件里
    "page": 25, //每25个单词翻页
    "div": ":" //online：1则在生成的文件中用此分隔；online：0则读取的文件用此分隔意思和单词
}
```
### .\log:
- 记录你单词背到多少个了
- 删掉默认从头开始
## .\list.txt:（可以改名）
- 单词列表
- 注意：
	1. 需要你自己建立
	2. 每行一个单词/一个单词+意思，用"div"的内容隔开
## 特色
- 可以朗读单词🙃
