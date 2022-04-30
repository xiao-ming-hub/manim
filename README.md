# manim
## 介绍
Manim视频源代码

B站账号[HelloWorldXi](https://space.bilibili.com/517182576)
## manim安装思路
大概就是装好依赖，然后安装，完事

```sh
sudo apt install ffmpeg -y
sudo apt install texlive-full -y
#然后安装pango，这个我不太确定怎么装
```
如果你想修改Manim源代码并使用或者使用最新版本，可以这样：
```sh
#安装opengl，我也不确定大概是怎么样（逃
git clone https://github.com/3b1b/manim.git
cd manim
sudo pip install -e .
manimgl --help #测试
```
如果你只想用Manim的话那就这样：
```sh
sudo pip install manimgl
manimgl --help #测试
```
[建议看看这个Manim Kindergarten成员编写的中文文档](https://github.com/manim-kindergarten/manim_document_zh)

