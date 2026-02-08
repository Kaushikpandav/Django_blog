import { useContext } from 'react'
import { stockContext, userContext } from '../../App'

const child3 = () => {

  const stockdata = useContext(stockContext)
  const userdata = useContext(userContext)

  return (
    <>
      <div>child3</div>
      <p>It's calling DDDD</p>
      {/* <h1>Stock: {props.stock}</h1> */}

      {/* #context api */}
      {/* <stockContext.Consumer>
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
    </stockContext.Consumer> */}


      <h2>Child C : stock {stockdata.stock} </h2>
      <h2>Child C : price {stockdata.price} </h2>
      <h2>Child C : user name {userdata.user.name} </h2>
      <p> IS user login ?? : {userdata.user.Islogin}</p>








      {/* #useContext hook */}




    </>
  )
}

export default child3