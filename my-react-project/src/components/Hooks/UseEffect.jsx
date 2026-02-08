import React from 'react'

const UseEffect = () => {
    const [count, setCount] = React.useState(0)
    const [randomNumber, setRandomNumber] = React.useState(0)


    useEffect(() => {
        console.log("useEffect")

        //  effect of this 2 state it's will call on every time when count or randomNumber change

        // To connect server or DB code logic will write here

        // cleanup function
        return () => {
            // when you release the component it will call this function, dependecy change or unmounting
            //  To disconnect server or DB code logic will write here
            console.log("useEffect return")
        }
    }, [count, randomNumber])
    return (
        <>
            <h1>UseEffect</h1>
            <p>Count: {count}</p>
            <button onClick={() => setCount(count = 0)}>Reset</button>
            <button onClick={() => setCount(count + 1)}>Increase</button>
            <button onClick={() => setCount(count - 1)}>Decrease</button>


            <button onClick={() => setRandomNumber(Math.floor(Math.random() * 100))}>Generate Random Number</button>
            <p>Random Number: {randomNumber}</p>
        </>
    )
}

export default UseEffect

// # to perform side effects
// And It's alwasy call on little change on any compopnent !! when you pass empty array ut will just effect on mounting !!

// fecthing data from API
// Subscribning data stream
// Manuallly changing DOM