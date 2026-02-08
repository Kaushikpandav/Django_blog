import { useState } from 'react'

function Usecounter(intialvalue = 0) {
    const [count, setCount] = useState(intialvalue)

    const increment = () => {
        setCount(count + 1)
    }
    const decrement = () => {
        setCount(count - 1)
    }
    const reset = () => {
        setCount(intialvalue)
    }

    return { count, increment, decrement, reset }
}
export default Usecounter


// # it's use to create a custom hook that can be reused in different components. It is a function that starts with "use" and it can call other hooks inside it. It is used to share logic between components and it can return any value that we want. It is also used to create a custom hook that can be used to manage the state of a component. It is also used to create a custom hook that can be used to manage the side effects of a component. It is also used to create a custom hook that can be used to manage the context of a component. It is also used to create a custom hook that can be used to manage the refs of a component. It is also used to create a custom hook that can be used to manage the lifecycle of a component. It is also used to create a custom hook that can be used to manage the forms of a component. It is also used to create a custom hook that can be used to manage the animations of a component. It is also used to create a custom hook that can be used to manage the timers of a component. It is also used to create a custom hook that can be used to manage the media queries of a component. It is also used to create a custom hook that can be used to manage the scroll position of a component. It is also used to create a custom hook that can be used to manage the previous state or props of a component.