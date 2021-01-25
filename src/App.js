import FirstPage from "./Components/FirstPage"
import React, { useState, useEffect } from 'react';
import './App.css';


function App() {

  const [data, setData] = useState([])

  function buttonTest() {
    //fetch('/test').then(response => response.json()).then(data => setData(data))
  }






  return (
    <div className="App">

      <button onClick={buttonTest}>Click Me</button>


      <FirstPage data={data} />

    </div>
  );
}

export default App;
