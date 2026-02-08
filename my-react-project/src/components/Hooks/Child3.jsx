import React from 'react'
import { stockContext, userContext } from '../../App'
const child3 = () => {
  return (
    <>
    <div>child3</div>
    <p>It's calling DDDD</p>
    {/* <h1>Stock: {props.stock}</h1> */}
    <stockContext.Consumer>
     {
        ({stock, price})=> {
          return (
            <userContext.Consumer>
                {
                    ({user})=> {
                        return (
                            <>
                            <h1>Stock: {stock}</h1>
                            <h1>Price: {price}</h1>
                            <h1>User Name: {user.name}</h1>
                            <h1>User Login Status: {user.Islogin}</h1>
                            </>
                  )
                }
            }
            </userContext.Consumer>
            )
        }
     }
    </stockContext.Consumer>
    </>
  )
}

export default child3