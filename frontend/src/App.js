import { useEffect, useState} from 'react';

function App() {
  const [data, setData] = useState({})
  useEffect(() => {
    fetchData();
  },[])

  const fetchData = async ()=>{
    try{
      // Note: Fetches jsonified data from url from the backend
      const response = await fetch("http://127.0.0.1:5000/api/data");
      const jsonData = await response.json();
      setData(jsonData)
    }
    catch(error){
      console.log('Error', error)
    }
  }

  return (
    <div className="App">
      <h1>Frontend gng</h1>
      <h3>{data.message}</h3>
    </div>
  );
}

export default App;
