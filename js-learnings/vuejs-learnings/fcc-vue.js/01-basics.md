[source-youtube-fcc](https://www.youtube.com/watch?v=8pn9KEuXG28)
- ref vs reactive -> to update values

### Vue Directives
Vue directives are special attributes within Vue.js that start with the `v-` prefix and provide enhanced functionality to HTML elements
- `v-bind`: 
    This directive dynamically binds an HTML attribute to a data property within your Vue instance. For example, `v-bind:href="url"` would bind the `href` attribute to a `url` data property. A shorthand for `v-bind` is using a colon, e.g., `:href="url"`.
- `v-if`, 
    `v-else-if`, and `v-else`: These directives are used for conditional rendering of elements. They work similarly to JavaScript's `if`, `else if`, and `else` statements, allowing you to display or hide elements based on a condition's truthiness.
- `v-show`: 
    This directive conditionally toggles the visibility of an element by manipulating its CSS `display` property. Unlike `v-if`, `v-show` always renders the element in the DOM and simply shows or hides it with CSS.
- `v-for`: 
    This directive is used to render a list of elements based on an array or iterable object in your Vue instance. It iterates over the data and generates a corresponding element for each item.
- `v-on`: 
    This directive attaches event listeners to HTML elements, allowing you to execute JavaScript expressions or methods from your Vue instance when a specific event occurs (e.g., `click`, `submit`, `input`). A shorthand for `v-on` is using an `@` symbol, e.g., `@click="myMethod"`.
- `v-model`: 
    Primarily used with form input elements, `v-model` creates a two-way data binding between an input element and a data property in your Vue instance. Changes in the input element automatically update the data property, and vice-versa.
- `v-cloak`: 
    This directive is used to hide uncompiled template content, such as mustache interpolations (e.g., `{{ message }}`), until the Vue instance has finished compiling the template, preventing a "flicker" effect during page load.
