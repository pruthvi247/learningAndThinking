[udermy-course](https://rakuten.udemy.com/course/design-and-develop-a-killer-website-with-html5-and-css3/learn/lecture/27511932#overview)
[Git-Code](https://github.com/jonasschmedtmann/html-css-course)
# SuperScript&Subscript


`<sup>`

The < sup > element is used  
to contain characters that should be superscript such  
as the suffixes of dates or mathematical concepts like raising a number to a power such as 22.

`<sub>`

The < sub > element is used to contain characters that should be subscript. It is commonly used with foot notes or chemical formulas such as H20.

`Example`

<p>On the 4<sup>th</sup> of September you will learn about E=MC<sup>2</sup>.</p>

<p>The amount of CO<sub>2</sub> in the atmosphere grew by 2ppm in 2009<sub>1</sub>.</p>

<br />

As you have already seen, the browser will automatically show each new paragraph or heading on a new line. But if you wanted to add a line break inside the middle of a paragraph you can use the line break tag <br />.

<hr />

To create a break between themes — such as a change of topic in a book or a new scene  
in a play — you can add a horizontal rule between sections using the <hr /> tag.

There are a few elements that do not have any words between an opening and closing tag. They are known as empty elements and they are written differently.

# semantic Markup
There are some text elements that are not intended to affect the structure of your web pages, but they do add extra information to the pages — they are known as semantic markup.

``<strong>``

The use of the ``<strong>``element indicates that its content has strong importance. For example, the words contained in this element might be said with strong emphasis.

By default, browsers will show the contents of a ``<strong> `` element in bold.
`example`
<p><strong>Beware:</strong> Pickpockets operate in this area.</p><p>This toy has many small pieces and is <strong>not suitable for children under five years old. </strong></p>
``<em>``

The ``<em>`` element indicates emphasis that subtly changes the meaning of a sentence.

By default browsers will show the contents of an ``<em>`` element in italic.
`example`
<p>I <em>think</em> Ivy was the first.</p>
<p>I think <em>Ivy</em> was the first.</p> <p>I think Ivy was the <em>first</em>.</p>

# Quotations
``<blockquote>``

The ``<blockquote>`` element is used for longer quotes that take up an entire paragraph. Note how the ``<p>`` element is still used inside the ``<blockquote>`` element.

Browsers tend to indent the contents of the ``<blockquote>`` element, however you should not use this element just to indent a piece of text — rather you should achieve this effect using CSS.
``<q>``

The ``<q>`` element is used for shorter quotes that sit within  
a paragraph. Browsers are supposed to put quotes around the ``<q> `` element, however Internet Explorer does not — therefore many people avoid using the ``<q>`` element.

Both elements may use the cite attribute to indicate where the quote is from. Its value should be a URL that will have more information about the source of the quotation.

`Example`
<blockquote cite="http://en.wikipedia.org/wiki/ Winnie-the-Pooh">  
<p>Did you ever stop to think, and forget to start

again?</p> </blockquote>

<p>As A.A. Milne said, <q>Some people talk to animals. Not many listen though. That's the problem.</q></p>

# \<head\>
Contents of `head` element are not displayed in browser 

# Semantic html
In programming, **Semantics** refers to the _meaning_ of a piece of code
In HTML, for example, the [h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) element is a semantic element, which gives the text it wraps around the role (or meaning) of "a top level heading on your page."
Non-semantic elements are used to create structure and presentation for web pages. They don't provide any information about the content of the web page. They are used to define sections of a web page and apply styles to the content.

Not all elements are semantic for eg `<strong>` is not semantic element because it just bold the text 
Semantic elements, such as ``<header>``, ``<nav>``, ``<section>``, and ``<footer>``, are used to define the structure of a web page and give meaning to the content. Non-semantic elements, such as ``<div>`` and ``<span>``, are used for layout and formatting purposes only.

### List of new semantic elements

The semantic elements added in HTML5 are:

- `<article>`
- `<aside>`
- `<details>`
- `<figcaption>`
- `<figure>`
- `<footer>`
- `<header>`
- `<main>`
- `<mark>`
- `<nav>`
- `<section>`
- `<summary>`
- `<time>`
Elements such as `<header>`, `<nav>`, `<section>`, `<article>`, `<aside>`, and `<footer>` act more or less like `<div>` elements. They group other elements together into page sections. However where a `<div>` tag could contain any type of information, it is easy to identify what sort of information would go in a semantic `<header>` region.
## HTML Entity List: 

Some characters are reserved in HTML and they have special meaning when used in HTML document. For example, you cannot use the greater than and less than signs or angle brackets within your HTML text because the browser will treat them differently and will try to draw a meaning related to HTML tag.
https://www.freeformatter.com/html-entities.html