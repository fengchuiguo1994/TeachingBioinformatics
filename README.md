# TeachingBioinformatics
作为助教一些要做的事情

### 1. 在root下面安装python和pip，建议直接安装miniconda
```
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh
bash Miniconda3-py39_4.11.0-Linux-x86_64.sh
安装完毕后
pip install xpinyin
```

### 2. 给上课学生批量创建账号
从老师那获取到学生名单（一般给的excel表格的形式），提取学号和姓名两列，学号在前，姓名在后，创建文件[user.list.txt](创建账号\user.list.txt)。账号的形式是 黄星宇->xyhuang，诸葛星宇->gxyzhu（名的首字母加姓的全拼），密码的形式是 xyhuang_123456 （账号名_学号后六位）
```
python generateuers.py user.list.txt user.passwd.list.txt
bash createuser.sh user.passwd.list.txt
```
bug<br/>
- 1：无法处理复姓，如上文提到的诸葛是没法识别的，识别的结构是 诸 葛星宇
- 2：当出现相同账号的时候程序会将这些账号报道出来，但是本身不做处理，需要管理员自行修改