import React from 'react';

export const Card = (props) => (

    <div style = {{
        /*width:'50%',*/
     /*   margin: '200px auto 30px auto',*/
        boxShadow: '0 5px 10px 2px rgba(0,0,0, 0.5)',
        padding: '20px',
  
       

    }}>
        {props.children}
    </div>
)