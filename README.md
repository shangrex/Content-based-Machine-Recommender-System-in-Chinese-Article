# 基於內容之機器推薦中文文章系統(Content-based Machine Recommender System in Chinese article)

## 問題定義
現代的小說推薦系統以及詩詞推薦系統都是利用collaborative-filter來做推薦，或是簡單的運用類型來做基礎的推薦，致使使用者無法得知自己想要閱讀的文章。此系統解決只運用content-based來推薦傳統中華文學，如詩詞和小說，可在不受別人喜好影響下推薦文章，並且在推薦的同時，可以快速了解此篇文章的基礎資訊，提供人以內容為導向閱讀自己喜歡的文章。
## 功能介紹
* 推薦文章：兩種推薦方法，一種依循關鍵字和作者寫作風格推薦詩詞和小說，第二種為依尋關鍵字回傳詩詞和小說類別。
* 產生文章：輸入狀況產生詩詞。
* 文章概覽：可查詢和瀏覽詩詞的作者、風格、題目、年代、部份內容、ＦＤＡ產物和文字內容難度。
* 圖片支援: 在查詢階段，透過關鍵字提取找到相對應的圖片做支援，並加入文字雲讓人可以快速了解詩詞或小說內容。
* 建立自己的Profile，來推薦不同類型的文章。
* 與詩詞對話


## 功能介紹
### home page
![](https://i.imgur.com/O7cIQW5.jpg)
介紹POEM資料集
![](https://i.imgur.com/CXxw657.png)
介紹MINGYAN資料集
使用KMEANS把資聊集分成6個cluster，並隨機抽出兩個展示
![](https://i.imgur.com/lzdCAs8.png)
![](https://i.imgur.com/UKzQKL0.png)
介紹NOVEL資料集
![](https://i.imgur.com/gk84dJ2.png)

### POEM
搜索詩詞，存作者和題目和內容三個方向去搜索，利用LDA去尋找主題下的關鍵字，顯示在tags上
![](https://i.imgur.com/wvPjju4.png)
![](https://i.imgur.com/EqX7bHr.png)
輸入詩詞，利用BERT做分類任務，預測和哪個左者風格最相近
![](https://i.imgur.com/5OkackP.png)
輸入詩詞，利用word vector計算，選出最相近的幾首詩詞
![](https://i.imgur.com/bSuaAU1.png)
![](https://i.imgur.com/aXLaSj4.png)

### MINGYAN
輸入句子，利用word vector計算，選出最相近的幾句名言
![](https://i.imgur.com/FOv72Hk.png)
輸入句子，利用word vector計算，選出最相近的幾句名研的書名
![](https://i.imgur.com/Sjn9vfZ.png)

### NOVEL
輸入句子，利用word vector計算，選出小說書名
![](https://i.imgur.com/D0YeIJj.png)
輸入句子，利用word vector計算，利用小說內容選出小說作者
![](https://i.imgur.com/qSlCDxb.png)

