# kyopro

D, E がどっちか解けるまで精進する...

## ABC167

- C は、DP かと思ったら違った...
  - bit 全探索なる手法で通せるらしい
- D は、お風呂でおおよその解き方が思いついたがコーナーケース通せず...
- GSoC 落ち着いたら、これやるのもよさそう
  - https://sites.google.com/view/open-data-structures-ja

## ABC166

- C で勘違いしていたことに気づき、そのまま萎えてしまっていた...
- 緑になるまでは続けるが、それ以降は Leetcode のコンテストにでるのが良さそう
- D 問題
  - これは解く必要ないと思う
- E 問題
  - これは落ち着けばできた
  - やっぱり紙で考察したほうがよさそう...

## ABC 165

- C 問題
  - 全列挙っぽいことまで検討はついていた
    - コードがかなり面倒だと思って投げた
    - `combinations_with_replacement` とかいう便利メソッドがある...
    - https://qiita.com/junkls/items/10384950963056cc8e08
  - 単調増加の数列は、組み合わせと考えることが可能
- D 問題
  - 時間かかり過ぎな感じがするが、とりあえず解けた
  - `x = min(B − 1, N)` になるらしい

## ABC 164

- D 問題
  - 類題見つけられたが解けず...
    - https://drken1215.hatenablog.com/entry/2020/03/08/020200
  - 各桁の mod 計算を効率化する必要性があった
    - mod も桁がでかすぎると計算が遅くなる
    - https://azapen6.hatenablog.com/entry/2013/12/31/235453

## ABC 163

- D 問題
  - 解説の解法は一瞬思いついた
    - max-min で求められるわけないと思って退散してしまった
- E 問題
  - `Ai が大きいものから順に、左詰め、または、右詰めしていく` ところまでは考察できた
  - DP だった
  - dp[i][j] : 大きい方から i+j 個を左から i 個, 右から j 個詰めたときの最大のうれしさ
  - わかりやすい解説
    - https://drken1215.hatenablog.com/entry/2020/04/21/153400
    - 2 択問題は DP に帰着できることが多い

## Code Jam 2020

- ３問目解けなかった....
  - これは解けないとだめ...
  - np.array と idx を使ってソートしようとしたのが原因
    - なんかどこかで同じ間違えをした気がする
    - **ソートは np と idx を使って絶対にやらない!!**

## ABC 162

- 今回も D 問題はときたい
  - 方針はほとんど OK
  - 細かいところの計算量の見積もりが甘い
    - list の `in` は O(n)
    - set の `in` は O(1)

## ABC 161

- D 問題はときたい
  - 全探索 or Queue
  - Queue は、井上さんの考察が分かりやすかった
    - 実際書いたら一瞬
  - 全探索でも解いてみる
    - 再帰が今回はよかった (桁 DP でもできる)
    - n 桁の値から n+1 桁を求めるのを愚直にかけば OK
    - https://qiita.com/pinokions009/items/1e98252718eeeeb5c9ab

> LunLun Number を最初から順番に書いてみると
> 1, 2, 3, 4, 5, 6, 7, 8, 9
> 10, 11, 12,
> 21, 22, 23,
> …
> 87, 88, 89,
> 98, 99
> 100, 101,
> 110, 111, 112,
> 121, 122, 123,
> …
> という並びになるので, 1 桁の LunLun Number からはじめて, 後ろに条件に合う数を一桁ずつくっつけていけば良さそう, って感じで考えたよ

## ABC 160

- D 問題
  - 重みなしグラフの経路探索
    - DFS や BFS を使うのが一般的
    - http://yamagensakam.hatenablog.com/entry/2018/09/15/094504
  - 重みありグラフの経路探索
    - https://hfuji.hatenablog.jp/entry/2015/12/12/165413
    - 全ノードについて探索 : ワーシャルフロイド法 O(N^3)
    - ある特定ノードについて探索
      - ダイクストラ法 (エッジの重みが非負整数の時) : O(E \* logV)
      - ベルマン–フォード法 : O(V\*E)
  - Atcoder の計算量
    - 10^7 くらいが限度な感じ
  - 今回はいらなかった....
    - 最短経路は以下で簡単にもとまる... グラフに結構惑わされた感ある...
    - 求める最短距離は min{|j − i|, |X − i| + 1 + |j − Y |, |Y − i| + 1 + |j − X|}
    - 最近の D 問題は、数学的な問題が多い気がする
- E 問題
  - 考察問題だけど、落ち着けばかなり簡単だった...
  - これはとりたい...

## ABC 158

- D 問題
  - 文字列の先頭追加は遅い
  - データの追加や削除は Queue で管理しよう
    - **list は参照に強いが、データの追加にはそこまで強くない**

> Deque はどちらの側からも append と pop が可能で、スレッドセーフでメモリ効率がよく、どちらの方向からもおよそ O(1) のパフォーマンスで実行できます。list オブジェクトでも同様の操作を実現できますが、これは高速な固定長の操作に特化されており、内部のデータ表現形式のサイズと位置を両方変えるような pop(0) や insert(0, v) などの操作ではメモリ移動のために O(n) のコストを必要とします

## ABC 157

酷すぎた...

- D 問題
  - Union Find を使う問題
  - Union Find を使うのを思いつくのがキツそう
  - グラフ問題面白い

## ABC 156

急いで出したら、WA だらけだった...  
CLI 出た!! : https://qiita.com/sachaos/items/37bb4a32ff49ab4a3ac0

- B 問題
  - 10 進数 -> n 進数の変換
  - n で割っていき、その余りをつなげる
- D 問題
  - n_C_k の計算の高速化まではわかった
    - 2\*\*n - n_C_a - n_C_b - 1 まではいけた
    - そのまま使える
      - http://wakabame.hatenablog.com/entry/2017/09/21/211357
  - コンペ中の理解は諦めた...
- E 問題
  - 普通に考察問題だった
    - 数え上げの条件を正確に掴むのがポイント
    - xHy = x+y−1Cx−1 (忘れていた)
  - 数え上げさえ分かれば、あとは nCk や nHk を計算するだけ
  - https://img.atcoder.jp/abc156/editorial.pdf
  - https://drken1215.hatenablog.com/entry/2018/06/08/210000

## ABC 155

- D 問題
  - E より難しいらしい...
  - 類題がある : https://atcoder.jp/contests/abc149/tasks/abc149_e
    - https://tt-conpetitive.hatenablog.com/entry/2020/01/03/221433
    - 類題をみると 二分探索 + 累積和 の知識が必要という感じ
  - 解説読んでもピント来ないので今回はパス
- 前回に引き続き桁 dp とかいうやつ (E 問題)
  - 今回は制約がかなり大きいので再帰は通らない
    - メモ化してもきついものはきつい...
  - 解説の通りにすれば良い
    - https://qiita.com/c-yan/items/cb843ad3ba9a5009ad51#abc155e---payment
    - ちゃんと考察すればわかりそう

## ABC 154

- 入出力でハマった (B 問題)
  - 問題は改行コードだった
  - 標準入力の enter は改行になる
  - int 関数は改行文字を処理する
- 区間和は累積和で前処理すると早い (D 問題)
  - https://qiita.com/drken/items/56a6b68edef8fc605821
  - これは実務でも役立ちそう
- 桁 dp とかいうやつ (E 問題)
  - 制約がバカみたいにでかい (それ気になった...)
  - メモ化再帰で書いた方がわかりやすかった
    - 計算量はかかるし、メモリ効率も悪いからいつも使えるとは限らない
  - DP : 要は適切に場合分けできるか
  - https://maspypy.com/atcoder-%E5%8F%82%E5%8A%A0%E6%84%9F%E6%83%B3-2019-02-09abc-154#toc3
  - divmod 積極的に使っていきたい

## ABC153

- 計算量の感覚
  - https://qiita.com/drken/items/872ebc3a2b5caaa4a0d0
  - 実用上の多くの場面では、n=10^5 ~ 10^7 付近のデータを扱うケースが多い
  - O(n^2) なアルゴリズムを O(nlogn) に改善できるかどうかが鍵
- ソートの計算量 (B 問題)
  - https://qiita.com/drken/items/44c60118ab3703f7727f
  - ソートの最悪計算量の最小が O(nlogn)
  - マージソートとクイックソートが有名...?
- DP の計算 (D 問題)
  - https://qiita.com/drken/items/a5e6fe22863b7992efdb
  - 自分は典型的なハマり方をしたっぽい
  - http://wakabame.hatenablog.com/entry/2017/09/10/211428
  - DP はテーブルを埋めていくイメージ
  - 難しい...完全に慣れな予感がする
