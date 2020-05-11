import React, { Component } from 'react';
import ScrollOut from "scroll-out";

import "./display.css"


ScrollOut({
    
});

class Display extends Component {
    render () {
        return (
            <section className="display-wrapper">
                <script>
                    ScrollOut();
                </script>
                <div className="media-wrapper">
                    <img src={this.props.img} alt="Just a sample img"/>
                </div>
                <div className="content-wrapper">
                    <div C>
                        <h1>{this.props.title}</h1> 
                            <h2>{this.props.title2}</h2> 
                            <div className="paragraph1"> 
                                <p>{this.props.paragraph1}</p> 
                            </div>
                            <div className="paragraph2"> 
                                <p>{this.props.paragraph2}</p> 
                            </div>
                            <div className="paragraph3"> 
                                <p>{this.props.paragraph3}</p> 
                            </div>
                    </div>
                </div>
            </section>
        )
    }
}



export default Display;