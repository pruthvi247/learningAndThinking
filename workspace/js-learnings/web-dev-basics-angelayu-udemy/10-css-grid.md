Grids are for 2-d

**flex vs grid**
[app-brew-demo-site](https://yuangela.com/grid-vs-flexbox/)

[good-read](https://css-tricks.com/snippets/css/complete-guide-grid/)
![[Pasted image 20230618125615.png]]



## Grid Elements

A grid layout consists of a parent element, with one or more child elements.
syntax:
```
grid-template-columns: none|auto|max-content|min-content|_length_|initial|inherit;
-------------------------------------------
`grid-template-columns: auto auto auto;`
-------------------------------------------
`grid-template-columns: 1fr 1fr 1fr;` -> three columns
-------------------------------------------
`grid-template: 1fr 1fr 1fr / 2rem 2rem 2rem ;` -> `grid-template: rows/columns
```

```
[source-code](https://www.w3schools.com/css/tryit.asp?filename=trycss_grid)
```html
<!DOCTYPE html>
<html>
<head>
<style>
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  background-color: #2196F3;
  padding: 10px;
}
.grid-item {
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(0, 0, 0, 0.8);
  padding: 20px;
  font-size: 30px;
  text-align: center;
}
</style>
</head>
<body>

<h1>Grid Elements</h1>

<p>A Grid Layout must have a parent element with the <em>display</em> property set to <em>grid</em> or <em>inline-grid</em>.</p>

<p>Direct child element(s) of the grid container automatically becomes grid items.</p>

<div class="grid-container">
  <div class="grid-item">1</div>
  <div class="grid-item">2</div>
  <div class="grid-item">3</div>  
  <div class="grid-item">4</div>
  <div class="grid-item">5</div>
  <div class="grid-item">6</div>  
  <div class="grid-item">7</div>
  <div class="grid-item">8</div>
  <div class="grid-item">9</div>  
</div>

</body>
</html>
```

# Grid sizing

[Demo application](https://yuangela.com/grid-sizing/)

## All CSS Grid Properties

|Property|Description|
|---|---|
|[column-gap](https://www.w3schools.com/cssref/css3_pr_column-gap.asp)|Specifies the gap between the columns|
|[gap](https://www.w3schools.com/cssref/css3_pr_gap.asp)|A shorthand property for the _row-gap_ and the _column-gap_ properties|
|[grid](https://www.w3schools.com/cssref/pr_grid.asp)|A shorthand property for the _grid-template-rows, grid-template-columns, grid-template-areas, grid-auto-rows, grid-auto-columns_, and the _grid-auto-flow_ properties|
|[grid-area](https://www.w3schools.com/cssref/pr_grid-area.asp)|Either specifies a name for the grid item, or this property is a shorthand property for the _grid-row-start_, _grid-column-start_, _grid-row-end_, and _grid-column-end_ properties|
|[grid-auto-columns](https://www.w3schools.com/cssref/pr_grid-auto-columns.asp)|Specifies a default column size|
|[grid-auto-flow](https://www.w3schools.com/cssref/pr_grid-auto-flow.asp)|Specifies how auto-placed items are inserted in the grid|
|[grid-auto-rows](https://www.w3schools.com/cssref/pr_grid-auto-rows.asp)|Specifies a default row size|
|[grid-column](https://www.w3schools.com/cssref/pr_grid-column.asp)|A shorthand property for the _grid-column-start_ and the _grid-column-end_ properties|
|[grid-column-end](https://www.w3schools.com/cssref/pr_grid-column-end.asp)|Specifies where to end the grid item|
|[grid-column-gap](https://www.w3schools.com/cssref/pr_grid-column-gap.asp)|Specifies the size of the gap between columns|
|[grid-column-start](https://www.w3schools.com/cssref/pr_grid-column-start.asp)|Specifies where to start the grid item|
|[grid-gap](https://www.w3schools.com/cssref/pr_grid-gap.asp)|A shorthand property for the _grid-row-gap_ and _grid-column-gap_ properties|
|[grid-row](https://www.w3schools.com/cssref/pr_grid-row.asp)|A shorthand property for the _grid-row-start_ and the _grid-row-end_ properties|
|[grid-row-end](https://www.w3schools.com/cssref/pr_grid-row-end.asp)|Specifies where to end the grid item|
|[grid-row-gap](https://www.w3schools.com/cssref/pr_grid-row-gap.asp)|Specifies the size of the gap between rows|
|[grid-row-start](https://www.w3schools.com/cssref/pr_grid-row-start.asp)|Specifies where to start the grid item|
|[grid-template](https://www.w3schools.com/cssref/pr_grid-template.asp)|A shorthand property for the _grid-template-rows_, _grid-template-columns_ and _grid-areas_ properties|
|[grid-template-areas](https://www.w3schools.com/cssref/pr_grid-template-areas.asp)|Specifies how to display columns and rows, using named grid items|
|[grid-template-columns](https://www.w3schools.com/cssref/pr_grid-template-columns.asp)|Specifies the size of the columns, and how many columns in a grid layout|
|[grid-template-rows](https://www.w3schools.com/cssref/pr_grid-template-rows.asp)|Specifies the size of the rows in a grid layout|
|[row-gap](https://www.w3schools.com/cssref/css3_pr_row-gap.asp)|Specifies the gap between the grid rows|

## CSS Syntax

grid-template-columns: none|auto|max-content|min-content|_length_|initial|inherit;

## Property Values

|Value|Description|Demo|
|---|---|---|
|none|Default value. Columns are created if needed|[Demo ❯](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_grid-template-columns)|
|auto|The size of the columns is determined by the size of the container and on the size of the content of the items in the column|[Demo ❯](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_grid-template-columns)|
|max-content|Sets the size of each column to depend on the largest item in the column|[Demo ❯](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_grid-template-columns&preval=max-content%20max-content)|
|min-content|Sets the size of each column to depend on the smallest item in the column||
|_length_|Sets the size of the columns, by using a legal length value. [Read about length units](https://www.w3schools.com/cssref/css_units.php)|[Demo ❯](https://www.w3schools.com/cssref/playdemo.php?filename=playcss_grid-template-columns&preval=50px%20100px)|
|initial|Sets this property to its default value. [Read about _initial_](https://www.w3schools.com/cssref/css_initial.php)||
|inherit|Inherits this property from its parent element. [Read about _inherit_](https://www.w3schools.com/cssref/css_inherit.php)|
|repeat|Repeats specified template eg : `grid-template-column: repeat(2,100px)`|



# Grid placement/layout
A grid layout consists of a parent element, with one or more child elements.

[source](https://www.w3schools.com/css/tryit.asp?filename=trycss_grid_lines2)
```html
<!DOCTYPE html>
<html>
<head>
<style>
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  gap: 10px;
  background-color: #2196F3;
  padding: 10px;
}

.grid-container > div {
  background-color: rgba(255, 255, 255, 0.8);
  text-align: center;
  padding: 20px 0;
  font-size: 30px;
}

.item1 {
  grid-row-start: 1;
  grid-row-end: 3;
}
.item2 {
  grid-row-start: 1;
  grid-row-end: 3;
}

</style>
</head>
<body>

<h1>Grid Lines</h1>

<div class="grid-container">
  <div class="item1">1</div>
  <div class="item2">2</div>
  <div class="item3">3</div>  
  <div class="item4">4</div>
  <div class="item5">5</div>
  <div class="item6">6</div>
  <div class="item7">7</div>
  <div class="item8">8</div>  
</div>

<p>You can refer to line numbers when placing grid items.</p>

</body>
</html>
```

