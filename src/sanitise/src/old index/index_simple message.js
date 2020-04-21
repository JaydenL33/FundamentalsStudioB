import React from 'react';
import ReactDOM from 'react-dom';
import * as apis from './APILoader.js';

var sampledata = apis.objectLoader("http://134.122.104.123:5000/test");


class Header extends React.Component {
	render() {
		return (
			<header className="App-Header">
				<img src={logo} className="App-Logo" alt="logo"/>
				<h1 className = "App-title"> Welcome to React </h1>
				</header>
		);
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
		<Message color="Blue" msg="how are you?" minutes={sampledata.date} />,
	document.getElementById('root')
)


