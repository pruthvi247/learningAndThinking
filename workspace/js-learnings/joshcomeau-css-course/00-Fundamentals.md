# media-query
```css
<style>
  @media (max-width: 300px) {
    .small-only {
      color: red;
    }
  }
</style>

<div class="small-only">
  Hello there!
</div>
```
In this case, the condition is `max-width: 300px`. If the window is between 0px and 300px wide, the CSS within will be applied.
```css
<style>
  .large-screens {
    display: none;
  }

  @media (min-width: 300px) {
    .large-screens {
      display: block;
    }
    .small-screens {
      display: none;
    }
  }
</style>

<div class="large-screens">
  I only show up on large screens.
</div>
<div class="small-screens">
  Meanwhile, you'll only see me on small ones.
</div>
```
If our window is at least 300px wide, however, we apply special overrides. This includes showing `large-screens` elements, and hiding `small-screens` elements.

Inside the parentheses, we typically use either `max-width` to add styles on small screens, or `min-width` to add styles on larger ones.

Not all CSS properties have corresponding media features. For example, this snippet is not valid:
```css
/* 🚫 Not valid, since `font-size` can't be queried */
@media (font-size: 32px) {
}
```

# Pseudo-classes

Let's say we have a button, and we want to change its text color when we hover over it.

We can do this with the `:hover` pseudo-class:
```css
<style>
  button:hover {
    color: blue;
  }
</style>

<button>Hover over me!</button>
```
Pseudo-classes let us apply a chunk of CSS based on an element's current state. In this case, we're adding a blue text color when the element is hovered.

This is similar to `onMouseEnter` / `onMouseLeave` events in JavaScript, but with built-in state management. If we were to do this in JS, we'd need to register event listeners, but we'd also need to manage the state somehow, to know if the element is _currently_ being hovered.
## focus

HTML comes with interactive elements like buttons, links, and form inputs. When we interact with one of these elements (either by clicking on it or tabbing to it), it becomes focused. It'll capture keyboard input, so we can type into a form field or press "Enter" to follow a link.

The `:focus` pseudo-class allows us to apply styles exclusively when an interactive element has focus:
```css
<style>
  button:focus {
    border: 2px solid royalblue;
    background: royalblue;
    color: white;
  }
</style>

<button>Hello</button>
<button>world</button>
<button>!</button>
```
## checked

The `:checked` pseudo-class only applies to checkboxes and radio buttons that are "filled in". You can apply additional styles to indicate that the input is activated:
```css
<style>
  input:checked {
    width: 24px;
    height: 24px;
  }
</style>

<h1>Pizza Toppings</h1>
<br />
<label>
  <input type="checkbox" />
  Avocado
</label>
<br />
<label>
  <input type="checkbox" />
  Broccoli
</label>
<br />
<label>
  <input type="checkbox" />
  Carrots
</label>
```
## first/last child

Pseudo-classes aren't just for states like hover/focus/checked! They can also help us apply _conditional logic._

For example, let's suppose we have a set of paragraphs within a `<section>`:
```css
<style>
  p {
    margin-bottom: 1em;
  }
  p:last-child {
    margin-bottom: 0px;
  }
</style>

<section>
  <p>This is a paragraph!</p>
  <p>This is another paragraph!</p>
  <p>
    What do you know, it's a third
    paragraph!
  </p>
</section>
```
**Here's how this works:** The `:last-child` pseudo-class will only select `<p>` tags which are the _final element within its container_. It needs to be the last child within its parent.

Similarly, the `:first-child` pseudo-class will match the first child within a parent container. For example:

**What about :first-of-type and :last-of-type?(info)**

In addition to `:first-child` and `:last-child`, we also have `:first-of-type` and `:last-of-type`. They're _almost_ identical, but they have one critical difference.

`:first-of-type` depends on the _type_ of the HTML tag.

For example, let's suppose we have the following setup:
```css
<style>
  p:first-child {
    color: red;
  }
</style>

<section>
  <h1>Hello world!</h1>
  <p>This is a paragraph!</p>
  <p>This is another paragraph!</p>
</section>
```
The first child within the parent `<section>` tag is an `<h1>`. Our `p:first-child` is looking for situations where a _paragraph_ is the first child within a parent container. It doesn't work in this case.

But, if we switch the selector to `p:first-of-type`, it _does_ work:
```css
<style>
  p:first-of-type {
    color: red;
  }
</style>

<section>
  <h1>Hello world!</h1>
  <p>This is a paragraph!</p>
  <p>This is another paragraph!</p>
</section>
```
The `:first-of-type` pseudo-class ignores any siblings that aren't of the same type. In this case, `p:first-of-type` is going to select the first _paragraph_ within a container, regardless of whether or not it's the first _child_.
# Pseudo-elements

Pseudo-elements are like pseudo-classes, but they don't target a specific state. Instead, they target "sub-elements" within an element.

For example, we can style the placeholder text in a form input with `::placeholder`:
```css
<style>
  input {
    font-size: 1rem;
  }
  input::placeholder {
    color: goldenrod;
  }
</style>

<label>
  Postal Code:
  <input
    type="text"
    placeholder="A1A 1A1"
  />
</label>
```
In terms of syntax, pseudo-elements use two colons instead of one (`::`), though some pseudo-elements also support single-colon syntax.

If we stop and think about it, something pretty interesting is happening here. We haven't explicitly created a `<placeholder>` element, but by adding the `placeholder` attribute to the `<input>` tag, a pseudo-element is created.

This is why they're called pseudo-_elements_ — these selectors target elements in the DOM that we haven't explicitly created with HTML tags.
## before and after

Two of the most common pseudo-elements are `::before` and `::after`.

Here's an example:
```css
<style>
  p::before {
    content: '→ ';
    color: deeppink;
  }
  
  p::after {
    content: ' ←';
    color: deeppink;
  }
</style>

<p>
  This paragraph has little arrows!
</p>
```
These pseudo-elements are added **inside the element**, right before and after the element's content. We could rewrite the above example like so:
```css
<style>
  .pseudo-pseudo {
    color: deeppink;
  }
</style>

<p>
  <span class="pseudo-pseudo">→ </span>
  This paragraph has little arrows!
  <span class="pseudo-pseudo"> ←</span>
</p>
```
There is no significant difference in terms of performance between these two examples. `::before` and `::after` are really just secret spans, nothing more. It's syntactic sugar.

In general, **we probably shouldn't use these two pseudo-elements.** In a vanilla HTML/CSS world, it can be helpful to "bundle" content in with a CSS selector. In the era of components, however, we have better ways of bundling content.

There are also some accessibility concerns with `::before` and `::after`. Some screen readers? will try to vocalize the `content`. Others will ignore them entirely. This inconsistency is problematic.

That said, if the effect is entirely decorative (eg. colorful shapes), I believe it's fine to create them with an empty `content` string:

# Combinators

When you think about it, the humble `<a>` tag has a lot of different hats to wear. The same element needs to handle navigation links in a header, as well as inline links in an article.

What if we wanted to _only_ style navigation links? Well, we could do that using a **combinator**:
```css
<style>
  nav a {
    color: red;
    font-weight: bold;
  }
</style>

<nav>
  <a href="">Home</a>
  -
  <a href="">Shop</a>
</nav>

<p>
  Hello world! You might be interested in reading <a href="">an article</a>!
</p>
```
By putting a space between `nav` and `a`, we're combining two selectors in a very specific way: we're saying that the styles should only apply to `a` tags that are _nested within_ `nav` tags. The first two links in the snippet qualify, but the last one doesn't.

The descendant selector will apply to all descendants, no matter how deeply nested they are. For example, the anchor tags will still work even if they're inside a list:
```css
<style>
  nav a {
    color: red;
    font-weight: bold;
  }
</style>

<nav>
  <ul>
    <li>
      <a href="">Home</a>
    </li>
    <li>
      <a href="">Shop</a>
    </li>
  </ul>
</nav>
```
In CSS, we can differentiate between _children_ and _descendants_. Think of a family tree: a child is only one level down from the parent. A descendant might be 1 level down (child), 2 levels down (grandchild), 3 levels down…

What if we only want to target children, and not deeper descendants?

Here's an example using another combinator. Take a minute and poke at it. I'll explain what's going on in the video below.
```css
<style>
  li {
    margin-bottom: 8px;
  }
  
  .main-list > li {
    border: 2px dotted;
  }
</style>

<ul class="main-list">
  <li>Salt</li>
  <li>Pepper</li>
  <li>
    Fruits & Veg:
    <ul>
      <li>Apple</li>
      <li>Banana</li>
      <li>Carrots</li>
    </ul>
  </li>
</ul>
```
## Color formats

CSS includes many different ways to represent color.

A lot of developers use hex codes (`#FF0000`), but I believe there are better options! my favourite color format is HSL (Hue/Saturation/Lightness).
```css
.colorful-thing {
color: hsl(200deg 100% 50%);
border-bottom: 3px solid hsl(100deg 75% 50%);ßß
}
```
The first number has the `deg` suffix since it's in degrees (from 0° to 360°), and the next two numbers are percentages (from 0% to 100%).

## Transparency

Certain color formats allow us to supply an additional value for the _alpha channel_.

This is a measure of opacity. At 1 (default), the color is fully opaque and solid. At 0, the color is invisible. We can specify decimal values to create a semi-transparent color.

Here's how we represent this in HSL:
```html
<style>
.box {
  width: 50px;
  height: 50px;
}

.first.box {
  background-color: hsl(340deg 100% 50% / 1);
}
.second.box {
  background-color: hsl(340deg 100% 50% / 0.75);
}
.third.box {
  background-color: hsl(340deg 100% 50% / 0.5);
}
.fourth.box {
  background-color: hsl(340deg 100% 50% / 0.25);
}
</style>

<div class="first box"></div>
<div class="second box"></div>
<div class="third box"></div>
<div class="fourth box"></div>
```
The `/` character is becoming a more common pattern in modern CSS. It isn't about _division_, it's about _separation_. The slash allows us to create groups of values. The first group is about the color. The second group is about its opacity.

# Units

The most popular unit for anything size-related is the pixel:

Pixels are nice because they correspond more-or-less with what you see on the screen
. It's a unit that many developers get comfortable with.

## Ems

The `em` unit is an interesting fellow. It's a _relative_ unit, equal to the font size of the current element.

If a heading has a font-size of 24px, and we give it a bottom padding of `2em`, we can expect that the element will have 48px of cushion underneath it (2 × 24px).
```css
<style>
  p {
    /* Change me! */
    font-size: 24px;
  }
</style>

<p>
  <span style="font-size: 1em">
    This
  </span>
  <span style="font-size: 0.8em">
    sentence
  </span>
  <span style="font-size: 0.64em">
    gets
  </span>
  <span style="font-size: 0.5em">
    quieter
  </span>
  <span style="font-size: 0.4em">
    and
  </span>
  <span style="font-size: 0.32em">
    quieter
  </span>
</p>
```
`Result`
![[Pasted image 20231209205446.png]]
**How often should you use ems?** I don't often reach for them. It can be _very_ surprising when a tweak to font-size affects the spacing of descendant elements.

This is especially true when it comes to modern component architectures. Using `em` means that a component's UI will change depending on the font size of the container it's placed within. This can be useful, but more often than not, it's a nuisance.

The `rem` unit is much more useful in most circumstances.
## Rems

The `rem` unit is quite a lot like the `em` unit, with one crucial difference: **it's always relative to the root element, the `<html>` tag.**

All of the rems across your app will be taking their cues from that root HTML tag. By default, the HTML tag has a font size of `16px`, so `1rem` will be equal to `16px`.
Please note, _you shouldn't actually set a `px` font size on the `html` tag._ This will override a user's chosen default font size. The only reason we're doing it here is to demonstrate how the `rem` unit works, and to _simulate_ a user changing their default font size.

If you really want to change the baseline font size for rem units, you can do that using percentages:
```css
html {
  /* 20% bigger `rem` values, app-wide! */
  font-size: 120%;
}
```
We _can_ do this, but we shouldn't.

In order to understand why, we need to talk about accessibility.
```html
html {
  font-size: 31px;
}
h1 {
  font-size: 2rem;
}
```
## Percentages
The percentage unit is often used with width/height, as a way to consume a portion of the available space.
```css
<style>
  .box {
    width: 250px;
    height: 250px;
    background-color: pink;
  }

  .child {
    width: 50%;
    height: 75%;
    background-color: black;
  }
</style>

<div class="box">
  <div class="child"></div>
</div>
```
In this example, we've created a box with a fixed size (250px by 250px), and then added a child with a relative size. When the size of the `.box` element changes, the child will scale accordingly.

There are some interesting quirks when it comes to percentage-based values. We'll see them throughout the course, like when we talk about [Height algorithms](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/11-height) and [aspect ratios](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/16-aspect-ratio#padding-fallback).
## When should I use which unit?

I recently published a blog post, [“The Surprising Truth about Pixels and Accessibility”](https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/). This blog post aims to answer the “pixels vs. rems” thing once and for all.

In the future, I plan on integrating this blog post into this course. For now, I _strongly_ recommend that you check the blog post out. Consider it a bonus lesson from this course!

You can read it here:  
[https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/](https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/)

### Media queries

Should we use pixels or rems for our media query values?
```css
/* Should we do this: */
@media (min-width: 800px) {
  }
/* …Or this: */
@media (min-width: 50rem) {
}
```
It's probably not obvious what the distinction is here, so let's break it down.

Suppose a user sets their default text size to 32px, double the standard text size. This means that 50rem will now be equal to _1600px_ instead of 800px.

By sliding the breakpoint up like this, it means that the user will see the _mobile_ layout until their window is at least 1600px wide. If they're on a laptop, it's very likely they'll see the mobile layout instead of the desktop layout.

At first, I thought this seemed like a bad thing. They're not actually a mobile user, so why would we show them the mobile layout??

I've come to realize, however, that **we usually _do_ want to use rems for media queries.**
### Vertical margins
Vertical margins on text (assuming we're working in a horizontally-written language like English) are typically used to improve its readability. We add extra space between paragraphs so that we can quickly tell where one paragraph ends and the next one begins.*

This space has a “functional” purpose when it comes to text. We aren't using it aesthetically.

For these reasons, I think it does make sense to scale these margins with the user's chosen root font size.
```html
h2 {
  margin-top: 2rem;
}
p, h2 {
  margin-bottom: 1rem;
}
```
**A rare opportunity for the “em” unit**

When I need a relative unit, I almost always reach for `rem`. It's much simpler and more predictable than `em`, for the “compounding” issues [discussed earlier](https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/#rems).

That said, the `em` unit works particularly well when it comes to margins on headings and paragraphs.

As an example, here's how I might style the headings using rems:
```css
h1 {
  font-size: 3rem
  margin-top: 6rem;
  margin-bottom: 1.5rem;
}
h2 {
  font-size: 2rem
  margin-top: 4rem;
  margin-bottom: 1rem;
}
h3 {
  font-size: 1.5rem;
  margin-top: 3rem;
  margin-bottom: 0.75rem;
}
```
Because each heading level has its own font size, we need to calculate unique margin values for each one.

Here's the exact same UI, described using `em` instead:
```css
h1 {
  font-size: 3rem;
}
h2 {
  font-size: 2rem;
}
h3 {
  font-size: 1.5rem;
}
h1, h2, h3 {
  margin-top: 2em;
  margin-bottom: 0.5em;
}
```
Each heading level has a unique font size, but with `em`, they can share their margin declarations. This is because `em` is calculated based on the current element's font size.

In other words, we're saying that each heading level should have “2x” top margin, and “0.5x” bottom margin. Those ratios are applied to the heading's font size.

Ultimately, both approaches are 100% valid, and equally accessible. I just wanted to share this neat little `em` trick. 😄
### Widths and heights
Alright, let's consider one more scenario. Here we have a button with a fixed width:
```css
.button {
  font-size: 1.25rem;
  width: 15rem;
  max-width: 100%;
}
```
So, we know that the button's `font-size` should be set in rems… but what about its `width`?

There's a really interesting trade-off here:
- If we set the width to be `240px`, the button won't grow with font size, leading to line-wrapping and a taller button.
- If we set the width to be `15rem`, the button will grow wider along with the font size.
**Which approach is best?** Well, it depends on the circumstances!
In most cases, I think it makes more sense to use rems. This preserves the button's proportions, its aesthetics. And it reduces the risk of an overflow, if the button has a particularly long word.

In some cases, though, pixels might be the better option. Maybe if you have a very specific layout in mind, and vertical space is more plentiful than horizontal space.
## Bonus: Rem quality of life

Alright, so as we've seen, there are plenty of cases where we need to use `rem` values for best results.

Unfortunately, this unit can often be pretty frustrating to work with. It's not easy to do the conversion math in our heads. And we wind up with _a lot_ of decimals:

- 14px → 0.875rem
- 15px → 0.9375rem
- **16px → 1rem**
- 17px → 1.0625rem
- 18px → 1.125rem
- 19px → 1.1875rem
- 20px → 1.25rem
- 21px → 1.3125rem

Before you go memorize this list, let's look at some of the things we can do to improve the experience of working with rems.

The 62.5% trick

Let's start with one of the most common options I've seen shared online.
Here's what it looks like:
```css
html {
  font-size: 62.5%;
}
p {
  /* Equivalent to 18px */
  font-size: 1.8rem;
}
h3 {
  /* Equivalent to 21px */
  font-size: 2.1rem;
}
```
The idea is that we're scaling down the root font size so that each `rem` unit is equal to 10px instead of 16px.

People like this solution because the math becomes way easier. To get the `rem` equivalent of 18px, you move the decimal (1.8rem) instead of having to divide 18 by 16 (1.125rem).
**But, honestly, I don't recommend this approach.** There are a couple of reasons.

First, It can break compatibility with third-party packages. If you use a tooltip library that uses rem-based font sizes, text in those tooltips is going to be 37.5% smaller than it should be! Similarly, it can break browser extensions the end user has.

There's a baseline assumption on the web that `1rem` will produce readable text. I don't wanna mess with that assumption.

Also, there are significant migration challenges to this approach. There's no reasonable way to “incrementally adopt” it*. You'll need to update every declaration that uses `rem` units across the app. Plus, you'll need to convince all your teammates that it's worth the trouble. Logistically, I'm not sure how realistic it is for most teams.
Let's look at some alternative options.

**Calculated values**
The `calc` CSS function can be used to translate pixel values to rems:
```css
p {
  /* Produces 1.125rem. Equivalent to 18px */
  font-size: calc(18rem / 16);
}
h3 {
  /* Produces 1.3125rem. Equivalent to 21px */
  font-size: calc(21rem / 16);
}
h2 {
  /* Produces 1.5rem. Equivalent to 24px */
  font-size: calc(24rem / 16);
}
h1 {
  /* Produces 2rem. Equivalent to 32px */
  font-size: calc(32rem / 16);
}
```
### Leveraging CSS variables

This is my favourite option. Here's what it looks like:
```css
html {
  --14px: 0.875rem;
  --15px: 0.9375rem;
  --16px: 1rem;
  --17px: 1.0625rem;
  --18px: 1.125rem;
  --19px: 1.1875rem;
  --20px: 1.25rem;
  --21px: 1.3125rem;
}
h1 {
  font-size: var(--21px);
}
```
We can do all the calculations once, and use CSS variables to store those options. When we need to use them, it's almost as easy as typing pixel values, but fully accessible! ✨

It's a bit unconventional to start CSS variables with a number like this, but it's compliant with the spec, and appears to work across all major browsers.

If you use a design system with a spacing scale, we can use this same trick:
```css
html {
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-md: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.3125rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 2.652rem;
  --font-size-4xl: 4rem;
}
```

# Typography

When web designers are learning how to design for the web, they're taught that text is the most important aspect. Remove the text from the page, and it becomes totally unusable. The same might not be true for images or colors or styles.

CSS gives us many levers we can pull to tweak the text on our page, and we'll go deep into them later on. For now, let's cover the fundamentals of styling text.

Font families come in different styles. The two most popular:
- Serif
- Sans-serif
A “serif” is a little adornment at the edge of strokes. Serif fonts are very common in print media, but less so on the web (they tend to create a more sophisticated, aged look).

By passing a _category_ instead of a specific font, the operating system will use its default system font from this category. For example, when specifying `sans-serif`, Windows 11 will use “Segoe UI”, while macOS Ventura uses [SF Pro](https://developer.apple.com/fonts/).

This can be useful if you want your site/app to feel “native” to its platform, but in general, we want to have our own branding! We can do this with a _web font_.
  
A web font is a custom font that we load in our CSS, allowing us to use any font we like. For example, AirBnb developed its own font in-house, [Cereal](https://airbnb.design/cereal/), and uses it across their web and native apps.

We'll explore this concept in depth [later in the course](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/08-web-fonts). **For now, here's what we need to know:** we can drop a snippet into our HTML which will download this custom font onto the user's device, when they visit our site/app.

For example, this is the snippet that Google Fonts provides, if we want to use [Roboto](https://fonts.google.com/specimen/Roboto), one of their hosted web fonts:
```css
<link rel="preconnect" href="https://fonts.gstatic.com">

<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
```
Typical text formatting
Word processing software like Microsoft Word or Google Docs provide many ways to format text, and CSS has inherited some of these conventions.
We'll focus on the 3 most common formatting options:
- Bold
- Italic
- Underline
This section looks at how to accomplish those goals on the web.
Bold text
We can create bold text with the font-weight property:
```css
font-weight: bold;
/*There's also a numbering system, from 1 to 1000, which lets us control the font weight more precisely:*/
/* Light, thin text*/
font-weight: 300;

/* Normal text */
font-weight: 400;

/* Heavy, bold text */
font-weight: 700;
```
### Styles and semantics

CSS allows us to change the cosmetic presentation of text, but it doesn't affect the semantic meaning of the markup. For that, we need to use specialized HTML tags.

The `<strong>` HTML tag is meant to convey that an element is critically important or urgent, like “**Warning: Product may explode if shaken**”.

The `<em>` HTML tag is used for emphasis, the way one might emphasize a particular word in a sentence, like “these pretzels are making me _thirsty_.”

**Semantics are important because not everyone can see the cosmetic styles.** For a variety of reasons, some people use assistive technologies like screen readers (software that reads the text using a synthesized voice) to help them navigate the web. When we use the `<em>` tag, for example, the synthesized voice will stress the syllable much like a human would!

That said, this applies specifically to “copy”, the text content on our websites. We don't need to follow the same rules when it comes to UI elements. For example, we might want to make an input's `<label>` bold, and we can do this purely in CSS, without using a `<strong>` tag.
```
**<b> and <i>?(info)**

Before we had `<strong>` and `<em>`, we had `<b>` (for _bold_) and `<i>` (for _italic_). When HTML5 came around and introduced semantic markup, these two tags were deprecated.

In the years since, however, these tags have been un-deprecated, and given new semantic meaning:

- `<b>` is used to draw attention to text _without_ implying that it's urgent or important.
    
- `<i>` is used to highlight “out of place” content, like a foreign word, or the internal thoughts that a character is having in fiction.
    

**Now, I'll be honest:** I rarely use `<b>` and `<i>` myself. I don't know why you'd want to draw attention to something that _isn't_ important. And it isn't clear to me what the semantic benefits are of the `<i>` tag.

It _is_ important to use semantic HTML, and we'll see plenty of examples throughout this course. My personal opinion is that I'd rather focus on higher-impact things.
```
## Alignment
Another word-processing concern: how do we tweak text alignment?
We can shift characters horizontally using the `text-align` property:
```css
p.left {
  text-align: left;
}
p.right {
  text-align: right;
}
p.center {
  text-align: center;
}

p {
  margin-bottom: 32px;
}
```
`text-align` is also capable of aligning other elements, like images. In general, though, we'll use other tools for those kinds of jobs. We should reserve `text-align` for text.
## Text transforms

We can tweak the formatting of our text using the `text-transform` property:
```css
/* RENDER WITH ALL CAPS */
text-transform: uppercase;
/* Capitalize The First Letter Of Every Word */
text-transform: capitalize;
```
Why use `text-transform` when we can edit the HTML? It's advisable to use this CSS so that the “original” casing can be preserved.

In the future, we may wish to undo the ALL-CAPS treatment. If we had edited the HTML, we'd have to track down and change every single instance. But if we do it in CSS, we only have to remove a single declaration!
## Spacing
We can tweak the spacing of our characters in two ways.
1. We can tweak the horizontal gap between characters using the `letter-spacing` property.
2. We can tweak the vertical distance between lines using the `line-height` property.
```css
<style>
  /* Try tweaking these properties! */
  h3 {
    letter-spacing: 3px;
  }
  
  p {
    font-size: 1rem;
    line-height: 1.5;
  }
</style>

<h3>About Us</h3>
<p>
  The Lumen Group was founded in 1984 in Berlin, Germany. We create purposeful products for the next generation of leaders and executives, luminaries and visionaries of tomorrow.
</p>
```
`line-height` is a bit of an odd duck because it takes a _unitless number_. This number is multiplied by the element's `font-size` to calculate the actual line height.
As an example, suppose we have the following CSS:
```css
p {
font-size: 2rem;
line-height: 1.5;
}
```
We can calculate the actual height of each line by multiplying the font size (2rem) by the line-height (1.5), for a derived value of 3rem.

By default, browsers come with a surprisingly small amount of line height. In Chrome, the default value is `1.15`. In Firefox, it's `1.2`.

These default values produce densely-packed lines of text which can be hard to read for people who are dyslexic or have poor vision. **To comply with accessibility guidelines, our body text should have a minimum line-height of 1.5.** This is according to [WCAG 1.4.12, Text Spacing guidelines](https://www.w3.org/WAI/WCAG21/Understanding/text-spacing.html).

>It's possible to pass other unit types (eg. pixels, rems), but I recommend always using this unitless number, so that the line-height always scales with the element's font-size.

**Careful with JSX!**
If you use JSX and React, there's a bit of a gotcha here.












