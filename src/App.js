import React, {useEffect, useState} from 'react';
import logo from './logo.svg';
import './App.css';
// import Image from 'https://photos.google.com/album/AF1QipM3pARMEXV75Ez--x_giuJefiTqITRN4d8Ga1NX/photo/AF1QipPCBeUuE1neE9Hdg5U3a_MgYlJoeWNrALr9AQms'

function loadProjects(callback){
  const xhr = new XMLHttpRequest()
  const method = 'GET' // 'POST'
  const url = "https://gasinc.herokuapp.com/projects/"
  // const url = "http://127.0.0.1:8000/projects/"
  const responseType = "json"
  xhr.responseType = responseType
xhr.open(method, url)
xhr.onload = function() {
  callback(xhr.response, xhr.status)
}
// xhr.onerror = function (e) {
//   callback({"message": "invalid request"}, 400)
// }
console.log('projects x', xhr)
xhr.send()
}

function loadMedia(callback){
  const xhr = new XMLHttpRequest()
  const method = 'GET' // 'POST'
  const url = "https://gasinc.herokuapp.com/projects/"
  // const url = "http://127.0.0.1:8000/media/"
  const responseType = "json"
  xhr.responseType = responseType
xhr.open(method, url)
xhr.onload = function() {
  callback(xhr.response, xhr.status)
}
// xhr.onerror = function (e) {
//   callback({"message": "invalid request"}, 400)
// }
// console.log('projects x', xhr)
xhr.send()
}


function loadImages(callback){
  const xhr = new XMLHttpRequest()
  const method = 'GET' // 'POST'
  const url = "https://gasinc.herokuapp.com/images/"
  // const url = "http://127.0.0.1:8000/images"
  const responseType = "json"
  xhr.responseType = responseType
xhr.open(method, url)
xhr.onload = function() {
  callback(xhr.response, xhr.status)
}
// xhr.onerror = function (e) {
//   callback({"message": "invalid request"}, 400)
// }
console.log('xhr', xhr)
xhr.send()
}


function App() {
  const [projects, setProjects] = useState([{name: "...loadingProjects..."}])
  useEffect(() => {
    const myCallback = (response, status) => {

      setProjects(response);

    }
    loadProjects(myCallback)
  }, [])

  const [media, setMedia] = useState([{name: "...loadingMedia..."}])
  useEffect(() => {
    const myCallback = (response, status) => {
      setMedia(response);
    }
    loadMedia(myCallback)
  }, [])

  const [images, setImages] = useState([{}])
  useEffect(() => {
    const myCallback = (response, status) => {

      setImages(response);

    }
    loadImages(myCallback)
  }, [])

  function idCheck(projects, images){
    return ({
      
    })
  }

  
  console.log('p', projects)
  console.log(images)
  return (
    <div className="App">
      {/* <header className="App-header"> */}
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
        <nav className='navbar'>
          <div className='nav-logo'><img className='nav-logo-image' src={`http://127.0.0.1:8000/media/logos/croplogo.png`} /></div>
          <div className='nav-links'>
            <ul className='links-list'>
              <li className='list-item item-Projects'>Projects</li>
              <li className='list-item item-Services'>Services</li>
              <li className='list-item item-Blog'>Blog</li>
              <li className='list-item item-History'>History</li>
              <li className='list-item item-Contact'>Contact</li>
            </ul>
          </div>
        </nav>
        <div className='jumbotron'></div>
        <p className='projects'>
          {projects.map((project, image, index)=>{
            console.log(project)
          return( 
            <li className='project-item'>
              <div className='p-n'>{project.name}</div>
              <div className='p-mt'>{project.main_tag}</div>
              <div class='p-imgs'>
                <img src={`http://127.0.0.1:8000/${project.image}`}/>
                
              {/* {images.map((image, index)=>{
                console.log(image)
                if(image.project == project.id){
              return( 
                
                  <img src={`http://127.0.0.1:8000${image.images}`}/>
                
          
                )
              }
            // }
            })} */}
              
              </div>
              
            </li>
    
            )
          })
          }
        </p>
      {/* </header> */}
    </div>
  );
}

export default App;
