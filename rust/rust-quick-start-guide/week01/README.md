# Week01 <!-- omit in toc -->

## Table of content <!-- omit in toc -->
- [Homework](#homework)
  - [Description](#description)
  - [Output](#output)
- [Course](#course)
  - [Char vs String](#char-vs-string)
  - [Copy vs Clone](#copy-vs-clone)


## Homework

### Description

1. 添加一个一层子模块，循环打印从’a’~’Z’ 之间的所有字符
2. 添加一个二层子模块，循环打印从’A’~’z’ 之间的所有字符
3. 使用Cargo编译运行此工程

P.S. 需要自行发现其中的细节，一个考点是：ascii码字符的顺序

### Output

```shell
$ cargo run
a`_^]\[Z
ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz
```

## Course

Resource
- [A half-hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust)
- [The Rust Standard Library](https://doc.rust-lang.org/std/index.html)

### Char vs String

The `char` is a 'Unicode scalar value' but a 'Unicode code point'. It's always four bytes in size.

The `String` is UTF-8-encoded and the UTF-8 is a variable width encoding.

- [char](https://doc.rust-lang.org/std/primitive.char.html)
  - [Unicode Scalar Value](https://unicode.org/glossary/#unicode_scalar_value)
- [String](https://doc.rust-lang.org/std/string/struct.String.html)
- [str](https://doc.rust-lang.org/std/primitive.str.html)
  - [Literals and escapes](https://doc.rust-lang.org/rust-by-example/std/str.html#literals-and-escapes)

### Copy vs Clone

Clone is an ability to explicitly duplicate an object.

Copy is simply copying bits. It also requires the Clone trait.

- [Copy](https://doc.rust-lang.org/std/marker/trait.Copy.html)
- [Clone](https://doc.rust-lang.org/std/clone/trait.Clone.html)
- [Drop](https://doc.rust-lang.org/std/ops/trait.Drop.html)

