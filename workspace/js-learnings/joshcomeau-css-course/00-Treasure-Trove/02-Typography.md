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












