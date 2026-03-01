import React, { useState, createContext } from "react"

export const stockContext = createContext()
export const userContext = createContext()

import Hello from "./components/learn/hello"
import Learn from "./components/learn/learn"
import Props from "./components/learn/props"
import Events from "./components/learn/Events"
import Lifting_state from "./components/learn/lifting_state"
import Hooks from "./components/learn/hooks"
import CounterApp from "./components/Hooks/CounterAppUseState"
import UseEffect from "./components/Hooks/UseEffect"
import UseMemo from "./components/Hooks/UseMemo"
import Child1 from "./components/Hooks/Child1"
import Useref from "./components/Hooks/Useref"
import CustomHooks from "./components/custom_Hooks/CustomHooks"
import ConditionalRendering from "./components/learn/ConditionalRendering"
import Map from "./components/learn/Map"
import Inlinecss from "./components/learn/Inlinecss"
import Loadimages from "./components/learn/Loadimages"
import Forms from "./components/learn/Forms"
import './assets/css/style.css'

function App() {
  let stock = 100
  let price = 9999

  const [user, setUser] = useState({ name: "AIML", Islogin: "yes" })

  const getStock = () => {
    return stock
  }

  // Cretae , provider and cosumer

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
      {/* <stockContext.Provider value={{ stock, price }}>
        <userContext.Provider value={{ user, setUser }}>
          <Child1 />
        </userContext.Provider>
      </stockContext.Provider> */}


      {/* #Useref */}
      {/* <Useref /> */}
      {/* <CustomHooks /> */}
      {/* <ConditionalRendering /> */}
      {/* <Map /> */}
      {/* <Inlinecss /> */}
      {/* <Loadimages />0 */}
      <Forms />
    </>
  )
}

export default App