# WikiDataPreprocess

## 简介

该项目是基于 [WikiExtractor](https://github.com/attardi/wikiextractor) 实现的,用于提取wikipedia的数据以及后续的处理，最终获得一篇article一行的数据。

## 本机环境
+ python 3.7.9

## 使用方法

+ 在使用之前需要前往[Wiki备份](https://dumps.wikimedia.org/backup-index.html)下载数据，选择最新版备份下载。链接：[英文版备份](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2)，[中文版备份](https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2)
+ 下载备份之后，即可使用WikiExtractor进行处理，获取数据。
```
python WikiExtractor.py -b 1024M -o output enwiki-latest-pages-articles.xml.bz2
```
+ 处理数据之后，可以在output/AA/文件夹下看到处理后的文件，即可用以下命令再次处理数据，获取每篇文章一行的数据。
```
python extra.py -p output/AA/ -o wikipedia.txt
```
+ -p 是上一步WikiExtractor处理后获得的数据，-o是最后的输出数据

## demo

+ 文件夹data中包含了一小部分由wikiextractor处理之后获取的数据，使用以下命令可对数据进行处理，wikipedia2.txt是处理后的数据。
```
python extra.py -p data -o wikipedia.txt
```