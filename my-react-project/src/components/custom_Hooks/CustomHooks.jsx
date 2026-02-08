
import Usecounter from '../../hooks/Usecounter'

const CustomHooks = () => {
  const { count, increment, decrement, reset } = Usecounter(10)
  console.log(count)
  return (
    <>
      <h1>Custom Hooks</h1>
      <h2>Count: {count}</h2>
      <button onClick={increment}>Increment</button>
      <button onClick={decrement}>Decrement</button>
      <button onClick={reset}>Reset</button>
    </>
  )
}

export default CustomHooks