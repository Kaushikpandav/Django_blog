import React from 'react'

const Useref = () => {
  return (
    <>
      <h1>UseRef</h1>
    </>
  )
}

export default Useref


// #it's use to access the dom element directly without using document.getElementById() or querySelector() method. It is a hook that allows us to create a reference to a DOM element in a functional component. It returns a mutable ref object which has a current property that can be used to access the DOM element. It is used to store a reference to a DOM element and it does not cause re-rendering when the value of the ref changes. It is also used to store any mutable value that does not cause re-rendering when it changes.

//  it's also use to store the mutable value that does not cause re-rendering when it changes. It is also used to store the previous value of a state or props. It is also used to store the interval or timeout id that can be cleared when the component unmounts. It is also used to store the value of a form input that can be accessed without causing re-rendering. It is also used to store the value of a timer that can be cleared when the component unmounts. It is also used to store the value of a WebSocket connection that can be closed when the component unmounts. It is also used to store the value of a media query that can be accessed without causing re-rendering. It is also used to store the value of a scroll position that can be accessed without causing re-rendering. It is also used to store the value of a previous state or props that can be accessed without causing re-rendering.