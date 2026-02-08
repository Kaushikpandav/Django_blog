import React from 'react'

const CounterApp = () => {
    const [count, setCount] = React.useState(0)
    const handleIncrement = () => {
        setCount(count + 1)
    }
    const handleDecrement = () => {
        setCount(count - 1)
    }
    const Reset = () => {
        setCount(0)
    }
    return (
        <>
            <h1>Counter App</h1>
            <p>Count: {count}</p>
            <button onClick={Reset}>Reset</button>
            <button onClick={() => handleIncrement(count + 1)}>Increment</button>
            <button onClick={handleDecrement}>Decrement</button>
        </>
    )
}

export default CounterApp