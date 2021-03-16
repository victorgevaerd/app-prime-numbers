import React from 'react'

const Card = ({title, children}) => {
  return (
    <div className="card border-secondary mb3" style={{marginBottom: '20px'}}>
      <div className="card-header">
        {title} 
      </div>
      <div className="card-body">
        {children}
      </div>
    </div>
  )
}

export default Card
