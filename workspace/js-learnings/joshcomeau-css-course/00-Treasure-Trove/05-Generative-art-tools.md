It's become quite common on the web to use geometric abstract art to enhance the look/feel of a product.

For example, here's a design from [Vladimir Gruev on Dribbble](https://dribbble.com/shots/14953088-spark-marketing-page):
The word “generative” refers to the fact that the art is algorithmically-generated. Instead of an artist carefully choosing the size and position of each shape, the artist writes an algorithm which randomly distributes them according to parameters. Often, these parameters can be tweaked to affect the resulting art.

Generative art is a lot of fun to create, but like any artistic endeavour, it takes years to develop the skillset. Fortunately, we can take advantage of online tools to help generate some art for us!

## Generative tools

### Tabbied

[Tabbied](https://tabbied.com/select-artwork) is a suite of generative art tools. For example, I created the hero art for this page using the “Blossom” tool:

While I wasn't able to find an explicit license for Tabbied art, their copy suggests that the art can be used for any purpose, including commercial purposes.

The only downside about Tabbied is that their tools export to .png, a raster image format. I would prefer if it exported to .svg, a vector format, but ultimately the art produced is still very useful.

Try them all out here: [tabbied.com/select-artwork](https://tabbied.com/select-artwork)

### Haikei

[Haikei](https://app.haikei.app/) is a webapp that bundles up 15 different generative algorithms:

Haikei offers SVG downloads, and is currently free-to-use, though it does seem as though this tool might soon become a paid service.

Check it out here: [app.haikei.app](https://app.haikei.app/)

### Magic Pattern

[Magic Pattern](https://www.magicpattern.design/tools/css-backgrounds) is a set of generative background gradients that can be used to create patterns and textures.

Remarkably, each texture is created using a set of CSS gradients. Instead of loading an image, the pattern is created in CSS.

Additionally, Magic Pattern also offers additional tools, similar to the ones provided by Haikei or Tabbied. These additional tools require a subscription, but it's priced very fairly.

Check it out here: [magicpattern.design](https://www.magicpattern.design/tools/css-backgrounds)

### Tinkersynth

[Tinkersynth](https://tinkersynth.com/) is a generative art tool I created a few years ago

## Honourable mentions

Here are some additional tools that you might also find useful!

- [Patternico](https://patternico.com/), a tool to create seamless tiled patterns from icons or emoji.
    
- [Repper](https://repper.app/), a tool that can create patterns from any image.
    
- [Weave Silk](http://weavesilk.com/), a WebGL tool that creates futuristic sci-fi art through clicking and dragging.
    

## A word of caution

Generative tools like this are wonderful, because they allow us to create art assets without needing to spend months/years learning how to create art from scratch.

But it's not a magic bullet; these tools won't automatically make our sites look professional.

When an artist creates art for a project, they generally have a sense of what the project's aesthetic is. They can make sure that the art matches the site's pre-existing design.

It doesn't matter how beautiful individual assets are; if they're combined in an incongruous way, the overall effect will be negative, not positive.

These tools are a great tool to have in the toolbox, but you still need to build up a design intuition in order to use them effectively. I write a little bit about developing a design intuition in my blog post, [“Effective Collaboration with Product and Design”](https://www.joshwcomeau.com/career/effective-collaboration/).

## Yours to modify

For this page's cover image, I used the "Blossom" tool from Tabbied.

Notice, though, that the pattern only exists _on one half of the image_:

The art produced by the Blossom tool doesn't naturally produce this sort of arrangement. To create this cover image, I imported two separate outputs and manually positioned the geometry in Photoshop.

Rather than using the art from these tools "as-is", it can be worth thinking of them as inputs. They produce raw assets that can be sculpted and arranged into a suitable final product. Generative art leans heavily on randomness, which isn't always ideal. Don't be afraid to get your hands dirty!

To make these sorts of tweaks, you'll need some graphics editing software.

For raster images (png/jpg), I use [Photoshop](https://www.adobe.com/ca/products/photoshop.html), which is part of Adobe's paid Creative Cloud suite, but free alternatives exist, like [GIMP](https://www.gimp.org/). For vector images (svg), I use [Figma](http://figma.com/).

Learning to use graphics-editing software is an investment, but it's a really worthwhile one. And it's still a heck of a lot quicker than learning to create generative art from scratch!