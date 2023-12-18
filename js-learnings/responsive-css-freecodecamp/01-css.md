# units
## Absolute units
- px
- cm,pt,mm
## Percentages
Are mainly used for widths 
- Relative to parent (Except heights, these work weird)
## Relative units
- Relative to font
- Relative to view port

### Relative to font
**em**
- em and rem(many other are less common )
- em and rem are called relative because , they are relative to other elements font size
- `em` is relative to their parent
- Font size is inherited property, so if you don't declared it will get it  from body or default value  which is normally 16px
#### Problem with `em`
Because its relative to parent, if you have hierarchy of elements then 1.5em can be different for different elements based on their parent element size

**rem**
- rem is the short for Root em
- That means its alway relative to root element
- Root of html is always html element

#### Rule of thumb
- Font size -> rem
- padding and margin -> em
- width  -> em or percentage
- 
### Relative to view port
- vw, vh,vmin,vmax
``
# Basic of flexbox
 **Demo page**
 ```css
 img {
  max-width: 100%;
}
body {
  font-size: 1.125rem;
  color: #707070;
  margin: 0;
}
header {
  background: purple;
  padding: 45px 0;
  color: #fff;
  text-align: center;
}
h1 {
  color: #212614;
  font-size: 3rem;
  text-align: center;
}
h2 {
  color: #212614;
  font-size: 1.5rem;
}
p {
  margin-top: 0;
}
span {
  color: purple;
}
/*layout*/
.container {
  /* background-color: aqua; */
  max-width: 980px;
  margin: 0 auto;
  width: 90%;
}
.columns {
  display: flex;
  margin: 1em 0;
  /* flex-wrap: inherit; */
  justify-content: space-evenly;
  align-items: flex-center;
}
.col-bg {
  background-color: #212614;
  padding: 1em;
  color: #fff;
}
.col-1 {
  width: 25%;
}
.col-2 {
  width: 50%;
}
.col-3 {
  width: 75%;
}
@media (max-width: 600px) {
  .columns {
    /* width: 50%; */
    /* width: 620px; */
    flex-direction: column;
    /* max-width: 600px;
    margin: 0 auto;
    padding: 0 15px;
    border: 2px solid magenta; */
  }
}

@media (max-width: 600px) {
  .col-1,
  .col-2,
  .col-3 {
    width: 100%;
    /* width: 620px; */
    flex-direction: column;
    /* max-width: 600px;
    margin: 0 auto;
    padding: 0 15px;
    border: 2px solid magenta; */
  }
}

nav ul {
  /*header*/
  background: #2e354f;
  padding: 45px 0;
  color: #fff;
  text-align: center;
  margin: 0;
  display: flex;
  justify-content: space-evenly;
  /* width: 500px; */
  /* height: 100%; */
}
nav ul li {
  display: inline-block;
  margin: 0 1em;
}
nav ul li a {
  text-decoration: none;
  color: #fff;
}
nav ul li a:hover,
a:focus {
  color: #707070;
}

.current-page {
  border-bottom: 1px solid #fff;
}
.current-page:hover {
  color: #fff;
}
@media screen and (max-width: 600px) {
  nav ul {
    flex-direction: column;
  }
  nav ul li {
    /* display: block; */
    margin: 0;
  }
}


```

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=, initial-scale=1" />
    <link rel="stylesheet" href="../css/flex-freecodecamp.css" />
    <title>css is fu title</title>
  </head>
  <body>
    <header>
          <div class="site-title">
            <h1></h1>
            <p class="subtitle">Navigating page</p>
          </div>
          <nav>
            <ul>
              <li><a href="#" class="current-page">Home</a></li>
              <li><a href="#">About me</a></li>
              <li><a href="#">Recent posts</a></li>
            </ul>
          </nav>
    </header>
    <div class="container">
      <h1>Lets start <span>getting little </span>more fancy </h1>
      <img src="../documents/img/batman.png" alt="Student image" />
      <div class="columns">
        <div class="col col-1">
          <h2>Dolor sit</h2>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Atque, reprehenderit consequatur ullam illo praesentium voluptatem nihil hic molestias et enim a earum corrupti, delectus, aperiam quasi facilis! Quidem, saepe velit! </p>
        </div>
        <div class="col col-2">
          <h2>consectetur adipiscing</h2>
          <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>
          <p>The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.</p>
        </div>
        <div class="col col-1 col-bg">
          <!-- <h2> </h2> -->
          
          <p>There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.</p>
        </div>
      </div>
      <div class="columns">
        <div class="col col-3">
          <h2>Deserunt mollit anim id est laborum</h2>
          <p>Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.</p>
        </div>
        <div class="col col-1 col-bg">
          <!-- <h2></h2> -->
          <p>It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).</p>
        </div>
      </div>
  </body>
</html>

```
# Media Queries- basics
This is the syntax for media queries:

```
@media type and (feature)
```
type and feature are optional, we should have either one of them.
More details : https://css-tricks.com/a-complete-guide-to-css-media-queries/
Example: 
```css
@media screen and (orientation: landscape) {
  body::after {
    content: "Landscape";
  }
}

@media screen and (orientation: portrait) {
  body::after {
    content: "Portrait";
  }
}

body {
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
  font-size: 10vmax;
}
```
## Adjust styles based on viewport size

For responsive design, one of the most useful media features involves the dimensions of the browser viewport. To apply styles when the browser window is wider than a certain width, use `min-width`.

```
@media (min-width: 400px) {  // Styles for viewports wider than 400 pixels.}
```
You can also combine media queries to apply more than one condition. Use the word `and` to combine your media queries:
```
@media (min-width: 50em) and (max-width: 60em) {  // Styles for viewports wider than 50em and narrower than 60em.}
```

# Second Exercise
[git source ](https://github.com/kevin-powell/reponsive-web-design-bootcamp/blob/master/Module%205%20-%20Social%20life%20with%20grid/css/styles.css)
```css
* {
  margin: 0;
  padding: 0;
}
body {
  margin: 0;
  font-family: "Ubuntu", sans-serif;
}
img {
  width: 90%;
}
h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: "Ubuntu", sans-serif;
  font-weight: 400;
  color: #143774;
  margin: 0;
}
h1 {
  color: #143774;
  font-size: 2rem;
  margin: 0;
}

/******* Layout *******/
.article-title {
  font-family: sans-serif;
}
.subtitle {
  font-weight: 700;
  color: #1792d2;
  font-size: 0.75rem;
  margin: 0;
}
.body-container {
  max-width: 1000px;
  margin: 0 auto;
  width: 100%;
}
.hero-container {
  width: 100%;
  /* max-width: 500px; */
  /* margin-left: 0%; */
  display: flex;
  justify-content: space-around;
}
.container-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 5%;
  margin-bottom: 5%;
  width: 100%;
}
.navigation-container {
  /* background-color: #1792d2; */
  width: 50%;
}

nav ul {
  list-style: none;
  padding: 0;
  display: flex;
  justify-content: space-between;
}
/* nav li {
  margin-left: 2rem;
} */
.sidebar {
  width: 100%;
  /* margin-left: 5%; */
}
.sidebar-widget {
  border: 20px solid #efefef;
  margin-bottom: 2em;
  padding: 1em;
}
/* .article-featured {
  height: 75%;
  border-bottom: 1px solid #143774;
} */
@media (max-width: 675px) {
  nav ul {
    flex-direction: column;
  }

  nav li {
    margin: 0.5em 0;
  }
}

.article-featured {
  border-bottom: #707070 1px solid;
  padding-bottom: 2em;
  margin-bottom: 2em;
}
.article-title {
  font-size: 1.5rem;
}
.article-read-more,
.article-info {
  font-size: 0.875rem;
}
.article-info {
  margin: 2em 0;
}
/* li:last-child {
  margin-left: 20%;
} */
@media (min-width: 675px) {
  .article-recent {
    flex-direction: row;
    justify-content: space-between;
  }

  .article-recent-main {
    width: 68%;
  }

  .article-recent-secondary {
    width: 30%;
  }

  .article-featured {
    display: flex;
    flex-direction: column;
  }

  .article-image {
    order: -2;
    min-height: 250px;
    object-fit: cover;
    /* object-position: left; */
  }

  .article-info {
    order: -1;
  }
}

@media (max-width: 675px) {
  header {
    text-align: left;
  }

  .container-flex {
    flex-direction: column;
  }

  main {
    width: 70%;
  }

  aside {
    width: 25%;
    min-width: 200px;
    margin-left: 1em;
  }
}

```

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=, initial-scale=1" />
  <link rel="stylesheet" href="../css/freecode-responsive.css" />
  <title>css is fu title</title>
</head>

<body class="body-container">
  <header>
    <div class="container-flex container-nav">
      <div class="site-title-container">
        <h1>Living social life</h1>
        <p class="subtitle">A blog exploring minimalism in life</p>
      </div>
      <div class="navigation-container">
        <nav>
          <ul>
            <li><a href="#"> Home</a></li>
            <li><a href="#"> About us</a></li>
            <li><a href="#"> Recent posts</a></li>
          </ul>
        </nav>
      </div>
    </div>
  </header>
  <div class="hero-container container-flex">
    <main role="main">
      <article class="article-featured">
        <img src="../documents/img/teenagers-at-desk.jpg" alt="featured image" class="article-image" />
        <p class="article-info">July 23,2019| 3 comments</p>
        <h2 class="article-title">Finding simplicity in life</h2>
        <p class="article-body">
          Life can get complicated really quickly,but it doesn't have to be! There are many ways to simplify your life,a
          few of which we've explored in the past.
        </p>
        <a href="#" class="article-read-more">Read more</a>
      </article>

      <article class="article-recent">
        <div class="article-recent-main">
          <h2 class="article-title">Keep cooking simple</h2>
          <p class="article-body"> Food is a very important part of everyone's life.If you want to be healthy, you have
            to eat healthy. One of the easiest ways to do that is to keep your cooking nice and simple.</p>
          <a href="#" class="article-read-more">Read more</a>
        </div>
        <div class="article-recent-secondary">
          <img src="../documents/img/teenagers-at-desk.jpg" alt="featured image" class="article-image" />
          <p class="article-info"></p>
        </div>
      </article>
    </main>
    <aside class="sidebar">
      <div class="sidebar-widget">
        <h3 class="sidebar-widget-title">About us</h3>
        <img src="../documents/img/teenagers-at-desk.jpg" alt="about us image" class="sidebar-widget-image" />
        <p class="sidebar-widget-body">I find life better, and I'm happier, when things are nice and simple. </p>
      </div>
      <div class="sidebar-widget">
        <h2 class="sidebar-widget-title">Recent posts</h2>
        <div class="sidebar-widget-recent-post">
          <h3 class="sidebar-widget-post-title">recent posts title</h3>
          <img src="../documents/img/teenagers-at-desk.jpg" alt class="sidebar-widget-post-image" />
        </div>
        <div class="sidebar-widget-recent-post">
          <h3 class="sidebar-widget-post-title">recent post title</h3>
          <img src="../documents/img/teenagers-at-desk.jpg" alt class="sidebar-widget-post-image" />
        </div>
      </div>
    </aside>
  </div>
  <footer>
    <p></p>
    <p></p>
    <p></p>
  </footer>
</body>

</html>
```


