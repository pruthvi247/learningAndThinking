
`document.querySelector("h1") => jquery("h1") => $("h1")`

### selecting elements with jquery

`$("h1.head")`

### Manipulating styles with jquery
``$("h1").css("color","yellow")`` - set
`$("h1").css("color")`` - get


```css
.bit-title{
font-size: 10rem;
color:yellow;
font-family;
}
.margin-50{
margin:50;
}

----------------separating css and jsquery/js -----------------
$("h1").addClass("bit-title");
$("h1").removeClass("bit-title");

--------------------adding multiple class ----------------------
$("h1").addClass("bit-title margin-50");

--------------------adding multiple class ----------------------
$("h1").hasClass("bit-title");
> true
```

### Manipulating text with jquery

`$("h1").text("Replace text")`
`$("h1").html("<em>hey<em>")` /// html is consider, `< em>` not taken as string

### Manipulating attibutes with jquery
`<img src= "drum.png" alt="">` -> src is attribute here

`$(a).attr("href","https://www.google.com")` -> gets all href and changes to google

### Manipulating Event Listners with jquery

```css
$( "#dataTable tbody tr" ).on( "click", function() {

  console.log( $( this ).text() );

});
```

#### Jquery vs css


```javascript

------------------ css ---------------------
document.getElementById('outer').addEventListener('mouseup', function (event) {
    alert('This alert should not show up!');
}, false);

------------------ jquery ---------------------

$('#outer').on('mouseup', function (event) {
    alert('This alert should not show up!');
}, false);

```

## Add/ remove elements
We will look at four jQuery methods that are used to add new content:

- `append()` - Inserts content at the end of the selected elements
- `prepend()` - Inserts content at the beginning of the selected elements
- `after()` - Inserts content after the selected elements
- `before()` - Inserts content before the selected elements
### jQuery append() Method

The jQuery `append()` method inserts content AT THE END of the selected HTML elements
> $("p").append("Some appended text.");

### jQuery prepend() Method

The jQuery `prepend()` method inserts content AT THE BEGINNING of the selected HTML elements.

> $("p").prepend("Some prepended text.");

```html
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
<script>
function appendText() {
  var txt1 = "<p>Text.</p>";        // Create text with HTML
  var txt2 = $("<p></p>").text("Text.");  // Create text with jQuery
  var txt3 = document.createElement("p");
  txt3.innerHTML = "Text.";         // Create text with DOM
  $("body").append(txt1, txt2, txt3);   // Append new elements
}
</script>
</head>
<body>

<p>This is a paragraph.</p>
<button onclick="appendText()">Append text</button>

</body>
</html>

```
## jQuery after() and before() Methods

The jQuery `after()` method inserts content AFTER the selected HTML elements.

The jQuery `before()` method inserts content BEFORE the selected HTML elements.
```html
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
<script>
function afterText() {
  var txt1 = "<b>I </b>";           // Create element with HTML
  var txt2 = $("<i></i>").text("love ");  // Create with jQuery
  var txt3 = document.createElement("b");   // Create with DOM
  txt3.innerHTML = "jQuery!";
  $("img").after(txt1, txt2, txt3);    // Insert new elements after img
}
</script>
</head>
<body>

<img src="/images/w3jquery.gif" alt="jQuery" width="100" height="140">

<p>Click the button to insert text after the image.</p>

<button onclick="afterText()">Insert after</button>

</body>
</html>
```

## jQuery Animations - The animate() Method

The jQuery `animate()` method is used to create custom animations.

```css
$("button").click(function(){  
  $("div").animate({left: '250px'});  
});
```
### jQuery animate() - Uses Queue Functionality

By default, jQuery comes with queue functionality for animations.

This means that if you write multiple `animate()` calls after each other, jQuery creates an "internal" queue with these method calls. Then it runs the animate calls ONE by ONE.

So, if you want to perform different animations after each other, we take advantage of the queue functionality:

```css
$("button").click(function(){  
  var div = $("div");  
  div.slideup().slidedown().animate({height: '300px', opacity: '0.4'}, "slow");  
  div.animate({width: '300px', opacity: '0.8'}, "slow");  
  div.animate({height: '100px', opacity: '0.4'}, "slow");  
  div.animate({width: '100px', opacity: '0.8'}, "slow");  
});
```
