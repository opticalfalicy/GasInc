import React, {useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';
// import Image from 'https://photos.google.com/album/AF1QipM3pARMEXV75Ez--x_giuJefiTqITRN4d8Ga1NX/photo/AF1QipPCBeUuE1neE9Hdg5U3a_MgYlJoeWNrALr9AQms'

function loadProjects(callback){
  const xhr = new XMLHttpRequest()
  const method = 'GET' // 'POST'
  const url = "https://gasinc.herokuapp.com/projects/"
  const responseType = "json"
  xhr.responseType = responseType
xhr.open(method, url)
xhr.onload = function() {
  callback(xhr.response, xhr.status)
}
// xhr.onerror = function (e) {
//   callback({"message": "invalid request"}, 400)
// }
console.log(xhr)
xhr.send()
}

function loadImages(callback){
  const xhr = new XMLHttpRequest()
  const method = 'GET' // 'POST'
  const url = "https://gasinc.herokuapp.com/images/"
  const responseType = "json"
  xhr.responseType = responseType
xhr.open(method, url)
xhr.onload = function() {
  callback(xhr.response, xhr.status)
}
// xhr.onerror = function (e) {
//   callback({"message": "invalid request"}, 400)
// }
console.log(xhr)
xhr.send()
}


function App() {
  const [projects, setProjects] = useState([{name: 123}])
  useEffect(() => {
    const myCallback = (response, status) => {

      setProjects(response);

    }
    loadProjects(myCallback)
  }, [])

  const [images, setImages] = useState([{}])
  useEffect(() => {
    const myCallback = (response, status) => {

      setImages(response);

    }
    loadImages(myCallback)
  }, [])


  

  console.log(images)
  return (
    <div className="App">
      {/* <header className="App-header"> */}
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <p className='projects'>
          {projects.map((project, index)=>{
            console.log(project)
          return( 
            <li className='project-item'>
              <div className='p-n'>{project.name}</div>
              <div className='p-mt'>{project.main_tag}</div>
              <div class='p-imgs'>
              {images.map((image, index)=>{
                console.log(image)
                // if(){
              return( 
                
                  <img src={`https://gasinc.herokuapp.com${image.image}`}/>
                
          
                )
              }
            // }
              )} 
              
              </div>
              
            </li>
    
            )
          })}
        </p>
      {/* </header> */}
    </div>
  );
}

export default App;
