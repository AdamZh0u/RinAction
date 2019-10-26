# R in Action

[toc]

## Day 0

### Markdown 语法回顾

#### Block Elements

``` markdown
Paragraph : return
Line breaks : shift+return/two spaces/ <br/>
Headers : #
Blockquotes : >
Unordered List : * / + / -
Ordered List : 1.
Task List : - [ ]
Code Blocks : ```
Math Blocks : $$
Tables : | Columns1 | Columns2 |
Footnotes : [^1]   [^1]:
Horizontal Rules : * * * / ---
Table of Contents : [toc]
YAML Front Matter : --- (at top) 
```

#### Span Elements

``` markdown
Inline Links : []() / <a href="http://example.net/">This link</a>
Internal Links : [](# title)
Reference Links : [][1]  [1]: 
URLs : <zhouzz400@gmail.com>
Images : ![caption](path)
Emphasis : *demo* / _demo_
Strong ： **demo**
Code : `code`
Strikethrough : ~ ~demo~ ~
Underlines : <u> under </u>
Emoji : :smile:
Subscript and Supscript : ~ / ^
Highlight : == demo ==
```

---

### 几点拓展与注意

* :red_circle: 注意enter是下一段，shift+enter是换行，有差别

* :red_circle:无序列表按tab到下一级，shift+tab到上一级

* 编辑网页的语言--html，也是一种标记语言（看看淘宝主页）。markdown中兼容html语言。复制下面两段网页源码到typora中看看！

    ``` html
    <h2>HTML Buttons</h2>    <!- h2 相当于markdown中的## ->
    <p>HTML buttons are defined with the button tag:</p>
    <button>Click me</button>
    ```

    ```html
    <iframe height='265' scrolling='no' title='Fancy Animated SVG Menu' src='http://codepen.io/jeangontijo/embed/OxVywj/?height=265&theme-id=0&default-tab=css,result&embed-version=2' frameborder='no' allowtransparency='true' allowfullscreen='true' style='width: 100%;'></iframe>
    ```

*  在zotero中做笔记时，编辑邮件时，都可以使用markdown。

* 几个用markdown生成的网页。

    * [使用markdown制作网页电子书](https://wizardforcel.gitbooks.io/markdown-simple-world/4.html)
    * [github的readme](https://github.com/AdamCh0u/RinAction)
    * [使用markdown制作网页](https://jekyllcn.com/)

* 使用markdown放小视频

    * <video src="./14966982-1-48.mp4"></video>

    * 这么快就学完了一种语言，我真的真的很不错！:cowboy_hat_face:
    

****

### 安装R与Rstudio

略

