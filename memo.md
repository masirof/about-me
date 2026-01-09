# 表示形式
- Hierarchical Square Packing
  - https://observablehq.com/%40esperanc/hierarchical-square-packing?utm_source=chatgpt.com
# ジャンル
- music
- book
- design
- shot
- avator
  - me
  - reference
- manga
- make
- anime
- good
- illustration

# 各サイトから画像取得
## soundcloud
- oEmbed
- https://soundcloud.com/oembed?format=json&url=
- https://soundcloud.com/oembed?format=json&url=https://soundcloud.com/sakuogt/longnightremix
- titleと画像を取得
  - title→カンマが入っているので、全部ダブルクオーテーションで囲む

## pinterest
- og:image
- スクレイピングでがんばる？

## youtube
- oEmbed
- https://www.youtube.com/oembed?format=json&url=
- https://www.youtube.com/oembed?format=json&url=https://www.youtube.com/watch?v=-xH_wmyWi5w

## twitter
- ❌oEmbed
- ❌スクレイピングは規約的によろしくない
- 無理そう
- https://publish.twitter.com/oembed?url=
- https://x.com/GuestSign/status/2007037493523399036?s=20
- https://publish.twitter.com/oembed?url=https://x.com/GuestSign/status/2007037493523399036

# items.csv AI用
- uv環境ある　/scripts/fetch_soundcloud.py を作成してほしい items.csvを読み取って、idカラムに入っているsoundcloud.comがついているurlをhttps://soundcloud.com/oembed?format=json&url={ここにurl}にしてoembed取得して、タイトルと画像を取得して、items.csvに書き込んでほしい　画像は/images/original/　idカラムは最大値+1したものを入れて　titleカラムはタイトルを入れて　imageカラムに画像を入れてほしい genre1にはmusicを入れて commentカラムに値があったら、そのままcommentカラムに値を入れて

# AI用
- d3-playground2.html にズームイン、ズームアウト、ドラッグ、d3-forceいらない、円ごとにカテゴリ分け、カテゴリ円の中に画像のモックを入れて、カテゴリ5つ、各画像モック20個 画像もっとズームインできるようにして　画像モックの大きさ512px*512px 画像モック同士の隙間を空けて、きれいに整列　画像モックを全部表示できる円カテゴリサイズにして　
- d3-playground2.html　Disjoint force-directed graphにして、画像モックを点ノードにしてみて画像モックの大きさ512px*512px　線は1つ　もうちょい線を太くして　もうちょいカテゴリごとにバラして
- d3-playground3.html　画像モックの大きさ512px*512px　を使ったグラフィックデザインっぽいグラフを作ってみて
- d3-playground4.html　画像モックの大きさ512px*512pxは絶対　をグリッド上に並べて　インタラクティブ操作　画像モック10個(カテゴリ)*200個 めっちゃズームアウト、画像一枚をmaxでズームインできるように　カテゴリは音楽、デザイン、アバター、漫画、作ったもの、写真、アニメで分けてほしい　カテゴリ分けする方法は任せる

- d3-playground5.html　画像モックの大きさ512px*512pxは絶対　をグリッド上に並べて　インタラクティブ操作　画像モック7個(カテゴリ)*20個 めっちゃズームアウト、画像一枚をmaxでズームインできるように　カテゴリは音楽、デザイン、アバター、漫画、作ったもの、写真、アニメで分けてほしい　カテゴリ分けする方法は任せる 添付画像みたいに雪の結晶みたいな形に画像をカテゴリ分けできる？ サムネは3d的に斜めで、マウスを乗せると拡大画像が中央に表示されるみたいなアニメーション　マウスを動かすと、瞬間的に拡大画像が変わるやつ　マウスを画像から外すと拡大画像は表示されない　マウスをサムネにおいてもサムネが消えないように

- d3-playground5.htmlをd3-playground6.htmlにコピーしたい　画像モックの大きさ512px*512pxは絶対　グリッド上に並べて　インタラクティブ操作　画像モック7個(カテゴリ)*20個 めっちゃズームアウト、画像一枚をmaxでズームインできるように　カテゴリは音楽、デザイン、アバター、漫画、作ったもの、写真、アニメで分けてほしい　カテゴリ分けする方法は任せる 添付画像みたいに雪の結晶みたいな形に画像をカテゴリ分けできる？ サムネは3d的に斜めで、マウスを乗せると拡大画像が中央に表示されるみたいなアニメーション　マウスを動かすと、瞬間的に拡大画像が変わるやつ　マウスを画像から外すと拡大画像は表示されない　マウスをサムネにおいてもサムネが消えないように items.csvを読み込んでid1~6を参照→imageカラムの画像ファイル名を表示したい(images/original/写真ファイル) 読み込めた画像は、拡大画像も、画像ファイル自体の解像度を表示させたい ジャンルはitems.csvのgenre1とgenre2を動的に使用してジャンル分けたい(items.csv以外のジャンルは使わないで)　genre1が親でgenre2が子　画像ファイルがないところはモックにしてね items.csvのカテゴリ+モックの数で子カテゴリを作成し、合計20枚になるようにして

- 拡大プレビューは画像の元の解像度にして、ディスプレイの全画面の70%の大きさにして

- 各カテゴリを星雲みたいにして 親カテゴリの中に子カテゴリがある感じにして

- d3-playground7.html　画像モックの大きさ512px*512pxは絶対　画像の間はスペースを開けたい　genre1が親でgenre2が子　画像ファイルがないところはモックにしてね items.csvのカテゴリ+モックの数で子カテゴリを作成し、合計20枚になるようにして　インタラクティブ操作　各子カテゴリに画像20枚　親カテゴリは音楽、デザイン、アバター、漫画、作ったもの、写真、アニメ　子カテゴリは適当で　Zoomable circle packingにしたい(クリックで拡大じゃなくて、スクロールで拡大)

- items.csvを更新したから、d3-playgroud7.htmlを更新して