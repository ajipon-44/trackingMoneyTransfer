# Ethereum の送金追跡プログラム

## 想定内容

犯人は以下のトランザクションでとあるアカウントから、まあまあな量の Ether を不正に送金し、その後捜査の撹乱のため複数のアカウントに対して流出した Ether を拡散しているとする。
https://rinkeby.etherscan.io/tx/0x4c86c6b2c176f0720f02f92adcf4044817e1e2bd76a518a4c2fd0e2429c5d29b

不正送金を Block Height4103935 まで追跡し、以下の情報を取得するプログラムを作成する。

- 送金に関わったアカウント数
- 送金に関わったアカウントリスト
- それぞれの送金に関する送金額

## 実行結果

```
Number of Account: 101
Accounts: {
0xa8df1e04d3ca8bd890b8b876b890d9fecff65bad
0x6020abdc3f6f6e53565f5ea24a62c1a1d6519170
0x3250bc56557e8dd169c2045d8ae99afbf519d296

省略

0xebe0f61ac9db88372b7a2f3ecc1161e588c84c2e
0xa5a0590113585b9ff43794e5fba5ab7e9abcd046
0x88283624eeb2035d7dcb3891fca1653c0f3fbe68
}
Transactions:
from: 0xd0e0a5c78fcc0f9d6a0a509e13645bf86b1e365f, to: 0xa8df1e04d3ca8bd890b8b876b890d9fecff65bad, send: 55.0ETH
from: 0xa8df1e04d3ca8bd890b8b876b890d9fecff65bad, to: 0x6020abdc3f6f6e53565f5ea24a62c1a1d6519170, send: 5.5ETH
from: 0x6020abdc3f6f6e53565f5ea24a62c1a1d6519170, to: 0x3250bc56557e8dd169c2045d8ae99afbf519d296, send: 0.55ETH

省略

from: 0x847cd45ef9fd56156b0ef61f39cdf6786b119504, to: 0xebe0f61ac9db88372b7a2f3ecc1161e588c84c2e, send: 0.00055ETH
from: 0xa1134baaa35ab70ed161b00561b12c710fc1d596, to: 0xa5a0590113585b9ff43794e5fba5ab7e9abcd046, send: 0.00262953737349ETH
from: 0x504a74c8f69c08d5b50fc85a73533ae8197566cc, to: 0x88283624eeb2035d7dcb3891fca1653c0f3fbe68, send: 3.6045567681e-05ETH
```
