import {useState} from 'react'

const Forms = () => {
    // const [Firstname, setFirstName] = useState("")
    // const [Email, setEmail] = useState("")
    // const [Password, setPassword] = useState("")
    
    //  in single state form handling
    const [formData, setFormData] = useState({
        firstname: "",
        email: "",
        password: ""
    })


   const handlechange = (e) => {
        // setFirstName(e.target.value)
        setFormData({...formData, [e.target.name]: e.target.value})
   }

   const handleformsubmit = (e) => {
        e.preventDefault()
        console.log(formData);
   }

  return (
    <>
    {/* <form action="" method="post">
        <input type="text"  vlaue={Firstname} onChange={handleFirstname} />
        <input type="email" vlaue={Email} onChange={handleemail}/>
        <input type="password" value={Password} onChange={handlePassword} />
        <button type='submit'>Submit</button>
    </form> */}

    <form action="" method="post" onSubmit={handleformsubmit}>
        <input type="text" name='firstname' vlaue={formData.firstname} onChange={handlechange} />
        <input type="email" name='email' vlaue={formData.email} onChange={handlechange}/>
        <input type="password" name='password' value={formData.password} onChange={handlechange} />
        <button type='submit' value='submit'>Submit</button>
    </form>

        
    </>
  )
}

export default Forms