css![[Pasted image 20231103153542.png]]

# Pseudo classes
A Pseudo class in CSS is used to define the special state of an element. It can be combined with a CSS selector to add an effect to existing elements based on their states. For Example, changing the style of an element when the user hovers over it, or when a link is visited. All of these can be done using Pseudo Classes in CSS.
syntax
```css
selector:pseudo-class {
property: value;
}
```
Pseudo-classes let you apply a style to an element not only in relation to the content of the document tree, but also in relation to external factors like the history of the navigator ([`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/:visited), for example), the status of its content (like [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/:checked) on certain form elements), or the position of the mouse (like [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/:hover), which lets you know if the mouse is over an element or not).
> **Note:** In contrast to pseudo-classes, [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements) can be used to style a _specific part_ of an element.

# Pseudo-elements
A CSS **pseudo-element** is a keyword added to a selector that lets you style a specific part of the selected element(s).

**pseudo-element** are essential elements doesn't exist in html but still we can select in css and modify
```css
selector::pseudo-element {
  property: value;
}
```
For example, [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/::first-line) can be used to change the font of the first line of a paragraph.
```css
/* The first line of every <p> element. */
p::first-line {
  color: blue;
  text-transform: uppercase;
}
```
Double colons (`::`) are used for pseudo-elements. This distinguishes pseudo-elements from [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) that use single colon (`:`) in their notation.

![[Pasted image 20231104153351.png]]

# CSS Boxmodel
![[Pasted image 20231104165617.png]]
 ![[Pasted image 20231104165801.png]]
`Final element width = left border + left padding +width + right padding + right border`

`Final element height = top border + top padding+height + bottom padding + bottom border`

# Types of boxes
## Box level elements
👉 Elements are formatted visually as blocks
👉 Elements occupy 100% of parent element’s width,
no matter the content
👉 Elements are stacked vertically by default, one
after another
👉 The box-model applies as showed earlier

**Default elements:**
`body, main, header,footer, section, nav, aside, div, h1-h6,p, ul, ol, li, etc.`

**With CSS:**
`display: block`
## Inline Elements

👉 Occupies only the space necessary for its content
👉 Causes no line-breaks after or before the element
👉 Box model applies in a different way: heights and
widths do not apply
👉 Paddings and margins are applied only horizontally (left and right)

**Default elements:** 
`a, img, strong, em,button, etc.``

**With CSS:**
`display: inline`

## Inline-Block Boxes

👉 Looks like inline from the outside, behaves like block level on the inside
👉 Occupies only content's space
👉 Causes no line-breaks
👉 Box-model applies as showed
👉 `display: inline-block`

![[Pasted image 20231113104512.png]]

# Positioning
[free-code-camp-blog](https://www.freecodecamp.org/news/css-positioning-position-absolute-and-relative/)

**Position property** takes in five values: `static`, `relative`, `absolute`, `fixed`, and `sticky`.
In this article, we'll focus on the `relative` and `absolute` values.

To view position in chrome dev tools:
Select the `Computed` tab and from there either scroll down to the `position` element or in the `filter` search box, type in `position`.

By default, the `position` property for all HTML elements in CSS is set to `static`. This means that if you don't specify any other `position` value or if the `position` property is not declared explicitly, it'll be `static`.
`position: relative` works the same way as `position: static;`, but it lets you change an element's position.

But just writing this CSS rule alone will not change anything.

To modify the position, you'll need to apply the `top`, `bottom`, `right`, and `left` properties and in that way specify where and how much you want to move the element.
```css
.one {
  background-color: powderblue;
  position: relative;
  right: 50px;
}
```
`position: relative;` changes the position of the element _relative_ to the parent element and relative to itself and where it would usually be in the regular document flow of the page. This means that it's relative to its original position within the parent element.

Using these offsets and `position: relative`, you can also change the order in which elements appear on the page.

The second square can appear on top of the first one:

```css
.one {
  background-color: powderblue;
  position: relative;
  top: 150px;
}

.two {
  background-color: royalblue;
  position: relative;
  bottom: 120px;
}
```

**Obsolute postion**
```css
.one {
  background-color: powderblue;
  position: absolute;
  top: 50px;
  left: 0;
}
```
Well now the square has completely abandoned it's parent.

Absolute-positioned elements are completely taken out of the regular flow of the web page.

They are not positioned based on their usual place in the document flow, but based on the position of their ancestor.

In the example above, the absolutely positioned square is inside a statically positioned parent.

This means it will be positioned relative to the whole page itself, which means relative to the `<html>` element – the root of the page.

The coordinates, `top: 50px;` and `left: 0;`, are therefore based on the whole page.
If you want the coordinates to be applied to its parent element, you need to relatively position the parent element by updating `.parent` while keeping `.one` the same:
```css
.parent {
  width: 500px;
  border: 1px solid red;
  margin: auto;
  text-align: center;
  position: relative;
}

.one {
  background-color: powderblue;
  position: absolute;
  top: 50px;
  left: 0;
}
```
Absolute positioning takes elements out of the regular document flow while also affecting the layout of the other elements on the page.
## Understanding Absolute Positioning
![[Pasted image 20231104191233.png]]

# CSS Combinator Selectors
A combinator is something that explains the relationship between the selectors.
There are four different combinators in CSS:

- descendant selector (space)
- child selector (>)
- adjacent sibling selector (+)
- general sibling selector (~)
- |Selector|Example|Example description|

|Selector|Example|Example description|
|---|---|---|
|[_element element_](https://www.w3schools.com/cssref/sel_element_element.asp)|div p|Selects all ``<p> ``elements inside ``<div>`` elements|
|[_element>element_](https://www.w3schools.com/cssref/sel_element_gt.asp)|div > p|Selects all ``<p>`` elements where the parent is a ``<div>`` element|
|[_element+element_](https://www.w3schools.com/cssref/sel_element_pluss.asp)|div + p|Selects the first ``<p>`` element that are placed immediately after ``<div>`` elements|
|[_element1~element2_](https://www.w3schools.com/cssref/sel_gen_sibling.asp)|p ~ ul|Selects every ``<ul>`` element that are preceded by a ``<p>`` element|

## & (Ampersend)
Source : https://www.reddit.com/r/css/comments/szntm4/what_this_does_in_css/?rdt=56511

in SCSS or .LESS, the & and > together really just cascade, like you see in the other response. This
```css
p {
    & > .bold-text {font-weight: bold;}
    & > .white-text {color: #FFFFFF;}
}
```
Becomes this:
```css
p > .bold-text {font-weight: bold;}
p > .white-text {color: #FFFFFF;}
```

`& > * { margin: 105px; } I`
Basically it says everything (* references all) directly under the parent container (& references the parent, > references directly under) should have a margin on all sides of 105px.

In Sass and Less, the `&` is a reference to the parent selector

A nested `&` selects the parent element in both SASS and LESS. It's not just for pseudo elements, it can be used with any kind of selector.
```css
h1 {
    &.class {

    }
}
```
is equivalent to
```css
h1.class {
}
```

