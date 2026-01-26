3 ways of building layouts with css
- Float Layouts
- FlexBox
- Css Grid
![[Pasted image 20231105142217.png]]
[blog](https://blog.logrocket.com/deep-dive-css-float-property/)
Use `float` when you want to pull an element to the side of a containing element while allowing other content to freely flow around it. There aren’t any other CSS methods for accomplishing this, so don’t be afraid to use it!

The valid values for `float` are a single keyword from the following list:

- `left`: positions the element on the left side of its containing block
- `right`: positions the element on the right side of its containing block
- `none`: does not float the element
- `inline-start` : positions the element on the first inline side of its containing block; this is the left side with left-to-right scripts and the right side with right-to-left scripts
- `inline-end`: positions the element on the last inline side of its containing block; this is the right side with left-to-right scripts and the left side with right-to-left scripts

```css
 img {
    float: inline-start;
    margin-inline-end: 4px;
}
```
`code pen example:` https://codepen.io/robatronbobby/pen/vYROzBo

## Opting out of CSS floated elements with `clear`

The CSS `[clear](https://developer.mozilla.org/en-US/docs/Web/CSS/clear)` property is a complementary property to `float`. You can use it when you want some elements to be free from the influence of floated elements. You can set an element to be “cleared” on one side, or both sides. The cleared element will be moved below any floating elements that precede it.
The `clear` property has a similar set of values as `float`:

- `none`: the element is not moved down to clear past floating elements
- `left`: the element is moved down to clear past left floats
- `right`: the element is moved down to clear past right floats
- `both`: the element is moved down to clear past both left and right floats
- `inline-start`: the element is moved down to clear floats on the start side of its containing block; that is, the left floats on left-to-right scripts and the right floats on right-to-left scripts
- `inline-end`: the element is moved down to clear floats on the end side of its containing block; that is, the right floats on left-to-right scripts and the left floats on right-to-left scripts
To fix this particular case, we can add `clear: inline-end;` or `clear: right;` to the `footer`.

If we want to prevent this from occurring completely, we can use `clear:both;` instead.
```css
.no-floats {
    clear:both;
}
```
`code pen example`: https://codepen.io/robatronbobby/pen/BarjmPE
### Getting creative with `shape-outside`

 let’s say we have an SVG image that has a single `path` that is a red star with a transparent background. Here’s what using `shape-outside` with this image looks like.
 ```css
 .star {
    width: 250px;
    float: left;
    shape-outside: url("https://upload.wikimedia.org/wikipedia/commons/3/34/Red_star.svg");
    shape-margin: 6px;
}
```
There is also a [shape-margin](https://developer.mozilla.org/en-US/docs/Web/CSS/shape-margin) property that enables us to adjust the margin around the shape.
We can provide a [\<basic-shape>](https://developer.mozilla.org/en-US/docs/Web/CSS/basic-shape) as the value to the `shape-outside` property with the following functions: [inset()](https://developer.mozilla.org/en-US/docs/Web/CSS/basic-shape/inset)(), [circle()](https://developer.mozilla.org/en-US/docs/Web/CSS/basic-shape/circle), [ellipse()](https://developer.mozilla.org/en-US/docs/Web/CSS/basic-shape/ellipse), [polygon()](https://developer.mozilla.org/en-US/docs/Web/CSS/basic-shape/polygon), or [path()](https://developer.mozilla.org/en-US/docs/Web/CSS/path). These are defined in the [CSS Shapes Module Level 1 specification](https://www.w3.org/TR/css-shapes/). If you’ve ever used the `clip-path` property, then you’ve also used these functions.

Let’s say we want to create a `div` that is a grey circle and have the text flow around it, like in the image below. We can create this by using `float` together with `shape-outside: circle()`.
Here’s the CSS to create the grey circle with the flowing text:
```css
.circle {
        border-radius: 50%;
        height: 200px;
        width: 200px;
        background-color: grey;
        float: right;
        shape-outside: circle();
}
```
`code pen example:`https://codepen.io/robatronbobby/pen/XWEWzGO

For more examples and deep dive follow Blog : https://blog.logrocket.com/deep-dive-css-float-property/

![[Pasted image 20231105152213.png]]

# Flex box

DeepDive blogs:
- [freecode-camp](https://www.freecodecamp.org/news/learn-flexbox-build-5-layouts/)
- [medium-flexbox-coolkids](https://medium.com/@emmabostian/css3-flexbox-the-cool-kid-on-the-block-cca8141cbee9)
- [marina-ferreira.github.io](https://marina-ferreira.github.io/tutorials/css/flexbox/)
--------------------SOB---------------------------
[freecode-camp-css-flexbox](https://www.freecodecamp.org/news/css-flexbox-tutorial-with-cheatsheet/)

The Flexbox model allows us to **layout the content** of our website. Not only that, it helps us create the structures needed for creating **responsive websites** for multiple devices.

## Flexbox Architecture

Depending on the flex-direction property, the layout position changes between rows and columns.

![[Pasted image 20231105173908.png]]
## Flexbox Chart

This chart contains every possible property and value you can use when you're working with Flexbox. You can reference it while doing your projects and experiment with different values.
![[Pasted image 20231105174010.png]]
## flex-direction property

This property allows us to set the direction and orientation in which our flex-items should be distributed inside the flex-container.
![[Pasted image 20231105175603.png]]
![[Pasted image 20231105175611.png]]
## Justify-content property

This property arranges flex-items along the **MAIN AXIS** inside the flex-container.
![[Pasted image 20231105175729.png]]
![[Pasted image 20231105175741.png]]
## align-content property

This property arranges flex-items along the **CROSS AXIS** inside the flex-container. This is similar to **justify-content**.
!!!Note: that without the **flex-wrap** property, this property doesn't work. Here's a demo:
![[Pasted image 20231105180123.png]]

## align-items property
This property distributes Flex-items along the **Cross Axis**.
![[Pasted image 20231105180343.png]]
## align-self property

This property works on the child classes. It positions the selected item along the **Cross Axis**.
![[Pasted image 20231105180612.png]]
In total we have 6 values:
- flex-start
- flex-end
- center
- baseline
- stretch
- auto

## flex - grow | shrink | wrap | basis properties
The properties we'll discuss now will work when we resize the window. Let's dive right in.
### flex-grow
This property grows the size of a flex-item based on the width of the flex-container.
### flex-shrink
This property helps a flex item shrink based on the width of the flex-container. It's the opposite of flex-grow.
**flex-grow** and **flex-shrink** work on child classes. So, we will target all our boxes like this:
!!!Note that you need to delete the flex-wrap property first, otherwise it won't work.

![[Pasted image 20231105181309.png]]

### flex-wrap
This property helps you set the number of flex-items you want in a line or row.
This works on the `.container` parent class. So, write the following code:
```css
.container{
    //other codes are here 
  
// Change value 👇 here to see results
    flex-wrap : wrap;
```
![[Pasted image 20231105181932.png]]
### flex-basis

This is similar to adding width to a flex-item, but only more flexible. flex-basis: 10em, for example, will set the initial size of a flex-item to 10em. Its final size will be based on the available space, flex-grow, and flex-shrink.

## Shorthand Flexbox Properties
### flex shorthand

This is the shorthand for the **flex-grow**, **flex-shrink** and **flex-basis** properties combined.
**Please note** that it only works on the child classes:
![[Pasted image 20231105182238.png]]
### flex-flow

This is the shorthand for the **flex-direction** and **flex-wrap** properties:
![[Pasted image 20231105182317.png]]
## place-content

This is the shorthand for the justify-content and align-content properties:
**Please note** that it works on the parent class.
![[Pasted image 20231105182341.png]]

---------------------EOB--------------------------
### Flex container: 
When we add `display:flex`  property inside any element, then that element becomes flex container
![[Pasted image 20231105191304.png]]

## Regex in css
### The ^
```css
[class^="mo"] {background:yellow;} /*class attribute begins with mo*/
```
The example above will select all elements containing a class which begins with ‘mo’. Examples of this would be elements with classes such as moon, motech, modern.

### The $
```css
[class$="mo"] {color:red;} /*class attribute ends with mo*/
```
The example above will select all elements containing a class which end with ‘mo’. Examples of this would be elements with classes such ammo, emo, alamo.
### The *
```css
[class*="mo"] {color:red;} /*class attribute contains mo anywhere within it*/
```
The example above will select all elements containing a class which contains ‘mo’ somewhere in it. Examples of this would be elements with classes such slowmotion, emotion, and locomotive.

## [You can target other attributes](https://www.clevelandwebdeveloper.com/tutorials/use-regular-expressions-css/)

You can select elements based on any attribute – not just class. You might consider selecting link elements based on the href value. Often times this is a useful technique I use if I want all phone number links to be styled uniformly in a way that sticks out as a call to action. See the code below:
```css
a[href^="tel"] { text-decoration:underline;color:green; }
```
This will make it so that all links where the href value begins with ‘tel’ (which is the standard protocol for phone number links) will be underlined and have the color green. Another idea to consider is that you might want to have all links to a given webpage by styled a certain way – here’s how you would do that:
```css
a[href*="cnn.com"] { font-weight:bold; font-size:200%; }
```
And Voila – now all your links to sites on cnn.com will be bolded and extra large.

## [USING THE CSS :NOT SELECTOR](https://www.clevelandwebdeveloper.com/code-snippets/using-css-selector/)
Normally in CSS the way to select your desired elements is based on a property or properties which the element has. For example, you might want to select all DIV elements with class “myspecialclass”. However, suppose that you want to select an element in CSS based on the property which an element DOES NOT have. The code below will show you how to achieve this.
```css
/* select 'element with class .column' which is a descendant of 'element with class content that does not have class blog_style*/
.content:not(.blog_style) .column {background:red;}
```
In the example below, only the second instance will be selected and made red, because this is the only element which matches the “Not” selector of our CSS above
```html
<div class="content blog_style">
	<div class="column">This is a column</div>
</div>
<div class="content"> 
	<div class="column">This is a column</div><!--CSS applies because 'ancestor with class content' DOES NOT 'have class blog_style' -->
</div>
<div class="content blog_style"> 
	<div class="column">This is a column</div>
</div>
```

# Css-Grid
CSS grid is used for creating two-dimensional layoutsThe advent of CSS grid means we no longer need to deploy hacks like `positioning` and `floats`.
In cases where you want fine-grained control over the position of each individual element on the page, CSS grid shines as the better tool. CSS grid’s `grid-template-areas`, grid lines, and grid-spanning features make this possible. While we can also achieve this fine-grained control with flexbox, it usually requires more lines of code, which can be tricky to maintain and manage over time, and wild CSS files are always difficult to work with.
![[Pasted image 20231105221343.png]]
![[Pasted image 20231105222117.png]]
A **grid container** is an [HTML element](https://codesweetly.com/web-tech-terms-h#html-element) whose [`display`](https://codesweetly.com/css-display-property) property's value is `grid` or `inline-grid`.
A **grid item** is any of the direct children of a grid container.

`grid` tells browsers to display the selected HTML element as a block-level grid box model.
In other words, setting an element's `display` property's value to `grid` turns the box model into a [block-level](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) grid layout module.
```css
section {
  display: grid;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```
!!!**Note:**

- The `display: grid` directive creates only a single-column grid container. Therefore, the grid items will display in the normal layout flow (one item below another).
- Converting a node to a grid box model makes the element's direct children become grid items.
- The `display: grid` directive only affects a box model and its direct children. It does not affect grandchildren nodes.
**inline-grid:**
`inline-grid` tells browsers to display the selected HTML element as an inline-level grid box model.

In other words, setting an element's `display` property's value to `inline-grid` turns the box model into an [inline-level](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements) grid layout module.
```css
section {
  display: inline-grid;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```
On converting a regular HTML element to a grid (or inline-grid) box model, the grid layout module provides two categories of properties for positioning the grid box and its direct children:

- Grid container's properties
- Grid item's properties
![[Pasted image 20231105222250.png]]
### Fractional units

The `fr` value, otherwise known as the fractional unit, solves the problem of automatically distributing free space among elements and replaces the need for percentages.
```css
.container {
  display: grid;
  gap: 10px;
  grid-template-columns: 1fr 1fr 1fr auto;
}
```
### `repeat()`

The [`repeat()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/repeat()) allows recurring patterns to be written succinctly — one you’ll use quite a bit when it comes to CSS grid. We define how many rows or columns we desire followed by a constraint, but you can also pass other functions or keywords as arguments. See the code below:
```css
.parent-container {
    grid-template-columns: repeat(2, 1fr) 2fr auto;
}
```
### [Placing Grid Items: Start Here, End There](https://www.digitalocean.com/community/tutorials/placing-spanning-and-density-in-css-grid#placing-grid-items-start-here-end-there)
The grid items have placement values defined by `grid-[x]-start` and `grid-[x]-end` (where `x` can be `column` or `row`). The value is auto.

When you see a grid layout, it can help to remember that each item in that grid has a placement value no matter how symmetric the flow looks:
```css
.item:nth-child(1) {
      grid-column-start: 1;
      grid-column-end: 5;
    }
```
- We want the first item in the grid `.item:nth-child(1)`
- To start at **line** one, `grid-column-start: 1;`
- And end at **line** 5, `grid-column-end: 5;`

There’s also shorthand syntax for `grid-[x]-start` and `grid-[x]-end` that allows you to do away with the `-start` and `-end` code:
```css
.item {
      grid-column: [start] / [end];
      grid-row: [start] / [end];
    }
```

```css
 .item {
      grid-column: 1 / 5; /*__ Line 1 to 5 */
      grid-row: 1 / 4; /*_ Line 1 to 4 __*/
      grid-column: 5 / auto; /* Line 5 to 6 *_*/
      grid-column: auto / 3; /*_ Line 2 to 3 _*/
    }
```

When we say line `1` to `5`, we are saying the grid item should span from `1` to `5`. I usually refer to this as implicit spanning.

There is a `span` keyword that serves as a value. When this is used, you can refer to it as explicit spanning. Placing and spanning are flexible enough that you can use both implicit and explicit spanning as value to a single property.

```css
.container{
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
}

.child-item:nth-child(1) {
  grid-column: span 2; /* span 2 columns */
}

.child-item:nth-child(2) {
  grid-column: span 3
}
```

```css
.child-item:nth-child(1) {
  grid-column: span 2 / 5;
}
```
The code above tells the browser to span my `grid` item two columns wide and end it at column five. This represents the `column-start`/`column-end` position, but notice we didn’t tell the browser where to start the column; we only said where to end.

This is something the browser figures out. It automatically understands that we want to span two columns and end column five’s grid line, so it calculates that the item will start at the end of column two’s grid line.

If we want to tell the browser exactly where to start a `child-item`, we’d remove the `span` keyword:
```css
.child-item {
  grid-column: 2 / 5;
}
```

### Grid Area
Using a set of quotes containing words of your choosing, such as `"sidebar1 content sidebar2"`, we begin to define our `grid areas`. You can also define multiple areas. For example:
```css
.container {
  display: grid;
  gap: 10px;
  grid-template:
    "header header header" auto
    "sidebar1 content sidebar2" 1fr
    "footer footer footer" auto
}
```
This property alleviates the need to worry about line numbers, and each one used will be positioned accordingly. You set the position by defining the property on a child item of your choosing:
```css
.header{
  grid-area: header;
}
.sidebar1{
  grid-area: sidebar1;
}
.content{
    grid-area: content;
}
.sidebar2{
  grid-area: sidebar2;
}
.footer{
    grid-area: footer;
}
```
Using `grid-area`, we pass the corresponding area as a value. Nothing more, nothing less; it’s that straightforward
`codepen example`: https://codepen.io/nefejames/pen/ZEjQrgG

### Named grid lines

This particular feature of CSS grid, [named grid lines](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Layout_using_Named_Grid_Lines), might be useful if you want to explicitly direct your layout behavior. You are granted the ability to name positions on your grid instead of using nameless numerical values:

When defining the grid, I name my lines inside square brackets. Those names can be anything you like. I have defined a name for the start and end of the container, both for rows and columns. Then defined the center block of the grid as `content-start` and `content-end` again, both for columns and rows although you do not need to name all of the lines on your grid. You might choose to name just some key lines for your layout.
```css
.wrapper {
  display: grid;
  grid-template-columns: [main-start] 1fr [content-start] 1fr [content-end] 1fr [main-end];
  grid-template-rows: [main-start] 100px [content-start] 100px [content-end] 100px [main-end];
}

```
Once the lines have names, we can use the name to place the item rather than the line number.
`Example for named grid :` https://developer.mozilla.org/en-US/play

### Functions
#### repeat()
The [`repeat()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/repeat()) allows recurring patterns to be written succinctly — one you’ll use quite a bit when it comes to CSS grid. We define how many rows or columns we desire followed by a constraint, but you can also pass other functions or keywords as arguments. See the code below:
```css
.parent-container {
    grid-template-columns: repeat(2, 1fr);
}
```

#### fit-content()

The [`fit-content()` property](https://developer.mozilla.org/en-US/docs/Web/CSS/fit-content) does one thing: clamps a value to a given size passed:

You’ll mostly use it with `grid-template-columns` and `grid-template-row`. For example:
```css
.parent-container {
    grid-template-columns: fit-content(200px) fit-content(400px) 1fr;
}
```
### `minmax()`

The [`minmax()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/minmax) defines a range between a set of values that functions as — you guessed it — a minimum and maximum constraint — and writing it is a breeze:
When content breaks column bounds, this function can be used inside `repeat()`. For example:
```css
.parent-container {
    grid-template-columns: repeat(3, minmax(150px, 1fr))
}
```
### `auto-fill` / `auto-fit`

The `auto-fill` keyword ends the grid on the explicit grid line and fills all the available space. It also stretches items inside the grid’s tracks to fit. This makes it a worthy approach for wrapping elements when combined with `minmax()`.

The `auto-fit` keyword ends the grid at the explicit column line. This is the opposite of what `auto-fill` does, as it expands the explicit grid.

You can use this keyword within the `repeat()` function. For example:

`repeat(auto-fill, 150px)`
