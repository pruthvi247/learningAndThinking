[source](https://courses.joshwcomeau.com/css-for-js/04-flexbox/01-hello-world)
There is also full article from josh in [developer_quest](https://github.com/pruthvi247/developer_quest/blob/dev/notes/UI-Blogs/css-blogs/josh-comeau-interactive-flexbox.md)

Video : https://player.vimeo.com/video/505370212
Here's a look at the CSS produced in this video:
```css
.wrapper {
  display: flex;
  flex-direction: row; /* row, column */
  justify-content: flex-start; /* flex-end, space-between… */
  align-items: stretch; /* flex-end, baseline… */
}
```

Responsive navigation menu:
video : https://player.vimeo.com/video/505369580
Solution: 
```css
<style>
  ul {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  a {
    display: block;
    padding: 8px;
  }

  @media (min-width: 300px) {
    ul {
      flex-direction: row;
      justify-content: space-evenly;
    }
  }
</style>
```
# Alignment Tricks

Flexbox gives us a couple pretty neat tricks when it comes to alignment. Let's learn a couple.

## Baseline alignment

A common UI pattern involves having the site's logo right before the primary navigation:
```css
<style>
.logo {
  font-size: 32px;
  font-weight: bold;
}

/* Resetting list and link styles */
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

a {
  color: inherit;
  text-decoration: none;
}
  ul {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
  }
</style>

<nav>
  <ul>
    <li>
      <div class="logo">Tom's</div>
    </li>
    <li>
      <a href="">Home</a>
    </li>
    <li>
      <a href="">Browse</a>
    </li>
  </ul>
</nav>
```
In this example, we've vertically aligned the items to `center`, but it doesn't quite look right, does it?
![[Pasted image 20231216200723.png]]

The trouble is that `align-items: center` isn't what we want in this case. Instead, we want to make sure the bottoms of each character are aligned, as they would be if they were written on a page.

This can be done with `align-items: baseline`:
Remarkably, this “just works” even if there are multiple DOM levels. It even works with specialized HTML elements like inputs and buttons. Here's a more complex example:
```css
<style>
  form {
    display: flex;
    align-items: baseline;
    justify-content: center;
  }
  strong {
  font-size: 1.5rem;
  margin-right: 8px;
}
input {
  font-size: 1rem;
  padding: 4px;
  border: none;
  border-bottom: 2px solid black;
}
</style>

<form>
  <label for="email">
    <div>
      <strong>
        Email:
      </strong>
    </div>
  </label>
  <input type="email" id="email" value="test@hello.com" />
</form>
```
**Watch out for Safari!(warning)**

It's almost a philosophical question: if a text input doesn't have any text in it, where should its baseline be drawn?

Most browsers will keep the baseline consistent, regardless of whether a text input has any text (or a placeholder) in it. But Safari marches to the beat of its own drummer.
Here's an example of a text input with a label, aligned using `align-items: baseline`:
![[Pasted image 20231216200946.png]]
Check out what happens, though, if that text input is empty:
![[Pasted image 20231216201002.png]]
[This is a bug in Safari](https://bugs.webkit.org/show_bug.cgi?id=142968). Unfortunately, there hasn't been a lot of movement in terms of getting it fixed.

**How do we work around this?** We can use placeholders! It's good practice for most inputs to have placeholder text anyway:
```css
<input
  type="email"
  placeholder="jane.smith@gmail.com"
/>
```
If you're not familiar, placeholders are an HTML feature that allow us to provide an example of the sort of input we expect. They help users quickly understand what's being asked of them.

(Many developers use placeholders incorrectly; they are _not_ meant to label the input! That's what `<label>` is for.)

What if placeholder text isn't suitable for the input in question? We can pass a single whitespace character to work around the Safari bug:
```html
<input
  type="text"
  placeholder=" "
/>
```
Alternatively, we can also use `align-items: center`. This will only work if our label and input fonts are the same size, but in general, it's good to keep the sizing consistent anyway. Use font-weight or color to add contrast between them, if desired.
### Centered AND baseline?

Here's an interesting thought experiment: What if we wanted to _combine_ `baseline` and `center` alignment, so that the tallest item would be vertically centered, and then all siblings would be aligned to its baseline?
![[Pasted image 20231216201215.png]]
Spend a couple minutes giving it a shot. Treat it as an open-ended exercise (there is no "right answer").

Video : https://player.vimeo.com/video/506532110
```css
<style>
  nav {
    height: 100px;
    outline: 2px solid;
    display: flex;
    flex-direction: column;
    justify-content: center;
    
  }
  ul {
    display: flex;
    justify-content: space-evenly;
    align-items: baseline;
  }
</style>

<nav>
  <ul>
    <li>
      <div class="logo">Tommy's</div>
    </li>
    <li>
      <a href="">Home</a>
    </li>
    <li>
      <a href="">Browse</a>
    </li>
  </ul>
</nav>
```
## Align self

So far, we've been aligning all children in a group. But what if we want specific children to have specific alignments?

Flexbox gives us the `align-self` property to manage this situation!

Here's an example. Notice that the first item sticks to the start of the container, while all other children are centered:
```css
<style>
  section {
    display: flex;
    flex-direction: column;
    /* Set all children to be center-aligned */
    align-items: center;
  }
  
  a:first-of-type {
    /* Override that default alignment */
    align-self: flex-start;
  }
  /* Resetting list and link styles */
a {
  color: inherit;
  text-decoration: none;
  padding: 16px;
}
</style>

<section>
  <a href="">← Go back</a>
  <a href="">View account</a>
  <a href="">Make a transfer</a>
  <a href="">Request a loan</a>
</section>
```
### What about justify-self?

`align-self` allows us to pick specific alignment options for each individual item along the cross (secondary) axis. But what about the primary axis?

Unfortunately, `justify-self` doesn't exist in Flexbox. And if you think about it, it kinda makes sense that it wouldn't! In fact, _it's good that it doesn't exist_.

We can solve for primary-axis positioning using other properties we'll discover, like `flex-grow`, `flex-shrink`, `flex-basis`, and `order`. These properties offer _much_ more flexibility than `justify-self` would!

We'll learn all about these properties in the lessons ahead.
## Exercises
### Conversation
Let's build an iMessage-style chat interface!
```css
<style>
  /* Default / cosmetic styles */
  html,
  body {
    height: 100%;
  }

  ol {
    min-height: 100%;
    list-style-type: none;
    margin: 0;
    padding: 0;
  }

  .message {
    display: block;
    padding: 16px;
    margin: 8px;
    border-radius: 6px;
    width: -moz-fit-content;
    width: fit-content;
    max-width: 70%;
  }

  .message.sent {
    background: hsl(240deg 100% 47%);
    color: white;
  }

  .message.received {
    background: hsl(0deg 0% 90%);
    color: black;
  }

  ol {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
  }

  .message.sent {
    align-self: flex-end;
  }
</style>

<ol>
  <li class="message sent">
    Can you get me a big salad?
  </li>
  <li class="message received">
    What big salad? I'm going to the coffee shop.
  </li>
  <li class="message sent">
    They have big salads.
  </li>
  <li class="message received">
    I've never seen a big salad.
  </li>
  <li class="message sent">
    They have a big salad.
  </li>
  <li class="message received">
    Is that what I ask for?
  </li>
  <li class="message received">
    The <em>BIG</em> salad?
  </li>
</ol>
```
To make this implementation production-ready, we'd also want to add some JavaScript that automatically scrolls down when the page loads / on new messages, since newer messages are appended to the end, and they might be out of the viewport if there's a larger message history. This is beyond the scope of this exercise.
# Growing and Shrinking
video : https://player.vimeo.com/video/506531531
## Takeaways 
#ImportantPoint 

- There are two important sizes when dealing with Flexbox: the _minimum content size_, and the _hypothetical size_.
- The minimum content size is the smallest an item can get without its contents overflowing.
- Setting `width` in a flex row (or `height` in a flex column) sets the _hypothetical_ size. It isn't a guarantee, it's a suggestion.
- `flex-basis` has the same effect as `width` in a flex row (`height` in a column). You can use them interchangeably, but `flex-basis` will win if there's a conflict.
- `flex-grow` will allow a child to consume any excess space in the container. It has no effect if there isn't any excess space.
- `flex-shrink` will pick which item to consume space from, if the container is too small. It has no effect if there _is_ any excess space.
- `flex-shrink` can't shrink an item below its minimum content size.

This is _a lot_ of takeaways, so don't feel bad if it's hard to remember them all! Feel free to revisit this video as-needed to get a refresher.

**Correction:** There is one more difference between `width` and `flex-basis`: `flex-basis` can't scale an element below its minimum content size, but `width` can. Consider this example:
```css
<style>
  .row {
    display: flex;
  }
  p {
    /* Try changing this to 'width': */
    flex-basis: 20px;
    width: 20px;
    border: 2px solid hotpink;
  }
</style>

<div class="row">
  <p>The word “enormousness” is itself an enormous word.</p>
</div>
```
Both `width` and `flex-basis` will change the _hypothetical_ size of an element, but `width` can set that value below the minimum content size. `flex-basis` can't.
## Ratios

When we use `flex-grow` and `flex-shrink`, we use unitless values like `1` or `10`. What do these numbers signify?
They represent _a ratio of the available space_.

Let's say we have the following markup:
```css
<style>
  .row {
    display: flex;
  }

  nav, aside {
    flex-grow: 1;
  }

  main {
    flex-grow: 3;
  }
</style>

<div class="row">
  <nav></nav>
  <main></main>
  <aside></aside>
</div>
```
We want the `main` element to consume _3 times_ as much space as `nav` or `aside`. It gets 3 "units" of space, whereas `nav` and `aside` only get 1 unit.

To find out the actual percentage, add all the numbers together. In this example, there are 5 units total (1 + 3 + 1). That means that `nav` and `aside` each get 20% of the total space (1 / 5), whereas `main` gets 60% (3 / 5).

Similarly, `flex-shrink` is also based on the ratios between elements.An element with `flex-shrink: 3` will shrink 3x faster than an element with `flex-shrink: 1` (though `flex-shrink` also takes the element's size into consideration).

## Exercises
### Sidebar

Let's build a common web layout: A main content area with a navigation sidebar.
example video : https://courses.joshwcomeau.com/cfj-mats/flex-grow-ex1-demo.mp4
We want to _prioritize the main content area_ by keeping it as large as possible once the viewport shrinks.
```css
<style>
  section {
    display:flex;
  }
  nav {
    width: 220px;
    flex-shrink:3;
  }

  nav, main {
    padding: 16px;
    border: 2px solid;
  }
  main{
    flex-grow:3;
  }
</style>

<section>
  <nav>
    <h2>Navigation</h2>
    <ul>
      <li>Home</li>
      <li>Shop</li>
      <li>Contact</li>
    </ul>
  </nav>
  <main>
    <h1>Welcome to ThingStore</h1>
    <p>
      Please enjoy your time shopping!
    </p>
  </main>
</section>
```
### Alert

Let's suppose we're building an `Alert` component for our component library:
Everything looks great when the element has some breathing room, but things take a turn when there isn't enough space for the heading:
![[Pasted image 20231216210153.png]]
Specifically, there are two issues we want to fix:

1. The icon gets squashed, becoming an oval.   
2. The icon gets center-aligned instead of sticking near the top.

Update the code so that it appears like this on smaller sizes:
```js
import styled from 'styled-components';
import { Check } from 'react-feather';

function Alert({ children }) {
  return (
    <Wrapper>
      <IconWrapper>
        <Check />
      </IconWrapper>
      <Heading>{children}</Heading>
    </Wrapper>
  );
}

const Wrapper = styled.div`
  display: flex;
  align-items: center;
  box-shadow: 0px 2px 20px hsl(0deg 0% 0% / 0.35);
  border-radius: 4px;
  padding: 8px;
`;

const IconWrapper = styled.div`
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: forestgreen;
  color: white;
  border-radius: 50%;
  margin-right: 8px
  // solution
  flex-shrink:0;
  align-self: flex-start;
`;

const Heading = styled.div`
  flex-grow: 1;
`;

const App = () => (
  <Alert>
    Thanks for participating in our survey!
  </Alert>
);

export default App;
```
solution video: https://player.vimeo.com/video/506532713

**An alternative solution(success)**

Instead of setting `flex-shrink: 0`, we can also solve this problem by changing `width` to `min-width`:
```js
const IconWrapper = styled.div`
  min-width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  background: forestgreen;
  color: white;
  border-radius: 50%;
  margin-right: 8px;
`;
```
This solves the problem, and for many developers it feels more intuitive / simpler, but I'd actually argue that **it's a _less_ direct way of solving the problem.**

Our icon gets squashed thanks to the Flexbox shrinking algorithm, and we want to prevent that behaviour. Setting `flex-shrink: 0` essentially says "Hey, I don't want this fella to shrink!".

**I think there's a risk here of confusing “simple” for “familiar”.** When I was first getting acquainted with `flex-shrink`, I had already had _years_ of experience using `min-width`, and so it seemed to me like `flex-shrink: 0` was an over-engineered solution. But as I've gotten more comfortable with the Flexbox algorithm, it actually feels _more_ straightforward to me to use flex-shrink in this situation.

I'd say once you reach the point where both approaches feel intuitive, you should use whichever you prefer. They both work, after all! But _if_ the `flex-shrink` approach feels more complicated, I'd encourage you to keep practicing with it, and build that muscle!

# The “flex” Shorthand
Video: https://player.vimeo.com/video/506592631
#ImportantPoint 
## Takeaways

- `flex` takes 3 individual values:
    
    - `flex-grow`, as a unitless value (eg. `1`)
    - `flex-shrink`, as a unitless value (eg. `5`)
    - `flex-basis`, as a length unit (eg. `200px`)
- By default, `flex-grow` will distribute any _extra_ space that isn't taken up by the elements.
- `flex: 1` will assign `flex-grow: 1`, but it will _also_ set `flex-basis: 0`. It won't affect the default value for `flex-shrink`, which is `1`.
- Since `flex-basis` is a synonym for `width` in a flex row, we're effectively shrinking each child to have a “hypothetical width” of 0px, and then distributing all of the space between each child.
That last takeaway is summarized handily by this graphic, courtesy of the W3C:
![[Pasted image 20231216211539.png]]

Exercise video solution: https://player.vimeo.com/video/658794396
# Constraints

We've seen how properties like `flex-grow`, `flex-shrink`, and `flex-basis` can be used to control the _proportions_ between siblings in a flex container.

What if we want to set hard limits, though, rather than ratios?

Fortunately, a familiar set of properties can help us out here: `min-width`/`max-width` and `min-height`/`max-height`.

In a flex row, `flex-basis` works just like `width`, and it _also_ respects the constraints set by `min-width` and `max-width`.

For example: say we have three children with their own ratios, but we want to clamp each one to a minimum width of 75px. Try resizing this playground to see the effect:
```css
<style>
  .wrapper{
    display: flex;
  }
  .biggie {
    flex: 2;
    min-width: 75px;
  }
  .tiny {
    flex: 1;
    min-width: 75px;
  }
</style>

<section class="wrapper">
  <div class="biggie"></div>
  <div class="tiny"></div>
  <div class="tiny"></div>
</section>
```
We're effectively changing the “minimum content size” to be a hardcoded value, rather than relying on the size of the element's children.

We can also use `max-width` to clamp an element's growth! And, in a column, `min-height` and `max-height` work the same way.
### Sidebar layout

Time for another content + sidebar layout, but this time, with different constraints!
Here are the rules:

- Items should be horizontally centered
- The nav should be 1/3rd of the total space, but no more than 150px
- The main content should max out at 500px
```css
<style>
  .wrapper {
    display: flex;
    justify-content:center;
  }
  nav {
    /* TODO */
    max-width:150px;
    flex:1;
  }
  main {
    /* TODO */
    flex:2;
    max-width:500px;
    
  }
</style>
<div class="wrapper">
  <nav></nav>
  <main></main>
</div>
```
### Facebook-style layout

On their desktop application, Facebook has a 3-column layout. I've added some borders so we can see how the columns flex (as well as a blur, to protect the anonymity of my Facebook friends!):
It's a 3 column layout, and below a certain threshold, the left-hand navigation disappears. It's interesting how things scale, though!

See if you can recreate this effect in the playground below. The media query that hides the sidebar has already been applied.

For our version of it, the nav and sidebar should be the **same size**, and should range between 150px and 250px.

demo video : https://courses.joshwcomeau.com/cfj-mats/facebook-scale.mp4

**More than meets the eye(warning)**

At first glance, this might not seem like a particularly challenging problem, but the devil is in the details.

Specifically, watch what happens towards the end of the video, right after the left-hand sidebar disappears. Pay careful attention to how the two remaining columns resize as the viewport shrinks. **You can scrub through the video** to get a precise look.

Honestly, this is a _surprisingly_ complex exercise, involving some out-of-the-box thinking with `flex-shrink` and minimum content sizes. It's intended to be a terrific challenge, and I think it's super valuable even if you can't solve it (_especially_ if you can't solve it, actually).

In the solution video, we'll dig deep into how this works.

Solution video : https://player.vimeo.com/video/510430411
```css
<style>
  .wrapper {
  display: flex;
}
nav, aside.contacts {
  min-width: 150px;
  max-width: 250px;
  flex-shrink: 9999999;
  flex-basis: 250px;
}
main {
  flex: 1;
  flex-basis: 500px;
}
  @media (max-width: 700px) {
    nav {
      display: none;
    }
  }
</style>
<div class="wrapper">
  <nav></nav>
  <main></main>
  <aside class="contacts"></aside>
</div>
```
It's more common to use the `flex` shorthand, likely because it's what the specification recommends. Here's what that looks like:
```css
.wrapper {
  display: flex;
}
nav, aside.contacts {
  min-width: 150px;
  max-width: 250px;
  flex: 0 999999 250px;
}
main {
  flex: 1 1 500px;
}
```
**Is “max-width” really necessary?(info)**

Several students have asked: Do we really need to specify `max-width: 250px` on the two sidebars? The solution seems to work without it!

It actually does make sense that it wouldn't be necessary in this case: we're setting its hypothetical size (via `flex-basis`) to 250px, and we haven't told it to grow (no `flex-grow`), so it doesn't have any reason to get bigger than 250px!

In other words, we're constraining it (with `max-width`), but it isn't trying to push past that limit anyway!

That said, in a real app, I'd probably add the `max-width` anyway. There may be some edge-cases where it can make a difference (eg. depending on the content within these columns), and a little redundancy never hurt!

# Shorthand Gotchas

There is a _really common_ gotcha when it comes to using the `flex` shorthand. I've been bitten by it countless times.

Let's explore in this video: https://player.vimeo.com/video/510430173
#ImportantPoint 
	**To summarize**: when we use the `flex` shorthand, we set `flex-basis` to `0`, and _this value will override any `width` you set_. In other words, `width` has no effect in this snippet (when used inside a `flex-direction: row` container). `Flexbasis` wins over `width`, when we use shorthand we are also setting `flexbasis` thats why if we interchange `flexbasis` with `width` it breaks the layout
```css
.item {
flex: 1;
width: 200px;
}
```
To prevent this unwanted surprise, we should instead use `flex-basis`. And if you need to set either `flex-grow` or `flex-shrink`, you should use the shorthand:
```css
.item {
flex: 1 1 200px;
}
```
# Wrapping

In Module 1, we saw how `inline` elements in Flow layout have a super-power: [they can line-wrap](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/09-flow-layout#inline-elements-can-line-wrap). Like a sushi roll getting chopped into pieces, inline elements can be broken up to spread over multiple lines.

In Flexbox, a similar concept exists, via the `flex-wrap` property.

Let's learn more about how it works:
Video : https://player.vimeo.com/video/510429840
Here's the final result from the video:
```css
<style>
article {
  margin: 8px;
  border-radius: 16px;
  box-shadow: 0px 2px 24px hsl(0deg 0% 0% / 0.2);
}
article img {
  border-radius: 12px 12px 0px 0px;
}
article section {
  padding: 8px 16px 16px;
}
article h2 {
  margin-bottom: 8px;
}
article p {
  font-weight: 300;
}
  main {
    display: flex;
    flex-wrap: wrap;
  }
  article {
    flex: 1 1 150px;
    max-width: 250px;
  }
  article img {
    width: 100%;
  }
</style>

<main>
  <article>
    <img src="https://courses.joshwcomeau.com/cfj-mats/dog-one-300px.jpg" />
    <section>
      <h2>The One Weird Trick to get tasty dinner scraps</h2>
      <p>Step one: Find the friendliest human at the dinner table. Step two: Give them sad pupper eyes. Step 3: Get slid human food on the sly.</p>
    </section>
  </article>
  <article>
    <img src="https://courses.joshwcomeau.com/cfj-mats/dog-two-300px.jpg"
    />
    <section>
      <h2>How to show them you mean business</h2>
      <p>Every dog park has their own scene. Different cliques. If you want to make a name for yourself, you'll need to make a good first impression…</p>
    </section>
  </article>
  <article>
    <img src="https://courses.joshwcomeau.com/cfj-mats/dog-three-300px.jpg" />
    <section>
      <h2>Life in the outdoors</h2>
      <p>We purchased and tested the 10 best outdoors accessories so you don't have to. Here's what we found…</p>
    </section>
  </article>
</main>
```
## Content vs. items
Video: https://player.vimeo.com/video/510448773
The `align-content` property is a sub-property of the [Flexible Box Layout module](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

It helps to align a flex container’s lines within it when there is extra space in the cross-axis, similar to how `justify-content` aligns individual items within the main-axis.

#ImportantPoint 
_Note, this property has no effect when the flexbox has only a single line._

**Two dimensions(info)**
Before this lesson, all of the examples we've seen have existed in a single dimension. `flex-wrap` allows us to dip our toes into two-dimensional layouts.
Ultimately, however, we aren't going to go _too_ deep into this. The reason is that CSS Grid offers a more compelling story for two-dimensional layouts.
CSS Grid is well-supported in all major browsers, but not in Internet Explorer. If you still need to support IE, I'd suggest having a reasonable fallback for that browser (eg. instead of placing things in a grid, stack elements in a large column). Supporting a browser does _not_ mean that the experience has to be 100% identical.

### Deconstructed Pancake

Here's a layout I bet you've seen on marketing pages before:

Demo video : https://courses.joshwcomeau.com/cfj-mats/deconstructed-pancake-demo.mp4

Now we could solve this with media queries, but I'd rather solve it using Flexbox. We should be able to use flex-wrap to reconstruct this effect!

Give it a shot:
```css
<style>
  main {
    display: flex;
    flex-wrap:wrap;
    justifiy-content: center;

  }
  article {
    flex:0 1 150px;
  }
</style>

<main>
  <article></article>
  <article></article>
  <article></article>
</main>
```
This layout is known as the [“Deconstructed pancake”](https://web.dev/one-line-layouts/#02.-the-deconstructed-pancake:-flex:-lessgrowgreater-lessshrinkgreater-lessbasewidthgreater).
# Groups and Gaps
Video : https://player.vimeo.com/video/510858833
```js
import styled from 'styled-components';

function Header() {
  return (
    <Wrapper>
      <Logo>My Thing</Logo>
      <AuthButton>Log in</AuthButton>
      <AuthButton>Sign up</AuthButton>
    </Wrapper>
  );
}

const Wrapper = styled.header`
  display: flex;
  gap: 8px;
`;

const Logo = styled.a`
  font-size: 1.5rem;
  margin-right: auto;
`;

const AuthButton = styled.button``

export default Header;
```
## Exercises

### Superheader

A lot of e-commerce sites feature a "superheader" — a header that sits above the main site header, advertising deals or providing secondary navigation.
![[Pasted image 20231217103711.png]]

In this exercise, we'll create our own version of that:
![[Pasted image 20231217103800.png]]
The search input and language toggle should be right-aligned, with the "Free shipping" text staying on the left. This should be done entirely through CSS, no markup changes.
```css
<style>
  /* TODO */
  header{
    display:flex;
    gap:8px;
    /* justify-content: space-between; */
  }
  label{
    margin-left:auto;
    display:flex;
  }
</style>

<header>
  Free shipping over $50!
  <label>
    <span class="visually-hidden">
      Search
    </span>
    <input
      type="text"
      placeholder="Search…"
    />
  </label>
  <button>
    <span class="visually-hidden">
      Current language:
    </span>
    English
  </button>
</header>
```
### Photo viewer

Alright, let's build something more complex.

In this exercise, we'll build a "photo viewer". A vertical strip of photos shows the available options, and a larger photo displays the current selection.

It should scale with the viewport size, as shown:

Demo video : https://courses.joshwcomeau.com/cfj-mats/media-gallery-exercise-v2.mp4
**NOTE:** We're focusing exclusively on the styles. The functionality of selecting photos is not included.

#ImportantPoint 
Solution video : https://player.vimeo.com/video/
Starter code : https://courses.joshwcomeau.com/css-for-js/04-flexbox/09-gaps
# Ordering

By default, Flexbox arranges its items based on their DOM order, the same way things work in Flow layout. But in Flexbox, we are given overrides to tweak that order.

There are several ways to accomplish this, but we'll focus primarily on `flex-direction`.
## Flipping flex-direction

We've seen how Flexbox has a `flex-direction` property: we use it to control whether our container's primary axis is vertical or horizontal.

There are two other values we can use as well:
- `row-reverse`
- `column-reverse`
As you might expect, this property flips the order so that they stack from last to first:
This works by swapping `flex-start` and `flex-end`; when working in English, a Flex row typically starts on the left and ends on the right. `flex-direction: row-reverse` flips this on its head.
#ImportantPoint 
This _does_ have a surprising side-effect: things will appear right-aligned instead of left-aligned. This is because we aren't just changing the order of the _elements_, we're changing the _direction of the axis_. A reversed row starts on the right, and ends on the left (in a left-to-right language like English).

If we want to flip the order of children without changing their alignment, we can do so with `justify-content`:
```css
.row {
flex-direction: row-reverse;
justify-content: flex-end;
}
```
**Visual order only!(warning)**

When we flip the order of flex children, it's important to know that we're only changing things cosmetically.

For users who navigate with the keyboard and/or use a screen reader, they'll still be going through items in the order laid out in the DOM / written in your HTML. `row-reverse` and `column-reverse` don't change anything for them.

This can actually be a boon, as we'll see shortly. But it's worth keeping in mind, to make sure we don't accidentally make things worse for them.
## Other mechanisms

There are two other mechanisms we can use to control order:

- The `order` property, on individual children
- `flex-wrap: wrap-reverse`

`order` works similar to `z-index` — a child with `order: 2` will show up after a child with `order: 1`, but before a child with `order: 5`.

`flex-wrap: wrap-reverse` causes elements to wrap upwards rather than downwards.

In a world without CSS Grid, these methods would be worth exploring. Honestly, though, CSS Grid is a better tool for the job when we have complex ordering requirements. For that reason, we won't be looking at `order` or `flex-wrap: wrap-reverse` in this course.
## Exercises
### Table of contents

It's common for blog posts and online magazine articles to feature an index of the contents, with convenient links to hop to specific sections:

Solution video : https://player.vimeo.com/video/513160445

one of the solution is to use `tab-index``tabindex` can be applied to any element - although it is not necessarily useful on every element - and takes a range of integer values. Using `tabindex`, you can specify an explicit order for focusable page elements, insert an otherwise unfocusable element into the tab order, and remove elements from the tab order. For example:
```
<input tabindex="3">
<input tabindex="0">
<input tabindex="-1">
<input>     
<input tabindex="2">
<input tabindex="1">
<span tabindex="4"> This wouldn't normally receive focus</span>
```
#ImportantPoint 
We should use tab index when we don't want tab to focus on element
`tabindex="-1"`: Removes an element from the natural tab order, but the element can still be focused by calling its `focus()` method
Any tabindex greater than 0 jumps the element to the front of the natural tab order. If there are multiple elements with a tabindex greater than 0, the tab order starts from the lowest value that is greater than zero and works its way up. Using a tabindex greater than 0 is considered an **anti-pattern**.

Setting `flex-direction: row-reverse;` is another solution
```css
.wrapper {
    display: flex;
    flex-direction: row-reverse;
  }
```

# Flexbox Interactions

So far, we've been discussing Flexbox on its own. Let's take a look at how Flexbox interacts with other properties and layout modes.
## Positioned flex children

What do you suppose happens when a flex child is given absolute or fixed positioning?
```css
<style>
  .row {
    display: flex;
  }

  .help-btn {
    flex: 1;
    position: fixed;
    right: 0;
    bottom: 0;
  }
  .help-btn {
  background: gold;
  padding: 16px;
}
main {
  background: pink;
}
</style>

<section class="row">
  <main>
    <!-- Stuff here -->
  </main>
  <div class="help-btn"></div>
</section>
```
We've put our `.help-btn` element in a bit of a bind, by asking it to participate in the flex layout (with `flex: 1`), but also giving it positioned layout (with `position: fixed`).

When there is a conflict between layout modes, **positioned layout always wins.** Our help button will become fixed to the bottom-right corner of the viewport, and the `.row` Flex container will ignore it, and act as though it only has one child (`<main>`).
#ImportantPoint 
As a general rule, elements can't participate in multiple layout modes at once. Either it's using flexbox, or it's using positioned layout. This is ultimately a very good thing, because CSS would be much more complicated if this wasn't true!
#ImportantPoint 
**What about relative positioning?(info)**

An exception to this rule is relative positioning, but it's kind of a special case.

When you give something relative positioning, you're instructing it to move based on its normal position. That normal position is "inherited" from whichever layout mode it happens to be rendered by.

If you give a flex child relative positioning, that element is technically being rendered in two different layout modes, but they're compatible; the element is first laid out inside the flex container, and then transposed using top/left/right/bottom by positioned layout.

Similarly, sticky positioning can also work in a flex container, though there is a bit of a "gotcha" there. We'll see it in the next lesson!
## Margin collapse

#ImportantPoint 
In Module 1, we learned about [margin collapse](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/11-margin-collapse-intro). When two block-level elements are adjacent or nested, their margins can overlap, or be absorbed.

_Margin collapse is exclusive to Flow layout._ It doesn't happen when elements are laid out inside a flexbox parent.

As the "original" layout mode of the web, Flow is built around documents, and margin collapse makes a lot of sense when documents are concerned. But when we're building layouts for dynamic web applications, collapsing margins don't make as much sense.

Here's a demo. Try changing `.column`'s "display" property to "block", and watch what happens with the margins!
```css
<style>
  .column {
    display: flex;
    flex-direction: column
  }
  p {
    margin: 16px;
  }
</style>

<section class="column">
  <p>This is a paragraph.</p>
  <p>Because it's in a flex column, its margins won't collapse.</p>
  <p>This is a good thing, but it can be confusing.</p>
</section>
```
## Flexbox and z-index

Here's a bit of a riddle for you: can you tell why `z-index` appears to work in this example?
```css
<style>
  .wrapper {
    display: flex;
  }
  .first {
    z-index: 2;
    width: 100px;
    height: 100px;
    background: slateblue;
  }
  .second {
    /*
      Change z-index to 3, and watch
      the order flip! This happens
      even though these elements are
      not using Positioned layout.
    */
    z-index: 1;
    width: 100px;
    height: 100px;
    background: deeppink;
    margin-left: -25px;
    margin-top: 25px;
  }
</style>
<section class="wrapper">
  <div class="first"></div>
  <div class="second"></div>
</section>
```
It's curious, right? Both `.first` and `.second` are statically positioned. If we rely purely on render order, the pink box should sit above the blue one. And yet, because `.first` has `z-index: 2`, it floats above!
#ImportantPoint 
Earlier, we learned that the `z-index` property is used by the Positioned layout algorithm. It has no effect in Flow layout, which is why we need to add `position: relative` in order to set a `z-index`.

It turns out, however, that the Flexbox algorithm _also supports z-index_. If our element is being laid out with Flexbox, it uses `z-index` as if it was rendered with Positioned layout.

The same thing is true for CSS Grid; a child in Grid layout can use `z-index` without setting `position: relative`.

#ImportantPoint 
Remember, CSS is comprised of layout modes, and each layout mode decides what each property should do. Positioned, Flexbox, and Grid all implement support for z-index. Flow layout does not.

### Combining layout modes

While Flexbox is super powerful, there are certain things it can't do on its own.

Let's say we're trying to build this kind of UI:
Demo video : https://courses.joshwcomeau.com/cfj-mats/flex-absolute-child.mp4

Specifically, it has these constraints:
- Two equal width columns
- The container should be the height of the _first column_.
- The second column should scroll vertically, since it won't fit in the shorter container.
This is a tricky exercise!
solution video : https://player.vimeo.com/video/512674281
```html
<style>
  section {
    display: flex;
    gap: 32px;
    border: 3px solid hotpink;
    /*Solution*/
    overflow: auto
  }

  .col {
    flex: 1;
    padding: 16px;
  }

  /*Solution*/
  .col:first-of-type {
    position: sticky;
    top: 0;
  }

  .col:last-of-type {
    height: 0px;
  }
</style>

<section>
  <div class="col">
    <h1>Growing Column</h1>
    <p>This column will grow very tall indeed, whilst the adjacent one will be clamped to whatever height this one rests
      at!</p>
    <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
      standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a
      type specimen book.</p>
  </div>

  <div class="col">
    <p>Here is a list of all the letters in the English language:</p>
    <ol>
      <li>Item A</li>
      <li>Item B</li>
      <li>Item C</li>
      <li>Item D</li>
      <li>Item E</li>
      <li>Item F</li>
      <li>Item G</li>
      <li>Item H</li>
      <li>Item I</li>
      <li>Item J</li>
      <li>Item K</li>
      <li>Item L</li>
      <li>Item M</li>
      <li>Item N</li>
      <li>Item O</li>
      <li>Item P</li>
      <li>Item Q</li>
      <li>Item R</li>
      <li>Item S</li>
      <li>Item T</li>
      <li>Item U</li>
      <li>Item V</li>
      <li>Item W</li>
      <li>Item X</li>
      <li>Item Y</li>
      <li>Item Z</li>
    </ol>
  </div>
</section>
```
A common alternative solution is to use absolute positioning (Check out [an example from Poissoj](https://stackblitz.com/edit/js-fagkqf?file=index.html) and [another from Guglielmo](https://codepen.io/guglielmodanna/pen/bGqqPbG)).

These solutions work pretty well, but there is one small difference: the cursor has to be positioned over the list for scrolling to work. In the sticky solution, scrolling works anywhere within the pink box.
# Recipes

Now that we've covered all of the theory when it comes to Flexbox, let's see how we can use it in some practical every-day examples!

If you prefer, you can treat these as exercises, and try to complete them before watching the videos. Totally up to you!
## Holy Grail layout

For a long time, the "Holy Grail" layout was simultaneously extremely common, and extremely difficult to implement correctly with the tools of the time (tables and floats).

Fortunately, Flexbox can handle it without any weird hacks!
Here's what we're going for:
Demo video : https://courses.joshwcomeau.com/cfj-mats/holy-grail.mp4

my solution : https://github.com/pruthvi247/huckleberry/blob/main/04-flex-box/05-holly-grail-layout.html

Solution video : https://player.vimeo.com/video/512675025
## Sticky sidebar

It's common for a sidebar to use `position: sticky`, to follow the user as they scroll through an article.

Does this work within a Flex container?
At first glance, it appears not to:
There is a way to make this work, however! Let's explore:
Solution : 
```html
<style>
  body {
    padding: 0;
  }

  * {
    box-sizing: border-box;
  }

  nav,
  main {
    padding: 16px;
    border: solid deeppink;
    /* solution: when we add border, we can see that nav is stretched to the end of page,
    `sticky` works with respect to parent and parent is full page, so we  added allign self */
    align-self: flex-start;
  }

  img {
    display: block;
    width: 300px;
    margin: 16px 0 64px;
  }

  .wrapper {
    display: flex;
  }

  nav {
    position: sticky;
    top: 0;
  }

  /* .box{
    position: sticky;
  } */

  main {
    flex: 1;
  }
</style>

<section class="wrapper">
  <nav class="box">
    <h2>Navigation</h2>
    <ul>
      <li>Section One</li>
      <li>Section Two</li>
    </ul>
  </nav>
  <main class="box">
    <p>This container contains random stuff to increase its height.</p>
    <img src="https://courses.joshwcomeau.com/cfj-mats/cat-300px.jpg" />
    <p>Normally, a blog post would exist in this container.</p>
    <img src="https://courses.joshwcomeau.com/cfj-mats/dog-one-300px.jpg" />
    <p>This container contains random stuff to increase its height.</p>
    <img src="https://courses.joshwcomeau.com/cfj-mats/cat-two-300px.jpg" />
    <p>Normally, a blog post would exist in this container.</p>
    <img src="https://courses.joshwcomeau.com/cfj-mats/dog-two-300px.jpg" />
  </main>
</section>
```
**An alternative approach(info)**

We can also solve this problem by constraining the height of the `<nav>` element:
```css
nav {
  position: sticky;
  top: 0;
  height: fit-content;
}
```
This works because `height` overrides the default “stretch” alignment in Flexbox. The Flexbox can't stretch the `<nav>` to fill the parent container's height anymore. As a result, the `<nav>` element has a bunch of empty space below, and it can stick to the edge of the viewport as the user scrolls.

This is a 100% acceptable solution, though it does feel a bit more complicated to me. Instead of tweaking the Flexbox algorithm to do what we want, we're forcing a conflict between size and alignment.

It reminds me a bit of what I mentioned a couple of lessons ago: [it's easy to mistake familiarity for simplicity](https://courses.joshwcomeau.com/css-for-js/04-flexbox/04-grow-shrink-basis#an-alternative-solution).

Most CSS developers are more comfortable with `height` than with Flexbox cross-axis alignment, and so it _feels_ simpler to tweak `height` and not have to fuss with Flexbox. I would have felt this way, a few years ago.

Ultimately, this is a personal-preference thing, and I'm not suggesting that one approach is better than the other. Some developers might be _very_ comfortable with Flexbox, and yet still prefer the `height` approach. But I want to make sure you're not leaning on familiar CSS properties as a crutch, to avoid developing your Flexbox muscles. ❤️
## Overstuffed and centered

There are many ways to center an item in a container, like this cat image:
What if we want it to stay centered _even if it exceeds its container?_
![[Pasted image 20231217132907.png]]
```html
<style>
body {
  padding: 32px;
}
x
* {
  box-sizing: border-box;
}

.wrapper {
  border: 2px solid;
  margin: 16px auto;
  
  /* align-items:center; */
}
  .wrapper {
    width: 50vw;
    display:flex;
  flex-direction: column;
  }
  img {
    display: block;
    width: 300px;
    margin-top: 16px;
    /*solution  */
    align-self:center;
  }
</style>

<section class="wrapper">
  <p>This is a cat:</p>
  <img src="https://courses.joshwcomeau.com/cfj-mats/cat-300px.jpg" />
</section>
```
usually we sill add`margin:auto` but this will only work when parent container is larger, in this case it will not work, as wrapper is smaller than child

Workshop :
Demo video : https://courses.joshwcomeau.com/cfj-mats/sole-and-ankle-resize.mp4

## Resources

Grab the starter code from Github, or work on CodeSandbox:
- [github.com/css-for-js/sole-and-ankle](https://github.com/css-for-js/sole-and-ankle)
- [codesandbox.io/s/sole-and-ankle-1z4ivh](https://codesandbox.io/s/sole-and-ankle-1z4ivh)
- solution to all exercise : https://github.com/css-for-js/sole-and-ankle/commits/solution

You'll find step-by-step instructions in the workshop's `README.md`.
## Exercise 1: Superheader

_Solution git :_ https://github.com/css-for-js/sole-and-ankle/commit/f6c85f87665d0c23ac91440ade630c9e943e5313
_Solution  Video:_ https://player.vimeo.com/video/509534779

**Height fix(warning)**

In the solution, we set the height of the superheader explicitly:
```css
const Wrapper = styled.div`
  height: 40px;
`;
```
This can cause problems if the user bumps up their default font size. Instead, we should either set `min-height: 40px` (so that it can grow as necessary), or `height: 2.5rem` (so that it scales smoothly with font size).

## Exercise 2: Header
solution video : https://player.vimeo.com/video/509534357
solution git : https://github.com/css-for-js/sole-and-ankle/commit/ad2863febfccdcc58d87e5ad5210b2ebfcd2faf8
#ImportantPoint  Notice that in solution these are different 
`</side>` and `<side />`

Example : https://stackoverflow.com/questions/39184716/what-does-tag-mean-in-xml
```xml
<a>
  <b>
    <c/>
    <d/>
  </b>
</a>
```
`<c/>` and `<d/>` are **[empty element tags](https://www.w3.org/TR/REC-xml/#NT-EmptyElemTag)**:
>Empty-element tags may be used for any element which has no content, whether or not it is declared using the keyword **EMPTY**. [For interoperability](https://www.w3.org/TR/REC-xml/#dt-interop), the empty-element tag should be used, and should only be used, for elements which are declared EMPTY.

## Exercise 3: Shell

Solution video : https://player.vimeo.com/video/509587174
Solution git : https://github.com/css-for-js/sole-and-ankle/commit/396ddc017f2f926db1ea0dfcf1647a2027994a5d

## Exercise 4: Sneaker Grid

This exercise has two distinct parts, so it's split into two distinct videos!
### Part A: Grid layout with Flexbox

Solution video : https://player.vimeo.com/video/509588077
Solution git : https://github.com/css-for-js/sole-and-ankle/commit/e5f47e38409931b45abebfcd660b5ff1dc928a57

**Correction:** At around the 6-minute mark, I mention that the elements sit on one line because of `flex-shrink`. In fact, the reason they compress so much is because `flex: 1` also sets `flex-basis` to `0`.
### Part B: Price and Flag touches
Solution video : https://player.vimeo.com/video/509587596
Solution git : https://github.com/css-for-js/sole-and-ankle/commit/4249d2bbc5bad803ad76524e3cb6fba6dd593427

**Forgotten: border radius!(info)**

So, one thing I totally missed: the design has rounded corners on the shoe images! Sorry about that. 😅

We can fix this by applying the following `border-radius` declaration:
By applying the border-radius directly to the image, we sidestep potential complications (the alternative is to apply it to the `<Wrapper>` and then clip the corners with `overflow: hidden`, but this will also clip our nifty flags!).

