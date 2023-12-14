HTML tags do include a few minimal styles. For example, here are the built-in styles for `<a>` tags, in Chrome 86:
```css
a {
  color: -webkit-link;
  cursor: pointer;
  text-decoration: underline;
}
```
These styles are part of the _user-agent stylesheet_. Each browser includes their own stylesheet full of base styles like this. There are some hard rules in the HTML specification, but for the most part, each browser comes up with its own default styles. That's why focus rings look so different across browsers!
In the past, it was common to use a [[01-Global Styles|CSS reset]], to strip away many of these default user-agent styles. These days, though, browsers are a bit more consistent in how they render elements, and there's a growing awareness that we shouldn't expect our sites/applications to be _identical_ across browsers and devices.

_certain_ CSS properties _inherit_. When I apply a `color` to an element, that value gets passed down to all children and grand-children.

Not all CSS properties are inheritable, though. Let's look at example
```css
<style>
  p {
    border: 1px solid hotpink;
  }
</style>
<p>
  I know <em>you</em> are, but what am I?
</p>
```
It's a similar situation, but instead of applying a pink text color, we apply a pink border.

Notice that the `border` value _doesn't_ get passed down to the `em`. We still only have 1 border, and it's around the entire paragraph.

If we explicitly add the same `border` value to both paragraphs _and_ emphasis tags, we see a second border within our paragraph:
```css
<style>
  p, em {
    border: 1px solid hotpink;
  }
</style>
<p>
  I know <em>you</em> are, but what am I?
</p>
```
If you've worked with CSS for a while, this behaviour probably isn't surprising to you, but it's a bit weird when you think about it!

The people who wrote the CSS spec opted to make certain properties inheritable for convenience. It's a DX? thing. It would be super annoying if we had to keep re-applying the same text color styles to every child and grand-child of a container.
Most of the properties that inherit are typography-related, like `color`, `font-size`, `text-shadow`, and so on. You can find a more-or-less complete [list of inheritable properties](https://www.sitepoint.com/css-inheritance-introduction/#list-css-properties-inherit) on SitePoint.

### Forcing inheritance

Occasionally, you may wish to have a property inherit even when it wouldn't normally do so.

A good example is link colors. By default, anchor tags have built-in styles that give unvisited, inactive links a blue hue
As we saw earlier, these are the “built-in” styles for `<a>` tags:
```css
a {
color: -webkit-link;
cursor: pointer;
text-decoration: underline;
}
```
The trouble is that even though `color` is an inheritable property, **it's being overwritten by the default style**, `color: -webkit-link`?.

We can fix this by explicitly telling anchor tags to inherit their containing text color:
```css
<style>
  a {
    color: inherit;
  }
</style>

<p>
  This paragraph contains <a href="#">a hyperlink</a>!
</p>
<p style="color: red;">
  This is a red paragraph with <a href="#">another link</a>.
</p>
```
# The Cascade

Consider the following bit of CSS and HTML:
```css
<style>
  p {
    font-weight: bold;
    color: hsl(0deg 0% 10%);
  }

  .introduction {
    color: violet;
  }
</style>

<p class="introduction">
  Hello world
</p>
```
We've created two rules, one targeting a tag (`p`), another targeting a class (`introduction`). Then, we've created an HTML element that matches them both.

You may already know what happens here: we wind up with a bold, violet paragraph. It plucks the `font-weight` declaration from the `p` tag, and the `color` declaration from the `.introduction` class.

This example shows the browser's _cascade algorithm_ at work.

When the browser needs to display our introduction paragraph on the screen, it first needs to figure out which declarations apply to it. And before it can do that, it needs to collect a set of matching rules. Once it has a list of applicable rules, it works out any conflicts. I imagine this as a sort of deathmatch: if multiple selectors each apply the same property, it pits them against each other. Two fighters enter, but only one emerges.

That's the main idea. The browser will take a set of applicable style rules, and whittle it down to a list of specific declarations that are applicable.

How does it determine which rules win each battle? It depends on the _specificity_ of the selector.

The CSS language includes many different selectors, and each selector has a relative power. For example, classes are "more specific" than tags, so if there is a conflict between a class and a tag, the class wins. IDs, however, are more specific than classes.

## Similarities with JS merging

Here's a fun thought experiment: how might we implement the cascade in JavaScript?

It turns out, JS has the perfect tool for the job: **[spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax).**

In principle, the cascade algorithm works something like this:

```css
const appliedStyles = {
...inheritedStyles,
...tagStyles,
...classStyles,
...idStyles,
...inlineStyles,
...importantStyles
}
```
In our earlier example, we saw this CSS snippet:
```css
p {
  font-weight: bold;
  color: hsl(0deg 0% 10%);
}

.introduction {
  color: violet;
}
```
This could be written in javascript as :
```css
const tagStyles = {
  fontWeight: 'bold',
  color: 'hsl(0deg 0% 10%)',
};
const classStyles = {
  color: 'violet',
}

const appliedStyles = {
  ...tagStyles,
  ...classStyles,
}
```
The order that they're merged in is determined by _specificity_; class styles are more specific than tag styles, so they're merged in later. This way, they overwrite any conflicting styles. All non-conflicting styles are kept.

**Relevance in modern application development(info)**

CSS specificity gets pretty tricky pretty quickly when you dive below the surface. For example, if both of the following selectors match a button, which one has higher specificity?

- `.form > button#submit`
- `#about-page button:last-of-type`?

You can calculate it by adding up the tags, classes, and IDs, but honestly, **I don't think you need to know this stuff anymore.**

This is a _controversial opinion_, but if you work with a component-based framework like React, you shouldn't ever have selectors like this.

With the methodology we'll use in this course, styles are tied to components. We won't have gargantuan selectors reaching across an application. All of our styles will be colocated in one place, and _components_ will be the mechanism of reuse, not classes.

I worked at [Khan Academy](https://www.khanacademy.org/), which was the first major non-Facebook application to use React. The codebase has been worked on by dozens and dozens of engineers since 2013! It's an _enormous_, complicated codebase. By far the most complex codebase I've worked on.

I mention it because it uses a component-based styling solution, and specificity issues **never came up.** Trust me when I say that if you follow the guidelines in this course, specificity wars will not be a problem for you.

Because of that, this course will spend much less time on the cascade than most other resources. Instead, we'll learn how to effectively use modern tooling and methodologies to solve problems for us.

We'll dig much deeper into this topic in [Module 3](https://courses.joshwcomeau.com/css-for-js/03-components).

If you do wish to go deeper into the cascade, I highly recommend this [lovely interactive article by Amelia Wattenberger](https://wattenberger.com/blog/css-cascade).

# Block and Inline Directions

The web was built for displaying inter-linked documents. A lot of CSS mechanics and terminology are inherited from the print world.

Let's take a written sheet of paper as an example:

English is a left-to-right language, meaning that the words are placed side-by-side, from left to right. Individual words are combined into _blocks_, like headings and paragraphs.

Pages are constructed out of blocks, placed one on top of the other. When a new paragraph is added to the page, it's inserted below the previous block element.

In other words, English documents have two "directions": the page consists of vertically-oriented blocks, made up of horizontally-oriented words:
CSS builds its sense of direction based on this system. It has a block direction (vertical), and an inline direction (horizontal).

Here's an easy way to remember the directions, for horizontal languages:

- Block direction is like lego blocks: they stack together one on top of the other.
- Inline direction is like people standing **in-line**; they stand side by side, not one on top of the other.
You can learn more about different writing modes in this [wonderful article by Jen Simmons](https://24ways.org/2016/css-writing-modes/).

## Logical properties

Earlier, we learned about ["built-in" styles](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/01-built-ins-and-inheritance) — these are the rules that each browser comes with out-of-the-box, defined in the user-agent stylesheet.

Here are the built-in styles for `p` tags, in Chrome:
p {
  display: block;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
}
You may not have seen `margin-block-start` before, but can you figure out what it means from context? Can you figure out why Chrome chose to use these properties, instead of a standard `margin` property?

These properties are equivalent to the 4 cardinal directions: `margin-top`, `margin-bottom`, `margin-left`, and `margin-right`.

`margin-block` refers to the vertical axis. `margin-block-start` refers to the top, since block elements are stacked top-to-bottom. Similarly, `margin-inline-start` refers to the left edge, since "inline" is the horizontal direction, and words are placed left-to-right.

Why use these alternatives? Because not all languages are left-to-right, top-to-bottom. If you were to switch your browser's language to Arabic, `margin-inline-start` would add spacing to the right instead of to the left, since Arabic is a right-to-left language.

These alternatives are known as _logical properties_. It's not just margin: there are logical variants for padding, border, and overflow as well.

There are still a few kinks around some of the shorthand variants (eg. `margin-block` instead of `margin-block-start`), but the properties we've seen are [supported in all major browsers](https://caniuse.com/css-logical-props).

Learn more about [logical properties on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties).

>Note that we're speaking purely in terms of _directions_ at this point. It's no coincidence that the `display` property can be set to `block` and `inline`, but _we're not actually talking about those values yet_; for now, the important takeaway is that content is structured along a block axis and an inline axis, just like a real-world document.

### When should we use logical properties?

Logical properties are intended to _entirely replace_ their conventional alternatives. In the future, we might all write `margin-inline-start` instead of `margin-left`!

That said, it's hard to overcome inertia. I'll be honest, I still reach for `margin-left` out of habit. 😅

The main selling point for logical properties is _internationalization_. If you want your product to be available in a left-to-right language like English _and_ a right-to-left language like Arabic, you can save yourself a lot of trouble by using logical properties.

The main argument against using logical properties is browser support. Now, to be clear, browser support for logical properties is [very good](https://caniuse.com/css-logical-props)—at the time of writing, 98% of devices support them. But there are some noticeable gaps, including Internet Explorer 10 and 11, Opera Mini, and relatively-recent versions of Safari.

In this course, we'll primary use conventional properties like `margin-left`, but if you're starting a new project, I'd encourage you to give logical properties a shot!
# The Box Model

The most common CSS-related job-interview question is probably this:

> Can you explain the box model?

It's the CSS version of "what is a closure?", or "what's the difference between classical and prototypal inheritance?".

Because it's such a common question, you may have read about it when prepping for job interviews, or maybe it was taught to you at a bootcamp. Typically, though, the answer given is quite shallow, and glosses over a lot of details. This is unfortunate, since the Box Model is a critical part of CSS' rendering model!

Over the next few lessons, we'll go a bit deeper, and learn about how the browser uses the box model to dictate layout.

## Winter Layers

The four aspects that make up the box model are:
1. Content
2. Padding
3. Border
4. Margin
A helpful analogy is to imagine a person out for a winter walk, wearing a big poofy coat:

- The _content_ is the person themselves, the human being inside the coat.
- The _padding_ is the polyester stuffing in the coat. The more stuffing there is, the more poofed-up the coat will be, and the more space the person will take up.
- The _border_ is the material of the coat. It has a thickness and a color, and it affects the person's appearance.
- The _margin_ is the person's “personal space”. As we've learned in recent years, it's good to have 2 meters (6 feet) of space around us.
## Box Sizing

When we say that an element should have a `width` of `100%`, what does that actually mean?

It turns out, the browser might have a slightly different interpretation than you do. Let's explore.

These aspects affect the size of the element. The code snippet below will draw a black rectangle on the screen (due to the border). What are the dimensions of that rectangle?

```
<style>
  section {
    width: 500px;
  }
  .box {
    width: 100%;
    padding: 20px;
    border: 4px solid;
  }
</style>

<section>
  <div class="box"></div>
</section>
```
> The answer we were looking for is `548px × 48px` ((500+20+20+4+4) * (20+20+4+4))
> horizontal * vertical

Keep reading for a thorough explanation!
When we set our `.box` to have `width: 100%`, we're saying that the box's _content size_ should be equal to the available space, `500px`. The padding and border is _added on top_.

Our box winds up being 548px wide because it adds 20px of padding and 4px of border to each side: `500 + 20 * 2 + 4 * 2`. 
The same thing happens with height: because the element is empty, it has a content size of 0px, with the same border and padding added on top.
![[Pasted image 20231210183906.png]]
This behaviour is surprising, and generally not what we want as developers! Thankfully, browsers provide an escape hatch.

The `box-sizing` CSS property allows us to change the rules for size calculations. The default value (`content-box`) only takes the inner content into account, but it offers an alternative value: `border-box`.

With `box-sizing: border-box`, things behave **much** more intuitively.
### A new default

Instead of having to remember to swap box-sizing on every layout element, we can set it as the default value for _all_ elements with this handy CSS snippet:
```css
*,
*::before,
*::after {
  box-sizing: border-box;
}
```

**Why the pseudo-elements?(info)**

You might be wondering: why do we need to add `*::before` and `*::after`? Shouldn't the wildcard selector (`*`) select _everything_?

Well, yes and no. The `*` selector will select all _elements_, but `::before` and `::after` aren't considered elements. They're _pseudo_-elements. And so we need to select them explicitly.

This is the very first rule in my [[01-Global Styles#1. Box-sizing model|custom CSS reset]], and arguably the most important. Everything is just so much more intuitive with this box-sizing model !
# Padding
A helpful way to think about padding is that it's "inner space".
Imagine that you add a background color to an element with some padding:
```css
.some-fella {
padding: 48px;
background-color: tomato;
}
```
Because padding is on the inside, the padded area also receives the background color:
![[Pasted image 20231210190601.png]]
Padding can be set for all directions at once, or it can be specified for individual directions:
```css
.even-padding {
  padding: 20px;
}
.asymmetric-padding {
  padding-top: 20px;
  padding-bottom: 40px;
  padding-left: 60px;
  padding-right: 80px;
}
/* The same thing, but using ✨ logical properties ✨ */
.asymmetric-logical-padding {
  padding-block-start: 20px;
  padding-block-end: 40px;
  padding-inline-start: 60px;
  padding-inline-end: 80px;
}
```
## Units

When applying padding, we can pick from a pretty wide range of units. The most common ones are:
- `px`
- `em`
- `rem`
Many developers believe that pixels are bad for accessibility. This is true when it comes to _font size_, but I actually think pixels are the best unit to use for padding (and other box model properties like margin/border). watch video for more explanation on why using px is better for margins
```css
<style>
  header {
    font-size: 2rem;
    padding: 32px;
    background-color: peachpuff;
  }
  main {
    background: silver;
    padding: 32px;
  }
</style>

<header>
  My App
</header>
<main>
  <p>
    These are some words you might find on a web application.
    They are indeed words, and nobody can refute that.
  </p>
</main>
```
**Padding percentages(warning)**

Can we use percentages for padding, like this?
```css
.box {
padding-top: 25%;
}
```
We _can_, but the result is surprising and counter-intuitive; **percentages are always calculated based on the element's available width.** This is true for left/right padding, and even for top/bottom padding!
```css
<style>
  .box {
    border: 2px solid;
    padding-top: 25%;
    background-color: pink;
  }
</style>
<div class="box">
<p>Hello World</p>
</div>
```

Try resizing the tab, and notice how the box grows and shrinks. This is because the top padding is equal to 25% of the available horizontal space, based on how wide the parent element is.

For a while, this quirky behavior was actually useful in certain situations, when we wanted to preserve a specific aspect ratio. We'll learn more about this [in Module 6](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/16-aspect-ratio).

## Shorthand properties
The `padding` property has a couple tricks up its sleeve. It can be used to set asymmetric padding, in a few different ways.
```css
.two-way-padding {
  padding: 15px 30px;
}

.asymmetric-padding {
  padding: 10px 20px 30px 40px;
}
```
If two values are passed, the first value is used for both vertical directions (top/bottom), and the second value is used for horizontal directions (left/right).

If all 4 values are passed, it applies them in a specific order: top, right, bottom, left.

The easiest way to remember this order is to picture a clock. We start at the top (12:00), and go clockwise for the remaining values:

When fewer than 4 values are passed, it "fills in the gaps". If you pass it two values, it mirrors the top to the bottom, and the right to the left. With only 3 values, we set top/right/bottom explicitly, and mirror the right value to the left.

**Beyond padding(info)**

This pattern is shared amongst other CSS properties that have shorthand values. For example:
- margin (`margin: 10px 20px 30px 40px`)
- border-style (`border-style: dotted solid dashed solid`)

A similar pattern is used for properties that affect corners, like `border-radius`; the pattern is `top-left`, `top-right`, `bottom-right`, `bottom-left`. It follows a clockwise pattern starting from the top-left.
## Overwriting values

Let's say we want to produce an element with only 3 padded sides:
We could do this with our shorthand property:
```css
.box {
padding: 48px 48px 0;
}
```
There is another way to represent the same intent, which is arguably clearer:
```css
.box {
padding: 48px;
padding-bottom: 0;
}
```
"Long-form" properties can _overwrite_ the relevant value in shorthand properties. The effect is the same, but it's a bit more semantic; instead of a random string of numbers, we're declaring that we want 48px of padding, hold the bottom.

**Please note:** the order matters! The overwrite has to come _after_ the shorthand, otherwise it won't have any effect.
```css
.box {
  /*
    🙅‍♀️ because `padding-bottom` comes first,
    it will be overwritten by the shorthand.
  */
  padding-bottom: 0;
  padding: 48px;
}
```
`padding-block` refers to the top and bottom (in top-down left-to-right languages like English). `padding-inline` refers to the left and right. `padding-inline-start` refers to the left.
```
padding-block: 20px;
padding-inline: 10px;
padding-inline-start: 0px;
```
# Border

Border is a bit of an odd duck in the trinity of padding/border/margin—unlike the other two, it has a visual/cosmetic component.
There are three styles specific to border:

- Border width (eg. `3px`, `1em`)
- Border style (eg. `solid`, `dotted`)
- Border color (eg. `hotpink`, `black`)
They can be combined into a shorthand:
```css
.not-good {
/* 🙅‍♀️ Won't work – needs a style! */
border: 2px pink;
}

.good {
/* 🙆‍♀️ Will produce a black, 3px-thick border */
border: solid;
}
```
The only required field is `border-style`. Without it, no border will be shown!
**Here's a fun fact:** If we _don't_ specify a border color, it'll default to using the element's text color! Check it out:
```css
<style>
  .box {
    width: 200px;
    padding: 24px;
    font-weight: bold;
    /* No border color specified: */
    border: 4px solid;
  }
  .box.one {
    /* Specify the *text* color: */
    color: hotpink;
  }
  
  .box.two {
    color: slateblue;
  }
</style>

<div class="box one">One</div>
<div class="box two">Two</div>
<div class="box three">Three</div>
```
If you want to specify this behaviour explicitly, it can be done with the special `currentColor` keyword.

`currentColor` is always a reference to the element's derived text color (whether set explicitly or inherited), and it can be used anywhere a color might be used:
```css
.box {
color: hotpink;
border: 1px solid currentColor;
box-shadow: 2px 2px 2px currentColor;
}
```
## Border radius

The CSSWG? has published a [list of mistakes](https://wiki.csswg.org/ideas/mistakes) they've made with the CSS language. One of these mistakes is listed:

> border-radius should have been corner-radius.

It's not hard to understand the rationale; the `border-radius` property rounds an element even if it has no border
Like `padding`, `border-radius` accepts discrete values for each direction. Unlike `padding`, it's focused on specific _corners_, not specific sides. Here are some examples:
```css
<style>
  .box {
    width: 100px;
    height: 100px;
    border: 4px solid hotpink;
    border-radius: 10px 10px 40px 40px;
  }
</style>

<div class="box"></div>
```
`individual propeprties`
```css
<style>
  .box {
    width: 100px;
    height: 100px;
    border: 4px solid hotpink;
    border-top-left-radius: 8px;
    border-top-right-radius: 16px;
    border-bottom-right-radius: 32px;
    border-bottom-left-radius: 64px;
  }
</style>

<div class="box"></div>
```
You can also use percentages; 50% will turn your shape into a circle or oval, since each corner's radius is 50% of the total width/height:

```css
<style>
  .box {
    width: 100px;
    height: 100px;
    border: 4px solid hotpink;
    border-radius: 50%;
  }
</style>

<div class="box"></div>
```

`border-radius` can do some funky and wild stuff, and we'll learn more about it later
## Border vs. Outline

A common stumbling block for devs is the distinction between `outline` and `border`. In some respects, they're quite similar! They both add a visual edge to a given element.
The core difference is that _outline doesn't affect layout_. Outline is kinda more like box-shadow; it's a cosmetic effect draped over an element, without nudging it around, or changing its size.

Outlines share many of the same properties:

- `border-width` becomes `outline-width`
- `border-color` becomes `outline-color`
- `border-style` becomes `outline-style`
Outlines are stacked outside border, and can sometimes be used as a "second border", for effect:
```css
<style>
  .box {
    width: 100px;
    height: 100px;
    border: 4px solid darkviolet;
    outline: 4px solid deeppink;
  }
</style>

<div class="box"></div>
```
A couple more quick tidbits about outlines:

- Outlines will follow the curve set with `border-radius` in all modern browsers. This is a relatively recent change, which landed in browsers between 2021 and 2023.
    
- **Outlines have a special `outline-offset` property**. It allows you to add a bit of a gap between the element and its outline.

**One more thing:** Outlines are sometimes used as focus indicators, for folks who use the keyboard (or other non-pointer devices) to navigate.

We'll learn all about focus outlines [later in the course](https://courses.joshwcomeau.com/css-for-js/09-little-big-details/11.01-focus-visible). In the meantime, you should avoid tweaking outlines on interactive elements like buttons or links.

# Margin

Finally, the third in our trinity: _margin_. Margin increases the space _around_ an element, giving it some breathing room. As we saw earlier, margin is "personal space".

In some ways, margin is the most amorphous and mysterious. It can do wacky things, like pull an element outside a parent, or center itself within its container.

Let's see if we can shed some light on this wily property!

```css
.individually-specified-box {
  margin-top: 10px;
  margin-left: 20px;
  margin-right: 30px;
  margin-bottom: 40px;
}
.logical-box {
  margin-block-start: 20px;
  margin-block-end: 40px;
  margin-inline-start: 60px;
  margin-inline-end: 80px;
}
```
## Negative margin

With padding and border, only positive numbers (including 0) are supported. With margin, however, we can drop into the negatives.

A negative margin can pull an element outside its parent:
```css
<style>
main {
  width: 200px;
  height: 200px;
  border: 3px solid;
}

.box {
  width: 50%;
  height: 50%;
  background: white;
}
.pink.box {
  border: 3px solid deeppink;
}
  .pink.box {
    margin-top: -32px;
    margin-left: -32px;
  }
</style>
<main>
  <div class="pink box"></div>
</main>
```
Negative margins can also pull an element's sibling closer:
```css
<style>
  .pink.box {
    margin-bottom: -32px;
  }
  .neighbor {
    margin-left: 16px;
  }
  main {
  width: 200px;
  height: 200px;
  border: 3px solid;
}

.box {
  width: 50%;
  height: 50%;
  background: white;
}
.pink.box {
  border: 3px solid deeppink;
}

.neighbor {
  width: 50%;
  height: 50%;
  background: silver;
}
</style>
<main>
  <div class="pink box"></div>
  <div class="neighbor"></div>
</main>
```
Interesting, right? The top `.pink.box` has a negative _bottom_ margin, and the result is that its sibling is _pulled up_, and overlaps the pink box.

It's easy to fall into the trap of thinking that margin is exclusively about changing the selected element's position. Really, though, it's about changing _the gap between elements_. Negative margin shrinks the gap below an element, causing the next element to scoot up closer.

Finally, negative margin can affect the position of _all siblings_. Check out what happens when we apply negative margin to the _first box_ in a series:
```css
<style>
  .lifted.box {
    border-color: deeppink;
    margin-top: -24px;
  }
  main {
  width: 200px;
  height: 200px;
  border: 3px solid silver;
}

.box {
  width: 25%;
  height: 25%;
  border: 3px solid;
  background: white;
}
</style>

<main>
  <div class="lifted box"></div>
  <div class="box"></div>
  <div class="box"></div>
</main>
```
The interesting thing is those two black boxes: **they "follow" the deep pink box up.**

When we use margin to tweak an element's position, we might also be tweaking every subsequent element as well. This is different from other methods of shifting an element's position, like using `transform: translate` (which we'll cover later on).

If you're keen to learn more about the intricacies of negative margin, check out this [in-depth article](http://www.quirksmode.org/blog/archives/2020/02/negative_margin.html) by Peter-Paul Koch.
## Auto margins

Margins have one other trick up their sleeve: they can be used to center a child in a container.

Watch what happens when we set an element's left and right margin to `auto`:
```css
<style>
  .content {
    width: 50%;
    margin-left: auto;
    margin-right: auto;
  }
</style>

<main>
  <section class="content">
    Hello World
  </section>
</main>
```
If we inspect this element in our devtools, we see that the browser has applied an equal amount of margin on either side of the element:
The `auto` value seeks to fill the _maximum available space_. It works the same way for the `width` property, as we'll discover shortly.

When we set both `margin-left` and `margin-right` to `auto`, we're telling them each to take up as much space as possible. Like a game of Hungry Hungry Hippos, both sides try to gobble up all of the free space around the element. They're evenly-matched, though, so neither side wins; they always end in a draw.

If you take the free space around an element and distribute it evenly on both sides, you wind up centering that element. This is a happy byproduct of this mechanism!

Two caveats:
- **This only works for horizontal margin.** Setting top/bottom margin to `auto` is equivalent to setting it to `0px`
- **This only works on elements with an explicit width**. Block elements will naturally grow to fill the available horizontal space, so we need to give our element a `width` in order to center it.
**Outdated?(info)**

You may be wondering if this technique for centering is outdated, now that we have modern layout rendering modes like Flexbox and Grid.

The answer is “no”, but it's a bit nuanced.
Flexbox and Grid are both powerful tools for managing layout, and we'll learn all about them soon. These properties are applied to a container, and affect all children.

The nice thing about the auto-margin trick is that it can be selectively applied to a single child in a container.

For example, let's say we're building a blog. Our article has a bunch of headings and paragraphs and images, and we want them to be laid out normally. But we want pull-quotes to be centered.

We could apply Flexbox or Grid to the parent, but we'd be affecting _all_ of the other stuff in that container. There are some [crafty ways](https://www.joshwcomeau.com/css/full-bleed/) we could work around that with Grid, but it would be a lot of fussing around.

The auto-margin trick can be slapped on to any existing layout, and it works like a charm.

Ultimately, they're different tools, and they're useful in different situations. By learning about them all, you'll never be caught trying to hammer in a screw, or screwing in a nail.
## Exercises

### Thinking outside the box

In Flow layout, elements are stacked neatly into boxes. Things don't overlap by default.

Sometimes, though, we want to pull something a little outside its parent container, for aesthetic effect.

Your mission in this exercise is to reproduce the following effect:
```css
<style>
  body {
    background: #222;
    padding: 32px;
  }

  .card {
    background-color: white;
    padding: 32px;
    border-radius: 8px;
  }

  h1 {
    background: deeppink;
    padding: 16px 32px;
    margin-bottom: 24px;
    /*Un comment below line for solution*/
    /*margin-top:-32px;*/
    font-size: 2rem;
    text-align: center;
    border-radius: 4px;
  }
</style>

<div class="card">
  <h1>An Otter Essay</h1>
  <p>
    Otters have long, slim bodies and relatively short limbs. Their most striking anatomical features are the powerful webbed feet used to swim, and their seal-like abilities holding breath underwater.
  </p>
</div>
```
### Stretched content

Our `.card` element has served us well so far, but now we have a bit of a problem.

Let's say we want to include a picture of an otter, and we want it to stretch out, to fill the available container width:
The container's padding is getting in our way. Update the code to allow for full-width children.

**Feel free to modify the HTML in this one!** This isn't one of those challenges where you mustn't touch the markup.
```css
<style>
  body {
    background: #222;
    padding: 32px;
  }

  .card {
    background-color: white;
    padding: 32px;
    border-radius: 8px;
  }
.stretched-out{
margin-left:-32px;
margin-right:-32px;
}
  img {
    display: block;
    width: 100%;
  }

  p, img {
    margin-bottom: 16px;
  }
</style>

<div class="card">
  <p>
    Otters have long, slim bodies and relatively short limbs. Their most striking anatomical features are the powerful webbed feet used to swim, and their seal-like abilities holding breath underwater.
  </p>
  <div class="stretched-out">
  <img alt="A cute otter in water" src="https://courses.joshwcomeau.com/cfj-mats/otter.jpg" />
  </div>
  <p>
    More importantly, otters are glorious water dogs, playful and curious. The otter, no other, is the best animal.
  </p>
</div>
```

> _solution:_ We added `.stretched-out` class around img and added `nagative` margin to `.stretched-out` class to break padding

**Wait, why do we need a wrapping element here?** I glossed over the explanation pretty quickly in the video, so let me elaborate here!

The default value for the `width` property is `auto`. By default, for _most_ elements, this means “automatically grow to fill as much space as possible”.

Images, as well as other “replaced elements” like `<video>` and `<canvas>`, are special. They don't automatically expand to fill the available space. Instead, they rely on their _intrinsic size_.

For example, suppose I take a photo on an old webcam. That photo has a native size of `640 × 480`. When I embed this image on the page, using an `<img>` tag, it'll have a default width of 640px.

**This is the problem.** `width: auto` has a different meaning for replaced elements. It doesn't mean “stretch out and fill all of the space”, it means “use your natural width”!

If you're still a bit confused, don't worry; we'll cover all of this stuff in greater depth shortly! There's an entire lesson [dedicated to the “width” property](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/10-widths) coming up soon.

# Flow Layout

When it comes to layout, CSS is more like a collection of mini-languages than a single cohesive language.

Every HTML element will have its layout calculated by a layout algorithm. These are known as _“layout modes”_, and there are 7 distinct ones.

We'll cover several layout modes in this course, including Positioned layout, “Flexible Box” layout (AKA Flexbox), and Grid layout (AKA CSS Grid). For now, though, let's focus on _Flow layout_.

Flow layout is the default layout mode. Everything we've seen so far has used Flow layout. A plain HTML document, with no CSS applied, uses Flow layout exclusively.

I like to think of Flow layout as the “Microsoft Word” layout algorithm. It's intended to be used for document type layouts.

There are two main element types in Flow layout:

- **Block elements:** things like headings, paragraphs, footers, asides. The chunks of content that make up a page.
- **Inline elements:** things like links, or a string of bold text. Generally, inline elements are meant to highlight bits of text, or elements within a block container.
Each HTML tag has a default type. `<div>` and `<header>` are block elements, `span` and `<a>` are inline elements.

We can toggle any particular element with the `display` property:
```css
/* Transform a particular <a> tag from `inline` to `block`: */
a.nav-link {
display: block;
}
```
It's no coincidence that `block` and `inline` align with the directions we were speaking about earlier. In flow layout, block elements stack in the block direction, and inline elements stack in the inline direction.

It's more than just direction, though. Each `display` value comes with its own behaviour, its own rules. Let's look at them in turn:
## Inline elements don't want to make a fuss

If you've ever tried to adjust the positioning or size of an inline element, you've likely been confounded by the fact that a bunch of CSS properties just don't work.

For example, this snippet will have no effect:
```css
strong {
height: 2em;
}
```
You can picture inline elements as go-with-the-flow-type folks. They don't want to inconvenience anyone by pushing any boundaries. They're like polite dinner-party guests who sit exactly where they're assigned.

You _can_ shift things in the inline direction with `margin-left` and `margin-right`, since that pushes it around in the _inline_ direction, but you can't give it a `width` or `height`. When it comes to layout, an inline element is where it is, and there's not much we can do about it.

>**Replaced elements(info)**
>
>There's an exception to this rule: _replaced elements_.
>
 A replaced element is one that embeds a "foreign" object. This includes:
>
> - `<img />`
> -  `<video />`
> - `<canvas />`
> 
 These elements are all technically inline, but they're special: they _can_ affect block layout. You can give them explicit dimensions, or add some `margin-top`.
>
 How do we reconcile this? I have a trick. I like to pretend that it's a foreign object within an inline wrapper. When you pass it a width or height, you're applying those properties _to the foreign object_. The inline wrapper still goes with the flow.

## Block elements don't share

When you place a block level element on the page, its content box greedily expands to fill the entire available horizontal space.

A heading might only need 150px to contain its letters, but if you put it in an 800px container, it will expand to fill 800px of width.
```css
<style>
  h2 {
    border: 2px dotted;
  }
</style>
<h2>
  Hello World
</h2>
```
What if we force it to shrink down to the minimum size required for the letters? We can do this with the special width keyword `fit-content`
```css
<style>
  h2 {
    width: fit-content;
    border: 2px dotted;
  }
  .box.red {
    width: 50px;
    height: 25px;
    background: red;
  }
</style>
<h2>
  Hello World
</h2>
<div class="box red"></div>
```
Even though there's plenty of space left on that first row, the red box sits underneath our heading. The `h2` does _not_ want to share any inline space.
In other words, elements that are `display: block` will stack in the block direction, regardless of their size.
## Inline elements have “magic space”

In the [[#The Box Model|box model lesson]], we learned about the different ways we can increase space around an element: we can change its content size, we can add padding, we can thicken the border, or increase the margin.

Inline elements are a bit sneaky, though.

Here's an example of an image with a fixed size of 300×300 pixels, sitting in a plain ol' div. Using your browser's devtools, take a look at the image and its div:

_Refer_ : https://courses.joshwcomeau.com/cfj-mats/inline-magic-space.mp4

You'll notice something peculiar… The image is taking up the correct size, 300×300, but the parent has a slightly larger height:

The image is 300px tall, but its parent `<div>` is 306px tall. Where are those extra few pixels coming from?? It's not padding, it's not border, it's not margin…
The reason for this extra “magic space” is that the browser treats inline elements as if they're typography. It makes sense that with text, you'd want a bit of extra space, so that the lines in a paragraph aren't crammed in too tightly.

There are two ways we can fix this problem:
1. Set images to `display: block` — if you're noticing this problem, there's a good chance your images aren't interspersed with text, so setting them to display as blocks makes sense.
2. Set the `line-height` on the wrapping div to `0`:
![[Pasted image 20231211083749.png]]
This space is proportional to the height of each line, so if we reduce the line height to 0, this “magic space” goes away. Because our container doesn't contain any text, this property has no other effect.
### Space between inline elements
There's another unrelated way that inline elements have a bit of extra spacing. Take a look at this example; notice that there are gaps between the 3 images:
```css
<img
  src="https://courses.joshwcomeau.com/cfj-mats/placekitten-100.jpg"
  width="100"
  alt="Cat photo"
/>
<img
  src="https://courses.joshwcomeau.com/cfj-mats/placekitten-100.jpg"
  width="100"
  alt="Cat photo"
/>
<img
  src="https://courses.joshwcomeau.com/cfj-mats/placekitten-100.jpg"
  width="100"
  alt="Cat photo"
/>
```
This space is caused by the **whitespace between elements**. If we squish our HTML so that there are no newlines or whitespace characters between images, this problem goes away:
```css
<!--
  This is exactly the same HTML,
  but without any whitespace
-->
<img src="https://courses.joshwcomeau.com/cfj-mats/placekitten-100.jpg" width="100" alt="Cat photo" /><img src="https://courses.joshwcomeau.com/cfj-mats/placekitten-100.jpg" width="100" alt="Cat photo" /><img src="https://courses.joshwcomeau.com/cfj-mats/placekitten-100.jpg" width="100" alt="Cat photo" />
```
This happens because HTML is _space-sensitive_, at least to an extent. The browser can't tell the difference between whitespace added to separate words in a paragraph, and whitespace added to indent our HTML and keep it readable.
How do we solve this problem? Well, it turns out that this issue is specific to Flow layout. Other layout modes, like Flexbox, ignore whitespace altogether. So, the simplest thing is to switch the container to use Flexbox. We'll learn all about Flexbox in [Module 4](https://courses.joshwcomeau.com/css-for-js/04-flexbox/01-hello-world).

## Inline elements can line-wrap
Inline elements have one pretty big trick up their sleeves; they can line-wrap.
This paragraph features a multi-line `<strong>` tag:
>This is a paragraph with **some very bolded words in it**.

Unlike block elements, an inline element can produce shapes other than boxes (With properties like 'border-radius', block-level elements might appear as different shapes, but as far as layout and positioning is concerned, block-level elements are always rectangles.)
. Firefox accurately reports on the situation:
![[Pasted image 20231211084412.png]]
his helps explain why certain CSS properties aren't available for inline elements. What would it even mean to increase the vertical margin on a shape like this?

It's worth noting that it's still considered "one shape". If we add a border, we can see that we don't get 2 discrete rectangles, but rather a single rectangle cut in half and repositioned:
```css
<style>
  strong {
    border: 2px solid;
  }
</style>
<p>
  This is a paragraph with <strong>some very bolded words in it</strong>.
</p>
```
`output`:
![[Pasted image 20231211084436.png]]
**I like to think of it like a sushi roll.** We have one long strip of text, and it's chopped up into individual bite-sized lines before being presented.

## The deal with inline-block
One of the most confusing things about Flow layout is the Frankenstein `display: inline-block` value. Honestly, it took a few tries before I truly understood what it was / how it worked.
**Here's how I've grown to think about it:** An `inline-block` element is a block-level element that can be placed in an inline context. You know the expression _“a wolf in sheep's clothing”_? We can think of `inline-block` as _“a block in inline's clothing”_.

In terms of layout, it's treated as an inline element. We can drop it in the middle of a paragraph, without totally borking the layout. But _internally_, it acts much more like a block element.
Let's look at an example:
```css
<style>
  strong {
    display: inline-block;
    color: white;
    background-color: red;
    width: 100px;
    margin-top: 32px;
    text-align: center;
  }
  strong:hover {
    transform: scale(1.2);
  }
</style>
<p>
  <strong>Warning:</strong> Alpaca may bite.
</p>
```
**Try removing the `display: inline-block` declaration to see the difference.**

In this example, we've set our `<strong>` to be inline-block. Because this tag is now secretly a block-level element, it has access to the _full universe_ of CSS. Usually, properties like `width` and `margin-top` have no effect on an inline element, but they _do_ work on inline-block elements.
We've effectively turned our `strong` element into a block element, as far as _its own_ CSS declarations are concerned. But from the _paragraph's_ perspective, it's an inline element. It lays it out as an inline element, in the inline direction beside the text.

In many ways, `inline-block` allows us to have our cake and eat it too. It's the best of both worlds! It's too good to be true!

Predictably, however, there's a catch.
### Inline-block doesn't line-wrap
It's said that all architects will at some point design a chair. Similarly, many front-end developers will at some point build a flashy link component. On my blog, I used to have this nifty hover effect

_Refer_: https://courses.joshwcomeau.com/cfj-mats/fancy-link-hover-crop.mp4
This effect is only shown on large screens, and only on hover (not focus). Here's a recording, for folks who can't trigger it:

This is a neat effect, but it relies on CSS properties like `clip-path`, properties that don't work with inline elements. In order for this to work, we need to switch to `display: inline-block`.

**Here's the big downside with inline-block:** It disables line-wrapping.
This might not seem like a big tradeoff, but consider what happens when we try to use this on longer-length links:
![[Pasted image 20231211085338.png]]
You may be tempted to pick really-short link text, to avoid this problem, but that would be a mistake; descriptive link text is [important for accessibility](https://www.a11yproject.com/posts/2019-02-15-creating-valid-and-accessible-links/). Therefore, we should only use effects like this when the links aren't part of a paragraph (eg. navigation links).

>**Building this link effect(info)**
>
 If you're curious about how this effect was created, we'll learn how to build a similar effect towards the end of this course (It's an [exercise in Module 9](https://courses.joshwcomeau.com/css-for-js/09-little-big-details/08.04-exercises#rising-nav-link), using the [`clip-path` property](https://courses.joshwcomeau.com/css-for-js/09-little-big-details/08-clip-path)).

# Width Algorithms

In the previous lesson, we learned how block-level elements like `h1` and `p` will expand to fill the available space.

It's easy to assume that this means that they have a default `width` of `100%`, but that wouldn't quite be right.

In the following playground, **try toggling the `width: 100%` declaration in the devtools**, to see how it affects the size of the heading:
```css
<style>
  h1 {
    /* width: 100%; */
    margin: 0 16px;
    background-color: chartreuse;
  }
</style>
<h1>
  Hello World
</h1>
```
When we enable `width: 100%`, we cause the heading to pop outside of our frame. This happens because of the margin.

When we use percentage-based widths, those percentages are **based on the parent element's content space**. If the `body` tag makes 400px of space available, any child with 100% width will become 400px wide, regardless of any other circumstances.

Block elements have a default `width` value of `auto`, not `100%`. `width: auto` works very similar to `margin: auto`; it's a hungry value that will grow as much as it's able to, but no more. In the case above, our `h1` will grow to consume (100% - 32px), since there is 16px of margin on either side.
It's a subtle but important distinction: by default, block elements have _dynamic sizing_. They're context-aware.

## Keyword values

Broadly speaking, there are two kinds of values we can specify for `width`:
1. Measurements (100%, 200px, 5rem)
2. Keywords (auto, fit-content)

Measurement-based values are either completely explicit (eg. 200px), or relative to the parent's available space (eg. 50%). Keywords, on the other hand, let us specify different sorts of behaviours depending on the context.
We've already seen how `auto` will let our element greedily consume the available space while respecting any constraints. Let's look at some of our other options!
### min-content
When we set `width: min-content`, we're specifying that we want our element to become as narrow as it can, _based on the child contents_. This is a totally different perspective: we aren't sizing based on the space made available by the parent, we're sizing based on the element's children!
This value is known as an _intrinsic value_, while measurements and the `auto` keyword are _extrinsic_. The distinction is based on whether we're focusing on the element itself, or the space made available by the element's parent.
```css
<style>
  h1 {
    width: min-content;
    background-color: fuchsia;
  }
</style>
<h1>
  This heading is shrunk down.
</h1>
```
In this case, we wind up with a _very_ narrow heading, because it chooses the smallest possible value for `width` that still contains each word. Whenever it encounters whitespace or a hyphenated word, it'll break it onto a new line.
This value can be useful for certain kinds of effects.
```css
<style>
  h1 {
    width: max-content;
    background-color: mediumspringgreen;
  }
</style>
<h1>
  This heading is constrained using max-content, which causes the line to extend far longer than it otherwise would!
</h1>
```
As you can see, an element with `width: max-content` pays no attention to the constraints set by the parent. It will size the element based purely on the length of its unbroken children.

Why would this be useful? Well, it produces a nice effect when the content is short enough to fit within the parent:
```css
<style>
  h1 {
    width: max-content;
    background-color: mediumspringgreen;
  }
</style>
<h1>A short heading</h1>
```
Unlike with `auto`, `max-content` doesn't fill the available space. If we want to add a background color _only_ around the letters, this would be a neat way to do it!

Of course, our work needs to render correctly across screens of all sizes. We can't assume that the container will always be big enough to contain the heading! Thankfully, one more value is provided by the browser…
### fit-content
If these keywords were bowls of porridge, `fit-content` would be the one that Goldilocks declares "just right".
Here's how it works: like `min-content` and `max-content`, the width is based on the size of the children. If that width can fit within the parent container, it behaves just like `max-content`, not adding any line-breaks.

If the content is too wide to fit in the parent, however, it adds line-breaks as-needed to ensure it never exceeds the available space. It behaves just like `width: auto`.
```css
<style>
  h2 {
    width: fit-content;
    background-color: peachpuff;
    margin-bottom: 16px;
    padding: 8px;
  }
</style>
<h2>Short</h2>
<h2>A mid-length heading</h2>
<h2>The longest heading you've ever seen in your life, will it ever end, ahhhhh ohmigod 😬😬😬😬😬😬😬</h2>
```
## Min and max widths

We can add constraints to an element's size using `min-width` and `max-width`.
```css
<style>
  .box {
    width: 50%;
    min-width: 170px;
    max-width: 300px;
    margin: 0 auto;
    border: solid hotpink;
  }
</style>

<div class="box">
  Hello World
</div>
```
Try resizing this result to see how the box changes size!

The particularly exciting thing about `min-width` and `max-width` is that they let us _mix units_. We can specify constraints in pixels, but set a percentage `width`.

We'll explore these ideas much more in Module 5.
## A thought experiment
`fit-content` is a really cool new value, but does it offer truly unique functionality? Can it be replicated using other less-shiny CSS properties?

Take a few minutes and think about it. Play around and see if you can replicate the effect without using `fit-content`
> For different approaches and their pitfalls refer [video](https://player.vimeo.com/video/488245059)

So far, two solutions have been found 😄 Expand below to see them:
The first solution uses a somewhat-obscure `display` value:
```css
h2 {
display: table;
}
```
`display: table` causes elements to render using _Table layout_. This is the layout mode used by the `<table>` HTML tag. It's an alternative layout algorithm to flow layout or positioned layout.

By default, tables will shrink to hold their contents, but are still block-level elements. This is exactly what we want in this case, though it is a bit of a hack; a table element expects to have table rows as children, not text.

In the old days, table layouts were used for just about everything. Nowadays, Flexbox and Grid are better solutions in most situations.We won't be covering table layouts in this course.
>The exceptions are: displaying tabular data, and creating HTML/CSS emails, since many email clients don't support modern CSS.

The next solution uses `min-content` and `max-content` to recreate `fit-content`:
```css
h2 {
min-width: min-content;
max-width: max-content;
}
```
Here's how this works:

- We haven't changed the `width` property, and so it will remain at `auto`. Because h2 is a block-level element, it will grow and shrink to fit the parent container.
    
- But, it can't grow above its `max-width`, which is equal to `max-content`. If our h2 only has a few characters, this might be a really small value, like 100px. By setting this value as `max-width`, we clamp the element so that it can't expand to fill the parent container.
    
- What if there's enough content to fill the parent container? For example, suppose we have 1000px worth of content in a 500px box… Well, **`max-width` doesn't have any effect in this case.** Our element grows to fill the container (thanks to `width: auto`), and this total width is 500px, well below the 1000px limit set using `max-width`.
    

`min-width: min-content` is necessary because of an edge-case: if our content has long, unbreakable words in a narrow container:

```css
<style>
  .narrow-wrapper {
    width: 100px;
    border: 2px solid;
  }
  .fit {
    width: fit-content;
  }
  .max {
    max-width: max-content;
    /* Enable this line to see the difference: */
    /* min-width: min-content; */
  }
  h2 {
    background-color: peachpuff;
    margin-bottom: 16px;
    padding: 8px;
  }
</style>

<div class="narrow-wrapper">
  <h2 class="fit">
    Antidisestablishmentarianism
  </h2>
  <h2 class="max">
    Antidisestablishmentarianism
  </h2>
</div>
```
**This stuff is really complicated.** If you're feeling confused, or overwhelmed, please know that I don't expect you to be able to make sense of this stuff at this point!

In fact, to fully understand this solution, you'll need to know about line-wrapping (discussed in [Module 6](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/03-text-overflow)), overflow (discussed in [Module 2](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/14-overflow)), and minimum content size (discussed in [Module 4](https://courses.joshwcomeau.com/css-for-js/04-flexbox/04-grow-shrink-basis)).

It might be worth bookmarking this lesson, and coming back to it once you're near the end of the course. I suspect you'll have a much easier time making sense of what's going on here!
`Exercise`
### Max Width Wrapper

Frequently, I'll find myself in situations where I want to constrain an element to sit in a centered column, like this:
demo video: https://courses.joshwcomeau.com/cfj-mats/max-width-wrapper-demo.mp4
In this exercise, we'll build a generic utility class that we can drop in to solve this problem wherever we encounter it.

Specifically, our goal with a max-width wrapper is to fulfill these constraints:
- It fills the available space on smaller viewports.
- It sets a maximum width, and will horizontally center itself within the parent if there is leftover space.
- It includes a bit of horizontal “breathing room”, so that its children aren't pressed right up against the edges of the viewport.

```css
<!--
Create a “max-width-wrapper” utility.

• Should have a max-width of 350px
• Should have 16px of “breathing room” on
  smaller screens.
• HINT: Some HTML changes might be necessary.
  Feel free to tweak the markup.
-->

<style>
  /* TODO */
  p{
    max-width:350px
  }
  /* Cosmetic styles */
body {
  background: #222;
  padding: 0px;
  padding-top: 32px;
}

.card {
  background-color: white;
  padding: 32px;
  border-radius: 8px;
}

p {
  margin-bottom: 16px;
}
</style>

<div class="card">
  <p>
    Otters have long, slim bodies and relatively short limbs. Their most striking anatomical features are the powerful webbed feet used to swim, and their seal-like abilities holding breath underwater.
  </p>
</div>
```
Solution
```css
<style>
  .max-width-wrapper {
    max-width: 350px;
    margin-left: auto;
    margin-right: auto;
    padding-left: 16px;
    padding-right: 16px;
  }
</style>

<div class="max-width-wrapper">
  <div class="card">
    <p>
      Otters have long, slim bodies and relatively short limbs. Their
      most striking anatomical features are the powerful webbed feet
      used to swim, and their seal-like abilities holding breath
      underwater.
    </p>
  </div>
</div>
```
In the solution code above, our `.max-width-wrapper` class has a max-width of 350px, and then we're applying 16px of padding on each side. This means that the card itself can only ever be 318px wide:
This is because of the [“border-box” box sizing](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/04-the-box-model#box-sizing). The 350px width we've set _includes_ the border + padding.

This might _seem_ like a problem, but honestly, I'm not worried about it 😄. In a realistic scenario, we'd probably want to adjust this max-width value based on the content anyway. I chose 350px because it displays nicely in this course platform.

Some students have thought to switch the `box-sizing` to `content-box`, so that the 350px width is applied to the _inner_ content size. This does indeed ensure that our card will be able to expand to 350px, but in my opinion, that's not a trade worth making. Switching `box-sizing` values between elements is a recipe for confusion.
### Figures and captions
The `<figure>` HTML element is fairly niche, but super useful. It allows us to display any sort of “non-typical” content: images, videos, code snippets, widgets, etc. It also lets us caption that content with `<figcaption>`.
example :
```css
<figure>
  <img
    src="/graph.jpg"
    alt="A bar graph showing the number of cats per capita"
  />
  <figcaption>
    Source: Cat Scientists Ltd.
  </figcaption>
</figure>
```
`<figure>` elements are block-level elements, which means they fill the available horizontal space. But what if we wanted them to shrink to wrap around the image inside?
Different figures will need to be different sizes, based on the widths of the images inside. Therefore, your solution shouldn't "hardcode" any pixel values.

Give it a shot:
```css
<style>
  figure {
    padding: 8px;
    border: 1px solid;
    margin-bottom: 32px;
  }

  figure img {
    margin-bottom: 8px;
  }

  figcaption {
    text-align: center;
    color: #666666;
  }
</style>

<figure>
  <img
    alt="A hallway with rainbow-colored lighting"
    src="https://courses.joshwcomeau.com/cfj-mats/wall-art.jpg"
    style="width: 200px;"
  />
  <figcaption>
    Photo by Efe Kurnaz in Camp Nou, Barcelona, Spain. Found on Unsplash.
  </figcaption>
</figure>

<figure>
  <img
    alt="A yawning kitten"
    src="https://courses.joshwcomeau.com/cfj-mats/cat-avatar-250px.jpg"
    style="width: 250px;"
  />
  <figcaption>
    Unknown photographer. Found on Unsplash.
  </figcaption>
</figure>
```

Solution : https://player.vimeo.com/video/520407797

# Height Algorithms

We've seen how widths are calculated in Flow layout, but how about height?

In some ways, it works the same way. Setting an element to have a `height` of `50%` will force that item to take up half of the parent element's content area: no more, no less.
In other ways, they're quite different. The default "width" behaviour of a block-level element is to fill all the available width, whereas the default "height" behaviour is to be as _small_ as possible while fitting all of the element's content; it's closer to `width: min-content` than `width: auto`!

Also, we tend to treat height as "more dynamic" than width. We might feel comfortable setting our main content wrapper to have a max width of 750px, but we wouldn't usually do this with height; We want our design to work whether the content is 200 words, or 20,000 words. And even for pages with the exact same content, we expect that our containers will grow taller on phone screens, and shorter on desktop monitors.
We generally want to avoid setting fixed heights.

But what about when we want to set a _minimum_ height?
For example, let's say that we have an element that wraps around our entire app. If a specific page doesn't have much content, the entire app might be less than 100% of our window height. What if we want it to take up _at least_ 100% of the available space?
![[Pasted image 20231212095015.png]]
Our goal is to have a `.wrapper` element that will be no smaller than 100% of the available height. But `min-height: 100%` doesn't work:
```css
<style>
  .wrapper {
    min-height: 100%;
    border: solid;
  }
</style>

<section class="wrapper">
  <p>
    I'm not very tall!
  </p>
</section>
```
**Have you ever tried to use a percentage-based height, only to discover that it seems to have no effect?** In this lesson, we're going to look at why this happens.

As we saw earlier, the default behaviour of an element in terms of height is to be as _small_ as possible, to contain its children.

Our `section` sits inside the `<body>` tag, and so when we set a percentage-based height or min-height, the percentage is based on that parent height. `<body>` doesn't _have_ a specific height set, which means it uses the default behaviour: stay as short as possible, while still containing all the children.

In other words, we have an impossible condition: we're telling the `<section>` to be a percentage of the `<body>`, and the `<body>` wants to base its size off of the `<section>`. They're both looking to each other for guidance.

**This is a really common source of confusion.** It isn't fixed by Flexbox or Grid, either; those tools help us control the contents of a container, but that container still needs to get its height from somewhere!

Here's how to fix it:
- Put `height: 100%` on every element before your main one (including `html` and `body`)
- Put `min-height: 100%` on that wrapper   
- Don't try and use percentage-based heights within that wrapper

When `html` is given `height: 100%`, it takes up the height of the viewport. That serves as our base. The `body` tag's 100% is based on that base size.
When we get to our wrapper, we want to use `min-height`. This way, the minimum size is equal to the viewport height, but it can overflow and take up more space if required by the content.

Here it is in code:
```css
<style>
  html, body {
    height: 100%;
  }
  .wrapper {
    min-height: 100%;
    border: solid;
  }
</style>

<div class="wrapper">
  <p>
    I fill the viewport now!
  </p>
</div>
```
**App wrapper gotcha(warning)**

JavaScript frameworks like React will render our applications into a container element. In order for percentage-based heights to work, we need to add `height: 100%` to this wrapper!

If you use create-react-app, the wrapper has an ID of `root`. In Next.js, it's `__next`.

Here's an example of how you can solve this problem for these two frameworks:
```css
html,
body,
#root, /* for create-react-app */
#__next /* for Next.js */ {
  height: 100%;
}
```
Note that this isn't specific to React. We need to include selectors for _every_ element that sits between the root `html` tag, and the element we want to stretch to 100% of the screen size.
But yeah, I don't want to distract from the fundamental takeaway here, because it's a really important one: **by default, width looks _up_ the tree, while height looks _down_ the tree.** An element's width is calculated based on its _parent's size_, but an element's _height_ is calculated based on its _children_.

When it comes to height, a parent element will “shrinkwrap” itself around its children, like a pouch of vacuum-sealed food.

We can override this default behaviour by specifying an explicit value. For example, `width: 300px` and `height: 500px` don't look up _or_ down the tree; they don't have to calculate anything, since we're giving it a specific value! So, I'm specifically talking about when we _don't_ set `width`/`height`.

**What about the vh unit?(info)**
You may be familiar with the `vh` unit, a unit designed exactly for this purpose. If you set `height: 100vh`, your element will inherit its height from the viewport size.

Unfortunately, this unit doesn't _quite_ work the way we'd often like, because of mobile devices.
When you scroll on a mobile device, the address bar and footer controls slide away, yielding their space to the content. This means that scrolling on a mobile device changes the viewport height.

To avoid flickering UI issues, browsers like iOS Safari and Chrome Android will set `vh` equal to the _maximum viewport height_, after scrolling. This means that when the page first loads, `100vh` will actually be quite a bit taller than the viewable area.

If you want to see this for yourself, here are some demos. Give them a shot on your phone!
- [courses.joshwcomeau.com/demos/full-height-vh](https://courses.joshwcomeau.com/demos/full-height-vh)
- [courses.joshwcomeau.com/demos/full-height-percentage](https://courses.joshwcomeau.com/demos/full-height-percentage)
**In 2023, there are new units we can use that don't share this problem.** In particular, the `svh` unit (“Small Viewport Height”) will always correspond to the _shorter_ viewport size, the initial condensed viewport.

In cases where you want an element's height to be equal to the viewport, my recommendation is to do this:
```css
.element {
height: 100vh; /* Fallback for older browsers */
height: 100svh;
}
```
This unit is available [across all modern browsers](https://caniuse.com/viewport-unit-variants), but it's still good to provide a fallback for older browsers.

It's still worth knowing how percentage-based heights work, since there will be cases where you want to use a parent container's size rather than the viewport. But hopefully this new `svh` unit comes in handy!
## But what about that footer?
Earlier, we talked about the common UI challenge of having a footer that stays at the bottom:
Having a full-height container is an important _pre-requisite_, but we haven't seen the tools needed to finish solving this problem. Ultimately, the goal with this module is to get comfortable with the height algorithm in Flow layout, to understand why `height` and `min-height` sometimes don't do what we expect.

Specifically, in order to solve this problem, we'd need to use Flexbox. Flexbox is the subject of an [upcoming module](https://courses.joshwcomeau.com/css-for-js/04-flexbox), and we'll see how to solve this and many other problems with it.
It is also possible to solve this problem with _absolute positioning_, something we'll see in Module 2. I do not recommend this approach though: the footer can "overlap" other content, unless you're _very_ careful and use a hacky workaround.
# Margin Collapse

Earlier, we talked about how margin is akin to "personal space". Let's suppose that we want to keep 6 feet
When we think about it, though, that 6 feet can be "shared". If each person has a 6-foot bubble, we don't actually need to be 12 feet away!

Marigins can overlap i.e if two elements has 6px margin , then the gap between both need not be 12px, it can be 6px

Must go through this video : https://player.vimeo.com/video/482761574 - explains about giving margin to element and how it effects the layout
If you'd like, you can [poke around with the same example](https://courses.joshwcomeau.com/demos/margin-collapse) shown in video
# Rules of Margin Collapse

To really understand margin collapse, we need to consider a lot of different circumstances. Let's go through them one by one, looking at how different situations lead to different results.

**This can be a lot to take in.** The very next lesson is a game testing you on these concepts; you may wish to bounce between the two. Go over a couple rules, try the game, rinse and repeat.
## Only vertical margins collapse

Here's the "canonical" margin-collapse example — multiple paragraphs in a row:
```css
<style>
  p {
    margin-top: 24px;
    margin-bottom: 24px;
  }
</style>

<p>Paragraph One</p>
<p>Paragraph Two</p>
```
Each paragraph has `24px` of vertical margin (`margin-top` and `margin-bottom`), and that margin collapses. The paragraphs will be 24px apart, not 48px apart.
![[Pasted image 20231212103303.png]]
When margin-collapse was added to the CSS specification, the language designers made a curious choice: horizontal margins (`margin-left` and `margin-right`) shouldn't collapse.

In the early days, CSS wasn't intended to be used for layouts. The people writing the spec were imagining headings and paragraphs, not columns and sidebars.

So that's our first rule: _only vertical margins collapse._
![[Pasted image 20231212103440.png]]
**Writing modes(info)**

CSS gives us the power to switch our writing modes, so that block-level elements stack horizontally instead of vertically. What effect do you think this would have on margin collapse?
When block elements are stacked horizontally, this rule flips: now, horizontal margins collapse, but vertical margins don't.
```css
<style>
  html {
    writing-mode: vertical-lr;
  }

  p {
    display: block;
    margin-block-start: 24px;
    margin-block-end: 24px;
  }
  .colorcoded{
    background-color: pink
  }
  .colorcoded2{
    background-color: red
  }
</style>

<p class='colorcoded'>Paragraph 1</p>
<p class='colorcoded2'>Paragraph 2</p>
```
So our first rule is a bit of a misnomer; it would be more accurate to say that only _block-direction margins collapse_.

Vertical text on the web is relatively rare, even among websites written in Han-based languages that are historically written top-down.

It's important to recognize that English is not the universal language of the web, but almost all web languages are written either from left-to-right, or right-to-left.
## Margins only collapse in Flow layout

The web has multiple layout modes, like positioned layout, flexbox layout, and grid layout.

Margin collapse is _unique to [[#Flow Layout|Flow layout]]_. If you have children inside a `display: flex` parent, those children's margins will never collapse.
## Only adjacent elements collapse

It is somewhat common to use the `<br />` tag (a line-break) to increase space between block elements.
```css
<style>
  p {
    margin-top: 32px;
    margin-bottom: 32px;
  }
</style>

<p>Paragraph One</p>
<br />
<p>Paragraph Two</p>
```
Regrettably, this has an adverse effect on our margins:
![[Pasted image 20231212104505.png]]
The `<br />` tag is invisible and empty, but _any_ element between two others will block margins from collapsing. Elements need to be adjacent in the DOM for their margins to collapse.
## The bigger margin wins

What about when the margins are asymmetrical? Say, the top element wants 72px of space below, while the bottom element only needs 24px?
![[Pasted image 20231212104624.png]]
The bigger number wins.

This one feels intuitive if you think of margin as "personal space". If one person needs 6 feet of personal space, and another requires 8 feet of personal space, the two people will keep 8 feet apart.
## Nesting doesn't prevent collapsing

Alright, here's where it starts to get weird. Consider the following code:
```css
<style>
  p {
    margin-top: 48px;
    margin-bottom: 48px;
  }
</style>

<div>
  <p>Paragraph One</p>
</div>
<p>Paragraph Two</p>
```
We're dropping our first paragraph into a containing `<div>`, but the margins will still collapse!
![[Pasted image 20231212104928.png]]
It turns out that many of us have **a misconception about how margins work.**

Margin is meant to increase the distance between siblings. It is _not_ meant to increase the gap between a child and its parent's bounding box; that's what padding is for.

Margin will always try and increase distance between siblings, **even if it means _transferring_ margin to the parent element!** In this case, the effect is the same as if we had applied the margin to the parent `<div>`, not the child `<p>`.

“But that can't be!”, I can hear you saying. “I've used margin before to increase the distance between the parent and the first child!”

Margins only collapse when they're _touching_. Here are some examples of nested margins that don't collapse.
### Blocked by padding or border

You can think of padding/border as a sort of wall; if it sits between two margins, they can't collapse, because there's an obstruction in the way
![[Pasted image 20231212105131.png]]
This visualization shows padding, but the same thing happens with border.

Even 1px of padding or border will cause margins not to collapse.
### Blocked by a gap

As we saw in [[#Height Algorithms|Height Algorithms]], a parent will "vacuum-seal" around a child. A 150px-tall single child will have a 150px-tall parent, with no pixels to spare on either side.

But what if we explicitly give our parent element a height? Well, that would create a gap underneath the child:
The empty space between the two margins stops them from collapsing, like a moat filled with hungry piranhas.

Note that this is on a _per-side basis_. In this example, the child's _top_ margin could still collapse. But because there's some empty space below the child, its bottom margin will never collapse.
### Blocked by a scroll container

Later in this course, we'll learn how the `overflow` property can [create a scroll container](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/14-overflow). If the parent element creates a scroll container, with a declaration like `overflow: auto` or `overflow: hidden`, it will disable margin collapse if the margins are on either side of the scroll container.

>Here's the takeaway from these three scenarios: **Margins must be touching in order for them to collapse.**

## Margins can collapse in the same direction

So far, all the examples we've seen involve adjacent opposite margins: the bottom of one element overlaps with the top of the next element.

Surprisingly, margins can collapse even in the same direction.
```css
<style>
  .parent {
    margin-top: 72px;
  }

  .child {
    margin-top: 24px;
  }
</style>

<div class="parent">
  <p class="child">Paragraph One</p>
</div>
```
![[Pasted image 20231212105714.png]]
This is an extension of the previous rule. The child margin is getting “absorbed” into the parent margin. The two are combining, and are subject to the same rules of margin-collapse we've seen so far (eg. the biggest one wins).

This can lead to big surprises. For example, check out this common frustration:
```css
<style>
  .blue {
    background-color: lightblue;
  }
  .pink {
    background-color: lightpink;
  }

  p {
    margin-top: 32px;
  }
</style>

<section class="blue">
  <p>Paragraph One</p>
</section>
<section class="pink">
  <p>Paragraph Two</p>
</section>
```
output:
![[Pasted image 20231212110206.png]]
In this scenario, you might expect the two sections to be touching, with the margin applied inside each container:
![[Pasted image 20231212105948.png]]
This seems like a reasonable assumption, since the `<section>`s have no margin at all! The intention seems to be to increase the space within the top of each box, to give the paragraphs a bit of breathing room.

The trouble is that **0px margin is still a collapsible margin.** Each section has 0px top margin, and it gets combined with the 32px top margin on the paragraph. Since 32px is the larger of the two, it wins.

> Own point: Margin is external to element, adding margin and border to section will give different perspective
```
section {
/* border: 1px solid black; */
margin-top: 6px;
}
```
## More than two margins can collapse

Margin collapse isn't limited to just two margins! In this example, 4 separate margins occupy the same space:
It's hard to see what's going on, but this is essentially a combination of the previous rules:
- Siblings can combine adjacent margins (if the first element has margin-bottom, and the second one has margin-top)
- A parent and child can combine margins in the same direction
Each sibling has a child that contributes a same-direction margin.

Here it is, in code. Use the devtools to view each margin in isolation:
```css
<style>
  header {
    margin-bottom: 10px;
  }

  header h1 {
    margin-bottom: 20px;
  }

  section {
    margin-top: 30px;
  }

  section p {
    margin-top: 40px;
  }
</style>

<header>
  <h1>My Project</h1>
</header>
<section>
  <p>Hello World</p>
</section>
```
The space between our `<header>` and `<section>` has 4 separate margins competing to occupy that space!

- The `header` wants space below itself
- The `h1` in the `header` has bottom margin, which collapses with its parent
- The `section` below the `header` wants space above itself
- The `p` in the `section` has top margin, which collapses with its parent
Ultimately, the paragraph has the largest cumulative margin, so it wins, and 40px separates the `header` and `section`.
## Negative margins

Finally, we have one more factor to consider: negative margins.

As we saw when we [[#Margin|looked at Margins]], a negative margin will pull an element in the opposite direction. A sibling with a negative `margin-top` might overlap its neighbour:
How do negative margins collapse? Well, it's actually quite similar to positive ones! The negative margins will share a space, and the size of that space is determined by the most significant negative margin.
![[Pasted image 20231212132613.png]]
In this example, the elements overlap by 75px, since the more-negative margin (-75px) was more significant than the other (-25px).

What about when negative and positive margins are mixed? In this case, the numbers are _added together_. In this example, the -25px negative margin and the 25px positive margin cancel each other out and have no effect, since -25px + 25px is 0.
![[Pasted image 20231212132709.png]]
Why would we want to apply margins that have no effect?! Well, sometimes you don't control one of the two margins. Maybe it comes from a legacy style, or it's tightly ensconced in a component. By applying an inverse negative margin to the parent, you can "cancel out" a margin.

Of course, this is not ideal. Better to remove unwanted margins than to add even more margins! But this hacky fix can be a lifesaver in certain situation
## Multiple positive and negative margins

We've gotten pretty deep into the weeds here, and we have one more thing to look at. It's the "final boss" of this topic, the culmination of all the rules we've seen so far.

What if we have multiple margins competing for the same space, and some are negative?

If there are more than 2 margins involved, the algorithm looks like this:
- All of the positive margins collapse together (eg. 10px and 50px collapse into a single 50px margin).
- All of the negative margins collapse together (eg. -20px and -30px collapse into a single -30px margin).
- Add those two numbers together (50px + -30px = 20px).
Here's an example in code. Poke around in the devtools to see how it all works out:
```css
<style>
  header {
    margin-bottom: -20px;
  }

  header h1 {
    margin-bottom: 10px;
  }

  section {
    margin-top: -10px;
  }

  section p {
    margin-top: 30px;
  }
</style>

<header>
  <h1>My Project</h1>
</header>
<section>
  <p>Hello World</p>
</section>
```
In this example, our most significant positive margin is 30px. Our most significant negative margin is -20px. Therefore, we wind up with 10px of realized margin, since we add the positive and negative values together.

You can probably understand now why margin collapse has such a dastardly reputation! This stuff is tricky, and that's no joke.

As mentioned, the next lesson features a game that will let you test your collapse knowledge. Don't be afraid to pop back to this lesson for a refresher after you play; it might take a few tries before everything clicks.

# Using Margin Effectively

Now that you've seen how hairy margin collapse can get, you may wonder: why use margin at all, if it has so many footgun
In fact, a growing trend amongst JavaScript developers is to forego margin altogether, and use a combination of padding and layout components instead. Max Stoiber, co-creator of styled-components, has written about how [margin is harmful](https://mxstbr.com/thoughts/margin/).

I personally really like this idea, but I also want to acknowledge that it isn't possible for most folks. Unless you're starting a brand-new project, and the entire team is onboard, you'll be stuck with margin. You need to learn how to use it effectively because most of the front-end world relies on it.

## Margin is like glue

I really like this quote by Heydon Pickering:

> Margin is like putting glue on something before you’ve decided what to stick it to, or if it should be stuck to anything.

I try and avoid putting margin on something at the component boundary. For example, let's say we have a `VideoClip` component:
```js
function VideoClip({ src }) {
  return (
    <video
      src={src}
      style={{ margin: 32 }}
    />
  );
}
```
You might be imagining embedding this video in a blog post, and you know you'll want some space around it... but applying margin in this way is gluing the component without knowing where you'll stick it.

You might be saying “But no, I know where I want to stick it! In the blog post!”. And that's fine for bespoke, one-off components… but `VideoClip` sounds generic and reusable.

For reusable components, we want them to be as _unopinionated_ as possible. Because next week, you may want to create a `VideoStrip` component that lines up several video clips without any gap, and now you have a problem, because the same component needs different amounts of margin in different situations.
What's the solution? Layout components!

We'll see more examples of this later in the course, but the basic idea is that components aren't allowed to have "external margin", margin that extends past the edge of the border box. Instead, components are grouped using layout components like `Stack`:
```js
function BlogPost() {
  return (
    <Stack>
      <p>Hello world!</p>
      <VideoClip />
      <p>Yadda yadda yadda</p>
      <SomeEmbeddedThing />
    </Stack>
  )
}
```
You can see an example of this kind of component in the [Braid design system](https://seek-oss.github.io/braid-design-system/components/Stack).

















