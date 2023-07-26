# Week04a <!-- omit in toc -->

## Table of content <!-- omit in toc -->
- [Homework](#homework)
  - [Description](#description)
  - [Output](#output)
  - [Comparison](#comparison)


## Homework

### Description

使用枚举包裹三个不同的类型，并放入一个Vec中，对Vec进行遍历，调用三种不同类型的各自的方法。  
定义三个不同的类型，使用Trait Object，将其放入一个Vec中，对Vec进行遍历，调用三种不同类型的各自的方法。  
同时，说明其上两种不同实现方法的区别。

### Output

```shell
$ cargo run
Enum:
Bird says hi enum!
Cat says hi enum!
Dog says hi enum!

Trait:
Bird says hi trait!
Cat says hi trait!
Dog says hi trait!
```

### Comparison

Enum vs Trait
- 弹性
  - Enum 适合限定数量的类型集合。
  - Trait 适合开放数量的类型集合。
  - Trait 比较弹性， 其他使用者可新增自定义类型实现 Trait。
- 如何达成 delegation
  - Enum 是在 method 中 match statement 实现。
  - Trait 是在 Trait Object 中，runtime 查找 vtable 达成。
  - Enum 比较有编译器优化的空间(ex: inline)，Trait 则无。
- 限制
  - Trait 需要符合 Object Safety 的规则才可创建 Trait Object。
    - 非所有 Trait 都可以创建成 Trait Object。
    - 不是所有 function 都可以放入 vtable。

下表引用自参考文章

| Delegation  Construct | Set of Types | Performance   | Restrictions  |
| :-------------------- | :----------- | :------------ | :------------ |
| Enum                  | Closed       | Fast (branch) | N/A           |
| Trait Object          | Open         | Slow (vtable) | Object Safety |

Reference
- [Enum or Trait Object](https://www.possiblerust.com/guide/enum-or-trait-object)
- [Polymorphism in Rust: Enums vs Traits](https://www.mattkennedy.io/blog/rust_polymorphism/)
- [Performance implications of `Box<Trait>` vs `enum` delegation](https://users.rust-lang.org/t/performance-implications-of-box-trait-vs-enum-delegation/11957)
- [trait object](https://zhuanlan.zhihu.com/p/23791817)
