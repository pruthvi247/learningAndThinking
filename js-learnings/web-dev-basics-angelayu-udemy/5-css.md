Adding css
- inline `< tag style="css" />`
- internal `< style > css </ style >`
- External `<link rel="stylesheet" href="style.css"/>`


---------------------
## CSS Selectors [](https://www.w3schools.com/css/css_selectors.asp)

CSS selectors are used to "find" (or select) the HTML elements you want to style.

We can divide CSS selectors into five categories:

- Simple selectors (select elements based on name, id, class)
- [Combinator selectors](https://www.w3schools.com/css/css_combinators.asp) (select elements based on a specific relationship between them)
- [Pseudo-class selectors](https://www.w3schools.com/css/css_pseudo_classes.asp) (select elements based on a certain state)
- [Pseudo-elements selectors](https://www.w3schools.com/css/css_pseudo_elements.asp) (select and style a part of an element)
- [Attribute selectors](https://www.w3schools.com/css/css_attribute_selectors.asp) (select elements based on an attribute or attribute value)

------------------------------------------


# Css selectors
```html
<!DOCTYPE html>
<html>
<head>
<style>
p {
  text-align: center;
  color: blue;
} 
</style>
</head>
<body>

<p>Every paragraph will be affected by the style.</p>
<p id="para1">Me too!</p>
<p>And me!</p>

</body>
</html>
```

> above code changes color to blue for all < p>  tags

## Id selector
```html
<!DOCTYPE html>
<html>
<head>
<style>
#para1 {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<p id="para1">Hello World!</p>
<p>This paragraph is not affected by the style.</p>

</body>
</html>


```

The id of an element is unique within a page, so the id selector is used to select one unique element!

To select an element with a specific id, write a hash (#) character, followed by the id of the element.

## Class selector
```html
<!DOCTYPE html>
<html>
<head>
<style>
.center {
  text-align: center;
  color: red;
}
</style>
</head>
<body>

<h1 class="center">Red and center-aligned heading</h1>
<p class="Large">Red and Large center-aligned paragraph.</p> 

</body>
</html>

```
> HTML elements can also refer to more than one class.

In this example the < p> element will be styled according to class="center" and to class="large": 
```html
<p class="center large">This paragraph refers to two classes.</p>
```

## Attribute selector
```html
<!DOCTYPE html>
<html>
<head>
<style>
a[target] {
  background-color: yellow;
}
a[target="_top"] {
  background-color: green;
}
</style>
</head>
<body>

<h2>CSS [attribute] Selector</h2>
<p>The links with a target attribute gets a yellow background:</p>

<a href="https://www.w3schools.com">w3schools.com</a>
<a href="http://www.disney.com" target="_blank">disney.com</a>
<a href="http://www.wikipedia.org" target="_top">wikipedia.org</a>

</body>
</html>
```


### CSS [attribute~="value"] Selector

The `[attribute~="value"]` selector is used to select elements with an attribute value containing a specified word.

The following example selects all elements with a title attribute that contains a space-separated list of words, one of which is "flower":


```html
<!DOCTYPE html>
<html>
<head>
<style>
[title~="flower"] {
  border: 5px solid yellow;
}
</style>
</head>
<body>

<h2>CSS [attribute~="value"] Selector</h2>
<p>All images with the title attribute containing the word "flower" get a yellow border.</p>

<img src="klematis.jpg" title="klematis flower" width="150" height="113">
<img src="img_flwr.gif" title="flower" width="224" height="162">
<img src="img_tree.gif" title="tree" width="200" height="358">

</body>
</html>
```

### CSS [attribute|="value"] Selector

The `[attribute|="value"]` selector is used to select elements with the specified attribute, whose value can be exactly the specified value, or the specified value followed by a hyphen (-).

**Note:** The value has to be a whole word, either alone, like class="top", or followed by a hyphen( - ), like class="top-text".

### CSS [attribute^="value"] Selector

The `[attribute^="value"]` selector is used to select elements with the specified attribute, whose value starts with the specified value.

The following example selects all elements with a class attribute value that starts with "top":

**Note:** The value does not have to be a whole word!

### CSS [attribute$="value"] Selector

The `[attribute$="value"]` selector is used to select elements whose attribute value ends with a specified value.

The following example selects all elements with a class attribute value that ends with "test":

**Note:** The value does not have to be a whole word!

### CSS [attribute*="value"] Selector

The `[attribute*="value"]` selector is used to select elements whose attribute value contains a specified value.

The following example selects all elements with a class attribute value that contains "te":

**Note:** The value does not have to be a whole word!


## Universal Selector
The universal selector (*) selects all HTML elements on the page.
```html
* {  text-align: center;  
  color: blue;}
```