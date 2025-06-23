# Python lambda（匿名函数）

Python 使用 lambda 来创建匿名函数。

lambda 函数是一种小型、匿名的、内联函数，它可以具有任意数量的参数，但只能有一个表达式。

匿名函数不需要使用 def 关键字定义完整函数。

lambda 函数通常用于编写简单的、单行的函数，通常在需要函数作为参数传递的情况下使用，例如在 map()、filter()、reduce() 等函数中。

## lambda 函数特点：

- lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
- lambda 函数通常只包含一行代码，这使得它们适用于编写简单的函数。

> lambda 语法格式：

```
lambda arguments: expression
```

- lambda是 Python 的关键字，用于定义 lambda 函数。
- arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
- expression 是一个表达式，用于计算并返回函数的结果。

