# [box-sizing](https://css-tricks.com/box-sizing/)
Back in the old days of web design, early versions of Internet Explorer (<= IE6) handled the box model differently when it was in "quirks mode". The "quirks" box model worked like this: width = actual visible/rendered width of an element's box height = actual visible/rendered height of an element's box The border and padding values were moved inside the element's box, cutting into the width/height of the box rather than expanding it.

Without box-sizing, the width property represents the content area of the element. The actual rendered width includes the content area, padding, and border.

This means that if you set a width of something like 200px or a relative width of 25%, the element will only be that exact size if it has no padding or border. If it does have padding or border (or both), then the actual rendered size will be larger. Put another way, the width property really just means the width of the content area, and not the total width of the element.

As a result, calculating a desired width on the page involves subtracting padding and border from the width property. For example, if you set a width of 200px and then you want 20px of padding on each side, you have to borrow 40px (20px for the left and 20px for the right) from the width. The same thing is true for the border property. This makes code a lot less readable, because even though the rendered element is still 200px across, you might have code that reads like this
```
.sidebar {
  width: 158px;
  padding: 20px;
  border: 1px solid #DDD;
}
```

It’s not very intuitive for the width property to say 158px if the actual rendered width is 200px. Fortunately, there’s a better method that achieves the same result.

Today, the current versions of all browsers use the original “width or height + padding + border = actual width or height” box model. With `box-sizing: border-box;`, we can change the box model to what was once the “quirky” way, where an element’s specified width and height aren’t affected by padding or borders. This has proven so useful in responsive design that it’s found its way into reset styles.

Though `box-sizing` has three possible values (`content-box`, `padding-box`, and `border-box`), the most popular value is `border-box`.
### Demo

This demo shows how `border-box` can help make responsive layouts more manageable. The parent `div`‘s width is 50%, and it has 3 children with different widths, padding, and margins. Click the `border-box` button to get all the children in the right place inside the parent.

**Codepen** : https://codepen.io/team/css-tricks/pen/NqGBym/970f26f621cfa3ae3eec7e2a6b0e8c97

### Good, Better, and (Probably) Best `box-sizing` Reset Methods

#### [](https://css-tricks.com/box-sizing/#aa-the-old-border-box-reset)The “Old” `border-box` Reset

The earliest `box-sizing: border-box;` reset looked like this:
```css
* { box-sizing: border-box; }
```
This works fairly well, but it leaves out pseudo elements, which can lead to some unexpected results. A revised reset that covers pseudo elements quickly emerged:

#### Universal Box Sizing
```css
*, *:before, *:after {
  box-sizing: border-box;
}
```
This method selected pseudo elements as well, improving the normalizing effect of `border-box`. But, the `*` selector makes it difficult for developers to use `content-box` or `padding-box` elsewhere in the CSS. Which brings us to the current frontrunner for best practice:
```css
html { 
	box-sizing: border-box;
	}
*, *:before, *:after {
	box-sizing: inherit;
 }
```

When you set `inherit` on a CSS property, the property takes the value from the element’s parent.Only direct child elements can inherit a CSS property from its parent element using the `inherit` value if the CSS property is set by the element’s parent element.

Explaining further, let’s say you have a component that was just designed to work with the default `content-box` `box-sizing`. You just wanted to use it and not mess with it.
```css
.component {
  /* designed to work in default box-sizing */
  /* in your page, you could reset it to normal */
  box-sizing: content-box;
}
```
The trouble is, this doesn’t actually reset the entire component. Perhaps there is a `<header>` inside that component that expects to be in a `content-box` world. If this selector is in your CSS, in “the old way” of doing a `box-sizing` reset…
```css
/* This selector is in most "old way" box-sizing resets */
* {
  box-sizing: border-box;
}
```
Then that header isn’t `content-box` as you might expect, it’s `border-box`. Like:
```html
<div class="component"> <!-- I'm content-box -->
  <header> <!-- I'm border-box still -->
  </header>
</div>
```
In order to make that reset easier and more intuitive, you can use the inheriting snippet up at the top there, and the inheriting will be preserved.
**Codepen example** : https://codepen.io/chriscoyier/pen/NWXWPz

### Vendor Prefixes

Every current browser supports `box-sizing: border-box;` unprefixed, so the need for vendor prefixes is fading. But, if you need to support older versions of Safari (< 5.1), Chrome (< 10), and Firefox (< 29), you should include the prefixes `-webkit` and `-moz`, like this:

```css
html {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*, *:before, *:after {
  -webkit-box-sizing: inherit;
  -moz-box-sizing: inherit;
  box-sizing: inherit;
  }
```

Read blog [CSS inheritance: inherit, initial, unset, and revert](https://blog.logrocket.com/css-inheritance-inherit-initial-unset-and-revert/)

# Responsive design
![[Pasted image 20231112150005.png]]

# Css units
## REM

**_Use rem for elements and fonts_**

When sizing fonts, whitespace and elements, consider using rem (root em) instead of px (pixels). When done properly, rem allows us to scale the user interface (UI) based on font size of the root element.

In most cases:

1 rem = 16 px

## EM

**_Use em for media queries_**

em is proven to be more suitable for media queries than rem and px:
```css
@media only screen and (max-width: **30em**) {}
```

## PX
Use px for things that need to be pixel perfect.

px is still useful in many cases. For example, when defining size of an image or video element that needs to be presented in its native resolution.
### Absolute length values

Examples of absolute length values are: `px` (which is 1/96th of an inch), `in` (an inch) or `cm` (which is 37.8px or 25.2/64in). You can find more information about these values in the [MDN](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units).

When you use these length values you can be sure that they will always be more or less the same size. This is especially useful when you know the exact dimensions of the output, which is mostly with print layouts. But it's not so useful when this is not the case, like with all the different screen sizes out there.

And don't forget the possible different browser settings people use, either because of preferences or accessibility needs.

### Relative length values

Relative length values are defined in terms of some other value. These are, for example, `REM`, `EM`, and `vw`. We are going to discuss `REM` in detail below, so lets discuss the others briefly.

`EM` is defined relative to:

- the font size of the parent element when the property `font-size` is concerned, and
- the font size of the element itself when we're dealing with other properties like `height`.

`vw` stands for 1% viewport width. That is to say that if you define the `width` property as 10vw, the element will take up 10% of the available viewport's width. There are many more, and you can find them [here](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units).

These relative length values have a clear advantage above the absolute ones, because they can help make your website responsive. That is to say, your website automatically adapts to the size of the available screen size, doing so in a predictable way.

## Root EM and Root Font Size

REM is defined relative to the font size of the root element. The root element is matched by the `:root` pseudo-class or the `html` selector.

`1rem` therefore takes on the value which is given to the `font-size` of the root element. This means that 1 REM keeps the same value throughout your whole CSS code. If the root element's font size is not changed by the user this value is normally `16px`.

Here's an example:

```css
html {
	font-size: 18px; // default value would be 16
}

h1 {
 	font-size: 2rem; // 2 * 18px = 36px;
}
```

Reasoning backwards from `2rem` to `px` is not a hard task. But do you need to keep a calculator nearby to know the exact font size of your sub-heading which you set to 1.125rem (that's: 16 * 1.125: `18px`)?

Thankfully there is a clever way of dealing with this problem. Keeping in mind that you can also specify the font size of the root element with a percentage (%), developers have found that 62.5% of the default value of the root element equals `10px`. This simplifies things really nicely:
```css
html {
	font-size: 62,5%; // 16px * 0.625 = 10px;
}

h1 {
	font-size: 1.8rem; // 10px * 1.8 = 18px;
}
```
You can check this code out [here](https://codepen.io/slimattcode/pen/jOaJrjZ?editors=0100) on CodePen. Change the size of your view port to see how the layout changes.

One thing that might stand out to you in the code above is that the value of  `1rem` in the defined media queries is always `16px`.  `1rem` inside the media query blocks follows the root definition of `font-size` of 62.5% of `16px`, which is `10px` as we found earlier.

#TODO 
- Flex
- Grid
- Trick to add border inside (inset box-shadow)
- css transition property
- 