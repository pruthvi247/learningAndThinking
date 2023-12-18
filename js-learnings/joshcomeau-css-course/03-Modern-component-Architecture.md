# styled-components 101

Shortly, we'll run through some exercises to help us get comfortable writing CSS in this way. First, though, I wanted to dig into some of the ideas we covered in the introduction, and explore a couple more concepts.

Here's a “Hello World” example:
```js
const Button = styled.button`
font-size: 32px;
`;
```
This library uses an obscure JavaScript feature called [tagged template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates). `styled.button` is a function, and it gets passed a template string as an argument. This is syntactic sugar?, and we'll see in a bit why it's so useful.
styled-components _also_ uses a Sass-like preprocessor behind the scenes called [stylis](https://stylis.js.org/). It automatically adds vendor prefixes for maximum browser compatibility. It also allows us to use the ampersand character (`&`) to reference the soon-to-be-created class, like so:
```js
const Button = styled.button`
  display: flex;
  &:hover {
    color: red;
  }
`;
```
Here's the CSS that will be produced:
```css
.abc123 {
  /* Vendor prefixes for legacy browsers: */
  display: -webkit-box;
  display: -webkit-flex;
  display: -ms-flexbox;
  display: flex;
}
/* Plucks out the `hover` pseudo-class:  */
.abc123:hover {
  color: red;
}
```
Note that _component names don't have to be globally unique_ — pretty much every React component I write has a `Wrapper` styled component in it. When styled-components generates the class, it picks a unique hash every time, even for components with the same name.

The `&` character can be thought of as a placeholder: it will be replaced by a class name, once that class is generated. This allows us to use additional selectors, like `&:hover` or `&:first-of-type`. It allows us to use the full power of CSS even though we aren't _typically_ specifying a selector.

**Coming to CSS!(info)**
This handy operator has been available in CSS preprocessors for years, but it's finally been included in the CSS specification under [CSS Nesting](https://www.w3.org/TR/css-nesting-1/).

We're still a long way from being able to use it in browsers; as of early 2023, Chrome is the [only browser to support it](https://caniuse.com/css-nesting). But hopefully soon, we won't need to rely on preprocessors for this sort of thing!

One last thing: the `styled` object has methods for **every HTML tag** (at least, the ones typically used within the `<body>`). Examples will frequently use `styled.div`, but it's important to point out that there is also `styled.a`, `styled.cite`, `styled.canvas`, `styled.marquee`, and so on. Semantic HTML is really important, and we need to be especially mindful of it when using styled-components!

## A worked example

Let's build a component from scratch using styled-components!
Video : https://player.vimeo.com/video/500538371

In the video, I mention a [CSS Tricks article](https://css-tricks.com/quoting-in-html-quotations-citations-and-blockquotes/) about semantic structure for quotes. It's worth a read if you're interested in refining your semantic-HTML chops!

Here's the source code we wind up with in this video:

https://github.com/pruthvi247/character-creator/blob/main/src/01-rough/stylecomponentarch.js
## CSS prop

styled-components comes with an alternative writing method: the `css` prop:
```css
const Title = ({ id, children }) => {
  return (
    <h1
      id={id}
      css={`
        font-size: 2rem;
        font-weight: bold;
    `}
    >
      {children}
    </h1>
  )
};
```
This method is similar in appearance to inline styles, but it's full-fat CSS — the same bag of tricks is available, including using pseudoclasses and media queries, things that aren't possible with inline styles. It's a bit closer to utility-first frameworks like Tailwind.

I personally don't love this style of writing CSS — it bloats the JSX and feels messy to me. But ultimately, it's a subjective, aesthetic choice. We still reap all the same benefits around specificity and scoping. So if you prefer this style, go for it!

[Read more about the `css` prop](https://styled-components.com/docs/api#css-prop) on the styled-components docs.

_Note that the `css` prop requires a Babel plugin, and as such, it won't work in the playgrounds on this course platform._
## Continue learning

If you're interested in learning more about how styled-components works, I wrote a blog post called [[03-styled-components|Demystifying Styled-component]]

If you've been using styled-components for a while and still feel like you don't quite understand what it's doing, this post will help you understand the magic, to increase your confidence with the tool.

## Babel plusgin

To make life easier, the styled-components team also released a Babel plugin which picks semantically-meaningful class names in development (the behaviour doesn't change in production, for performance reasons).
Class names will be structured in the following format: `Filename_componentName-hash`. So if the HTML is `<header class="ShoeIndex__Header-sc-123">`, you can look for the `const Header` inside `ShoeIndex.js`.

If you have access to your project's build tool (eg. Webpack), the plugin can be installed alongside other Babel plugins.

If you use [Create React App](https://github.com/facebook/create-react-app), the build configuration is hidden unless you eject. The styled-components team has you covered, though: you can use the Babel plugin _without ejecting_ with this one weird trick.

First, install the plugin as a dev dependency:
`npm install --save-dev babel-plugin-styled-components`
In your React application, change all imports to match the following:
```
// From this:
import styled from 'styled-components';

// ...to this:
import styled from 'styled-components/macro'
```
By importing from the macro, you get the benefits of the Babel plugin without needing to eject, or fuss with the build configuration.

This works because Create React App supports [Babel macros](https://github.com/kentcdodds/babel-plugin-macros). Other boilerplates/starters might not support it, so this trick may not work by default.
## Editor integrations

styled-components works by using tagged template literals. By default, this means that your styles will be treated like any other string: a solid, lifeless color:
Fortunately, editor integrations exist! This means that you can have proper CSS syntax highlighting even when using styled-components:
It isn't just syntax-highlighting, either: you also get proper auto-complete, and all the other niceties of working in a modern editor:

I personally use VS Code (and can wholeheartedly recommend [the official `vscode-styled-components` plugin](https://marketplace.visualstudio.com/items?itemName=styled-components.vscode-styled-components)!), but integrations exist for most popular IDEs. For the most up-to-date list, check out [the official list of resources](https://styled-components.com/docs/tooling#syntax-highlighting).

We learned that styled-components runs _in-browser_, and generates the classes on-the-fly.

styled-components has **server-side rendering support**, which means the initial HTML/CSS is generated beforehand. My blog uses Next.js, which means I can go 1 step further, and do all this work when I build the site.

In a way, this makes it like Sass — I can pre-compile all of the HTML and CSS before I even deploy the site! It's even more powerful, though, because it _also_ runs in the browser. I can do dynamic stuff that wouldn't otherwise be possible.

Learning how to integrate styled-components into your SSR(Server side rendering) process is beyond the scope of this course, but here are some links to help you get set up:

- [styled-components and Gatsby](https://www.gatsbyjs.com/docs/how-to/styling/styled-components/)
- [styled-components and Next.js](https://medium.com/swlh/server-side-rendering-styled-components-with-nextjs-1db1353e915e)
- [Official styled-components SSR documentation](https://styled-components.com/docs/advanced#server-side-rendering)
# Global Styles

With styled-components, the styles we write are indelibly bound to the elements created. In a component-driven framework like React, this is exactly what you want, most of the time.

But what about global styles? Things like CSS resets, and some baseline styles for native HTML elements?

styled-components has a specific API for creating global styles:
```js
// GlobalStyles.js
import { createGlobalStyle } from 'styled-components';

const GlobalStyles = createGlobalStyle`
  *, *::before, *::after {
    box-sizing: border-box;
  }

  html {
    font-size: 1.125rem;
  }

  body {
    background-color: hsl(0deg 0% 95%);
  }
`;

export default GlobalStyles;
```
This API is remarkably similar to the `styled` helpers we've seen so far: it's called using a tagged template literal, and it returns a component we can render in our app:
```js
// App.js
import GlobalStyles from '../GlobalStyles';

function App() {
  return (
    <Wrapper>
      <Router>
        {/* An entire app here! */}
      </Router>

      <GlobalStyles />
    </Wrapper>
  )
}

export default App;
```
When the `GlobalStyles` component is rendered, it will inject all of its CSS into the `<head>` of the document, applying those styles.

It doesn't really matter where you render this component; there is no significant advantage to putting it above or below the rest of your app's content. I normally include it in my top-level `App` component, so that I know it's _always_ being rendered, and I put it below the rest of the JSX in that component so that it's out of the way.
## Global style patterns

Let's talk about when and how to take advantage of global styles!
Video: https://player.vimeo.com/video/500582701

**Updated: my global styles(success)**

You can see the baseline set of global styles I personally use in new projects over in the Treasure Trove:

- [My Global Styles](https://courses.joshwcomeau.com/css-for-js/treasure-trove/010-global-styles) - josh blog
- same blog in obsidian- [[04-Global-Styles]]
# Dynamic Styles

One of the great things about using a tool like styled-components is that it allows us to dynamically alter our styles based on our application state. In this lesson, we'll look at some options for how to manage dynamic styles with styled-components.
video : https://player.vimeo.com/video/501289983

**Correction:** In the video, I use the term “back ticks” when I meant “dashes”, to describe the characters at the start of CSS variables (`--hover-color`). Sorry for the confusion!

In this video, we saw 3 different approaches for managing dynamic styles. They're summarized below:
## Inline styles
```css
const Button = ({ color, onClick, children }) => {
  return (
    <Wrapper onClick={onClick} style={{ color }}>
      {children}
    </Wrapper>
  );
}

const Wrapper = styled.button`
  color: black;
  padding: 16px 24px;
`;
```
Inline styles are quick and easy to add, but they carry two significant disadvantages:

1. They make it harder to understand what's going on by "splitting up" where the CSS definitions live
2. They aren't compatible with media queries, pseudo-classes, and any CSS that isn't straight-up property/value.
### Camel-case properties

When setting properties in JavaScript, we use “camelCase” versions of property names:
```css
<a
  style={{
    // Instead of `border-radius`:
    borderRadius: '8px',
    // Instead of `text-decoration`:
    textDecoration: 'none',
    // Instead of '-webkit-font-smoothing':
    WebkitFontSmoothing: 'antialiased',
  }}
>
  Hello
</a>
```
**This isn't React-specific!** This is how styles are written and read in vanilla JavaScript as well:
```css
const anchor = document.querySelector('a');
console.log(anchor.style.borderRadius); // 8px;
anchor.style.borderRadius = '16px';
console.log(anchor.style.borderRadius); // 16px;
```
## Interpolation functions

The official styled-components way of managing dynamic styles is to use [interpolation functions](https://styled-components.com/docs/basics#adapting-based-on-props):
```css
const Button = ({ color, onClick, children }) => {
  return (
    <Wrapper onClick={onClick} color={color}>
      {children}
    </Wrapper>
  );
}

const Wrapper = styled.button`
  color: ${props => props.color};
  padding: 16px 24px;
`;
```
This API leverages tagged template literals. If you're curious about how this all works, MDN has some [great documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates) on the subject.
## CSS Variables

Finally, we can solve this problem using CSS Variables (AKA CSS Custom Properties):
```css
const Button = ({ color, onClick, children }) => {
  return (
    <Wrapper onClick={onClick} style={{ '--color': color }}>
      {children}
    </Wrapper>
  );
}

const Wrapper = styled.button`
  color: var(--color);
  padding: 16px 24px;
`;
```
CSS Variables are really pretty neat, and we'll learn more about them later on in the course.

This method offers a great developer experience — it's quick and easy to add new styles, it feels lower-friction than using styled-components interpolations.

That said, they're a bit less flexible; they can only be used to provide property values, which can be limiting when it comes to media queries.

One important note I neglected to mention in the video: [CSS Variables aren't supported in Internet Explorer](https://caniuse.com/css-variables). If you need to support IE, you should use styled-components interpolations instead.

## Media queries

We haven't touched on media queries in styled-components yet! We'll learn much more about them in future modules, but here's a quick example for those curious:
```css
const Wrapper = styled.button`
  color: black;

  @media (min-width: 1200px) {
    color: red;
  }
`
```
Note that you _don't_ need to nest the selector within the `@media` tag, the way you do with vanilla CSS. This is done to make life easier for us.
# Exercises (pt. 2)

Now that we've covered global styles and interpolations, let's get some more practice!

These exercises take the same form as the last set: convert some vanilla-CSS snippets to use styled-components exclusively.
## Framed art

_Note_: You'll need to use [`createGlobalStyle`](https://styled-components.com/docs/api#createglobalstyle) in this exercise. This method has been imported for you, at the top of the `/App.js` file.
### Fragrments
If you're not familiar with fragments, and you'd like to learn a bit of React, you can read on:
Here's the deal. We can't return multiple top-level elements in React. It produces a syntax error:
```css
function App() {
  // 🚫 Syntax error:
  return (
    <p>Hello</p>
    <p>World</p>
  )
}
```
This isn't really a React limitation, it's a JavaScript one! It's equivalent to us trying to do something like this:
```css
function someFunction() {
  // 🚫 Syntax error:
  return (
    "hello"
    "world"
  )
}
```
In the old days, we would solve this by wrapping our React elements in a `<div>`:
```js
function App() {
  // ✅ Problem solved!
  return (
    <div>
      <p>Hello</p>
      <p>World</p>
    </div>
  )
}
```
This works, but it's a bit of a bummer that we're polluting the DOM with an extra `<div>`, just to make React/JavaScript happy!

Fragments are a solution to this problem. They allow us to return multiple elements _without_ adding anything else to the DOM:
```js
function App() {
  return (
    <>
      <p>Hello</p>
      <p>World</p>
    </>
  )
}
```
Fragments are handy, and if you're a React developer, they're definitely a tool you should keep in your back pocket. You can learn more about fragments in the [official docs](https://react.dev/reference/react/Fragment).

I'm sorry for any confusion! I probably should've mentioned this earlier.

video solution for exercise: https://player.vimeo.com/video/501289326
# Component Libraries

Over the past few years, it's become increasingly common for larger organizations to build a _component library_.

A component library is a collection of generic, reusable components that can be dropped in to multiple applications. It's a way to ensure consistency between products, and it can help boost new development speed, since you have a suite of drop-in primitives and don't have to build everything from scratch.

There are many open-source component libraries out there. For example, the [Material component library](https://material.angular.io/) for Angular:
In this module, we're going to explore this concept in depth, and learn how to build our own mini component library!

**This module is for you!(success)**
Some of you might be thinking: “I'm not looking to build a massive open-source component library! I just want to improve my CSS to build small web apps. Will this module help me with that goal?”

The answer is a resounding **yes!** The methodology used by large corporations to structure their component libraries can benefit every single React/Angular/Vue/Svelte app out there. By thinking of the components we write in these terms, we produce better applications.

This doesn't mean that you need to spin up an entirely separate project, or open-source anything. The lessons in this module are applicable even if your “component library” is a half-dozen components sitting inside your side-project application.
## Design systems and design tokens

Over the past few years, component-driven frameworks like React have grown to be massively popular within the front-end web scene. A similar transformation has been happening in the design world.

A design system is essentially the "designer version" of a component library. Instead of a suite of React components, though, a design system is made up of a suite of vector graphics produced in tools like Figma or Sketch or Adobe Illustrator.

In many organizations, the two are linked; the design team has a design system with components like Button and Modal and Combobox, and the development team has a component library with those same elements. Designers combine their design components into mockups, and we can map those components neatly to our component library.

Design systems also consist of _design tokens_. A lot of systems will specify scales for sizes or colors, and a design token is a value in that scale.

We saw this in an earlier workshop. Rather than allow all possible font sizes under the sun, we might limit it to a smaller subset:

- 0.75rem
- 0.875rem
- 1rem
- 1.25rem
- 1.5rem
- 2.5rem

## CSS as a specialty

Using a preexisting component library
video : https://player.vimeo.com/video/501294086

Library suggestions :
- https://reach.tech/

**Update:** Reach UI, the library we saw in this video, is no longer being actively maintained. Fortunately, there are plenty of other options for us to choose from!

Here are my current recommendations:
- [Radix Primitives](https://www.radix-ui.com/)
- [Headless UI](https://headlessui.com/)
- [Ariakit](https://ariakit.org/)
- [React Aria](https://react-spectrum.adobe.com/react-aria/)

I share more information about these tools [in the Treasure Trove](https://courses.joshwcomeau.com/css-for-js/treasure-trove/012-component-libraries).

# Breadcrumbs

Alright, enough theory: let's build some components!

We'll start with a `Breadcrumbs` component. Breadcrumbs are the helpful navigation links you often find near the top of e-commerce listing pages. They show the hierarchy of the content's structure, and let you quickly hop up to the parent or grandparent category page.

**For this lesson, you have a choice:**
- You can treat this as an exercise, and attempt to solve it on your own. Or,
- You can watch the video to see how I'd go about it.

Here's the video, where I walk through how to build this component:
Video : https://player.vimeo.com/video/501527994
## Composition

Before we start working on our `Button` component, we should talk about one more trick in the styled-components bag: **composition**.

If we need multiple variants of a component, we can choose one component to serve as the base for another. For example:
```css
import styled from 'styled-components';

export default function App() {
  return (
    <PrimaryButton>Button</PrimaryButton>
  );
}

const Base = styled.button`
  font-size: 21px;
`;

const PrimaryButton = styled(Base)`
  background: blue;
  color: white;
`;
```
If you inspect that element in the devtools, you'll notice that it's applying _both_ styles:
```css
<button class="iaGSPX coOzpk">Button</button>

<style>
  /* Base */
  .iaGSPX {
    font-size: 21px;
  }

  /* PrimaryButton: */
  .coOzpk {
    background: #00f;
    color: #fff;
  }
</style>
```
(In the devtools, you should also see some additional classes that start with `sc-`. We can ignore those. They're added as labels, designed to be transformed by the [babel plugin](https://courses.joshwcomeau.com/css-for-js/03-components/04-setup) for improved debugging.)

This kind of composition is common in the CSS world, but styled-components handles a lot of the messier details for us, like ordering our class names so that conflicts are solved correctly.

Exercise:
Video : https://player.vimeo.com/video/501960758

You can access my final code on [CodeSandbox](https://codesandbox.io/s/jwc-button-exercise-solution-4dbpw?file=/src/Button.js).

**Correction:** Towards the end of the video, I reduce the vertical padding by 4px on each side, when it should only be reduced by 2px on each side. This has been fixed in the [solution](https://codesandbox.io/s/jwc-button-exercise-solution-4dbpw?file=/src/Button.js).

# Dynamic tags

In this lesson, we'll see how to use the polymorphic `as` prop to dynamically change the tag that styled-components renders.
Video : https://player.vimeo.com/video/501960442

Here's our solution, from the video:
```js
import styled from 'styled-components';
function Button({ href, children }) {
  return (
    <Wrapper href={href} as={href ? 'a' : 'button'}>
      {children}
    </Wrapper>
  );
}
const Wrapper = styled.button`
  background: blue;
  color: white;
  border: none;
  padding: 16px 24px;
  border-radius: 4px;
`;
const App = () => (
  <Button href="/">Hello</Button>
);
export default App;
```

In plain css , above code can be thought of as 
````xml
<a href="/"><button type="Hello"></button></a>
````
Learn more by reading the [styled-components documentation](https://styled-components.com/docs/api#as-polymorphic-prop).
# Escape Hatches

So far, we've been operating under the assumption that our components are 100% well-suited for every situation that requires them. Unfortunately, things aren't usually so neat and tidy.

No matter how much preparation we do, we will always discover additional needs once we start using the component in our application. Sometimes, it's a matter of updating the standard to include an additional tweakable parameter. Other times, a special situation will call for special one-off handling.

In this lesson, we'll look at a few common scenarios to see which approach makes the most sense. We'll also learn how to build escape hatches into our components, to allow for specialized tweaks.
## A new variant

Let's imagine that we're working on a brand new feature: users can delete their accounts from our app.

We add a confirmation prompt, and realize that our button is missing something:

We really want this button to be red, to emphasize the gravity of this action… but our component only comes in a standard blue color.
There are many ways we could handle this situation, and to determine which path makes the most sense, I like to ask a question: is this tweak something we'll plausibly need to do again?

We can't predict the future, but we can make educated guesses. In this case, I imagine that we may want to add additional destructive actions to our application!

In fact, it's quite common for component libraries to include color variants for different statuses:
- “info” is usually a calm blue
- ”success” is usually green
- “alert” is usually orange or yellow
- “danger” is usually red
Adding all 4 at this point would be overkill, but I would update our component to take a new `mood` prop:
```js
<Button
mood="danger" // 'default' or 'danger'
/>
```
We've codified this behaviour so that it's there when we need it next time. It's important that we're always refining our components, to make sure they match the needs of our team!

That said, **each added prop carries a significant and exponential cost in terms of complexity**. We don't want to add new props whenever a new customization is needed! Let's look at some other options.

## Composition

Let's imagine another scenario: the marketing team is building a "spooky" landing page for Halloween, and they want to be able to create an orange button with a different font:
![[Pasted image 20231216141122.png]]
How might you allow for this new styling?

One approach could be to add a new `mood`, `spooky`. I don't love this idea, though, for a few reasons:

1. It adds significant complexity to our code: this new mood would tweak background color, text color, and font family.
2. This Halloween landing page sounds like a one-off, and not something we'll need to use again and again.
3. It doesn't really scale. What happens when the marketing team decides they want a “Christmas” mood, with animated cand
Instead, I prefer to use composition. Here's how I'd do it:
```js
/* components/SpookyButton.js */
import Button from './Button';

const SpookyButton = styled(Button)`
  font-family: 'Spooky Halloween Font';
  background-color: orange;
  color: black;
`;
export default SpookyButton
```
We build a one-off component that _composes_ our base Button component.

But hold on—The `Button` component we're importing isn't a styled-component, it's a custom component we created ourselves! Can we compose _custom components too_?

We can, though it does require a change:
```js
const Button = ({ variant, size, children, className }) => {
  const styles = SIZES[size];

  let Component;
  if (variant === "fill") {
    Component = FillButton;
  } else if (variant === "outline") {
    Component = OutlineButton;
  } else if (variant === "ghost") {
    Component = GhostButton;
  } else {
    throw new Error(`Unrecognized Button variant: ${variant}`);
  }

  return (
    <Component style={styles} className={className}>
      {children}
    </Component>
  );
};
```
The difference: we added a `className` prop to our component, and passed it along to the rendered `<Component>`.

To understand why this works, let's consider what happens when we try to _use_ our new `SpookyButton` component:
```js
function HalloweenPage() {
  return (
    <SpookyButton variant="fill">
      Sign up… if you dare!
    </SpookyButton>
  );
}
```
`SpookyButton` is a styled-component, so it will extract the declarations into a class, append that class to the `<head>`, and _apply that class to the element_.

`<Button>` will be given the class name that styled-components generates, and it will be added to the rendered `<Component>`. Our final markup will look like this:
```html
<button class="base-abc123 fill-def456 spooky-ghi789">
  Sign up… if you dare!
</button>
```
styled-components will apply the classes in order, so that the “spooky” styles will _overwrite_ the “fill” button styles, which in turn overwrite the “base” styles.

This is a really powerful idea, but like everything, there are tradeoffs. The downside is that it _does_ spread our styles around a bit.

The good news is that there are no mysteries. When we look at `SpookyButton`'s definition, we see that it builds upon the `Button` styles, so we have a trail of breadcrumbs we can follow to see all of the styles. But it's additional friction.

That said, it's way better than the alternative in this case: We could keep them all in 1 place, but then that place would be _really cluttered_. A typical large app will have too many one-off button styles to fit comfortably in 1 place; it's better to spread it out a little bit, so that one-off buttons can be viewed in isolation (and a developer trying to understand the common case isn't burdened with all the exceptions!)
## Escape hatches

Essentially what we've done, by forwarding `className`, is we've given ourselves an escape hatch.

Escape hatches are tools that allow us to break free of the constraints that normally serve us well. For example, React will automatically sanitize all children, but if you want to apply direct HTML, you can do so with this escape hatch:
```js
<div
  dangerouslySetInnerHTML={{
    __html: 'First &middot; Second'
  }}
/>;
```
You might look at that and say "huh, that seems unnecessarily complicated".

The same result could be accomplished with a lower-friction API:
The React team _intentionally adds friction_ because they want it to be clear that this is an escape hatch to be used in exceptional circumstances, not something you should reach for every day.

I like to follow a similar motto when it comes to building reusable components: **it should be easy to follow the convention, and hard (but possible!) to break free of it**.

Earlier, when we added a `mood` prop, we decided that it should be a part of the API, and we made it _very easy_ to change the background color:
```
<Button mood="danger">Confirm</Button>
```
For one-off components, though, the developer will need to go through a higher-friction process:
```js
import Button from './Button';

const SpookyButton = styled(Button)`
  font-family: 'Spooky Halloween Font';
  background-color: orange;
  color: black;
`;

export default SpookyButton
```
This will encourage us to use conventions when possible, but it gives us an escape hatch we can use to create special variants. In my opinion, it's the perfect level of flexibility.

Some folks disagree. They say that the point of a component library is to enforce a consistent style, and by incorporating an escape hatch, it becomes possible to change _any_ CSS. It's too much power.

My rebuttal is that the world is messy, and we will need to break with convention sometimes. Designs call for exceptions. If the component can't flex, we'll need to build a new one from scratch. And the end result will be an even-less-consistent user interface.

This framework — easy to follow the convention, possible to break free of it — has served me really well over the years.
# Single Source of Styles
Video : https://player.vimeo.com/video/501886722
In this video, we look at a challenging problem involving “contextual styles”. How do we allow components to take on different styles in different contexts _without_ "reaching in" and styling other elements?

Our goal is to update the code below so that `TextLink` has black, underlined text when it's inside the `Quote` component. When it's rendered outside the `Quote` component, it should be blue, and not have an underline.

It's important to stress: **we haven't learned how to do this yet.** I want to give you the chance to think about this problem, to see _why_ it's tricky. I don't expect you to be able to solve it yet, however.

Here's the playground. Spend a few minutes working on this problem, then watch the video to see how to solve it.
```js
import styled from 'styled-components';

const Quote = ({ by, source, children }) => {
  return (
    <figure>
      <QuoteContent>{children}</QuoteContent>
      <figcaption>
        <Author>
          <SourceLink href={source}>{by}</SourceLink>
        </Author>
      </figcaption>
    </figure>
  );
};

/*
  We want this TextLink to be black
  and underlined when it's inside
  a Quote component.
*/
const TextLink = styled.a`
  color: blue;
  text-decoration: none;
`;

const QuoteContent = styled.blockquote`
  margin: 0;
  background: hsl(0deg 0% 90%);
  padding: 16px 20px;
  border-radius: 8px;
  font-style: italic;

  &::before {
    content: '“';
  }
  &::after {
    content: '”';
  }
`;

/* You can safely ignore everything below this point! It doesn't need to change */
const Author = styled.cite`
  display: block;
  text-align: right;
  margin-top: 8px;
`;

const SourceLink = styled.a`
  text-decoration: none;
  color: hsl(0deg 0% 35%);

  &::before {
    content: '—';
  }
`;

const App = () => (
  <>
    <Quote by="Unknown" source="/">
      This quote <TextLink href="/">contains a link</TextLink>!
    </Quote>
    <p>
      This paragraph <TextLink href="/">contains a link</TextLink>!
    </p>
  </>
);

export default App;
```
As a hint: [“Referring to other components”](https://styled-components.com/docs/advanced#referring-to-other-components) in the docs will help!
## Working through the problem
Video : https://player.vimeo.com/video/501887123

Our solution applies TextLink styles when `TextLink` is found within `QuoteContent`:
```js
const TextLink = styled.a`
  /* Standard styles: */
  color: blue;
  text-decoration: none;

  /* Styles when rendered inside a quote: */
  ${QuoteContent} & {
    color: black;
    text-decoration: revert;
  }
`;
```
I call this approach **“Inversion of control nesting”**. It's the opposite from how many developers think about nesting, where we always start from the parent:


```js
const QuoteContent = styled.blockquote`
  margin: 0;
  background: hsl(0deg 0% 90%);
  padding: 16px 20px;
  border-radius: 8px;
  
// Standard nesting.
// **DON'T do this**  font-style: italic;

  ${TextLink}{
  color: deeppink;
  text-decoration: revert;
  }

  &::before {
    content: '“';
  }
  &::after {
    content: '”';
  }
`;
```
With this approach, we avoid "reaching in" and setting TextLink styles from within another component. As a bonus, it colocates all relevant TextLink styles in the same place.

Another huge bonus: _we aren't relying on our own memory_.

Imagine if we had solved this using a `variant` prop instead:

# In Summary

One of the hardest parts of working with styles in modern component-based applications is dealing with all the variations. Unfortunately, a single `Button` component might have _lots_ of different presentations depending on the context.

In this module, we've seen a lot of ways to add or tweak styles, and it may not be clear which to use when. Let's review the methods we've seen, and consider when they come in handy.

## Core options through props

When we created our `Button` component, we added props for `variant` and `size`. For example:
```js
<Button
variant="ghost"
size="small"
>
Click me
</Button>
```
Most of the reusable components we create will take a small number of props for their "core" options. These options will map to specific styles that get applied within the component.

## Composition with styled()

It's important not to add _too many_ core options. It would be hard to use (not to mention maintain!) a component that worked like this:

```js
<Button
  fontFamily="Spooky"
  buttonSize="small"
  textSize="small"
  backgroundColor="orange"
  color="black"
  cornerRadius="small"
  hoverEffect="grow"
  focusStyles="default"
  disappearOnClick={true}
  isPartOfAGroup={false}
>
  Click me
</Button>
```
As our application grows, we'll wind up with lots of "one-off" requirements, like our `SpookyButton` from earlier. We can solve for these problems using composition:
```js
/* components/SpookyButton.js */
import Button from './Button';

const SpookyButton = styled(Button)`
  font-family: 'Spooky Halloween Font';
  background-color: orange;
  color: black;
`;

export default SpookyButton
```
How do we decide whether a property is a "core option" or a "one-off variant"? Admittedly, sometimes the line can be a little blurry. Use your best judgment, and remember that you can always change your mind later! If the `Button` component starts to feel too overwhelming, with too many options, consider extracting a couple composed variants to lighten the mental load.

The goal should be to have props for every-day common use cases, and one-offs for niche, specialized situations.

## Contextual styles

Sometimes, we want to apply a style only when it's within another component, or in a specific situation.

In these cases, it's less about picking the right prop for a job, and more about _changing the defaults_.

We saw this in the last lesson. It's a technique I call "Inversion of control nesting":
```js
const ButtonBase = styled.button`
/* Standard styles omitted */

${ButtonGroup} & {
border-radius: 0px;
}
`;
```
This technique is useful when we want a change to be "implicit". It saves the developer (us) from having to remember to use a specific variant prop in a specific situation.

There is a bit of a blurry line here, though. Could we not say that `SpookyButton` is a contextual style, to be used whenever `Button` is inside `HalloweenPage`?
```js
// Button.js
import { Wrapper as HalloweenWrapper } from '../HalloweenPage';

const ButtonBase = styled.button`
  /* Standard styles omitted */

${HalloweenWrapper} & {
    font-family: 'Spooky Halloween Font';
    background-color: orange;
    color: black;
  }
`;
```
This accomplishes the exact same goal, but the tradeoffs are different:

- **Pro:** I can see these styles in the same spot as my other Button styles, letting me know that this variant exists.
- **Pro:** Makes the contextual styles "automatic". Developers don't need to remember to use `SpookyButton`, it happens automatically.
- **Con:** Bloats our JavaScript bundle. Because we need to import `HalloweenPage`, it means that any page that uses a Button also has to download all of the markup and code for the halloween page, even if it's the middle of February!
- **Con:** Having access to _all possible_ contextual styles in 1 place can be overwhelming. Adds a lot of noise.
For super-niche styles like `HalloweenPage`, I think the cons outweigh the pros. We don't want to bloat our bundle _or_ our style definition by adding all possible one-off variants.

By reserving this trick for common, every-day situations, we increase its power, since we're more likely to _pay attention_ to them. If there are 30 contextual styles defined in 1 place, we'll probably just ignore them, since it's too much mental overhead to go through each of them.
### Removing the JS bloat(info)

The "inversion of control nesting" idea requires that we import the parent component. I know this makes a lot of JavaScript developers nervous, since it seems like it could inflate our JS bundle sizes!

In my experience, it hasn't really been a problem. I reserve this trick for "low-level" components like `TextLink` and `Quote`. These components tend to be small, and really widely-used. This means that we aren't pulling in _that_ many unnecessary components, and when we do, they tend to be quite tiny.

That said, there _is_ an alternative approach that avoids the import. **I don't recommend it** for most use cases, since it has its own tradeoffs, but it can be a worthwhile trick on _very_ large or performance-sensitive applications, for advanced users.
The alternative is to use data-attributes as selectors:
```js
// ButtonGroup.js
const ButtonGroup = styled.div.attrs({
  'data-id': 'ButtonGroup'
})`
  padding: 16px;
  border: 1px solid;
`;
```
```js
// Button.js
const Button = styled.button`
  border-radius: 16px;

  [data-id=ButtonGroup] & {
    border-radius: 0px;
  }
`;
```
We haven't seen [the “attrs” API](https://styled-components.com/docs/api#attrs), but it's a way to associate specific HTML attributes with the element. This means that whenever we render a `<ButtonGroup>`, we'll wind up with `<div className="abc123" data-id="ButtonGroup">`.

**Here's my problem with this approach:** A developer might change the `data-id` inside `ButtonGroup.js` and not realize that they've accidentally broken the styles in `Button.js`! There's an implicit dependency between these two files.

With the “inversion of control” technique, this relationship is explicit. `Button.js` would import `ButtonGroup`. It's a much harder link to accidentally break (if someone deletes `ButtonGroup.js`, we'll even get a build error, because the import will fail!).

For this reason, I don't recommend this approach for most use cases, but wanted to include it for advanced users looking to optimize very-large applications.
## The right tool for the job

styled-components provides many different tools, and developing an intuition for which to use when is the work of many years. Hopefully this summary has helped set you on the right track, but ultimately this is the kind of thing that comes with practice. Don't worry if you don't feel like you have a handle on it yet!

For those who aren't using styled-components outside of this course, spend a few moments considering how these alternatives relate to your tool of choice. How might you simulate each of these alternatives in your current stack, to achieve similar tradeoffs?

Taking it back to where we started, our goal is to understand which styles affect which elements, and ultimately, the ideas in this module are all in service of that goal.
# Workshop: Mini Component Library
In this workshop, we build our own component library!
## Your mission

Our component library consists of 3 components:
- Progress bar
- select input(drop down)
- text input
These components might seem simple, but building robust, accessible versions of these components isn't so simple.

Access starter files
You can access the Figma design here:

“Mini Component Library” on Figma
And here's the starter code:

github.com/css-for-js/mini-component-library
codesandbox.io/p/sandbox/mini-component-library-l79u06 (Experimental)
The CodeSandbox URL is “experimental” because this workshop uses Storybook, a tool for component testing that typically needs to run on a local machine. CodeSandbox has recently begun to support these types of applications, and it seems to work great (just give it a few minutes to boot up)!

## A polarizing workshop

I've heard feedback from some students that this workshop is particularly stressful / frustrating. In particular, the second exercise (`<Select>`) requires some out-of-the-box thinking, and possibly some googling / experimentation. It feels unfair.

At the same time, other students have reached out to tell me that they _loved_ this workshop, precisely because it challenged them, and helped them build their problem-solving skills.

CSS is a _huge_ language, and there's no way that I can possibly cover every challenge, property, or UI component in this course. Instead, I want to help you build the skills needed to be able to solve challenging problems on your own!

All of that said, I don't want you to feel frustrated. If you reach the point where you're not having fun with this one, I've added a hint to the [solution page](https://courses.joshwcomeau.com/css-for-js/03-components/19-workshop-select) that should offer just enough guidance to get you unstuck.

You can also take a “hybrid approach”. Spend a few minutes hacking on the problem, then watch a few minutes of the solution videos. Bounce between working and watching until you finish the workshop.

As always, **this is your course.** You can choose your own adventure. The most important thing is that you get value from this course. If you're not having fun, you're not likely to finish the course, and that's the worst outcome of all.

solution code : https://github.com/css-for-js/mini-component-library/tree/solution/src/components
## Native vs. custom

HTML comes with a `<progress>` element. In some cases, you may wish to use that element rather than build something custom from scratch.

[Progress elements can be styled](https://css-tricks.com/html5-progress-element/), but only on Chrome and Safari. Even then, support for animations is limited, and there are likely many designs that will not be possible using native `<progress>`.

If we choose to build our own element, as we do in this workshop, we need to make sure our alternative is just as usable and accessible as the native element. [This MDN doc](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/progressbar_role) explains how to use this role correctly.

## Trimmed corners

We can use wrapping elements to trim corners of all children with `overflow: hidden`.
```js
const Trimmer = styled.div`
  border-radius: 16px;
  overflow: hidden;
`;
```

This is useful in our ProgressBar because it allows us to round the edges of the `<Bar />` element in exactly the right way, as it approaches 100%.

## Concentric circles

When we nest elements that use `border-radius`, we need to tweak the outer element to be _more curved_ than the inner one.

We discuss this strategy in depth [in Module 9](https://courses.joshwcomeau.com/css-for-js/09-little-big-details/02-radius).

## Alternative approaches

Several students have suggested using a linear-gradient to create the progress-bar aesthetic. This removes the need for `BarWrapper`, since we don't have to trim the corners of a child element.

There are two reasons I've opted not to use that approach here:

1. If we wanted to animate this progress bar, the transform-based solution will be more fluid and performant.
2. Creating a sharp edge with a gradient is a bit tricky, and it's beyond what we've seen in the course so far. We'll learn more about this approach in [Module 9](https://courses.joshwcomeau.com/css-for-js/09-little-big-details/05.01-linear-gradients).

Those caveats aside, it's totally valid to use gradients to create a progress bar! If you've gone with this approach, you don't have to change anything. 💯

### Select/Drop down
An important correction(warning)
In the video, I left out a pretty important declaration:

const NativeSelect = styled.select`
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  appearance: none;
`;
In Safari, < select > tags have a default height, one which can't be overridden with the height property. The appearance property removes this restriction.

If not using a CSS preprocessor, you may wish to use -webkit-appearance instead of appearance. The appearance property is supported in Safari 15.4+, but there's still lots of folks on older versions of Safari.
Some important highlights from this video:

The sweet spot
Generally, developers pick one of two strategies when it comes to styling the ``< select >`` element / creating a single-select input:

Take the native ``< select >`` element and style it, acknowledging that certain things (eg. the icon) can't be customized and will vary by platform
Build it entirely from scratch, a daunting challenge when considering mobile devices and accessibility
For inputs like ``< select >`` and`` <input type="file">``, a third option exists: we can keep the native input, but set it to be invisible. We can create whatever presentation we want, and when the user clicks the form control, the real input will become activated, preserving the great cross-platform, accessible UX that these elements bring.

The adjacent sibling combinator
CSS offers a method to style elements based on their siblings: the adjacent sibling combinator.

This allows us to style our presentational element when the real element is focused:

const NativeSelect = styled.select`
```
  /* styles */
`;

const PresentationalBit = styled.div`
  ${NativeSelect}:focus + & {
    outline: 1px dotted #212121;
    outline: 5px auto -webkit-focus-ring-color;
  }

  ${NativeSelect}:hover + & {
    color: ${COLORS.black};
  }
`;
```
Note that we still follow the same best practices when it comes to keeping a single source of styles; all of the styles that affect PresentationalBit are still stored within the relevant styled element.

There is also the general sibling combinator (~), which works much the same way but doesn't require elements be directly adjacent.

(Lastly, the order matters: div ~ p will only affect p tags coming after div tags.)

Restyling the native select(info)
Several students have written in, saying they found a way to achieve the design without hiding the native ``<select>.``

By applying appearance: none, the default chevron is stripped away. We can then include our own ``<Icon>`` component, and make it absolutely-positioned to sit in front of the ``<select>.``

This approach works, but there are some gotchas to be aware of:

Because the ``<Icon>`` is sitting in front of the ``<select>``, it has the potential to block clicks, if the user happens to click right where the icon is. We can fix this by applying pointer-events: none. We'll learn more about this property in Module 9.
Because the ``<select>`` is being used for layout calculations, it will stretch based on the length of the longest option (rather than dynamically resizing based on the currently-selected option). This isn't necessarily a problem, but it's something to be aware of.
appearance has pretty good browser support, though it's missing Internet Explorer. If you're not using a preprocessor, you'll want to include the -webkit-appearance property as well, to pull the browser support from ~88% to ~98%.
But yeah, this is an absolutely valid solution to the problem!
### Icon input
**One small correction:** In the end, we use straight-up pixels for the font size and height, and this is a mistake! We should have kept using rems. This is corrected in the solution:

[View the solution code on Github](https://github.com/css-for-js/mini-component-library/blob/solution/src/components/IconInput/IconInput.js)

## Styling placeholder text

We can use the `placeholder` pseudo-element to tweak the styles of our placeholder text:
```
const TextInput = styled.input`
  /* other styles omitted */

  &::placeholder {
    font-weight: 400;
    color: ${COLORS.gray500};
  }
`;
```
## Alternative: Using composition

Something we didn't look at in the video is an alternative solution which uses **composition** instead. Here's what that alternative would look like, omitting the parts that don't need to change:
```js
const IconInput = ({
  label,
  icon,
  width = 250,
  size,
  ...delegated
}) => {
  const iconSize = size === 'small' ? 16 : 24;
  const Input = size === 'small'
    ? SmallInput
    : LargeInput;

  return (
    <Wrapper>
      <IconWrapper style={{ '--size': iconSize + 'px' }}>
        <Icon id={icon} size={iconSize} />
      </IconWrapper>
      <Input
        {...delegated}
        style={{
          '--width': width + 'px',
        }}
      />
    </Wrapper>
  );
};


const TextInput = styled.input`
  width: var(--width);
  border: none;
  color: inherit;
  font-weight: 700;
  outline-offset: 2px;

  &::placeholder {
    font-weight: 400;
    color: ${COLORS.gray500};
  }
`;

const SmallInput = styled(TextInput)`
  height: 24px;
  font-size: ${14 / 16}rem;
  border-bottom: 1px solid ${COLORS.black};
  padding-left: 24px;
`;

const LargeInput = styled(TextInput)`
  height: 36px;
  font-size: ${18 / 16}rem;
  border-bottom: 2px solid ${COLORS.black};
  padding-left: 36px;
`;
```
In general, composition approaches like this work best when there are many variants and many differences between each variant; it can be hard to follow the logic otherwise. In this case, however, I think both approaches are equally valid.








































































