# 程序文档

**data 文件夹**：存放矩阵数据的 txt 文件，最后一列是 b。

**model 文件夹**：
模型文件在 model 文件夹中。

**utils 文件夹**：存放辅助功能实现文件，如格式化输出矩阵，从文件中读取矩阵。

**main.py**：是模型使用的核心文件，可以调用关于矩阵正交分解的 `Modified Gram-Schmidt`、`Householder Reduction` 和 `Givens Reduction` 的程序实现。具体使用方式如下：

```python
python main.py --model HR --input ./data/input.txt
```

其中：
- `--model` 参数需要传入要调用的矩阵分解方法，可选项为 `[MGS, HR, GR]` ，
  不传入参数则默认是`HR`分解。

- `--input` 参数需要传入矩阵 txt 文件所在路径，不传入路径则默认路径为`./data/input.txt`。