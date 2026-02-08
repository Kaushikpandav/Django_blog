import React from 'react'

const UseMemo = () => {
    const [count, setCount] = React.useState(0)
    const [number, setNumber] = React.useState(100)
    const calculate = () => {
        console.log("calculate")
        let sum = 0;
        for (let i = 0; i < number; i++) {
            sum += i;
        }
        return sum;
    }
    const memoizedCalculate = React.useMemo(calculate, [number])
    return (
        <>
            <div>UseMemo</div>


            <p>Count: {count}</p>
            <button onClick={() => {
                if (count === 10) {
                    setNumber(9999999)
                }
            }}>Increment</button >
            <button onClick={() => setCount(count - 1)}>Decrement</button>
            console.log("render")
            <p>Sum: {memoizedCalculate}</p>
        </>
    )
}

export default UseMemo



// it can remember result of funtion , avoid expensive calculation on every render