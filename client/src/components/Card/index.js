import React from 'react';
import {AiOutlineCloseCircle} from 'react-icons/ai';

const Card = ({title, children, onClick, isVisible=true}) => {
  return (
    <div className="card border-secondary mb3" style={{marginBottom: '20px'}}>
      <div className="card-header row">
        {title}
        {
          isVisible ?
            <a className="closeButton" onClick={onClick}>
              <AiOutlineCloseCircle color="red" size={25}/>
            </a>
          :
          <div/>
        }
      </div>
      <div className="card-body">
        {children}
      </div>
    </div>
  )
}

export default Card
