# Css units
CSS has several different units for expressing a length.

Many CSS properties take "length" values, such as `width`, `margin`, `padding`, `font-size`, etc.

**Length** is a number followed by a length unit, such as `10px`, `2em`, etc.

**Note:** A whitespace cannot appear between the number and the unit. However, if the value is `0`, the unit can be omitted.

For some CSS properties, negative lengths are allowed.

There are two types of length units: **absolute** and **relative**.

## Absolute Lengths

The absolute length units are fixed and a length expressed in any of these will appear as exactly that size.

Absolute length units are not recommended for use on screen, because screen sizes vary so much. However, they can be used if the output medium is known, such as for print layout.

| Unit | Description                  |
| ---- | ---------------------------- |
| cm   | centimeters                  |
| mm   | millimeters                  |
| in   | inches (1in = 96px = 2.54cm) |
| px * | pixels (1px = 1/96th of 1in) |
| pt   | points (1pt = 1/72 of 1in)   |
| pc   | picas (1pc = 12 pt)          |
\* Pixels (px) are relative to the viewing device. For low-dpi devices, 1px is one device pixel (dot) of the display. For printers and high resolution screens 1px implies multiple device pixels.

## Relative Lengths

Relative length units specify a length relative to another length property. Relative length units scale better between different rendering medium.

| Unit | Description                                                                               |     |
| ---- | ----------------------------------------------------------------------------------------- | --- |
| em   | Relative to the font-size of the element (2em means 2 times the size of the current font) |     |
| ex   | Relative to the x-height of the current font (rarely used)                                |     |
| ch   | Relative to the width of the "0" (zero)                                                   |     |
| rem  | Relative to font-size of the root element                                                 |     |
| vw   | Relative to 1% of the width of the viewport*                                              |     |
| vh   | Relative to 1% of the height of the viewport*                                             |     |
| vmin | Relative to 1% of viewport's* smaller dimension                                           |     |
| vmax | Relative to 1% of viewport's* larger dimension                                            |     |
| %    | Relative to the parent element                                                            |     |
`
**Tip:** The em and rem units are practical in creating perfectly scalable layout!  
* Viewport = the browser window size. If the viewport is 50cm wide, 1vw = 0.5cm.
`
## Box model

![[Pasted image 20250809220315.png]]

_Box-sizing_ is a CSS style property that is applied to HTML elements (via said CSS). If not specified, the default box-sizing property of every box is implicitly set to _content-box;_, which means the whole implicit attribute would be: _box-sizing: content-box;._

When not altered, or left to its default _content-box_ property, an HTML element’s box total width will be the sum of the specified width, padding (times 2 because padding and border add its length to the left and also to the right), and border (also times 2 just as with padding). So for example,
```css
#name-form{
width: 500px;
padding: 10px;
Border: 5px;
}
/* 
no border-sizing specified, so the default setting is content-box
*/
```
In the above example, the total width of the #name-form element will be 530px because with the default (unspecified) content-box setting, the padding and border are added to the specified width. So, 500px (width) + 10px (padding left side) + 10px (padding right side) + 5px (border left side) + 5px (border right side).

```css
#name-form{
width: 500px;
padding: 10px;
Border: 5px;
box-sizing: border-box;
}

```

In this example, the box-sizing property is explicitly changed to border-box. This means that the specified width will always be the final size of the element’s box, this includes padding and border (but not margin, margin is always outisde of the border box dimensions). So from the total 500px width of the box, 20px will be for padding and 10px will be for the border (remember, times 2 because they are on the left and right side), leaving the content area left with 470px.


### Outline property

![[Pasted image 20250809221735.png]]

## Display property
`Block vs inline`

`Block`: Always starts a new line and takes full width
`Inline`: Does not start and only take up as much as content space

![[Pasted image 20250809222153.png]]
> `display:none` - will not even show element in inspector

We can control these inline/block
```css
.inline{
background: red;
color: white;
display: block;
}
```

`how to center block elements ??` - by using margin property

```css
.block{
backgroud:blue;
margin: 0 auto;
}
```

> Note: For `inline` elements, browser doesn't honour top and bottom margins, But it honours if its `block` element

`inline-block` : honours margins

> Note: Padding increases size of box(parent)
#### box-sizing- borderbox
padding is inserted inside the box, if not it's added outside
![[Pasted image 20250809224426.png]]


# Media query

`min-width`: starting from
`max-width` : upto
>mobile first

## CSS Z-index
When there are multiple overlapping elements, the z-index helps in deciding the order of their visibility. The element having the highest value of z-index is shown first, followed by the other elements.
```css
<!DOCTYPE html>
<html>

<head>
    <title>CSS Z Index</title>
    <style>
        .container {
            position: relative;
        }
       
        .box1-box {
            position: relative;
            z-index: 1;
            border: 2px solid black;
            height: 100px;
            margin: 40px;
            background-color: aqua;
        }
       
        .box2-box {
            position: absolute;
            z-index: 3;
            background-color: rosybrown;
            height: 60px;
            width: 70%;
            left: 250px;
            top: 50px;
            border: 2px solid;
        }
       
        .box3-box {
            position: absolute;
            color: wheat;
            z-index: 2;
            background-color: rebeccapurple;
            width: 45%;
            left: 270px;
            top: 15px;
            height: 100px;
            border: 2px solid;
        }
    </style>
</head>

<body>

    <h1>CSS z-index</h1>

    <div class="container">
        <div class="box1-box">Box 1 (z-index: 1)</div>
        <div class="box2-box">Box 2 (z-index: 3)</div>
        <div class="box3-box">Box 3 (z-index: 2)</div>
    </div>

</body>

</html>
```

output
![[Pasted image 20250810105049.png]]
> Note : z index doesn't work on static position

# Pseudo-Classes and Pseudo-Elements in CSS
###### Syntax

- The single colon `:` refers to pseudo-classes
- The double colon `::` refers to pseudo-elements
### What are Pseudo-Classes in CSS?

Pseudo-classes (`:`) are primarily used to style an element that's under various states. When referring to state, this includes the condition or user behavior, for example hover, active, focus, or disabled. States generally involve user interaction.

For example, we can target all links to have a text color of lavender when the user hovers over the link.

```css
a:hover {
  color: lavender;
}
```
### What are Pseudo-Elements in CSS?

Pseudo-elements (`::`) are used to style specified parts of an element. They can be used to target the first letter or first line. Or they can be used to insert content before or after the element.

It's worth getting familiar with this [index of pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements#alphabetical_index) to learn more about the available keywords.

As an example, to create a large first letter of a paragraph, you can do that using `first-letter` like this:

```css
p::first-letter {
  font-size: 9em;
}
```

1. CSS Transitions:

- **Purpose:**
    
    Transitions provide a straightforward way to animate changes in CSS properties over a specified duration.
    
- **Application:**
    
    Applied to the base element, they define how a property changes when its value is altered (e.g., on `:hover`, `:focus`).
    
- **Properties:**
    
    - `transition-property`: Specifies the CSS property to be animated (e.g., `transform`, `opacity`, `background-color`). Use `all` to transition all changing properties.
    - `transition-duration`: Sets the time the transition takes (e.g., `0.3s`, `500ms`).
    - `transition-timing-function`: Defines the acceleration curve of the transition (e.g., `ease`, `linear`, `ease-in-out`).
    - `transition-delay`: Specifies a delay before the transition begins.
    
- **Example:**
    

Code

```css
     .box {
        transition: transform 0.5s ease-in-out;
    }

    .box:hover {
        transform: scale(1.2);
    }
```

2. CSS Transforms:

- **Purpose:** The `transform` property allows for manipulating an element's position, rotation, scale, and skew in 2D or 3D space.
- **Functions:**
    - `translate()`: Moves an element (e.g., `translateY(10px)`).
    - `rotate()`: Rotates an element (e.g., `rotate(45deg)`).
    - `scale()`: Scales an element (e.g., `scale(1.5)`).
    - `skew()`: Skews an element (e.g., `skewX(20deg)`).
- **Example:**

Code

```css
    .element {
        transform: rotate(30deg) translateX(50px);
    }
```

3. Combining Transitions and Transforms:

- Transitions are frequently used to animate changes in `transform` properties, resulting in smooth animations like scaling on hover or rotating on click.

4. CSS Animations (Keyframes):

- **Purpose:**
    
    For more complex, multi-step animations, CSS Animations using `@keyframes` offer greater control.
    
- **Mechanism:**
    
    Define specific styles at different points (percentages) within the animation's timeline.
    
- **Properties:**
    
    `animation-name`, `animation-duration`, `animation-timing-function`, `animation-iteration-count`, `animation-direction`, `animation-fill-mode`.
    
- **Example:**
    

Code

```css
        @keyframes slideIn {
        0% {
            transform: translateX(-100%);
        }
        100% {
            transform: translateX(0);
        }
    }

    .menu {
        animation: slideIn 1s forwards;
    }
```

>`Transition` 0 ->100%
`Animation`  0 1% 2% 3% ....100%

`Animation-fill-mode`: What values are applied by the animation outside the time it is executing
