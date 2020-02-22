from distutils.core import setup, Extension
# 模块名
mode_name = "test4"
# 资源文件
src = ["test_cpy_model.c"]
# 设置
setup(name=mode_name, ext_modules=[Extension(mode_name, src)])

# (pyenv1) liangfeng@liangfengdeMacBook-Pro:learnCpy$ pwd
# /Users/liangfeng/PycharmProjects/ml2/learnCpy
# (pyenv1) liangfeng@liangfengdeMacBook-Pro:learnCpy$ python setup.py build
# (pyenv1) liangfeng@liangfengdeMacBook-Pro:learnCpy$ python setup.py install