import Hello from "./components/hello"
import Learn from "./components/learn"
import Props from "./components/props"
import Events from "./components/Events"
import Lifting_state from "./components/lifting_state"
import Hooks from "./components/hooks"
import CounterApp from "./components/Hooks/CounterApp"
import UseEffect from "./components/Hooks/UseEffect"
import UseMemo from "./components/Hooks/UseMemo"
import Child1 from "./components/Hooks/child1"
import Child2 from "./components/Hooks/child2"
import Child3 from "./components/Hooks/child3"
import { createContext } from "react"

const stockContext = createContext()
const userContext = createContext()

function App() {
  let stock = 100
  let price = 9999
  const getStock = () => {
    return stock
  }

  // Cretae , provider and cosumer

  const [user, setUser] =  React.useState({name: "AIML", Islogin: "yes"})

      
  return (  
    <>
      {/* <Hello />
      <Learn />
      <Props name="AIML" price={price} />
      <Events />
      <Lifting_state getStock={getStock} /> */}
      {/* <Hooks /> */}
      {/* <CounterApp /> */}
      {/* <UseEffect /> */}

      {/* Props Driling  */}
      {/* <Child2 /> */}
      {/* <Child3 /> */}
      {/* <Child1 stock={stock}/> */}

      {/* Context APi Example */}
      <stockContext.Provider value={{stock, price}}>
        <userContext.Provider value={{user, setUser}}>
         <Child1 />
        </userContext.Provider>
      </stockContext.Provider>
    </>
  ) 
}

export default App
export {stockContext, userContext}