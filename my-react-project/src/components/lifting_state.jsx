import React from 'react'

const Lifting_state = (props) => {


    const handleClick = () => {
        let stock = "tesla"
        props.getStock(stock)
    }
    return (
        <>
            <h1>Lifting_state</h1>
            <button onClick={handleClick}>Click here</button>
        </>
    )
}

export default Lifting_state