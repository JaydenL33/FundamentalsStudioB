import React, { Component } from 'react';
import "animate.css/animate.min.css";
import ScrollAnimation from 'react-animate-on-scroll';

import './display.css'

class Display extends Component {
    render () {
        return (
            <ScrollAnimation animateIn={this.props.animation} initiallyVisible="false" offset="700" 
            delay="1" animatePreScroll="false" animateOnce="false" animateOut="fadeOut"
            duration="2.5">
            <section className="display-wrapper">
                <div className="media-wrapper">
                    <img src={this.props.img} alt="Just a sample img"/>
                </div>
                <div className="content-wrapper">
                    <div>
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
            </ScrollAnimation>
        )
    }
}

  // Set default props
Display.defaultProps = {
    animation: "fadeInDown",
    animateOnce: "false"
}

export default Display;