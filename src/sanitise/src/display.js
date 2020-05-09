import React, { Component } from 'react';

class Display extends Component {
    render () {
        return (
        <div className = "sampleDisplay">
        <div> <img src={this.props.img} alt="This is a Sample Alt" /></div>
        <div className = "paragraph1"> <p>{this.props.paragraph1}</p> </div>
        <div className = "paragraph2"> <p>{this.props.paragraph2}</p> </div>
        <div className = "paragraph3 "></div><div> <p>{this.props.paragraph3}</p> </div>
        </div>
        )
    }
}

export default Display;