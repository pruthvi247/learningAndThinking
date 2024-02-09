# CSS-selector chart
```css
.module.news {  
  /* Selects elements with BOTH of those classes */
}
section[data-open] {
  /* Selects only section elements if they have this attribute */
}
.module > h2 {
  /* Select h2 elements that are direct children of an element with that class */
} 
selector1 selector2{ 
color: firebrick;
}
/** selector2 can be some where with in selector1, ie. selector1 comes first and selector2 is in same tree */
h2 + p {
  /* Select p elements that are directly following an h2 element */
}
li ~ li {
  /* Select li elements that are siblings (and following) another li element. */
}
```
`header > *` selects all direct children of the `<header>` element, regardless of their specific type. It targets any element that is a direct child of the `<header>`