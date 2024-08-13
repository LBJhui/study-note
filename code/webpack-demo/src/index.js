import Header from './components/header.js';
import Sidebar from './components/sidebar.js';
import Content from './components/content.js';

const dom = document.getElementById('root');

// header
new Header(dom);
// side-bar
new Sidebar(dom);
// content
new Content(dom);
