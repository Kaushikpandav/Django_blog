import React from 'react'
import '../assets/css/style.css'

const Inlinecss = () => {
    const style = {
        container: {
            color: 'red',
            backgroundColor: 'yellow',
        },
        paragraph: {
            color: 'blue',
            backgroundColor: 'pink',
        },

        h2Text: {
            color: 'green',
            backgroundColor: 'orange',
            textAlign: 'center',
        }
    }
    return (
        <>

            <style>
                {`
                .Internal {
                    color: purple;
                    background-color: cyan;
                    text-align: center;
                    font-weight: bold;
                    font-size: 20px;
                    font-family: Arial, sans-serif;
                }
            `}

            </style>
            <h1 style={{ color: 'red', backgroundColor: 'yellow' }}>This is heading</h1>
            <p style={{ color: 'blue', backgroundColor: 'pink' }}>This is paragraph</p>


            <div style={style.container}>
                <h2 style={style.h2Text}>This is h2 text</h2>
            </div>
            <hr />

            <div className='Internal'>it's experiment</div>

            <h1>It's external CSS</h1>
            <div className="Bluebox">Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis voluptates laboriosam eaque, repellat adipisci sequi. Expedita alias, magnam fugiat placeat, temporibus quas possimus obcaecati provident ab, cum repellendus ullam nemo.</div>
        </>
    )
}

export default Inlinecss