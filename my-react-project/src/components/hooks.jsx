

// usestate, useEffect, useContext, useRef, useMemo, useCallback
// Custom hooks

import { useState } from 'react'

const Hooks = () => {
    const [count, setCount] = useState(0)
    const [stockPrice, setStockPrice] = useState({ stock: "Apple", price: 100 })

    const handleUpdateStock = () => {
        // setStockPrice({ stock: "Google", price: 200 })
        setStockPrice({ ...stockPrice, price: 200 }) // spread operator
    }
    return (
        <>
            <div>hooks</div>
            <button onClick={() => setCount(count + 1)}>Click</button>
            <p>Count: {count}</p>

            <p>Stock: {stockPrice.stock}</p>
            <p>Price: {stockPrice.price}</p>
            <button onClick={handleUpdateStock}>Update Stock</button>
        </>
    )
}

export default Hooks

