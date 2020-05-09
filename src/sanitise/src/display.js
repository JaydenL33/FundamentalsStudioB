import React, { Component } from 'react';

class Display extends Component {
    render () {
        return (
        <div className="content-wrapper">
        {/* <div> <img src={this.props.img} alt="This is a Sample Alt" /></div> */}
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
        )
    }
}

export default Display;