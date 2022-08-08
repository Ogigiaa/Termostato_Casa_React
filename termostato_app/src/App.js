import {React, useState, useEffect} from 'react';


function send2server(gradi){
  fetch('http://localhost:5050/saveGradi',{
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify({
      'gradi'     : gradi,
      'user_name' : 'dom'
    }) 
  })
}


function loadFromServer(setGradi){
  fetch('http://localhost:5050/getGradi',{
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify({
      'user_name' : 'dom'
    }) 
  }).then( (response)=>{
    response.text().then((i)=>{
      setGradi(parseInt(i))
    })
  })
}

function App() {
  let [gradi, setgradi] = useState(1)
  let rosso = 12 + gradi / 35 * (230 - 12)
  let verde = 246 - gradi / 35 * (246 - 174)
  let blu = 246 - gradi / 35 * (246 -21)
  function add(){
    setgradi( (g) => {
      if(g<35){
        send2server(g+1)
        return g+1
      }
      return g
    })
  }
  function sub(){
    setgradi( (g) => {
      if(g>5){
        send2server(g-1)
        return g-1
      }
      return g
    })
  }
  useEffect(function(){
    loadFromServer(setgradi)
  },[])

  /*setInterval(()=>{
    loadFromServer(setgradi)
  },500)*/

  return (
    <div className="App">
      <div id='r1'>
        <h1>Termostato casa</h1>
        <button onClick={add}>+</button>
      </div>
      <div id='r2'>
        <div id='temp_box'>
          <div id='temp'> {gradi} </div>
          <div id='temp_bar' style={{
            width: (gradi/35*100)+'%',
            backgroundColor: `rgb(${rosso},${verde},${blu})`
            }}  >&nbsp;</div>
        </div>
      </div>
      <div id='r3'>
        <button onClick={sub}>-</button>
      </div>
    </div>
  );
}



export default App;
