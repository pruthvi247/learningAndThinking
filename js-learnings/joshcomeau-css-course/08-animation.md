Animation is a _huge_ topic, one that deserves its own course, but in this module, we'll cover the fundamentals of animation in CSS. We'll build a sturdy foundation, one that you can build on top of.

We'll cover:
- The magic of `transform` functions
- A deep dive into how the `transition` property works
- How to use `@keyframes` effectively
- How to design animations, to create next-level user experiences, using principles like action-driven motion and orchestration.
- Understanding animation performance, how to leverage hardware acceleration for smoother motion
- Another "ecosystem world tour", this time looking at the animation landscape.
As always, we focus on mental models to help you understand how this stuff _really_ works. Learn the principles, not the properties!

# Transforms

Over the last 8 modules, we've bumped into the `transform` property a couple times. As we start talking about animation, we need to become properly acquainted with this fella.

As the name implies, `transform` allows us to change a specified element in some way. It comes with a grab-bag of different transform functions that allow us to move and contort our elements in many different ways.
## Transform functions
### Translation
Translation allows us to move an item around:
We can use `translate` to shift an item along in either axis: `x` moves side to side, `y` moves up and down. Positive values move down and to the right. Negative values move up and to the left.
Critically, _the item's in-flow position doesn't change_. As far as our layout algorithms are concerned, from Flow to Flexbox to Grid, this property has no effect.

For example: in this visualization, we have 3 children aligned using Flexbox. When we apply a transform to the middle child, the Flexbox algorithm doesn't notice, and keeps the other children in the same place:
This is similar to how `top` / `left` / `right` / `bottom` work in positioned layout, with relatively-positioned elements.

When we want to move an element along a single axis, we can use `translateX` and `translateY`:
```css
.box {
  transform: translateY(20px);

  /* It's equivalent to: */
  transform: translate(0px, 20px);
}
```
There's one thing that makes `translate` ridiculously powerful, though. Something _totally unique_ in the CSS language.

When we use a percentage value in `translate`, that percentage refers to _the element's own size_, instead of the available space in the parent container.
Setting `transform: translateY(-100%)` moves the box up by its exact height, no matter what that height is, to the pixel.

Here's another example in code, showing how percentages vary between transforms and other CSS properties like `left`:
```css
<style>
  .relative.box {
    position: relative;
    left: 50%;
  }
  .transform.box {
    transform: translateX(50%);
  }
  .relative.box {
  background: deeppink;
}
.transform.box {
  background: navy;
}

.box {
  width: 80px;
  height: 80px;
}
.wrapper {
  position: relative;
  width: 90%;
  max-width: 500px;
  border: 4px solid;
}
</style>

<div class="wrapper">
  <div class="relative box"></div>
  <div class="transform box"></div>
</div>
```
Here are the two scales that are being used:
![[Pasted image 20231221114001.png]]
In the exercise below, we'll see why this is such a handy superpower!
With the magic of `calc`, we can even mix relative and absolute units:

``transform: translateX(calc(100% + 50px));``
This allows us to add a "buffer", so that we can translate something by its own size _plus_ a few extra pixels.
### Scale

Alright, let's look at another transform function!`scale` allows us to grow or shrink an element:
Scale uses a unitless value that represents a _multiple_, similar to `line-height`. `scale(2)` means that the element should be 2x as big as it would normally be.

We can also pass multiple values, to scale the `x` and `y` axis independently:``transform: scale(1, 1);`
At first glance, this might seem equivalent to setting `width` and `height`, but there's one big difference.

Check out what happens when our element has some text in it,The text scales up and down with the element. We aren't just transforming the size and shape of the box, we're transforming the _entire element_ and all of its descendants.

**Simpler calculations(success)**

This reveals an important truth about transforms: **elements are flattened into a texture**. All of these transforms essentially treat our element like a flat image, warping and contorting it as you might in Photoshop.

Incidentally, this is why they're so important for animations!

Think about how much work is required when we change something like `width`. All of the layout algorithms need to re-run, figuring out exactly where this element and all of its siblings should be. If the element has text inside, the line-wrapping algorithm needs to figure out if this new width affects the line breaks. Then, the paint algorithms run, figuring out which color every pixel needs to be, and filling it in.

It's fine to do this once when the page loads, but when we animate something, we need to do all of those calculations _many many times a second_. With transforms, we can skip a bunch of steps. This means that the calculations run quicker, leading to smoother motion.

We'll learn more about animation performance soon.
It may seem like a bummer that `scale` will stretch/squash the element's contents, but we can actually use this effect to our advantage. For example, check out this old-timey TV power animation:
```css
transform: scale(1, 1);  
filter: brightness(100%);
```
For this animation, the squashing effect actually improves the effect!

And, if we _really_ don't want our text to squash, we can apply an _inverse transform_ to the child.

This is an advanced technique, far beyond the scope of this course, but know that it's possible to use `scale` to increase an element's size _without_ distorting its children. Libraries like [Framer Motion](https://www.framer.com/motion/) take advantage of this fact to build highly-performant animations without stretching or squashing.
### Rotate
You guessed it: `rotate` will rotate our elements:
We typically use the `deg` unit for rotation, short for degrees. But there's another handy unit we can use, one which might be easier to reason about:``transform: rotate(0.5turn);``
The `turn` unit represents how many turns the element should make. 1 turn is equal to 360 degrees.It's obscure, but well-supported; the `turn` unit goes all the way back to IE 9!
### Skew

Finally, `skew` is a seldom-used but pretty-neat transformation:`transform: skew(29deg);` As with `translate`, we can skew along either axis.Skew can be useful for creating diagonal decorative elements (à la [Stripe](https://stripe.com/)). With the help of `calc` and some trigonometry, it can also be used on elements without distorting the text! This technique is explored in depth in Nils Binder's awesome blog post, “[Create Diagonal Layouts Like It's 2020](https://9elements.com/blog/create-diagonal-layouts-like-it-s-2020/)”.
## Transform origin

Every element has an _origin_, the anchor that the transform functions execute from.Check out how rotation changes when we tweak the transform origin:
```
transform: rotate(360deg);  
transform-origin: left top;
```
The transform origin acts as a pivot point!It isn't exclusive to rotation, either; here's how it affects scale:
```
transform: scale(0.85);  
transform-origin: left top;
```
This is useful for certain kinds of effects (for example, an element "growing out of" another one).
## Combining multiple operations

We can string together multiple transform functions by space-separating them:``transform: translateX(38px) rotate(143deg);``
#ImportantPoint **The order is important:** the transform functions will be applied sequentially.The transform functions are applied from right to left, like composition in functional programming.
`transform: rotate(0deg) translateX(0px);  transform-origin: center;`
We can use this to our advantage:
```css
<style>
.wrapper {
  position: relative;
}

.planet {
  width: 80px;
  height: 80px;
  background: dodgerblue;
  border-radius: 50%;
}

.moon {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;
  width: 20px;
  height: 20px;
  background: silver;
  border-radius: 50%;
}
  @keyframes orbit {
    from {
      transform:
        rotate(0deg)
        translateX(80px);
    }
    to {
      transform:
        rotate(360deg)
        translateX(80px);
    }
  }
  
  @media (prefers-reduced-motion: no-preference) {
    .moon {
      animation: orbit 6000ms linear infinite;
    }
  }
</style>

<div class="wrapper">
  <div class="planet"></div>
  <div class="moon"></div>
</div>
```
In this example, we start by positioning the moon in the dead center of the planet. Our animation will shift it 80px to the right, and then cause it to rotate in a circle. Because the moon's origin is still in the center of the planet, it orbits around at a distance.

We'll learn more about keyframe animations shortly.
## Inline elements

#ImportantPoint One common gotcha with transforms is that they don't work with inline elements in Flow layout.Remember, inline elements go with the flow. Their goal is to wrap around some content with as little disruption as possible. Transforms aren't their cup of tea.

The easiest fix is to switch it to use `display: inline-block`, or to use a different layout mode (eg. Flexbox or Grid).

Solution video : https://player.vimeo.com/video/580324693
Solution code : 
```css
<style>
  .dialog-wrapper {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    /* background: hsl(0deg 0% 0% / 0.75); */
    /* background: red; */
    display: grid;
  place-content: center;
  }

  .dialog-content {
    width: 600px;
    max-width: 100vw;
    height: 400px;
    background: white;
    border-radius: 6px;
     position: relative;
  }

  .close-btn {
    padding: 16px;
    background: transparent;
    border: none;
    font-weight: bold;
     position: absolute;
  top: 0;
  right: 0;
  transform: translateY(-100%);
  }
</style>

<div class="dialog-wrapper">
  <div class="dialog-content">
    <button class="close-btn">
      Close
    </button>
  </div>
</div>
```
# CSS Transitions
```css
<style>
  .btn {
    transition: transform 250ms;
  }
  
  .btn:hover {
    transform: translateY(-10px);
  }
</style>

<button class="btn">
  Hello World
</button>
```

As we'll discover, the `transition` property is highly configurable, but only two values are required:

1. The name of the property we wish to animate
2. The duration of the animation

If you plan on animating multiple properties, you can pass it a comma-separated list:
```css
.btn {
  transition: transform 250ms, opacity 400ms;
}

.btn:hover {
  transform: scale(1.2);
  opacity: 0;
}
```
**Selecting all properties(warning)**

`transition-property` takes a special value: `all`. When `all` is specified, any CSS property that changes will be transitioned.

It can be tempting to use this value, as it saves us a good chunk of typing if we're animating multiple properties, but **I recommend not using it.**

At some point in the future, you (or someone on your team) will change this CSS. You might add a new declaration that you _don't_ want to transition. It's better to be specific, and avoid any unintended animations.

Animation is like salt: too much of it spoils the dish.
## Timing functions

When we talk about “motion” on the web, we're really talking about _simulated_ motion. The pixels themselves aren't moving across the display!

What we're really doing is more like a flipbook. Each frame draws the element at a slightly different position. If we do this fast enough, it appears like fluid motion, but it's an optical illusion.
There are several timing functions available to us in CSS. We can specify which one we want to use with the `transition-timing-function` property:
```css
.btn {
  transition: transform 250ms;
  transition-timing-function: linear;
}
```
Or, we can pass it directly to the transition shorthand property:
```css
.btn {
  transition: transform 250ms linear;
}
```
`linear` is rarely the best choice — after all, pretty much nothing in the real world moves this way

*

. Good animations mimic the natural world, so we should pick something more organic!

Let's run through our options.
- `ease-out` comes charging in like a wild bull, but it runs out of energy. By the end, it's pootering along like a sleepy turtle.**When would you use `ease-out`?** It's most commonly used when something is entering from off-screen (eg. a modal appearing). It produces the effect that something came hustling in from far away, and settles in front of the user.
- `ease-in` is the opposite of `ease-out`. It starts slow and speeds up:`ease-in` is pretty much exclusively useful for animations that end with the element offscreen or invisible; otherwise, the sudden stop can be jarring.
- `ease-in-out`. It's the combination of the previous two timing functions.This timing function is _symmetrical_. It has an equal amount of acceleration and deceleration.I find this curve most useful for anything that happens in a loop (eg. an element fading in and out, over and over)
- `ease` is very similar to `ease-in-out`, with one key difference: it isn't symmetrical. It features a brief ramp-up, and _lots_ of deceleration.**`ease` is the default value** — if you don't specify a timing function, `ease` gets used. This tends to be a good thing.

**Time is constant(info)**

An important note about all of these demos: _time is constant_. Timing functions describe how a value should get from 0 to 1 over a fixed time interval, **not** how quickly the animation should complete. Some timing functions may feel faster or slower, but in these examples, they all take exactly 1 second to complete.
### Custom curves

If the provided built-in options don't suit your needs, you can define your own custom easing curve, using the cubic bézier timing function!
```css
.btn {
  transition:
    transform 250ms cubic-bezier(0.1, 0.2, 0.3, 0.4);
}
```
All of the values we've seen so far are really just presets for this `cubic-bezier` function. The `linear` value can also be represented as `cubic-bezier(0, 0, 1, 1)`.

Coming up with custom curves can be difficult, but it's extremely worthwhile. I share my tool of choice, and how I use it, over in the Treasure Trove:
- [cubic-bezier](https://courses.joshwcomeau.com/css-for-js/treasure-trove/011-cubic-bezier) - https://cubic-bezier.com/#.17,.67,.83,.67

You can also pick from this [extended set of timing functions](https://easings.net/). Though beware: a few of the more outlandish options won't work in CSS.
![[Pasted image 20231221142707.png]]
**Time for me to come clean(warning)**

I have a confession to make: the demonstrations above, showing the different timing functions, were exaggerated.

In truth, timing functions like `ease-in` are more subtle than depicted, but I wanted to emphasize the effect to make it easier to understand. The `cubic-bezier` timing function makes that possible!
If you'd like to use my custom juiced-up alternatives, you can do so with the following declarations:
```css
.btn {
  /* ease-out */
  transition-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);

  /* ease-in */
  transition-timing-function: cubic-bezier(0.75, 0, 1, 1);

  /* ease-in-out */
  transition-timing-function: cubic-bezier(0.645, 0.045, 0.355, 1);

  /* ease */
  transition-timing-function: cubic-bezier(0.44, 0.21, 0, 1);
}
```
## Delays

Have you ever tried to mouse over a nested navigation menu, only to have it close before you get there?
Demo gif : https://courses.joshwcomeau.com/cfj-mats/dropdown.gif

  
As a JS developer, you can probably work out why this happens: the dropdown only stays open while being hovered! As we move the mouse diagonally to select a child, our cursor dips out of bounds, and the menu closes.

This problem can be solved in a rather elegant way without needing to reach for JS. We can use `transition-delay`!

```css
.dropdown {
  opacity: 0;
  transition: opacity 400ms;
  transition-delay: 300ms;
}

.dropdown-wrapper:hover .dropdown {
  opacity: 1;
  transition: opacity 100ms;
  transition-delay: 0ms;
}
```
`transition-delay` allows us to keep things status-quo for a brief interval. In this case, when the user moves their mouse outside `.dropdown-wrapper`, nothing happens for 300ms. If their mouse re-enters the element within that 300ms window, the transition never takes place.

After 300ms elapses, the `transition` kicks in normally, and the dropdown fades out over 400ms.

## Doom flicker
Demo video : https://player.vimeo.com/video/580324177
This video describes a "doom flicker", a common animation bug where an element jumps up and down quickly in an unintentional
Here's the "before" code:
```css
<style>
  .btn {
    width: 100px;
    height: 100px;
    border: none;
    border-radius: 50%;
    background: slateblue;
    color: white;
    font-size: 20px;
    font-weight: 500;
    line-height: 1;
    transition: transform 250ms;
  }
  
  .btn:hover {
    transform: translateY(-10px);
  }
</style>

<button class="btn">
  Hello World
</button>
```
And here's the "after" solution code:
```css
<style>
  .btn {
    width: 100px;
    height: 100px;
    border: none;
    background: transparent;
    padding: 0;
  }
  
  .btn:hover .btn-contents {
    transform: translateY(-10px);
  }
  
  .btn-contents {
    display: grid;
    place-content: center;
    height: 100%;
    border-radius: 50%;
    background: slateblue;
    color: white;
    font-size: 20px;
    font-weight: 500;
    line-height: 1;
    transition: transform 250ms;
  }
</style>

<button class="btn">
  <span class="btn-contents">
    Hello World
  </span>
</button>
```

To solve this problem, we **separate the trigger from the effect.** We listen for hovers on the parent `<button>`, but apply the transformation to a child element. This ensures that the hover target won't move out from under the cursor.

This works because **hover states bubble up**, just like `mouseEnter` events in JavaScript. When we hover over `.btn-contents`, we're also hovering over all of its ancestors (`.btn`, `body`, etc).

Exercise solution video : https://player.vimeo.com/video/580398586

To solve this problem, we **separate the trigger from the effect.** We listen for hovers on the parent `<button>`, but apply the transformation to a child element. This ensures that the hover target won't move out from under the cursor.

This works because **hover states bubble up**, just like `mouseEnter` events in JavaScript. When we hover over `.btn-contents`, we're also hovering over all of its ancestors (`.btn`, `body`, etc).

Here is the before code ; 
```css
<style>
  .btn {
    width: 100px;
    height: 100px;
    border: none;
    border-radius: 50%;
    background: slateblue;
    color: white;
    font-size: 20px;
    font-weight: 500;
    line-height: 1;
    transition: transform 250ms;
  }
  
  .btn:hover {
    transform: translateY(-10px);
  }
</style>

<button class="btn">
  Hello World
</button>
```
And here's the "after" solution code:
```css
<style>
  .btn {
    width: 100px;
    height: 100px;
    border: none;
    background: transparent;
    padding: 0;
  }
  
  .btn:hover .btn-contents {
    transform: translateY(-10px);
  }
  
  .btn-contents {
    display: grid;
    place-content: center;
    height: 100%;
    border-radius: 50%;
    background: slateblue;
    color: white;
    font-size: 20px;
    font-weight: 500;
    line-height: 1;
    transition: transform 250ms;
  }
</style>

<button class="btn">
  <span class="btn-contents">
    Hello World
  </span>
</button>
```

Exercise solution video : https://player.vimeo.com/video/580323852
```css
.thumbnail {
  transition: transform 500ms;
}

.thumbnail-wrapper {
  overflow: hidden;
}

.thumbnail-wrapper:hover .thumbnail {
  transform: scale(1.2);
}
```
If we wanted the animation to apply for keyboard users as well, we'd need to add the transform on focus as well as hover:
```css
.thumbnail-wrapper:hover .thumbnail,
.thumbnail-wrapper:focus .thumbnail {
  transform: scale(1.2);
}
```
In this particular case, I probably _wouldn't_ add this transition on focus; I worry it'd be distracting as keyboard navigators tab through each photo in the grid. I tend to be a bit more selective about which animations apply on focus. That said, it's good to be in the habit of structuring our markup in such a way that we _could_ add focus animations easily!

Thanks to Discord member Diego for bringing this up!

At the end of the video, I mention that the weird “snapping into place” effect will be covered in a future lesson. If you're keen to figure that out, you'll want to learn about the `will-change` property, discussed in the [Animation Performance](https://courses.joshwcomeau.com/css-for-js/08-animations/08-animation-performance) lesson.
# Keyframe Animations

CSS keyframe animations are declared using the `@keyframes` at-rule. We can specify a transition from one set of CSS declarations to another:
```css
@keyframes slide-in {
  from {
    transform: translateX(-100%);
  }
  to {
    transform: translateX(0%);
  }
}
```
Each `@keyframes` statement needs a name! In this case, we've chosen to name it `slide-in`. You can think of this like a global variable.
Keyframe animations are meant to be general and reusable. We can apply them to specific selectors with the `animation` property:
As with the `transition` property, `animation` requires a duration. Here we've said that the animation should last 1 second (1000ms).

The browser will _interpolate_ the declarations within our `from` and `to` blocks, over the duration specified. This happens immediately, as soon as the property is set.

We can animate multiple properties in the same animation declaration. Here's a fancier example that changes multiple properties:
```css
<style>
  @keyframes drop-in {
    from {
      transform:
        rotate(-30deg) translateY(-100%);
      opacity: 0;
    }
    to {
      transform:
        rotate(0deg) translateY(0%);
      opacity: 1;
    }
  }

  .box {
    animation: drop-in 1000ms;
  }
  body {
  padding: 32px;
}
.box {
  width: 100px;
  height: 100px;
  background: slateblue;
  padding: 8px;
  display: grid;
  place-content: center;
  color: white;
  text-align: center;
}
</style>

<div class="box">
  Hello World
</div>
```
## Timing functions

As with `transition`, keyframe animations default to an `ease` timing curve, but can be overridden.

We can do this with the `animation-timing-function` property:
```css
  @keyframes drop-in {
    from {
      transform: translateY(-100%);
    }
    to {
      transform: translateY(0%);
    }
  }

  .box {
    animation: drop-in 1000ms;
    animation-timing-function: linear;
  }
</style>
```
## Looped animations

By default, keyframe animations will only run once, but we can control this with the `animation-iteration-count` property:
```css
 .box {
    animation: slide-in 1000ms;
    animation-iteration-count: 3;
  }
```
It's somewhat rare to specify an integer like this, but there is one special value that comes in handy: `infinite`For example, we can use it to create a loading spinner
Note that for spinners, we generally want to use a `linear` timing function so that the motion is constant (though this is somewhat subjective—try changing it and see what you think!).
## Multi-step animations

In addition to the `from` and `to` keywords, we can also use percentages. This allows us to add more than 2 steps:
```css
<style>
  @keyframes fancy-spin {
    0% {
      transform: rotate(0turn) scale(1);
    }
    25% {
      transform: rotate(1turn) scale(1);
    }
    50% {
      transform: rotate(1turn) scale(1.5);
    }
    75% {
      transform: rotate(0turn) scale(1.5);
    }
    100% {
      transform: rotate(0turn) scale(1);
    }
  }
  
  .spinner {
    animation: fancy-spin 2000ms;
    animation-iteration-count: infinite;
  }
</style>
```
The percentages refer to the progress through the animation. `from` is really just syntactic sugar? for `0%`. `to` is sugar for `100%`.

Importantly, _the timing function applies to each step_. We don't get a single ease for the entire animation:
```css
<style>
  @keyframes spin {
    0% {
      transform: rotate(0turn);
    }
    100% {
      transform: rotate(1turn)
    }
  }
  @keyframes multi-step-spin {
    0% {
      transform: rotate(0turn);
    }
    25% {
      transform: rotate(0.25turn);
    }
    50% {
      transform: rotate(0.5turn);
    }
    75% {
      transform: rotate(0.75turn);
    }
    100% {
      transform: rotate(1turn);
    }
  }
  
  .spinner {
    animation: spin 2000ms;
    animation-iteration-count: infinite;
  }
  .multi-step-spinner {
    animation: multi-step-spin 2000ms;
    animation-iteration-count: infinite;
  }
  .spinner, .multi-step-spinner {
  display: block;
  width: 32px;
  height: 32px;
}
body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 16px;
  height: calc(100vh - 16px);
}
</style>

<img
  class="spinner"
  alt="Loading…"
  src="https://courses.joshwcomeau.com/cfj-mats/loader.svg"
/>
<img
  class="multi-step-spinner"
  alt="Loading…"
  src="https://courses.joshwcomeau.com/cfj-mats/loader.svg"
/>
```
In this playground, both spinners complete 1 full rotation in 2 seconds. But `multi-step-spin` breaks it into 4 distinct steps, and each step has the timing function applied.

There's no way around it using CSS keyframe animations, though it _is_ possible to configure this behaviour in the Web Animations API. We take a brief look at this [at the end of the module](https://courses.joshwcomeau.com/css-for-js/08-animations/16-ecosystem-world-tour#the-web-animations-api)
## Alternating animations

Let's suppose that we want an element to "breathe", inflating and deflating.
We could set it up as a 3-step animation:
```css
<style>
  @keyframes grow-and-shrink {
    0% {
      transform: scale(1);
    }
    50% {
      transform: scale(1.5);
    }
    100% {
      transform: scale(1);
    }
  }

  .box {
    animation: grow-and-shrink 4000ms;
    animation-iteration-count: infinite;
    animation-timing-function: ease-in-out;
  }
</style>

<div class="box"></div>
```
It spends the first half of the duration growing to be 1.5x its default size. Once it reaches that peak, it spends the second half shrinking back down to 1x.

This works, but there's a more-elegant way to accomplish the same effect. We can use the `animation-direction` property
```css
<style>
  @keyframes grow-and-shrink {
    0% {
      transform: scale(1);
    }
    100% {
      transform: scale(1.5);
    }
  }

  .box {
    animation: grow-and-shrink 2000ms;
    animation-timing-function: ease-in-out;
    animation-iteration-count: infinite;
    animation-direction: alternate;
  }
</style>

<div class="box"></div>
```
`animation-direction` controls the order of the keyframes. The default value is `normal`, going from 0% to 100% over the course of the specified duration.

We can also set it to `reverse`. This will play the animation backwards, going from 100% to 0%.

The interesting part, though, is that we can set it to `alternate`, which ping-pongs between `normal` and `reverse` on subsequent iterations.

Instead of having 1 big animation that grows and shrinks, we set our animation to grow, and then reverse it on the next iteration, causing it to shrink.

**Half the duration(info)**
Originally, our "breathe" animation lasted 4 seconds. When we switched to the alternate strategy, however, we cut the duration in half, down to 2 seconds.

This is because _each iteration only performs half the work_. It always took 2 seconds to grow, and 2 seconds to shrink. Before, we had a single 4-second-long animation. Now, we have a 2-second-long animation that requires 2 iterations to complete a full cycle.

## Shorthand values

We've picked up a lot of animation properties in this lesson, and it's been a lot of typing!

Fortunately, as with `transition`, we can use the `animation` shorthand to combine all of these properties.

The above animation can be rewritten:
```css
.box {
  /*
  From this:
    animation: grow-and-shrink 2000ms;
    animation-timing-function: ease-in-out;
    animation-iteration-count: infinite;
    animation-direction: alternate;

  ...to this:
  */
  animation: grow-and-shrink 2000ms ease-in-out infinite alternate;
}
```
Here's a piece of good news, as well: **the order doesn't matter.** For the most part, you can toss these properties in any order you want.

This works because different properties accept different values; `alternate`, for example, isn't a valid timing-function or iteration-count, so the browser can deduce that you mean to assign it to `animation-direction`.
```css
.box {

/* This works: */
animation: grow-and-shrink 2000ms ease-in-out infinite alternate;

/* This also works! */
animation: grow-and-shrink alternate infinite 2000ms ease-in-out;
}
```
There is an exception: `animation-delay`, a property we'll talk more about shortly, needs to come after the duration, since both properties take the same value type (milliseconds/seconds).

For that reason, I prefer to exclude delay from the shorthand:
```css
.box {
animation: grow-and-shrink 2000ms ease-in-out infinite alternate;
animation-delay: 500ms;
}
```
# Fill Modes

Probably the most confusing aspect of keyframe animations is _fill modes_. They're the biggest obstacle on our path towards confidence.

First, let's start with a problem.

We want our element to fade out. The animation itself works fine, but when it's over, the element pops back into existence:
```css
<style>
  @keyframes fade-out {
    from {
      opacity: 1;
    }
    to {
      opacity: 0;
    }
  }
  
  .box {
    animation: fade-out 1000ms;
  }
</style>

<div class="box">
  Hello World
</div>
```
If we were to graph the element's opacity over time, it would look something like this:
![[Pasted image 20231221190538.png]]
Why does the element jump back to full visibility? Well, the declarations in the `from` and `to` blocks only apply _while the animation is running_.

After that first 1000ms, the animation packs itself up and hits the road. The declarations in the `to` block dissipate, leaving our element with whatever CSS declarations have been defined elsewhere. Since we haven't set `opacity` for this element anywhere else, it snaps back to its default value (`1`).

One way to solve this is to add an `opacity` declaration to the `.box` selector directly
```css
<style>
  @keyframes fade-out {
    from {
      opacity: 1;
    }
    to {
      opacity: 0;
    }
  }
  
  .box {
    animation: fade-out 1000ms;
    /*
      Change the "default" value for opacity,
      so that it reverts to 0 when the
      animation completes.
    */
    opacity: 0;
  }
</style>
```
While the animation is running, the declarations in the `@keyframes` statement overrule the opacity declaration in the `.box` selector. Once the animation wraps up, though, that declaration kicks in and keeps the box hidden.

**Specificity?(info)**
You might be wondering: how "specific" are the declarations in a `@keyframes` statement? Will they _always_ overrule other selectors while the animation is running?

But what about keyframe animations? What is their specificity?
It turns out that specificity isn't really the right way to think about this; instead, we need to think about **cascade origins.**
A “cascade origin” is a source of selectors. For example, browsers come with a bunch of built-in styles—that's why anchor tags are blue and underlined by default. These styles are part of the _User-Agent Origin_.

**The specificity rules only apply when comparing selectors in the same origin.** The styles we write normally are part of the “Author Origin”, and Author Origin styles win out over ones written in the User-Agent Origin.

Here's why this is relevant: keyframe animations are their own special origin, and its styles are applied later.

Think of it in terms of a fighting video game. In Round One, all of the default browser styles are applied, following standard specificity rules. In Round Two, the selectors we've provided battle it out. In Round Three, `@keyframes` declarations are applied. It doesn't matter how specific a selector is if it's applied in Round Two; our `@keyframes` declaration will overwrite it.

[According to the specification](https://www.w3.org/TR/css-cascade-3/#cascade-sort), there are actually 8 rounds, not 3. Interestingly, declarations with `!important` are considered part of a different origin! At least, in theory.
This is why our keyframe animations will apply, regardless of specificity.
So, we can update our CSS so that the element's properties match the `to` block, but is that really the best way?
## Filling forwards

Instead of relying on default declarations, let's consider another approach, using `animation-fill-mode`:
```css
<style>
  @keyframes fade-out {
    from {
      opacity: 1;
    }
    to {
      opacity: 0;
    }
  }
  
  .box {
    animation: fade-out 1000ms;
    animation-fill-mode: forwards;
  }
</style>

<div class="box">
  Hello World
</div>
```
`animation-fill-mode` lets us persist the final value from the animation, _forwards in time_.
![[Pasted image 20231221193901.png]]
"forwards" is a very confusing name, but hopefully seeing it on the graph makes it a bit clearer.

Imagine if we recorded the first 10 seconds the user spent on our page. We can now scrub forwards and backwards in time through this recording.

As we scrub through the first second, the box slowly disappears. For the next 9 seconds, the box remains invisible, because `animation-fill-mode: forwards` effectively copying the declarations from the `to` block, and persisting them as we scrub forwards in time.
## Filling backwards

By default, animations will run immediately, as soon as the `animation` property is set.

Like with `transition`, though, we can specify a delay if we'd like the animation to start a bit later.Unfortunately, we run into a similar issue:
```css
<style>
  @keyframes slide-in {
    from {
      transform: translateX(-100%);
      opacity: 0.25;
    }
    to {
      transform: translateX(0%);
      opacity: 1;
    }
  }

  .box {
    animation: slide-in 1000ms;
    animation-delay: 500ms;
  }
</style>

<div class="box">
  Hello World
</div>
```
For that first half-second, the element is fully visible
![[Pasted image 20231221194051.png]]
This issue is caused by the same culprit. For that first 500ms, no CSS from the animation is applied.

`animation-fill-mode` has another value, `backwards`, which allows us to apply the animation's initial state **backwards in time.**
![[Pasted image 20231221194119.png]]
Essentially what we've said here is to copy all of the declarations in the `from` block and apply them to the element ASAP, before the animation has started.
```css
<style>
  @keyframes slide-in {
    from {
      transform: translateX(-100%);
      opacity: 0.25;
    }
    to {
      transform: translateX(0%);
      opacity: 1;
    }
  }

  .box {
    animation: slide-in 1000ms;
    animation-delay: 500ms;
    animation-fill-mode: backwards;
  }
</style>

<div class="box">
  Hello World
</div>
```
What if we want to persist the animation forwards _and_ backwards? We can use a third value, `both`, which persists in both directions:
![[Pasted image 20231221194227.png]]
In general, I want the initial value in my keyframe to be applied during the delay. And I want the final value to keep applying after the animation has ended. I apply `animation-fill-mode: both` as a matter of habit to my keyframe animations. I wish it was the default value.

Like all of the animation properties we're discussing, it can be tossed into the `animation` shorthand:
```css
.box {
  animation: slide-in 1000ms ease-out both;
  animation-delay: 500ms;
}
```
# Dynamic Updates

So far, all of the examples we've seen involve an animation running right on page load (or after a prescribed delay).

That's not quite the right way to think about it though. There's no rule that says that animations need to happen immediately!

It's more accurate to say that the animation will start as soon as a valid animation is wired up, using the `animation` property. Using JavaScript, we can add that property dynamically, at any point in time:
When the page loads, the `animation` property is set to `undefined`, and so nothing happens. When the user clicks the "Enable animation" button, though, that property is updated to `jump 1000ms infinite`. The moment the `animation` property is set to a valid value, the animation begins.

If the button is clicked again, `animation` is reverted back to `undefined`, and the animation is disabled.
## Playing and pausing

You may have noticed in the example above: disabling the animation can lead to some pretty jarring transitions:
Demo video : https://courses.joshwcomeau.com/cfj-mats/interrupted-keyframes.mp4
When we remove the `animation` property, all of the CSS in the `from` and `to` blocks evaporates immediately. The element will revert back to its default CSS.

This is known as an “interruption”. `@keyframes` animations don't handle interruptions well.

There is a tool that can help in certain situations, though: **play states.**

Here's an updated example:
```js
import React from 'react';
import styled from 'styled-components';

function App() {
  const [
    animated,
    setAnimated
  ] = React.useState(false);
  
  return (
    <Wrapper>
      <Box
        style={{
          animationPlayState: animated
            ? 'running'
            : 'paused',
        }}
      />
      <button
        onClick={() => {
          setAnimated(!animated);
        }}
      >
        {animated
          ? 'Pause animation'
          : 'Start animation'
        }
      </button>
    </Wrapper>
  );
}

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 32px;
  height: 100vh;
`;

const Box = styled.div`
  width: 80px;
  height: 80px;
  background: slateblue;
  animation: jump 1000ms infinite;
`

export default App;
```
(Quick reminder: styles are "camelCased" when setting them in JavaScript. `animationPlayState` sets the CSS property `animation-play-state`.)

Before, we were dynamically applying and removing the animation altogether. In this updated example, the animation is always applied (inside the `Box` styled-component), but we dynamically toggle it between running and paused.

`paused` works like the pause button on a remote control. Everything freezes in place. Toggling it back to `running` will pick up from where it left off.

`animation-play-state` has [excellent browser support](https://caniuse.com/?search=animation-play-state), going all the way back to IE10.

Not many animations require "pause" functionality, but it's a neat property to have in your back pocket!

## Animations vs. transitions

You might be wondering: when should I use `@keyframes`, and when should I use `transition`?

There are some things that only `@keyframes` can do:

- Looped animations
- Multi-step animations
- pauseable animations
We _can_ do some of this stuff from JS, if we really wanted to. But usually, it's simpler to use `@keyframes`.

If an animation needs to run immediately when the page loads or the component mounts, it's easiest to use `@keyframes`.

On the other hand, I reach for `transition` when my CSS will change as a result of some application state or user action. I use it when I want to smooth out an otherwise harsh transition between values.

Both tools serve slightly different purposes, and it takes some practice to build an intuition for which to use when.

# With styled-components
When we write CSS with styled-components, all of our styles are coupled with a specific component. The `@keyframes` at-rule is meant to be declared globally, though. How do we use `@keyframes` with styled-components?

Happily, the library comes with a utility for this!

We can import `keyframes` from the styled-components package, and use it like so:
```js
import styled, { keyframes } from 'styled-components';

function App() {
  return <FloatingCircle />;
}

const float = keyframes`
  from {
    transform: translateY(10px);
  }
  to {
    transform: translateY(-10px);
  }
`;

const FloatingCircle = styled.div`
  animation: ${float} 1000ms infinite alternate ease-in-out;
`;
```
The `keyframes` function is called using tagged template literals, just like the `styled` helper functions.

To apply our animation, we interpolate it within the styles for a specific component.

This is a good thing! While it might seem like this is a pointless bit of added friction, it comes with a terrific advantage: **it removes the possibility for naming conflicts.**

In vanilla CSS, `@keyframes` definitions are global. If we create a keyframe animation called `fadeIn`, any component anywhere in our application can use this animation. If another developer on our team also decides to name their animation `fadeIn`, one of the animations will overwrite the other.

In styled-components, each animation is given a unique, random name, just like the component classes! Under the hood, this `float` animation might actually be named `exvRVV` or `BozTiK`.

Beyond this one difference, keyframe animations created in styled-components function exactly like `@keyframes` statements written in vanilla CSS.

Learn more in the [styled-components documentation](https://styled-components.com/docs/api#keyframes).

#ImportantPoint Animations doesn't work on inline elements, hence we should changes the display to `disply:inline-block`
## Pop-up Help Circle

Update the code below so that the help circle slides in from the bottom, after a short delay:

Solution video : https://player.vimeo.com/video/580893403
Solution code : 
```css
<style>
@keyframes slide-in {
  from {
    transform: translateY(
      calc(100% + var(--spacing))
    );
  }
  to {
    transform: translateY(0%);
  }
}
.help-circle {
  --spacing: 32px;
  position: fixed;
  bottom: var(--spacing);
  right: var(--spacing);
  animation: slide-in 500ms backwards;
  animation-delay: 1000ms;
}
  .help-circle {
  display: grid;
  place-content: center;
  width: 60px;
  height: 60px;
  color: white;
  background: slateblue;
  border-radius: 50%;
  border: 3px solid white;
  box-shadow:
    0px 2px 8px hsl(0deg 0% 0% / 0.1),
    0px 4px 16px hsl(0deg 0% 0% / 0.1),
    0px 8px 32px hsl(0deg 0% 0% / 0.1);
  cursor: pointer;
}
.help-circle img {
  width: 32px;
  height: 32px;
}

.visually-hidden {
  position: absolute;
  overflow: hidden;
  clip: rect(0 0 0 0);
  height: 1px;
  width: 1px;
  margin: -1px;
  padding: 0;
  border: 0;
}
</style>

<button class="help-circle">
  <img
    alt=""
    src="https://courses.joshwcomeau.com/cfj-mats/help-white.svg"
  />
  <span class="visually-hidden">
    Access help center
  </span>
</button>
```
## Waving hand

Update the "waving hand" emoji below so that it actually waves at the user:
```css
<style>
 @keyframes wave {
  from {
    transform: rotate(-10deg);
  }
  to {
    transform: rotate(30deg);
  }

}
  .wave {
    display: inline-block;
    animation: wave 1000ms infinite alternate ease-in-out;
    transform-origin: 75% 80%;
  }
  html, body {
  height: 100%;
}
body {
  display: grid;
  place-content: center;
}
.wave {
  font-size: 3rem;
}
</style>

<p>
  <span
    class="wave"
    role="img"
    aria-label="Waving hand"
  >
    👋
  </span>
</p>
```

external site : https://csstriggers.com/
# Animation performance

As JS developers, we focus quite a bit on performance. Which is good! Performance is important.

It's also really important when it comes to our animations. Sluggish animations can ruin an otherwise good user experience.

The tolerances are also _really tight_. In order for our brain to perceive motion as fluid and believable, it needs to run at 60 frames per second: this leaves us with only ~16 milliseconds to update each frame!

If our animation is too computationally expensive, it'll appear janky and choppy. The device just can't keep up, and the framerate drops.

Experience this for yourself by tweaking the "Frames per second" control:
In practice, poor performance will often take the form of _variable_ framerates, so this isn't a perfect simulation.

Animation performance is a surprisingly deep and interesting area, well beyond the scope of this course. But let's cover the absolutely-critical, need-to-know bits.
## The pixel pipeline

If we want to update the colors of the pixels on our screen, there's a pipeline of possible steps:

1. **Recalculating style** — first, we need to figure out which CSS declarations apply to which elements.
2. **Layout** — next, we need to figure out where each element sits on the page.
3. **Paint** — once we know where everything is, we can start painting them. This is the process of figuring out which color every pixel should be (“rasterization”), and filling it in.   
4. **Compositing** — Finally, we can transform previously-painted elements.

**What the heck is “compositing”?(info)**

The 4th step in our pixel pipeline is the most confusing. What the heck is it?! And how is it different from painting?

Compositing lets the browser re-use the work done in previous frames.
It was invented to help with scroll performance. In the early days of the web, the entire page had to be repainted _on every frame_ when the user scrolled. This was slow and miserable, so the smart folks who work on browsers found a way to skip the paint process, and instead slide the page's content up or down when the user scrolls.

Compositing is lightning-quick because it doesn't have to do many calculations. It's all about transforming the stuff it has already calculated (sliding it around, rotating it, etc).

Different CSS properties will trigger different steps in the pixel pipeline. If we animate an element's `height`, we'll need to recalculate the layout, since an item shrinking might mean that its siblings scoot up to fill the space.

For this reason, it's best to try and avoid animating any properties that affect layout: this is things like `width`, `height`, `padding`, `margin`.

Properties like `background-color` will never affect layout, because there aren't any colors that change an element's position on the page. So it'll be faster than animating a property that does affect layout.

The `transform` property, however, is special: it can animate a property _without even triggering a paint step!_ Like with scrolling, it can reuse the work done on previous steps.

There are only two properties that can be animated with compositing alone: `transform` and `opacity`. In Chrome, `filter` can also be composited, and they're [working on supporting more properties](https://developer.chrome.com/blog/hardware-accelerated-animations/), like `clip-path` and `background-color`.

Does that mean that you can only ever animate `transform` and `opacity`? Personally, I think we can be a little bit more flexible than that. Not all repaints / layout-recalculations are created equal! For example, tweaking the height of an absolutely-positioned element tends to be quicker, since there's no chance that it will cause siblings to be shifted.

The best thing you can do is to test your animations on a very low-end device, like the low-end smartphones discussed [in Module 5](https://courses.joshwcomeau.com/css-for-js/05-responsive-css/03-mobile-testing). If you're satisfied with the performance on a low-end device, ship it!
## Hardware Acceleration

Depending on your browser and OS, you may occasionally notice a curious flicker on certain animations:

When we animate an element using `transform` and `opacity`, the browser will sometimes try to optimize this animation. Instead of rasterizing the pixels on every frame, it transfers everything to the GPU as a texture. GPUs are very good at doing these kinds of texture-based transformations, and as a result, we get a very slick, very performant animation. This is known as “hardware acceleration”.

Here's the problem: GPUs and CPUs render things _slightly_ differently. When the CPU hands it to the GPU, and vice versa, you get a snap of things shifting slightly.

We can fix this problem by adding the following CSS property:
```css
.btn {
  will-change: transform;
}
```
`will-change` is a property that allows us to hint to the browser that we're going to animate the selected element, and that it should optimize for this case.

In practice, what this means is that the browser will let the GPU handle this element _all the time_. No more handing-off between CPU and GPU, no more telltale “snapping into place”.

`will-change` lets us be intentional about which elements should be hardware-accelerated. Browsers have their own inscrutable logic around this stuff, and I'd rather not leave it up to chanc

**Alternative properties(info)**

Hardware acceleration has been around for a long time—longer than the `will-change` property, in fact!

For a long time, it was accomplished by using a 3D transform, like `transform: translateZ(0px)`. Even with a 0px value, the browser still hands it off to the GPU, since moving in 3D space is definitely a GPU strength. There's also `backface-visibility: hidden`.

When `will-change` came out, it was intended to give developers a proper, semantically-meaningful way to hint to the browser that an element should be optimized. In the early days, though, [`will-change` had some problems](https://greensock.com/will-change/).

Happily, it seems as though all of these issues have been resolved. I've done some testing, and have found that I get the best results across modern browsers with `will-change`. But you should always do your own testing, to make sure that these techniques work on the devices and browsers you target.

There's another benefit to hardware acceleration: we can take advantage of _sub-pixel rendering_.Properties like `margin-top` can't sub-pixel-render, which means they need to round to the nearest pixel, creating a stepped, janky effect. `transform`, meanwhile, can smoothly shift between pixels.

It isn't clear to me if this legitimately uses subpixels (the R/G/B pixel fragments we discussed in [Module 6](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/02-text-rendering)), or if it uses anti-alias trickery. Either way, though, the effect is consistently smoother, on both retina and non-retina displays.

**Tradeoffs(warning)**

Nothing in life comes free, and hardware acceleration is no exception.

By delegating an element's rendering to the GPU, it'll consume more video memory, a resource that can be limited, especially on lower-end mobile devices.

This isn't as big a deal as it used to be — I've done some testing on a Xiaomi Redmi 7A, a popular budget smartphone in India, and it seems to hold up just fine. Just don't broadly apply `will-change` to elements that won't move. Be intentional about where you use it.
If you're interested in learning more about animation performance, I gave a talk on this subject at React Rally. It goes deep into this topic:

Video :  https://youtu.be/DNGGzwmfouU

# Designing Animations

As developers, our job is generally focused on _implementation_; a product/design team gives us designs, and we bring them to life.

In my experience, however, most teams don't have a motion designer on them. And the standard design tools—things like Figma, Sketch, Illustrator—don't really support animations.
This is really unfortunate, because animation is a critical part of the user experience, and it's _hard to get right_. We've all had the experience of being annoyed by an aggressive or out-of-place animation.

This course isn't about motion design, so we won't go too deep, but I wanted to provide some high-level tips to make it easier to design animations.
## Types of animation

In her amazing book [“Animation At Work”](https://abookapart.com/products/animation-at-work), author Rachel Nabors describes 5 common categories of animation:

1. _Transitions_ change the content on the page in a significant way, like moving from one page to another, a modal opening or closing, or a multi-step wizard moving to the next step.
2. _Supplements_ add or remove information from the page, without changing their "location" or task. For example, a notification might pop up in the corner.
3. _Feedback_ helps the user understand how the application has responded to user input. For example, an error message appearing when submitting a form, or a button sliding down on click to indicate that it's being depressed.
4. _Demonstrations_ are used for education, a way of showing the user how something works. Many of the animations on this platform, like the visualizations in [the “Rules of Margin Collapse” lesson](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/12-rules-of-margin-collapse), fit into this category.
5. _Decorations_ are aesthetic and don't affect the information on the page. For example, confetti to celebrate a piece of good news being delivered to the user.
Of these categories, decorations are often dismissed as frivolous. And they certainly can be! But I'm of the view that each of these categories is valid and valuable. The important thing is that you understand _why_ you're adding animation: which of these categories does it fit into? How does it help the user?

Every animation we add should have a purpose behind it. We shouldn't add animation just to be fancy. Animation can make a product feel more polished, but only when it's thoughtful, and it's clear to the user why it exists.

## Additional reading

We've only scratched the surface of animation and motion design!

Here are some resources to keep going, if you're interested in this subject:

- [Animation At Work](https://abookapart.com/products/animation-at-work) by Rachel Nabors. It's an incredibly helpful resource for understanding the "why" around animation.
    
- [Improving the Payment Experience With Animations](https://medium.com/bridge-collection/improve-the-payment-experience-with-animations-3d1b0a9b810e), a fantastic article written by Stripe designer Michaël Villar about the Stripe Checkout animations.

exercise video solution : https://player.vimeo.com/video/582281795


# 3D Transforms

So far, we've been thinking primarily in two dimensions: we've been moving stuff left-to-right and top-to-bottom.

CSS comes with a surprisingly robust 3D engine, one that we can leverage to do all kinds of fancy stuff.
## Isometric vs. perspective

Remember “Where's Waldo?”, the puzzle game where you had to find a red-striped thrill-seeker on a mission to find the world's most chaotic environments?
There's something a bit curious about these puzzles: there's no perspective.
In real life, things that are further away appear smaller to us. A smartphone held a few inches from our face will appear larger than a TV across the room.

If this “Where's Waldo?” puzzle was a photograph, the people near the top should appear much smaller than the people at the bottom. But they're all drawn to the same scale.

This is known as **isometric projection**. Artists use this to achieve a certain effect. Another example is popular pixel artist [Eboy](https://hello.eboy.com/pool/~Pixorama/1?q=project):

By contrast, **perspective projection** mimics how things appear in real life, where things vanish into the distance:
![[Pasted image 20231221225733.png]]
By default, the 3D engine in CSS will assume that we want to use **isometric projection**. Everything will be the same size, no matter how far away it is. We can switch to a perspective projection using the `perspective` CSS property:
 When an element moves away from the user, it gets smaller. When it rotates along the X or Y axis, we can tell which edge is closer to us, and which edge is further away.

In order to switch to _perspective projection_, we also need to pass it a length value:
`perspective: 250px;`
The value we pass to `perspective` can be thought of as a measure of how close the user is to the screen.

If the user is _right next_ to the screen, small changes in position will appear **huge**. Imagine spinning a card that's only a few inches from your face.

If the user is further away, though, that same motion will appear smaller and more subtle.

We can choose a `perspective` value based on how attention-grabbing we want our animation to be:
**Pixels?(info)**

It's a bit weird to use pixels for perspective, isn't it? What does it mean for the user to be 500 pixels away from the screen, exactly?

Interestingly, CSS does have units for both inches and centimeters. This is totally valid CSS:
```css
.box-wrapper {
perspective: 20cm;
}
```
The trouble is that the browser doesn't actually have enough information for this to be trustworthy / accurate. `1cm` is equivalent to `38px`, on all devices, no matter the pixel density or screen size.

As weird as it is, pixels is the right choice. Experiment with different values until you find one that feels right, based on the effect you're going for!
## Applying perspective

There are two different ways to apply perspective. The first is with the `perspective` CSS property:
```css
<style>
  .container {
    perspective: 250px;
  }
  .box {
    transform: rotateX(45deg);
  }
</style>

<div class="container">
  <div class="box"></div>
  <div class="box"></div>
  <div class="box"></div>
</div>
```
Note that the `perspective` property needs to be set **on the parent element**. It's kind of like `display: grid`; we set `perspective` to control how the _children_ will be presented.

The cool thing about the `perspective` property is that it _groups the children into the same environment_. Our 3 cards above are each rendered a little differently, based on their position within the box.

Essentially, the box's position within the perspective-parent will control what angle we see it at. We can see this by moving a rotated box — try moving your mouse around in the “Result” pane:
```js
import React from 'react';
import styled from 'styled-components';

function App() {
  const [x, y] = useMousePosition();

  return (
    <Wrapper
      style={{ perspective: '400px' }}
    >
      <Box
        style={{
          transform: `
            translate(${x}px, ${y}px)
            rotateX(30deg)
          `,
        }}
      />
    </Wrapper>
  );
}

const Wrapper = styled.div`
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /*
    Prevent horizontal scrollbar when
    box is moved to edge of screen
  */
  overflow: hidden;
`;

const Box = styled.button`
  width: 50px;
  height: 50px;
  background: slateblue;
  border: none;
`;

/*
  React hook that dynamically sets the user's current
  cursor position.
*/
function useMousePosition() {
  const [position, setPosition] = React.useState([0, 0]);

  React.useEffect(() => {
     function handleMouseMove(ev) {
      setPosition([ev.clientX, ev.clientY]);
    }

    window.addEventListener('mousemove', handleMouseMove);

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
    }
  }, []);

  return position;
}

export default App;
```
### The perspective function

In addition to the `perspective` property, there is also a `perspective()` transform function:
```css
.box {
transform: perspective(250px) rotateX(45deg);
}
```
Unlike the `perspective` property, the `perspective()` function will give each transformed element its own little environment.
```css
<style>
  .box {
    transform: perspective(250px) rotateX(45deg);
  }
</style>

<div class="container">
  <div class="box"></div>
  <div class="box"></div>
  <div class="box"></div>
</div>
```
I tend to prefer using the `perspective` property, since I generally want my siblings to share an environment, for a more realistic effect.
# Rendering Contexts

So far, we've seen how to make something _appear_ 3D, with the `perspective` property.

Here's an example of how this property can be used, alongside 3D transforms, to build “tilting” cards. **Hover/focus the cards** to see them tilt:
```css
<style>
  .wrapper {
    perspective: 500px;
  }
  .card-link {
    display: block;
    transform-origin: top center;
    will-change: transform;
    transform: rotateX(0deg);
    transition: transform 750ms;
  }
  .card-link:hover,
  .card-link:focus {
    transform: rotateX(-35deg);
    transition: transform 250ms;
  }
  body {
  background-color: hsl(240deg 80% 90%);
}
.wrapper {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
}
.card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 200px;
  background: white;
  border-radius: 8px;
  border: 2px solid hsl(240deg 100% 75%);
}
.card img {
  width: 64px;
  height: 64px;
}
/*
  The default focus style looks bad with the
  transform. Let's remove it, and apply a
  better one!
*/
.card-link:focus {
  outline: none;
}
.card-link:focus .card {
  outline: 3px solid hsl(240deg 100% 50%);
  outline-offset: 2px;
}
</style>

<div class="wrapper">
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/chrome.svg"
      />
    </article>
  </a>
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/firefox.svg"
      />
    </article>
  </a>
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/safari.png"
      />
    </article>
  </a>
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/edge.svg"
      />
    </article>
  </a>
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/opera.svg"
      />
    </article>
  </a>
</div>
```
  

This demo combines a bunch of stuff we've been learning through this module:

- On hover/focus, each card is rotating by -35 degrees along the X axis. We're animating the effect using [the “transition” property](https://courses.joshwcomeau.com/css-for-js/08-animations/02-transitions).
- We want the cards to pivot along their top edge, and so we've set the [“transform-origin”](https://courses.joshwcomeau.com/css-for-js/08-animations/01-transforms#transform-origin) to change the element's origin. 
- We want all cards to share the same [perspective projection](https://courses.joshwcomeau.com/css-for-js/08-animations/13-3d-transforms#the-perspective-property), and so we set `perspective: 500px` on the shared `.wrapper` parent. Cards on the left and right sides will tilt towards the center.

**There are a number of problems with this demo, however.**

You might've noticed the biggest issue: cards on the right tilt _in front_ of their siblings:
demo video : https://courses.joshwcomeau.com/cfj-mats/flap-card-bug.mp4
**Why does this happen?** Well, we're rotating the cards in 3D space, but they're still being stacked according to the [stacking context stuff](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/07-stacking-contexts) we learned in Module 2. Specifically, because we haven't used `z-index`, the stacking order is determined by DOM order; the 5th card sits in front of the 4th, the 4th in front of the 3rd, etc.

So, hm. We _could_ solve this by manually tweaking the `z-index` on each card, so that the middle card is in front… Maybe something like this
![[Pasted image 20231221230706.png]]
This could work, **but there's a better option.**

Introducing the `transform-style` property:
```css
<style>
  .wrapper {
    transform-style: preserve-3d;
    perspective: 500px;
  }
</style>

<div class="wrapper">
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/chrome.svg"
      />
    </article>
  </a>
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/firefox.svg"
      />
    </article>
  </a>
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/safari.png"
      />
    </article>
  </a>
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/edge.svg"
      />
    </article>
  </a>
  <a href="/" class="card-link">
    <article class="card">
      <img
        src="https://courses.joshwcomeau.com/images/logos/opera.svg"
      />
    </article>
  </a>
</div>
```
**Glitchy on Firefox(info)**

If you're using Firefox, you might notice that the hover event triggers inconsistently. It's not very pleasant!

We'll address this issue in the next lesson, [Gotchas](https://courses.joshwcomeau.com/css-for-js/08-animations/15-gotchas)

**Much better!**
When we set `transform-style: preserve-3d`, we opt into a different stacking algorithm. Instead of being based purely on stacking contexts and `z-index` layers, we _position the elements in 3D space!_

With `transform-style: preserve-3d`, the `z-index` property can still be used to set the default position, but the moment we start tilting or moving an item in 3D space, that takes precedence.

**This is a big deal.** It essentially gives us a legit 3D engine to work with in CSS! We can do things that aren't otherwise possible with `z-index`:
`style.css`
```css
.wrapper {
  width: 250px;
  height: 250px;
  border: 2px solid;
  position: relative;
}
.red-box {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  margin: auto;  background: hsl(350deg 100% 50%);
  width: 100px;
  height: 60px;
}
.yellow-circle {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 75px;
  height: 75px;
  border-radius: 50%;
  background: hsl(50deg 100% 50%);
  margin: auto;
}
```
`index.html`
```css
<style>
  @keyframes move-around {
    from {
      transform: translateZ(50px);
    }
    to {
      transform: translateZ(-50px);
    }
  }
  
  .wrapper {
    perspective: 500px;
    transform-style: preserve-3d;
  }
  .red-box {
    transform: rotateX(45deg);
  }
  .yellow-circle {
    animation:
      move-around 2000ms ease-in-out
      infinite alternate;
  }
</style>

<div class="wrapper">
  <div class="red-box"></div>
  <div class="yellow-circle"></div>
</div>
```
In this example, a yellow circle is moving forwards and backwards in 3D space. A red rectangle has been tilted backwards, so that the circle will intersect it at an angle.

Here's the same animation, but rotated so that we can see what's going on more clearly:
Demo video : https://courses.joshwcomeau.com/cfj-mats/intersect-animation.mp4

## 3D rendering contexts

When we apply `transform-style: preserve-3d`, we create a **3D rendering context**.

It's a bit like how certain CSS properties like `position: fixed` create a _stacking_ context. With `transform-style: preserve-3d`, we allow the element's children to be repositioned in 3D space. When one element moves closer, it'll be painted above its siblings in the 3D rendering context.

I feel like it's really easy to get `perspective` and `transform-style` mixed up, but they accomplish different goals:

- `perspective` is all about the visuals of how items are presented. By default, CSS uses _orthographic projection_, like that “Where's Waldo?” drawing, but we can flip to _perspective projection_ with the `perspective` attribute.
    
- `transform-style` creates a 3D rendering context, which allows items to be moved around in 3D space, changing which elements show up “in front”, and allowing elements to intersect.
    

We've already seen what happens when we set `perspective` without setting `transform-style`: elements will appear to rotate and move in 3D space, but it's a purely visual effect. The layering / paint order is still determined by things like `z-index` and DOM order.

And if we set `transform-style` without setting `perspective`, elements can move in 3D space, but they still appear flat:

we can use above style.css for below html
```css
<style>
  .wrapper {
    /* perspective: 500px; */
    transform-style: preserve-3d;
  }
</style>

<div class="wrapper">
  <div class="red-box"></div>
  <div class="yellow-circle"></div>
</div>
```

# Ecosystem World Tour

As we did in [Module 3](https://courses.joshwcomeau.com/css-for-js/03-components/02-ecosystem-world-tour), this lesson takes a look at the modern landscape, this time with a focus on animation. We'll look at different libraries and APIs, with the goal of helping you understand what your options are, and how to get started with them.

Unfortunately, this list is a bit React-heavy, for the simple reason that it's what I know best. I'm not as familiar with other UI frameworks, and sadly many of the animation packages are often framework-specific.

As before, **this is based on my personal experience and opinions**. Plenty of very-smart people will likely disagree with me on certain aspects. This isn't meant to be either objective or definitive. My hope is that this can point you in the right direction, and you can do your own research and experimentation.

Also: this lesson is at the very end of this module for a reason: it's important to get comfortable with the basics of CSS animation first!
## The Web Animations API

The Web Animations API is a low-level animation API built into the browser. We can build animation sequences and control them from within JavaScript.

It mirrors the `@keyframes` API. Here's a quick example:
```css
const elem = document.querySelector('.box');

const frames = [
  { opacity: 0, transform: 'translateY(100%)' },
  { opacity: 1, transform: 'translateY(0%)' },
];

elem.animate(
  frames,
  {
    duration: 1000,
    iterations: Infinity,
  }
);
```
This is equivalent to the following CSS animation:
```css
@keyframes pop-in {
  from {
    opacity: 0;
    transform: translateY(100%);
  }

  to {
    opacity: 1;
    transform: translateY(0%);
  }
}

.box {
  animation: pop-in 1000ms infinite;
}
```
For the most part, the Web Animations API can be thought of as "CSS keyframe animations in JavaScript". Under the hood, the Web Animations API even uses the same low-level implementation as keyframe animations, so their performance characteristics are identical.

But there _are_ some things that are different between the two.

The most significant, IMO, is that the Web Animations API will let us apply a single timing function for _the whole_ animation. Each step isn't given its own easing, by default.
```js
<div class="box js"></div>
<div class="box css"></div>

<script>
  const elem = document.querySelector('.box.js');

  const frames = [
    { transform: 'translate(-20px, -10px)' },
    { transform: 'translate(0px, 10px)' },
    { transform: 'translate(20px, -10px)' },
    { transform: 'translate(-20px, -10px)' },
  ]
  
  elem.animate(
    frames,
    {
      duration: 2000,
      iterations: Infinity,
      easing: 'ease',
    }
  )
</script>
```
```css
@keyframes dance-moves {
  0% {
    transform: translate(-20px, -10px);
  }
  33.3% {
    transform: translate(0px, 10px);
  }
  66.7% {
    transform: translate(20px, -10px);
  }
  100% {
    transform: translate(-20px, -10px);
  }
}

.box.css {
  animation: dance-moves 2000ms infinite;
}

.box {
  width: 50px;
  height: 50px;
  background: slateblue;
  margin: 64px;
  border-radius: 4px;
}

html {
  height: 100%;
}
body {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
```
The box on the left uses the Web Animations API, and so the _entire animation_ uses a single easing curve. The box on the right uses keyframe animations, and so each step in the sequence is given its own ease.

We can also apply custom timing functions to each step in the Web Animations API:
**Pros:**

- It's built into the browser, so no hefty package needs to be included in your bundle.
- It has good performance, and won't be affected by any work happening in the JS main thread.
- It has [solid browser support](https://caniuse.com/web-animation).
- It allows a bit more customization compared to CSS keyframe animations
**Cons:**

- It's not fundamentally different from CSS keyframe animations. It doesn't really let you do anything "new".
- Frustratingly, there are lots of subtle differences between keyframe animations and the Web Animation API for you to get tripped up by. For example, the default timing function is "linear" instead of "ease". And in order to change the timing function, you set `easing` instead of `animationTimingFunction`.

**Resources:**
- [Using the Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API), on MDN
- [CSS Animations vs. Web Animations API](https://css-tricks.com/css-animations-vs-web-animations-api/), on CSS Tricks

**Motion One(success)**
The Web Animations API is definitely a bit quirky. A new library, [Motion One](https://motion.dev/), aims to improve the developer experience of using this API.

I haven't personally used it, but it looks incredible. It's built by Matt Perry, creator of Framer Motion (discussed further below).

## Framer Motion

Framer Motion is an **incredible** piece of technology.

First, a bit of confusion to clear up: **this is _not_ the same thing as Framer / Framer X**, a design tool used to create mockups. It's produced by the same company, but it's an entirely different thing.

Framer Motion is a production-ready library for React. It does a lot of things, but the most impressive and noteworthy thing is that it can animate CSS properties that aren't normally able to be animated.

For example: earlier in this course, we saw these Flexbox visualizers:
In "real life", when we change Flexbox properties, that transition can't be animated. `transition: justify-content 300ms` has no effect. But I've done it here, using Framer Motion.

Framer Motion works by calculating a complex sequence of transforms required to interpolate between the start and end positions. This is known as _the FLIP technique_. As someone who built a FLIP-based library myself, let me tell you: this stuff is ridiculously hard.

Because it uses transforms, the animations are highly performant. Even if we _could_ animate Flexbox properties, they wouldn't be this smooth.

It's not limited to Flexbox, either. Framer Motion can animate just about _any_ CSS change. If your element goes from being a child in a Grid container to setting `position: absolute; top: 50px`, Framer Motion can animate that transition.

It can even animate transitions **between components**.
Here is an example from their docs:
Demo video : https://courses.joshwcomeau.com/cfj-mats/framer-motion-demo.mp4

**Pros:**

- Can animate all kinds of things that would normally not be animatable, leading to next-level user experiences. We can build stuff that would have been unimaginably complex, just a year or two ago.
- Uses hardware-accelerated transforms for performant transitions.
- Supports using spring physics instead of Bézier curves (discussed below).
- Ties in beautifully with React. Can add sophisticated animations in a remarkably small amount of code.

**Cons:**

- All of that magic comes at a cost: [according to Bundle Phobia](https://bundlephobia.com/package/framer-motion@4.1.17), the package weighs ~32kb gzip.
- Like all JS-based animation libraries, the animation might run choppy if the main thread becomes occupied.
- Only works with React.
**Resources:**

- [More on Framer Motion in the Treasure Trove](https://courses.joshwcomeau.com/css-for-js/treasure-trove/009-framer-motion)
- [Official site / docs](https://www.framer.com/motion/)
- [Github](https://github.com/framer/motion)
## React Spring

React Spring allows us to model our animations based on spring physics, rather than Bézier curves.

Spring physics are an entirely different model for running animations. When we work with spring physics, we don't pick a duration for our animations; instead, we configure the characteristics of a spring.

Why would we want to do this? Because the resulting motion is _incredible._ It feels fluid and realistic. Spring physics are modeled on the natural world, and it convinces our brain in a way that Bèzier curves can't fully imitate.
Sample video : https://courses.joshwcomeau.com/cfj-mats/react-spring-list.mp4
React Spring is the most common way to animate using spring physics in React. They've done _a ton_ of work to make an incredibly powerful, highly-configurable library. You can do lots of wild stuff with React Spring, and it's been my go-to library for years.

**Pros:**

- Fluid, organic motion compared with CSS transitions / keyframe animations.
- Highly optimized performance.
- Relatively small: 18kb gzip, [according to Bundle Phobia](https://bundlephobia.com/package/@react-spring/web@9.2.4).
- A rich API with lots of advanced options, including wonderful orchestration tools.
- Ties in with an ecosystem created by the same folks. For example, we can use it with `react-use-gesture` to create the card-grabbing animation above, or this one:
At its core, React Spring is a number generator. This means it can be used for all kinds of animations, not just transitioning CSS properties. 
**Cons:**

- It can't do "magic" animations in the way that Framer Motion can. And given that Framer Motion _does_ support spring physics, it may be the better choice for your application.
- The learning curve is pretty steep, both with spring physics in general, and this library in particular.
- Like all JS-based animation libraries, the animation might be janky if the main thread becomes occupied.
**Resources:**

- [Official site / docs](https://react-spring.io/)
- [Github](https://github.com/pmndrs/react-spring)
- [A Friendly Introduction to Spring Physics](https://www.joshwcomeau.com/animation/a-friendly-introduction-to-spring-physics/), by me!
## GreenSock GSAP

GSAP is one of the oldest and most well-known animation libraries out there.

I personally haven't used it much, but folks like Sarah Drasner [swear by it](https://css-tricks.com/how-to-animate-on-the-web-with-greensock/). It offers advanced Bézier-based easing (much more flexible than the `cubic-bezier` CSS function), and a timeline to manage orchestration (animating multiple elements at specific moments).

In terms of bundle size, it sits right between the two other libraries we've seen (24kb gzip, [according to BundlePhobia](https://bundlephobia.com/package/gsap@3.7.1)), though that number might be artificially low: GSAP has a rich plugin ecosystem, and those plugins may inflate your bundle.

It's created by GreenSock, a for-profit organization, and there's a lot of confusion around whether this tool is free-to-use or not. To clarify, at the time of writing, GSAP is [open-source](https://github.com/greensock/GSAP), though it does come with a [more-restrictive license](https://greensock.com/standard-license/) than most other libraries: if you use GSAP on a paid product, you'll need to pay GreenSock a couple hundred bucks a year for their “BusinessGreen” license.
**Pros:**
- Large, active community.
- Can be used with any framework, not just React.
- Highly optimized performance.
- Rich plugin ecosystem for things like adding scroll-based triggers
- Probably lots of other things! I'm not familiar enough with it to say.

**Cons:**
- While it can emulate spring physics in a more-accurate way than CSS transitions, it doesn't support true spring physics.
- Because it's framework-agnostic, it won't tie in as neatly as framework-specific solutions.
- Probably lots of other things! I'm not familiar enough with it to say.
**Resources:**
- [Official site / docs](https://greensock.com/gsap/)
- [How to Animate on the Web With GreenSock](https://css-tricks.com/how-to-animate-on-the-web-with-greensock/), by Sarah Drasner
## Other libraries

There's a _huge_ ecosystem out there, and we're just scratching the surface.

That said, there are relatively few tools out there doing truly remarkable things. Most of the libraries I've seen are all about _ergonomics_. They offer a different way to accomplish the same stuff you could do with CSS transitions or keyframe animations.

Once you become comfortable with CSS transitions and keyframe animations, these sorts of tools don't seem to offer as much value. But they come with a cost: you need to spend time learning how to use them, and they increase the size of your JS bundles!

I prefer to focus on tools that let us do things not otherwise possible. CSS doesn't come with a built-in way to use spring physics, so a spring-physics-based library is worthwhile to me.

If you don't use React, I'd encourage you to look for libraries with similar game-changing potential!

(Svelte comes with a bunch of advanced animation stuff built-in. If you're a Svelte dev, you may not need a library!)

**The fundamentals always matter(info)**

With amazing tools like Framer Motion and React Spring and GSAP, you might be wondering: is there any point to using the fundamental animation tools in CSS?
**Yes it is!** I still rely on the CSS `transition` property and CSS keyframe animations a ton.
CSS animations run off the main thread, which means they have an inherent performance advantage over these fancy JS animation libraries. For small, straightforward animations, nothing works better than CSS transitions and animations!
I reach for modern tools in two cases:
- The animation is too complex or sophisticated to be done with CSS (eg. 'crossfading' between DOM elements).
- The animation is very prominent, and I want to squeeze a bit of extra lush-ness out of it with spring physics.

# Workshop
## Exercise 1: Sneaker Zoom
solution video :  https://player.vimeo.com/video/594243367
Solution git : - [View the code on Github](https://github.com/css-for-js/sole-and-ankle-animated/commit/4617a469c6e9caede11581732903c0e494c34c25)

Each exercise in this workshop encourages you to extend or replace the given animation. Here's an example of how I'd tackle the “Stretch Goal” part of this, by using CSS filters and rotation to enhance the effect:
Solution video : https://player.vimeo.com/video/594242920

## Exercise 2: Navigation link flip-up
solution video : https://player.vimeo.com/video/594242338
solution code : [View the code on Github](https://github.com/css-for-js/sole-and-ankle-animated/commit/9c00dc274a0d36af90329f0cbc1b7f9810673d35)
## Exercise 3: Modal enter animation
Solution video : https://player.vimeo.com/video/594295450
Solution code : [View the code on Github](https://github.com/css-for-js/sole-and-ankle-animated/commit/6eb4163069270ae7d7fd5e5af7d37798d8c05b24)

