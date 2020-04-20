import React from 'react';
import ReactDOM from 'react-dom';
import * as apis from './APILoader.js';


class SkiDayCounter extends React.Component 
{
	render() 
	{ 
		return(
		<section>
			Ski Days
			</section>
		)
	}
}

class Message extends React.Component {
	render() {
		return (
				<div>
					<h1 style={{color: this.props.color}}>
						{this.props.msg}	
						</h1>
					<p> I'll check back in {this.props.minutes} minutes</p>
				</div>
		)
	}
}



ReactDOM.render(
		<Message color="Blue" msg="how are you?" minutes="10" />,
	document.getElementById('root')
)


