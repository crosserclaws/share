# Week04b <!-- omit in toc -->

## Table of content <!-- omit in toc -->
- [Homework](#homework)
  - [Description](#description)
  - [Result](#result)


## Homework

### Description

实现一个函数，为u32类型的整数集合求和，参数类型为 &[u32]，返回类型为Option，溢出时返回None

### Result

```shell
$ cargo run
Sum of [1, 2, 3] is Some(6)
Sum of [1, 2, 4294967295] is None
```
