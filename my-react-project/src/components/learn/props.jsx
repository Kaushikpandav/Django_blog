import React from 'react'

// const Props = (props) => {
//     return (
//         <>
//             <div>Props</div>
//             <p>vdvdvvdvd {props.name}</p>
//             <h4>{props.price}</h4>
//         </>
//     )
// }

const Props = ({ price, name }) => {
    return (
        <>
            <div>Props</div>
            <p>lob  cbdn n bjibc :{name}</p>
            <h4>{price}</h4>
        </>
    )
}

export default Props