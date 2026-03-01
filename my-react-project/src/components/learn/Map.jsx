import React from 'react'

const Map = () => {
    const name = ["NEW", "AIML", "REACT", "DJANGO"]
  return (
    <>
      <h1>Map</h1>
      <ul>
        {name.map((item, index) => (
            <li key={index}>Index is : {index}{item}</li>
        ))}
      </ul>
    </>
  )
}

export default Map