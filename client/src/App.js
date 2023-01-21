import React, {useState, useEffect} from "react"

function App() {
  const [data,setData] = useState([{}])
  
  useEffect(() => {
    fetch("/variables").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  },[])

  return (
    <div>
      {(typeof data.variables === 'undefined') ? (
        <p>Loading...</p>
      ): (
        data.variables.map((variable, i) => (
          <p key={i}>{variable}</p>
        ))
      )}
    </div>
  )
}

export default App