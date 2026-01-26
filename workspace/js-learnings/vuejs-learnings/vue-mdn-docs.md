[source](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_getting_started)
[Also refer](https://www.youtube.com/watch?v=FXpIoQ_rT_c)

Vue is a modern JavaScript framework that provides useful facilities for progressive enhancement — unlike many other frameworks, you can use Vue to enhance existing HTML. This lets you use Vue as a drop-in replacement for a library like jquery

Vue allows you to take advantage of libraries for client-side routing and state management when you need to. Additionally, Vue takes a "middle ground" approach to tooling like client-side routing and state management. While the Vue core team maintains suggested libraries for these functions, they are not directly bundled into Vue. This allows you to select a different routing/state management library if they better fit your application.
 Most of the time, Vue components are written using a special HTML template syntax. When you need more control than the HTML syntax allows, you can write JSX or plain JavaScript functions to define your components.

## [Installation](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_getting_started#installation)

To use Vue in an existing site, you can drop one of the following [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) elements onto a page. This allows you to start using Vue on existing sites, which is why Vue prides itself on being a progressive framework. This is a great option when migrating an existing project using a library like jQuery to Vue. With this method, you can use a lot of the core features of Vue, such as the attributes, custom components, and data-management.

- Development Script (not optimized, but includes console warnings which is great for development.)
    
    HTMLCopy to Clipboard
    
    ```html
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    ```
- Production Script (Optimized version, minimal console warnings. It is recommended that you specify a version number when including Vue on your site so that any framework updates do not break your live site without you knowing.)
    
    HTMLCopy to Clipboard
    
    ```
    <script src="https://unpkg.com/vue@3/dist/vue.global.prod.js"></script>
    ```
However, this approach has some limitations. To build more complex apps, you'll want to use the [Vue npm package](https://www.npmjs.com/package/vue). This will let you use advanced features of Vue and take advantage of bundlers like WebPack. To make building apps with Vue easier, there is a CLI to streamline the development process.

To install the CLI, run the following command in your terminal:
```sh
npm install --global @vue/cli
```
Once installed, to initialize a new project you can then open a terminal in the directory you want to create the project in, and run `vue create <project-name>`. The CLI will then give you a list of project configurations you can use. There are a few preset ones, and you can make your own. These options let you configure things like TypeScript, linting, vue-router, testing, and more.

We'll look at using this below.

## [Initializing a new project](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_getting_started#initializing_a_new_project)

The Vue CLI will default to this package manager from now on. If you need to use a different package manager after this, you can pass in a flag `--packageManager=<package-manager>`, when you run `vue create`. So if you wanted to create the `moz-todo-vue` project with npm and you'd previously chosen yarn, you'd run `vue create moz-todo-vue --packageManager=npm`.
## Project structure
If everything went successfully, the CLI should have created a series of files and directories for your project. The most significant ones are as follows:

- `package.json`: This file contains the list of dependencies for your project, as well as some metadata and `eslint` configuration.
- `yarn.lock`: If you chose `yarn` as your package manager, this file will be generated with a list of all the dependencies and sub-dependencies that your project needs.
- `babel.config.js`: This is the config file for [Babel](https://babeljs.io/), which transforms modern JavaScript features being used in development code into older syntax that is more cross-browser compatible in production code. You can register additional babel plugins in this file.
- `jsconfig.json`: This is a config file for [Visual Studio Code](https://code.visualstudio.com/docs/languages/jsconfig) and gives context for VS Code on your project structure and assists auto-completion.
- `public`: This directory contains static assets that are published, but not processed by [Webpack](https://webpack.js.org/) during build (with one exception; `index.html` gets some processing).
    - `favicon.ico`: This is the favicon for your app. Currently, it's the Vue logo.
    - `index.html`: This is the template for your app. Your Vue app is run from this HTML page, and you can use lodash template syntax to interpolate values into it.
- `src`: This directory contains the core of your Vue app.
    - `main.js`: this is the entry point to your application. Currently, this file initializes your Vue application and signifies which HTML element in the `index.html` file your app should be attached to. This file is often where you register global components or additional Vue libraries.
    - `App.vue`: this is the top-level component in your Vue app. See below for more explanation of Vue components.
    - `components`: this directory is where you keep your components. Currently, it just has one example component.
    - `assets`: this directory is for storing static assets like CSS and images. Because these files are in the source directory, they can be processed by Webpack. This means you can use pre-processors like [Sass/SCSS](https://sass-lang.com/) or [Stylus](https://stylus-lang.com/).
**Note:** Depending on the options you select when creating a new project, there might be other directories present (for example, if you choose a router, you will also have a `views` directory).

## [.vue files (single file components)](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_getting_started#.vue_files_single_file_components)

Like in many front-end frameworks, components are a central part of building apps in Vue. These components let you break a large application into discrete building blocks that can be created and managed separately, and transfer data between each other as required. These small blocks can help you reason about and test your code.

While some frameworks encourage you to separate your template, logic, and styling code into separate files, Vue takes the opposite approach. Using [Single File Components (SFC)](https://vuejs.org/guide/scaling-up/sfc.html), Vue lets you group your templates, corresponding script, and CSS all together in a single file ending in `.vue`. These files are processed by a JS build tool (such as Webpack), which means you can take advantage of build-time tooling in your project. This allows you to use tools like Babel, TypeScript, SCSS and more to create more sophisticated components.

As a bonus, projects created with the Vue CLI are configured to use `.vue` files with Webpack out of the box. In fact, if you look inside the `src` folder in the project we created with the CLI, you'll see your first `.vue` file: `App.vue`.

Let's explore this now.
### [App.vue](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_getting_started#app.vue)

Open your `App.vue` file — you'll see that it has three parts: `<template>`, `<script>`, and `<style>`, which contain the component's template, scripting, and styling information. All Single File Components share this same basic structure.

`<template>` contains all the markup structure and display logic of your component. Your template can contain any valid HTML, as well as some Vue-specific syntax that we'll cover later.
>**Note:** By setting the `lang` attribute on the `<template>` tag, you can use Pug template syntax instead of standard HTML — `<template lang="pug">`. We'll stick to standard HTML through this tutorial, but it is worth knowing that this is possible.

`<script>` contains all of the non-display logic of your component. Most importantly, your `<script>` tag needs to have a default exported JS object. This object is where you locally register components, define component inputs (props), handle local state, define methods, and more. Your build step will process this object and transform it (with your template) into a Vue component with a `render()` function.

In the case of `App.vue`, our default export sets the name of the component to `App` and registers the `HelloWorld` component by adding it into the `components` property. When you register a component in this way, you're registering it locally. Locally registered components can only be used inside the components that register them, so you need to import and register them in every component file that uses them. This can be useful for bundle splitting/tree shaking since not every page in your app necessarily needs every component.

```js
import HelloWorld from "./components/HelloWorld.vue";

export default {
  name: "App",
  components: {
    //You can register components locally here.
    HelloWorld,
  },
};
```
> **Note:** If you want to use [TypeScript](https://www.typescriptlang.org/) syntax, you need to set the `lang` attribute on the `<script>` tag to signify to the compiler that you're using TypeScript — `<script lang="ts">`.

`<style>` is where you write your CSS for the component. If you add a `scoped` attribute — `<style scoped>` — Vue will scope the styles to the contents of your SFC. This works similar to CSS-in-JS solutions, but allows you to just write plain CSS.
>**Note:** If you select a CSS pre-processor when creating the project via the CLI, you can add a `lang` attribute to the `<style>` tag so that the contents can be processed by Webpack at build time. For example, `<style lang="scss">` will allow you to use SCSS syntax in your styling information.

## [Running the app locally](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_getting_started#running_the_app_locally)

The Vue CLI comes with a built-in development server. This allows you to run your app locally so you can test it easily without needing to configure a server yourself. The CLI adds a `serve` command to the project's `package.json` file as an npm script, so you can easily run it.

In your terminal, try running `npm run serve` (or `yarn serve` if you prefer yarn). Your terminal should output something like the following:

# Creating our first Vue component

 we'll start by creating a component to represent each item in the todo list. Along the way, we'll learn about a few important concepts such as calling components inside other components, passing data to them via props, and saving data state.
 >**_Note:_** If you need to check your code against our version, you can find a finished version of the sample Vue app code in our [todo-vue repository](https://github.com/mdn/todo-vue). For a running live version, see [https://mdn.github.io/todo-vue/](https://mdn.github.io/todo-vue/).
## [Creating a ToDoItem component](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Client-side_JavaScript_frameworks/Vue_first_component#creating_a_todoitem_component)

Let's create our first component, which will display a single todo item. We'll use this to build our list of todos.

1. In your `moz-todo-vue/src/components` directory, create a new file named `ToDoItem.vue`. Open the file in your code editor.
2. Create the component's template section by adding `<template></template>` to the top of the file.
3. Create a `<script></script>` section below your template section. Inside the `<script>` tags, add a default exported object `export default {}`, which is your component object.
 Your file should now look like this:
```js
<template></template>
<script>
export default {};
</script>
```
We can now begin to add actual content to our `ToDoItem`. Vue templates are currently only allowed a single root element — one element needs to wrap everything inside the template section (this will change when Vue 3 comes out). We'll use a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div) for that root element.
1. Add an empty `<div>` inside your component template now.
2. Inside that `<div>`, let's add a checkbox and a corresponding label. Add an `id` to the checkbox, and a `for` attribute mapping the checkbox to the label, as shown below.    
  ```js
    <template>
      <div>
        <input type="checkbox" id="todo-item" />
        <label for="todo-item">My Todo Item</label>
      </div>
    </template>
    ```
