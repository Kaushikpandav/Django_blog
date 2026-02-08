import React from 'react'

const Inlinecss = () => {
    const style = {
        container:{
            color:'red',
            backgroundColor:'yellow',
        },
        paragraph:{
            color:'blue',
            backgroundColor:'pink',
        },

        h2Text:{
            color:'green',
            backgroundColor:'orange',
            textAlign:'center',
        }
    }
  return (
    <>  
    <h1 style={{color:'red',backgroundColor:'yellow'}}>This is heading</h1>
    <p style={{color:'blue',backgroundColor:'pink'}}>This is paragraph</p>


    <div style={style.container}>
        <h2 style={style.h2Text}>This is h2 text</h2>
    </div>
    </>
  )
}

export default Inlinecss