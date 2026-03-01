import React from 'react'

const ConditionalRendering = () => {
    const [isLoggedIn, setIsLoggedIn] = React.useState(false)
    const [status, setStatus] = React.useState(false)
  return (
   <>

   <h1>Conditional Rendering Example</h1>
   {isLoggedIn ? (<h1>Welcome User!</h1>) : (<h1>Please Login</h1>)}
   <button onClick={() => setIsLoggedIn(!isLoggedIn)}>Toggle Login</button>

    {status && (
        <h2> shown </h2>
    )}


   </>
  )
}

export default ConditionalRendering