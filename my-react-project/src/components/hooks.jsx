

// usestate, useEffect, useContext, useRef, useMemo, useCallback
// Custom hooks

import { useState } from 'react'

const Hooks = () => {
    const [count, setCount] = useState(0)
    return (
        <>
            <div>hooks</div>
            <button onClick={() => setCount(count + 1)}>Click</button>
            <p>Count: {count}</p>
        </>
    )
}

export default Hooks

