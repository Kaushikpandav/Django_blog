import React from 'react'

const Events = () => {
    const [clickCount, setClickCount] = React.useState(0)
    const handleClick = () => {
        setClickCount(clickCount + 1)
    }
    const handleDecrement = (param) => {
        console.log("dsdsd" + param)
    }
    return (
        <>  <h1>Events</h1>
            <p>Events are the actions that are performed by the user or by the system.</p>

            <button onClick={handleClick}>Click here</button>
            <p> click count: {clickCount}</p>

            <button onClick={() => handleDecrement(clickCount - 1)}>Click here</button >
        </>
    )
}

export default Events