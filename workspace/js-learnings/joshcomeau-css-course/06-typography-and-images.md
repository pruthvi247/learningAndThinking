## Kerning

To the best of my understanding, the reason that the letter placement is slightly different between browsers is that the browsers implement different **kerning algorithms**.
**Custom kerning?(info)**

Over the course of my career, I can think of a few times when designers asked me to tweak the kerning for a particularly important heading.

We can do this with a few steps:

1. Disable the built-in kerning with `font-kerning: none`.
2. Wrap each letter in a span.
3. Shift letters closer/further using `letter-spacing`, picking custom values for each span.
If you're interested in improving your kerning skills, [a super-neat kerning minigame](https://type.method.ac/) can help you practice.
## Text Rasterization

In addition to the role that browsers play, the browser's _operating system_ also affects how typography is rendered.
## Font Smoothing

You may have heard of the `-webkit-font-smoothing` property.

This property allows us to switch which aliasing algorithm the browser uses. But, tragically, it only works on macOS, and only in Chrome/Safari/Edge (not Firefox).
```css
*, *:before, *:after {
  box-sizing: border-box;
  -webkit-font-smoothing: antialiased;
}
```
You may have heard that changing this property is an accessibility risk, because antialiased text is less legible. A widely-shared 2012 article, [“Stop ‘Fixing’ Font Smoothing”](https://usabilitypost.com/2012/11/05/stop-fixing-font-smoothing/), made the case that subpixel-antialiasing was inherently superior, and produced crisper text than the `antialiasing` alternative.

**Just what is “WebKit”, anyway?(info)**

WebKit is a browser rendering engine created by Apple, and used in Safari on macOS, and all mobile browsers on iOS.

Early versions of Chrome and Opera also used WebKit, across all platforms (Windows, macOS, Android). In 2013, Google announced that it was forking WebKit to create its own rendering engine, Blink.

Nowadays, Chrome and Microsoft Edge also use Blink as their rendering engine.

This means that just about every major browser has its roots in the WebKit codebase. This history helps explain why `-webkit` prefixes are supported in many non-Safari browsers!
# Text Overflow

Have you ever thought about how the browser's text placement algorithm works? How does it decide when to line-break?

It turns out, the algorithm is (relatively) straightforward and intuitive. If you've ever had to manually edit a Markdown file to keep each line under 80 characters, you've likely followed a very similar process.

It goes something like this:
demo video : https://courses.joshwcomeau.com/cfj-mats/text-wrapping-algorithm-demo.mp4

The browser groups characters into "words". A word, in this case, is a collection of characters that can't be broken up. “https://www.google.com” is a word. So is “kool_kat_99”.

Words are separated by "breaking characters". The CSS specification refers to them as [soft wrap opportunities](https://www.w3.org/TR/css-text-3/#line-breaking). Each whitespace character is a soft wrap opportunity. So is the dash character (`-`).

When content would spill outside the containing block, the browser looks for the closest soft wrap opportunity, and splits everything afterwards to the next line. This process repeats for all of the text.
**Non-breaking spaces(info)**

Suppose we want to add a space to our paragraph, but in a way that _doesn't_ create a soft wrap opportunity. In other words, a space that can't be used to line-break.

There is a special HTML entity that can be used in this case: `&nbsp;`.
`&nbsp;` is the code for “Non Breaking Space”. A whitespace character that connects the words on either side into a single unbreakable mega-word.
```html
<p>
  That sandwich costs $10&nbsp;USD, or you can barter for it.
</p>
```
Here's a question: what happens if a single word is too long to fit in the container? What if there are no "soft wrap opportunities" present, to keep a word from overflowing?

You've probably been in this frustrating situation before:
```html
<style>
.wrapper {
  border: 2px solid;
  padding: 16px;
}

p:not(:last-of-type) {
  margin-bottom: 1em;
}
</style>
<div class="wrapper">
  <p>
    This is a narrow column of text, with a very long word: antidisestablishmentarianism.
  </p>
  <p>
    The same problem happens with URLs: https://www.somewebsite.com/articles/a1b2c3
  </p>
</div>
```
## Wrapping onto multiple lines

With the `overflow-wrap` property, we can linewrap longer words/strings:
```html
<style>
  p {
    overflow-wrap: break-word;
  }
</style>

<div class="wrapper">
  <p>
    This is a narrow column of text, with a very long word: antidisestablishmentarianism.
  </p>
  <p>
    The same problem happens with URLs: https://www.somewebsite.com/articles/a1b2c3
  </p>
</div>
```
`verflow-wrap: break-word` tweaks the text-placing algorithm. If the browser realizes that it can't fit the current word, _and_ it doesn't have any spare soft wrap opportunities, this declaration gives the browser permission to break after any character.

This property is supported across all browsers. In Internet Explorer, the property is called `word-wrap` instead of `overflow-wrap`, so you'll need to supply both properties if targeting IE.
### Hyphenation

`overflow-wrap: break-word` splits long words across multiple lines without any visual indication that a word has been split.
Adding hyphens is not part of the text-placement algorithm, but we can add it in with the `hyphens` property:
```css
<style>
  p {
    overflow-wrap: break-word;
    hyphens: auto;
    
    /* Prefix for Safari */
    -webkit-hyphens: auto;
  }
</style>

<div class="wrapper">
  <p>
    This is a narrow column of text, with a very long word: antidisestablishmentarianism.
  </p>
</div>
```
For best results, I like to combine `hyphens` with `overflow-wrap`. The hyphens might not always show up, but at least the layout should never break.

In terms of text selection, the hyphens will not be selectable. This is good, since it means line-broken URLs can be copy/pasted properly

**Gotchas(warning)**
`hyphens: auto` only works if the `lang` attribute is set on the `<html>` tag (and it mainly only works in English, though some browsers have added hyphen support for other languages; [see a complete list](https://developer.mozilla.org/en-US/docs/Web/CSS/hyphens#browser_compatibility) on MDN).

Also, `hyphens: auto` varies quite a bit between browsers and devices. Chrome will add hyphens to a long URL on macOS, but not on Windows. Firefox doesn't support
## Ellipsis

Another option is that we can trail off, leaving the sentence unfinis…
```html
<style>
  p {
    overflow: hidden;
    text-overflow: ellipsis;
  }
</style>

<div class="wrapper">
  <p>
    This is a narrow column of text, with a very long word: antidisestablishmentarianism.
  </p>
  <p>
    The same problem happens with URLs: https://www.somewebsite.com/articles/a1b2c3
  </p>
</div>
```
Weirdly, we need `overflow: hidden` in order for `text-overflow` to work. A bit odd, but it is what it is.
### Single-line ellipsis

In other cases, we may wish to prevent line-wrapping altogether, and add an ellipsis if the string can't fit on a single line.
```html
<style>
  /*
    This selector matches the table
    cells containing student names:
  */
  /* tbody th {
    overflow: hidden;
    text-overflow: ellipsis;
    max-width: 250px;
  } */
  tbody th {

 white-space: nowrap;
 
 overflow: hidden;
  text-overflow: ellipsis;
  max-width: 250px;
}
</style>

<table>
  <thead>
    <tr>
      <th></th>
      <th>Trigonometric Functions</th>
      <th>The Unit Circle</th>
      <th>Non-Right Triangles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="col">Eli Aquina</th>
      <td>89</td>
      <td>61</td>
      <td>74</td>
    </tr>
    <tr>
      <th scope="col">Zhivko Germano</th>
      <td>78</td>
      <td>96</td>
      <td>77</td>
    </tr>
    <tr>
      <th scope="col">George Julius Edward Bradley-Coulson</th>
      <td>84</td>
      <td>89</td>
      <td>92</td>
    </tr>
    <tr>
      <th scope="col">Nessa Wilfrith</th>
      <td>97</td>
      <td>83</td>
      <td>91</td>
    </tr>
    <tr>
      <th scope="col">Shafaqat Kohinoor Sadi Vsevolod</th>
      <td>93</td>
      <td>88</td>
      <td>79</td>
    </tr>
  </tbody>
</table>
```
### Multi-line ellipsis

What if we want to show a few lines, and add the ellipsis afterwards?

For a long time, this was a very hard problem that required some very complicated JavaScript. Fortunately, there is a modern way to solve this problem: the `-webkit-line-clamp` property.

We need `overflow: hidden` to hide the lines that will be clamped off.

If you're thinking that this is an awful lot of ceremony, with `-webkit-box-orient` and `display: -webkit-box`, you're not alone: browsers are working on a new version of this property, called `line-clamp`. Unfortunately, at the time of writing, it's still early days.

**Watch out for Flexbox/Grid!(warning)**

In certain cases, `-webkit-line-clamp` can appear buggy, showing thin slices of truncated text below the ellipsis.

This can happen when the element we're applying these styles to is _also_ used as a Flexbox child / in a layout capacity.

To avoid possible issues, always apply line clamping to a paragraph tag that isn't being stretched or flexed as part of flexbox or CSS Grid. We can solve for this by using a wrapper div:
```html
<style>
.row {
  display: flex;
}

.clamped {
  -webkit-line-clamp: 8;
  /* Supporting declarations omitted for brevity */
}
</style>

<article class="row">
  <!-- This div is super important! -->
  <div>
    <p class="clamped">Safe to apply line-clamping to me!</p>
  </div>
</article>
```

Solution video : https://player.vimeo.com/video/558276533
```css
.article-summary .title {
  hyphens: auto;
  overflow-wrap: break-word;
}
.article-summary p {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
```
# Print-style Layouts
## Column layout

So far, we've seen a few layout modes:

- Flow layout, the “OG” layout algorithm.
- Positioned layout, letting us position elements based on an anchor (either its in-flow position, a containing block, or the viewport).
- Flexible Box (“Flexbox”) layout, for arranging elements in a row or column.
To accomplish this goal, we'll need 1 more layout mode: **Multi-Column Layout**.

This layout mode is fairly niche, but it does something that no other layout mode can do: automatically split content across multiple columns, in a manner that allows the parent container to grow and shrink accordingly.
```html
<style>
  .wrapper {
    columns: 2;
    column-gap: 16px;
    padding: 16px;
  }

  p {
    margin-bottom: 16px;
  }
</style>

<main class="wrapper">
  <p>
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
  </p>
  <p>
    It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
  </p>
  <p>
    Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.
  </p>
  <p>
    Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source.
  </p>
  <p>
    Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
  </p>
</main>
```
Try tweaking `columns: 2` to `columns: 3` to change the number of columns.

This layout mode is really pretty incredible. Notice that it can even spread paragraphs across multiple columns:
If we want to make sure that a particular child isn't broken across columns
```html
p {
  break-inside: avoid;
}
```
The algorithm's chief concern is distributing content evenly so that all columns are the same height. It's very good at its job; it re-evaluates whenever new content is added, to find the ideal distribution. This obscure layout mode can accomplish things that no other layout mode can.
## Floats

Let's look at yet another layout algorithm!

Floats were a fundamental building block of the pre-Flexbox toolkit. In the late '00s / early '10s, floats were all the rage. They allowed us to build common UI elements like sidebars.

Their reign was short-lived, as Flexbox offered a much-more elegant solution to these types of problems. And now that CSS Grid has widespread browser support, Floats are often thought of as a relic of the past, a tool from a bygone era.

So why are we talking about it? Well, it turns out that there are some things that _only_ floats can accomplish. And the CSSWG? hasn't forgotten about it, either—they've continued to beef up float capabilities. It can do some wild stuff nowadays!

Floats allow text to "wrap around" an embedded element. Check out how text wraps around this image:
```html
<style>
  img {
    float: left;
    margin-right: 16px;
  }
</style>

<p>
  Lorem Ipsum is simply dummy text of the printing and typesetting industry.
  Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and
  scrambled it to make a type specimen book.
</p>
<img src="https://courses.joshwcomeau.com/cfj-mats/cat-300px.jpg" />
<p>
  It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
</p>
<p>
  Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old.
</p>
```
A floated element is like a boulder in a stream; the other content flows smoothly around it. In this case, text wraps seamlessly around an image, but we can use this trick for _any_ embedded element, not just images!

We can choose which side the element should be floated by passing either `left` or `right` to the `float` property. Try switching the above code snippet to float the image on the opposite side!

Floated items don't come with any default margin. This means that the surrounding text will run _right up_ to the floated element, which often feels claustrophobic. By adding `margin-right` to a left-floated element, we create a bit of buffer around it.

## Indentation

On the web, it's conventional for paragraphs to be differentiated through spacing; we can tell where the paragraphs are because there's a bunch of space between them.

This isn't the only way to differentiate paragraphs, though. Books generally use _indentation_ instead.

The first line of each paragraph is inset, and this is how our eyes can distinguish one paragraph from another. There isn't any additional space between them.

How might we accomplish this on the web? There are a couple options.

We can select the first letter in a paragraph with the `:first-letter` pseudo-element. A bit of margin can accomplish this effect:
more-explicit way we can do it: using the `text-indent` CSS property:
```html
<style>
  p {
    text-indent: 2rem;
  }

  p {
    max-width: 500px;
    margin: 0 auto;
  }
</style>

<p>
  This is a paragraph that has been indented, using the <em>first-letter</em> pseudo-element. Normally, we can't apply CSS directly to text, but this pseudo-element acts as an invisible "span" that wraps around the first character.
</p>
<p>
  Indentation isn't super common on the web, but it's everywhere in print media! Most published books will use indentation like this, and will only add space between paragraphs at the end of a "section" or sub-chapter.
</p>
```
`text-indent` is not a new property: it is supported in all browsers, all the way back to IE 6!

`::first-letter` is still useful for certain typographical effects, like "drop caps" (a larger first letter, typically on the first paragraph in a page/chapter).

## Justified alignment

In print, it's common for text to be "justified" — this means that the spacing between each word is tweaked so that each line fills the available horizontal space:
```html
<style>
  p {
    text-align: justify;
    padding: 16px;
  }
</style>

<p>
  This paragraph has been justify-aligned. The goal with justify-aligned text is to create a sharp block of text that aligns both on the left and right edges. It accomplishes this goal by tweaking the spacing between each word. Historically, this process was painstakingly done by typographers, using their intuition and a hearty amount of hyphens to create well-formatted text.
</p>
```

**More info on justification(info)**

It's interesting to read about how print designers think about typography. In [The Elements of Typographic Style](https://www.goodreads.com/book/show/44735.The_Elements_of_Typographic_Style), author Robert Bringhurst explains that text should be "ragged" (fancy typographic word for left-aligned) when using a sans-serif or monospace font, or when there isn't much horizontal space.

If the column of text is too narrow, justified alignment will either produce awkward spacing or way too much hyphenation.

Solution video : https://player.vimeo.com/video/558277621
Solution code:
```css
.wrapper {
  column-count: 2;
  column-gap: 150px;
  max-width: 64rem;
  margin: 32px auto;
  border: 2px solid hsl(35deg 10% 40%);
  padding: 50px;
  background: linear-gradient(
    to right,
    hsl(35deg, 30%, 90%),
    hsl(35deg, 30%, 90%) 47%,
    hsl(35deg, 30%, 70%) 49.5%,
    hsl(35deg, 20%, 50%) 50%,
    hsl(35deg, 30%, 70%) 50.5%,
    hsl(35deg, 30%, 90%) 53%,
    hsl(35deg, 30%, 90%)
  );
}

h2 {
  font-size: 2rem;
  margin-bottom: 2em;
}

p {
  text-align: justify;
}

p:first-of-type:first-letter {
  font-size: 3em;
  float: left;
  line-height: 1em;
  margin-right: 0.2em;
}

p:not(:first-of-type) {
  text-indent: 2em;
}

* {
  font-family: 'Merriweather', serif;
}
```

# Masonry Grid with Columns

## What is masonry layout?

Made famous by sites like Pinterest and Unsplash, masonry layout is a way of stacking elements in an asymmetric grid, like this:
![[Pasted image 20231219104123.png]]
This layout method is commonly used with images, because it allows us to create a seamless grid with elements of all different sizes. If we tried to recreate something like this with CSS Grid or Flexbox, we'd wind up with something much less appealing:

Demo video : https://player.vimeo.com/video/555890644
Here's the code playground from the video:
```html
<style>
/* Quick lil' CSS reset */
body, ul, li {
  padding: 0;
  margin: 0;
}
ul {
  list-style-type: none;
}

/* Real code starts here */
ul {
  --gap: 16px;
  column-count: 3;
  column-gap: var(--gap);
  padding: var(--gap);
}

li {
  break-inside: avoid;
}

img {
  display: block;
  width: 100%;
  margin-bottom: var(--gap);
}
</style>

<ul>
  <li>
    <a href="">
      <img src="https://courses.joshwcomeau.com/cfj-mats/night-sky.jpg" />
    </a>
  </li>
  <li>
    <a href="">
      <img src="https://courses.joshwcomeau.com/cfj-mats/nasa-earth-shot.jpg" />
    </a>
  </li>
  <li>
    <a href="">
      <img src="https://courses.joshwcomeau.com/cfj-mats/cat-four-300px.jpg" />
    </a>
  </li>
  <li>
    <a href="">
      <img src="https://courses.joshwcomeau.com/cfj-mats/wall-art.jpg" />
    </a>
  </li>
 
</ul>
```
if we dynamically add more items to the grid (eg. infinite scroll), they don't get added onto the end, as we'd expect. Instead, the elements are added to the final column, and everything is redistributed.

Here's how we expect it to process new items (new items indicated with a blue color + border):
![[Pasted image 20231219105017.png]]
…And here's how it actually processes new items:
![[Pasted image 20231219105040.png]]
**Preserving order(info)**

On his blog, Tobias Ahlin shares a [rather clever way](https://tobiasahlin.com/blog/masonry-with-css/) to use `order` and `:nth-of-type` pseudoclasses to better approximate a Masonry layout with Flexbox.

It's definitely a heavier cognitive lift, but it can be a worthwhile approach if the order is important!
## The future

The good news is that browser vendors recognize that web developers want an easy way to implement masonry layouts, and they're working on it. Soon, we'll be able to use a special variant of CSS Grid that will let us create masonry rows:
```css
.container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-template-rows: masonry;
}
```
This new variant is customizable, letting us easily control the order that elements are rendered in!

The bad news is that as I write this, [no browsers support this variant](https://caniuse.com/mdn-css_properties_grid-template-columns_masonry). Once it reaches mainstream support, I'll update this lesson.

In the meantime, if you need a pagination-safe masonry layout, I suggest using a JavaScript library. The most popular option is aptly named [Masonry.js](https://masonry.desandro.com/) (which has been [wrapped for React](https://github.com/eiriklv/react-masonry-component) and possibly other frameworks).
# Text Styling

In the first module of this course, we covered the [fundamentals of typography](https://courses.joshwcomeau.com/css-for-js/00-recap/07-typography), things like creating bold/italic text, font sizes, and text alignment.

In this lesson, we're gonna expand on that knowledge. We'll learn a few more tricks, and see how text layout intersects with some of the stuff we've learned in the other modules.

## Line length

Have you ever tried to read Wikipedia on a very large screen?
Wikipedia doesn't constrain the maximum width, and so it'll grow as wide as it can.

This might seem like a good thing, since it makes use of all available space, but it makes the text much harder to read. Having to scan such wide lines tends to fatigue our eyes. And when we reach the end of a line, it's hard to figure out which line is next.

When I encounter text like this on the web, I wind up needing to use text selection in order to track where the line wraps:
Research on the ideal line length is a bit mixed, but most sources agree that the acceptable range is [between 50 and 75 characters per line](https://baymard.com/blog/line-length-readability).

Fortunately, CSS has a built-in unit for this purpose—the `ch` unit:
```html
<style>
  p {
    max-width: 50ch;
    margin-bottom: 1em;
  }
</style>

<p>
  Many poor golf courses are made in a futile attempt to eliminate the element of luck. You can no more eliminate luck in golf than in cricket, and in neither case is it possible to punish every bad shot. If you succeeded you would only make both games uninteresting.
</p>
<p>
  It is an important thing in golf to make holes look much more difficult than they really are. People get more pleasure in doing a hole which looks almost impossible, and yet is not so difficult as it appears.
</p>
<p>
  Excerpt taken from <cite>GOLF ARCHITECTURE</cite> by Dr. A Mackenzie, published 1920.
</p>
```
`1ch` is equal to the width of the `0` character, at the current font size.

Does setting a width of `50ch` mean that we'll get an average of 50 characters per line? Not exactly. Depending on your font, the `0` character might be significantly thinner or thicker than average.

On this platform, I use a font called [Wotfard](https://www.atipofoundry.com/fonts/wotfard). Wotfard's “0” is chunky: I've found that 50ch creates line lengths around 70 characters long.

Ultimately, we don't need to be _too_ precise here. As long as we're somewhere near the sweet spot of 50-75 characters, our users will have a pleasant reading experience.

## Text alignment

In [Module 4](https://courses.joshwcomeau.com/css-for-js/04-flexbox/02-cardinality), we saw how Flexbox can be used to precisely control the distribution of elements, including paragraphs.

You may wonder: does `text-align` still have a role to play, in a Flexbox / Grid world?

It does seem like the two approaches can be used interchangeably, within a Flex column:
```css
<style>
  .with-text-align {
    text-align: center;
  }

  .with-flexbox {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  p {
    padding: 16px;
  }
</style>

<div class="with-text-align">
  <p>Hello there!</p>
  <p>These paragraphs are centered</p>
</div>

<hr />

<div class="with-flexbox">
  <p>Hello there!</p>
  <p>These paragraphs are centered</p>
</div>
```
the middle of each line, the way you'd expect centering to work in a rich text editor.

`align-items`, though, is more about layout alignment. It positions _the paragraph as a block_. It doesn't affect the individual characters within that block.
![[Pasted image 20231219105707.png]]
# Font Stacks

The `font-family` property is how we change the font for a given element (and its children, since the property is inheritable).

Curiously, it's usually given multiple comma-separated values:
```css
.title {
  font-family: 'Lato', Futura, Helvetica, Arial, sans-serif;
}
```
This acts as a sort of "preference list". We've given the browser a list of fonts we'd like to use, in priority order. Ideally, it'll pick the first one, but if it's not available, it can use the second, or the third, or the fourth.

The last font in the list should always be the "category" for the font, like `serif`, `sans-serif`, `monospace`, or `cursive`. This ensures that if none of the other options are available, the browser will use its default font for that category.

Fonts can be unavailable for two reasons:
- The font isn't installed on the user's device.
- The font is a web font, and it hasn't yet been downloaded.

While every operating system comes with dozens of fonts, there are only a small handful that are "universally" available. Fonts like:

- Arial
- Courier New
- Georgia
- Helvetica
- Tahoma
- Times New Roman

The helpful website [CSS Font Stack](https://www.cssfontstack.com/) shows how common each font is between Windows and macOS. For example, _Calibri_ is available on 83% of Windows devices, but only 39% of macOS ones. Even historically-standard fonts like Arial aren't available for 100% of users.

So the goal with a font stack is to provide a menu of fonts that the browser can pick from, making sure that every user sees an acceptable font and nobody sees the (usually quite ugly) default serif browser font.

**Consistent experiences across devices(info)**

You might be wondering: don't we want _all_ users to see the exact same font? Why would we specify a list of possible fonts? Won't that lead to inconsistent experiences?
Indeed, fonts can be an important part of a brand identity. AirBnb commissioned their own font, [Cereal](https://airbnb.design/cereal/), and I imagine they want to make sure all users see it.
Unfortunately, we don't really live in a world where we can guarantee that sort of thing. As we'll learn in the lessons ahead, optimizing for the best user experience can mean making some sacrifices with fonts.
## System font stack

A rising trend in recent years is to use the "system font stack". This is a stack of fonts that default to the nicest default option for each platform.

It looks like this:
```css
p {
  font-family:
    -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui,
    helvetica neue, helvetica, Ubuntu, roboto, noto, arial, sans-serif;
}
```
That's a lot of fonts!

Over the years, the default system font on macOS has changed. As I write this, macOS and iOS both use the ["San Francisco" font](https://developer.apple.com/fonts/). `-apple-system` and `BlinkMacSystemFont` are aliases for the current system font. `avenir next` and `avenir` are fonts from previous versions of macOS.

When a user running Windows 10 visits our app, the browser won't recognize the first 4 options, but it _will_ recognize Segoe UI — as I write this, Segoe UI is the default system font in Windows 10.

The system font stack is nice because it automatically matches the conventions of the user's device, just like the radio buttons or select tags. And modern operating systems use well-designed fonts, so our application won't suffer cosmetically.

There are system font stacks for serif and monospace fonts as well. Find the full set at [systemfontstack.com](https://systemfontstack.com/).

Here's an example of the same page, rendered in Windows 10 and macOS Big Sur, using serif and sans-serif font stacks:

CSS Variables to the rescue!(info)
When it comes to working with the system font stack, CSS variables make life way nicer:
```css
html {
  --font-sans-serif:
    -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui,
    helvetica neue, helvetica, Ubuntu, roboto, noto, arial, sans-serif;
  --font-serif:
    Iowan Old Style, Apple Garamond, Baskerville, Times New Roman,
    Droid Serif, Times, Source Serif Pro, serif, Apple Color Emoji,
    Segoe UI Emoji, Segoe UI Symbol;

  /* Set a global default */
  font-family: var(--font-sans-serif);
}

/* Apply different fonts as needed */
p {
  font-family: var(--font-serif);
}
```
# Web Fonts

If we want to use a font that doesn't come pre-installed on the user's device, we can download and use a custom font!

There are lots of ways to do it. In this lesson, we'll look at a couple popular services that can help, and also see how to do it from scratch.

## Using Google Fonts

[Google Fonts](https://fonts.google.com/) is an online repository of free, open-source web fonts. They have hundreds of popular options.

It also effectively works as a CDN for fonts; they serve the fonts for us, from their own servers.

Google Fonts works by providing a snippet that looks like this:
```html
<link rel="preconnect" href="https://fonts.gstatic.com">
<link
  href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@1,400;1,600&display=swap"
  rel="stylesheet"
>
```
Drop this in the `<head>` of your HTML file.

The snippet will download a stylesheet which downloads a font. We can access that font in our CSS:
```css
.thing {
  font-family: 'Open Sans', sans-serif;
}
```
Web fonts should be wrapped in quotes (`'Open Sans'`, not `Open Sans`). This isn't strictly required if your web font is a single word, but it's a helpful convention: it indicates which fonts in the stack are web fonts vs. local fonts.

**No HTML file?(info)**

If you use a framework like Next.js, you may be a bit confused by the lack of an `index.html` anywhere in the project.

Some frameworks generate this file automatically, so that they can include the JS bundles and perform other optimizations.
These frameworks generally include built-in methods for working with web fonts. In Next.js, for example, there's the [next/font module](https://nextjs.org/docs/pages/building-your-application/optimizing/fonts).
You might need to do some research to figure out how to do this for your framework of choice.

The main benefit to Google Fonts is that it's nice and easy. Drop an HTML snippet in your app, and you're good to go!

There are some downsides, though:

- Lots of amazing fonts aren't available on Google Fonts
- Self-hosted web fonts can perform better

Gatsby creator Kyle Matthews discovered that self-hosting fonts can [save 300ms on desktop, and 1s+ on mobile 3G](https://www.bricolage.io/typefaces-easiest-way-to-self-host-fonts/).
**Performance trade-offs(info)**

I was initially surprised to learn that Google Fonts was a bit sluggish. Why are their servers so slow??

It's not actually about server speed, it's about the difference in approach.
Let's explore what happens when we use Google's HTTP snippet:

1. The browser fetches and parses our `index.html` file
2. The browser sees the `<link href="https://fonts.googleapis.com/css2">` tag, and fires off a request to fetch a CSS file
3. The browser parses the requested CSS file, and discovers that a web font needs to be downloaded from `https://fonts.gstatic.com`, so it fires off a request for that font file.
The CSS file is on `fonts.googleapis.com` and the font file itself is on `fonts.gstatic.com`. Because these are both external domains, some additional overhead is required (I'm not an HTTPS expert, but I believe there's some sort of handshake?).

The request for the CSS file is blocking; this means that the browser is stuck waiting on this request before it can start rendering the page.

When we use a self-hosted web font, by contrast, we can skip one of those steps: we can embed the CSS that fetches the font right in our HTML file, skipping Step #2. And because the font assets are on the same server, we can skip the third-party request overhead.

In the old days, this could be offset by the fact that browsers had a global cache; it was possible that your users would already have a cached version of the font, because a different site sourced the font from the same CDN. Due to privacy concerns, however, browsers have [started using partitioned caches](https://wicki.io/posts/2020-11-goodbye-google-fonts/). This means that your users will always need to download your web font on the first visit, even if they've visited other sites using the same font from the same CDN.

**GDPR compliance(warning)**

In 2022, a German court ruled that [Google Fonts doesn't comply with GDPR](https://www.theregister.com/2022/01/31/website_fine_google_fonts_gdpr/), the EU privacy laws. A website owner was fined €100 for the violation.

To stay fully compliant with GDPR, you should self-host your fonts. We'll explore how to do this in [the “Font Optimization” lesson](https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/10-font-optimization).
## Using modern tooling

Vercel, the company behind the Next.js framework, has released an interesting free resource called [Fontsource](https://fontsource.org/).

The idea with Fontsource is that it provides an easy-to-use method to install and use _self-hosted_ web fonts. It's built specifically for modern JS applications, letting you NPM install the fonts you wish to use. They support all Google Fonts, as well as additional open-source free-to-use fonts.

You can learn more by [reading their documentation](https://fontsource.org/docs/getting-started/introduction).

Angular v11+ has built-in support for Google Fonts, with configuration for inlining the fonts directly. You can [learn more in the Angular docs](https://angular.io/guide/workspace-config#fonts-optimization-options).
## The manual way

What if you want to use a font that isn't available on Google Fonts or Fontsource?

The rest of this lesson shows how to add web fonts "from scratch". Feel free to skip the rest of this lesson if you're happy with another option (though it may still be interesting to learn more about how web fonts work!).
### Converting formats

The fonts that run on our computers typically come in `.otf` or `.ttf` file formats. These file formats were never intended to be used on the web, and their files tend to be relatively enormous.

Our first order of business is to convert our font into a web-friendly format. You can use online converter tools like [Fontsquirrel's webfont generator](https://www.fontsquirrel.com/tools/webfont-generator).
### The font-face tag

How do we tell the browser that we want to use a web font? The `@font-face` at-rule has us covered:
```css
@font-face {
  font-family: 'Wotfard';
  src: url('/fonts/wotfard-regular.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'Wotfard';
  src: url('/fonts/wotfard-medium.woff2') format('woff2');
  font-weight: 500;
  font-style: normal;
}

@font-face {
  font-family: 'Wotfard';
  src: url('/fonts/wotfard-bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}

@font-face {
  font-family: 'Wotfard';
  src: url('/fonts/wotfard-regular-italic.woff2') format('woff2');
  font-weight: 400;
  font-style: italic;
}
```
We need multiple statements because each font weight and style has its own file. In this case, I'm loading 3 different font weights (regular, medium, and bold) and an italic variant for the regular weight.

The font file itself doesn't contain any "metadata" about what weight/style it is, so we need to link them up. That's what all the declarations in the `@font-face` statement are doing. We specify the source for a set of characters (`src`), and then the associated metadata with that set (`font-family`, `font-weight`, `font-style`).
Our goal is to start loading the fonts ASAP, so I like to put these `@font-face` statements right in the `index.html`:
```html
<html>
<head>
  <style>
    @font-face {
      font-family: 'Wotfard';
      src: url('/fonts/wotfard-regular.woff2') format('woff2');
      font-weight: 400;
      font-style: normal;
    }

    /* Other @font-face statements omitted for brevity */
  </style>
</head>
```
When those `@font-face` statements are parsed by the browser, the font file declared under `src` will be fetched and loaded. You can use the font in your CSS the way you'd use any font:
**Static files in React(warning)**

One of the tricky things about React is that you can't access static files like fonts or images in the same way you would in a standard HTML/CSS project.

It's beyond the scope of this course, but check out the following guides depending on your generator/meta-framework:

- [create-react-app](https://create-react-app.dev/docs/using-the-public-folder/)
- [Next.js](https://nextjs.org/docs/basic-features/static-file-serving)
- [Gatsby](https://www.gatsbyjs.com/docs/how-to/images-and-media/static-folder/)
## Faux bolds and italics

The `@font-face` statement lets us connect a specific font weight value (eg. 700) to a character set. When we use either `font-weight: bold` or `font-weight: 700`, the browser will use the heavier characters instead of the default ones.

But what happens if we try to use bold text when we haven't supplied a bold font file?

The browser can create "faux" bold text. It achieves this by expanding the thickness of every line in every font, stretching it out in all directions. This tends to create muddy, indistinct letters.

When font designers create bold variants of a font, they're very intentional and strategic about how they change the characters, optimizing for aesthetics and readability. Browser-generated faux-bolds are much less sophisticated; they just make the lines thicker.

Similarly, when it comes to italics, the browser simply slants the letters, whereas true italics use alternate characters:
To be fair, I'm using a highly-stylized font ([Playfair Display](https://fonts.google.com/specimen/Playfair+Display?category=Serif)) in these examples. The differences can be more subtle than this. But it's the kind of small detail that can make a surprisingly big impact on how polished/professional your site/application appears to users.

# Font Loading UX

When a person visits our site for the first time, they'll need to download all of the web font files we're using

*

.

This doesn't happen instantaneously. In most cases, our HTML will be ready-to-go while the font files are still zipping around the internet.

What should we do?

There are two main options:
1. Wait until the web font has been downloaded before showing any text.
2. Render the text in a "fallback" font, one that is locally installed on the user's device.
Both of these options introduce problems. With Option 1, we're depriving the user of the text they care about. With Option 2, the experience can be quite jarring, flipping between fonts and causing layout shifts.

Option 1 is colloquially known as **FOIT** — Flash Of Invisible Text. Option 2 has been called **FOUT** — Flash Of Unstyled Text.

As long as users need to download web fonts when they visit our page, this problem will exist. Fortunately, however, we can improve things a bit with some modern CSS.

**Works on my machine(info)**

It may surprise you to learn that this is a problem. It's likely that you've never experienced any flashes of unstyled/invisible text, when viewing your application on your machine!

There are some things to keep in mind:

- On localhost, the font can be downloaded instantly, so you won't encounter this problem.
- In production, you'll only notice this the first time you visit the page, since the browser will cache it for your site.
- You might already have the font installed locally on your machine.
- Your internet connection might be significantly faster than the worldwide average.

For a more realistic picture of how your users see your application, you should [throttle your network speeds](https://developer.chrome.com/docs/devtools/network/#throttle) and [disable local fonts](https://developer.chrome.com/blog/new-in-devtools-86/#emulate-local-fonts).

## The font-display property

To control how a font should be rendered before it's available, we can take advantage of the `font-display` property.

It's included in our `@font-face` statement:
```css
@font-face {
  font-family: 'Great Vibes';
  src: url('/fonts/great-vibes.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap; /* 👈👈👈 */
}
```
When we add the Google Font snippet, it includes a query parameter that sets this property:
![[Pasted image 20231219113242.png]]
  
The moment an HTML element tries to render text in our web font, a timer starts. Like a hockey game, there are 3 periods:

- **The block period**. During this time, the text will be painted in an invisible ink, so that no text is visible. It'll render the font ASAP if it becomes available during this period.
- **The swap period**. During this time, a fallback font is rendered (the first available font in the font stack). If the web font becomes available during this period, it gets swapped in immediately.
- **The failure period**. If the font isn't loaded during the block or swap periods, it stops trying, and will keep showing the fallback font no matter what happens with the web font.

How long are each of these periods? It depends on the `font-display` property. Essentially, **`font-display` is a way to control the length of each window**.

Let's go through the options:
![[Pasted image 20231219113412.png]]
`font-display: block` prioritizes the availability of the font over everything else. It has a relatively-long block period, and an infinite swap period.

The specification doesn't provide explicit time durations for these periods, but it does provide recommended maximums. For `font-display: block`, the block period should be no more than 3 seconds.

This value should only be used when the font is absolutely critical. For example, if you use an icon font, we really do want the font to be loaded before the "text" is shown, otherwise we might see random letters instead of the icons. As we'll learn later in this module, though, icon fonts in general should be avoided.

![[Pasted image 20231219113505.png]]
With `font-display: swap`, there is little to no block period

*

, and an infinitely-long swap period. The goal is to get text rendering as quickly as possible.

This is the value that Google Fonts uses. It's a good option, but I think there's a better one for most cases.

![[Pasted image 20231219113531.png]]
`font-display: fallback` is the most intricate value, and I think it strikes the perfect balance.

It features a very-short block period (about 100ms), and a moderate swap period (about 3s).

**This is my preferred value.** I use it in all of my projects. It prioritizes a smooth user experience above all else:

- On speedy connections, it's likely that the font can be downloaded within the block period, preventing an uncomfortable flash between font families
- On very slow or intermittent connections, the fallback font is used forever, preventing a random flash between fonts seconds/minutes after the page has loaded.
![[Pasted image 20231219113703.png]]
Finally, `font-display: optional` is a great choice when the font is a subtle improvement, but not really very important. It features a short block period (100ms or less), and no swap period at all. If the font doesn't load immediately, it won't be used at all.

Generally, this value means that users will see the fallback font for their first page, but the web font for all subsequent pages. The first page view loads the font in the background, to be applied on the _next_ page view.

It means that almost everyone will see the fallback font on their first visit, but there won't be any flashes of unstyled text, and no layout shifts caused by a slow-loading font.

**So, which value should you use?** Ultimately, there's no “right” answer. I prefer `font-display: fallback` because I think it strikes the right balance for _my_ projects, but you may have different priorities.

## Font matching

If you use a font-display with a swap period (everything except _optional_), there's a good chance that the rendered text will flip from one font to another. If the fonts are very different in size/shape, this can cause a pretty unpleasant layout shift:

Browsers have recently begun implementing a new feature called "font descriptors" (also known as f-mods). These let us tweak the characteristics of our fallback font to match the web font, for a much-less-jarring swap.

Here's what it looks like:
```css
@font-face {
  font-family: "Great Vibes";
  src: url('/fonts/great-vibes.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: "Fallback";
  size-adjust: 95%;
  ascent-override: 90%;
  descent-override: 20%;
  src: local("Arial");
}

body {
  font-family: "Great Vibes", "Fallback", sans-serif;
}
```
`size-adjust`, `ascent-override`, and `descent-override` all control the vertical size/position of the text. `size-adjust` is similar to `font-size`, `ascent-override`/`descent-override` are similar to `line-height`.

As I write this in January 2023, Chrome/Firefox/Edge have implemented the first category, and several tools have popped up to take advantage of it:

- [Fallback Font Generator](https://screenspan.net/fallback), a tool to help you come up with appropriate `size-adjust`, `ascent-override`, and `descent-override` values.
- [Fontaine](https://github.com/danielroe/fontaine), a plugin that automatically calculates and applies `size-adjust`, `ascent-override`, and `descent-override`.
- [next/font](https://nextjs.org/docs/basic-features/font-optimization) applies these same optimizations, for folks using Next.js.

I did some experimentation on my blog, and found I had best results using the “Fallback Font Generator” tool to manually tweak things. I chose Verdana as my fallback font, since it looked the most-similar to Wotfard, the web font I use.

demo video : https://courses.joshwcomeau.com/cfj-mats/blog-fmods.mp4

Note that f-mods aren't yet supported in Safari, but that shouldn't stop you from experimenting with this stuff! Your web fonts will still work just fine in Safari, they just won't benefit from the optimizations.

You can learn more about f-mods here:
- [Intro to f-mods from Simon Hearne](https://simonhearne.com/2021/layout-shifts-webfonts/#reduce-layout-shift-with-f-mods)
# Font Optimization

Font optimization is a _huge_ topic, and one well beyond the scope of this course.

I'll link to some resources at the bottom of this article, but for our purposes, I'm gonna suggest that we let Google do all the hard work for us.

A little-known fact about Google Fonts is that they come _heavily_ optimized. Let's look at an example.

Inter is a critically-acclaimed sans-serif font. It's free and open-source. When you download it from its [official website](https://rsms.me/inter/), each `.woff2` font file ranges from 99kb to 151kb. When I added 3 font weights to a sample product, it downloaded 427kb worth of fonts.

When I load the same 3 font weights through Google Fonts, it squeezes them all into 1 file that was only 37kb. A savings of over 90%!
In this video, we'll show how this is possible, and how we can self-host Google's optimized versions of fonts.
In this video, we'll show how this is possible, and how we can self-host Google's optimized versions of fonts.
Demo video : https://player.vimeo.com/video/558252679

In addition to the method shown in this video, Discord member tris shared a helpful tool, [google-webfonts-helper](https://gwfh.mranftl.com/fonts). It allows you to quickly download optimized fonts from Google Fonts. It seems quite a bit more convenient, though there is a caveat: it doesn't support variable fonts.

**Font optimization(success)**

If we can reduce the filesize of each font file, we can increase our expressiveness without harming performance.

For example, if your app only includes a single language like English, you can remove glyphs that only appear in other languages, like `é` or `ç`. This can drastically reduce the size of a font file.

Font optimization is beyond the scope of this course, but here are some resources to get you started:

- [Using Glyphhanger to optimize font files](https://www.sarasoueidan.com/blog/glyphhanger/), by Sara Soueidan
- [Reduce Web Font Size](https://web.dev/reduce-webfont-size/), a guide from Google's web.dev.
# Variable Fonts

When using web fonts, each weight and style is its own file. If you want to have three weights (regular, medium, and bold) and two styles (regular and italic), you'd need **six** different font files. Having this many files is a recipe for invisible/unstyled text, as we saw in the last lesson.

Fortunately, a spiffy new technology has come to our rescue: **variable fonts**.

The idea with a variable font is that the font has parameters that can be tweaked to control the rendered output. The most obvious example is font weight:

With standard fonts, we need to pick 2 or maybe 3 weights. With variable fonts, there are _hundreds of valid values_.

Font weight is an example of an "axis", essentially a variable that can slide within a specified range. There are 5 standardized axes, but font designers can add custom ones as well. This font, Recursive, defines 5 axes (2 standard and 3 custom):

For demo refer : https://courses.joshwcomeau.com/css-for-js/06-typography-and-media/11-variable-fonts

Font designers are having fun and building amazing fonts. [Decovar](https://v-fonts.com/fonts/decovar), by David Berlow, provides a suite of different stems and skeletons. You can make some zany and illegible words with it:

## Variable fonts on Google Fonts

Happily, Google Fonts recently added support for variable fonts! You can [view a full list of supported fonts](https://fonts.google.com/variablefonts), and [learn how to use them](https://developers.google.com/fonts/docs/css2) in their docs.

As I write this, their docs are unfortunately not _super_ clear.
Here's how to correctly pull variable fonts from Google Fonts:

Demo video : https://player.vimeo.com/video/559677837
```css
<link rel="preconnect" href="https://fonts.gstatic.com">
<link
  rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap"
>
```
## Variable fonts from scratch

Here's an updated `@font-face` statement:
```css
@font-face {
  font-family: 'Recursive';
  src:
    url('/fonts/recursive-variable.woff2') format('woff2 supports variations'),
    url('/fonts/recursive-variable.woff2') format('woff2-variations');
  font-weight: 300 1000;
  font-display: fallback;
}
```
If we want to use "custom" variations like “casual”, we'll need to indicate that it's a special version of the `.woff2` format. This was initially done with `woff2-variations`, but was updated to be `woff2 supports variations`. During this transition period, we'll need to supply both.

Notice, too, that we specify _two numbers_ for `font-weight`. This is the range of font weights that this variable font supports. We're specifying that this `@font-face` statement should apply for any font weight between 300 and 1000, inclusive.
### Using variable fonts

When it comes to font weight, things are nice and straightforward. We can use `font-weight`, same as we always have, except now we can pick any value within our range:
```css
.hello {
font-weight: 777;
}
```
But how would we specify custom variations, like "cursive" or "casual"? The new `font-variation-settings` property can help:
```css
<style>
  .fun-heading {
    color: deeppink;
    font-variation-settings:
      "CRSV" 1,
      "CASL" 0.9;
  }
</style>

<h2>
  This is a serious heading
</h2>

<h2 class="fun-heading">
  This one, not so much!
</h2>
```
`font-variation-settings` accepts a comma-separated list of settings. Each setting tweaks an axis (written as a four-letter string in quotes), and a value (always a number).

We can also use this property to set “built-in” font properties, things like font-weight and font-style:
```css
/* This rule: */
.with-settings {
  font-variation-settings:
    "wght" 725,
    "wdth" 125,
    "slnt" -10;
}

/* …is equivalent to this rule: */
.without-settings {
  font-weight: 725;
  font-stretch: 125%;
  font-style: oblique -10deg;
}
```
That said, **I recommend using the standard properties.** `font-weight: 725` feels more readable to me than `font-variation-settings: "wght" 725`. It also seems as though some variable fonts don't implement `font-variation-settings` correctly; it's more hit-or-miss.

And so really, I view `font-variation-settings` as a way for us to customize _non-standard_ font aspects, like the cursive/casual options we saw above.

Each font has its own axes and ranges, so you'll need to consult the documentation for each font to figure out what your options are. For Recursive, this information is available [on their homepage](https://www.recursive.design/):

Solution video : https://player.vimeo.com/video/559987370 
Solution Git : [View the solution](https://github.com/css-for-js/variable-fonts-exercise/compare/solution) on Github.

**A small correction(info)**

In the video, you may have noticed that I applied my global CSS using the wildcard selector (`*`):
This has been changed. In the updated version of the exercise, I instead apply the CSS variables to the root `html` tag:
```css
html {
  --color-gray-100: hsl(270deg 25% 96%);
  --color-gray-300: hsl(270deg 17% 84%);
  --color-gray-500: hsl(270deg 17% 72%);
}
```
**Ultimately, both of these approaches work, but there's a subtle difference.** It's slightly better to place our global CSS variables on the root `html` tag.

If you're curious, we'll dig into the difference here:
The reason is **inheritance.** Suppose I have this setup:
```css
<style>
  * {
    --color-primary: black;
  }
  aside {
    --color-primary: red;
  }
  strong {
    color: var(--color-primary);
  }
</style>

<aside>
  <strong>Warning:</strong> alien invasion imminent.
</aside>
```
**What color do you think that “Warning” text is?**

Well, let's think about it: the default value for `--color-primary` is black, but we've _overwritten_ that value on the `aside` selector. For the `<aside>` element, `--color-primary` will be red.

The `<strong>` tag is within the `<aside>`, and so it'll inherit that red color for `--color-primary`, right?

**Afraid not.** The color will be black.
The wildcard selector (`*`) can be thought of as a stand-in for every possible valid selector. And so, it's as if we had done this:
```css
div, span, aside, strong, em /* And so on, for all valid selectors */ {
  --color-primary: black;
}
aside {
  --color-primary: red;
}
```
The value for `--color-primary` will only be inherited by children when that child doesn't specify its own value. And when we use the wildcard selector, we specify a value on _every tag_. The `strong` element gets its own `--color-primary: black`, and so it won't inherit the `red` from its parent `aside`.

We don't even have to talk about specificity; the lowest-specificity selector will always win over inheritance.

When we use the `html` selector instead, it's like a beautiful waterfall. We apply this property right at the top, and it flows down through all the layers of our tree. When our `aside` sets `--color-primary`, it establishes a new value for this chunk of the DOM tree, affecting all descendants:
```css
<style>
  html {
    --color-primary: black;
  }
  aside {
    --color-primary: red;
  }
  strong {
    color: var(--color-primary);
  }
</style>

<aside>
  <strong>Warning:</strong>
  alien invasion imminent.
</aside>
```
**In general, this is what we want.** It allows us to change a CSS variable for a chunk of the DOM tree, without having to micro-manage each and every descendant. And so, while it doesn't make a _huge_ difference, this is seen as the better practice.

One more quick note: we can use `html` and `:root` interchangeably. It makes no difference.

`:root` refers to the top-level element in the DOM. In a properly-formed HTML document, this is always the `<html>` tag. And so `:root` is essentially an alias for `html`. I prefer to use `html` because it feels like a pointless abstraction to me, but ultimately it's all the same thing.
# Icons

Icons are a super important part of just about every modern application.

When it comes to the web, there are two common ways of implementing them: we can use an "icon font", where each character resolves to an icon instead of a letter, or we can use SVG, where each icon is an inline SVG DOM node.
Of the two, I _much_ prefer the SVG approach, for so many reasons:

- SVGs tend to look more crisp and sharp.
- They're easier to position and use (`width` instead of `font-size` makes way more sense!).
- They can be more accessible.
- They can be multi-color.
- They can be tweaked and animated.

In this lesson, we'll learn how to use modern SVG icon packs in JavaScript frameworks.
**What's an SVG?(info)**

SVG stands for “Scalable Vector Graphic”. Unlike other image formats like JPEG and PNG, which store binary information about the colors of specific pixels, SVG stores the mathematical instructions for how to draw the shapes within the image.

It's written in XML, which means it looks an awful lot like HTML. Here's a "Hello world" SVG which draws a pink circle:
```xml
<svg
  viewBox="0 0 100 100"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
>
  <circle cx="50" cy="50" r="40" stroke="black" fill="pink" />
</svg>
```
You can save this into a file called `circle.svg` and use it like any other image format (for example, `<img src="/circle.svg" />`). But you can also copy/paste the code directly into your HTML. This is known as "inline SVG":
```xml
<html>
<body>
  <h1>Hello World</h1>
  <div class="icon-wrapper">
    <svg
      viewBox="0 0 100 100"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <circle cx="50" cy="50" r="40" stroke="black" fill="pink" />
    </svg>
  </div>
</body>
</html>
```
When we inline our SVGs, we can target individual sub-elements with CSS and JS!
```css
/* This will change the circle from pink to green! */
.icon-wrapper circle {
  fill: green;
}
```
SVG is an incredible technology, and its presence on the web opens all kinds of fascinating doors. Unfortunately, we won't be exploring them much in this course, though I definitely plan on creating educational materials about SVG in the future!

## Popular icon sets

Unless you have a design team on hand, you'll likely want to use a pre-existing icon set rather than creating one from scratch.

Here are some of my favourites:

- [Feather icons](https://feathericons.com/)
- [icomoon](https://icomoon.io/)
- [Material Design icons](https://github.com/google/material-design-icons)
**More information about Feather Icons(info)**

I share a bit more information about how I use Feather Icons over in the Treasure Trove: [Feather Icons](https://courses.joshwcomeau.com/css-for-js/treasure-trove/003-feather-icons)
## Using icons

When you visit the homepage for an icon pack, you're given the option to download individual SVG files for each icon.

If you use React, you'll also need to convert each of the SVG files to JSX, so that they can be used as React components. There are [online tools that can help with this](https://svg2jsx.com/), but if you have dozens or hundreds of icons, it winds up being quite a bit of work.

Fortunately, there are packages that can help us out!

In React, for example, Feather's creator has created an NPM package, `react-feather`. Feather icons can be imported and rendered:
```js
import React from 'react';
import { HelpCircle } from 'react-feather';

function Something() {
  return (
    <div>
      <HelpCircle />
    </div>
  );
}
```
Similar packages exist for [Vue](https://www.npmjs.com/package/vue-feather), [Angular](https://www.npmjs.com/package/angular-feather), and even [Svelte](https://www.npmjs.com/package/svelte-feather-icons).
**Icons and accessibility(warning)**

It's important to remember that some of our users will use our product with a screen reader instead of a typical display. Screen readers can accurately dictate the text on our page, but they don't know how to deal with our SVG icons.

There are a number of ways we can add additional text information for folks using a screen reader. Here's my favourite:
```html
<button>
  <HelpCircle />
  <span class="visually-hidden">
    Visit the help center
  </span>
</button>
```
For more information about the `.visually-hidden` class, check out the [“Hidden Content” lesson](https://courses.joshwcomeau.com/css-for-js/02-rendering-logic-2/18-hidden-content#hiding-from-screens).

If you choose to use an icon font, you have an additional challenge: the icon is mapped to a random character, which can produce garbled output to screen readers. You'll need to add `aria-hidden` to the icon element (as well as provide fallback text, using visually-hidden

## Spacing issues

For all of the benefits that SVG icons bring, there is one super-common, super-frustrating issue with them.

Take a look at the following example:
```js
import styled from 'styled-components';

import { Home } from 'react-feather';

function Header() {
  return (
    <Button>
      <Home />
    </Button>
  );
}

const Button = styled.button`
  padding: 0;
  border: 2px solid black;
`

export default Header;
```

Our button has no padding, and yet there's a noticeable, asymmetric amount of bottom spacing.

Take a minute to think about this. Can you figure out where this space is coming from?
The culprit here is something we saw much earlier, in a very different context. The problem is that SVG elements have a default value of `display: inline`, and [inline elements have "magic space"](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/09-flow-layout#inline-elements-have-magic-space).

Using an icon pack can make this a bit tricky, since we may or may not have access to the underlying SVG element. I like to solve this in CSS, using a descendant selector:
```js
import styled from 'styled-components';

import { Home } from 'react-feather';

function Header() {
  return (
    <Button>
      <Home />
    </Button>
  );
}

const Button = styled.button`
  padding: 0;
  border: 2px solid black;

  & > svg {
    display: block;
  }
`

export default Header;
```
**Isn't this a bad practice?(info)**

_In general_, I'm not a fan of nesting when working with a component-driven JavaScript framework.

Nesting makes it harder to understand where styles are coming from; the brilliant thing about solutions like styled-components is that all of an element's styles are colocated in 1 spot

*

. We can solve so many problems by deftly side-stepping the cascade and tying our styles to the element. When we start messing with descendant selectors, we open the door for all sorts of troubles (eg. specificity wars).

In this situation, though, the SVG is an element created by a third-party component. I make an exception for third-party components.

Here's why it's different: I don't have the ability to write styles within the `Home` component, since it's tucked away inside an NPM package. So instead, my `Header` component “adopts” it. It becomes the single source of styles.

The most important thing is that we don't "compete" with our own styles. When I write a declaration, I shouldn't have to worry about some other style somewhere else in the app that might be overwriting it. With this solution, all of my styles for that `<svg>` HTML element are in 1 place. That's what's important.

# Images

Like so many things in CSS / the web, images are deceptively complex.

It's (relatively) easy to get started with images. Throw a url in an `<img>` tag, and it displays! And yet, there is so much complexity under the surface.

Working with images in CSS has changed a lot over the past few years. We've gotten some new tools to make it easier, and some other new tools that make it more complex, but better for our users.

Over the next few lessons, we'll dig into the intricacies of image rendering and layout. Before we get ahead of ourselves, though, let's go over the fundamentals.

## About the img tag

The `img` HTML tag has two required attributes:

- `src`
- `alt`
`alt` is a property that allows you to specify "alternative text". It's meant to serve as a description of what the image contains.

You've probably heard that alt text is important. It provides critical context to folks who aren't able to see the images, whether because of a visual disability or because of a faulty network connection.

Not all images require alternative text. If the image is purely decorative and has no semantic value, you can specify `alt=""` to indicate that screen readers can ignore it.

How do we know if an image is semantically valuable? I try and imagine what the user experience would be like if the image failed to load. If I don't know what's depicted in the image, would it make the product harder to use? If so, it definitely requires alt text.

In some cases, an image isn't critical to the user experience, but it still provides value. For example, Wikipedia articles include relevant photos. While the article still makes sense without these photos, they provide valuable context, and should be described with alt text.

If you're not sure if an image qualifies as decorative or not, it's best to err on the safe side, and add alt text. Folks using screen readers can easily skip past images, so don't worry about "polluting" the experience for them!

Eric Bailey writes about how to judge if an image is decorative in the blog post “[Your Image Is Probably Not Decorative](https://www.smashingmagazine.com/2021/06/img-alt-attribute-alternate-description-decorative/)”.

### Writing effective alt text

There is a lot of confusion around how to write effective alternative text.

The goal with alternative text should be to convey the _semantic meaning_ of the image to the user.

Let's look at an example. Suppose we're building an analytics dashboard called _Octo Analytics_. Here's a mockup I found online ([source](https://dribbble.com/shots/15298655-Vanti)):

Like many sites, the company logo is in the top-left corner. Let's assume that it links to the product's homepage.

What should the alt text be, for this green corner logo?

Many developers will describe the image as they see it, something like “Abstract green octopus illustration”. This _seems_ to make sense, but it isn't actually very helpful for real users. What is the _purpose_ of this green octopus? What happens if I click on it?

As sighted users, we can infer a lot of meaning from the visual context. An image in the top-left corner of the page is usually a logo, and it usually links back to the homepage.

If we can't see the layout of the page, though, we don't have that context
. So we need to provide it in the alt text.
Here's what I'd set it to:
```html
<img
  alt="Octo Analytics logo - Home"
  src="/logo.png"
/>
```
We're letting the user know that it's a logo, and that it leads to the homepage. It's the same context that sighted users take for granted.

Interestingly, this means that the exact same image might have _totally_ different alt text depending on the circumstances. The alt text depends on the context the image is used in, not just the contents of the image.

**One more thing:** Alt text should _not_ include additional contextual information. For example, here's what you _shouldn't_ do:
```html
<img
  src="/landscape.jpg"
  alt="Painting of a beautiful landscape. Artist: C. Essess"
/>
```
Instead, the attribution should go in a `<figcaption>` below the image:
```html
<figure>
  <img
    src="/landscape.jpg"
    alt="Painting of a beautiful landscape."
  />
  <figcaption>
    Artist: C. Essess
  </figcaption>
</figure>
```
Here are the best resources I've found for learning more about writing effective alt text:

- [How To Design Great Alt Text](https://www.deque.com/blog/great-alt-text-introduction/) by Deque
- [Alternative Text](https://webaim.org/techniques/alttext) by WebAIM

**Contradictory guidance(warning)**

The two guides linked above, from Deque and WebAIM, are slightly contradictory in places.
For example, Deque recommends company logo images should have the word "logo", as well as some additional context about where the link goes (eg. "Octo Analytics logo - Home"). WebAIM says that the company name alone is sufficient ("Octo Analytics").

Which one of these options is better? Well, it's subjective. On the one hand, WebAIM's suggestion is more terse, saving the user from an unnecessarily-long description. On the other hand, Deque's option is clearer, and the extra bit of information will be helpful for some people / in some contexts.

Here's my personal view: it doesn't really matter which option you go with. Either way, you're doing better than 95% of the sites on the internet.

The important thing is that you're writing alt text with the right goal in mind. You're not simply describing images for people who can't see them. You're trying to provide the context needed so that people can navigate and use your website / web application.

## img vs. background-image

In addition to the `<img>` tag, there's another common way to use images on the web: as a background image, through the `background-image` CSS declaration.

The `background-image` property is meant to be used for, well, backgrounds! For example, the old "Space Jam" website has a twinkly star background texture:
I would definitely use `background-image` in this case, because it functions as a wallpaper, something meant to be hung behind the content, for a purely aesthetic purpose.

It's important to use an `img` tag for semantically-meaningful images, because background images can't be given alt text.

A mistake developers often make is to use `background-image` on a semantically-relevant image because they need to take advantage of related CSS properties like `background-size` and `background-position`.

Thankfully, modern CSS has our back. In the next lesson, we'll learn how to control image rendering.

# Fit and Position

It's important to understand that the `<img>` tag is fundamentally _weird_
`img` is known as a "replaced element". Unlike other DOM nodes, the browser replaces the `<img>` tag with a foreign entity: the image itself. Images aren't like other DOM nodes, and they don't always follow the rules.

For example, images are inline elements, and inline elements "go with the flow"; we generally can't give an inline element a `height`, since that would mess with the layout. And yet, images can be given a height.

Images come with their own intrinsic size, based on the dimensions of the image file., image has a natural size of 400 × 300:

Images also have an _intrinsic aspect ratio_. This means that if we only supply one dimension, either `width` or `height`, the other dimension scales up or down as-needed, to preserve the aspect ratio:
```html
<style>
  img {
    width: 200px;
  }
</style>

<img
  alt="Blank image showing its own measurements, 400 by 300"
  src="https://courses.joshwcomeau.com/cfj-mats/size-400-300.png"
/>
```
Even though we haven't set a `height`, it scales down to 150px, to preserve the same proportions.

What happens if we provide both a width _and_ a height? What if it doesn't match the image's natural aspect ratio?

By default, the image will distort, stretching like a sock being pulled over a foot:
answer. It's impossible to display an image accurately when we change its proportions. Something's gotta give.

That said, this default behaviour is almost never what we want it to do. A better alternative in most cases is to crop the image, trimming off any excess that can't fit in the specified rectangle.

For many years, this was only possible with background images. Fortunately, modern CSS includes a couple tools that can help us out in this case. First, let's look at `object-fit`:

Demo Video : https://player.vimeo.com/video/559667783

**“Object”?(info)**
The `object-fit` property works on images, but it isn't exclusive to images: it can also be used on `<video>` tags!

In general, it's less relevant with videos, but it can come in handy when working with "video GIFs" (short videos that look/act like animated GIFs, but come in at a fraction of the size).
### Object Position

When using an `object-fit` value like `cover`, the browser will crop our image so that we see the very center of the image, and trim off the edges. But in some cases, we'll want to use a different anchor point.

`object-position` lets us specify how the image should be translated or cropped within its available space. It's very similar to `background-position`, if you're familiar with that property.

In its purest form, `object-position` takes two numbers: one for the horizontal offset, and one for the vertical offset. Play around with the horizontal position here, with the different `object-fit` values, to get a sense of how it works:
```css
.thing {
  /* Anchor to the top-left corner */
  /* Same as "0% 0%" */
  object-position: left top;
}
```
### Swoops

One of my little design tricks is to use SVG swoops like this one for decorative effect:
I generally want this image to grow wider and wider on larger monitors. On smaller devices, though, it looks a bit _too_ swoopy, so I'd prefer to crop it.

Here's the effect we're after:
demo video : https://courses.joshwcomeau.com/cfj-mats/swoops-resize-hd.mp4

Solution Code :
```html
<style>
  body {
    margin: 0;
    padding: 0;
  }

  img {
    width: 100%;
    /* Solution */
    min-height:150px;
    object-fit:cover;
    object-position:left center;
  }
</style>

<img
  alt=""
  src="https://courses.joshwcomeau.com/cfj-mats/swoops.svg"
/>
```
**Scaling and vector images(info)**

You may be wondering: isn't it bad to have an image stretch like this, growing to any possible size? Won't it get pixellated and blurry on large monitors?

This is indeed a concern for raster images, formats like `jpg`, `gif`, and `png`. The swoops above, however, are stored as SVGs. One of the neat things about SVG images is that they can grow to any size without loss of quality. As we saw in the previous lesson, SVGs contain instructions for how to draw the image, not raw color values for individual pixels.
# Images and Flexbox

Because the image tag is fundamentally weird, it doesn't always behave the way we expect when it interacts with certain layout modes. This is _especially_ true when it comes to Flexbox.

For example, here we have an image in a flex container. Try resizing the result window, and see if anything curious happens:
```html
<style>
  body {
    margin: 0;
    padding: 0;
  }

  main {
    display: flex;
  }

  img {
    flex: 1;
  }
</style>

<main>
  <img
    alt=""
    src="https://courses.joshwcomeau.com/cfj-mats/size-200-300.png"
  />
</main>
```

We've set `flex: 1`, which sets `flex-basis` to `0`. So why is it overflowing the container on smaller window sizes?

Here's another curiosity: we have two images, and one is set to consume twice as much space as the others. Check out what happens when the window grows, though:
```html
<style>
  body {
    margin: 0;
    padding: 0;
  }

  main {
    display: flex;
    gap: 8px;
  }

  img {
    flex: 1;
  }
  .twice-as-big {
    flex: 2;
  }
</style>

<main>
<img
  alt=""
  src="https://courses.joshwcomeau.com/cfj-mats/size-200-300.png"
/>
<img
  alt=""
  class="twice-as-big"
  src="https://courses.joshwcomeau.com/cfj-mats/size-200-300.png"
/>
</main>
```
Most developers assume that setting `flex: 2` will cause the image to scale up twice as quickly, for a layout
Can you make sense of _why_ the images are behaving the way they are? Take a couple minutes and think about the rules of Flexbox and how they may or may not be applied here.

We'll explore in this video:
Demo video : https://player.vimeo.com/video/559741741

From above example , we should wrap img with `<div>` so that flex layout will keep up its element layout. if we use `img` as is , it might behave wired as `img` is a inline element

Exercise solution video : https://player.vimeo.com/video/560002573
Soluton code :
```css
main {
  display: flex;
  gap: 32px 0;
  flex-wrap: wrap;
}

.image-wrapper, .reviews {
  flex: 1;
}

.image-wrapper img {
  width: 100%;
  min-width: 300px;
  object-position: -32px 0;
}

/* Everything else unchanged */
<main>
  <div class="image-wrapper">
    <img
      alt=""
      class="book-img"
      src="https://courses.joshwcomeau.com/cfj-mats/whispering-owl.png"
    />
  </div>
  <div class="reviews">
    <!-- Reviews unchanged -->
  </div>
</main>
```
# Aspect Ratio

As we saw earlier, images have an _intrinsic_ aspect ratio. We can see this in action by passing the exact same CSS to images with different intrinsic ratios:
What if we wanted  all images to have the same aspect ratio? We could accomplish this by giving them all the same width and height, and using `object-fit` to avoid stretching:
```css
img {
  width: 200px;
  height: 200px;
  object-fit: cover;
}
```
This is handy — we can tweak the `width` and `height` to change the effective aspect ratio for all images.

But what if we _don't know_ the specific pixel size? Maybe our images use a percentage-based width. Or, the image will grow and shrink inside a Flex container.

How can we scale our images proportionally, at a prescribed aspect ratio?
We can do that with the help of a brand-new property, `aspect-ratio`:
```css
<style>
  img {
    width: 30%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
  }
</style>

<section>
  <img
    alt="A wide-open outdoor concrete area. Architecture"
    src="https://courses.joshwcomeau.com/cfj-mats/architecture-hugo-sousa.jpg"
  />
  <img
    alt="A modular building against a blue sky. Architecture"
    src="https://courses.joshwcomeau.com/cfj-mats/architecture-joel-filipe.jpg"
  />
  <img
    alt="A unique building with inset curves. Architecture"
    src="https://courses.joshwcomeau.com/cfj-mats/architecture-julien-moreau.jpg"
  />
</section>
```
The `aspect-ratio` property takes two slash-separated numbers, like `4 / 3` or `7 / 11`. This is a ratio of width to height; an aspect ratio of `2 / 1` means that the image will be twice as wide as it is tall.

**This new feature is huge.** It allows us to auto-calculate the height of an element based on its dynamic width, whether that's a percentage or a flex-grow ratio.

Here's another example, using Flexbox. Try changing the `aspect-ratio` to see how nifty it is!
```css
<style>
  section {
    display: flex;
    gap: 8px;
  }
  .image-wrapper {
    flex: 1;
  }
  img {
    display: block;
    width: 100%;
    aspect-ratio: 3 / 2;
    object-fit: cover;
  }
</style>

<section>
  <div class="image-wrapper">
    <img
      alt="A wide-open outdoor concrete area. Architecture"
      src="https://courses.joshwcomeau.com/cfj-mats/architecture-hugo-sousa.jpg"
    />
  </div>
  <div class="image-wrapper">
  <img
    alt="A modular building against a blue sky. Architecture"
    src="https://courses.joshwcomeau.com/cfj-mats/architecture-joel-filipe.jpg"
  />
  </div>
  <div class="image-wrapper">
  <img
    alt="A unique building with inset curves. Architecture"
    src="https://courses.joshwcomeau.com/cfj-mats/architecture-julien-moreau.jpg"
  />
  </div>
</section>
```
## Padding fallback

The `aspect-ratio` has [very solid browser support](https://caniuse.com/mdn-css_properties_aspect-ratio) nowadays, but it'll never be supported in Internet Explorer. If we want to support _all_ browsers, we can rely on an old hack using `padding-bottom`.

Here's what the code looks like:
```css
<style>
  .image-wrapper {
    flex: 1;
  }
  .padding-hack {
    height: 0px;
    padding-bottom: 100%;
    position: relative;
  }
  img {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
</style>
```
What the heck is going on here?
If we inspect it in the developer tools, we're given a bit of a hint:
![[Screenshot 2023-12-20 at 9.10.04 AM.png]]

The `.padding-hack` element has been given a height of `0px`, so its content box is 228px by 0px. But the resulting image is square, because it has 228px of bottom padding, exactly the same amount as the width.

#ImportantPoint 
As we saw [in Module 1](https://courses.joshwcomeau.com/css-for-js/01-rendering-logic-1/05-padding#units), **percentages in padding always refer to width.** When we set `padding-bottom: 50%`, for example, we're saying that the element's bottom padding should be half of its width. Not its height.

So by combining 0px height with a percentage-based `padding-bottom`, we can recreate any aspect ratio:

We can solve that with _absolute positioning_. The `.padding-hack` element becomes a containing block with `position: relative`. Our image uses absolute positioning to take it out of flow and fill that containing block.

This fallback approach is a pain. It's hacky and it pollutes our markup. Is there an alternative?
## Progressive enhancement

In most cases, the `aspect-ratio` property is used to add a bit of visual polish, for presentational purposes. It isn't usually required for functionality.

Given that _most_ browsers support it, it's reasonable to ask: can we start using it, and provide a different-but-still-good alternative experience, for those using unsupported browsers?

I think so. Here's one way to do this:
```css
<style>
section {
  display: flex;
  gap: 8px;
}
.image-wrapper {
  flex: 1;
}
  img {
    width: 100%;
    height: 200px;
    object-fit: cover;
  }

  @supports (aspect-ratio: 1 / 1) {
    img {
      height: revert;
      aspect-ratio: 1 / 1;
    }
  }
</style>

<section>
  <div class="image-wrapper">
    <img
      alt="A wide-open outdoor concrete area. Architecture"
      src="https://courses.joshwcomeau.com/cfj-mats/architecture-hugo-sousa.jpg"
    />
  </div>
  <div class="image-wrapper">
    <img
      alt="A modular building against a blue sky. Architecture"
      src="https://courses.joshwcomeau.com/cfj-mats/architecture-joel-filipe.jpg"
    />
  </div>
  <div class="image-wrapper">
    <img
      alt="A unique building with inset curves. Architecture"
      src="https://courses.joshwcomeau.com/cfj-mats/architecture-julien-moreau.jpg"
    />
  </div>
</section>
```
On supported browsers, our images will all scale as squares.On unsupported browsers, a fixed 200px height will be used instead.

`@supports` is known as a _feature query_. It works just like a media query, but instead of targeting specific window sizes, it targets support for specific CSS declarations. We'll learn more about feature queries [in the next module](https://courses.joshwcomeau.com/css-for-js/07-css-grid/03-browser-support#progressive-enhancement-with-feature-queries)

# Responsive Images

As we learned in Module 5, modern screens come in all sorts of configurations and densities. A new iPhone has a 3-to-1 ratio between hardware and software pixels. These are known as "high-DPI" displays.

If we render an image at its native size, it's going to be fuzzy on a high-DPI display. To keep things crisp, we need to serve different images depending on the screen's pixel ratio.

When exporting assets from the design tool, it's common to export 2 or 3 versions of the image. The ratio is generally included in the filename, like this:

- `cat.jpg` (300 × 300)
- `cat@2x.jpg` (600 × 600)
- `cat@3x.jpg` (900 × 900)
Let's talk about how we can use those assets properly.

**Image components(info)**
Image optimization is a _huge_ topic, and we're only going to scratch the surface of it in this course.

If you use a meta-framework like Gatsby or Next, there's some good news: these tools come with battle-tested Image components that implement all the hard stuff for you:
- [next/image](https://nextjs.org/docs/api-reference/next/image)
- [gatsby-image](https://www.gatsbyjs.com/plugins/gatsby-image/)

These packages offer a ton of neat features out-of-the-box:
1. They create high-res variants and apply them automatically (the topic of this lesson)
2. They automatically generate and use next-gen image formats like .webp and .avif, gracefully falling back to jpg/png on unsupported browsers.
3. They implement lazy-loading, and some of them even support special effects, like embedding an SVG outline into the page whilst the image loads
Unfortunately, to accomplish these goals, the framework needs to integrate with your build system, which is why you won't find these features built straight into React or Vue.

If you're interested in learning more about image optimization, I strongly recommend Addy Osmani's insightful book, [Image Optimization](https://www.smashingmagazine.com/printed-books/image-optimization/).
## The srcset attribute

The quickest way to get up and running with responsive images is to use the `srcset` HTML attribute:
```html
<img
  alt=""
  src="https://courses.joshwcomeau.com/cfj-mats/responsive-diamond.png"
  srcset="
    https://courses.joshwcomeau.com/cfj-mats/responsive-diamond.png 1x,
    https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@2x.png 2x,
    https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@3x.png 3x
  "
/>
```
We keep a redundant `src` property strictly for older browsers: `srcset` enjoys [universal browser support](https://caniuse.com/srcset) amongst modern browsers, but the `src` attribute ensures that IE users will still see our images.

To help debug, the browser devtools will let you know which source is currently being served if you hover over the URL in the _Elements_ pane:

**camelCase in JSX(warning)**
React expects all HTML attributes to be camelCase. This means that this attribute should be written as `srcSet`, not `srcset`.
If you forget, a helpful console warning will let you know.
## The picture element

There's another way to solve the same problem: the `<picture>` element!
Here's what that looks like:
```html
<picture>
  <source
    srcset="
      https://courses.joshwcomeau.com/cfj-mats/responsive-diamond.png 1x,
      https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@2x.png 2x,
      https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@3x.png 3x
    "
  />
  <img
    alt=""
    src="https://courses.joshwcomeau.com/cfj-mats/responsive-diamond.png"
  />
</picture>
```
Structurally, this looks pretty similar to our `srcset` solution. We've essentially moved the `srcset` solution to a new `<source>` element, and wrapped the whole thing in a `<picture>`.

The benefit to this approach is that we can specify _multiple sources_. This allows us to supply different file formats:
```html
<picture>
  <source
    type="image/avif"
    srcset="
      https://courses.joshwcomeau.com/cfj-mats/responsive-diamond.avif 1x,
      https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@2x.avif 2x,
      https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@3x.avif 3x
    "
  />
  <source
    type="image/webp"
    srcset="
      https://courses.joshwcomeau.com/cfj-mats/responsive-diamond.webp 1x,
      https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@2x.webp 2x,
      https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@3x.webp 3x
    "
  />
  <img
    alt=""
    src="https://courses.joshwcomeau.com/cfj-mats/responsive-diamond.png"
  />
</picture>
```
If you're not familiar, AVIF is a fascinating new image format. It's based on the lessons learned in video compression, and it creates dramatically smaller images; in this example, the `.avif` version of our 3x image is 75% smaller than the `.png`!

At the time of writing, only Chrome, Firefox, and Opera support AVIF. If we tried to use an AVIF image in an `<img>` tag, it would render as a broken image icon in other browsers.

`<picture>` allows us to use modern image formats in a safe way, by providing fallbacks for other browsers.

When the browser encounters a `<picture>` tag, it scans through the `<source>` children, and the individual paths within `srcset`. **The order matters:** When the browser finds a match, it will download the image from the server and show it to the user. We want our smallest files (AVIF) to be on top.

Here are some resources, if you're interested in learning more about modern image formats, or using them in your applications:

- [“AVIF Has Landed”](https://jakearchibald.com/2020/avif-has-landed/), an introductory article by Jake Archibald.
- [Squoosh](https://squoosh.app/), a webapp created by Google to allow comparison and conversion between modern image formats.
- [“Embracing Modern Image Formats”](https://www.joshwcomeau.com/performance/embracing-modern-image-formats/), by yours truly!

**Why so funky?(info)**

The `<picture>` element has been rightly criticized for being overly complex. Why does it need to have a nested `<img>` tag? Can't it just be its own thing?

In fact, there's a very good reason for the bewildering structure: backwards-compatibility.
HTML is an incredibly forgiving language. If it sees an element that it doesn't recognize, it treats it like a `<div>` and moves on. If we were to view the above code in a legacy browser, it would be interpreted as this:
```css
<div>
  <div></div>
  <div></div>
  <img
    alt=""
    src="https://courses.joshwcomeau.com/cfj-mats/responsive-diamond.png"
  />
</div>
```
Buried inside our modern `<picture>` element is a plain ol' `<img>` tag. It may not be the most optimal format or size, but that's way better than not having an image at all.

Nowadays, `<picture>` is [widely supported across all major browsers](https://caniuse.com/picture)
### Styling and targeting picture elements

Because `<picture>` breaks what was a single element (`img`) into multiple elements (`picture`, `source`, `img`), it may not be clear how to style it.

First, we should ignore `<source>` tags from a styling perspective. They're essentially metadata: they aren't visible, and shouldn't be targeted.

Next, it's important to understand that no matter which source is selected, the `<img>` tag will always be used, and it acts like any other image tag. The sources exist to "swap out" the `src` attribute. We want to add additional properties, like alt text, to the `<img>` tag, and not to `<picture>` or `<source>`.

Finally, the `<picture>` element behaves like a `<span>`, an inline wrapper that wraps around the `<img>` tag
This `<picture>` wrapper comes in handy. For example, we can use it to our advantage inside a Flex container:
```css
<styles>
main {
  display: flex;
  gap: 8px;
}

picture {
  flex: 1;
  padding: 8px;
  border: 2px solid;
}

picture img {
  display: block;
  width: 100%;
}

p {
  flex: 2;
  border: 2px solid;
}
</styles>
<main>
  <picture>
    <source
      srcset="https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@2x.png 2x"
    />
    <source
      srcset="https://courses.joshwcomeau.com/cfj-mats/responsive-diamond@3x.png 3x"
    />
    <img
      alt=""
      src="https://courses.joshwcomeau.com/cfj-mats/responsive-diamond.png"
    />
  </picture>
  <p>Hello World</p>
</main>
```
## Deciding which to use

There's no doubt about it: the `<picture>` element can do some pretty cool stuff. We've only scratched the surface!

It can also add quite a bit of friction to our work, however. If we want to support 3 media types and 3 device pixel ratios, we need to generate 9 images for every image! This can be very tedious if you don't have a process to do it automatically.

You'll need to find the right balance for you and your team.

As mentioned at the start of this article, there are projects that exist to solve these problems for you, things like [next/image](https://nextjs.org/docs/api-reference/next/image) and [gatsby-image](https://www.gatsbyjs.com/plugins/gatsby-image/). They do have some tradeoffs of their own, but they can reduce a lot of the associated friction.

# Background Images

As CSS has evolved, the `<img>` tag has grown much more flexible and powerful, but there's one thing that it can't do: tile the image. When we have a repeating pattern, we'll need to use a CSS background image instead.
Let's look at an example:
```css
<style>
  body {
    background-image:
      url('https://courses.joshwcomeau.com/cfj-mats/geometric-pattern.png');
  }
  main {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
h1 {
  font-size: 2rem;
}
body {
  margin: 0;
  padding: 0;
}
</style>

<main>
  <h1>Hello World</h1>
</main>
```
By default, a background image will be rendered at its native size, and then tiled across the element.

There's a problem with this, though. As we've discussed, most monitors are "high DPI". If we render an image at its natural size, it'll look blurry and fuzzy, since a single software pixel is being stretched across multiple hardware pixels.

To keep things crisp, we'll need to provide different images for different devices, scaling up based on the pixel ratio. When it comes to background images, we can do this with a media query, `min-resolution`:
```css
<style>
  body {
    background-image:
      url('https://courses.joshwcomeau.com/cfj-mats/geometric-pattern.png');
    background-size: 450px;
  }
  
  @media
    (-webkit-min-device-pixel-ratio: 2),
    (min-resolution: 2dppx)
  {
    body {
      background-image:
        url('https://courses.joshwcomeau.com/cfj-mats/geometric-pattern@2x.png');
    }
  }
  
  @media
    (-webkit-min-device-pixel-ratio: 3),
    (min-resolution: 3dppx)
  {
    body {
      background-image:
        url('https://courses.joshwcomeau.com/cfj-mats/geometric-pattern@3x.png');
    }
  }
  main {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
h1 {
  font-size: 2rem;
}
body {
  margin: 0;
  padding: 0;
}
</style>

<main>
  <h1>Hello World</h1>
</main>
```
`min-resolution` is supported across all major browsers except Safari. We can support Safari with an alternative syntax, `-webkit-min-device-pixel-ratio`.

Notice that we also need to specify a `background-size` in pixels; otherwise, our high-DPI images will render in their native size, producing much larger images without any additional clarity. The `background-size` should match the width of the standard 1x image.
## Fit and positioning

The `background-size` property also accepts certain keyword values, just like `object-fit`. For example, we can choose to have our background image cover the element.
In fact, the `object-fit` property was inspired by `background-size`. It was added to the specification when the authors realized that developers were using background images instead of `<img>` tags specifically for the `background-size` property.

There's also `background-position`, which works just like `object-position`.
## Background repeat

By default, the background image will be tiled side-by-side, top-to-bottom. In most cases, this is fine, but it does mean that the pattern will be truncated at the bottom and on the right.

The `background-repeat` property allows us to tweak this algorithm. There are two additional options that can be used:
```css
<style>
  .demo {
    margin-bottom: 32px;
    margin-top: 16px;
    height: 175px;
    background-size: 75px 75px;
    background-repeat: repeat;
    background-color: hsl(220deg 100% 50%);
    background-image: url('https://courses.joshwcomeau.com/cfj-mats/yellow-circle.svg')
  }

  .space {
    background-repeat: space;
  }

  .round {
    background-repeat: round;
  }
</style>

<h2>Background-repeat: repeat</h2> (default)
<div class="demo"></div>

<h2>Background-repeat: round</h2>
<div class="demo round"></div>

<h2>Background-repeat: space</h2>
<div class="demo space"></div>
```
`round` will scale the image up or down, to avoid having the image cut off at the bottom or the right. It preserves the aspect ratio.

`space` won't tweak the size of the image. Instead, it'll leave gaps between the images.

## Generative backgrounds

In addition to accepting the URL to an image file, the `background-image` property also accepts gradients.

We'll explore gradients more in a future module, but I wanted to share this neat resource: pure-CSS background patterns, generated using very-clever gradients.

- [“Magic Pattern” CSS background patterns](https://www.magicpattern.design/tools/css-backgrounds)
# Workshop: Unsprinkle

In this workshop, we're going to apply what we've learned about typography and images to improve the performance, accessibility, and UX of an existing web application.

Our application is called Unsprinkle, a photo-sharing website:
## Resources

Grab the starter code from Github:
- [github.com/css-for-js/unsprinkle](https://github.com/css-for-js/unsprinkle)

You'll find step-by-step instructions in the workshop's `README.md`.

No design is provided, as the application is complete from a design perspective. Our focus is on optimization.

This workshop is on the shorter end, but jam-packed with actionable lessons and little nuggets. Have fun!

# Exercise-1: Optimise fonts
Solution video : https://player.vimeo.com/video/558765211
Solution code : [View the code on Github](https://github.com/css-for-js/unsprinkle/commit/9204dfb87c54e31590e933ef0cbfc0de845f775e)
## Exercise 2: Improve images
Solution video : https://player.vimeo.com/video/558766353
Solution code : [View the code on Github](https://github.com/css-for-js/unsprinkle/commit/01e20e39ed3ca75eac7c1a814d305685756fecf2)
## Exercise 3: Accessibility issues
Solution video : https://player.vimeo.com/video/558777828
Solution code : [View the code on Github](https://github.com/css-for-js/unsprinkle/commit/892e7637d397f6ec8e95e2b6540a8b11af9b88ae)
From above video `wave` tool will help to analyse the webpage for accessibility issues
## Exercise 4: Tag overflow
Solution Video : https://player.vimeo.com/video/558765730
Solution Code : [View the code on Github](https://github.com/css-for-js/unsprinkle/commit/deda6d43177d98804be9a8103de98c87ce366b61)


























