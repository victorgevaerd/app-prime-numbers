/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react';
import {AiOutlineGithub, AiOutlineLinkedin} from 'react-icons/ai';

import './styles.css';

const NavBar = () => {

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
      <a className="navbar-brand nav-title">
        Laboratório Bridge - Processo Seletivo: Desafio Dev Web Full Stack
      </a>
      <div className="row nav-author">
        <a className="navbar-brand">Victor Gevaerd Luiz</a>
        <a href="https://github.com/victorgevaerd">
          <AiOutlineGithub color="#fff" size={40}/>
        </a>
        <a href="https://br.linkedin.com/in/victorgevaerd">
          <AiOutlineLinkedin color="#fff" size={40}/>
        </a>
      </div>
    </nav>
  )
};

export default NavBar;
