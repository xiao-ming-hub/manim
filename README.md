# manim
Manim 视频代码

[B站账号](https://space.bilibili.com/517182576)

[ManimGL 中文教程文档](https://docs.manim.org.cn/)

## 安装（Ubuntu）
```sh
python3 -m venv manimgl
source manimgl/bin/activate                   # 退出虚拟环境使用 deactivate 命令
# 删除环境：rm -rf manimgl
git clone https://github.com/3b1b/manim
cd manim
pip install -e .                              # 因为是虚拟环境，所以不用 sudo
manimgl example_scenes.py OpeningManimExample # 测试
```

