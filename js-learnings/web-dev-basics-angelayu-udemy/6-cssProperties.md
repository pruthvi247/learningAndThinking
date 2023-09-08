
# color properties
```html
<!DOCTYPE html>
<html>
<head>

<style>
body {
  color: red;
  background-color : antiquewhite
}

h1 {
  color: #00ff00;
}

p.ex {
  color: rgb(0,0,255);
}
</style>
</head>
<body>

<h1>This is heading 1</h1>

<p>This is an ordinary paragraph. Notice that this text is red. The default text-color for a page is defined in the body selector.</p>

<p class="ex">This is a paragraph with class="ex". This text is blue.</p>

</body>
</html>
```

# Font properties

```
font: _font-style_ _font-variant_ _font-weight_ _font-size/line-height font-family_|caption|icon|menu|message-box|small-caption|status-bar|initial|inherit;
```

|Property/Value|Description|Demo|
|---|---|---|
|_[font-style](https://www.w3schools.com/cssref/pr_font_font-style.php)_|Specifies the font style. Default value is "normal"|[Demo ❯](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_font-style)|
|_[font-variant](https://www.w3schools.com/cssref/pr_font_font-variant.php)_|Specifies the font variant. Default value is "normal"|[Demo ❯](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_font-variant)|
|_[font-weight](https://www.w3schools.com/cssref/pr_font_weight.php)_|Specifies the font weight. Default value is "normal"|[Demo ❯](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_font-weight)|
|_[font-size](https://www.w3schools.com/cssref/pr_font_font-size.php)/[line-height](https://www.w3schools.com/cssref/pr_dim_line-height.php)_|Specifies the font size and the line-height. Default value is "normal"|[Demo ❯](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_font-size)|
|_[font-family](https://www.w3schools.com/cssref/pr_font_font-family.php)_|Specifies the font family. Default value depends on the browser|[Demo ❯](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_font-family)|
|caption|Uses the font that are used by captioned controls (like buttons, drop-downs, etc.)||
|icon|Uses the font that are used by icon labels||
|menu|Uses the fonts that are used by dropdown menus||
|message-box|Uses the fonts that are used by dialog boxes||
|small-caption|A smaller version of the caption font||
|status-bar|Uses the fonts that are used by the status bar||
|initial|Sets this property to its default value. [Read about _initial_](https://www.w3schools.com/cssref/css_initial.php)||
|inherit|Inherits this property from its parent element. [Read about _inherit_](https://www.w3schools.com/cssref/css_inherit.php)|
```html
<!DOCTYPE html>
<html>
<head>
<style>
p.a {
  font: 15px Arial, sans-serif;
}

p.b {
  font: italic small-caps bold 12px/30px Georgia, serif;
}
p#c {
  font: 55px Arial, sans-serif;
}
</style>
</head>
<body>

<h1>The font Property</h1>

<p class="a">This is a paragraph. The font size is set to 15 pixels, and the font family is Arial.</p>


<p id="c">This is a paragraph. The font size is set to 55 pixels, and the font family is Arial.</p>

<p class="b">This is a paragraph. The font is set to italic and bold, with small-caps (all lowercase letters are converted to uppercase). The font size is set to 12 pixels, the line height is set to 30 pixels, and the font family is Georgia.</p>

</body>
</html>
```

# Boxmodel

The CSS box model is essentially a box that wraps around every HTML element. It consists of: margins, borders, padding, and the actual content. The image below illustrates the box model:

![[Pasted image 20230617120633.png]]

Explanation of the different parts:

- **Content** - The content of the box, where text and images appear
- **Padding** - Clears an area around the content. The padding is transparent
- **Border** - A border that goes around the padding and content
- **Margin** - Clears an area outside the border. The margin is transparent

The box model allows us to add a border around elements, and to define space between elements.

```html
<!DOCTYPE html>
<html>
<head>
<style>
div {
  background-color: lightgrey;
  width: 300px;
  border: 15px solid green;
  padding: 50px;
  margin: 20px;
}
</style>
</head>
<body>

<h2>Demonstrating the Box Model</h2>

<p>The CSS box model is essentially a box that wraps around every HTML element. It consists of: borders, padding, margins, and the actual content.</p>

<div>This text is the content of the box. We have added a 50px padding, 20px margin and a 15px green border. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>

<div>
<p>
Div element acts as a container for differect sections we can group elements in div
</p>
</div>

</body>
</html>
```
Here is the calculation:  

```
320px (width)  
+ 20px (left + right padding)  
+ 10px (left + right border)  
+ 0px (left + right margin)  
**= 350px**
```
The total width of an element should be calculated like this:

Total element width = width + left padding + right padding + left border + right border + left margin + right margin

The total height of an element should be calculated like this:

`Total element height = height + top padding + bottom padding + top border + bottom border + top margin + bottom margin`

#extension

[pesticide chrome extension](https://chrome.google.com/webstore/detail/pesticide-for-chrome/bakpbgckdnepkmkeaiomhmfcnejndkbi)


# 7-Specificity and in heritance

> ## Important
> position < specificity < Type < Importance

### Position order:

- Last one will be considered in the order

### specificity order :
` id > attribute > class > element`

### Type order: 

`inline > internal > external`

```html
<link rel="stylesheet" href="./stylesheet.css"> /// external
<Style> ###### </style> //// internal
<h1 style = " "> hello </h1> //// inline
```

### importance : 
```css
color: red;
color: green !important; /// this will take priority
```



Also refer : https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance

**Specificity** is the algorithm used by browsers to determine the [CSS declaration](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/What_is_CSS#css_syntax) that is the most relevant to an element, which in turn, determines the property value to apply to the element. The specificity algorithm calculates the weight of a [CSS selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference#selectors) to determine which rule from competing CSS declarations gets applied to an element.

Also significant here is the concept of [**inheritance**](https://developer.mozilla.org/en-US/docs/Web/CSS/Inheritance), which means that some CSS properties by default inherit values set on the current element's parent element and some don't. This can also cause some behavior that you might not expect.

## Specificity 
In the below example, we have two rules that could apply to the `<h1>` element. The `<h1>` content ends up being colored `blue`. This is because both the rules are from the same source, have an identical element selector, and therefore, carry the same specificity, but the last one in the source order wins.
```css
h1 { 
    color: red; 
}
h1 { 
    color: blue; 
}
---------------
<h1>This is my heading.</h1>
```

- An element selector is less specific; it will select all elements of that type that appear on a page, so it has less weight. Pseudo-element selectors have the same specificity as regular element selectors.
- A class selector is more specific; it will select only the elements on a page that have a specific `class` attribute value, so it has more weight. Attribute selectors and pseudo-classes have the same weight as a class.

Below, we again have two rules that could apply to the `<h1>` element. The `<h1>` content below ends up being colored red because the class selector `main-heading` gives its rule a higher specificity. So even though the rule with the `<h1>` element selector appears further down in the source order, the one with the higher specificity, defined using the class selector, will be applied.

```css
.main-heading { 
    color: red; 
}
        
h1 { 
    color: blue; 
------------
<h1 class="main-heading">This is my heading.</h1>

------------
output: red
```

## Inheritance

Inheritance also needs to be understood in this context — some CSS property values set on parent elements are inherited by their child elements, and some aren't.

For example, if you set a `color` and `font-family` on an element, every element inside it will also be styled with that color and font, unless you've applied different color and font values directly to them.

```css
body {
    color: blue;
}

span {
    color: black;
}

-------------
<p>As the body has been set to have a color of blue this is inherited through the descendants.</p>
<p>We can change the color by targeting the element with a selector, such as this <span>span</span>.</p>
    
```

>Some properties do not inherit — for example, if you set a [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/width) of 50% on an element, all of its descendants do not get a width of 50% of their parent's width. If this was the case, CSS would be very frustrating to use!

Properties like `width` (as mentioned earlier), `margin`, `padding`, and `border` are not inherited properties.

## [Understanding how the concepts work together](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#understanding_how_the_concepts_work_together)

These three concepts (cascade, specificity, and inheritance) together control which CSS applies to what element. In the sections below, we'll see how they work together. It can sometimes seem a little bit complicated, but you will start to remember them as you get more experienced with CSS, and you can always look up the details if you forget!\

### [Controlling inheritance](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#controlling_inheritance)
[`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/inherit)

Sets the property value applied to a selected element to be the same as that of its parent element. Effectively, this "turns on inheritance".

[`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/initial)

Sets the property value applied to a selected element to the [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/initial_value) of that property.
[`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/revert)

Resets the property value applied to a selected element to the browser's default styling rather than the defaults applied to that property. This value acts like [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/unset) in many cases.
[`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/revert-layer)

Resets the property value applied to a selected element to the value established in a previous [cascade layer](https://developer.mozilla.org/en-US/docs/Web/CSS/@layer).
[`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/unset)

Resets the property to its natural value, which means that if the property is naturally inherited it acts like `inherit`, otherwise it acts like `initial`.

Example `:
```css
body {
    color: green;
}
          
.my-class-1 a {
    color: inherit;
}
          
.my-class-2 a {
    color: initial;
}
          
.my-class-3 a {
    color: unset;
}
-----------------------

<ul>
    <li>Default <a href="#">link</a> color</li>
    <li class="my-class-1">Inherit the <a href="#">link</a> color</li>
    <li class="my-class-2">Reset the <a href="#">link</a> color</li>
    <li class="my-class-3">Unset the <a href="#">link</a> color</li>
</ul>
    
```
preview:
![[Pasted image 20230617155159.png]]

1. The second list item has the class `my-class-1` applied. This sets the color of the `<a>` element nested inside to `inherit`. If you remove the rule, how does it change the color of the link?
2. Do you understand why the third and fourth links are the color that they are? The third link is set to `initial`, which means it uses the initial value of the property (in this case black) and not the browser default for links, which is blue. The fourth is set to `unset` which means that the link text uses the color of the parent element, green.
3. Which of the links will change color if you define a new color for the `<a>` element — for example `a { color: red; }`?
4. After reading the next section on resetting all properties, come back and change the `color` property to `all`. Notice how the second link is on a new line and has a bullet. What properties do you think were inherited?

Example 2:
```css
.main {
    color: rebeccapurple;
    border: 2px solid #ccc;
    padding: 1em;
}

.special {
    color: black;
    font-weight: bold;
}
--------------------
<ul class="main">
    <li>Item One</li>
    <li>Item Two
        <ul>
            <li>2.1</li>
            <li>2.2</li>
        </ul>
    </li>
    <li>Item Three
        <ul class="special">
            <li>3.1
                <ul>
                    <li>3.1.1</li>
                    <li>3.1.2</li>
                </ul>
            </li>
            <li>3.2</li>
        </ul>
    </li>
</ul>
```


### quiz: [](https://rakuten.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37350528#overview)
`Q1

`Q2`
```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .a-class{
            color: blue ;
        }
        .another-class{
            color:green;
        }
    </style>
</head>
<body>
    <h1 class="a-class another-class id">hello there!</h1> //// two classes later one will be applied based on position
</body>
</html> 

```

`Q2`
```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .a-class{
            color: blue ;
        }
        #an-id{
            color:green;
        }
    </style>
</head>
<body>
    <h1 class="a-class" id="an-id">hello there!</h1> //// Id has more weight based on specificity order/
</body>
</html> 

```
`q3`
```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #an-id{
            color:green;
        }
    </style>
</head>
<body>
    <h1  id="an-id" style="color:blue">hello there!</h1> //// Inline style based on css specifity type> speceficity
</body>
</html> 

```

`exercise`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      html {
        background-color: blue;
      }
      h1.whitetext {
        background-color: red;
        width: 300px;
        /* border: 15px solid green; */
        /* padding: 50px; */
        /* margin: 20px; */
      }
      .yellowtext {
        color: yellow;
      }
      #an-id {
        color: green;
      }
    </style>
  </head>
  <body>
    <div>
      <h1 class="yellowtext">yellow-text</h1>
      <h1 class="whitetext">White text</h1>
    </div>
  </body>
</html>

```


quiz
```css
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        .a-class{
            color: blue !important;
        }
        #an-id{
            color:green;
        }
    </style>
</head>
<body>
    <h1 class="a-class" id="an-id">hello there!</h1>
</body>
</html> 

```

## combinng css selectors

### **Group selectors**
```css
selector, selector{
color : blue;
}
----------

.class-selector-name, h2{
color: red;
}
```

### Child selector
```css
selector > selector{
color: firebrick;
}
----------------
parent > child{
color: firebrick;
}
----------------
.class-selector-name > p{
color: firebrick;
}

```

### Descendant selector : 
Apply to a descendent of left side

```css
selector1 selector2{ 
color: firebrick;
}
////// selector2 can be some where with in selector1, ie. selector1 comes first and selector2 is in same tree
---------------------
.class-selector-name li{ 
color: firebrick;
}
////// li is in under .class-name, not just one level below, could be anywhere under .class-name

```
### Chaining selector:
Apply where all selectors are true
```css
selector1selector2selector3{ /// selectors with out space 
color: firebrick;
}
-----------------
class-selector-nameh1{ 
color: firebrick;
}
//// avoid class names first, because "class-selector-nameh1" can be a class name, so start with elements, class and id selectors start with special charecters(#,.) so avoid
-------------------
h1class-selector-name{
color: firebrick;
}

```

### combining combiners
```css
selector1 > h1class-selector-name{ 
color: firebrick;
}
```

# Css positioning

**Positions** : [git examples](https://yuangela.com/css-positioning/)
1. Static (default)
2. Relative
3. Absolute
4. Fixed

## Static positioning:
```html
<div class="positioning-type static" style="display: block;">
      <h2>Static Positioning</h2>
      <code>
        position: static;<br>
        left: 50px;<br>
        top: 50px;<br></code>
      <div class="box"></div>
    </div>
```
### Relative positioning:
Position relative to default position
```css
<div class="positioning-type relative" style="display: none;">
      <h2>Relative Positioning</h2>
      <code>position: relative;<br>
      left: 50px;<br>
      top: 50px;<br></code>
      <div class="box"></div>
    </div>
```

### Absolute positioning: 
Position relative to nearest positioned ancestor or top left corner of webpage

```html
<div class="positioning-type absolute" style="display: none;">
      <h2>Absolute Positioning</h2>
      <code>
          position: absolute;<br>
          top: 50px;<br>
          left: 50px;<br>
      </code>
      <div class="box"></div>
    </div>
```

### Fixed positioning
Position relative to top left corner of browser window

```css
<div class="positioning-type fixed" style="display: none;">
      <h2>Fixed Positioning</h2>
      <code>
            position: fixed;<br>
            top: 50px;<br>
            left: 50px;<br>
      </code>
      <div class="box"></div>
    </div>
```


`Exercise` [](https://rakuten.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/37350652#questions/19589256)
```css
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>CSS Flag Project</title>
  <style>
    .flag {
      width: 900px;
      height: 600px;
      position: relative;
      background-color: #CE1126;

    }

    .flag > div {
      background-color: #002868;
      height: 300px;
      width: 100%;
      position: absolute;
      top: 150px;
    }

    .flag > div > div {
      background-color: white;
      position: absolute;

      height: 200px;
      width: 200px;
      border-radius: 50%;
      top: 50px;
      left: 350px;
    }

    p {
      font-size: 5rem;
      color: white;
      text-align: center;
      padding: 0;
      margin: 0;
    }

    .flag>div div p {
      color: black;
    }
  </style>
</head>

<body>
  <div class="flag">
    <p>The Flag</p>
    <div>
      <div>
        <p>of Laos</p>
      </div>
    </div>
  </div>
</body>

</html>
```

