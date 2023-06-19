# Adding Event Listner
## The addEventListener() method

Add an event listener that fires when a user clicks a button:
`_element_.addEventListener(_event, function, useCapture_);`
>document.getElementById("myBtn").addEventListener("click", displayDate);

The `addEventListener()` method attaches an event handler to an element without overwriting existing event handlers.

You can add many event handlers to one element.

You can add many event handlers of the same type to one element, i.e two "click" events.

You can add event listeners to any DOM object not only HTML elements. i.e the window object.

The `addEventListener()` method makes it easier to control how the event reacts to bubbling.

When using the `addEventListener()` method, the JavaScript is separated from the HTML markup, for better readability and allows you to add event listeners even when you do not control the HTML markup.

You can easily remove an event listener by using the `removeEventListener()` method.
[example](https://www.w3schools.com/js/tryit.asp?filename=tryjs_addeventlistener_displaydate)
```html
<!DOCTYPE html>
<html>
<body>

<h2>JavaScript addEventListener()</h2>

<p>This example uses the addEventListener() method to attach a click event to a button.</p>

<button id="myBtn">Try it</button>

<p id="demo"></p>

<script>
document.getElementById("myBtn").addEventListener("click", displayDate);

function displayDate() {
  document.getElementById("demo").innerHTML = Date();
}
</script>

</body>
</html> 

```

### Higher order functions:
Functions that can take other functions as inputs

[example](https://rakuten.udemy.com/course/the-complete-web-development-bootcamp/learn/lecture/12384168#overview)
```js
function anotherAddEventListener(typeOfEvent,callback){
/// detect event code..

var eventThatHappened={
eventType:"Keydown",
key:"p",
durationOfKeypress:2
}
if (eventThatHappened.eventType == typeOfEvent){
callback(eventThatHappened);
}
}
--------------calling listners-----------
anotherAddEventListener("keydown",function(event){
console.log(event);
 });
 ----------------------
document.addEventListener("keydown",function(event){
console.log(event);
 });
```
