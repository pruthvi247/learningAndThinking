Adding css
- inline `< tag style="css" />`
- internal `< style > css </ style >`
- External `<link rel="stylesheet" href="style.css"/>`


---------------------
## CSS Selectors [](https://www.w3schools.com/css/css_selectors.asp)

CSS selectors are used to "find" (or select) the HTML elements you want to style.

We can divide CSS selectors into five categories:

- Simple selectors (select elements based on name, id, class)
- [Combinator selectors](https://www.w3schools.com/css/css_combinators.asp) (select elements based on a specific relationship between them)
- [Pseudo-class selectors](https://www.w3schools.com/css/css_pseudo_classes.asp) (select elements based on a certain state)
- [Pseudo-elements selectors](https://www.w3schools.com/css/css_pseudo_elements.asp) (select and style a part of an element)
- [Attribute selectors](https://www.w3schools.com/css/css_attribute_selectors.asp) (select elements based on an attribute or attribute value)

------------------------------------------


# Css selectors
```html
<!DOCTYPE html>
<html>
<head>
<style>
p {
  text-align: center;
  color: blue;
} 
</style>
</head>
<body>

<p>Every paragraph will be affected by the style.</p>
<p id="para1">Me too!</p>
<p>And me!</p>

</body>
</html>
```

> above code changes color to blue for all < p>  tags

## Id selector
```html
<!DOCTYPE html>
<html>
<head>
<style>
#para1 {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<p id="para1">Hello World!</p>
<p>This paragraph is not affected by the style.</p>

</body>
</html>


```

The id of an element is unique within a page, so the id selector is used to select one unique element!

To select an element with a specific id, write a hash (#) character, followed by the id of the element.

## Class selector
```html
<!DOCTYPE html>
<html>
<head>
<style>
.center {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<h1 class="center">Red and center-aligned heading</h1>
<p class="Large">Red and Large center-aligned paragraph.</p> 

</body>
</html>

```
> HTML elements can also refer to more than one class.

In this example the < p> element will be styled according to class="center" and to class="large": 
```html
<p class="center large">This paragraph refers to two classes.</p>
```

## Attribute selector
```html
<!DOCTYPE html>
<html>
<head>
<style>
a[target] {
  background-color: yellow;
}
a[target="_top"] {
  background-color: green;
}
</style>
</head>
<body>

<h2>CSS [attribute] Selector</h2>
<p>The links with a target attribute gets a yellow background:</p>

<a href="https://www.w3schools.com">w3schools.com</a>
<a href="http://www.disney.com" target="_blank">disney.com</a>
<a href="http://www.wikipedia.org" target="_top">wikipedia.org</a>

</body>
</html>
```


### CSS [attribute~="value"] Selector

The `[attribute~="value"]` selector is used to select elements with an attribute value containing a specified word.

The following example selects all elements with a title attribute that contains a space-separated list of words, one of which is "flower":


```html
<!DOCTYPE html>
<html>
<head>
<style>
[title~="flower"] {
  border: 5px solid yellow;
}
</style>
</head>
<body>

<h2>CSS [attribute~="value"] Selector</h2>
<p>All images with the title attribute containing the word "flower" get a yellow border.</p>

<img src="klematis.jpg" title="klematis flower" width="150" height="113">
<img src="img_flwr.gif" title="flower" width="224" height="162">
<img src="img_tree.gif" title="tree" width="200" height="358">

</body>
</html>
```

### CSS [attribute|="value"] Selector

The `[attribute|="value"]` selector is used to select elements with the specified attribute, whose value can be exactly the specified value, or the specified value followed by a hyphen (-).

**Note:** The value has to be a whole word, either alone, like class="top", or followed by a hyphen( - ), like class="top-text".

### CSS [attribute^="value"] Selector

The `[attribute^="value"]` selector is used to select elements with the specified attribute, whose value starts with the specified value.

The following example selects all elements with a class attribute value that starts with "top":

**Note:** The value does not have to be a whole word!

### CSS [attribute$="value"] Selector

The `[attribute$="value"]` selector is used to select elements whose attribute value ends with a specified value.

The following example selects all elements with a class attribute value that ends with "test":

**Note:** The value does not have to be a whole word!

### CSS [attribute*="value"] Selector

The `[attribute*="value"]` selector is used to select elements whose attribute value contains a specified value.

The following example selects all elements with a class attribute value that contains "te":

**Note:** The value does not have to be a whole word!


## Universal Selector
The universal selector (*) selects all HTML elements on the page.
```css
* {  
text-align: center;  
  color: blue;
  }
```
## ::before Selector
The `::before` selector inserts something before the content of each selected element(s).
eg: Insert content before every < p > element's content, and style the inserted content:
```html
<!DOCTYPE html>
<html>
<head>
<style>
p::before { 
  content: "Read this -";
  background-color: yellow;
  color: red;
  font-weight: bold;
}
</style>
</head>
<body>
<h1>Demo of the ::before selector</h1>
<p>My name is Donald</p>
<p>I live in Ducksburg</p>
</body>
</html>
```
--------------------------
Below code is from plugin : https://github.com/tnichols217/obsidian-columns

```````col
``````col-md
flexGrow=1
===
> [!info] Callouts
>  Stuff inside the callout
>  More stuff inside.
>> [!ERROR] Error description
>>  Nested callout
>>  `````col-md
>>  - example MD code
>>  - more stuff
>>  `````
``````

``````col-md
flexGrow=2.5
===
# Text annotation example:

`````col
````col-md
flexGrow=1
===
1. Function name **a** should be more descriptive

2. Remove **if/else** by using **||**
````

````col-md
flexGrow=2
===
```js
function a(word) {
	if (word != null) {
		console.log(word);
	} else {
		console.log("a");
	}
}
let msg = "Hello, world!";
console.log(msg)
```
````
`````
``````
```````

# [css-selectors-source](https://css-tricks.com/how-css-selectors-work/)


### ID Selector

`````col
````col-md
```css
#happy-cake {

}
```
````
````col-md
```html
<!-- WILL match -->
<div id="happy-cake"></div>

<!-- WILL match -->
<aside id="happy-cake"></aside>

<!-- Will NOT match -->
<div id="sad-cake">Wrong ID!</div>

<!-- Will NOT match -->
<div class="happy-cake">That's not an ID!</div>
```
````
`````
ID selectors are the most **powerful** type of selector in terms of [CSS specificity](https://css-tricks.com/specifics-on-css-specificity/). Meaning that they _beat out_ other types of selectors and the styles defined within _win_. That sounds good, but that’s typically [considered bad](https://css-tricks.com/a-line-in-the-sand/), because it’s nice to have lower-specificity selectors that are easier to override when needed.

### Class Selector
`````col
````col-md
```css
.module {

}
```
````
````col-md
```html
<!-- WILL match -->
<div class="module"></div>

<!-- WILL match -->
<aside class="country module iceland"></aside>

<!-- Will NOT match -->
<div class=".module">The dot is for CSS, not HTML</div>

<!-- Will NOT match -->
<div class="bigmodule">Wrong class</div>
```
````
`````
Class selectors are your friend. They are probably the most useful and versatile selectors out there. In part because they are well supported in all browsers. In part because you can add multiple classes (just separated by a space) on HTML elements. In part because there are JavaScript things you can do specifically for manipulating classes.

### Tag Selector
`````col
````col-md
```css
h2 {

}
```
````
````col-md
```html
<!-- WILL match -->
<h2>Hi, Mom</h2>

<main>
  <div>
     <!-- WILL match -->
     <h2>Anywhere</h2>
  </div>
</main>

<!-- Will NOT match -->
<div class="h2">Wrong tag, can't trick it</div>

<!-- Will NOT match -->
<h2class="yolo">Make sure that tag has a space after it!</h2>
```
````
`````
Tag selectors are at their most useful when changing properties that are unique to that HTML element. Like setting the `list-style` on a `<ul>` or `tab-size` on a `<pre>`. Also in [reset stylesheets](https://css-tricks.com/reboot-resets-reasoning/) where you are specifically trying to _un_set styles that browsers apply to certain elements.

Don’t rely on them too much though. It’s typically more useful to have a class define styling that you can use on _any_ HTML element.
>A **reset stylesheet** (or **CSS reset**) is a collection of [CSS rules](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Cascading Style Sheets") used to clear the browser's default formatting of [HTML](https://en.wikipedia.org/wiki/HTML "HTML") elements, removing potential inconsistencies between different browsers. It also prevents developers from unknowingly relying on the browser default styling and force them to be explicit about the styling they want to apply on the page.

### Attribute Selector
`````col
````col-md
```css
[data-modal="open"] {

}
```
````
````col-md
```html
<!-- WILL match -->
<div data-modal="open"></div>

<!-- WILL match -->
<aside class='closed' data-modal='open'></aside>

<!-- Will NOT match -->
<div data-modal="false">Wrong value</div>

<!-- Will NOT match -->
<div data-modal>No value</div>

<!-- Will NOT match -->
<div data-modal-open>Wrong attribute</div>
```
````
`````
You might argue that [attribute selectors](https://css-tricks.com/attribute-selectors/) are even more useful than classes because they have the same [specificity value](https://css-tricks.com/specifics-on-css-specificity/), but can be any attribute not just `class`, _plus_ they can have a value you can select by.

Hardly an issue anymore, but attribute selectors aren’t supported in IE 6.

### Positional Selectors
`````col
````col-md
```css
:nth-child(2) {

}
```
````
````col-md
```html
<ul>
  <li>nope</li>
  <!-- WILL match -->
  <li>yep, I'm #2</li>
  <li>nope</li>
</ul>
```
````
`````
There are several different positional selectors beyond [:nth-child](https://css-tricks.com/how-nth-child-works/). Using simple expressions (like `3n` = “every third”) you can select elements based on their position in the HTML. You can [play with that idea here](https://css-tricks.com/examples/nth-child-tester/) or check out [some useful recipes](https://css-tricks.com/useful-nth-child-recipies/).

### Pseudo Selectors
`````col
````col-md
```css
:empty { }
```
````
````col-md
```html
<!-- WILL match -->
<div></div>

<!-- WILL match -->
<aside data-blah><!-- nothin' --></aside>

<!-- Will NOT match -->
<div> </div>

<!-- Will NOT match -->
<div>
</div>
```
````
`````
`:empty` is one of many [pseudo selectors](https://css-tricks.com/pseudo-class-selectors/), which you can recognize by the colon (:) in them. They typically represent something that you couldn’t know by just the element and attributes alone.

Note that these are slightly different than [pseudo elements](https://css-tricks.com/pseudo-element-roundup/), which you can recognize by the double colon (::). They are responsible for adding things to the page by the things they select.

#### More Leveling Up

Selectors can be combined together. For instance:
```css
.module.news {  
  /* Selects elements with BOTH of those classes */
}
#site-footer::after {
  /* Adds content after an element with that ID */
}
section[data-open] {
  /* Selects only section elements if they have this attribute */
}
```
There are also [selector combinators](https://css-tricks.com/child-and-sibling-selectors/) like `~` and `+` and `>` that affect selectors, like:
```css
.module > h2 {
  /* Select h2 elements that are direct children of an element with that class */
} 
h2 + p {
  /* Select p elements that are directly following an h2 element */
}
li ~ li {
  /* Select li elements that are siblings (and following) another li element. */
}
```
`+` combinator is similar to the sibling combinator(~). The difference is that while the sibling combinator matches all siblings that come AFTER an element, the adjacent combinator matches only the **IMMEDIATE** sibling that comes after an element.
#### > vs. Space

Consider the two scenarios `div > span { }` vs. `div span { }`

Here, the   (space) selects all the all the `<span>` elements inside `<div>` element even if they are nested inside more than one element. The `>` selects all the children of `<div>` element but if they are not inside another element.
`A > B` will only select B that are direct children to A (that is, there are no other elements inbetween).

`A B` will select any B that are inside A, even if there are other elements between them.















