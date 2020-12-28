# Graph-Cut

## 运行方法

需要安装依赖，除常用包以外，需要安装图算法工具包python-graph。
命令行运行：
```
pip install python-graph-core
pip install python-graph-dot
```
运行main.py即可。
输入图片路径以及希望生成的图片大小均hard-coded在main.py中。

## 实现
### graph-cut 算法
基于工具包的minimax中提供的最小割最大流算法。
有bug, 输出的图片效果很差。

### 确定新加入patch位置
只实现了随机选取加入位置（若新加入patch完全在已有图片内，则跳过此轮重新选择位置)

