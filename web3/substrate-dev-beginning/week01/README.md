# Week01 <!-- omit in toc -->

## Table of content <!-- omit in toc -->
- [Homework A](#homework-a)
  - [Description](#description)
  - [Result](#result)
  - [Reference](#reference)
- [Homework B](#homework-b)
  - [Description](#description-1)
  - [Result](#result-1)
  - [Reference](#reference-1)


## Homework A

### Description

请阅读比特币白皮书，并写下你的观后感。需条理清晰，200字以上。

### Result

作为现代社会金融体系里的一员，如果不是因缘阅读比特币白皮书，恐怕也没机会去思考如何跳脱中心化(可信任的第三方)的方式发行货币与从事交易。

比特币白皮书提出基于密码学、资料结构与算法等领域结合的思路，创造出去中心化电子货币：通过公私钥和签名确保交易的真实性，利用 Merkle Tree、链式交易区块和 PoW 解决公开分布式账本下的双重支付问题，并确保交易不受篡改。

虽然比特币实现了去中心化交易的同时仍保有一定的隐私性，但也并非完美，比如部分人士抨击 PoW 机制会消耗巨大的能源，且其交易速度较慢。尽管如此，比特币的出现仍然标志着区块链技术的重要里程碑，启发了 Ethereum 等新一代区块链，也影响了现代金融科技的发展。

### Reference

- [Bitcoin white paper](https://bitcoin.org/en/bitcoin-paper)

## Homework B

### Description

请提供substrate地址。  
参考 [Substrate的地址生成][substrate-zhihu]

### Result

Step 1. 参考 Substrate Doc 的 [Install][substrate-doc-install]，选择对应的平台设定环境，比如 macOS。

设定后的版本如下

```shell
$ rustup +stable -V
rustup 1.26.0 (5af9b9484 2023-04-05)
info: This is the version for the rustup toolchain manager, not the rustc compiler.
info: The currently active `rustc` version is `rustc 1.71.1 (eb26296b5 2023-08-03)`

$ rustup +nightly -V
rustup 1.26.0 (5af9b9484 2023-04-05)
info: This is the version for the rustup toolchain manager, not the rustc compiler.
info: The currently active `rustc` version is `rustc 1.73.0-nightly (03a119b0b 2023-08-07)`
```

Step 2. 参考 [Substrate的地址生成][substrate-zhihu]，并使用其提供的 repository。

```shell
$ git clone https://github.com/antaintan/subx-address.git
$ cd subx-address
$ rustup default nightly
$ cargo update
$ cargo run
```

CAVEAT
- 使用 stable 版本的 Rust 无法通过编译。
- 使用 nightly 版本的 Rust，如果没有升级 dependencies，也会出现编译错误。

Step 3. 使用 API 创建 Substrate 地址(ss58Address)。

```shell
$ curl -X POST localhost:8000/address/new
```

### Reference

- [Substrate的地址生成][substrate-zhihu]
  - [antaintan/subx-address][substrate-address-repo]
- [Substrate Documentation](https://docs.substrate.io/)
  - [Install][substrate-doc-install]
  - Reference
    - [Address formats](https://docs.substrate.io/reference/address-formats/)

[substrate-zhihu]: https://zhuanlan.zhihu.com/p/262929418
[substrate-doc-install]: https://docs.substrate.io/install/
[substrate-address-repo]: https://github.com/antaintan/subx-address