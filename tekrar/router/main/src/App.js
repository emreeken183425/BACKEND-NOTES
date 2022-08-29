
import './App.css';
import Navbar from './components/Navbar';
import Home from './pages/Home.jsx'
import Blog from './pages/Blog.jsx'
import Contact from './pages/Contact.jsx'
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
    <BrowserRouter>
    <Navbar/>
     <Routes>
      <Route path='/' element={<Home />} />
      <Route path='blog' element={<Blog />} />
      <Route path='contact' element={<Contact />} />
     </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
