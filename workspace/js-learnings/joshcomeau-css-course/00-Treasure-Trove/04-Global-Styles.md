Whenever I start a new project, the first order of business is to sand down some of the rough edges in the CSS language. I do this with a functional set of custom baseline styles.

For a long time, I used Eric Meyer's famous [CSS Reset](https://meyerweb.com/eric/tools/css/reset). It's a solid chunk of CSS, but it's a bit long in the tooth at this point; it hasn't been updated in more than a decade, and _a lot_ has changed since then!

Recently, I've been using my own custom CSS reset. It includes all of the little tricks I've discovered to make CSS nicer to work with, and better for my users.

Like other CSS resets, mine is unopinionated when it comes to design / cosmetics. You can use this reset for any project, no matter the aesthetic you're going for.

Here are the styles I use. Below, we'll examine each group in detail.
```css
/*
  1. Use a more-intuitive box-sizing model.
*/
*, *::before, *::after {
  box-sizing: border-box;
}

/*
  2. Remove default margin
*/
* {
  margin: 0;
}

/*
  3. Allow percentage-based heights in the application
*/
html, body {
  height: 100%;
}

/*
  Typographic tweaks!
  4. Add accessible line-height
  5. Improve text rendering
*/
body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

/*
  6. Improve media defaults
*/
img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}

/*
  7. Remove built-in form typography styles
*/
input, button, textarea, select {
  font: inherit;
}

/*
  8. Avoid text overflows
*/
p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
}

/*
  9. Create a root stacking context
*/
#root, #__next {
  isolation: isolate;
}
```
**CSS Reset?(info)**

As we've learned, browsers come with a [built-in set of CSS styles](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/01-built-ins-and-inheritance), known as the “User-Agent Stylesheet”.

Historically, the main goal of a CSS reset has been to ensure consistency between browsers, and to undo all default styles, creating a blank slate. My CSS reset doesn't really do either of these things.

These days, browsers don't have massive discrepancies when it comes to layout or spacing. By and large, browsers implement the CSS specification faithfully, and things behave as you'd expect. So it isn't as necessary anymore.

I also don't believe it's necessary to strip away all of the browser defaults. I probably _do_ want _em_ tags to set “font-style: italic”, for example! I can always make different design decisions in the individual project styles, but I see no point in stripping away common-sense defaults.

My CSS reset may not fit the classical definition of a “CSS reset”, but I'm taking that creative

## 1. Box-sizing model

As we saw [in Module 1](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/04-the-box-model#box-sizing), most browsers use a default box-sizing model of `content-box`. This model is way less intuitive, and can lead to lots of weird issues (eg. having a child overflow because it sets `width: 100%`).

By setting `box-sizing: border-box`, we change how the browser interprets percentage-based sizes and distances.

**This is a must-have rule, in my opinion.** It makes CSS _significantly_ nicer to work with.

**Inheriting box-sizing(info)**
I've seen some recommendations online to do this instead:
```css
html {
  box-sizing: border-box;
}

*, *:before, *:after {
  box-sizing: inherit;
}
```
This can be a helpful strategy if you're trying to migrate a large pre-existing project to use border-box. It isn't necessary if you're starting a brand new project from scratch. To keep things simple, I've omitted it from my CSS reset.

Expand to see an example of when this might be helpful.
First, we can create a "legacy" selector that will flip the box-sizing to `content-box`, the default value for the `box-sizing` property:
```css
.legacy {
box-sizing: content-box;
}
```
Then, whenever we have a slice of our app that hasn't been migrated to use border-box, we can slap the class on:
```html
<body>
  <header class="legacy">
    <nav>
      <!-- Legacy stuff here -->
    </nav>
  </header>
  <main>
    <section>
      <!-- Modern stuff here -->
    </section>
    <aside class="legacy">
      <!-- Legacy stuff here -->
    </aside>
  </main>
</body>
```
**Why does this work?** Well, let's think about how the elements in this snippet are evaluated.

`<header>` is given the `legacy` class, so it uses `box-sizing: content-box`.

Its child, `<nav>`, has `box-sizing: inherit`. Because its parent is set to `content-box`, `nav` will be set to `content-box` as well.

The `<main>` tag doesn't have the `legacy` class, and so it inherits from its parent, `<body>`. `<body>` inherits from `<html>`. And `<html>` is set to `border-box`.

Essentially, every element will now figure out its box-sizing behavior from its parent. If it has an ancestor that sets the `legacy` class, it'll be `content-box`. Otherwise, it'll ultimately inherit from the `html` tag, and use `border-box`.
## 2. Remove default margin
```css
* {
margin: 0;
}
```
Browsers will make common-sense assumptions around margin: for example, a heading will include more margin by default than a paragraph.

These assumptions are reasonable within the context of a word-processing document, but they might not be accurate for a modern webapp.

Margin is a [tricky devil](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/12-rules-of-margin-collapse), and more often than not, I find myself wishing elements didn't have any by default. So I've decided to remove it all. 🔥

If/when I do want to add some margin to specific tags, I can do so in my custom project styles. The wildcard selector (`*`) has extremely low specificity, so it'll be easy to override this rule.
## 3. Percentage-based heights
```css
html, body {
  height: 100%;
}
```
As discussed in the [“Height Algorithms” lesson](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/11-height), using the percentage unit for the `height` property won't always work. This only works if the parent defines an absolute height (eg. `height: 400px`), or if _all of the ancestors_ use percentages, all the way up to the root HTML element.

By setting `html` and `body` to have `height: 100%`, we make it easier for us to use percentage-based heights down the line, if we decide to.

We might wish to add a third selector, to target the app container. For example, in my Next.js projects, I update the rule as follows:
```css
html, body, #__next {
height: 100%;
}
```
`__next` is an ID applied automatically by the Next.js framework to the element right inside `body` that will house our Next.js application.

This will vary from framework to framework. In Create React App, for example, the container ID is `root`.
## 4. Tweaking line-height
```css
body {
  line-height: 1.5;
}
```
As we covered in the [Typography recap lesson](https://courses.joshwcomeau.com/css-for-js/00-recap/07-typography#spacing), we want to use a `line-height` of at least `1.5`. This is because tightly-packed lines are difficult for dyslexic people to read, [according to the WCAG criteria](https://www.w3.org/WAI/WCAG21/Understanding/text-spacing.html)
The "default" value varies between browsers, but tends to be around 1.2. This bumps it up to an accessible value.

**Smarter line-heights with “calc”(success)**
I've been experimenting with an alternative way to manage line-heights. Here it is:
```css
* {
  line-height: calc(1em + 0.5rem);
}
```
Instead of calculating the line height by _multiplying_ the font-size with a number like 1.5, this alternative uses the font-size as a base, and _adds_ a fixed amount of space to each line.

For body text like paragraphs, this declaration has no effect; either way, each line will resolve to 24px (assuming a default browser font size).

On larger text, though, this declaration produces tighter lines.

You can play with this idea here:
```css
<style>
  * {
    line-height: 1.5;
    /*
      Delete this line to see
      the difference:
    */
    line-height: calc(1em + 0.5rem);
  }
  h1 {
  font-size: 4rem;
  margin-top: 0.5em;
}
</style>

<p>
  Because this paragraph doesn't set a font-size, it uses the browser default of 1rem. Our line-height expression add 0.5rem, for a total line height of 1.5rem (24px). This is equivalent to the value produced by “line-height: 1.5”.
</p>
<h1>
  This heading has 4.5rem (72px) line-height; we add 0.5rem to its font-size of 4rem.
</h1>
```
**Proceed with caution.** I'm still in the process of experimenting with this one.

One downside is that we have to set it on all elements with `*` instead of applying it to the `body`. This is because the `em` unit doesn't inherit well; it won't recalculate the value of `1em` for every element.

On this blog, for example, it broke my code playgrounds, because the third-party code assumed that line-height was inheritable, as it usually is.

For more information on this technique, check out this awesome blog post by Kitty Giraudel: [Using calc to figure out optimal line-height](https://kittygiraudel.com/2020/05/18/using-calc-to-figure-out-optimal-line-height/).
## 5. Font smoothing
```css
body {
-webkit-font-smoothing: antialiased;
}
```
As we saw in [Module 6](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/02-text-rendering#font-smoothing), this property improves text rendering on macOS browsers.

We set these properties on `body` rather than in a wildcard selector (`*`) because typography styles are inheritable. This means they'll automatically be carried down the DOM tree for us, while still being very easy to override when needed.
## 6. Sensible media defaults
```css
img, picture, video, canvas, svg {
display: block;
max-width: 100%;
}
```
So here's a weird thing: images are considered "inline" elements. This implies that they should be used in the middle of paragraphs, like `<em>` or `<strong>`.

This doesn't jive with how I use images most of the time. Typically, I treat images the same way I treat paragraphs or headers or sidebars; they're layout elements.

If we try to use an inline element in our layout, though, weird things happen. We have to worry about [inline magic space](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/09-flow-layout#inline-elements-have-magic-space). By setting `display: block` on all media elements by default, we sidestep a whole category of funky issues.

I also set `max-width: 100%`. This is done to keep large images from overflowing, if they're placed in a container that isn't wide enough to contain them. Because images/videos are [replaced elements](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/09-flow-layout), they don't behave like other elements do.
## 7. Inherit fonts for form controls
```css
input, button, textarea, select {
font: inherit;
}
```
By default, buttons don't inherit typographic styles.

On Chrome, for example, buttons will have a default font size of 13.333px. This is _way too small_; we want most text to be at least 1rem (16px), as we saw in the [“Responsive Typography” lesson](https://courses.joshwcomeau.com/css-for-js/05-responsive-css/14-responsive-typography).

Rather than set custom font sizes and styles for buttons and other inputs, we should set it to `inherit`. This way, these elements will automatically match their surrounding typography.
## 8. Word wrapping
```css
p, h1, h2, h3, h4, h5, h6 {
overflow-wrap: break-word;
}```
As we saw in [Module 6](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/03-text-overflow), we have a few ways to manage text overflow in CSS. To avoid unbreakable text from spilling out the sides of their parent containers, we can apply this rule to allow hard wraps.

Thanks to Sophie Alpert for [suggesting a similar rule](https://twitter.com/sophiebits/status/1462921205359386628)! She suggests applying it to _all_ elements, which is probably a good idea, but not something I've personally tested.

You can also try adding the `hyphens` property:
```css
p {
overflow-wrap: break-word;
hyphens: auto;
}
```
`hyphens: auto` uses hyphens (in languages that support them) to indicate hard wraps. It also makes hard wraps much more common.

It can be worthwhile if you have very-narrow columns of text, but it can also be a bit distracting. I chose not to include it in the reset, but it's worth experimenting with!
## 9. Root stacking context
```css
#root, #__next {
isolation: isolate;
}
```
As we saw [in Module 2](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/08-reducing-z-index#the-isolation-property), the `isolation` property allows us to create a new stacking context without setting a `z-index`.

By creating a stacking context on our application's container, we ensure that everything within our application will participate in an "app-specific" context, rather than the global top-level context. This makes it possible for us to guarantee that elements created using portals (eg. modals, tooltips) will always show up on top of our application.

We're using the selector `#__next` here because in the Next.js framework, the application container is given this ID. The specific selector will vary depending on your framework; with Create React App, for example, the root container is `#root`.

## Alternatives

In the past, I've used [Eric Meyer's CSS Reset](https://meyerweb.com/eric/tools/css/reset/). It's by far the most common set of global styles. It was the gold standard for many years. At this point, though, it's more than a decade old, and browsers have come a long way since then. I don't believe that this reset is necessary anymore.

Andy Bell has shared his [Modern CSS Reset](https://piccalil.li/blog/a-modern-css-reset/). It inspired some of the styles in my own set of global styles, in fact!

## Making it your own

As your journey with CSS continues, you'll likely pick up some tricks and conventions you'll want to take with you from project to project. You can use the styles provided here as a baseline template, but don't be afraid to build on top of it!
































