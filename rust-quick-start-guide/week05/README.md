# Week05 <!-- omit in toc -->

## Table of content <!-- omit in toc -->
- [Homework](#homework)
  - [Description](#description)
  - [Answer](#answer)
  - [Reference](#reference)


## Homework

### Description

请搜索相关文档，实现：一个简单的声明宏。并理解其代码结构，和编译过程。

### Answer

Rust 中，宏(Macros) 方便开发者在编译期拓展和生成新代码。
1. 声明宏(Declarative macros): 以声明性的方式定义句法拓展(Syntax Extension)。
2. 过程宏(Procedural macros): 可对 Rust 句法(Syntax) 进行操作。

定义 2 个声明宏
1. `set`: 简易创建 HashSet 的方式，`vec!` 的 HashSet 版本。
2. `eval`: 输出表达式的内容和执行结果。

Note
1. set 使用了 2 条规则(rule)，分别对应无元素(element)和一个以上的元素。
2. 两个宏都只用了表达式(expr)类型。 

使用范例如下

```rust
fn main() {
    let my_set = set!(1, 2, 3);
    eval!(my_set);
}
```

```shell
$ cargo run
Eval: "my_set" = {1, 2, 3}
```

范例经过 `cargo expand` 后的输出如下

```rust
#![feature(prelude_import)]
#[prelude_import]
use std::prelude::rust_2021::*;
#[macro_use]
extern crate std;
fn main() {
    let my_set = {
        let mut s = std::collections::HashSet::new();
        s.insert(1);
        s.insert(2);
        s.insert(3);
        s
    };
    {
        ::std::io::_eprint(format_args!("Eval: {0:?} = {1:?}\n", "my_set", my_set));
    };
}
```

### Reference
- The Rust Programming Language
  - [19.5. Macros](https://doc.rust-lang.org/book/ch19-06-macros.html)
- The Rust Reference
  - [3. Macros](https://doc.rust-lang.org/reference/macros.html)
- Rust By Example
  - [17. macro_rules!](https://doc.rust-lang.org/rust-by-example/macros.html)
- [The Little Book of Rust Macros](https://veykril.github.io/tlborm/introduction.html)



