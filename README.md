# 不会真有人连问卷星都要弄虚作假吧
## 仅支持多选题，单选题，以不放回的方式随机选择
形式主义既然是形式，那就试着形式地自动化

python+selenium，虽不优雅，但省时有效

我相信会用自动化的宝贝们没人会在真正重要的作业上搞自动化吧。

```python
choose_one(题号,[概率1,概率2,...])
choose_multiple(题号,[概率1,概率2,...],最多选项限制（可选参数）)
```
首先安装依赖
```
pip install -r requirements.txt
```

chromedriver记得替换成自己系统的版本，并在以下句子中更改路径

```python
driver = webdriver.Chrome(executable_path=r'./chromedriver', options=opt)
```

大概连续提交三十次左右会触发滑动验证码，换ip可解，也有解决验证码的代码，但我没跑起来。

我一个晚上跑了两百多份，我感觉差不多够了。


