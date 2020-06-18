import React, { Component } from 'react';
import "animate.css/animate.min.css";
import ScrollAnimation from 'react-animate-on-scroll';

import './display.css'
import BarChart from './BarChart';

class Display extends Component {
    render () {
        return (
            <ScrollAnimation animateIn={this.props.animation} initiallyVisible={false} offset={200}
            delay={20} animatePreScroll={true} animateOnce={true} animateOut="fadeOut"
            duration={2} className="animated-FadeIn">
            <section className="display-wrapper">
                <div className="media-wrapper">
                    <BarChart> </BarChart>
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
    animation: "fadeIn",
    animateOnce: "false"
}

export default Display;