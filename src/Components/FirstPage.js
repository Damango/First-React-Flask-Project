import React, { useState, useEffect } from 'react';
import "./FirstPage.css"

const FirstPage = (props) => {

    const [initialData, setInitialData] = useState()

    useEffect(() => {
        fetch('/api').then(response => response.json()).then(data => console.log(data))

    })


    function buttonTest() {
        fetch('/test').then(response => response.json()).then(data => setInitialData(data))
    }




    return (<div className="test-page">


        <div>User ID: {JSON.stringify(props.data.userID)}</div>
        <div>Current Weight: {JSON.stringify(props.dataa.currentWeight)}</div>
        <div>User Name: {JSON.stringify(props.data.username)}</div>
    </div>);
}

export default FirstPage;