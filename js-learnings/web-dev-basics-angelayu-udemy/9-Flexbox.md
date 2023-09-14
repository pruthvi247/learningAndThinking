
Before the Flexbox Layout module, there were four layout modes:

- Block, for sections in a webpage
- Inline, for text
- Table, for two-dimensional table data
- Positioned, for explicit position of an element

The Flexible Box Layout Module, makes it easier to design flexible responsive layout structure without using float or positioning.

## Flexbox Elements

To start using the Flexbox model, you need to first define a flex container.

```html
<!DOCTYPE html>
<html>
<head>
<style>
.flex-container {
  display: flex;
  background-color: DodgerBlue;
}

.flex-container > div {
  background-color: #f1f1f1;
  margin: 10px;
  padding: 20px;
  font-size: 30px;
}
</style>
</head>
<body>

<h1>Create a Flex Container</h1>

<div class="flex-container">
  <div>1</div>
  <div>2</div>
  <div>3</div>  
</div>

<p>A Flexible Layout must have a parent element with the <em>display</em> property set to <em>flex</em>.</p>

<p>Direct child elements(s) of the flexible container automatically becomes flexible items.</p>

</body>
</html>
```

Examples:
`same layout but with different approaches`
![[js-learnings/attachments/flex.html]]
![[absolute-position.html]]![[float.html]]
![[html-table.html]]

![[inline-block.html]]

# Flex-Layout

[demo-site](https://yuangela.com/flex-layout/)
[best-site-forpractice](https://flexboxfroggy.com/)
[cheet-sheet](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
![[Pasted image 20230618114028.png]]

# Flex-sizing

[good-read](https://webdesign.tutsplus.com/tutorials/a-comprehensive-guide-to-flexbox-sizing--cms-31948)
`Content width < width < flex-basis < min-width/max-width`

One of the most challenging aspects of writing CSS is figuring out how to allocate the free space that remains on the screen after the page has been populated with content. At some viewport sizes, you’ll often find there’s too much remaining space and you want to fill it with something. At other viewport sizes, you might find there’s not enough space, and the layout breaks in one way or another.

Flexbox’s sizing properties allow you to make decisions about three kinds of scenarios:

1. `flex-grow`: how flex items should behave when there’s a _surplus of free space_ (how they should _grow_).
2. `flex-shrink`: how flex items should behave when there’s a _shortage of free space_ (how they should _shrink_).
3. `flex-basis`: how flex items should behave when there’s _exactly as much space as needed._
**flex-grow**: 
 Let’s start with the following HTML:

```html
<div class="container">
    <div class="item item-1">1</div>
    <div class="item item-2">2</div>
    <div class="item item-3">3</div>
</div>
```
The  `.container` class will be the flex container (defined by `display: flex;`) and our `.item` elements will be the flex items:
```css
.container {
  background-color: darkslategrey;
  padding: 1rem;
  display: flex;
  flex-direction: row;
}
.item {
  font-size: 2rem;
  line-height: 1;
  text-align: center;
  width: 3rem;
  padding: 2rem 1rem;
  background: #e2f0ef;
  border: 3px solid #51aaa3;
  color: #51aaa3;
  margin: 0.375rem; 
}
```

```css
.item {
    flex-grow: 1;   
}
.item-1 {
    flex-grow: 2;
}
```

**Flex-shrik**
The `[flex-shrink](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-shrink)` property is the opposite of `flex-grow`. It defines how flex items should behave when there’s not enough space on the screen. This happens when flex items are larger than the flex container.

Without `flex-shrink`, the following CSS would result in a layout where the items overflow the container, as the total width of the items (3*10rem) is bigger than the container’s width (20rem).

```css
.item-1 {
   flex-shrink: 1;
}
.item-2 {
   flex-shrink: 1;
}
.item-3 {
   flex-shrink: 2;
}
```

**Flex-basis**
The last scenario of free space allocation is when there’s exactly as much space on the screen as you need. This is when flex items will take the value of `flex-basis`. 

The `[flex-basis](https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis)` property defines the initial size of flex items. The default value of `flex-basis` is `auto`, which means that the size of the flex items is calculated using either the `width` or `height` of the element (depending on if it’s a row-based or column-based layout). 

However, when the value of `flex-basis` is something other than `auto`, it overrides the value of `width` (or `height` in case of vertical layouts). For example, the following CSS overrides the default `width: 20rem;` rule with a respective value for each flex item:
```css
.item {
    width: 20rem;
    padding: 2rem 1rem;
    font-size: 2rem;
    line-height: 1;
    text-align: center;  
    background: #e2f0ef;
    border: 3px solid #51aaa3;
    color: #51aaa3;
    margin: 0.375rem; 
}
.item-1 {
   flex-basis: 5rem;
}
.item-2 {
   flex-basis: 10rem;
}
.item-3 {
   flex-basis: 30rem;
}
```
`Note` that while `flex-grow` and `flex-shrink` have relative values (`0`, `1`, `2`, etc.), `flex-basis` always takes an absolute value (`px`, `rem`, `content`, etc.).

## flex Shorthand

Flexbox’s sizing properties also have a shorthand called [flex](https://developer.mozilla.org/en-US/docs/Web/CSS/flex). The `flex` property abbreviates `flex-grow`, `flex-shrink`, and `flex-basis` in the following way:
```css/* Longhand form of default values */
.item {
  flex-grow: 0;
  flex-shrink: 1;
  flex-basis: auto;
}
/* Shorthand form of default values */
.item {
    flex: 0 1 auto;
}
```
You don’t necessarily have to list all the three values if you don’t want. You can use `flex` with one or two values, according to the following rules and assumptions:
```
/* One relative value: flex-grow */
flex: 1;
/* One absolute value: flex-basis */
flex: 20rem;
flex: 50px;
/* One relative and one absolute value: flex-grow | flex-basis */
flex: 1 20rem;
/* Two relative values: flex-grow | flex-shrink */
flex: 1 2;
/* Three values: flex-grow | flex-shrink | flex-basis */
flex: 1 2 20rem;
/* Fully inflexible layout: equivalent of flex: 0 0 auto */
flex: none;
```

**Exercise**
![[58-pricing-table-solution.html]]
























