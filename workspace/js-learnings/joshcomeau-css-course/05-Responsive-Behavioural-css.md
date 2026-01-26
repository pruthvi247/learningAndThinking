Mobile devices have a “device pixel ratio”. This can be accessed in JavaScript with the following statement:
`console.log(window.devicePixelRatio);`
This number is the ratio between the physical LED pixels on the device, and the "theoretical" pixels we use in CSS.

On my iPhone, this number is `3`. This means that a 10px length will actually be 30px long. Each software pixel actually corresponds to 9 hardware pixels:
![[Pasted image 20231217164739.png]]
(In reality, [pixels aren't tiny squares](http://alvyray.com/Memos/CG/Microsoft/6_pixel.pdf), but for our purposes, we can pretend they are.)

Mapping a software pixel to multiple hardware pixels happens “under the hood”. In CSS, we can only access software pixels
This is especially important to know when rendering images: We want to use large images on high-DPI screens, to make sure they look sharp and clear. We'll see how to do this later on in the course.
### The magical meta tag

To make sure that our pages render correctly on mobile, it's imperative that we add the following meta tag to our HTML:
```html
<meta
name="viewport"
content="width=device-width, initial-scale=1"
>
```
This tag comes stock with every HTML skeleton and boilerplate out there. It's included by default when generating an app with tools like create-react-app.

But what is it doing, exactly?

This tag was invented by Apple as a way to disable some of the "optimizations" that the browser makes. Android quickly adopted it as well, and it's [making its way](https://www.w3.org/TR/css-device-adapt-1/#viewport-meta) into the CSS specification.

When the iPhone was released, mobile websites didn't exist. Safari would therefore render the website _as if_ it was a desktop browser window with a width of 980px, and then scale it down to fit on its 320px-wide screen.

This gave users a 30,000-foot view of the page, and they could pinch-to-zoom when they spotted the content they were interested in, sort of like a mini-map.

We don't want mobile browsers to do this anymore. On the modern web, pages are built with the expectation that they'll be viewed on a narrow mobile screen.

`width=device-width` instructs the browser to set the viewport width to match the device's width (so, 320px instead of 980px). `initial-scale=1` says that we should start at 1x zoom.

**Other options(info)**
This meta tag also allows us to constrain the user's ability to zoom, either by setting a min/max scale, or by disabling it altogether.

This can be useful when building certain types of applications. For example, if we were building Google Maps, we would want to disable user scaling so that we could implement our own pinch gestures. But this is an escape hatch that 99.9% of applications don't need, and shouldn't use. Zooming is a critical browser feature, and disabling or limiting it will make our products less accessible.
# Media Queries

When it comes to building responsive interfaces, the _media query_ is the primary tool in our toolbox.

As a refresher, here's what the syntax looks like:
```css
<style>
  .signup-button {
    color: deeppink;
    font-size: 1rem;
  }
  
  @media (max-width: 400px) {
    .signup-button {
      font-size: 2rem;
    }
  }
</style>

<button class="signup-button">
  Sign Up
</button>
```
The `@media` keyword is known as an "at-rule". at-rules are a special kind of CSS statement that changes behaviour. There are a handful of at-rules that all do different things; another example is `@keyframes`, which allows you to define an animation sequence.

Media queries selectively apply rules based on one or more conditions. In this case, we're saying that the `.signup-button` selector should adopt an additional declaration when the viewport is 400px wide or less.

**Notice that the button always has pink text**. Media queries allow us to _merge_ rules together. We're not picking "one or the other"—when the viewport is 400px or smaller, declarations from both rules will apply

Media queries are really like _if_ statements in JavaScript. We can think of it like this:
```js
let signupButtonStyles = {
  color: 'deeppink',
  fontSize: '1rem'
}

if (windowWidth <= 400) {
  signupButtonStyles.fontSize = '2rem';
}
```
It's also important to note that **media queries don't affect specificity**. The only reason that `font-size: 2rem` beats `font-size: 1rem` is because it comes later. Notice what happens when the order is flipped:

The button never changes size, because the `font-size: 2rem` declaration is _always_ overwritten by the `font-size: 1rem` declaration.

In JS terms, it's as if we had done this:
```js
let signupButtonStyles = {}

if (windowWidth <= 400) {
  signupButtonStyles.fontSize = '2rem';
}

signupButtonStyles.color = 'deeppink';
signupButtonStyles.fontSize = '1rem';
```
## With styled-components

Here's how we use a media query with styled-components:
```js
const SignupButton = styled.button`
  color: deeppink;
  font-size: 1rem;

  @media (max-width: 400px) {
    font-size: 2rem;
  }
`;
```
styled-components allows us to nest media queries within our component definitions.

This might seem like a small thing, but it **totally changes our mental model** when it comes to styling. With regular media queries, declarations are grouped by viewport size
```css
/* All mobile styles */
.wrapper {
  padding: 8px;
  border: 2px solid;
}
.button {
  font-size: 1rem;
}
h2.title {
  font-size: 2rem;
}

/* All tablet styles */
@media (min-width: 550px) {
  .wrapper {
    padding: 16px;
    border: 3px solid;
  }
  h2.title {
    font-size: 2.5rem;
  }
}

/* All desktop styles */
@media (min-width: 1100px) {
  .button {
    font-size: 1.5rem;
  }

  h2.title {
    font-size: 3em;
  }
}
```
With styled-components, all of the declarations for an element are in the same spot:
```js
// All Wrapper styles
const Wrapper = styled.div`
  padding: 8px;
  border: 2px solid;

  @media (min-width: 550px) {
    padding: 16px;
    border: 3px solid;
  }
`;

// All Button styles
const Button = styled.button`
  font-size: 1rem;

  @media (min-width: 1100px) {
    font-size: 1.5rem;
  }
`;

// All Title styles
const Title = styled.h2`
  font-size: 2rem;

  @media (min-width: 550px) {
    font-size: 2.5rem;
  }

  @media (min-width: 1100px) {
    font-size: 3rem;
  }
`;
```
This pattern makes it way easier to reason about which styles apply to which elements. Everything you need to know, in 1 place.

Fortunately, **this "nested media queries" thing is not unique to styled-components.** CSS preprocessors like Sass also support nested media queries. I suggest using this pattern if your tool allows for it.
## Mobile-first vs desktop-first

There are two distinct ways we can write the media query we saw above:
```css
.signup-button {
  color: deeppink;
  font-size: 1rem;
}

@media (max-width: 400px) {
  .signup-button {
    font-size: 2rem;
  }
}
```
---
```css
.signup-button {
  color: deeppink;
  font-size: 2rem;
}

@media (min-width: 401px) {
  .signup-button {
    font-size: 1rem;
  }
}
```
The first snippet is known as **desktop-first**, since our default styles (the ones not inside `@media`) target desktop devices, and then we specify overrides for mobile devices. By contrast, the second snippet is **mobile-first**, since the main styles are for mobile devices (400px or smaller).

To be clear, _the end result is the same_. These are two different roads to the same place. But the mental model is different.
#ImportantPoint 
the most important thing is to **be consistent with the approach.** If you decide to build mobile-first, you should almost always use `min-width` media queries. It can be very confusing if you mix `min-width` and `max-width` media queries.
### Mixing patterns
Here's a pattern I _try_ to avoid:
```css
<style>
  @media (max-width: 600px) {
    .desktop-button {
      display: none;
    }
  }

  @media (min-width: 601px) {
    .mobile-button {
      display: none;
    }
  }
</style>

<button class="desktop-button">
  Click me
</button>
<button class="mobile-button">
  Tap me
</button>
```
This code is designed to "toggle" between two buttons: on mobile, the `.mobile-button` is shown. On desktop, `.mobile-button` is hidden and `.desktop-button` is shown instead.

One minor problem is that fractional viewport widths (eg. 600.5px) _are_ possible, according to the specification. I've seen this firsthand when the page is embedded in an iframe, but there may be other situations that lead to non-integer viewport widths.

But here's the real reason I try not to do this: It complicates the mental model.

I believe that our applications should be either mobile-first or desktop-first. If we consistently use a single set of media queries, it'll help us quickly scan chunks of CSS to understand the structure.

How would we solve this problem without mixing queries? Here's how I'd structure this
```css
.desktop-button {
  display: none;
}

@media (min-width: 601px) {
  .desktop-button {
    display: revert;
  }

  .mobile-button {
    display: none;
  }
}
```
`revert` is a special keyword that restores the property to its default value. It's a way of undoing the `display: none` set outside the media query.

Alternatively, if the application is desktop-first, it would look like this:
```css
.mobile-button {
  display: none;
}

@media (max-width: 600px) {
  .mobile-button {
    display: revert;
  }

  .desktop-button {
    display: none;
  }
}
```
Structuring things this way is more verbose, but I think it's worth it.

That said, there are exceptions. Sometimes, it's just too much trouble to structure things this way.

For example, if we have a completely different layout that only exists on tablet, it can be nice to wrap it in a "tablet only" media query:
```css
@media (min-width: 500px) and (max-width: 1023px) {
  .wrapper {
    display: flex;
    flex-direction: row;
    gap: 32px;
    align-items: flex-start;
    justify-content: center;
  }

  .wrapper:first-child {
    width: 200px;
    min-height: 200px;
  }
}
```
It _is_ possible to rewrite this to only use `min-width`, but it would ultimately make the CSS harder to understand.

Ultimately, this comes down to judgment and intuition, and the only way to build that intuition is to experiment. Try both approaches, and see what works best for you in your applications!
## Media queries and units

When creating `min-width` / `max-width` media queries, should we use pixels? Or maybe another unit, like rems?

**What's the difference?** As we learned in [Module 1](https://courses.joshwcomeau.com/css-for-js/00-recap/06-units), the `rem` unit is equal to 16px by default, but can be redefined, either by the developer _or by the end user._

Suppose the user has poor vision, and they want to boost the size of text. They go into their browser settings, and crank up the baseline font size to 32px. Now, each `rem` unit is equal to 32px instead of 16px.

And so here's the question: **Should our media queries be affected by the user's chosen baseline font size?**

For a long time, I thought the answer was “no”, and I used pixels for all media queries. But over the past few months, I've reconsidered this position.

To help me explain why, let's use this course platform as an example. In this example, they've cranked the baseline font size to 32px:
![[Pasted image 20231217172345.png]]
With pixel-based media queries, we stick with the desktop layout no matter what the user does with their default font size. When cranked to 32px, it means we wind up with a really cramped layout: the sidebar expands and fills half of the screen (since it uses a rem-based width).

When we use rem-based media queries, we flip to the _mobile_ view (even though they're using a desktop-sized window). The large text has more room to breathe, and it's generally just a much better experience.

For this reason, **I recommend using `rem` media queries in most situations.**

You can also use `em` instead of `rem`; the two units function exactly the same way, when it comes to media queries.

For more information, check out my blog post, [“The Surprising Truth about Pixels and Accessibility”](https://www.joshwcomeau.com/css/surprising-truth-about-pixels-and-accessibility/#media-queries).

**Do as I say, not as I said(info)**

I started using rem-based media queries in my own work in mid-2022. Unfortunately, this course was created _before_ this point. As a result, some lessons in this course will still use pixel-based media queries. Sorry for any confusion!

## Disappearing sidebar

Below you'll find a two-column layout: A sidebar with navigation links, and a main content area.

Update the code so that the navigation column disappears on windows less than 700px wide:

Solution Video : https://player.vimeo.com/video/541129468
Solution git : https://github.com/pruthvi247/huckleberry/blob/main/05-media-query/01-media-sol.html

## Mobile modal

In this exercise, we're given an application with a pre-built modal, and asked to make it mobile-responsive.

Here's how it currently looks when being shrunk:
Demo video : https://courses.joshwcomeau.com/cfj-mats/modal-unresponsive.mp4
This exercise will be solved on CodeSandbox:
- [Access starter code](https://codesandbox.io/s/exercise-mobile-friendly-modal-d2klo?file=/src/Modal.js)
[View final solution code](https://codesandbox.io/s/exercise-mobile-friendly-modal-solution-nxgjy?file=/src/Modal.js)

## Bonus: Building accessible modals

Video : https://player.vimeo.com/video/541862577
**Note:** In this video, I use Reach UI, but this library is no longer being actively maintained. Instead, I recommend using the `<Dialog>` component from [Radix Primitives](https://www.radix-ui.com/docs/primitives/components/alert-dialog).

Also, if you don't use React, there are other tools you can use to build accessible modals:

- [a11y-dialog](https://github.com/KittyGiraudel/a11y-dialog) A Vanilla JS solution
    
- [vue-accessible-modal](https://github.com/andrewvasilchuk/vue-accessible-modal) (I haven't personally used this, but I poked at the demo and it seems solid)
# Other Queries

When we talk about “media queries”, we're generally talking about adapting our CSS based on the screen/window size of the client. But that's only one of the tricks media queries have up their sleeves!

## Hovering

Hovering is a gesture only possible when using a pointer device, like a mouse or a trackpad. On mobile devices, we typically use our fingers, and our fingers are incapable of hovering.

When Apple created iOS Safari, they decided that tapping on an interactive element (like a link or button) should trigger the hover state. This is a questionable decision nowadays, but it made sense at the time—web developers at the time _assumed_ that everyone could hover, since smartphones weren't a thing yet. It was common for tooltips to only be shown on hover.

Android devices work the same way. Tapping an interactive element will show the "hover" state. It'll stay hovered until you tap somewhere else.

To see how this can be a bit annoying, check out [this great demo](https://loud-magnetic-afrovenator.glitch.me/) by Mezo Istvan. Try the demo first on desktop, and then on your mobile device.

**Double-tap to continue(info)**

If you've been an iPhone user for a few years, you may have run into some curious behaviour: sometimes, tapping a link or a button will trigger the hover state, but nothing else. It requires a _second_ tap to actually click the link/button.

This used to happen if the element in question had a hover style that changed the visibility of an element (eg. showing/hiding a child element).

Fortunately, iOS Safari no longer behaves this way. Starting in 2019, links/buttons will always trigger a click event on tap, no matter what the hover state is.
So how do we avoid setting hover styles on mobile devices? Your first instinct might be to only apply hover styles on larger screens:
```css
@media (min-width: 1100px) {
  button:hover {
    text-decoration: underline;
  }
}
```
This isn't quite right, though: after all, some users on a large desktop display will shrink their windows to a smaller size. Also, not all desktop users navigate using a pointer device. We shouldn't think of hover events as a "big screen thing", we should think of them as a "mouse/trackpad thing"

There's another media query we can use for this:
```css
@media (hover: hover) and (pointer: fine) {
  button:hover {
    text-decoration: underline;
  }
}
```
This is a relatively new addition to the Media Queries specification. They're called [“Interaction Media Features”](https://drafts.csswg.org/mediaqueries-4/#mf-interaction). They allow us to apply styles based on which input mechanism the user is using.

What's the difference between "hover" and "pointer"? They actually refer to two distinct capabilities. `hover` is the ability for a device to move the cursor without also triggering a click/tap on the element underneath; a mouse can do this, but your finger or a stylus can't. `pointer` refers to the level of control the user has over the position of the cursor.

This table should help make this distinction clear:
![[Pasted image 20231217183947.png]]
A "fine" pointer like a mouse or trackpad means that the user can be very precise with their clicks. Using our fingers on a touchscreen, though, is "coarse": we can't be anywhere near as precise.

Somewhat magically, browsers are able to infer which input device you're using! This is a dynamic query: if you switch from using a mouse to using a keyboard (for navigation, not for typing), the values for `hover` and `pointer` will update dynamically.

While relatively new, interaction media features are [broadly supported in all major browsers](https://caniuse.com/css-media-interaction), though Internet Explorer is left out.
### Boolean logic in media queries

In the hover/pointer media query above, we also introduced something new: the “and” keyword.
```css
@media (hover: hover) and (pointer: fine) {
  /* styles */
}
```
“and” is essentially the same as `&&` in JavaScript. In order for the styles to be applied, **all** of the queries must be satisfied.

**Screen**
`screen` is a “media type”. In this case, we're saying that the styles should only apply when displaying the site/app on a screen. We can also specify `print` styles which apply when the page is printed onto paper or saved as a PDF.

(specifying `screen` has become less common in recent years, as browsers have chosen more-sensible defaults when it comes to printing.)
```css
@media screen and (min-width: 600px) {
  /* styles */
}
```
In addition to “and”, it's also possible to specify “or” (`||`) as well.

Truthfully, “or” isn't super useful. it's more of an academic curiosity than something you'll use in day-to-day life.

if we want to specify that _any_ of the conditions can be met, we can use a comma:
```css
@media (max-width: 600px), (min-width: 800px) {
  /* styles */
}
```
This is effectively the same as creating two entirely-separate media queries
```css
@media (max-width: 600px) {
  /* styles */
}
@media (min-width: 800px) {
  /* Repeated styles */
}
```
Chris Coyier shared an interesting set of logical operators in a [CSS Tricks article](https://css-tricks.com/logic-in-media-queries/). It's a fun little rabbit hole, but ultimately these tools aren't super necessary in practical terms.
## Preference-based media queries

Another feature of media queries is that they can "hook in" and access user preferences. This allows us to tailor our styles based on the user's personal preferences and needs.

For example, we can detect whether the user prefers light mode or dark mode with this media query:
```css
@media (prefers-color-scheme: dark) {
  /* Dark-mode styles here */
}
```
It's not just about "preference", though. These queries allow us to create safer, more accessible experiences.

For example, some folks are sensitive to motion. Our fun parallax animation might give them a migraine, or make them feel so nauseous they need to lie down for an hour. We can avoid this by wrapping our animation-based styles in this media query:
```css
@media (prefers-reduced-motion: no-preference) {
  /* Animations here */
}
```
**Orientation(info)**

Aside from `min-width` / `max-width`, there are other ways to target specific window proportions. One of the most interesting is `orientation`:
```css
@media (orientation: portrait) {
  /* Styles for windows that are taller than they are wide */
}
@media (orientation: landscape) {
  /* Styles for windows that are wider than they are tall */
}
```
I've done some pretty extensive experimentation with this media query, and have found that it's **not usually worth using.** It's not as flexible as `min-width` / `max-width`, and it leads to confusing conflicts between both types of queries.

In rare cases, though, it can be a useful tool to have in the toolbox.
# Breakpoints

To help add structure to a chaotic world, it helps to pick a series of breakpoints.

A breakpoint is a specific viewport width that lets us segment all devices into a small set of possible experiences. For example, we might set a breakpoint at 500px. Any device under 500px will be put in the same bucket, and can be styled separately. This ensures a consistent experience; someone on a 375px-wide phone will share the same layout as someone on a 414px-wide phone.
## Picking breakpoint values

There's no such thing as a universal set of "perfect" breakpoints: it will depend on your design, and the devices you target. But I do have some thoughts about how to pick a solid set of values.

Developers typically pick breakpoints based on common device resolutions. The iPhone 12 has a screen width of 375px, so maybe that'll become our "phone" breakpoint.

**I don't think that this is the right approach.** I believe that the most common device resolutions should _sit in the middle of each grouping_. A 375px iPhone should probably be in the same bucket as a 320px iPhone SE and a 412px Android phone.

In other words, we should put our breakpoints in _dead zones_, as far away from “real-world” resolutions as possible. They should be in “no-device land”. This way, all similar devices will share the same layout.

This data visualization shows the most popular screen resolutions by platform, [according to StatCounter](https://gs.statcounter.com/screen-resolution-stats). Focus or hover over the dots to see the devices they represent:
> Its a css/html visualisation, hence could not be copied

(Credit to [David Gilbertson](https://www.freecodecamp.org/news/the-100-correct-way-to-do-css-breakpoints-88d6a5ba1862/) for the idea for this visualization.)

The resolutions come in several clusters. If we draw circles around them, we'll know where to put our breakpoints:
![[Pasted image 20231217184935.png]]
Here are the groups I've identified:

- 0-550px — Mobile
- 550-1100px — Tablet
- 1100-1500px — Laptop
- 1500+px — Desktop

I don't bother disambiguating between "small" mobile devices (like the iPhone SE, 320px-wide) and "large" mobile devices (like the iPhone X Max, 414px-wide) because I don't generally create distinct layouts for different sizes of phone. Your circumstances might vary, though! Keep your design in mind when picking breakpoint values.
## Implementing breakpoints

Our exact implementation will depend on whether we go mobile-first or desktop-first.

Here's how it'd work if we go _desktop-first_:
```css
/* Default: Desktop monitors, 1501px and up */
@media (max-width: 1500px) {
  /* Laptop */
}
@media (max-width: 1100px) {
  /* Tablets */
}
@media (max-width: 550px) {
  /* Phones */
}
```
Conversely, if we went _mobile-first_, it would look like this:
```css
/* Default: Phones from 0px to 549px */
@media (min-width: 550px) {
  /* Tablets */
}
@media (min-width: 1100px) {
  /* Laptop */
}
@media (min-width: 1500px) {
  /* Desktop */
}
```
Some developers like to create queries for "exclusive" ranges. For example, if we wanted to target _only_ tablet sizes—nothing smaller, nothing bigger—we could do this with the `and` keyword:
```css
@media (min-width: 550px) and (max-width: 1099.99px) {
  /* Tablet-only styles */
}
```
## Managing breakpoints

Unfortunately, CSS doesn't have any built-in way to manage breakpoints. CSS has media queries, and media queries always take "raw" values (like 550px), not breakpoints.

The _good_ news is that just about every CSS preprocessor and framework has a solution for this problem.

Here's how I've solved this using styled-components. First, I create some variables in JS:
```js
// constants.js

// For this example, I'm going mobile-first.
const BREAKPOINTS = {
  tabletMin: 550,
  laptopMin: 1100,
  desktopMin: 1500,
}

const QUERIES = {
  'tabletAndUp': `(min-width: ${BREAKPOINTS.tabletMin}px)`,
  'laptopAndUp': `(min-width: ${BREAKPOINTS.laptopMin}px)`,
  'desktopAndUp': `(min-width: ${BREAKPOINTS.desktopMin}px)`,
}
```
Because our breakpoints are in no-device-land, it makes it a bit easier to name things. `550px` is the smallest possible size for a tablet, so we can name the breakpoint `tabletMin`. The media query can be named `tabletAndUp`, since it includes all tablets, laptops, and desktops.

When I want to use a media query, I can interpolate these values:
```css
import { QUERIES } from '../../constants';

const Wrapper = styled.div`
  padding: 16px;

  @media ${QUERIES.tabletAndUp} {
    padding: 32px;
  }
`;
```
If you're not used to it, this might feel like total anarchy. It doesn't look at all like valid CSS!

The important thing to remember is that styled-components will process this string _before_ the browser tries to parse it. By the time the browser receives the CSS, it's a 100%-normal media query.

**These names are a lie(warning)**
For convenience, we've decided to name our media queries based on device categories. It's important to recognize that they won't _actually_ map 1:1 to these devices.

When we talk about "popular screen resolutions", like in our data visualization above, we're talking about the monitor's maximum resolution. A popular desktop screen resolution is 1920x1080, but the user might be viewing our app in a small window sized at 500x600. They'd fall into our "phone" bucket, despite being on a desktop computer.

Similarly, tablets are often used in "landscape mode", which tends to push their resolution into the laptop bucket. But, tablets in landscape mode can now "multi-task", which might push each half into the "phone" bucket!

The point is that we don't actually know what type of device the user is using. Our breakpoints are _assumptions_, and those assumptions aren't always right.

If we use width-based media queries as-intended, this shouldn't cause any problems. But we do need to be careful not to "over-reach", and tweak things that shouldn't be tweaked based on window width.
Here's an example of some CSS that is **not** using a min-width media query as intended:
```css
@media (min-width: 1100px) {
  button:hover {
    text-decoration: underline;
  }
}
```
The biggest problem with this code is that we're depriving some users of the hover state. If a desktop keyboard-and-mouse user is running a 1000px-wide window, they might not realize that this button is interactive (depending on other styles / feedback).

It also suggests a flaw in our mental model: not everyone using a desktop computer uses a mouse/trackpad.

As we saw in the last lesson, the `hover` and `pointer` queries are a better fit for these sorts of situations.

**styled-component themes(info)**

styled-components has a “theming system”. This allows us to access theme variables like colors and breakpoints without needing to import our constants.

We haven't focused on its built-in theming system for a couple reasons:

- It's too specific to styled-components.
- To understand how it works, you need to be familiar with React context, an advanced API.
- The benefits are relatively modest.
## Rem breakpoints

As I mentioned [a couple lessons ago](https://courses.joshwcomeau.com/css-for-js/05-responsive-css/04-media-queries#media-queries-and-units), I've started to use rem-based media queries in my own work.

If you use something like styled-components, you can create rem-based breakpoints using pixel values like this
```js
// constants.js

// Values in pixels:
const BREAKPOINTS = {
  tabletMin: 550,
  laptopMin: 1100,
  desktopMin: 1500,
}

// Converted to rems:
const QUERIES = {
  'tabletAndUp': `(min-width: ${BREAKPOINTS.tabletMin / 16}rem)`,
  'laptopAndUp': `(min-width: ${BREAKPOINTS.laptopMin / 16}rem)`,
  'desktopAndUp': `(min-width: ${BREAKPOINTS.desktopMin / 16}rem)`,
}
```
Before, our `tabletAndUp` query was equal to `min-width: 550px`. Now, it's equal to `min-width: 34.375rem`.

## Deviating from our breakpoints

You might be wondering: is it bad to pick "one-off" values for our media queries? What if we have a UI that needs to change CSS at a different viewport width?

No matter how perfect our breakpoints are, they'll never be suitable for 100% of cases. **I think it's totally fine to use the occasional custom value**.

It's important not to get too caught up in “best practices”. Sometimes, you need to do something custom in order to achieve the best possible UX, and that should be encouraged!

That said: if you find that you need to use custom values often, it's probably a sign that your breakpoints are at the wrong spots. I'd say that a well-matched set of breakpoint values should be used 80-90%+ of the time.
# CSS Variables

CSS variables are one of the most exciting developments to come to CSS of all time. They're **incredibly powerful**, and they unlock lots of really effective workflows.

We've already seen them briefly, but in this lesson we'll go deeper, to understand exactly what they are, how they work, and why they're so great.
## Custom properties
#ImportantPoint 
The first thing to understand about CSS variables is that they function exactly like _properties_ (like `display`, `color`, etc). We aren't setting a variable, we're creating a brand-new property:
```css
strong {
  display: block;
  color: red;
  --favorite-food: tomato;
  --temperature: 18deg;
}
```
Custom properties always start with two dashes (`--`), to differentiate them from built-in properties.
#ImportantPoint 
Custom properties are also inheritable, just like `color` or `font-size`. Inspect the anchor tag in your devtools to see what I mean:
```css
<style>
  main {
    font-size: 2rem;
    --favorite-food: tomato;
  }
</style>

<main>
  <section>
    <a>Hello World</a>
  </section>
</main>
```
The anchor inherits both the font-size _and_ our custom `--favorite-food` property:
![[Pasted image 20231217190334.png]]
Of course, `--favorite-food` doesn't have any effect on its own; the CSS rendering engine doesn't make use of that property. But we can access its value using the `var` function:
```css
<style>
  main {
    font-size: 2rem;
    --favorite-food: tomato;
  }

  a {
    padding: 32px;
    background-color: var(--favorite-food);
  }
</style>

<main>
  <section>
    <a>Hello World</a>
  </section>
</main>
```
(I'm being a bit cheeky here; `tomato` is one of the [140 named HTML colors](https://htmlcolorcodes.com/color-names/). Most foods don't actually work as colors.)

## Not global
#ImportantPoint 
A common misconception is that CSS variables are "global". When we attach a CSS variable to an element, it's only available to that element and its children:
```html
<style>
  a {
    --color: red;
  }

  main {
    color: var(--color);
  }
</style>

<main>
  <section>
    <a>Hello World</a>
  </section>
</main>
```
The variable `--color` is only available to the `a` and its children. When `main` tries to use it, it has no effect, since that property was defined lower in the tree.
The reason for this misconception, I believe, is that CSS variables are often hung on `:root`:
```css
:root {
  --color-primary: red;
  --color-secondary: green;
  --color-tertiary: blue;
}
```
`:root` is an alias for the `html` tag, the “root” of the HTML document. By attaching our CSS variables to the top-level element, they're inherited through the entire DOM tree.

But we can attach CSS variables to _any_ selector! It doesn't _have_ to be the root `html` tag. I frequently use CSS variables lower down in the tree. We'll see an example of this shortly.

**Disabling inheritance(info)**
By default, all CSS variables are inheritable. This is why CSS variables hung on `:root` are available globally.

But what if we _only_ want our CSS variable's value to only be available to the element in question, not any of its children?
An exciting new API makes this possible. Here's what it looks like:
```html
<style>
  @property --text-color {
    syntax: '<color>';
    inherits: false;
    initial-value: black;
  }

  main {
    --text-color: deeppink;
    color: var(--text-color);
  }

  section {
    color: var(--text-color);
  }
</style>

<main>
  This text is just inside main.
  <section>
    This text is inside section.
  </section>
</main>
```
If you're viewing this in a supported browser, you'll notice that the first line is coloured pink, but the second line is black
If you set `inherits:true` , both the lines will be over-ridden with the latest `--text-color` property
```html
<style>
  @property --text-color {
    syntax: '<color>';
    inherits: true;
    initial-value: black;
  }

  main {
    --text-color: deeppink;
    color: var(--text-color);
  }

  section {
    color: var(--text-color);
  }
</style>

<main>
  This text is just inside main.
  <section>
    This text is inside section.
  </section>
</main>
```
> 	In above case both lines will be in `deeppink`
## Default values

Our `var` function takes two arguments. The second argument is a default value:
```css
.btn {
  padding: var(--inner-spacing, 16px);
}
```
If our `.btn` element or one of its ancestors assigns a value to the `--inner-spacing` property, that value will be used. Otherwise, it'll use a fallback of 16px.
## Reactive properties

If you've used a CSS preprocessor like Sass or Less, you might be thinking _“So what? We've had variables in preprocessors for years!"_.

The big difference is that CSS preprocessors can only be used to generate _initial_ values. A `.scss` file will get compiled into a `.css` file, and the variables are resolved during that process, before the code ever runs in the browser.

**With CSS variables, however, the variable exists in the browser.** This means we can dynamically change its value with JavaScript.

Check this out:
```js
<style>
  button {
    font-size: var(--inflated-size);
  }
</style>

<button>Click me</button>

<script language="javascript">
  let fontSize = 1;
  const button = document.querySelector('button');
  
  button.addEventListener('click', () => {
    fontSize += 0.25;
    button.style.setProperty(
      '--inflated-size',
      fontSize + 'rem'
    );
  });
</script>
```
CSS variables are _reactive_—when their value changes, any properties that reference that value also change. In this case, clicking the button causes us to update the value for `--inflated-size`, which automatically updates the button's `font-size` property.

Being able to mutate variables from within JS opens lots of exciting doors.

As we learned about [earlier in the course](https://courses.joshwcomeau.com/css-for-js/03-components/08-dynamic-styles), styled-components has its own built-in solution for dynamic styles, but I prefer to use platform features whenever possible. The skills I learn with CSS variables will work with _any_ tool or framework.

(That said, styled-components' interpolation syntax is more powerful, and can do things not possible with CSS variables. For example, we can interpolate in a whole chunk of CSS based on a condition, or dynamically create media queries. So it's worth knowing about both strategies, if you work with styled-components!)
## Responsive values

We can use the fact that CSS variables are reactive to our advantage when it comes to responsive design.

As an example, let's look at interactive mobile UI elements like buttons or inputs.

As we saw earlier, our fingers aren't particularly precise instruments when it comes to tapping on things (it's a _coarse_ pointer, in official terms). We've all experienced the frustration of trying to tap on a super-tiny checkbox, and not being able to hit it.

in [Apple's Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/adaptivity-and-layout/), they recommend a minimum tap size of 44×44px.

Our CSS for a button might therefore look something like this:
```css
const FancyButton = styled.button`
  /* Other styles omitted for brevity */

  @media (pointer: coarse) {
    min-height: 44px;
  }
`;
```
This works well enough, but in reality, we'll have many other components that need to implement the same thing! Maybe a `TextInput` component as well, with a default min-height:
```css
const TextInput = styled.input`
  /* Other styles omitted for brevity */
  min-height: 32px;

  @media (pointer: coarse) {
    min-height: 44px;
  }
`;
```
We can use CSS variables here to make our life a bit easier.

First, let's define a new global CSS variable, `--min-tap-height`:
```js
const GlobalStyles = createGlobalStyle`
  @media (pointer: coarse) {
    html {
      --min-tap-height: 44px;
    }
  }
`;
```
_We only define this variable for folks with a coarse pointer._ We'll leave the variable undefined for everyone else.

Then, we can use this property inside our styled-components:
```js
const FancyButton = styled.button`
  min-height: var(--min-tap-height);
`;

const TextInput = styled.input`
  min-height: var(--min-tap-height, 32px);
`;
```
If the user is using a mouse or other “fine” pointer, `--min-tap-height` will never be set. `FancyButton` won't have a `min-height`, and `TextInput` will fall back to the default value of 32px.

But, if the user is using a finger or similarly “coarse” pointer, `--min-tap-height` will be set to `44px`, and that value will be used in both components.

This is a really handy trick, since it means we aren't saddling individual components with any media queries / responsive logic. At the same time, individual components are still able to set default `min-height` values using the fallback syntax.

**Tap target trickery(info)**

In some cases, we may want to be a bit more subtle with our tap target sizes. In Module 9, we'll learn [an alternative way](https://courses.joshwcomeau.com/css-for-js/09-little-big-details/06-mobile-ux#increasing-target-sizes) to increase tap target sizes without affecting the design.
### Stacked cards

This UI features a stacked set of cards. Depending on the viewport size, we want to apply different styles:
Demo video : https://courses.joshwcomeau.com/cfj-mats/stacked-cards.mp4
As it stands, we're solving this problem by setting new values for `padding`, `gap`, and `border-radius` inside media queries. For example, here's how we're changing `padding` on `main`:
```css
main {
  padding: 8px;
}

@media (min-width: 350px) {
  main {
    padding: 16px;
  }
}

@media (min-width: 500px) {
  main {
    padding: 32px;
  }
}
```
Your mission in this exercise is to see if you can simplify the CSS a bit by using CSS variables.

**Acceptance criteria:**
- A CSS variable should hold the spacing value, so that the amount of `padding`/`gap`/`border-radius` can be changed by editing a single value.
- The media queries should not directly change `padding`/`gap`/`border-radius`.

Solution Video : https://player.vimeo.com/video/541345681
Solution screen shot :
![[Pasted image 20231217192949.png]]
#ImportantPoint 
Notice that we haven't changed `gap` property or `padding` , we are updating `--spacing` value inside `media` query

# Variable Fragments

One of the coolest things about CSS variables is that they're like lego blocks. We can use them as pieces or fragments.

Take a look at this example:
```css
<style>
  body {
    --standard-border-width: 4px;
  }

  strong {
    --border-details: dashed goldenrod;
    border:
      var(--standard-border-width)
      var(--border-details);
  }
</style>

<strong>Hello World</strong>
```
We can combine multiple variables to form a single property value. In this case, the end result is the declaration `border: 4px dashed goldenrod`. **As long as the final product is valid, we're golden(rod).**

This works because CSS variables are evaluated _when they're used_, not when they're defined.

Taking this a step further: CSS variables are _composable_:
```css
<style>
  body {
    --pink-hue: 340deg;
    --blue-hue: 275deg;
    --intense: 100% 50%;
    
    --color-primary: hsl(
      var(--pink-hue)
      var(--intense)
    );
    --color-secondary: hsl(
      var(--blue-hue)
      var(--intense)
    );
  }

  strong {
    color: var(--color-primary);
  }
  a {
    color: var(--color-secondary);
  }
</style>

<p>
  Hi <strong>Mario</strong>!
  <br />
  The princess is in <a href="">another castle</a>.
</p>
```
The `--color-primary` variable is built up using the variables `--pink-hue` and `--intense`. This helps us keep our code DRY, and makes it possible to build rich structures that make it easy to tweak entire color themes!

## Dark mode settings:
video : https://player.vimeo.com/video/541404352
# The Magic of Calc

For almost a decade now, CSS has had the ability to do math!
```css
.something {
  width: calc(100px + 24px);
  height: calc(50px + 25px * 4);
}
```
The expression will be evaluated, and the end result will be used as a value. The above example is equivalent to:
```css
.something {
  width: 124px;
  height: 150px;
}
```
We can use 4 mathematical operators:

- `+` (addition)
- `-` (subtraction)
- `*` (multiplication)
- `/` (division)
**Why would we want to do this?** For starters, it can be useful for “showing your work”. For example, which of these two declarations make it clearer that you want `.something` to take up 1/7th of the available space?
```css
.something {
  width: 14.286%;
  width: calc(100% / 7);
}
```
The _real_ magic of `calc`, though, is that **it allows us to mix units:**
```css
.spill-outside {
  margin-left: -16px;
  margin-right: -16px;
  width: calc(100% + 16px * 2);
}
```
We're saying that this element should take up `100%` of its containing block's width, plus an extra 32 pixels. Pretty neat, right?

`calc` gets even cooler when we **combine it with CSS variables.** Let's take another look at the [“stacked cards” exercise](https://courses.joshwcomeau.com/css-for-js/05-responsive-css/08-css-variables#stacked-cards):
On small screens, `--spacing` is equal to 8px, and we use that value for 4 different properties. But do we _really_ want to use the exact same values for them?

We can use `--spacing` as an input, and transform it to a proportional value using `calc`:
```css
article {
  padding: var(--spacing);
  border-radius: calc(var(--spacing) / 2);
  /*
    8px -> 4px
    16px -> 8px
  */
}
```
Our equation can be more complex if we want to tweak the relationship between the values:
```css
article {
  border-radius: calc(var(--spacing) / 2 + 2px);
  /*
    8px -> 6px
    16px -> 10px
  */
}
```
## Unit conversion

We've talked about how the `rem` unit is better-suited for setting font sizes, because it can be increased or decreased by the user. But it can be harder to think in terms of rems, since they're generally multiples of 16 rather than 10.

We can use calc to convert pixels to rems.

Let's presume we want our `h2` to be 24px:
Assuming we haven't set a `font-size` on our HTML tag, 1rem will be equal to 16px. We can convert from pixels to rems by dividing by 16:
Instead of doing this math ourselves, we can let CSS do it for us, using `calc`:
```css
h2 {
  font-size: calc(24 / 16 * 1rem);
}
```
The very first number, `24`, is our value in pixels. We can use this pattern anywhere we want to be responsible and use the `rem` unit, without having to change our mental model.

## Calculating colors and gradients

As we've learned, the HSL color model is awesome because it gives us an intuitive way to reason about color.

We can leverage that intuition to create color palettes with CSS `calc`:
```css
<style>
  :root {
    --red-hue: 0deg;
    --intense: 100% 50%;
  
    --red: hsl(
      var(--red-hue) var(--intense)
    );
    --orange: hsl(
      calc(var(--red-hue) + 20deg)
      var(--intense)
    );
    --yellow: hsl(
      calc(var(--red-hue) + 40deg)
      var(--intense)
    );
    --pinkred: hsl(
      calc(var(--red-hue) - 20deg)
      var(--intense)
    );
    --pink: hsl(
      calc(var(--red-hue) - 40deg)
      var(--intense)
    );
  }
</style>

<div class="row">
  <div
    class="demo-box"
    style="background: var(--pink)"
  ></div>
  <div
    class="demo-box"
    style="background: var(--pinkred)"
  ></div>
  <div
    class="demo-box"
    style="background: var(--red)"
  ></div>
  <div
    class="demo-box"
    style="background: var(--orange)"
  ></div>
  <div
    class="demo-box"
    style="background: var(--yellow)"
  ></div>
</div>
```
To explain what's going on here: we have a default hue, 0°. On the color wheel, 0° is "pure red". As we increase the hue, the color becomes more and more orange, and then yellow. If we spin the color wheel the other way, we veer towards pink, purple, blue.

In the code above, we're using `calc` to come up with new hues for each color. The 5 values used are -40°, -20°, 0°, 20°, and 40°.

**Negative values?(info)**

When we talk about color hues in HSL, we're generally thinking of them in the range of 0° to 360°. How do negative values fit in?

The trick here is that _hue is a circular value_. It's like rotating in a circle. If you rotate 360°, you're right back where you started. If you rotate 720°, it's the same thing, you've just done 2 full circles instead of 1.

If 0° and 360° are the same value, it stands to reason that -20° would be the same value as 340°. Happily, we can use these values in CSS!

Being able to use `calc` with color fragments is _really_ handy when it comes to CSS gradients.

We'll learn all about gradients towards the [end of the course](https://courses.joshwcomeau.com/css-for-js/09-little-big-details/05-gradients), but essentially, a linear gradient has 3 components:
- A direction
- A start color
- An end color
(We can also specify more than 2 colors, but for now, we'll stick with 2).

Here's an example:
```css
<style>
  .box {
    width: 150px;
    height: 150px;
    border-radius: 2px;
    background: linear-gradient(
      45deg,
      hsl(-30deg 100% 50%),
      hsl(30deg 100% 50%)
    );
  }
</style>

<div class="box" />
```
Exercise solution Video : https://player.vimeo.com/video/543299854
[View the code](https://courses.joshwcomeau.com/playground/css-variables/solution) created in this video.

You can also view the code for the images shown above:

- [Paintchip](https://courses.joshwcomeau.com/playground/css-variables/paintchip)
- [Windows](https://courses.joshwcomeau.com/playground/css-variables/windows)
- [Beach Day](https://courses.joshwcomeau.com/playground/css-variables/beachday)
# Viewport Units

Did you know that CSS has types?

Every value that you might think to use, like _24px_ or _10%_ or _#FF0000_, has a type. It might be a `<length>` or a `<color>` or an `<angle>`, or one of [many other possible types](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Types).

Our CSS properties, meanwhile, accept values of specific types. `background-color` accepts a `<color>`, so `hsl(0deg 100% 50%)` is a valid value, but `100%` isn't.
The `<length>` type is one of the most common. Properties like `width` or `padding` accept `<length>` values, and it contains units like _px_ and _em_ and _rem_, and more obscure ones we'll cover later, like _ch_.

It also includes _viewport units_, the subject of this lesson.

There are two main viewport units: `vw` (Viewport Width) and `vh` (Viewport Height).

`1vw` is equivalent to 1% of the viewport width. For example:
```css
.box {
  width: 10vw; /* 10% of the viewport width */
  height: 25vh; /* 25% of the viewport height */
}
```
We can use these units with `width` and `height`, but the _really_ cool thing is that we can use them with _any property that accepts `<length>` units_.

In this playground, we use it to increase the distance between letters:
```css
<style>
  .heading {
    letter-spacing: 2vw;
  }
</style>
<h2 class="heading">Resize me!</h2>
```
**Digging deeper(info)**

You can learn much more about CSS' type system, and how it helps keep us in check, in Eric Bailey's awesome article, [“CSS is a Strongly Typed Language”](https://css-tricks.com/css-is-a-strongly-typed-language/).
## The mobile height issue

The `vh` unit in particular is often used to solve one annoying problem: making sure that an element is exactly as tall as the viewport. No taller, no shorter.

Unfortunately, it doesn't quite work as you'd expect on mobile. To understand why, we need to look at how modern mobile browsers work.

When a page is loaded on a mobile browser, it includes an "expanded" browser UI: the address bar is tall and tappable, and an array of buttons line up along the bottom. Once you start scrolling, though, the browser UI slips away, making more space for the content:
![[Pasted image 20231217213917.png]]
The screenshots are from Safari on my iPhone X, but Chrome on Android has a similar effect.

When Apple first introduced this "slide-away" UI feature, the `vh` unit was dynamic: it would grow to match the viewport height when the UI slid away. This led to some really bad experiences, though: having elements shift and resize when you start scrolling is unexpected, and led to some very janky experiences.

So nowadays, the `vh` unit **always refers to the largest possible height**. In our example above, `100vh` will always equal 750px, even when the page first loads, and the viewport is actually only 635px tall.

If you set an element to have `100vh`, therefore, it won't fit on the screen:
You can try this demo yourself, on your mobile device, at this URL:

- [courses.joshwcomeau.com/demos/full-height-vh](https://courses.joshwcomeau.com/demos/full-height-vh)
How do we work around this? We have a few options:

1. We can use a JS-based solution to change how the `vh` unit works. The most popular solution is [viewport-units-buggyfill](https://github.com/rodneyrehm/viewport-units-buggyfill). Personally, I wouldn't recommend this unless you _really_ need the `vh` unit to work. Even if it works perfectly today, it could break when browsers update (and imagine how hard it would be to trace that bug!)

2. We can use the [percent-based trick we learned in Module 1](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/11-height), passing percentages down so that they can be used where you need them.

3. We can tweak our designs so that they don't need to fill the viewport exactly. Fixed-height designs tend to be rigid and flaky; better to have a fluid design that doesn't have such a strict height requirement.
The `vh` unit can still come in handy, but it probably shouldn't be used in this exact situation.

**Dynamic viewport units(success)**

So, browser vendors are aware of this issue, and they've been working on fixing it!

There are several new units we can use:

- `svh` — Small Viewport Height
- `lvh` — Large Viewport Height
- `dvh` — Dynamic Viewport Height

The `lvh` unit works like the `vh` unit does; it always refers to the _full_ viewport height, once the browser UI has shrunk down.

`svh` always refers to the _smaller_ height, the height that first shows when the page loads.

Finally, `dvh` will dynamically adjust as the viewport height changes. This is the way our `height: 100%` alternative works.

When I originally created this course, these units were only in a very small % of browsers. As I write this update in April 2023, these units have [shipped in all major browsers](https://caniuse.com/viewport-unit-variants), and are available for 86% of users!

It's still worth adding a `vh` fallback for the other 14% of people. Here's how I recommend using viewport units today:
```css
.some-element {
  height: 100vh; /* Fallback for legacy users */
  height: 100dvh;
}
```
Unfortunately, I haven't had the chance to update the rest of this course. So, anywhere you see me use `vh`, pretend I'm also adding a `dvh` declaration!
## The desktop scrollbar issue

Unfortunately, `vh` isn't alone in having some problems: the `vw` unit isn't perfect either!

Here's the problem: `vw` refers to the viewport width _not counting the scrollbar_.

On mobile, this is fine, because the scrollbar floats transparently above the content. On desktop, though, the scrollbar usually takes up its own space, within the viewport. The exact width depends on the platform and on the styling.

This means that if we set an element to stretch to `100vw`, and our scrollbar is 15px wide, we'll wind up with 15px of horizontal overflow:
You can also [view a live example](https://courses.joshwcomeau.com/demos/100vw) of this issue, though the issue will only be present on desktop (on mobile, scrollbars don't take up any width).
**Enabling scrollbars on macOS(info)**

As we saw in the [“Overflow” lesson](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/14-overflow#scroll), macOS treats scrollbars a little bit differently from other operating systems.

If you're using a device with horizontal scroll, like a trackpad or a magic mouse, macOS will _hide scrollbars by default_, and show them as a semi-transparent overlay when needed.

We should update this setting so that our experience matches that of our users. It can be done in the system preferences. Set “Show scroll bars” to “Always”:

**Can we fix this?** Sorta, but not really. 😬

In an earlier version of this lesson, I included a JS snippet that would dynamically measure the width of the scrollbar, and make it available to us through a CSS variable. Since publishing this lesson, though, I've come to realize that it's not the best idea. This is for several reasons:

1. If you're using "server-side rendering" in a JS framework like React, there will be a delay before the JS runs, meaning that the value won't be defined at first, potentially breaking the layout.
2. If the page loads without a scrollbar, but later introduces one (eg. after fetching data from the network), the scrollbar width won't be defined.
3. While it _seems_ to work pretty well in most situations I've tried, there are probably more edge-cases I haven't run into.

This is a bummer, but honestly, **I don't really find the `vw` unit super useful.** As we learned about in [Module 1](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/11-height), block-level elements will expand horizontally, making it much easier to use percentage-based widths compared to percentage-based heights.

The one common use case I've seen for `vw` is to "break out" of parent containers, but I have a [grid-based approach](https://courses.joshwcomeau.com/css-for-js/07-css-grid/15-full-bleed) that feels much less hacky to me.

I'll include my JS snippet below, but please use it with caution:

**Legacy JS snippet(warning)**
Here's the content this lesson used to contain, showing how to dynamically compute the scrollbar width and store it in a CSS variable:

First, we need to calculate the width of the scrollbar. We can do so with this expression:
```css
const scrollbarWidth =

  window.innerWidth - document.documentElement.clientWidth;
```

`window.innerWidth` refers to the viewport width; it doesn't care about scrollbars. `documentElement.clientWidth`, however, refers to the usable space within the document.

Here's an example: Let's say our window is 500px wide, and our scrollbar is taking up 20px. `window.innerWidth` will be `500`, and `clientWidth` will be 480. By subtracting, we get the difference of `20`.

If there is no scrollbar, or the scrollbar is a non-blocking overlay, `scrollbarWidth` will be `0`, since our two width values will be identical.

Now that we know how wide the scrollbar is, we can assign it to a CSS variable:
```css
document.documentElement.style.setProperty(
  '--scrollbar-width',
  scrollbarWidth + 'px'
);
```
By attaching this CSS variable to the `documentElement`, we make it globally available (it's the same thing as targeting `html` in CSS).

With the help of magical `calc`, we can work with `vw` units without worrying about scrollbars:
```css
.wrapper {
  width: calc(100vw - var(--scrollbar-width));
}
```
We can even take this a step further, by assigning that `calc` expression to a variable:
```css
html {

  --full-width: calc(100vw - var(--scrollbar-width));
}
.wrapper {

  width: var(--full-width);
}
```
We want to make sure to set the `--scrollbar-width` as early as possible.

## vmin and vmax

There are two more nifty viewport units: `vmin` and `vmax`.

`vmin` will refer to the _shorter dimension_, while `vmax` refers to the longer one. On a portrait phone, `50vmin` is equivalent to `50vw`, but on a landscape monitor, `50vmin` would be equal to `50vh`.
```css
<style>
  .box {
    width: 50vmin;
    height: 50vmin;
    border: solid deeppink;
  }
</style>

<div class="box">Resize me</div>
```
These units are nifty, but honestly, I don't find myself reaching for them that often. If they have practical everyday use cases, I haven't discovered them yet
# Clamping Values

Let's suppose we have a column of text, and we want it to occupy 65% of the viewport:

We can do that with a percentage-based width, and some auto-margins for centering:

```css
.column {
  width: 65%;
  margin-left: auto;
  margin-right: auto;
}
```

This works great for the sizes shown in the GIF, but it doesn't scale well beyond that. On large screens, the lines are much too long to read comfortably:

![](https://courses.joshwcomeau.com/cfj-mats/clamping-values-65-percent-wide.png)

Meanwhile, on phones, the column is much too narrow:

![](https://courses.joshwcomeau.com/cfj-mats/clamping-values-65-percent-thin.png)

We can constrain this value using our friends `min-width` and `max-width`:
```css
<style>
  .column {
    width: 65%;
    min-width: 500px;
    max-width: 800px;
    margin: 0 auto;
  }
</style>
```
(Depending on your screen size, you might need to hit the Toggle fullscreen icon to make the playground full-screen, to give you the space to see this effect, as you resize the "Result" pane.)

The really cool thing about `min-width` and `max-width` is that **we can mix units**. We can set our column to take up 65% of the available space, but limit it between 500px and 800px:

There's a problem though. When we reduce the viewport even further, we cause a horizontal overflow:

Why does this happen? Well, we've given our element a _minimum width_ of 500px! Phone screens are narrower than that.

On mobile, we want our `.column` to fill the entire available width, which is the default behaviour of block-level elements. So, we can solve this by moving our styles to within a media query:
```css
@media (min-width: 550px) {
  .column {
    width: 65%;
    min-width: 500px;
    max-width: 800px;
  }
}
```

We set the query to trigger at 550px, 50px larger than our minimum width. We need to add a 50px buffer because of the page's built-in padding/margin. Otherwise, we'll still overflow slightly around 500px wide:

![A screenshot showing how a 500px column with 8px of padding on each side overflows a 500px viewport](https://courses.joshwcomeau.com/cfj-mats/clamping-values-500px-overflow.png)

This feels like a code smell to me. 550px is a "magic number", and we shouldn't assume that it'll always be the right value; in the future, we might tweak the page's padding, and inadvertently break this UI!

Fortunately, we have another option: `clamp`. Here's what it looks like:
```css
<style>
  .column {
    width: clamp(500px, 65%, 800px);
    max-width: 100%;
    margin: 0 auto;
  }
</style>
```
`clamp` takes 3 values:

1. The minimum value
2. The ideal value
3. The maximum value

It works quite a bit like the trio of `min-width`, `width`, and `max-width`, but it combines it into _a single property value_. In other words, these two rules are functionally identical:
```css
/* Method 1 */
.column {
  min-width: 500px;
  width: 65%;
  max-width: 800px;
}

/* Method 2 */
.column {
  width: clamp(500px, 65%, 800px);
}
```

By moving our built-in constraints to the `clamp` value, we _free up_ `max-width`. Our solution combines them:
```css
.column {
  width: clamp(500px, 65%, 800px);
  max-width: 100%;
}
```

In this snippet, we're essentially applying _two_ maximum widths: `800px` and `100%`. Our `.column` element will never be larger than 800px _or_ 100% of the available space.

This is handy, but it's only one example of the cool things `clamp` can do.

## It works with other properties!

Historically, we've only been able to limit widths and heights. There is no `min-padding`/`max-padding` or `min-font-size`/`max-font-size`
The amazing thing about `clamp` is that _it's a value_, not a property. This means that it can be used with just about any property!

Here's a silly example:

```css
<style>
  .box {
    border: solid pink;
    border-width: clamp(4px, 4vw, 22px);
    background: navy;
    width: 100px;
    height: 100px;
    border-radius: 50%;
  }
</style>

<div class="box"></div>
```

We'll see how this trick can be used to create fluid typography in [an upcoming lesson](https://courses.joshwcomeau.com/css-for-js/05-responsive-css/15-fluid-typography).

## Min and max

`clamp` allows us to specify a lower _and_ upper bound. But what if we only want to limit one end?

There are `min` and `max` functions we can use as well:
```css
.box {
  padding: min(32px, 5vw);
}
```

This works just like [`Math.min`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/min) in JavaScript—it evaluates to whichever value is smaller.

In this example, our `.box` will have dynamic padding that scales with the viewport width, but only until it reaches 32px; it won't grow larger than that.

**Browser support(info)**

`clamp` has [very good browser support](https://caniuse.com/css-math-functions). It's supported in the latest versions of all major browsers, though it's notably absent in Internet Explorer.

For a while, `clamp` was less supported than its sibling functions `min` and `max`, because of Safari. Starting in Safari 13.4, however, there's no difference: all browsers support `min`, `max`, and `clamp` equally well.

## Exercises

### Max-height hero

A popular pattern is to have a "hero" that fills most of the viewport:

![An example of a hero, with some text over a large space photo](https://courses.joshwcomeau.com/cfj-mats/hero-demo.png)

Unfortunately, these types of user interfaces generally suffer from two problems:

**1.** If the font size is cranked up and/or if additional content is added, it can overflow onto the subsequent content:

![A version of the exercise with very-large text, overflowing and making a big mess](https://courses.joshwcomeau.com/cfj-mats/vh-hero-overflow.png)

**2.** On large & tall screens, it looks a little silly:

![A large desktop screen with a bunch of dead space around the heading](https://courses.joshwcomeau.com/cfj-mats/vh-hero-too-tall.png)

Update the playground below so that it meets these constraints:

- A default height of `80vh`
- A max height of 500px, to prevent it from getting too big on taller viewports:
- If the content doesn't fit, the hero should grow to prevent an overflow. You can test this by duplicating the content a bunch:

Solution Video : https://player.vimeo.com/video/538442101

**Correction:** At around 6:15, I say "500px is the _bigger_ of these two values", but I meant to say _smaller_.
# Scrollburglars

A scrollburglar is my cute made-up name for a common phenomenon: A webpage has an accidental horizontal scrollbar that allows you to scroll by a few pixels.

Frustratingly, there isn't a single cause for this phenonenon. They can be triggered by lots of different things. Some examples:

- An element has an explicit width that is too large to fit in the parent container.
- A replaced element (eg. a video or an image) is used without constraining its width to fit in the parent container.
- A really long word like “disestablishmentarianism” forces an element to be too wide for its parent container.
- An element is explicitly pulled outside of the parent (positioned elements with negative left/right values, elements with negative margin, etc).
Our first step when solving these sorts of issues is to find the specific element causing the overflow, and fix it so that it stops doing that.

Our second (and often neglected) step is to try and find a way to prevent this issue from reoccuring.
I've created a Git repository which has 3 different projects, each with a horizontal scrollbar on mobile. You can access it here:

- [https://github.com/css-for-js/scrollburglars](https://github.com/css-for-js/scrollburglars)

The exercises are sorted by difficulty. The 2nd and 3rd are quite a bit more challenging than the first.

Why would I ask you to try solving a problem you probably won't be able to solve? Because there is value in this process. **Struggling with a problem is the best way to ensure that you learn.** If I start with an explanation, and you breeze through the exercises, that knowledge probably won't be absorbed into your brain. In a month, when you encounter a scrollburglar in the real world, you won't remember how you solved it.

This is an increasingly-popular practice. It's known as **productive failure**. From a [2019 scientific article](https://www.nature.com/articles/s41539-019-0040-6):

> In Productive Failure, the conventional instruction process is reversed so that learners attempt to solve challenging problems ahead of receiving explicit instruction. While students often fail to produce satisfactory solutions (hence “Failure”), these attempts help learners encode key features and learn better from subsequent instruction (hence “Productive”).

When I worked at Khan Academy, we spoke a lot about cultivating a “growth mindset”. A growth mindset is the belief that our brains are elastic, that we become smarter through practice, and that _failure is the fastest way to learn_.

If you're interested in cultivating a growth mindset, I recommend this [free series of lessons](https://www.khanacademy.org/ela/cc-4th-reading-vocab/x5ea2e43787f7791b:cc-4th-growth-mindset/x5ea2e43787f7791b:building-knowledge/a/growth-mindset--unit-intro-4) from Khan Academy.

All of that said, this is your course, and I encourage you to use it in whichever manner is most worthwhile for you.
### Exercise 1: Recut

Solution video: https://player.vimeo.com/video/539866636
Solution git: [View the final code on Github](https://github.com/css-for-js/scrollburglars/compare/solution?expand=1#diff-afdaa6dae60f7df96d5dc3d78119295565adde6a6e19c5272f225385c1dfdb3cR67)

**An alternative solution?(info)**

Several students have asked if this is an acceptable solution:
```css
.max-w-md {
  max-width: 28rem; /* Unchanged */
  width: 100%;
}
```
By setting `width: 100%`, the image will shrink if the available space is less than 28rem. It _appears_ to satisfy all of the conditions!

But there's a (slight) catch.
In this particular case, the image in question has an intrinsic size of 650px. We're clamping it to be 28rem wide, which (at a default font size) is equal to 448px.
![[Pasted image 20231217225546.png]]
But, **what if we put a smaller image in?** For example, suppose this new image has an intrinsic width of 300px?

![[Pasted image 20231217225612.png]]
In this case, we _don't_ want to apply `width: 100%`, because that will _stretch out_ the image, to fill the 448px of available space. This will make the image appear fuzzy, like a low-res image blown up to fit on a billboard.

So yeah, the reason I chose to set `max-width: min(28rem, 100%)` is that we never have to worry about stretching out smaller images, because I'm only concerned with clamping it beyond a specific size.

### Exercise 2: Warp and Weave

Solution video: https://player.vimeo.com/video/539660514
Solution git : [View the final code on Github](https://github.com/css-for-js/scrollburglars/compare/solution?expand=1#diff-7f2f6395f528faf446c66a7912ff818baf2f754ac25dbc548237b47fdf86a8e4R7169)

### Exercise 3: Blog example

This exercise solution is broken into two parts, because there are multiple possible solutions.

Part 1:

Solution video : https://player.vimeo.com/video/541321717
Solution Git : [View the final code on Github](https://github.com/css-for-js/scrollburglars/compare/solution?expand=1#diff-e979ea9681f20b1bc6cfed7d58f381d4e14e4d114b637e3b2f8e05c9c4186886R160)
#ImportantPoint 
`Sticky` property doesn't work if its parent has `overflow` property

Part 2 (stretch goal):
Solution video : https://player.vimeo.com/video/541322571
Solution git : [View the final code on Github](https://github.com/css-for-js/scrollburglars/compare/solution?expand=1#diff-e979ea9681f20b1bc6cfed7d58f381d4e14e4d114b637e3b2f8e05c9c4186886R160)

**A JS snippet to help(success)**

Discord member SSHari shared a small JS console script that can be used to quickly identify elements that are wider than the viewport:
```js
function checkElemWidth(elem) {
  if (elem.clientWidth > window.innerWidth) {
    console.info(
      "The following element has a larger width than " +
      "the window’s outer width"
    );
    console.info(elem);
    console.info("\n\n");
  }

  // Recursively check all the children
  // of the element to find the culprit.
  [...elem.children].forEach(checkElemWidth);
}

checkElemWidth(document.body);
```

It won't find all possible scrollburglars, because there are so many different ways for scrollburglars to be produced. But of the 3 examples above, this snippet correctly identified the culprit in two of them!

Note that I tweaked this snippet a bit. You can see SSHari's initial snippet [on Github](https://gist.github.com/joshwcomeau/215a383add2ef61bb40a8c94318c99c3).

**Even more tools!(success)**

Firefox, as well as developer browser Polypane, both have tools to help you find scroll containers. Learn more in this awesome article:

- [Debug Unwanted Scrollbars](https://devtoolstips.org/tips/en/debug-unwanted-scrollbars/)

# Responsive Typography

Here's a surprisingly complicated question: should text get bigger or smaller when viewed on a mobile device (compared to a desktop monitor)?

You might think that text should shrink, so that it can fit on the narrower display. Or, you might feel like text should grow _larger_, so that users don't have to squint to be able to read it.

The answer to this question will depend on the type of text we're talking about.
## Body text

“Body text” is the text in our paragraphs and lists. It's the baseline text that fills most of our pages.

When it comes to body text, the answer to the question above is surprisingly simple: **it should stay the same size across all devices.**

Why? Because device manufacturers have already done the hard work of making sure that font sizes are consistent!

Here's a photo of me holding my phone, up in front of a desktop display showing the same website:
![[Pasted image 20231218065545.png]]

I did my best to simulate "real" conditions: the phone is about as far from the camera as it usually is from my eyes, and ditto for the desktop monitor.

When we compare the _perceived size_ of the body text, it takes up about as much space in my field of view:
We generally want our body text to be [at least 16px](https://www.smashingmagazine.com/2011/10/16-pixels-body-copy-anything-less-costly-mistake/). Anything less and users will need to hold the phone uncomfortably close to their face, or do a bunch of pinch-and-zooming.

**What about on very large displays?** As counter-intuitive as it is, most web applications use the same font size regardless of display size. Facebook, Twitter, and Google generally stick around 16px no matter how big the screen gets! That said, it's somewhat common for content-heavy sites like blogs to use larger font sizes, up to 21px, for body text.
**Font size units(info)**

As we've discussed, we don't want to use the `px` unit when it comes to typography. This is because browsers let users pick a default font size, but that won't work if we use "absolute" units like pixels.

So, when we say that body text should be at least 16px, what we're really saying is that it should be at least 1rem. The `rem` unit is relative to the root font size, which defaults to 16px in all browsers.

What if we want to set a different baseline font size, in an accessible way? The following code works:
```css
html {
  font-size: 125%;
}
```
Even though we _can_ do this, I wouldn't personally recommend it.
## Smaller text

In addition to the "body" text found in paragraphs and lists, we also have smaller bits of text that annotate or label things.It's a widely-accepted convention that 1rem is equal to 16px. We're just making things more complicated if we change that convention.

Is this a problem? I think it depends on the circumstances. If the text is relatively unimportant (eg. copyright notices in the footer), I don't mind if folks have to pinch-to-zoom to read it. But if the content is important, we should bump it up on mobile so that it's easier to read:
```css
@media (max-width: 550px) {
  figcaption {
    font-size: 1rem;
  }
}
```
### Form fields

Form input fields like `<input>` and `<select>` generally have a pretty small default font size. This makes them hard to read on mobile devices.

To compensate, iOS Safari will automatically zoom in to focused form fields with small text, to make them easier to read. While this does make them more legible, it makes everything else harder and more tedious.

Fortunately, there is an easy fix: **Safari only zooms in if the fields are smaller than 16px**.
By default, iOS will zoom in so that the input text is _the equivalent_ of 16px. We can skip this zoom by setting the text to 16px by default:
```css
input, select, textarea {
  font-size: 1rem;
}
```
If you have an iOS device, you can try out the following demo. Try tapping each input:

- [courses.joshwcomeau.com/demos/safari-inputs](https://courses.joshwcomeau.com/demos/safari-inputs)
The only difference between the two inputs is that the second has a font-size of `1rem`.

## Headings

When it comes to headings, we need a slightly different approach.
Mobile devices are very narrow, and they can't fit that many characters per line. Large headings feel awkward:

2.5rem (40px) isn't an unreasonable font size for a large desktop heading, but it's totally unwieldy on mobile. It takes up most of the screen!
One way to deal with this is to use media queries; we can decrease the font size on mobile devices:
```css
h1 {
  font-size: 2.5rem;
}

@media (max-width: 550px) {
  h1 {
    font-size: 1.75rem;
  }
}
```
But there's another option: we can choose a fluid value so that the font scales smoothly with the viewport width.

This concept is discussed in the next lesson.
# Fluid Typography

The idea with fluid typography is that instead of creating discrete font sizes at specific breakpoints, our typography smoothly scales with the viewport.

This is done with the `vw` unit:
```html
<style>
  h1 {
    font-size: 6vw;
    margin-bottom: 0.5em;
  }
</style>

<h1>
  This is a fluid headline!
</h1>
<p>
  The heading will grow and shrink with the viewport.
</p>
</main>
```
Try resizing the _Result_ pane to see how the heading's font size behaves.

This is a neat trick, but there are two problems with it.

The first is that it gets a bit ridiculous on very-large or very-small screens. On an iPhone SE, for example, the heading is almost as small as the body text
We can solve this problem by using our new friend `clamp`, to set bounds on how big or small the font can grow:
```html
<style>
  h1 {
    font-size: clamp(1.5rem, 6vw, 3rem);
    margin-bottom: 0.5em;
  }
</style>

<h1>
  This is a fluid headline!
</h1>
<p>
  The heading will grow and shrink with the viewport.
</p>
</main>
```
`clamp` lets us set a hard boundary. In this case, our text is guaranteed to always be between 1.5rem and 3rem, no matter what size the viewport is.
#ImportantPoint 
You can use `min()`, `max()`, and `clamp()` on the right hand side of any CSS.the browser determines which one is either the smallest or largest, respectively. For example, in the case of: `min(1rem, 50%, 10vw)`, the browser calculates which of these relative units is the smallest, and uses that value as the actual value.
To use `clamp()` enter three values: a minimum value, ideal value (from which to calculate), and maximum value.

**Safari quirk(warning)**

Safari supports the `vw` unit, and it supports `clamp`, but when they're used together, Safari behaves a little strangely.

Specifically, it only calculates the value _when the element first appears_. It won't recalculate the font size when the window is resized.

This peculiar rendering behaviour can be fixed with the following declaration:
```css
h1 {
  font-size: clamp(1.5rem, 6vw, 3rem);
  min-height: 0vh;
}
```
Why does this work? I'm not 100% sure, but I believe it has to do with the fact that this declaration forces the browser to recalculate the "values" for the viewport units.

Here's how I understand it: When the element is first rendered, the browser caches the pixel equivalent of 6vw. On a 1000px-wide viewport, this value is 60px. When used inside clamp(), 6vw will always equal 60px, even if the window gets resized.

When we use vw or vh elsewhere in the style, we guarantee that the browser will refresh the pixel equivalent for all viewport units in the style, including within our clamp() call.

This seems like buggy behaviour to me, and hopefully it's something that will be fixed in future versions of Apple's browser.

All of that said: it may not matter that the text size doesn't scale smoothly when the window is resized. In many cases, the initial value is the only thing that matters. Most users don't resize their windows, and even if they do, it's not the end of the world if the heading doesn't scale.
There's one more problem with our solution: we've introduced an accessibility violation.

Check out what happens when we zoom the page in/out:
Demo video : https://courses.joshwcomeau.com/cfj-mats/fluid-zoom.mp4

The WCAG guidelines state that [text should be scalable up to 200%](https://www.w3.org/WAI/WCAG21/Understanding/resize-text.html). If the default font size is 32px, the user should be able to scale it up to 64px (in fact, many folks with poor vision will crank it up even further than that; 200% is the _minimum_ recommendation).

When we use viewport units for our font sizes, that text is locked at that size. It won't be increased by zooming in or by bumping up the browser's default font size.

We can solve this problem by “mixing in” a relative unit:
```html
<style>
  h1 {
    font-size: clamp(
      1.5rem,
      4vw + 1rem,
      3rem
    );
    margin-bottom: 0.5em;
    /*
      HACK: Add this declaration if you're
      using Safari to see the text scale
      when resizing:

      min-height: 0vh;
    */
  }
</style>

<h1>
  This is a fluid headline!
</h1>
<p>
  The heading will grow and shrink with the viewport.
</p>
</main>
```
To understand what's going on here, it helps for us to convert all of these units in our heads.

Each vw unit is 1% of the viewport width. With a 1000px-wide window, 4vw will be 40px.

We then add this number with 1rem. By default, 1rem equals 16px. Added together, our total font size at 1000px will be 56px (40px + 16px).

The first half of this equation is controlled by resizing the window. This table shows the calculated results for 3 different viewport widths.
![[Pasted image 20231218071541.png]]
**The second half of the equation is controlled by the user's font size.** If the user doubles their default font size, `1rem` becomes equal to 32px, not 16px.

By mixing a viewport unit with a relative unit, we give the user control over the font size once more, allowing them to crank it up (albeit at a slower rate).
**Look ma, no calc!(info)**

Earlier, we saw how `calc` lets us do math with our CSS values. You may be wondering why we didn't need to use it in this situation, like this:
```css
h1 {
  font-size: clamp(
    1.5rem,
    calc(4vw + 1rem),
    3rem
  );
}
```
As a courtesy, the `clamp` function (along with `min` and `max`) will automatically resolve any `calc`-style equations within. This helps keep our code a bit cleaner, with no nested function calls required.
## Use responsibly

Fluid typography is useful when it comes to headings and other large text elements, but I don't recommend using this strategy on smaller text like body text.

Our body text is already at the perfect size, without bumping it up or down. Viewport units tend to produce very-small text on mobile. And while users can pinch-zoom to read small text, it's not a pleasant experience
# Fluid Calculator

So we've seen how the `vw` unit lets us scale the font size with the viewport width… but what if we want to change the _rate of change_?

To show you what I mean, try resizing the playground below. Both headings use fluid typography, but they change at very different rates:
```css
<style>
  .fluid {
    font-size: clamp(
      2rem,
      5vw + 1rem,
      5rem
    );
  }
  .fluid-fast {
    font-size: clamp(
      2rem,
      14vw - 1.5rem,
      5rem
    );
  }
</style>

<h2 class="fluid">Fluid Text</h2>
<h2 class="fluid-fast">Fluid Text</h2>
```
The trick is that we can _play with the ratio_ between viewport and relative units.

I explain this technique in this video: https://player.vimeo.com/video/541122010

you can find the fluid calculation in josh tutorial : https://courses.joshwcomeau.com/css-for-js/05-responsive-css/16-fluid-calculator
### Fluid spacing

This trick can be useful even beyond font sizes!

Exercise Solution video : https://player.vimeo.com/video/542686563
# Fluid Design

In the last lesson, we saw how we have two choices when it comes to scaling text based on the viewport:

1. We can define specific sizes at specific breakpoints using media queries (“responsive”).   
2. We can proportionally grow/shrink text based on the viewport width using the `vw` unit (“fluid”).
Here are the two strategies side-by-side:
```css
<style>
  .responsive {
    font-size: 2rem;
  }
  @media (min-width: 400px) {
    .responsive {
      font-size: 2.5rem;
    }
  }
  @media (min-width: 525px) {
    .responsive {
      font-size: 3rem;
    }
  }

  .fluid {
    font-size: clamp(
      2rem,
      6vw + 1rem,
      3rem
    );
  }

  figure {
    padding: 16px;
    border: 2px solid;
    margin: 0;
    margin-bottom: 8px;
  }
  figcaption {
    font-size: 0.875rem;
    color: #444;
    margin-top: 8px;
  }
</style>

<div class="demo">
  <figure>
    <h2 class="responsive">
      Hello World
    </h2>
    <figcaption>
      Responsive, using breakpoints
    </figcaption>
  </figure>
  <figure>
    <h2 class="fluid">
      Hello World
    </h2>
    <figcaption>
      Fluid, using viewport units
    </figcaption>
  </figure>
</div>
```
This _responsive vs. fluid_ dynamic isn't just a typography thing; it's becoming increasingly common to use Flexbox/Grid to build “fluid layouts” instead of defining concrete breakpoints.

That said, fluid isn't inherently _better_ than responsive. They are different approaches with different tradeoffs. Generally, they solve separate problems, though there is some overlap. They're two different tools, and I use them in different situations.

Let's look at an example.
Demo video : https://player.vimeo.com/video/540293591
`code from the video`
```html
<style>
.wrapper {
  padding: 8px;
  background: white;
  border-radius: 8px;
  margin: 16px 0;
}

.description {
  padding: 5px 16px 8px 8px;
}

.description h2 {
  margin-bottom: 8px;
}

.bibliography {
  background: hsl(250deg 20% 90%);
  padding: 8px;
  padding-left: 32px;
  border-radius: 0 4px 4px 0;
}

.bibliography ul {
  margin: 0;
  padding: 0;
}

.bibliography li {
  margin-bottom: 8px;
}

.bibliography a {
  color: hsl(250deg 100% 50%);
  text-underline-offset: 3px;
}

body {
  background: hsl(250deg 20% 20%);
}
  /* RESPONSIVE APPROACH */
  .wrapper {
    display: flex;
  }
  .description {
    flex: 1;
  }
  .bibliography {
    flex: 1;
  }
  
  @media (max-width: 32rem) {
    .wrapper {
      flex-direction: column;
    }
    .bibliography {
      border-radius: 0 0 4px 4px;
    }
  }
  
  /* FLUID APPROACH */
  /*
  .wrapper {
    display: flex;
    flex-wrap: wrap;
  }
  .description {
    flex: 1;
    min-width: 15rem;
  }
  .bibliography {
    flex: 1;
    min-width: 20rem;
  }
  */
</style>

<div class="wrapper">
  <div class="description">
    <h2>Becky Chambers</h2>
    <p>
      Becky Chambers is an American science fiction writer, and the author of the Hugo-award winning Wayfarers series. She is known for her imaginative world-building and character-driven stories.
    </p>
  </div>
  <nav class="bibliography">
    <ul>
      <li>
        <a href="/">
          A Psalm For The Wild-Built
        </a>
      </li>
      <li>
        <a href="/">
          The Galaxy, And The Ground Within
        </a>
      </li>
      <li>
        <a href="/">
          To Be Taught, If Fortunate
        </a>
      </li>
    </ul>
  </nav>
</div>
<div class="wrapper">
  <div class="description">
    <h2>John Scalzi</h2>
    <p>
      John Michael Scalzi II is an American science fiction author and former president of the Science Fiction and Fantasy Writers of America. He is best known for his Old Man's War series, three novels of which have been nominated for the Hugo Award.
    </p>
  </div>
  <nav class="bibliography">
    <ul>
      <li>
        <a href="/">
          Old Man's War
        </a>
      </li>
      <li>
        <a href="/">
          Questions For A Soldier
        </a>
      </li>
      <li>
        <a href="/">
          The Ghost Brigades
        </a>
      </li>
    </ul>
  </nav>
</div>
```

## Advanced Flex techniques

The fluid approach, using Flexbox, can pull off some pretty impressive tricks.

Here's the most extreme version I've found. This snippet is by Adam Argyle. Try resizing the _Result_ pane: there are **4 different layouts supported**

Demo Video : https://courses.joshwcomeau.com/cfj-mats/adam-argyle-4-layouts.mp4
code : 
```css
<!-- CREDIT: Adam Argyle -->
<style>
  form {
    display: flex;
    flex-wrap: wrap;
  }
  form > input {
    flex: 1 1 10ch;
    margin: .5rem;
  }
  form > input[type="email"] {
    flex: 3 1 30ch;
  }
  body {
  min-height: 100vh;
  display: grid;
  align-items: center;
}

input {
  border: none;
  background: hsl(0 0% 93%);
  border-radius: .25rem;
  padding: .75rem 1rem;
}
input[type="submit"] {
  background: hotpink;
  color: white;
  box-shadow: 0 .75rem .5rem -.5rem hsl(0 50% 80%);
}
</style>

<form>
  <input type="text" placeholder="Name">
  <input type="email" placeholder="Email Address">
  <input type="submit" value="Subscribe">
</form>
```
This demo works by taking advantage of the fact that text inputs and submit buttons have different default minimum widths. It leverages the flex wrapping algorithm to create these 4 different layouts.

This is an undeniably impressive demo. Adam is incredibly talented, and it's clear he possesses a deep intuition of Flexbox mechanics. But honestly, **I'm not a fan of this approach in real-world contexts.** I think it's a bit too clever for its own good.

Have you ever solved problems on sites like Codewars or Project Euler? These sites let you practice your programming skills by answering tough questions. A question might be something like “Write a function that returns all the prime numbers that are also part of the fibonacci sequence under 1 million”.

When you submit a solution, you're able to see the solutions that other folks have submitted. The most popular solutions are terse and clever and _impossible to understand_.

The types of clever impress-your-friends "code golf"

 code that does well on these sites is in many ways _the opposite_ of real-world code that we write for our day jobs.

When I write code, I want my code to be as easy-to-understand as possible. Next week, when the junior dev on my team has to update this code, I want it to be as accessible for them as possible. It's not about "dumbing down" our solutions, it's about optimizing for clarity. The clearer the code is, the quicker we'll be able to fix bugs and ship new features.
I wrote more about this idea in a blog post a few years back, [“Clever Code Considered Harmful”](https://medium.com/@joshuawcomeau/clever-code-considered-harmful-a1fb1054e8a1).

Adam's constraint-driven Flexbox form is an incredibly elegant piece of CSS, but it takes _a while_ to figure out. I suspect Adam himself would agree: this is a fancy demo, but it's probably not the clearest way to create a responsive form.

Sometimes, responsive solutions are simpler. Other times, fluid solutions are simpler. Sometimes, the fluid solution is _slightly_ more complex, but it offers better user experience, so we pick it anyway. There are lots of factors to consider. “Understandability” isn't the only thing that matters, but it's a significant variable in the equation for me.

**Form best practices(info)**

In the form demo above, the “placeholder” field is used to label the form field:
![[Pasted image 20231218093047.png]]
This isn't a very good practice.

Placeholders and labels are two different things, with two different purposes. Labels explain what the field is, and placeholders provide an example input, to give users a hint about what's expected and show how to format the data. For example:
```html
<label for="postal-code">
  Postal Code:
</label>
<input
  type="text"
  id="postal-code"
  placeholder="A1B 2C3"
/>
```
The trouble with using a placeholder as a label is that the placeholder disappears when something is entered into the input. We've all had the frustrating experience of our browser auto-filling a form, and then not being able to tell which fields are which, and having to empty out the fields to make sure the browser put the right data in the right fields.

For folks who use screen-readers, this process is even more painful.

Certain designs call for "floating" labels that are overlaid over the text input, and shift up above when the field is selected. Famously, Google's Material Design does this:

Personally, I don't love this pattern, since it deprives us of the ability to use a _real_ placeholder, and confuses the convention of "label above, placeholder within".

That said, it's fine to build inputs this way so long as the right markup is used. You can check out how Google does it by inspecting the [example text input](https://material.io/components/text-fields) in the Material Design docs.

# Workshop

It's time to apply some of this responsive and functional CSS to a larger project!

For this module, we're going to revisit the **Sole&Ankle workshop** from the [the Flexbox module's workshop](https://courses.joshwcomeau.com/css-for-js/04-flexbox/13-workshop). We're going to make it mobile-responsive:
## Resources

Grab the starter code from Github:
- [github.com/css-for-js/sole-and-ankle-revisited](https://github.com/css-for-js/sole-and-ankle-revisited)
**I recommend starting fresh with this repo, rather than continuing on from your Flexbox workshop.** The reason is that a lot of the underlying files have been updated. If you choose to keep building on top of your Flexbox workshop, you may find that you're missing some pieces.

As always, step-by-step instructions can be found in [the project's README.md](https://github.com/css-for-js/sole-and-ankle-revisited/blob/main/README.md).
# Workshop Solution

## Exercise 1: Breakpoints setup

Solution video : https://player.vimeo.com/video/542263712
Solution git : [View the code on Github](https://github.com/css-for-js/sole-and-ankle-revisited/commit/62a4159d74b4ff9cd991b286e594e1c8e51626ff)
## Exercise 2: Mobile header
Solution Video : https://player.vimeo.com/video/542289887
Solution Git : [View the code on Github](https://github.com/css-for-js/sole-and-ankle-revisited/commit/532ca0c31f812e9cadfcacc3db45575efc5da253)

**Correction:** The `border-top` declaration on `Header` should have been in the `tabletAndSmaller` media query. This has been fixed in the solution source code on Github:

## Exercise 3: Tweaks to the main view

Solution Video : https://player.vimeo.com/video/542640125
Solution Git: [View the code on Github](https://github.com/css-for-js/sole-and-ankle-revisited/commit/77a0e33668c84ac365d6d5afca955368186f7e63)

## Exercise 4: Mobile menu modal

Solution video : https://player.vimeo.com/video/542638662
Solution Git : [View the code on Github](https://github.com/css-for-js/sole-and-ankle-revisited/commit/12111fc151e4f893170f17ae38b8f0d31900ba98)

**Correction:** In this video, I neglect to add an `aria-label` to the `<Content>` element, so that screen reader users have context about what this modal is. This has been fixed in the solution source code on Github

## Exercise 5: Fluid desktop navigation

Solution video : https://player.vimeo.com/video/544361936
Solution git : [View the code on Github](https://github.com/css-for-js/sole-and-ankle-revisited/commit/be25cbb7cd5517437c3ac9ed92eecd46e206b760)
## Exercise 6: Theming with CSS variables

Solution Video : https://player.vimeo.com/video/544543038
Solution git :  [View the code on Github](https://github.com/css-for-js/sole-and-ankle-revisited/commit/4d3301d04b34dcc0e0f102a1f0d130ce6d1aa0a5)


































