import Hello from "./components/hello"
import Learn from "./components/learn"
import Props from "./components/props"
import Events from "./components/Events"
import Lifting_state from "./components/lifting_state"
import Hooks from "./components/hooks"
function App() {
  let price = 100
  const getStock = (stock) => {
    console.log(stock)
  }
  return (
    <>
      {/* <Hello />
      <Learn />
      <Props name="AIML" price={price} />
      <Events />
      <Lifting_state getStock={getStock} /> */}
      <Hooks />
    </>
  )
}

export default App
