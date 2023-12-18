In this section, we're going to look at another layout mode: _Positioned layout_.

The defining feature of positioned layout is that items can overlap. The Flow Layout algorithm tries very hard to make sure that multiple elements never occupy the same pixels. With positioned layout, however, we can break out of the box.

We can opt into Positioned layout using the `position` property. It can be set to `relative`, `absolute`, `fixed`, or `sticky`. Each one works in a unique way, like a mini-layout-algorithm within the layout algorithm.
**Static positioning(info)**

The default value of the `position` property is `static`.

Occasionally, you'll see tutorials refer to "statically-positioned" elements. All this really means is that the elements are _not_ using Positioned layout; they're using some other layout mode, like Flow or Flexbox or Grid.

If an element is currently using Positioned layout and you want to opt out, you can set `position` to either `static` or `initial`:
```css
.box {
/* Revert to its default value, which is ‘static’ */
position: initial;
}
```
## Relative positioning
Of all the Positioned layout sub-genres, `relative` is the most subtle.
You can often slap `position: relative` on an element, and observe zero difference. It appears to have no effect!

In fact, it does two things:
1. Constrains certain children (we'll get to this shortly!)
2. Enables additional CSS properties to be used.

When we opt into Positioned layout, we enable a handful of new CSS properties, including:
- top
- left
- right
- bottom
We can use those directional values to shift the element around. With relative positioning, those values are _relative to its natural position._

It's common to use `top` and `left` to push things along the vertical and horizontal axes respectively. Setting `left: 10px` pushes the element 10px to the right.
You can also use negative numbers to push the element in the opposite direction; for relatively-positioned nodes, `left: -10px` has the same effect as `right: 10px`.

You might be thinking "That's cool and all, but I can already push an element around with margin! What's the difference?"

#ImportantPoint  The big difference is that **`position` doesn't impact layout.** they don't get pulled along for the ride, as they do with margin.
When we push a relatively-positioned element around with top/left/right/bottom, the browser acts like the element is still in its original position. The displacement is purely cosmetic.
```css
<style>
body {
  display: flex;
  align-items: flex-start;
}
section {
  flex: 1;
  background: #EEE;
  border: 2px solid;
  border-radius: 4px;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 0.875rem;
  line-height: 3;
}
section:not(:last-of-type) {
  margin-right: 20px;
}
.box {
  width: 48px;
  height: 48px;
  border: 4px solid;
  margin-bottom: 8px;
}
.pink.box {
  border-color: deeppink;
}
  .with-margin {
    margin-top: 20px;
  }
  .with-position {
    position: relative;
    top: 20px;
  }
</style>

<section>
  Natural
  <div class="pink box"></div>
  <div class="box"></div>
  <div class="box"></div>
</section>
<section>
  “margin-top”
  <div class="pink box with-margin"></div>
  <div class="box"></div>
  <div class="box"></div>
</section>
<section>
  “top”
  <div class="pink box with-position"></div>
  <div class="box"></div>
  <div class="box"></div>
</section>
```
play around and change some numbers to see what happens!

Whether we use relative-positioning and `top` or `margin-top`, the pink box winds up in the same spot (20px lower than its natural position). With `margin-top`, though, the black boxes below the pink ones get shuffled along too, like a row of cars forced to back up to let a truck turn.

Similarly, when block items don't have a specified width, they can dynamically resize when, say, `margin-left` is increased. `left`, on the other hand, pushes an item around without ever changing its dimensions.
```css
<style>
  .with-margin {
    margin-left: 40px;
  }
  .with-position {
    position: relative;
    left: 0px;
  }
</style>

<section>
  “margin-left”
  <div class="pink box with-margin"></div>
</section>
<section>
  “left”
  <div class="pink box with-position"></div>
</section>
```
Sometimes you want to shift an item around independently, and sometimes you'll want it to remain "context-aware". There's also a third option, using transforms, which we'll learn about [later on in the course](https://courses.joshwcomeau.com/css-for-js/08-animations/01-transforms).
Finally, it's important to note that relative positioning can be applied to _both block and inline elements_. This allows us to nudge inline elements in a way that isn't really possible otherwise.
```css
<style>
  strong {
    position: relative;
    top: -4px;
  }
</style>

<p>
  This paragraph has some bolded text, and it <strong>appears to float</strong> a bit!
</p>
```
# Absolute Positioning

So far, all of the elements we've seen are laid out in an orderly fashion, one on top of the other. We generally refer to this as “in flow”, a reference to Flow layout (though, these days, it can also refer to other layout modes like Flexbox).

What if we want to break the rules, though? What if we want to take an element out of this orderly flow, and stick it wherever we want?

In these cases, _absolute positioning_ is our friend.
We generally use absolute positioning for things like:

- UI elements that need to float above the UI, like tooltips or dropdowns.
- Decorative elements that need to be stuck in certain positions (eg. abstract illustrations).
- Stacking multiple elements in the same place, like a deck of cards.
```css
<style>
  .pink.box {
    position: absolute;
    top: 0px;
    right: 0px;
    width: 75px;
    height: 75px;
    background: deeppink;
  }
</style>

<div class="pink box"></div>
<p>Hello World</p>
```
In Flow layout, we would expect the pink box to sit on top of the paragraph, since that's their order in the DOM. Because our pink box uses absolute positioning, though, two things are different:
1. The pink box is nestled up in the top-right corner of the preview frame.
2. The "Hello world" paragraph has shifted up, to fill the space the pink box would normally fill.
## Placement based on the frame

This is the main thing people think about when it comes to absolute positioning. We can stick something in the corner, or otherwise position something based on the box it's being constrained by, ignoring its "natural" position.

We can do this with 4 properties: `top`, `left`, `right`, and `bottom`. Above, we stuck our box in the top-right corner by specifying that it should be 0px from the top edge and 0px from the right edge.

It doesn't have to be stuck along an edge, either. Consider:
### Default placement

Here's a question: what happens if you set `position: absolute`, but _don't_ give it an anchor by setting `top` / `left` / `right` / `bottom`?

Here's a playground. See if you can figure out what it's doing:
```css
<style>
  .box {
    position: absolute;
    background: slateblue;
  }
</style>

<p>
  Lorem Ipsum is simply dummy text of
  the printing and typesetting industry.
  <span class="box">Hello World</span>
  It has survived not only five centuries,
  but also the leap into electronic
  typesetting, remaining essentially
  unchanged.
</p>
```
Hint: try resizing the “Result” pane!

#ImportantPoint If we don't give our absolute element an anchor, **it sits in its default in-flow position**. I think of it as "inheriting" its default position from Flow layout.

See this for yourself by removing `position: absolute`. Notice that the element sits more-or-less in the same spot!
It has one other effect, though. It causes the absolute element to stack on top of the surrounding text. Which takes us to the second aspect of absolute positioning…
## Effect on layout

This point is a bit less obvious, but maybe even more important. When we set something to be `position: absolute`, we **pull it out of flow.**

#ImportantPoint the browser is laying out elements, it effectively pretends that absolutely-positioned elements don't exist. They're “incorporeal”: you can stick your hand right through them, like a hologram or a ghost.

To drive the point home, here are 3 paragraphs that have been set to be absolutely positioned:
```css
<style>
  p {
    position: absolute;
  }
</style>

<p>This is a paragraph.</p>
<p>Another paragraph, with different words.</p>
<p>Finally, to complete the set, a third.</p>
```
The browser starts by putting that first paragraph in its natural position, at the top of the document, but because it's absolute, it still considers that space empty.

Next, the second paragraph gets added in its natural position, which is also right at the top, since the container is effectively “empty”.

This process will continue for each provided `absolute` element.

Being able to take elements out-of-flow is super handy. Any time you want an element to be "floating above" the content, like a tooltip or a dropdown or a modal, absolute positioning is your friend.
### Collapsing parents

While often the ability to take an element out-of-flow is useful, there are times when it can be annoying. Consider this example:
```css
<style>
  .child {
    /* Toggle this property: */
    /* position: absolute; */
    width: 200px;
    height: 200px;
    background: hotpink;
    opacity: 0.5;
  }
  .parent {
    border: 4px solid;
  }</style>
<div class="parent">
  <div class="child"></div>
</div>
```
In this example, we have a pink box sitting within a black-border parent. When we toggle on that `position: absolute`, you'll notice that the parent "collapses" down, so that it's 8px tall (4px top border, 4px bottom).

Why does this happen? Well, in terms of flow layout, the parent is empty! Remember, absolute elements are like holograms, they don't _really_ exist. And since this parent element has no other children, it's as if it was an empty div.

> **The right tool for the job(info)**
> 
You might be wondering: _how do we fix this?_ Is there a way to stop the parent from collapsing, while still using absolute positioning on the child?
Unfortunately, I'm not aware of any way to do this (at least, not without resorting to a bunch of hacky JS), but I sorta think it's the wrong question.
_In general,_ absolute positioning is intended to be used in situations where we _don't_ want it to affect its surrounding layout.
If you find yourself running into this problem over and over, it's likely that you're reaching for absolute positioning in situations where another layout mode (eg. Flexbox, Grid) would be more appropriate.

## Absolute sizes

video : https://player.vimeo.com/video/612741161
```css
<style>
  .abs {
    position: absolute;
    top: 32px;
    left: 32px;
    right:32px;
    border: 2px solid slateblue;
  }
</style>

<div class="abs">
  Lookatm!Iamaverylongsentencewithfartoomanywordsandletterstofitonasinglelineintheavailablespace.
</div>
```
# Centering Trick

So we've seen how we can position an element by specifying a distance from the edge, like this:
Absolutely-positioned elements have another trick up their sleeve; we can use these properties to center the element!

Video : https://player.vimeo.com/video/612733652
Here's the playground from the video:
```css
<style>
  .box {
    position: absolute;
    top: 0px;
    left: 0px;
    right: 0px;
    bottom: 0px;
    width: 100px;
    height: 100px;
    margin: auto;
    background: deeppink;
  }
</style>

<div class="box"></div>
```
There are 4 important ingredients for this trick to work:
- absolute positioning (`position: absolute`)
- Equal distances from each edge (ideally `0px`)
- A fixed size (defined `width` and `height` properties)
- Hungry margins (`margin: auto`)

**Still relevant?(info)**
Given the rise of modern layout algorithms (Flexbox and Grid), you might wonder if this trick is still worth using.
In fact, I still use this trick a ton! It's especially useful for prominent bits of UI, things like modals or drawers or dialog boxes.

## The “inset” property

As we saw, the centering trick requires setting all 4 edge properties to the same value:
This feels very tedious, and modern CSS has given us a more terse way to accomplish this:
```css
.box {
inset: 0;
}
```
The `inset` property will set all 4 edge properties (`top`, `left`, `right`, and `bottom`) to the provided value.

It's useful for this centering trick, but also when we want an element to be “inset” within its parent:

In the lessons ahead, I'll keep using `top`/`left`/`right`/`bottom` instead of `inset`, but this is only because I hadn't gotten accustomed to using `inset` when I originally created these lessons. Going forward, I use `inset` regularly, and I suggest you do as well!
# Containing Blocks

In CSS, every HTML element has a “containing block”. A containing block is a rectangle that forms the bounds of the element's container.

In Flow layout, elements are contained by their parents. For example, this paragraph is contained by its parent `<section>`:

To be precise: the paragraph is contained by a “containing block” the size and shape of the parent element's _content box_:
![[Pasted image 20231212212505.png]] Containing block
Flow layout uses containing blocks to figure out where on the screen to place the element.

When it comes to absolute positioning, however, containing blocks work a little bit differently.

When we set the position of an element using `top` / `left` / `right` / `bottom`, we're positioning the element **based on the element's containing block.** If our element sets `top: 0; left: 0`, the element will be nestled in the top-left corner of the containing block.

The million-dollar question is this: _how is an absolute element's containing block calculated?_

Unlike in Flow layout, absolutely-positioned elements aren't necessarily contained by their direct parent. They're a bit like **rebellious teenagers** in this way. They won't necessarily pay any attention to their parents.

Here's an example of an absolute element ignoring its parent:
```css
<style>
  .parent {
    width: 200px;
    height: 150px;
    border: 5px solid;
  }

  .rebellious-teenager {
    position: absolute;
    bottom: 0px;
    left: 0px;
    background: deeppink;
    width: 50px;
    height: 50px;
    border-radius: 50%;
  }
</style>

<div class="parent">
  <div class="rebellious-teenager"></div>
</div>
```
Here's what's going on: **Absolute elements can only be contained by _other_ elements using Positioned layout.** This is a really important point, and a really common source of confusion.

If we add `position: relative` to the `.parent` class, it flips the child's containing block. It will now be contained by the parent:
```css
<style>
  .parent {
    /* The magic property: */
    position: relative;

    width: 200px;
    height: 150px;
    border: 5px solid;
  }

  .rebellious-teenager {
    position: absolute;
    bottom: 0px;
    left: 0px;
    background: deeppink;
    width: 50px;
    height: 50px;
    border-radius: 50%;
  }
</style>

<div class="parent">
  <div class="rebellious-teenager"></div>
</div>
```
#ImportantPoint Here's how the algorithm works: 
When deciding where to place an absolutely-positioned element, it crawls up through the tree, looking for a Positioned ancestor. The first one it finds will provide the containing block.

**What if it doesn't find one?** In many of the examples we've seen so far, there aren't any Positioned ancestors.

In this case, the element will be positioned according to the **“initial containing block”**. This is a box the size of the viewport, right at the top of the document.

Here's another example. Our box is placed in a Russian-nesting-dolls-type collection of boxes. It only pays attention to the closest `relative` ancestor:
```css
<style>
  .block {
    padding: 16px;
    border: 2px solid silver;
  }

  .relative.block {
    position: relative;
    border-color: black;
  }

  .pink-box {
    position: absolute;
    top: 0px;
    right: 0px;
    background: deeppink;
    width: 50px;
    height: 50px;
  }
</style>

<div class="block">
  <div class="relative block">
    <div class="block">
      <div class="block">
        <div class="pink-box"></div>
      </div>
    </div>
  </div>
</div>
```
It doesn't matter how many parent elements are wrapping the child, it will ignore all of them until it finds a `position`. It doesn't have to be `relative`, as seen here, but it has to use Positioned layout. `absolute`, `fixed`, and `sticky` will also work.

One last quick point: **the pink box ignores the padding of the containing block.** It sits right up against the border, even though each of these boxes has `16px` of padding. The way to think about this: padding is used in Flow layout calculations, and absolute elements are taken out-of-flow. Those rules don't apply.
## Bubble Border

Absolute positioning can be very useful when it comes to creating whimsical flourishes! Let's create a “bubble border”:
```css
<style>
  .box {
    height: 150px;
    margin: 64px;
    border: 4px solid blue;
  }

  .circle {
    position: obsolute;
    border: inherit;
  }

  .big.circle {
    width: 50px;
    height: 50px;
    position: obsolute;
    top: 100px;
    left: 1110px;
    border-radius: 50%;
  }
</style>

<div class="box">
  <div class="big circle"></div>
  <!-- <div class="medium circle"></div>
  <div class="small circle"></div> -->
</div>
```

# Stacking Contexts

Here's a question with a surprisingly-complex answer: how does the browser decide which element to render "on top" when elements overlap?

It depends on the layout mode!

In Flow layout, elements don't overlap much, but we can force it with negative margin
in Flow layout, content is painted separately from the background.

Check out what happens if we add some text to these boxes
![[Pasted image 20231213113909.png]]
```css
<style>
  .box {
    width: 50px;
    height: 50px;
    border: 3px solid;
    background: silver;
    font-size: 2rem;
    text-align: center;
  }
  
  .second.box {
    margin-top: -30px;
    margin-left: 20px;
    background: hotpink;
  }
</style>

<div class="first box">
  A
</div>
<div class="second box">
  B
</div>
```
#ImportantPoint In Flow layout, background colors and borders are truly meant to be _in the background_. The content will float on top. That's why the letter `A` shows up on top of the pink box.

The truth is that Flow layout isn't really built with layering in mind. Most of the time, when we want to layer elements, we'll want to use positioned layout.

Check out what happens if we add relative positioning to the silver box:
```css
<style>
  .first.box {
    position: relative;
  }
</style>

<div class="first box">
  A
</div>
<div class="second box">
  B
</div>
```
![[Pasted image 20231213114051.png]]
#ImportantPoint As a general rule, **positioned elements will always render on top of non-positioned ones**. We can think of it as a two-stage process: first, all of the non-positioned elements are rendered (everything using Flow, Flexbox, Grid…). Next, all of the positioned elements are rendered on top (relative, absolute, fixed, sticky).

What if we set _both_ elements to use relative positioning? In that case, the DOM order wins
To summarize:
- When all siblings are rendered in Flow layout, the DOM order controls how the background elements overlap, but the content will always float to the front.
- If one sibling uses positioned layout, it will appear above its non-positioned sibling, no matter what the DOM order is.   
- If both siblings use positioned layout, the DOM order controls which element will be on top. Unlike in Flow layout, the content does not float to the front.

That's how the stacking order is calculated by default, but CSS gives us a tool to override this default behaviour. Let's talk about the `z-index` property.
## z-index

If we want the layered order to be different from the DOM order, we can use the `z-index` property to manually reorder them:
```css
<style>
  .box {
    position: relative;
  }
  
  .first.box {
    z-index: 2;
  }
  
  .second.box {
    z-index: 1;
  }
</style>

<div class="first box">
  A
</div>
<div class="second box">
  B
</div>
```
`z-index` only works with positioned elements. It will have no effect on an element being rendered in Flow layout.
The `z` in `z-index` refers to the `z` axis:
- `x` is left/right
- `y` is up/down 
- `z` is forward/backward
A good way to think about this is that elements with a higher z-index are placed _closer_ to the viewer in 3D space, coming out of the screen:
![[Pasted image 20231213114601.png]]
### Negative z-indexes

z-index values must be integers, and they're allowed to be negative. `z-index: -1` is a valid declaration.

In my experience, though, negative z-indexes introduce additional complexity without offering much benefit. Every time I've tried to use negative z-index values, I've wound up regretting it.

As such, we won't cover them in this course.
## Introducing stacking contexts

Video : https://player.vimeo.com/video/496500884
Code from the video
```css
<style>
  header {
    position: relative;
    z-index: 2;
  }

  main {
    position: relative;
    /*
      Toggle this property to
      create/destroy the stacking
      context
    */
    /* z-index: 1; */
  }

  .tooltip {
    position: absolute;
    z-index: 999999;
    top: -12px;
  }
  /* Additional styles: */
  body {
    background: #eee;
  }

  header {
    height: 60px;
    line-height: 60px;
    background: pink;
    text-align: center;
  }

  main {
    padding: 32px;
  }

  .tooltip {
    left: 0px;
    right: 0px;
    margin: 0 auto;
    width: 90px;
    text-align: center;
    padding: 8px;
    background: white;
    box-shadow: 1px 2px 8px hsl(0deg 0% 0% / 0.25);
    border-radius: 6px;
  }
</style>

<header>
  My Cool Site
</header>

<main>
  <div class="tooltip">
    A tooltip
  </div>
  <p>Some main content</p>
</main>
```
We can map out the stacking contexts being created in this snippet:

- The root context
    - `<header>`     
    - `<main>`     
        - `<div class="tooltip">`

Our `.tooltip` element has a z-index of 999999, but that value is only relevant within the `<main>` stacking context. It controls whether the tooltip shows up above or below the adjacent `<p>` tag, nothing more.

Meanwhile, in the parent context, `<header>` and `<main>` are compared. Because `<main>` has a smaller z-index, it shows up underneath `<header>`. **All of its children come along for the ride.**


**It's like semantic versioning**

I recognize that not everyone has experience with software like Photoshop / Figma / Sketch. If the analogy above didn't resonate, I have another one that you're more likely to be familiar with: _semantic versioning._

In semantic versioning, different "tiers" of versions are separated by dots. For example, version 2.0 of a package is a larger version than 1.0, but it's also a larger version than 1.999.

z-indexes are like version numbers, and stacking contexts are like tiers. Every time a stacking context is created, we add a dot to our version:
```html
<header> <!-- 2.0 -->
  My Cool Site
</header>
<main> <!-- 1.0 -->
  <div class="tooltip"> <!-- 1.999999 -->
    A tooltip
  </div>
</main>
```
Our tooltip shows up underneath our `<header>` because 1.999999 is a lower version than 2.0. It doesn't matter how many 9s we add to the minor version, it'll never eclipse a larger major version.

### Creating new contexts

#ImportantPoint In the video above, we saw how we can create a stacking context by combining a non-static position with a `z-index`. This isn't the only way, however!

Here are some other declarations that create a new stacking context:
- Setting `opacity` to a value less than `1`
- Setting `position` to `fixed` or `sticky` (No z-index needed for these values!)
- Applying a `mix-blend-mode` other than `normal`
- Adding a `z-index` to a child inside a `display: flex` or `display: grid` container
- Using `transform`, `filter`, `clip-path`, or `perspective`
- Explicitly creating a context with `isolation: isolate` (More on this soon!)

If you're curious, you can see the [full list of how stacking contexts are created](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Positioning/Understanding_z_index/The_stacking_context) on MDN.

**This can lead to some surprising situations.** Check out what's happening here:
```css
<style>
  header {
    position: relative;
    z-index: 2;
  }
  .tooltip {
    position: absolute;
    z-index: 999999;
  }
  main {
    position: relative;
    /*
      No more z-index…
      but it's still broken??
    */
    will-change: transform;
  }
</style>

<header>
  My Cool Site
</header>
<main>
  <div class="tooltip">
    A tooltip
  </div>
  <p>Some main content</p>
</main>
```
`main` doesn't set a z-index anymore, but it uses `will-change`, a property that can create a stacking context all on its own.
## A common misconception about z-index

In order for z-index to work, we need to set `position` to something like `relative` or `absolute`, right?

Not quite. Check out what's happening here
```css
<style>
  .wrapper {
    display: flex;
  }
  .second.box {
    z-index: 1;
    background: hotpink;
    margin-top: 20px;
    margin-left: -20px;
    margin-right: -20px;
  }
</style>

<div class="wrapper">
  <div class="first box"></div>
  <div class="second box"></div>
  <div class="third box"></div>
</div>
```
![[Pasted image 20231213120248.png]]
The second box is lifted above its siblings using `z-index`. There are no `position` declarations anywhere in the snippet, though!

In general, `z-index` only works with "positioned" elements (elements that set `position` to something other than the default “static”). But the Flexbox specification adds an exception: flex children can use `z-index` even if they're statically-positioned.

An earlier version of this post said that all elements that create a stacking context can use `z-index`, but that was incorrect. 😬

## Hold on a minute…

There's a Weird Thing here, and I think it's worth pondering about for a minute or two.

In our Photoshop analogy, there is a clear distinction between groups and layers. All of the visual elements are layers, and groups can be conjured as structural helpers to contain them. They are distinct ideas.

On the web, however, the distinction is a bit less clear. Every element that uses z-index must _also_ create a stacking context.

When we decide to give an element a z-index, our goal is typically to lift or lower that element above/below some other element in the parent stacking context. _We aren't intending to produce a stacking context on that element!_ But it's important that we consider it.

When a stacking context is created, it “flattens” all of its descendants. Those children can still be rearranged internally, but we've essentially locked those children in.

Let's take another look at the markup from earlier:
```css
<header>
  My Cool Site
</header>
<main>
  <div class="tooltip">
    A tooltip
  </div>
  <p>Some main content</p>
</main>
```
By default, HTML elements will be stacked according to their DOM order. Without any CSS interference, `main` will render on top of `header`.

We can lift `header` to the front by giving it a z-index, but not without flattening all of its children. This mechanism is what led to the bug we discussed earlier.

#ImportantPoint We shouldn't think of `z-index` purely as a way to change an element's order. We should _also_ think of it as a way to form a group around that element's children. z-index won't work unless a group is formed.

**Believe it or not, this is a good thing**

As we've seen in our tooltip demo, stacking contexts can cause subtle, hard-to-diagnose bugs. Wouldn't it be better if z-index values were compared globally instead?

I don't think so, and I can think of a few reasons why:

- As it stands, z-index inflation (the ever-creeping-upwards trend of huge z-index values) is an epidemic. Imagine how much worse it would be if _every single element with a z-index_ had to fit in the same scale?
- I'm not a browser engineer, but I'd guess that stacking contexts are good for performance. Without them, the browser would have to compare every item with a z-index against every other item with a z-index. Sounds like a lot more work.
- Once we understand stacking contexts, we can use them to our advantage to "seal off" elements. This is an especially powerful pattern with component-driven frameworks like React.

That last point is especially interesting. Let's dig deeper into it.
## Airtight abstractions with “isolation”

One of my favourite CSS properties is also one of the most obscure. I'd like to introduce you to the `isolation` property, a hidden gem in the language.

Here's how you'd use it:
```css
.wrapper {
  isolation: isolate;
}
```
When we apply this declaration to an element, it does precisely 1 thing: it creates a new stacking context.

With so many different ways to create a stacking context, why do we need another one? Well, with every other method, stacking contexts are created implicitly, as the result of some other change. `isolation` creates a stacking context in the purest way possible:
- No need to prescribe a z-index value
- Can be used on statically-positioned* elements   
- Doesn't affect the child's rendering in any way

This is **incredibly useful**, since it lets us "seal off" an element's children.
## Debugging stacking contexts

Stacking contexts are the source of a lot of trouble.

When I worked at Khan Academy, we kept having regressions around our modal and our site header; no matter how aggressively-high we set the modal's `z-index`, the blasted header kept poking out on top.

On this very course platform, early beta users spotted a similar problem:

Video showing the problem : https://courses.joshwcomeau.com/cfj-mats/envelope/z-index-bug.mp4

No matter how much experience you have, you'll occasionally run into these issues. The good news is that with the right combination of knowledge, experience, and tooling, we can solve these issues without breaking a sweat.

We're going to learn more about stacking contexts in the lessons ahead, but I want to introduce a _super_ nifty tool first: [**CSS Stacking Context Inspector**](https://github.com/andreadev-it/stacking-contexts-inspector).

This is a free Chrome/Firefox extension which answers a few critical questions about any individual element:

- Which stacking context does this element belong to?
- Does it create a stacking context of its own?
- If it uses the `z-index` property, is it having any effect? If not, why not?
- Where does it sit relative to other elements in the same stacking context?
# Managing z-index

One of the most common frustrations when it comes to CSS is getting stuck fighting the "z-index wars".

Here's how this happens: you have an element which is rendering behind another element, but you want it to be in front. So you pick a bigger value for its z-index, maybe 100, and it solves your problem. Later, you have another element that needs to be even higher, so you pick an even higher arbitrary value. This process repeats over and over. As the application matures, the numbers get bigger and bigger. It's like z-index inflation.

Here's the good news: we don't have to play these reindeer games!

In some cases, we can avoid setting z-index, relying on DOM order instead. And in other cases, we can bundle up our layers into an isolated stacking context.

Let's look at some strategies for reducing z-index pain.
## Swapping DOM order

Let's suppose we have a card, and we want to sprinkle some decorative blobs behind the card:
![[Pasted image 20231213121800.png]]
We'll use absolute positioning to place those shapes around the card. The code might look something like this:
```css
<style>
  .wrapper {
    /* Create a containing block */
    position: relative;
  }
  .card {
    position: relative;
    z-index: 2;
  }
  .decoration {
    position: absolute;
    z-index: 1;
  }
</style>

<div class="wrapper">
  <div class="card">
    Hello World
  </div>
  <img
    alt=""
    src="/decorative-blob-1.svg"
    class="decoration"
    style="top: -20px; left: -70px;"
  />
  <img
    alt=""
    src="/decorative-blob-2.svg"
    class="decoration"
    style="top: -50px; left: -10px;"
  />
  <!-- Other blobs omitted for brevity -->
</div>
```
We want the card to sit in front of the blobs, so we give it a higher z-index.

But! If we were to switch the order of these DOM nodes, we wouldn't need to use z-index at all:
```css
<style>
  .wrapper {
    position: relative;
  }
  .card {
    position: relative;
  }
  .decoration {
    position: absolute;
  }
</style>

<div class="wrapper">
  <img
    alt=""
    src="https://courses.joshwcomeau.com/cfj-mats/decorative-blob-1.svg"
    class="decoration"
    style="top: -20px; left: -70px;"
  />
  <img
    alt=""
    src="https://courses.joshwcomeau.com/cfj-mats/decorative-blob-2.svg"
    class="decoration"
    style="top: -50px; left: -10px;"
  />
  <img
    alt=""
    src="https://courses.joshwcomeau.com/cfj-mats/decorative-blob-3.svg"
    class="decoration"
    style="bottom: -80px; right: -50px;"
  />
  <img
    alt=""
    src="https://courses.joshwcomeau.com/cfj-mats/decorative-blob-4.svg"
    class="decoration"
    style="bottom: 50px; right: -120px;"
  />
  <div class="card">
    Hello World
  </div>
</div>
```
If we don't specify a z-index, the browser will paint positioned elements based on their DOM order. So as long as our card uses positioned layout (with `position: relative`) and comes _after_ the blobs, it'll be painted on top. This is true across browsers and devices.

(We can put the CSS rules in whichever order we'd like; the only thing that matters is the order of the HTML elements.)

> **Be careful with this strategy!(warning)**
> Swapping the DOM order to control rendering can be a very useful trick, but it isn't always appropriate.
> 
> When we swap the order of two DOM nodes, we also swap their order in the tab index. For folks who navigate with a keyboard, they encounter elements _based on the DOM order_.
> 
> In the example above, this isn't a problem, since the decorative images aren't interactive. Keyboard users will skip right past them no matter where in the DOM they are.
> 
> But if we were to swap the order of an element containing _interactive_ elements — links, buttons, form inputs — it can have a jarring effect on the user experience for keyboard navigators.
## Isolated stacking contexts

Let's suppose we're building a "pricing" page.

We implement the design we receive, and wind up with the following UI:
![[Pasted image 20231213122740.png]]
We're all set to ship it, when our PM swings by our desk and says “Hi Pruthvi — the marketing team wants us to make a change…”

The new design emphasizes the "pro" plan by floating it so that it sits above the other two cards:
![[Pasted image 20231213122756.png]]
We can render this sort of UI using something like Flexbox, but we'll hit a problem: by default, elements stack according to their DOM order. We'll wind up emphasizing the wrong card:
![[Pasted image 20231213122826.png]]

Unfortunately, we can't use the DOM-order-swap trick we learned earlier—it would mess up the keyboard tab order. So instead, we'll use `z-index`, giving the middle card a higher z-index value so that it shows up on top:
```css
<style>
  .card {
    position: relative;
    z-index: 1;
  }
  .primary.card {
    z-index: 2;
  }
</style>

<section class="pricing">
  <article class="card">
    <!-- Stuff omitted -->
  </article>
  <article class="primary card">
    <!-- Stuff omitted -->
  </article>
  <article class="card">
    <!-- Stuff omitted -->
  </article>
</section>
```
We test this code, and it works great! The middle card sits on top. So we ship it to production, feeling satisfied with ourselves. But then, an hour later, we receive a Slack message from the customer success team:

“Pruthvi, I think your recent deploy broke something…”

We check it out, and sure enough, something very funky is going on:

Video : https://courses.joshwcomeau.com/cfj-mats/pricing-cards-header-bug.mp4
We forgot about the site's sticky header! And, weirdly, it's slipping _between_ the cards.

Here's why this is happening: the cards and that header are **all in the same stacking context**. Their z-index values are being compared and applied. And it just so happens that the header shares the same z-index value as our primary card.

Here's a wider view of the HTML/CSS responsible for this bug:
```css
<style>
  header {
    position: fixed;
    z-index: 2;
  }

  .card {
    position: relative;
    z-index: 1;
  }
  .primary.card {
    z-index: 2;
  }
</style>

<header>Synergistic Inc.</header>
<main>
  <section class="pricing">
    <article class="card">
      <!-- Stuff omitted -->
    </article>
    <article class="primary card">
      <!-- Stuff omitted -->
    </article>
    <article class="card">
      <!-- Stuff omitted -->
    </article>
  </section>
</main>
```
The two side cards have a `z-index` of 1, so they slip behind the header. But the primary card matches the header's `z-index` of 2. And since the primary card comes later in the DOM order, it shows up on top.

#ImportantPoint In order to fix this, we need to **create an isolated stacking context**. If we can bundle those 3 cards into their own context, we can guarantee that they all slip behind the header.

One way to do this is to give the `.pricing` wrapper a `position` and `z-index`:
```css
.pricing {
position: relative;
z-index: 1;
}
```
These two properties create a stacking context, _flattening_ all of the elements inside. This means that the elements _as a group_ will either sit above or below our header, but there's no way for them to become interlaced with other elements.

It doesn't matter how high the z-index inflation gets _within_ that group, either: even if we had 10 cards with 10 different z-index values, none of those values will matter outside of that context.

This is a key strategy when it comes to fighting the z-index wars. By intentionally bundling layered elements into stacking contexts, we reduce the number of "top-level" elements with z-index values.

But there's one more thing that makes this strategy even better.
### The isolation property

Instead of adding `position: relative; z-index: 1;` to our `.pricing` selector, we can do this:
```css
.pricing {
isolation: isolate;
}
```
#ImportantPoint The `isolation` property does precisely 1 thing: creates a stacking context.

It has the same effect of flattening all of the child elements, but it does so without requiring that we also set a `z-index` on the parent. It's the lightest-touch way to create a stacking context.

This is especially valuable in the era of component-driven frameworks. Our application might have a `Pricing` component that renders our group of cards, and we might use that component in multiple places. This way, we aren't prescribing a z-index value to be used _everywhere_.

Ever since discovering the `isolation` property, I've been using it a ton. Whenever a child within a component applies a `z-index` value, I add `isolation: isolate` to the component's parent element. This guarantees that we won't see weird "slip-in-between" bugs, like the one we saw with the sticky header. But it doesn't contribute at all to z-index inflation, or force me to pick a value.

Adam Wathan, creator of Tailwind, has similarly [discovered its value](https://twitter.com/adamwathan/status/1413172824487907333), and has added an `isolate` utility to the library.

Here's a live-editable version of the code we've been talking about. Play with it yourself to see how it works!

```css
<style>
body {
  background: hsl(260deg 20% 20%);
}
header {
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  padding: 1rem;
  background: hsl(260deg 20% 30%);
  color: white;
}
.card {
  flex: 1;
  max-width: 300px;
  padding: 16px 32px;
  border-radius: 8px;
  background: white;
  box-shadow: 0px 2px 16px hsl(260deg 50% 20% / 0.7);
}
.primary.card {
  flex: 1.25;
  max-width: 350px;
}
.card h2 {
  font-size: 1rem;
  font-weight: 500;
  color: hsl(0deg 0% 40%);
}
.price {
  font-size: 2rem;
  font-weight: 700;
}
.card button {
  width: 100%;
  height: 3rem;
}
.pricing {
  display: flex;
  justify-content: center;
  align-items: flex-end;
}
body {
  padding: 128px 16px;
  min-height: 150vh;
}
  header {
    position: fixed;
    z-index: 2;
  }
  .pricing {
    /*
      Try removing me, and then
      scroll the page.
    */
    isolation: isolate;
  }
  .card {
    position: relative;
    z-index: 1;
  }
  .primary.card {
    z-index: 2;
    margin: -32px -16px;
  }
</style>

<header>
  Synergistic Inc.
</header>
<section class="pricing">
  <article class="card">
    <h2>Starter</h2>
    <div class="price">$29</div>
    <p>For personal projects.</p>
    <ul>
      <li>3 projects</li>
      <li>100gb monthly transfer</li>
      <li>20gb storage</li>
      <li>No support</li>
    </ul>
    <button>Buy Now</button>
  </article>
  
  <article class="primary card">
    <h2>Pro</h2>
    <div class="price">$99</div>
    <p>For small businesses looking to grow. Our most popular plan for ambitious organizations.</p>
    <ul>
      <li>10 projects</li>
      <li>500gb monthly transfer</li>
      <li>1tb storage</li>
      <li>Email customer support</li>
    </ul>
    <button>Buy Now</button>
  </article>
  
  <article class="card">
    <h2>Enterprise</h2>
    <div class="price">Contact Us</div>
    <p>For large orgs.</p>
    <ul>
      <li>Unlimited projects, transers, storage.</li>
      <li>Dedicated phone & email support</li>
    </ul>
    <button>Buy Now</button>
  </article>
</section>
```

>**Flexbox?(warning)**
>
>This snippet uses some CSS we haven't seen yet, like Flexbox and fixed positioning. We'll learn much more about this stuff soon enough.
>
>There's one interesting interaction here, though: The `.card` elements can use `z-index` even if they don't set `position: relative`!
>
>This happens because the Flexbox algorithm uses the `z-index` property in the same way that the Positioned layout algorithm does. `z-index` doesn't work in Flow layout, but it does in Flexbox (as well as Grid).
>
>We'll learn more about how [Flexbox interacts with other layout modes](https://courses.joshwcomeau.com/css-for-js/04-flexbox/11-flex-interactions#flexbox-and-z-index) in Module 4.

`isolation` is supported by all modern browsers, but not by Internet Explorer.

# Fixed Positioning

#ImportantPoint Fixed position is a close cousin to absolute positioning. The main difference is that it's even more rebellious: it can _only_ be contained by the viewport. It doesn't care about containing blocks.

The main advantage of fixed-position elements is that they're immune to scrolling.

For example, here's a help button that sticks in the bottom-right corner regardless of scroll position:
```css
<style>
/* Decorative properties */
body {
  background: hsl(248deg 80% 95%);
}
.help-btn {
  width: 75px;
  height: 75px;
  line-height: 44px;
  border-radius: 50%;
  background: hsl(345deg 100% 40%);
  color: white;
  text-align: center;
  font-size: 20px;
  font-weight: 500;
  border: 3px solid white;
  box-shadow: 2px 2px 20px hsl(248deg 80% 40% / 0.33);
  cursor: pointer;
}
/*
  Artificially boost the size of the
  "body", so that the frame can be
  scrolled.
*/
html {
  height: 100%;
}
body {
  height: 150%;
}
  .help-btn {
    position: fixed;
    right: 32px;
    bottom: 32px;
  }
</style>
<button class="help-btn">
  Help
</button>
```
When you scroll in the “Result” pane, the button doesn't budge. It's cemented in place.

In many ways, “fixed” can be thought of as _spicy absolute_. It's very similar in principle — it's taken out-of-flow and positioned according to some sort of parent boundary — but the boundary it uses is different. Instead of the closest non-static ancestor, it listens to the _“initial containing block”_, a box the size and position of the viewport
Many of the tips and tricks we learned for absolute positioning will work here as well: for example, a fixed element can be centered on the screen using the [same party trick](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/03-centering-trick#absolute-centering). This is perfect for overlays like modals:

**Fixed without anchor points?(info)**

Here's a question for you: what do you suppose happens if we remove the "anchor points" (`top`, `left`, `right`, and `bottom`) for a fixed-position element?

Well, let's give it a shot! Below, you'll find a playground anchored to the bottom right corner. Try removing the `right` and `bottom` properties:
```css
<style>
  .help-btn {
    position: fixed;
    /* 👇 Remove these two properties */
    right: 32px;
    bottom: 32px;
  }
  body {
  background: hsl(248deg 80% 90%);
}

.wrapper {
  margin-top: 100px;
  margin-left: 100px;
  height: 900px;
  border: solid;
  background: hsl(248deg 80% 95%);
}

.help-btn {
  width: 75px;
  height: 75px;
  line-height: 44px;
  border-radius: 50%;
  background: hsl(345deg 100% 40%);
  color: white;
  text-align: center;
  font-size: 20px;
  font-weight: 500;
  border: 3px solid white;
  box-shadow: 2px 2px 20px hsl(248deg 80% 40% / 0.33);
  cursor: pointer;
}
</style>

<div class="wrapper">
  <button class="help-btn">
    Help
  </button>
</div>
```
Here is what you should see: https://courses.joshwcomeau.com/cfj-mats/fixed-without-anchor.mp4?v=2

If we don't set an anchor point, **they sit in their in-flow position**. If this element wasn't `position: fixed`, it would sit in the top-left corner of its parent element, `.wrapper`. This behavior is consistent with absolute positioning.

Amazingly, though, fixed positioning still works! When we scroll the “Result” pane, the box stays locked in place!

This is mostly a curiosity, but it can be useful in certain situations, when we want to "inherit" an in-flow position while still remaining fixed in place.
## Incompatibility with certain CSS properties

Certain CSS properties, when applied to an ancestor, will mess with fixed positioning.

#ImportantPoint For example, if an ancestor (parent, grandparent, …) uses the `transform` property, it stops being locked to the viewport:
```css
<style>
  .container {
    margin: 50px;
    border: solid hotpink;
    /*
      This property breaks
      fixed positioning on
      ALL descendants:
    */
    transform: translate(1px, 1px);
  }

  .fixed {
    position: fixed;
    top: 0;
  }

  /*
    Artificially boost the size of the
    "body", so that the frame can be
    scrolled.
  */
  html, body {
    height: 125%;
  }
</style>

<div class="container">
  <button class="fixed">
    ☹️ I'm not really fixed
  </button>
</div>
```
**Here's what's happening here:** By applying a transform to `.container`, it becomes the containing block for this fixed-position child. As a result, it functions like an absolutely-positioned child.

### Diagnosing the problem

Frustratingly, this issue often pops up in large and complex applications. There might be 15-20 ancestors above our fixed-position element; do we have to check _all_ of them??

I've created a short snippet that can help us automatically find the culprit:

```js
// Replace “.the-fixed-child” for a CSS selector
// that matches the fixed-position element:
const selector = '.the-fixed-child';

function findCulprits(elem) {
  if (!elem) {
    throw new Error(
      'Could not find element with that selector'
    );
  }

  let parent = elem.parentElement;

  while (parent) {
    const {
      transform,
      willChange,
      filter,
    } = getComputedStyle(parent);

    if (
      transform !== 'none' ||
      willChange === 'transform' ||
      filter !== 'none'
    ) {
      console.warn(
        '🚨 Found a culprit! 🚨\n',
        parent,
        { transform, willChange, filter }
      );
    }
    parent = parent.parentElement;
  }
}

findCulprits(document.querySelector(selector));
```
To use this snippet, copy/paste it into the browser console. It will log out any ancestors that set one of the troublesome CSS properties. You'll have an opportunity to practice in the exercise below.

Once you find the element(s) in question, there are two things you can do:

1. You can try to remove or replace the CSS property (eg. for `filter: drop-shadow`, you can use `box-shadow` instead).
2. If you can't change the CSS, you can [use a portal](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/10-portals), like we saw in the previous lesson, or otherwise find a way to move the fixed element to a different container.

## Exercises

### Reuniting the boxes

I've created a little codepen that includes a broken fixed element. **Your mission is to fix it, using the browser devtools and the snippet above.**

The element in question is a solid purple box. Your goal is to reunite it with a hollow purple box:
Solve this problem **using the snippet provided above,** rather than looking through the CSS code (it would be like trying to find a needle in a haystack in a larger, more-realistic scenario!).

- [Access the Codepen](https://codepen.io/joshwcomeau/full/KKgBmYL)
This exercise is considered "solved" when you find and disable the culprit from the “Elements” pane, reuniting the boxes.

Solution video : https://player.vimeo.com/video/596727551

# Overflow

When designers work on mockups, they tend to make assumptions about the kinds of data we'll be working with; they might, for example, assume that all names are fewer than 20 characters long.

As JS developers, we know that these assumptions never survive first contact with real data. 😅

As a fun example: you've probably heard of Pablo Picasso, the world-famous Spanish artist, with the weird geometrical faces. But do you know his full name? Here it is:

This section deals with **overflow**, a condition that happens when content doesn't fit into its parent's content box.

Here's a quick example:
```css
<style>
  .info {
    width: 150px;
    max-height: 100px;
    border: 3px solid;
  }
</style>

<div class="info">
  <strong>Name:</strong> Pablo Diego José Francisco de Paula Juan Nepomuceno María de los Remedios Cipriano de la Santísima Trinidad Ruiz y Picasso
</div>
```
The browser solves for this by letting the content spill outside the bounds, but without accounting for it in flow computations. If we add some additional content below that `name` box, you'll see that _the overflow has no effect on layout_, and we get a big mess of overlapping text:
```css
<style>
  .info {
    width: 150px;
    max-height: 100px;
    border: 3px solid;
  }
</style>

<div class="info">
  <strong>Name:</strong> Pablo Diego José Francisco de Paula Juan Nepomuceno María de los Remedios Cipriano de la Santísima Trinidad Ruiz y Picasso
</div>
<div class="info">
  <strong>Born:</strong> 25 October 1881
</div>
```
To help us manage these kinds of situations, the browser makes a property available: `overflow`.
## Accepted values

`overflow` defaults to `visible`, which allows an element's content to extend beyond its bounds. Let's see what our other options are.
### Scroll

If we know that our content is going to overlap, we can slap an `overflow: scroll` declaration on it:
```css
<style>
  .info {
    overflow: scroll;
    width: 150px;
    max-height: 100px;
    border: 3px solid;
  }
</style>

<div class="info">
  <strong>Name:</strong> Pablo Diego José Francisco de Paula Juan Nepomuceno María de los Remedios Cipriano de la Santísima Trinidad Ruiz y Picasso
</div>
<div class="info">
  <strong>Born:</strong> 25 October 1881
</div>
```
**A warning for macOS developers!(warning)**

Beware: depending on your operating system and peripherals, `overflow: scroll` can look quite different!
Technically speaking, `overflow` is a shorthand for 2 distinct properties:
- `overflow-x`
- `overflow-y`
When we pass a single value, it uses that value for both horizontal and vertical axes. If we only want to allow scrolling in 1 direction, though, we can be a bit more precise:

### Auto

`overflow: auto` is a "have your cake and eat it too" kind of property. It's recommended for most situations where you want a given element to be scrollable.
```css
<style>
  .info {
    overflow: auto;
    max-height: 100px;
    border: 3px solid;
  }
</style>

<div class="info">
  <strong>Name:</strong> Pablo Diego José Francisco de Paula Juan Nepomuceno María de los Remedios Cipriano de la Santísima Trinidad Ruiz y Picasso
</div>
<div class="info">
  <strong>Born:</strong> 25 October 1881
</div>
```
`auto` is a smart value that adds a scrollbar when one is required. Try resizing the "Result" frame above to see what happens when the name can't fit!

We won't always know if an element will need a scrollbar or not: windows come in lots of shapes and sizes (not to mention, the content itself might be dynamic!). `overflow: auto` is the ideal behaviour when we know an element _might_ overflow.

Should we pop this declaration onto all elements? I don't think so; we often _want_ content to overflow, as we saw in the [negative-margins](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/07-margin#negative-margin) and [absolute-positioning](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/06-exercises#bubble-border) lessons.

**Why use overflow: scroll?(info)**
In most cases, `overflow: auto` is a better choice than `overflow: scroll`, but as with everything, there are tradeoffs involved.

Inside an `auto` container, a layout shift will occur when the content grows to exceed the available space; the content box shrinks by ~15 pixels, the width of the scrollbar.

This can be a bit jarring, so if you _know_ that a container will need to scroll, using `overflow-y: scroll` can make for a smoother experience.

An example might be any UI with a "Load more" button. If we know that the additional content will not fit in our container, I like to start with the scrollbar.

We'll discuss this optimization strategy [much later in the course](https://courses.joshwcomeau.com/css-for-js/09-little-big-details/10.04-scroll-optimization).
### Hidden

Finally, there's the most extreme option: `hidden`.
This option truncates anything that extends beyond the bounds of the container:
Why would you ever want to do this? I can think of two main reasons:

1. Hidden overflow is a necessary ingredient for truncating text with an ellipsis (…). We'll learn all about that in [Module 6](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/03-text-overflow).
2. We can hide overflow for artistic purposes, on decorative elements:
```css
<style>
  .wrapper {
    overflow: hidden;
    position: relative;
    height: 150px;
    border: 3px solid;
    border-radius: 8px;
  }
  .flourish {
  position: absolute;
  border-radius: 100px;
  width: 75px;
  height: 75px;
}
.flourish.one {
  background: slateblue;
  right: -40px;
  top: -20px;
}
.flourish.two {
  background: deeppink;
  right: 0px;
  top: -45px;
}
</style>

<div class="wrapper">
  <div class="flourish one"></div>
  <div class="flourish two"></div>
</div>
```
Try removing `overflow: hidden`, and you'll notice two things:

1. The decorative blobs are no longer being constrained by the box.
2. We've introduced an undesirable horizontal scrollbar!

Accidental horizontal scrollbars are awful. We'll learn how to identify and prevent them in [Module 5](https://courses.joshwcomeau.com/css-for-js/05-responsive-css/13-scrollburglars).

**Do future-you a favour(info)**
So here's the thing about `overflow: hidden`. It's often deployed strategically, to solve specific problems.

In this course platform, for example, I shift content over to show the menu on mobile:
Video : https://courses.joshwcomeau.com/cfj-mats/overflow-mobile-menu.mp4
I use `overflow: hidden` to make sure that when the menu is open, the lesson content doesn't force the container to be wider than the screen.

In my source code, I added a detailed comment explaining exactly why I'm using this property:
```css
.wrapper {
  /*
    On mobile, we shift the lesson-content 300px to the right,
    off-screen. I want it to be truncated, so that we only see
    a sliver of the content when the menu is open.
  */
  overflow: hidden;
}
```
#ImportantPoint Adding detailed comments when using `overflow: hidden` is absolutely critical. Otherwise, you'll never remember why you set the property. If you refactor this property away, it won't be immediately obvious that you've broken something; it only causes problems on mobile, and this is primarily a desktop application.

**My rule of thumb:** Always add a comment when employing this declaration. Future-you will thank you.
# Scroll Containers

In CSS, there are certain “hidden mechanisms”, devices and concepts that exist within the language, but are totally invisible to most developers. If we want to _truly_ understand how CSS works, we have to learn about these mechanisms.

One such mechanism is the _scroll container_.

Let's suppose we're trying to do something like this:
![[Pasted image 20231214110906.png]]
Notice that the circles are cropped horizontally, but allowed to spill out vertically.

How should we solve this? Well, maybe we can take advantage of `overflow-x`, to hide overflow along the X axis? Maybe something like this?
```css
.wrapper {
  /* Hide overflow in the X axis: */
  overflow-x: hidden;
  /* ...but allow it in the Y axis: */
  overflow-y: visible;
}
```
Unfortunately, this doesn't work:
```css
<style>
  .wrapper {
    overflow-x: hidden;
    overflow-y: visible;
    background: pink;
  }
  body {
  background: hsl(0deg 0% 95%);
  padding: 32px;
}
.wrapper {
  position: relative;
  height: 150px;
}
.flourish {
  position: absolute;
  border-radius: 100px;
  width: 75px;
  height: 75px;
}
.flourish.one {
  background: slateblue;
  right: -40px;
  bottom: 10px;
}
.flourish.two {
  background: deeppink;
  right: -20px;
  bottom: -45px;
}
</style>

<div class="wrapper">
  <div class="flourish one"></div>
  <div class="flourish two"></div>
</div>
```
Hm, it's as if we set `overflow-y: scroll`. What's going on here?

**To understand what's going on here, we need to learn about _scroll containers_**

I like to think of scroll containers like the _TARDIS_ from the British sci-fi show _Dr. Who_: It's a regular-sized telephone ship from the outside, but a large spaceship inside, somehow defying physics.

#ImportantPoint When we set the `overflow` property to `scroll`, `hidden`, or `auto`, we create one of these magical "bigger inside than outside" spaceships.

For example, this `.wrapper` element is a 150px-tall box, and yet it somehow contains a much larger image, as if it was a portal to some alternative dimension:
```css
<style>
  .wrapper {
    height: 150px;
    background: pink;
    overflow-y: auto;
  }
  .photo {
    display: block;
    width: 100%;
  }
</style>

<div class="wrapper">
  <img
    class="photo"
    alt="artistic shot of a building"
    src="https://courses.joshwcomeau.com/cfj-mats/architecture-julien-moreau.jpg"
  />
</div>
```
**And here's the problem:** when a container becomes a scroll container, it manages overflow in _both directions_. The moment we set `overflow-x` _or_ `overflow-y`, it becomes a portal to an alternative dimension, and all children/descendants will be affected.

When a child is placed in a scroll container, it _guarantees_ that the child will never spill outside of it. It's on the other side of the portal! Either a child _is_ or _isn't_ in a scroll container. We can't mix and match for vertical/horizontal.

**Critically, this is true regardless of whether we set `scroll`, `auto`, or `hidden`.** All 3 values have the same effect: it creates a scroll container.

But wait… Why would `hidden` create a scroll container? It makes sense that `scroll` and `auto` would create a scroll container, but we can't scroll within an `overflow: hidden` element!

#ImportantPoint **Here's the trick:** `overflow: hidden` is identical to `overflow: scroll`, _but with the scrollbars removed._
I'm not sure why it was implemented this way, but an element with `overflow: hidden` is literally a scroll container without scrollbars.

I can prove it. Try to tab through the links within this scroll container:
```css
<style>
  .wrapper {
    height: 100px;
    background: pink;
    overflow: hidden;
  }
</style>

<div class="wrapper">
  <ol>
    <li><a href="/">Link one</a></li>
    <li><a href="/">Link two</a></li>
    <li><a href="/">Link three</a></li>
    <li><a href="/">Link four</a></li>
    <li><a href="/">Link five</a></li>
    <li><a href="/">Link six</a></li>
  </ol>
</div>
```
As you tab through the links, the container should automatically scroll
There may not be any visible scrollbars, but it's definitely still a scroll container. We can force it to scroll by tabbing through interactive elements. A crafty user might even write some JS that can programmatically scroll this container!

So, to summarize: #ImportantPoint 

- When we use `overflow: scroll`, `overflow: auto`, or `overflow: hidden`, we create a scroll container. This is true whether we set the property on the X axis, the Y axis, or both.
- A scroll container is like a portal to a pocket dimension. When an element is contained by a scroll container, it's guaranteed to be stuck inside. It will never overflow beyond the 4 corners of the scroll container.
- Setting `overflow: hidden` creates a scroll container and then hides the scrollbars. It follows all the same rules as `overflow: scroll`.
But, don't give up hope! Modern CSS has provided a **shiny new way** to solve this problem.
## Overflow: clip

#ImportantPoint Over the past few months, a new `overflow` value has been landing in browsers:
`overflow: clip` works quite a bit like `overflow: hidden`, _but it doesn't create a scroll container_. Essentially, it acts the way most developers think `overflow: hidden` _should_ work. It trims off any overflow, in one or both directions.

**We can solve our problem using this property:**
```css
<style>
  .wrapper {
    overflow-x: clip;
    background: pink;
  }
  body {
  background: hsl(0deg 0% 95%);
  padding: 32px;
}

.wrapper {
  position: relative;
  height: 150px;
}

.flourish {
  position: absolute;
  border-radius: 100px;
  width: 75px;
  height: 75px;
}
.flourish.one {
  background: slateblue;
  right: -40px;
  bottom: 10px;
}
.flourish.two {
  background: deeppink;
  right: -20px;
  bottom: -45px;
}
</style>

<div class="wrapper">
  <div class="flourish one"></div>
  <div class="flourish two"></div>
</div>
```
Pretty cool, right??

With `overflow: clip`, no scroll container is created. Any content that spills outside the bounds of this containing block is made invisible.

In terms of browser support, `overflow: clip` [is supported in all major browsers](https://caniuse.com/mdn-css_properties_overflow_clip), though it only arrived in Safari in September 2022, with version 16. As I write this in November 2022, ~20% of users are using browsers that don't support `overflow: clip`, mostly because of Safari users on older versions of iOS/macOS.

That's not the only catch, either. If the container has a `border-radius` set, it will force the clipping to happen in both directions in certain browsers:

So, given these caveats, it might be a _little_ early to start relying on `overflow: clip`.

**Can we solve this problem without `overflow: clip`?** We can indeed! In the next section, I'll share the workaround I've been using for years.

**A blessing and a curse(warning)**
`overflow: clip` is a wonderful addition to the CSS language, but there are some significant tradeoffs worth considering.

For example, let's update our list of links to use `clip`:

Because no scroll container is created, the final couple of links won't be made visible upon focus. As we tab through the list, the focus indicator becomes invisible, and we have no idea what we're selecting.

`overflow: hidden` has built-in guardrails: interactive elements like links, buttons, and form inputs will be made visible if they're focused, but we lose these guardrails with `overflow: clip`. The onus is on us to test across different devices and screen sizes, to make sure we aren't accidentally building something unusable!

## Workaround

So, let's suppose we don't want to use `overflow: clip`, because we want something that will work for 100% of users.

Here's how I'd solve it:
```html
<style>
  html, body {
    height: 100%;
  }
  .outer-wrapper {
    overflow-x: hidden;
    min-height: 100%;
    /*
      Adding a border so you can see the
      size/shape of this container:
    */
    border: 2px dashed silver;
  }
  .wrapper {
    background: pink;
  }
</style>

<div class="outer-wrapper">
  <div class="wrapper">
    <div class="flourish one"></div>
    <div class="flourish two"></div>
  </div>
  <p>Hello world</p>
</div>
```
**Here's how this works:** I've created a new parent, `.outer-wrapper`, indicated by the dashed silver border. _This_ element is going to be the one that hides overflow. And it's going to wrap over _everything else_ on the page as well.

Our pink box, `.wrapper`, is no longer trying to hide the overflow. It no longer creates a scroll container.

Now, you might be thinking: **won't this still add a vertical scrollbar when the container fills up?** What if I have a bunch of stuff inside?

Well, let's try it:

**Here's how this works:** I've created a new parent, `.outer-wrapper`, indicated by the dashed silver border. _This_ element is going to be the one that hides overflow. And it's going to wrap over _everything else_ on the page as well.

Our pink box, `.wrapper`, is no longer trying to hide the overflow. It no longer creates a scroll container.

Now, you might be thinking: **won't this still add a vertical scrollbar when the container fills up?** What if I have a bunch of stuff inside?

```css
<style>
  html, body {
    height: 100%;
  }
  body {
  background: hsl(0deg 0% 95%);
  padding: 32px;
}
h2 {
  margin: 1em 0;
}
p {
  margin-bottom: 2em;
}

.wrapper {
  position: relative;
  height: 150px;
  border-radius: 8px;
}

.flourish {
  position: absolute;
  border-radius: 100px;
  width: 75px;
  height: 75px;
}
.flourish.one {
  background: slateblue;
  right: -40px;
  bottom: 10px;
}
.flourish.two {
  background: deeppink;
  right: -20px;
  bottom: -45px;
}
  .outer-wrapper {
    overflow-x: hidden;
    min-height: 100%;
    /*
      Adding a border so you can see the
      size/shape of this container:
    */
    border: 2px dashed silver;
  }
  .wrapper {
    background: pink;
  }
</style>

<div class="outer-wrapper">
  <div class="wrapper">
    <div class="flourish one"></div>
    <div class="flourish two"></div>
  </div>
  <h2>
    What is Lorem Ipsum?
  </h2>
  <p>
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
  </p>
  <h2>
    Where does it come from?
  </h2>
  <p>
    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
  </p>
  <p>
    The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
  </p>
  <p>
    Source: https://www.lipsum.com/
  </p>
</div>
```
The trick here is that **scroll containers only scroll when there's overflow.** Because `.outer-wrapper` doesn't have a constrained height, the container is free to grow and shrink as much as it wants. As long as I don't explicitly set something like `height: 400px`, we won't get an awkward scrollbar.

In Module 1, we talked about how `width` and `height` are different; height looks [down the tree](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/11-height) to calculate its height. And so our `.outer-wrapper` will keep growing as we put more stuff on it.

To put it another way: scroll containers only start to scroll when the _inner size_ exceeds the _outer size_. As long as the outer size can keep on growing, that doesn't happen.

# Horizontal Overflow

So far, all of the examples we've seen involve _vertical_ overflow. But what if we want data to overflow in the alternative direction?

For example: let's say we have a collection of images, and we want the user to be able to scroll horizontally:
Images are inline by default. Like words in a paragraph, they line-wrap when they can't all fit. The `overflow` property on its own won't help us:
```css
<style>
  .wrapper {
    overflow: auto;
    border: 3px solid;
  }

  .wrapper img {
    width: 32%;
  }
</style>

<div class="wrapper">
  <img
    alt="Cat licking itself"
    src="https://courses.joshwcomeau.com/cfj-mats/cat-300px.jpg"
  />
  <img
    alt="Curious cat with bright blue background"
    src="https://courses.joshwcomeau.com/cfj-mats/cat-two-300px.jpg"
  />
  <img
    alt="Majestic white cat with piercing blue eyes"
    src="https://courses.joshwcomeau.com/cfj-mats/cat-three-300px.jpg"
  />
  <img
    alt="The grumpiest cat you've ever seen"
    src="https://courses.joshwcomeau.com/cfj-mats/cat-four-300px.jpg"
  />
</div>
```
 How can we instruct the container to _not_ linewrap, and instead to leave the content in a single line? The `white-space` property has got our back:
```css
<style>
  .wrapper {
    overflow: auto;
    border: 3px solid;
    /* The secret ingredient: */
    white-space: nowrap;
  }

  .wrapper img {
    width: 32%;
  }
</style>
```
#ImportantPoint `white-space` is a property that lets us tweak how words and other inline/inline-block elements wrap. By setting it to `nowrap`, we instruct the container to never break lines. That, in tandem with `overflow: auto`, allows us to achieve a horizontally-scrollable element.

We'll learn more about the `white-space` property in Module 6, when we talk about [text wrapping](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/03-text-overflow).

**white-space: nonsense(info)**

You might be wondering: why is `nowrap` smushed together? Why isn't it `no-wrap`, like all other multi-word CSS keywords?

There isn't a good reason. The CSSWG? has [labeled it a mistake in the language](https://wiki.csswg.org/ideas/mistakes).

Here's an easy way to remember this peculiarity: it's like the word “nonsense”. It's not “non-sense”, after all.

# Positioned Layout

When we talk about managing overflow, we're generally thinking about "in-flow" children, either in Flow layout, or something like Flexbox / Grid.

How does overflow work with _positioned_ layout, though? Will an absolutely-positioned child trigger a scrollbar if the parent has `overflow: auto`? What about fixed positioning?

In this lesson, we'll put these ideas under the microscope.
## Overflow and containing blocks

Earlier in this module, we learned about [containing blocks](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/04-containing-blocks). Every element is contained by a block. Most of the time, it's the parent, but absolutely-positioned elements ignore their parents unless they, too, use positioned layout.

This dynamic plays a role when it comes to overflow!

Take a look at the following playground, and see if you can figure out why the pink box is peeking outside its parent, despite the `overflow: hidden`:
```css
<style>
.wrapper {
  position: relative;
  overflow: auto;
}
.box {
  /* Change me to 'fixed': */
  position: fixed;
}
  .wrapper {
    overflow: hidden;
    width: 150px;
    height: 150px;
    border: 3px solid;
  }
  .box {
    top: 24px;
    left: 24px;
    background: deeppink;
    width: 150px;
    height: 200px;
  }
</style>

<div class="wrapper">
  <div class="box" />
</div>
```
`.box` is _not_ being contained by `wrapper`. As a result, it ignores the `overflow: hidden` set on that parent.

We can fix this by adding `position: relative` to the parent:
```css
.wrapper {
  /* The missing ingredient: */
  position: relative;
  
  overflow: hidden;
  width: 150px;
  height: 150px;
  border: 3px solid;
}
```
#ImportantPoint Absolutely-positioned elements act just like static-positioned elements when it comes to overflow. If the parent sets `overflow: auto`, _as long as that parent is the containing block_, it will allow that child to be scrolled into view:
```css
.wrapper {
  position: relative;
  overflow: auto;
  width: 150px;
  height: 150px;
  border: 3px solid;
}
```
This is pretty surprising! In general, absolute positioning is ignored by standard layout algorithms, and yet `overflow: auto` treats it just like any other element!

It's important to realize this so that you don't get caught off guard by this peculiar behaviour.

**Using this knowledge to our advantage(success)**:
Here's a common frustration: you have an element that creates a scroll container (eg. through `overflow: hidden`), but you want to let _some_ items escape the scroll container. For example, maybe you want to add a tooltip to a scrollable list:
Video : https://courses.joshwcomeau.com/cfj-mats/overflow-breakout.mp4
In general, I recommend solving this problem using portals, as we saw [a few lessons back](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/10-portals). But we can also solve this problem by exploiting the way containing blocks work with scroll containers.

Remember, absolutely-positioned elements will be anchored to their containing block. If their containing block sits _above_ the scroll container, the element will be free to spill beyond.
Here's the sort of structure that could work:
```css
<style>
/*
  Cosmetic / placeholder styles,
  to show that it's working.
*/
.scroll-container {
  width: 200px;
  height: 200px;
  border: solid;
}
ol {
  margin: 0;
  /* Force a scrollbar */
  height: 600px;
}
.tooltip {
  width: 100px;
  height: 100px;
  background: pink;
  display: flex;
  justify-content: center;
  align-items: center;
}
  .containing-block {
    position: relative;
  }

  .scroll-container {
    overflow: auto;
  }

  .tooltip {
    position: absolute;
    left: 200px;
  }
</style>

<div class="containing-block">
  <div class="scroll-container">
    <ol>
      <!-- Imagine a list here -->
    </ol>
    <div class="tooltip">
      Boop
    </div>
  </div>
</div>
```

Now, we _will_ need to use some JavaScript in order to position the tooltip in the correct spot. This goes beyond the scope of this course, but the strategy is explored in depth in this fantastic CSS Tricks article: [Popping Out Of Hidden Overflow](https://css-tricks.com/popping-hidden-overflow/).

## Fixed positioning

So, here's a question for you.

If we changed the pink box above from `absolute` to `fixed`, what would happen? Would the parent element remain scrollable?

Take a minute and think about it. Then, try it out, and see if it does what you expect:

```css
<style>
  .wrapper {
    width: 150px;
    height: 150px;
    border: 3px solid;
  }

  .box {
    top: 200px;
    left: 24px;
    background: deeppink;
    width: 150px;
    height: 200px;
  }

  .wrapper {
    position: relative;
    overflow: auto;
  }

  .box {
    /* Change me to 'fixed': */
    position: absolute;
  }
</style>

<div class="wrapper">
  <div class="box" />
</div>
```
This result surprised me at first. Did it surprise you?

#ImportantPoint When we switch to `position: fixed`, the parent's scrollbars disappear, and the element pops into view, as if `overflow` was set to its default value, `visible`. Why is that?

In order for a child to "trigger" the overflow, it needs to be contained by it. Setting `position: relative` is enough to contain an absolute child, but _fixed_ children are only ever contained by the “initial containing block”, a box that exists outside the DOM structure.

In other words: `.wrapper` will only add a scrollbar when one of its _contained_ children spills out of its bounds. But regular ol' HTML elements can't contain fixed children.

Similarly, this also means that fixed-position elements are immune from being hidden with `overflow: hidden`:
# Sticky Positioning

`position: sticky` is the newest addition to the crew. The idea is that as you scroll, an element can "stick" to the edge. At that moment, it transitions from being relatively-positioned to being fixed-positioned.

In addition to setting `position: sticky`, you also need to pick at least one edge to stick to (top, left, right, bottom). Most commonly, this is done with `top: 0px` (or `top: 0`; the unit is optional when it's zero).
```css
<style>
  .sticky-ball {
    position: sticky;
    top: 0;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: deeppink;
  }
  /*
    Artificially boost the size of the
    "body", so that the frame can be
    scrolled.
  */
  html, body {
    height: 150%;
    padding: 48px;
  }
</style>

<div class="sticky-ball"></div>
<p>Scroll within this white box!</p>
```
There's a lot of subtlety with `position: sticky`. Let's go through some of the details.
## Stays in their box

#ImportantPoint An often-overlooked aspect of `position: sticky` is that the element will never follow the scroll outside of its parent container. Sticky elements only stick while their container is in view.

In the following example, scroll all the way to the bottom, and note that the pink circle never leaves the black rectangle:
```css
<style>
  .sticky-ball {
    position: sticky;
    top: 0;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: deeppink;
  }

  .wrapper {
    height: 50%;
    margin-top: 25%;
    margin-bottom: 100%;
    border: 4px solid;
  }
  html, body {
    height: 165%;
  }
</style>

<div class="wrapper">
  <div class="sticky-ball"></div>
</div>
```
I used this effect years ago in a portfolio I created for myself. Notice how each section's header stays adjacent to its content:
Video: https://courses.joshwcomeau.com/cfj-mats/sticky-portfolio-demo.mp4
Here's an example of how this effect could be built. Note that it uses a bit of Flexbox to structure the layout. We'll cover Flexbox in depth in Module 4.
```css
<style>
  section h2 {
    position: sticky;
    top: 0;
  }
  section {
    display: flex;
    align-items: flex-start;
    padding: 8px 0px;
  }
  section p {
    flex: 1;
    margin-left: 32px;
  }
  /*
  Add a bunch of empty space, so that
  we can scroll, and see the effect:
*/
  section:last-of-type {
    margin-bottom: 100vh;
  }
</style>

<section>
  <h2>Section 1</h2>
  <p>large paragraph here..............</p>
</section>
<section>
  <h2>Section 2</h2>
  <p>large paragraph here..............</p>
</section>
<section>
  <h2>Section 3</h2>
  <p>large paragraph here..............</p>
</section>
```
This effect is so cool because it convinces the eye that each heading "knows" to stop before the next one. In reality, each heading is inside a box, and can't leave that box.

Add a border to each `section` to reveal the truth.
## Offset

As we've seen, every `position` value changes the way `top`/`left`/`right`/`bottom` work:
- With relative positioning, the element is shifted from its natural, in-flow position
- With absolute positioning, the element is distanced from its containing block's edge    
- With fixed positioning, the element is adjusted based on the viewport

With sticky positioning, the value controls the **minimum gap between the element and the edge of the viewport** while the container is in-frame.
We can set it to `0px` if we want it to stick right against the edge, or we can pick a bigger number to give it a bit of breathing room. We can even use negative numbers if we want!
```css
<style>
  .sticky-ball {
    position: sticky;
  }
  .sticky-ball.one {
    top: 25px;
  }
  .sticky-ball.two {
    top: 0px;
  }
  .sticky-ball.three {
    top: -25px;
  }
  html,
  body {
    height: 100%;
  }
  .wrapper {
    height: 200%;
    padding: 64px;
    display: flex;
    justify-content: space-between;
  }
  .sticky-ball {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: linear-gradient(0deg,
        deeppink,
        pink);
  }
</style>
<div class="wrapper">
  <div class="sticky-ball one"></div>
  <div class="sticky-ball two"></div>
  <div class="sticky-ball three"></div>
</div>
```
This does feel sorta weird to me. Typically, we imagine directions like `top` pushing an element around, affecting its position on the page. With sticky positioning, however, it's all about the “stick point”. `top` has no effect until we start scrolling.

In many cases, we'll want to use `top: 0px` so that the element sticks the moment the user scrolls to that element, but we can choose different values depending on the effect we're going for.
## Not incorporeal

#ImportantPoint Earlier, we saw how absolute and fixed elements are “incorporeal”—they don't block out any space, like holograms. If they have any static or relative siblings, those siblings will be positioned as if the absolute/fixed elements don't exist.

#ImportantPoint Sticky elements are like relative or static elements in this regard; they're laid out in-flow. They take up real space, and that space remains taken even when the element is stuck to an edge during scrolling.

Toggle the `.main.box` element below between fixed and sticky, and **notice how its siblings and parent container change:**
```css
<style>
  .main.box {
    /* Change me to “fixed”! */
    position: sticky;
    top: 0;
  }
  body {
  padding: 32px;
}
.wrapper {
  border: 2px solid;
  margin-bottom: 100vh;
}
.box {
  border: 4px solid silver;
  width: 40px;
  height: 40px;
}
.main.box {
  border-color: deeppink;
  height: 80px;
}
</style>

<div class="wrapper">
  <div class="main box"></div>
  <div class="box"></div>
  <div class="box"></div>
</div>
```
When we change our pink box to be `position: fixed`, the other boxes move up to fill the space, and the parent shrinks to half of its original height.

Sticky elements are considered "in-flow", while fixed elements aren’t.
## Horizontal stickiness

Sticky positioning is almost always used with vertical scrolling, but it doesn't have to be! Here's an example with both vertical and horizontal stickiness:
```css
<style>
  .box {
    position: sticky;
    top: 0;
    left: 0;
  }
  section {
  padding: 45px 45px;
  width: 100%;
  height: 100%;
}

.box {
  border: 4px solid deeppink;
  width: 50px;
  height: 50px;
}
html, body {
  width: 150%;
  height: 150%;
}
</style>

<section>
  <div class="box"></div>
</section>
```
## Sticky positioning and browser support

Happily, `position: sticky` is [supported across all major browsers](https://caniuse.com/css-sticky).

You may have heard that sticky (or even fixed!) positioning is buggy on mobile. It is true that for a while, iOS Safari in particular had trouble with it… but those days are long over. **You can safely use sticky positioning on iOS and Android.**

For a very long time, `position: sticky` didn't play nicely with HTML tables in Chrome: specifically, you couldn't set a `<thead>` or `<tbody>` to be sticky, you had to set individual cells (and it was kinda wonky). Fortunately, this has been addressed in Chrome 91; [sticky tables work across all major browsers now!](https://twitter.com/chriscoyier/status/1400897989842030593)
## 2. Fix the bug

In the following playground, I expect the pink square to stick to the top edge on scroll, but it isn't working!

Can you figure out why?
```css
<style>
html {
  height: 100%;
}
body {
  height: 150%;
  padding: 0;
}
header, main {
  padding: 16px;
}

.sticky {
  position: sticky;
  top: 0;
  width: 50px;
  height: 50px;
  background: deeppink;
  border-radius: 4px;
}
</style>
<header>
  <div class="sticky"></div>
</header>
<main>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
</main>
```
**Note:** An even better solution might be to move the `position: sticky` to the header! Make the entire header stick, rather than the pink box within. The best solution will depend on the particular circumstances in any given situation.
# Troubleshooting

Unfortunately, it's very common to apply `position: sticky` to an element, only for nothing to happen; the element won't stick!

Let's look at some common reasons for this.
## A parent is hiding/managing overflow

This is probably the most common reason in a large, real-world application.

#ImportantPoint When we set `overflow` to `hidden`/`scroll`/`auto`, we create a scroll container. And when it comes to sticky positioning, elements stick _to the closest scroll container._

Here's a concrete example of the problem:
```css
<style>
  main {
    /*
      Comment out this line to enable
      sticky positioning!
    */
    
    overflow: auto;
  }
  header {
    position: sticky;
    top: 0;
  }
  main {
  height: 120vh;
}
header {
  text-align: center;
  background: pink;
  padding: 8px;
}
</style>

<main>
  <header>
    Sticky Header
  </header>
</main>
```
Because `<main>` sets `overflow: auto`, it creates a scroll container. The header will only stick _when scrolling within this scroll container._

If we reduce the height and add a bunch of content, the scroll container has enough stuff to warrant a scrollbar. Try scrolling within the black box:
```css
<style>
  main {
    overflow: auto;
    max-height: 200px;
  }
  
  header {
    position: sticky;
    top: 0;
  }
</style>

<main>
  <header>
    Sticky Header
  </header>
  <p>
    Because the main tag has a max-height, the content inside that element won't fit. The 'overflow: auto' means that this container will have its own scrollbar, and the header will stick *within this context*.
  </p>
  <p>
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
  </p>
</main>
```
#ImportantPoint  Here's how to think about it: `position: sticky` can only stick in one "context". If it's within a scroll container, it can only stick within that container.

Frustratingly, it doesn't have to be a direct parent, either — it might be a great-great-great-great-grandparent that sets `overflow: hidden`, maybe to remove an unwanted horizontal scrollbar!

**How do we figure out which element is the culprit?** Here's a snippet you can run in the browser devtools to figure it out:
```js
// Replace “.the-sticky-child” for a CSS selector
// that matches the sticky-position element:
const selector = '.the-sticky-child';

function findCulprits(elem) {
  if (!elem) {
    throw new Error(
      'Could not find element with that selector'
    );
  }

  let parent = elem.parentElement;

  while (parent) {
    const { overflow } = getComputedStyle(parent);

    if (['auto', 'scroll', 'hidden'].includes(overflow)) {
      console.log(overflow, parent);
    }

    parent = parent.parentElement;
  }
}

findCulprits(document.querySelector(selector));
```
You can copy/paste this snippet into the browser console, replacing `selector` with a CSS selector that matches your sticky element. It will crawl up the DOM tree looking for an ancestor with `overflow` set to either `auto`, `scroll`, or `hidden`.

**So how do we fix it, once we've found the culprit?**

- If the culprit uses `overflow: hidden`, we can switch to `overflow: clip`. Because `overflow: clip` doesn't create a scroll container, it doesn't have this problem!

- If the culprit uses `auto` or `scroll`, you _might_ be able to remove this property, or push it lower in the DOM. This is a tricky problem, often without a quick solution. We saw an example of this sort of restructuring in the [solution to the last exercise](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/16-sticky-exercises#two-fix-the-bug).
    

Later, in Module 5, we'll discuss some strategies for [removing horizontal scrollbars](https://courses.joshwcomeau.com/css-for-js/05-responsive-css/13-scrollburglars). For now, just know that if sticky positioning isn't working, there's a good chance that an ancestor is managing overflow.
## The sticky element is stretched

When using Flexbox or Grid, it's possible for a sticky element to be stretched along the cross-axis. This, in effect, makes it so that the element has no space to move in its parent container.

We haven't covered Flexbox yet, but if you're already familiar, you can see the problem and its solution in [this Module 4 lesson, under “Sticky Sidebar”](https://courses.joshwcomeau.com/css-for-js/04-flexbox/12-recipes).
## There's a thin gap above my sticky header!

If you intend for an element to sit right against the edge of the viewport, you might discover a thin 1px gap between the element and the edge in Chrome.

This is a rounding issue with fractional pixels. I've solved this issue by insetting the sticky element by a single pixel:
```css
header {
position: sticky;
top: -1px; /* -1px instead of 0px */
}
```

# Hidden Content

We have one last thing to get to before we wrap this module up: _invisible stuff_.

There's a surprising amount of subtlety when it comes to hidden content — there are a variety of ways to hide elements in CSS, and they all come with different tradeoffs. If you're not careful, you can introduce accessibility problems, or hurt your search engine rankings!

Let's look at some of the most common methods.
## display: none

This method is probably the most well-known way to hide content in CSS. It means business: elements hidden using this declaration are effectively removed from the DOM. They're totally invisible and incorporeal.

It's unfortunate that this behaviour is triggered using the `display` property — it already has so many hats to wear! That same property is used to control whether an element is block or inline, as well as used to enable Flexbox and CSS Grid.

A button which is set to `display: none` cannot be clicked or focused. Notice that you can't select the "Two" button by tabbing through the existing buttons:
```css
<style>
  .hidden {
    display: none;
  }
</style>

<button>One</button>
<button class="hidden">Two</button>
<button>Three</button>
<button>Four</button>
```
This property can be very useful when combined with media queries to toggle between mobile and desktop variants of an element:
```css
.desktop-header {
  display: none;
}

@media (min-width: 1024px) {
  .desktop-header {
    display: block;
  }

  .mobile-header {
    display: none;
  }
}
```
In this snippet, we can see that by default, our `.desktop-header` is hidden. If the user's viewport is at least 1024px wide, however, we show the header by setting `display: block`, and hide the _mobile_ header, flipping from one to the other. There will always be exactly 1 visible: never zero, and never both.
## Visibility: hidden

The `visibility` property allows you to hide an element, but in a slightly different way. It's like a cloak of invisibility; the item can't be seen, but it's still there, taking up space.

This property isn't as commonly used, because generally you don't want a big hole in your UI! But sometimes, it's helpful to be able to "hold space open" for an element that will soon become visible.
```css
<style>
  .answer {
    visibility: hidden;
  }
  
  /*
    Show the answer when hovered or focused
  */
  .answer-wrapper:hover .answer,
  .answer-wrapper:focus .answer {
    visibility: visible;
  }
  .answer-wrapper {
  border: none;
  border-bottom: 3px solid;
  background: transparent;
}
h2 {
  font-size: 1rem;
  margin-bottom: 32px;
}
</style>

<h2>Question: What was the first feature-length animated film ever released?</h2>
<p>Answer:
  <button class="answer-wrapper">
    <span class="answer">
      Snow White and the Seven Dwarfs
    </span>
  </button>
</p>
```
## Opacity

Finally, there's opacity!

Unlike the other options, _opacity is not binary_. We can flip it from 1 to 0 to fully hide an element, but we can use fractional values to make it semi-transparent.
Unsurprisingly, hiding an element with opacity does not remove it from flow. In fact, items hidden with opacity aren't _really_ hidden:

- Buttons can still be clicked
- Text is still selectable
- Form elements can still be focused
If we're not careful, we can introduce accessibility issues: imagine we hide a set of buttons, but keyboard users will still be able to tab through them, without knowing where their focus is! Opacity on its own is not a great way to hide something from view.

Opacity is helpful when:

- An item needs to be semi-visible   
- An item's visibility needs to be animated, fading in and out
## Accessibility

We've seen how to hide elements visually, using a few different methods. But not everyone who uses the web views it on a screen. We also need to consider how to make the best possible experience for folks using screen readers.

### Hiding from screens

Let's look at how to hide an element from screens, but keep it discoverable for folks using a screen reader.

Video: https://player.vimeo.com/video/496891624

css snippet for visually hidden elements
```css
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
```
### Hiding from screen readers

The `.visually-hidden` snippet lets us hide content from sighted users while keeping it around for folks using screen readers. But what if we want to do the opposite?

Sometimes, a DOM node serves some sort of cosmetic purpose, but we don't want its content to be accessible for folks using screen readers. We occasionally need to tell screen readers to ignore some markup.

For example: later in the course, we'll learn how to create  [rising link effect](https://courses.joshwcomeau.com/css-for-js/09-little-big-details/08.04-exercises#rising-nav-link):

































































