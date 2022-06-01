# 不会真有人连问卷星都要弄虚作假吧
## 仅支持多选题，单选题，以不放回的方式随机选择

```python
choose_one(题号,[概率1,概率2,...])
choose_multiple(题号,[概率1,概率2,...],最多选项限制（可选参数）)
```

chromedriver记得替换成自己系统的版本，并在以下句子中更改路径

```python
driver = webdriver.Chrome(executable_path=r'./chromedriver', options=opt)
```

大概连续提交三十次左右会触发滑动验证码，换ip可解，也有解决验证码的代码，但我没跑起来。

我一个晚上跑了两百多份，我感觉差不多够了。


