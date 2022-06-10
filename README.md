# Auto WJX

### 原作者留言：

- 不会真有人，连问卷星都要弄虚作假吧。
- 形式主义既然是形式，那就试着形式地自动化。
- 我相信会用自动化的宝贝们，没人会在真正重要的作业上搞自动化吧。
- 仅支持多选题，单选题，以不放回的方式随机选择
- python + selenium，虽不优雅，但省时有效
- ~~954-ivory 的回复：帮女票弄的，顺手给你改了些东西，现在应该优雅了点。~~

### 教程 - Tutorial

#### 配置教程（Bing 能搜出一堆教程，以下仅供参考）

1. 安装 [python](https://www.python.org/downloads/) （安装完毕，可用以下命令查询 python 安装路径）

```python
from os import path

print(path)  # Windows 下，在 Python 命令行中可直接打印当前 path。
```

2. 利用 pip 安装项目依赖

```shell
pip install -r requirements.txt
```

3. 下载

- 谷歌浏览器
  [Chrome Driver](http://chromedriver.storage.googleapis.com/index.html) ,
  [Chrome Driver 淘宝镜像](https://registry.npmmirror.com/binary.html?path=chromedriver/)
- 火狐浏览器 [Gecko Driver](https://github.com/mozilla/geckodriver/releases)
- IE 浏览器 [IE Driver](http://selenium-release.storage.googleapis.com/index.html)

4. 在 `wjx.py` 中配置 Driver

```python
# wjx.py 

driver = webdriver.Chrome(options=opt)  # Windows下，将对应版本的 chromedriver 放置在 python 根目录，默认启用该行。

# ------或者 -------

driver = webdriver.Chrome(executable_path=r'./chromedriver', options=opt)  # 该行已被注释

```

#### 示例用法

1. 修改 `conf.py` 中的配置项

```python
# conf.py

# 以配置项执行
QUESTION_URL = "https://www.wjx.cn/vm/wE5Js0M.aspx"  # 问卷地址
LOOP_COUNT = 1  # 执行次数

# ------或者-------

# 以命令行交互
QUESTION_URL = None
LOOP_COUNT = None
```

2. 修改 `wjx.py` 中的 `choose_answer()` 方法

```python
# wjx.py

# 为方便非计算机专业朋友们食用，以下示例以伪代码的形式给出，请自行替换参数。
choose_one(题号, [概率1, 概率2, ...])
choose_multiple(题号, [概率1, 概率2, ...], 最多选项限制（可选参数）)
```

3. 利用 `cmd` 执行项目脚本

```shell
cd /path/to/auto_wjx # 这里的 /path/to/auto_wjx 替换成你本机的文件夹路径
python wjx.py
```

---

### 更新日志 - Update log

#### 2022-06-11

_以下示例以 `choose_one` 为例，`choose_multiple` 同理。_

1. 实现了相同概率选项的自动填充：

```python
# wjx.py

choose_one(1, [0.25, 0.25, 0.25, 0.25])  # 之前的做法。
choose_one(1)  # 各项均为相同概率，可省略不写。
```

2. 新增排除某些选项的支持（目前仅支持上述自动填充的写法）：

```python
# wjx.py

choose_one(1, exclude=[1])  # 排除第 1 题中，第 1 个选项。
choose_one(1, exclude=[1, 2, 3])  # 排除第 1 题中，第 1, 2, 3 个选项。 

choose_one(1, [0, 0.4, 0.6])  # 各项概率不相同，则没必要用 `exclude`，直接将排除项置 0。
```

3. 实现了右滑验证码逃逸（默认窗口大小应该能够逃逸，有问题请自行调教参数 dest）。
4. 用 Python 层的实现，替代了 `circle.sh`，降低了使用门槛。

### TODO

- 新增利用 `conf.py` 来配置选中项的功能。
- 实现其他类型 `input` 的自动填写功能。
