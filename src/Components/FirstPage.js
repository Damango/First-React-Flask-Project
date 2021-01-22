import React, { useState, useEffect } from 'react';

const FirstPage = () => {

    const [initialData, setInitialData] = useState()

    useEffect(() => {
        fetch('/api').then(response => response.json()).then(data => console.log(data))

    })


    function buttonTest() {
        fetch('/test').then(response => response.json()).then(data => setInitialData(data))
    }




    return (<div>

        <button onClick={buttonTest}>Click Me</button>
        <div>{JSON.stringify(initialData)}</div>
    </div>);
}

export default FirstPage;